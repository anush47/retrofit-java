# Phase 0 Inputs

- Mainline commit: 6b0c28a33d560ec4ebf11a8b1ed169e67953dfb8
- Backport commit: c1644ebe26ff063017b88db616e2ebca0004e745
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 3

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java']
- Developer Java files: ['server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java']
- Overlap Java files: ['server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 6b0c28a33d560ec4ebf11a8b1ed169e67953dfb8 Mon Sep 17 00:00:00 2001
From: baur <baurzhansahariev@gmail.com>
Date: Wed, 23 Apr 2025 17:57:36 +0200
Subject: [PATCH] Apply fail_fast on non-retryable IO errors

---
 docs/appendices/release-notes/5.10.5.rst      |  4 ++
 .../collect/files/FileReadingIterator.java    | 12 ++++-
 .../files/FileReadingIteratorTest.java        | 52 +++++++++++++++++++
 3 files changed, 67 insertions(+), 1 deletion(-)

diff --git a/docs/appendices/release-notes/5.10.5.rst b/docs/appendices/release-notes/5.10.5.rst
index 9709927ffc..57275e1046 100644
--- a/docs/appendices/release-notes/5.10.5.rst
+++ b/docs/appendices/release-notes/5.10.5.rst
@@ -71,3 +71,7 @@ Fixes
     
   now returns ``TRUE`` because ``''`` is padded with ``' '`` which is ``32`` in
   ``ASCII`` and ``e'\n'`` is ``10`` in ``ASCII``.
+
+- Fixed behavior of ``COPY ... FROM ... with (fail_fast = true)`` to stop on
+  non-retryable IO errors as well. Before the flag used to be applied only for
+  write errors.
diff --git a/server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java b/server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java
index 321402d78a..4aff791a24 100644
--- a/server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java
+++ b/server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java
@@ -21,12 +21,14 @@
 
 package io.crate.execution.engine.collect.files;
 
+import static io.crate.analyze.CopyStatementSettings.FAIL_FAST_SETTING;
 import static io.crate.common.exceptions.Exceptions.rethrowUnchecked;
 
 import java.io.BufferedReader;
 import java.io.IOException;
 import java.io.InputStream;
 import java.io.InputStreamReader;
+import java.io.UncheckedIOException;
 import java.net.SocketException;
 import java.net.SocketTimeoutException;
 import java.net.URI;
@@ -91,6 +93,7 @@ public class FileReadingIterator implements BatchIterator<FileReadingIterator.Li
     private final int numReaders;
     private final int readerNumber;
     private final boolean compressed;
+    private final boolean failFast;
     private final List<FileInput> fileInputs;
 
     private volatile Throwable killed;
@@ -188,6 +191,7 @@ public class FileReadingIterator implements BatchIterator<FileReadingIterator.Li
         this.fileInputFactories = fileInputFactories;
         this.cursor = new LineCursor();
         this.shared = shared;
+        this.failFast = FAIL_FAST_SETTING.get(withClauseOptions);
         this.numReaders = numReaders;
         this.readerNumber = readerNumber;
         this.scheduler = scheduler;
@@ -257,6 +261,11 @@ public class FileReadingIterator implements BatchIterator<FileReadingIterator.Li
         } catch (IOException e) {
             cursor.failure = e;
             closeReader();
+            if (failFast) {
+                // Treat IO error as a data error on fail_fast and stop consuming other URI-s.
+                // Bubble up to exception to the BatchIteratorBackpressureExecutor
+                throw new UncheckedIOException(e);
+            }
             // If IOError happens on file opening, let consumers collect the error
             // This is mostly for RETURN SUMMARY of COPY FROM
             if (cursor.lineNumber == 0) {
@@ -311,7 +320,8 @@ public class FileReadingIterator implements BatchIterator<FileReadingIterator.Li
         currentReader = createBufferedReader(stream);
     }
 
-    private void closeReader() {
+    @VisibleForTesting
+    void closeReader() {
         if (currentReader != null) {
             try {
                 currentReader.close();
diff --git a/server/src/test/java/io/crate/execution/engine/collect/files/FileReadingIteratorTest.java b/server/src/test/java/io/crate/execution/engine/collect/files/FileReadingIteratorTest.java
index 8171065529..c47e513ba4 100644
--- a/server/src/test/java/io/crate/execution/engine/collect/files/FileReadingIteratorTest.java
+++ b/server/src/test/java/io/crate/execution/engine/collect/files/FileReadingIteratorTest.java
@@ -26,13 +26,16 @@ import static org.assertj.core.api.Assertions.assertThatThrownBy;
 import static org.mockito.ArgumentMatchers.any;
 import static org.mockito.ArgumentMatchers.eq;
 import static org.mockito.Mockito.mock;
+import static org.mockito.Mockito.spy;
 import static org.mockito.Mockito.times;
 import static org.mockito.Mockito.verify;
 
 import java.io.BufferedReader;
+import java.io.EOFException;
 import java.io.IOException;
 import java.io.InputStream;
 import java.io.InputStreamReader;
+import java.io.UncheckedIOException;
 import java.net.SocketTimeoutException;
 import java.net.URI;
 import java.nio.charset.StandardCharsets;
@@ -185,6 +188,55 @@ public class FileReadingIteratorTest extends ESTestCase {
         tester.verifyResultAndEdgeCaseBehaviour(lines);
     }
 
+    @Test
+    public void test_iterator_closes_current_reader_and_throws_exception_on_fail_fast() throws Exception {
+        Path tempFile = createTempFile("tempfile1", ".csv");
+        List<String> lines = List.of("1", "2");
+        Files.write(tempFile, lines);
+        List<URI> fileUris = Stream.of(tempFile.toUri().toString())
+            .map(FileReadingIterator::toURI).toList();
+
+        var fi = spy(new FileReadingIterator(
+            fileUris,
+            null,
+            Map.of(LocalFsFileInputFactory.NAME, new LocalFsFileInputFactory()),
+            false,
+            1,
+            0,
+            Settings.builder().put("fail_fast", true).build(),
+            THREAD_POOL.scheduler()
+        ) {
+
+            @Override
+            BufferedReader createBufferedReader(InputStream inputStream) throws IOException {
+                return new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8)) {
+
+                    private int currentLineNumber = 0;
+
+                    @Override
+                    public String readLine() throws IOException {
+                        var line = super.readLine();
+                        currentLineNumber++;
+                        if (currentLineNumber > 1) {
+                            throw new EOFException("dummy");
+                        }
+                        return line;
+                    }
+                };
+            }
+        });
+
+
+        assertThat(fi.moveNext()).isTrue();
+        assertThat(fi.currentElement().line()).isEqualTo("1");
+        verify(fi, times(0)).closeReader();
+
+        assertThatThrownBy(() -> fi.moveNext())
+            .isExactlyInstanceOf(UncheckedIOException.class)
+            .hasMessageContaining("dummy");
+        verify(fi, times(1)).closeReader();
+    }
+
     @Test
     public void test_loadNextBatch_implements_retry_with_backoff() throws IOException {
         ScheduledExecutorService scheduler = mock(ScheduledExecutorService.class);
-- 
2.43.0


```
