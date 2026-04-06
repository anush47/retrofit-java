# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java']
- Developer Java files: ['x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java']
- Overlap Java files: ['x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java']

## File State Comparison
- Compared files: ['x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java']
- Mismatched files: ['x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -58,7 +58,7 @@
         int maxEnd = Math.min(maxStart + extent, values.length);
         double maxSum = sum(values, maxStart, maxEnd, negate);
         for (int start = maxStart + 1; start <= argmax; start++) {
-            if (start + extent >= values.length) {
+            if (start + extent > values.length) {
                 break;
             }
             double average = sum(values, start, start + extent, negate);

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -58,7 +58,7 @@
-         int maxEnd = Math.min(maxStart + extent, values.length);
-         double maxSum = sum(values, maxStart, maxEnd, negate);
-         for (int start = maxStart + 1; start <= argmax; start++) {
--            if (start + extent >= values.length) {
-+            if (start + extent > values.length) {
-                 break;
-             }
-             double average = sum(values, start, start + extent, negate);
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
diff --git a/docs/changelog/119637.yaml b/docs/changelog/119637.yaml
new file mode 100644
index 00000000000..c2fd6dc51f0
--- /dev/null
+++ b/docs/changelog/119637.yaml
@@ -0,0 +1,5 @@
+pr: 119637
+summary: Fix spike detection for short spikes at the tail of the data
+area: Machine Learning
+type: bug
+issues: []
diff --git a/x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java b/x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java
index 365ebe8562d..fa632f643ff 100644
--- a/x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java
+++ b/x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetector.java
@@ -58,7 +58,7 @@ final class SpikeAndDipDetector {
         int maxEnd = Math.min(maxStart + extent, values.length);
         double maxSum = sum(values, maxStart, maxEnd, negate);
         for (int start = maxStart + 1; start <= argmax; start++) {
-            if (start + extent >= values.length) {
+            if (start + extent > values.length) {
                 break;
             }
             double average = sum(values, start, start + extent, negate);
diff --git a/x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetectorTests.java b/x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetectorTests.java
index b21a7c4625e..c80cfffbd73 100644
--- a/x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetectorTests.java
+++ b/x-pack/plugin/ml/src/test/java/org/elasticsearch/xpack/ml/aggs/changepoint/SpikeAndDipDetectorTests.java
@@ -184,4 +184,14 @@ public class SpikeAndDipDetectorTests extends ESTestCase {
         assertThat(change, instanceOf(ChangeType.Spike.class));
         assertThat(change.changePoint(), equalTo(10));
     }
+
+    public void testSpikeAtTail() {
+        MlAggsHelper.DoubleBucketValues bucketValues = new MlAggsHelper.DoubleBucketValues(
+            null,
+            new double[] { 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 9, 8 }
+        );
+        ChangeType change = new SpikeAndDipDetector(bucketValues).detect(0.01);
+        assertThat(change, instanceOf(ChangeType.Spike.class));
+        assertThat(change.changePoint(), equalTo(27));
+    }
 }

```
