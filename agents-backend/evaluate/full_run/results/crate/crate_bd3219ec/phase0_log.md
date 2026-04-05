# Phase 0 Inputs

- Mainline commit: bd3219ec49ccabf5a70191a20fba2cadd07ed6ac
- Backport commit: 0df5dbcccfe8357ef9d86d38fcee3f24ca409f65
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 4

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/rest/action/RestResultSetReceiver.java']
- Developer Java files: ['server/src/main/java/io/crate/rest/action/RestResultSetReceiver.java']
- Overlap Java files: ['server/src/main/java/io/crate/rest/action/RestResultSetReceiver.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From bd3219ec49ccabf5a70191a20fba2cadd07ed6ac Mon Sep 17 00:00:00 2001
From: baur <baurzhansahariev@gmail.com>
Date: Fri, 13 Jun 2025 11:28:24 +0200
Subject: [PATCH] Ensure that RestResultSetReceiver.setNext throws an error

Callers must handle thrown exceptions.

Fixes a regression introduced in 9b61be3
---
 docs/appendices/release-notes/5.10.9.rst            |  4 ++++
 .../io/crate/rest/action/RestResultSetReceiver.java |  6 +++---
 .../crate/rest/action/RestActionReceiversTest.java  | 13 ++++++++-----
 3 files changed, 15 insertions(+), 8 deletions(-)

diff --git a/docs/appendices/release-notes/5.10.9.rst b/docs/appendices/release-notes/5.10.9.rst
index 21299125d7..b954164dd5 100644
--- a/docs/appendices/release-notes/5.10.9.rst
+++ b/docs/appendices/release-notes/5.10.9.rst
@@ -62,3 +62,7 @@ Fixes
 - Fixed an issue that would cause :ref:`aggregation functions <aggregation>` on
   columns used in the ``PARTITION BY()`` clause of a
   :ref:`partitioned table <partitioned-tables>` to always return ``NULL``.
+
+- Fixed a regression introduced with :ref:`version_5.10.8` that caused a query
+  to keep running even if a ``CircuitBreakerException`` was thrown while
+  constructing the result set.
diff --git a/server/src/main/java/io/crate/rest/action/RestResultSetReceiver.java b/server/src/main/java/io/crate/rest/action/RestResultSetReceiver.java
index 0ab51943d1..11b3ef72c5 100644
--- a/server/src/main/java/io/crate/rest/action/RestResultSetReceiver.java
+++ b/server/src/main/java/io/crate/rest/action/RestResultSetReceiver.java
@@ -22,6 +22,7 @@
 package io.crate.rest.action;
 
 import java.io.IOException;
+import java.io.UncheckedIOException;
 import java.util.List;
 import java.util.concurrent.CompletableFuture;
 
@@ -68,9 +69,8 @@ class RestResultSetReceiver implements ResultReceiver<XContentBuilder> {
             builder.addRow(row, outputFields.size());
             rowCount++;
             return null;
-        } catch (Exception e) {
-            fail(e);
-            return null;
+        } catch (IOException e) {
+            throw new UncheckedIOException(e);
         }
     }
 
diff --git a/server/src/test/java/io/crate/rest/action/RestActionReceiversTest.java b/server/src/test/java/io/crate/rest/action/RestActionReceiversTest.java
index b1d6cadb9b..a7f04645dd 100644
--- a/server/src/test/java/io/crate/rest/action/RestActionReceiversTest.java
+++ b/server/src/test/java/io/crate/rest/action/RestActionReceiversTest.java
@@ -23,12 +23,14 @@ package io.crate.rest.action;
 
 import static io.crate.data.breaker.BlockBasedRamAccounting.MAX_BLOCK_SIZE_IN_BYTES;
 import static org.assertj.core.api.Assertions.assertThat;
+import static org.assertj.core.api.Assertions.assertThatThrownBy;
 
 import java.io.IOException;
 import java.util.Collections;
 import java.util.List;
 
 import org.elasticsearch.common.Strings;
+import org.elasticsearch.common.breaker.CircuitBreakingException;
 import org.elasticsearch.common.breaker.TestCircuitBreaker;
 import org.elasticsearch.common.xcontent.XContentBuilder;
 import org.elasticsearch.common.xcontent.json.JsonXContent;
@@ -152,7 +154,7 @@ public class RestActionReceiversTest extends ESTestCase {
     }
 
     @Test
-    public void test_result_reciever_future_completed_on_cbe() throws Exception {
+    public void test_result_reciever_future_is_not_completed_on_cbe() throws Exception {
         TestCircuitBreaker breaker = new TestCircuitBreaker();
         breaker.startBreaking();
         RamAccounting ramAccounting = new BlockBasedRamAccounting(
@@ -171,9 +173,10 @@ public class RestActionReceiversTest extends ESTestCase {
             false
         );
 
-        // Fails with CBE, resultReceiver's future must be completed, so that sys.jobs entry is cleared.
-        resultReceiver.setNextRow(rows.get(0));
-        assertThat(resultReceiver.completionFuture().isDone()).isTrue();
-        assertThat(resultReceiver.completionFuture().isCompletedExceptionally()).isTrue();
+        // Fails with CBE, resultReceiver's future must not be completed,
+        // it's handled by the consumer/response emitter which also closes iterator/clears sys.jobs entry
+        assertThatThrownBy(() -> resultReceiver.setNextRow(rows.get(0)))
+            .isExactlyInstanceOf(CircuitBreakingException.class);
+        assertThat(resultReceiver.completionFuture().isDone()).isFalse();
     }
 }
-- 
2.43.0


```
