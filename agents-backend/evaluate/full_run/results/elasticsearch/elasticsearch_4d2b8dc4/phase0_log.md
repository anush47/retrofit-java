# Phase 0 Inputs

- Mainline commit: 4d2b8dc4f2e908821dfb34d4ffc14244fce83c41
- Backport commit: 8421006641a2d8e617636d0a10bbe63e60648420
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 3

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java']
- Developer Java files: ['x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java']
- Overlap Java files: ['x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 4d2b8dc4f2e908821dfb34d4ffc14244fce83c41 Mon Sep 17 00:00:00 2001
From: Nhat Nguyen <nhat.nguyen@elastic.co>
Date: Mon, 24 Feb 2025 08:49:54 -0800
Subject: [PATCH] Fix early termination in LuceneSourceOperator (#123197)

The LuceneSourceOperator is supposed to terminate when it reaches the
limit; unfortunately, we don't have a test to cover this. Due to this
bug, we continue scanning all segments, even though we discard the
results as the limit was reached. This can cause performance issues for
simple queries like FROM .. | LIMIT 10, when Lucene indices are on the
warm or cold tier. I will submit a follow-up PR to ensure we only
collect up to the limit across multiple drivers.
---
 docs/changelog/123197.yaml                    |  5 +++++
 .../compute/lucene/LuceneSourceOperator.java  |  2 +-
 .../lucene/LuceneSourceOperatorTests.java     | 22 +++++++++++++++++++
 3 files changed, 28 insertions(+), 1 deletion(-)
 create mode 100644 docs/changelog/123197.yaml

diff --git a/docs/changelog/123197.yaml b/docs/changelog/123197.yaml
new file mode 100644
index 00000000000..ffb4bab79fe
--- /dev/null
+++ b/docs/changelog/123197.yaml
@@ -0,0 +1,5 @@
+pr: 123197
+summary: Fix early termination in `LuceneSourceOperator`
+area: ES|QL
+type: bug
+issues: []
diff --git a/x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java b/x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java
index 3d34067e1a8..61a7cbad3e8 100644
--- a/x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java
+++ b/x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java
@@ -140,7 +140,7 @@ public class LuceneSourceOperator extends LuceneOperator {
 
     @Override
     public boolean isFinished() {
-        return doneCollecting;
+        return doneCollecting || remainingDocs <= 0;
     }
 
     @Override
diff --git a/x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/lucene/LuceneSourceOperatorTests.java b/x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/lucene/LuceneSourceOperatorTests.java
index 574f9b25ff1..42c9f49a2db 100644
--- a/x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/lucene/LuceneSourceOperatorTests.java
+++ b/x-pack/plugin/esql/compute/src/test/java/org/elasticsearch/compute/lucene/LuceneSourceOperatorTests.java
@@ -25,6 +25,7 @@ import org.elasticsearch.compute.data.Page;
 import org.elasticsearch.compute.operator.Driver;
 import org.elasticsearch.compute.operator.DriverContext;
 import org.elasticsearch.compute.operator.Operator;
+import org.elasticsearch.compute.operator.SourceOperator;
 import org.elasticsearch.compute.test.AnyOperatorTestCase;
 import org.elasticsearch.compute.test.OperatorTestCase;
 import org.elasticsearch.compute.test.TestResultPageSinkOperator;
@@ -117,6 +118,27 @@ public class LuceneSourceOperatorTests extends AnyOperatorTestCase {
         testSimple(driverContext(), size, limit);
     }
 
+    public void testEarlyTermination() {
+        int size = between(1_000, 20_000);
+        int limit = between(10, size);
+        LuceneSourceOperator.Factory factory = simple(randomFrom(DataPartitioning.values()), size, limit, scoring);
+        try (SourceOperator sourceOperator = factory.get(driverContext())) {
+            assertFalse(sourceOperator.isFinished());
+            int collected = 0;
+            while (sourceOperator.isFinished() == false) {
+                Page page = sourceOperator.getOutput();
+                if (page != null) {
+                    collected += page.getPositionCount();
+                    page.releaseBlocks();
+                }
+                if (collected >= limit) {
+                    assertTrue("source operator is not finished after reaching limit", sourceOperator.isFinished());
+                    assertThat(collected, equalTo(limit));
+                }
+            }
+        }
+    }
+
     public void testEmpty() {
         testSimple(driverContext(), 0, between(10, 10_000));
     }
-- 
2.43.0


```
