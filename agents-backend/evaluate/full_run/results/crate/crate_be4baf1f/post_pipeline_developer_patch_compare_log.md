# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java']
- Developer Java files: ['server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java']
- Overlap Java files: ['server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java']
- Mismatched files: ['server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java

- Developer hunks: 3
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -21,6 +21,13 @@
 
 package io.crate.expression.symbol;
 
+import java.io.IOException;
+import java.util.Locale;
+import java.util.Objects;
+
+import org.elasticsearch.common.io.stream.StreamInput;
+import org.elasticsearch.common.io.stream.StreamOutput;
+
 import io.crate.data.Row;
 import io.crate.expression.scalar.cast.CastMode;
 import io.crate.expression.symbol.format.Style;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,14 +1 @@-@@ -21,6 +21,13 @@
- 
- package io.crate.expression.symbol;
- 
-+import java.io.IOException;
-+import java.util.Locale;
-+import java.util.Objects;
-+
-+import org.elasticsearch.common.io.stream.StreamInput;
-+import org.elasticsearch.common.io.stream.StreamOutput;
-+
- import io.crate.data.Row;
- import io.crate.expression.scalar.cast.CastMode;
- import io.crate.expression.symbol.format.Style;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -28,11 +35,6 @@
 import io.crate.types.DataTypes;
 import io.crate.types.IntegerType;
 import io.crate.types.UndefinedType;
-import org.elasticsearch.common.io.stream.StreamInput;
-import org.elasticsearch.common.io.stream.StreamOutput;
-
-import java.io.IOException;
-import java.util.Locale;
 
 public class ParameterSymbol implements Symbol {
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,12 +1 @@-@@ -28,11 +35,6 @@
- import io.crate.types.DataTypes;
- import io.crate.types.IntegerType;
- import io.crate.types.UndefinedType;
--import org.elasticsearch.common.io.stream.StreamInput;
--import org.elasticsearch.common.io.stream.StreamOutput;
--
--import java.io.IOException;
--import java.util.Locale;
- 
- public class ParameterSymbol implements Symbol {
- 
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -126,4 +128,19 @@
             ));
         }
     }
+
+    @Override
+    public boolean equals(Object o) {
+        if (this == o) return true;
+        if (o == null || getClass() != o.getClass()) return false;
+        ParameterSymbol that = (ParameterSymbol) o;
+        return Objects.equals(index, that.index) &&
+            Objects.equals(boundType, that.boundType) &&
+            Objects.equals(internalType, that.internalType);
+    }
+
+    @Override
+    public int hashCode() {
+        return Objects.hash(index, boundType, internalType);
+    }
 }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,20 +1 @@-@@ -126,4 +128,19 @@
-             ));
-         }
-     }
-+
-+    @Override
-+    public boolean equals(Object o) {
-+        if (this == o) return true;
-+        if (o == null || getClass() != o.getClass()) return false;
-+        ParameterSymbol that = (ParameterSymbol) o;
-+        return Objects.equals(index, that.index) &&
-+            Objects.equals(boundType, that.boundType) &&
-+            Objects.equals(internalType, that.internalType);
-+    }
-+
-+    @Override
-+    public int hashCode() {
-+        return Objects.hash(index, boundType, internalType);
-+    }
- }
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
diff --git a/docs/appendices/release-notes/5.10.7.rst b/docs/appendices/release-notes/5.10.7.rst
index 6e5474b8f4..d87bdb76f1 100644
--- a/docs/appendices/release-notes/5.10.7.rst
+++ b/docs/appendices/release-notes/5.10.7.rst
@@ -47,6 +47,14 @@ See the :ref:`version_5.10.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- Fixed an issue that would cause :ref:`window functions <window-functions>` to
+  use inefficient execution plans, resulting in poor performance, when the
+  :ref:`window definition <window-definition>` is using query parameters. e.g::
+
+    SELECT min(x) OVER (w), max(x) OVER(w), avg(x) OVER (w)
+    FROM tbl
+    WINDOW w AS (PARTITION BY (x / ?))
+
 - Fixed a bug where the session setting
   :ref:`conf-session-error_on_unknown_object_key` was not persisted into a view,
   and such not taken into account when executing the view. Previously created
diff --git a/server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java b/server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java
index 6d0aa5c254..12f57d946a 100644
--- a/server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java
+++ b/server/src/main/java/io/crate/expression/symbol/ParameterSymbol.java
@@ -21,6 +21,13 @@
 
 package io.crate.expression.symbol;
 
+import java.io.IOException;
+import java.util.Locale;
+import java.util.Objects;
+
+import org.elasticsearch.common.io.stream.StreamInput;
+import org.elasticsearch.common.io.stream.StreamOutput;
+
 import io.crate.data.Row;
 import io.crate.expression.scalar.cast.CastMode;
 import io.crate.expression.symbol.format.Style;
@@ -28,11 +35,6 @@ import io.crate.types.DataType;
 import io.crate.types.DataTypes;
 import io.crate.types.IntegerType;
 import io.crate.types.UndefinedType;
-import org.elasticsearch.common.io.stream.StreamInput;
-import org.elasticsearch.common.io.stream.StreamOutput;
-
-import java.io.IOException;
-import java.util.Locale;
 
 public class ParameterSymbol implements Symbol {
 
@@ -126,4 +128,19 @@ public class ParameterSymbol implements Symbol {
             ));
         }
     }
+
+    @Override
+    public boolean equals(Object o) {
+        if (this == o) return true;
+        if (o == null || getClass() != o.getClass()) return false;
+        ParameterSymbol that = (ParameterSymbol) o;
+        return Objects.equals(index, that.index) &&
+            Objects.equals(boundType, that.boundType) &&
+            Objects.equals(internalType, that.internalType);
+    }
+
+    @Override
+    public int hashCode() {
+        return Objects.hash(index, boundType, internalType);
+    }
 }
diff --git a/server/src/test/java/io/crate/planner/operators/WindowAggTest.java b/server/src/test/java/io/crate/planner/operators/WindowAggTest.java
index ddd95311ec..81c564f59f 100644
--- a/server/src/test/java/io/crate/planner/operators/WindowAggTest.java
+++ b/server/src/test/java/io/crate/planner/operators/WindowAggTest.java
@@ -62,6 +62,33 @@ public class WindowAggTest extends CrateDummyClusterServiceUnitTest {
         return e.logicalPlan(statement);
     }
 
+    @Test
+    public void test_two_window_functions_with_same_window_definition_results_in_one_operator() {
+        LogicalPlan plan = plan("SELECT avg(x) OVER (PARTITION BY x), avg(x) OVER (PARTITION BY x) FROM t1");
+        var expectedPlan =
+            """
+            Eval[avg(x) OVER (PARTITION BY x), avg(x) OVER (PARTITION BY x)]
+              └ WindowAgg[x, avg(x) OVER (PARTITION BY x)]
+                └ Collect[doc.t1 | [x] | true]
+            """;
+        assertThat(plan).isEqualTo(expectedPlan);
+    }
+
+    @Test
+    public void test_two_window_functions_with_same_window_definition_with_param_results_in_one_operator() {
+        LogicalPlan plan = plan("SELECT min(x) OVER (PARTITION BY x * $1::int), avg(x) OVER (PARTITION BY x * $1::int) FROM t1");
+        var expectedPlan =
+            """
+            Eval[min(x) OVER (PARTITION BY (x * $1)), avg(x) OVER (PARTITION BY (x * $1))]
+              └ WindowAgg[x, (x * $1), min(x) OVER (PARTITION BY (x * $1)), avg(x) OVER (PARTITION BY (x * $1))]
+                └ Collect[doc.t1 | [x, (x * $1)] | true]
+            """;
+        assertThat(plan).isEqualTo(expectedPlan);
+
+        plan = plan("SELECT min(x) OVER (w), avg(x) OVER (w) FROM t1 WINDOW w AS (PARTITION BY (x * ?::int))");
+        assertThat(plan).isEqualTo(expectedPlan);
+    }
+
     @Test
     public void testTwoWindowFunctionsWithDifferentWindowDefinitionResultsInTwoOperators() {
         LogicalPlan plan = plan("SELECT avg(x) OVER (PARTITION BY x), avg(x) OVER (PARTITION BY y) FROM t1");

```
