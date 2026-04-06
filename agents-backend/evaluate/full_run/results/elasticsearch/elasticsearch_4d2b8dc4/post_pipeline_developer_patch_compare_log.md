# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java']
- Developer Java files: ['x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java']
- Overlap Java files: ['x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java']

## File State Comparison
- Compared files: ['x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java']
- Mismatched files: ['x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### x-pack/plugin/esql/compute/src/main/java/org/elasticsearch/compute/lucene/LuceneSourceOperator.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -140,7 +140,7 @@
 
     @Override
     public boolean isFinished() {
-        return doneCollecting;
+        return doneCollecting || remainingDocs <= 0;
     }
 
     @Override

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -140,7 +140,7 @@
- 
-     @Override
-     public boolean isFinished() {
--        return doneCollecting;
-+        return doneCollecting || remainingDocs <= 0;
-     }
- 
-     @Override
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
index b7114bb4e9b..cba8722a384 100644
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

```
