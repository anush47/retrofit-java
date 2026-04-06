# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java']
- Developer Java files: ['server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java']
- Overlap Java files: ['server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java']
- Mismatched files: ['server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -848,11 +848,15 @@
             if (node.getEscape() != null) {
                 throw new UnsupportedOperationException("ESCAPE is not supported.");
             }
-            Symbol arraySymbol = node.getValue().accept(this, context);
-            Symbol leftSymbol = node.getPattern().accept(this, context);
+            Symbol value = node.getValue().accept(this, context);
+            Symbol pattern = node.getPattern().accept(this, context);
+            int valueDimensions = ArrayType.dimensions(value.valueType());
+            int patternDimensions = ArrayType.dimensions(pattern.valueType());
+            int diff = valueDimensions - patternDimensions;
+            value = ArrayUnnestFunction.unnest(value, diff - 1);
             return allocateFunction(
                 LikeOperators.arrayOperatorName(node.quantifier(), node.inverse(), node.ignoreCase()),
-                List.of(leftSymbol, arraySymbol),
+                List.of(pattern, value),
                 context);
         }
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,19 +1 @@-@@ -848,11 +848,15 @@
-             if (node.getEscape() != null) {
-                 throw new UnsupportedOperationException("ESCAPE is not supported.");
-             }
--            Symbol arraySymbol = node.getValue().accept(this, context);
--            Symbol leftSymbol = node.getPattern().accept(this, context);
-+            Symbol value = node.getValue().accept(this, context);
-+            Symbol pattern = node.getPattern().accept(this, context);
-+            int valueDimensions = ArrayType.dimensions(value.valueType());
-+            int patternDimensions = ArrayType.dimensions(pattern.valueType());
-+            int diff = valueDimensions - patternDimensions;
-+            value = ArrayUnnestFunction.unnest(value, diff - 1);
-             return allocateFunction(
-                 LikeOperators.arrayOperatorName(node.quantifier(), node.inverse(), node.ignoreCase()),
--                List.of(leftSymbol, arraySymbol),
-+                List.of(pattern, value),
-                 context);
-         }
- 
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
diff --git a/docs/appendices/release-notes/5.10.6.rst b/docs/appendices/release-notes/5.10.6.rst
index 00e7beca35..12ab18afcc 100644
--- a/docs/appendices/release-notes/5.10.6.rst
+++ b/docs/appendices/release-notes/5.10.6.rst
@@ -48,6 +48,10 @@ See the :ref:`version_5.10.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- ``LIKE ANY`` now behaves the same as any other operators used with ``ANY`` and
+  automatically levels the dimensions by wrapping the right side in an
+  ``array_unnest`` as necessary - as documented.
+
 - Fixed a bug where references to a column initially created in versions of CrateDB
   before 5.5 would return ``NULL`` instead of their actual value when the column was
   addressed via ``doc['column']``
diff --git a/server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java b/server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java
index 3db5401f8d..6aae1b5195 100644
--- a/server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java
@@ -848,11 +848,15 @@ public class ExpressionAnalyzer {
             if (node.getEscape() != null) {
                 throw new UnsupportedOperationException("ESCAPE is not supported.");
             }
-            Symbol arraySymbol = node.getValue().accept(this, context);
-            Symbol leftSymbol = node.getPattern().accept(this, context);
+            Symbol value = node.getValue().accept(this, context);
+            Symbol pattern = node.getPattern().accept(this, context);
+            int valueDimensions = ArrayType.dimensions(value.valueType());
+            int patternDimensions = ArrayType.dimensions(pattern.valueType());
+            int diff = valueDimensions - patternDimensions;
+            value = ArrayUnnestFunction.unnest(value, diff - 1);
             return allocateFunction(
                 LikeOperators.arrayOperatorName(node.quantifier(), node.inverse(), node.ignoreCase()),
-                List.of(leftSymbol, arraySymbol),
+                List.of(pattern, value),
                 context);
         }
 
diff --git a/server/src/test/java/io/crate/analyze/expressions/ExpressionAnalyzerTest.java b/server/src/test/java/io/crate/analyze/expressions/ExpressionAnalyzerTest.java
index 0449a9123b..0af5d02cd0 100644
--- a/server/src/test/java/io/crate/analyze/expressions/ExpressionAnalyzerTest.java
+++ b/server/src/test/java/io/crate/analyze/expressions/ExpressionAnalyzerTest.java
@@ -521,6 +521,8 @@ public class ExpressionAnalyzerTest extends CrateDummyClusterServiceUnitTest {
     public void test_any_automatically_levels_array_dimensions() throws Exception {
         assertThat(executor.asSymbol("1 = ANY([1, 2])")).isLiteral(true);
         assertThat(executor.asSymbol("3 = ANY([1, 2])")).isLiteral(false);
+        assertThat(executor.asSymbol("'Hello' LIKE ANY(['Hell%', 'No'])")).isLiteral(true);
+        assertThat(executor.asSymbol("'Hello' LIKE ANY([['Hell', 'No'], ['Hell_']])")).isLiteral(true);
 
         assertThat(executor.asSymbol("[1, 2] = ANY([[3, 4], [1, 2]])")).isLiteral(true);
         assertThat(executor.asSymbol("[1, 3] = ANY([[3, 4], [1, 2]])")).isLiteral(false);
diff --git a/server/src/test/java/io/crate/lucene/CommonQueryBuilderTest.java b/server/src/test/java/io/crate/lucene/CommonQueryBuilderTest.java
index 6ef873a746..40875498d6 100644
--- a/server/src/test/java/io/crate/lucene/CommonQueryBuilderTest.java
+++ b/server/src/test/java/io/crate/lucene/CommonQueryBuilderTest.java
@@ -524,6 +524,12 @@ public class CommonQueryBuilderTest extends LuceneQueryBuilderTest {
             "+o_array.xs:{1 2} #([1, 2] = ANY(o_array['xs']))");
     }
 
+    @Test
+    public void test_like_any_on_nested_array() throws Exception {
+        assertThat(convert("'Hello' LIKE ANY(o_array['xs'])"))
+            .hasToString("('Hello' LIKE ANY(array_unnest(o_array['xs'])))");
+    }
+
     @Test
     public void testGtAnyOnNestedArrayIsNotSupported() {
         assertThatThrownBy(() -> convert("[1, 2] > any(o_array['xs'])"))

```
