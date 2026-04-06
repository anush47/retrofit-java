# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java']
- Developer Java files: ['server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java']
- Overlap Java files: ['server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java']
- Mismatched files: ['server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/execution/engine/collect/files/FileReadingIterator.java

- Developer hunks: 5
- Generated hunks: 0

#### Hunk 1

Developer
```diff
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

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,15 +1 @@-@@ -21,12 +21,14 @@
- 
- package io.crate.execution.engine.collect.files;
- 
-+import static io.crate.analyze.CopyStatementSettings.FAIL_FAST_SETTING;
- import static io.crate.common.exceptions.Exceptions.rethrowUnchecked;
- 
- import java.io.BufferedReader;
- import java.io.IOException;
- import java.io.InputStream;
- import java.io.InputStreamReader;
-+import java.io.UncheckedIOException;
- import java.net.SocketException;
- import java.net.SocketTimeoutException;
- import java.net.URI;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -91,6 +93,7 @@
     private final int numReaders;
     private final int readerNumber;
     private final boolean compressed;
+    private final boolean failFast;
     private final List<FileInput> fileInputs;
 
     private volatile Throwable killed;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -91,6 +93,7 @@
-     private final int numReaders;
-     private final int readerNumber;
-     private final boolean compressed;
-+    private final boolean failFast;
-     private final List<FileInput> fileInputs;
- 
-     private volatile Throwable killed;
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -187,6 +190,7 @@
         this.fileInputFactories = fileInputFactories;
         this.cursor = new LineCursor();
         this.shared = shared;
+        this.failFast = FAIL_FAST_SETTING.get(withClauseOptions);
         this.numReaders = numReaders;
         this.readerNumber = readerNumber;
         this.scheduler = scheduler;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -187,6 +190,7 @@
-         this.fileInputFactories = fileInputFactories;
-         this.cursor = new LineCursor();
-         this.shared = shared;
-+        this.failFast = FAIL_FAST_SETTING.get(withClauseOptions);
-         this.numReaders = numReaders;
-         this.readerNumber = readerNumber;
-         this.scheduler = scheduler;
+*No hunk*
```

#### Hunk 4

Developer
```diff
@@ -256,6 +260,11 @@
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

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,12 +1 @@-@@ -256,6 +260,11 @@
-         } catch (IOException e) {
-             cursor.failure = e;
-             closeReader();
-+            if (failFast) {
-+                // Treat IO error as a data error on fail_fast and stop consuming other URI-s.
-+                // Bubble up to exception to the BatchIteratorBackpressureExecutor
-+                throw new UncheckedIOException(e);
-+            }
-             // If IOError happens on file opening, let consumers collect the error
-             // This is mostly for RETURN SUMMARY of COPY FROM
-             if (cursor.lineNumber == 0) {
+*No hunk*
```

#### Hunk 5

Developer
```diff
@@ -310,7 +319,8 @@
         currentReader = createBufferedReader(stream);
     }
 
-    private void closeReader() {
+    @VisibleForTesting
+    void closeReader() {
         if (currentReader != null) {
             try {
                 currentReader.close();

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -310,7 +319,8 @@
-         currentReader = createBufferedReader(stream);
-     }
- 
--    private void closeReader() {
-+    @VisibleForTesting
-+    void closeReader() {
-         if (currentReader != null) {
-             try {
-                 currentReader.close();
+*No hunk*
```



## Full Generated Patch (Agent-Only, code-only)
```diff

```

## Full Generated Patch (Final Effective, code-only)
```diff

```
## Full Developer Backport Patch (full commit diff)
```diff
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
index c59cffe281..b6998f34c5 100644
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
@@ -187,6 +190,7 @@ public class FileReadingIterator implements BatchIterator<FileReadingIterator.Li
         this.fileInputFactories = fileInputFactories;
         this.cursor = new LineCursor();
         this.shared = shared;
+        this.failFast = FAIL_FAST_SETTING.get(withClauseOptions);
         this.numReaders = numReaders;
         this.readerNumber = readerNumber;
         this.scheduler = scheduler;
@@ -256,6 +260,11 @@ public class FileReadingIterator implements BatchIterator<FileReadingIterator.Li
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
@@ -310,7 +319,8 @@ public class FileReadingIterator implements BatchIterator<FileReadingIterator.Li
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

```
