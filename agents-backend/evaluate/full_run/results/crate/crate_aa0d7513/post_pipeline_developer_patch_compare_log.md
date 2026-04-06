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
@@ -1264,6 +1264,9 @@
                             functionName));
                     }
                 }
+            } else if (filter != null) {
+                throw new UnsupportedOperationException(
+                    "FILTER is not implemented for non-aggregate window functions (" + functionName + ")");
             }
             newFunction = new WindowFunction(
                 signature,

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -1264,6 +1264,9 @@
-                             functionName));
-                     }
-                 }
-+            } else if (filter != null) {
-+                throw new UnsupportedOperationException(
-+                    "FILTER is not implemented for non-aggregate window functions (" + functionName + ")");
-             }
-             newFunction = new WindowFunction(
-                 signature,
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
diff --git a/docs/appendices/release-notes/5.9.7.rst b/docs/appendices/release-notes/5.9.7.rst
index c7aaed714b..de3d645921 100644
--- a/docs/appendices/release-notes/5.9.7.rst
+++ b/docs/appendices/release-notes/5.9.7.rst
@@ -47,6 +47,9 @@ See the :ref:`version_5.9.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- Fixed an issue that caused ``FILTER`` clauses on non-aggregate window
+  functions to be ignored instead of raising an unsupported error.
+
 - Fixed an issue leading to an error when exporting big tables via ``COPY TO``
   to the :ref:`Azure Blob Storage <sql-copy-to-az>`.
   This also has a positive effect on performance.
diff --git a/server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java b/server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java
index 24818ec068..45428cc4c8 100644
--- a/server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/expressions/ExpressionAnalyzer.java
@@ -1264,6 +1264,9 @@ public class ExpressionAnalyzer {
                             functionName));
                     }
                 }
+            } else if (filter != null) {
+                throw new UnsupportedOperationException(
+                    "FILTER is not implemented for non-aggregate window functions (" + functionName + ")");
             }
             newFunction = new WindowFunction(
                 signature,
diff --git a/server/src/test/java/io/crate/planner/operators/WindowAggTest.java b/server/src/test/java/io/crate/planner/operators/WindowAggTest.java
index 03d5c1fcd5..5043c17ebf 100644
--- a/server/src/test/java/io/crate/planner/operators/WindowAggTest.java
+++ b/server/src/test/java/io/crate/planner/operators/WindowAggTest.java
@@ -24,6 +24,7 @@ package io.crate.planner.operators;
 import static io.crate.testing.Asserts.assertThat;
 import static io.crate.testing.Asserts.isReference;
 import static org.assertj.core.api.Assertions.assertThat;
+import static org.assertj.core.api.Assertions.assertThatThrownBy;
 
 import org.junit.Before;
 import org.junit.Test;
@@ -143,6 +144,13 @@ public class WindowAggTest extends CrateDummyClusterServiceUnitTest {
         assertThat(orderBy.orderBySymbols()).satisfiesExactly(isReference("y"), isReference("x"));
     }
 
+    @Test
+    public void test_window_functions_do_not_support_filter_clause() throws Exception {
+        assertThatThrownBy(() -> plan("SELECT ROW_NUMBER() FILTER (WHERE x > 1) OVER (ORDER BY x) FROM t1"))
+            .isExactlyInstanceOf(UnsupportedOperationException.class)
+            .hasMessage("FILTER is not implemented for non-aggregate window functions (row_number)");
+    }
+
     private WindowDefinition wd(String expression) {
         Symbol symbol = e.asSymbol(expression);
         assertThat(symbol).isExactlyInstanceOf(WindowFunction.class);

```
