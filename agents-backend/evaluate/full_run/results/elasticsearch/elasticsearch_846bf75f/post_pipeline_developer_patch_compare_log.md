# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java']
- Developer Java files: ['x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java']
- Overlap Java files: ['x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java']

## File State Comparison
- Compared files: ['x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java']
- Mismatched files: ['x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -294,9 +294,13 @@
          */
         String redactMatches(byte[] utf8Bytes, String redactStartToken, String redactEndToken) {
             var merged = mergeOverlappingReplacements(replacementPositions);
-            int longestPatternName = merged.stream().mapToInt(r -> r.patternName.getBytes(StandardCharsets.UTF_8).length).max().getAsInt();
+            int maxPatternNameLength = merged.stream()
+                .mapToInt(r -> r.patternName.getBytes(StandardCharsets.UTF_8).length)
+                .max()
+                .getAsInt();
 
-            int maxPossibleLength = longestPatternName * merged.size() + utf8Bytes.length;
+            int maxPossibleLength = (redactStartToken.length() + maxPatternNameLength + redactEndToken.length()) * merged.size()
+                + utf8Bytes.length;
             byte[] redact = new byte[maxPossibleLength];
 
             int readOffset = 0;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,16 +1 @@-@@ -294,9 +294,13 @@
-          */
-         String redactMatches(byte[] utf8Bytes, String redactStartToken, String redactEndToken) {
-             var merged = mergeOverlappingReplacements(replacementPositions);
--            int longestPatternName = merged.stream().mapToInt(r -> r.patternName.getBytes(StandardCharsets.UTF_8).length).max().getAsInt();
-+            int maxPatternNameLength = merged.stream()
-+                .mapToInt(r -> r.patternName.getBytes(StandardCharsets.UTF_8).length)
-+                .max()
-+                .getAsInt();
- 
--            int maxPossibleLength = longestPatternName * merged.size() + utf8Bytes.length;
-+            int maxPossibleLength = (redactStartToken.length() + maxPatternNameLength + redactEndToken.length()) * merged.size()
-+                + utf8Bytes.length;
-             byte[] redact = new byte[maxPossibleLength];
- 
-             int readOffset = 0;
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
diff --git a/docs/changelog/122640.yaml b/docs/changelog/122640.yaml
new file mode 100644
index 00000000000..f46fc55fc53
--- /dev/null
+++ b/docs/changelog/122640.yaml
@@ -0,0 +1,5 @@
+pr: 122640
+summary: Fix redact processor arraycopy bug
+area: Ingest Node
+type: bug
+issues: []
diff --git a/x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java b/x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java
index 187126fb31e..c378b822ce0 100644
--- a/x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java
+++ b/x-pack/plugin/redact/src/main/java/org/elasticsearch/xpack/redact/RedactProcessor.java
@@ -294,9 +294,13 @@ public class RedactProcessor extends AbstractProcessor {
          */
         String redactMatches(byte[] utf8Bytes, String redactStartToken, String redactEndToken) {
             var merged = mergeOverlappingReplacements(replacementPositions);
-            int longestPatternName = merged.stream().mapToInt(r -> r.patternName.getBytes(StandardCharsets.UTF_8).length).max().getAsInt();
+            int maxPatternNameLength = merged.stream()
+                .mapToInt(r -> r.patternName.getBytes(StandardCharsets.UTF_8).length)
+                .max()
+                .getAsInt();
 
-            int maxPossibleLength = longestPatternName * merged.size() + utf8Bytes.length;
+            int maxPossibleLength = (redactStartToken.length() + maxPatternNameLength + redactEndToken.length()) * merged.size()
+                + utf8Bytes.length;
             byte[] redact = new byte[maxPossibleLength];
 
             int readOffset = 0;
diff --git a/x-pack/plugin/redact/src/test/java/org/elasticsearch/xpack/redact/RedactProcessorTests.java b/x-pack/plugin/redact/src/test/java/org/elasticsearch/xpack/redact/RedactProcessorTests.java
index 76bf99d170a..bf287735d9f 100644
--- a/x-pack/plugin/redact/src/test/java/org/elasticsearch/xpack/redact/RedactProcessorTests.java
+++ b/x-pack/plugin/redact/src/test/java/org/elasticsearch/xpack/redact/RedactProcessorTests.java
@@ -108,6 +108,18 @@ public class RedactProcessorTests extends ESTestCase {
             var redacted = RedactProcessor.matchRedact(input, List.of(grok));
             assertEquals("<CREDIT_CARD> <CREDIT_CARD> <CREDIT_CARD> <CREDIT_CARD>", redacted);
         }
+        {
+            var config = new HashMap<String, Object>();
+            config.put("field", "to_redact");
+            config.put("patterns", List.of("%{NUMBER:NUMBER}"));
+            config.put("pattern_definitions", Map.of("NUMBER", "\\d{4}"));
+            var processor = new RedactProcessor.Factory(mockLicenseState(), MatcherWatchdog.noop()).create(null, "t", "d", config);
+            var grok = processor.getGroks().get(0);
+
+            String input = "1001";
+            var redacted = RedactProcessor.matchRedact(input, List.of(grok), "_prefix_", "_suffix_");
+            assertEquals("_prefix_NUMBER_suffix_", redacted);
+        }
     }
 
     public void testMatchRedactMultipleGroks() throws Exception {

```
