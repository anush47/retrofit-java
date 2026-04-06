# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java']
- Developer Java files: ['server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java']
- Overlap Java files: ['server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java']
- Mismatched files: ['server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java

- Developer hunks: 3
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -25,9 +25,12 @@
 import java.util.List;
 import java.util.Set;
 
+import io.crate.expression.operator.AndOperator;
 import io.crate.expression.operator.EqOperator;
 import io.crate.expression.operator.OrOperator;
 import io.crate.expression.predicate.NotPredicate;
+import io.crate.expression.scalar.cast.ExplicitCastFunction;
+import io.crate.expression.scalar.cast.ImplicitCastFunction;
 import io.crate.expression.symbol.Function;
 import io.crate.expression.symbol.ScopedSymbol;
 import io.crate.expression.symbol.Symbol;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,13 +1 @@-@@ -25,9 +25,12 @@
- import java.util.List;
- import java.util.Set;
- 
-+import io.crate.expression.operator.AndOperator;
- import io.crate.expression.operator.EqOperator;
- import io.crate.expression.operator.OrOperator;
- import io.crate.expression.predicate.NotPredicate;
-+import io.crate.expression.scalar.cast.ExplicitCastFunction;
-+import io.crate.expression.scalar.cast.ImplicitCastFunction;
- import io.crate.expression.symbol.Function;
- import io.crate.expression.symbol.ScopedSymbol;
- import io.crate.expression.symbol.Symbol;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -82,6 +85,12 @@
             }
             String functionName = function.name();
             switch (functionName) {
+                case AndOperator.NAME, ExplicitCastFunction.NAME, ImplicitCastFunction.NAME -> {
+                    for (Symbol arg : function.arguments()) {
+                        arg.accept(this, context);
+                    }
+                    return null;
+                }
                 case NotPredicate.NAME -> {
                     if (context.insideEqualOperand) {
                         // Not a top-level expression but inside EQ operator.

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,13 +1 @@-@@ -82,6 +85,12 @@
-             }
-             String functionName = function.name();
-             switch (functionName) {
-+                case AndOperator.NAME, ExplicitCastFunction.NAME, ImplicitCastFunction.NAME -> {
-+                    for (Symbol arg : function.arguments()) {
-+                        arg.accept(this, context);
-+                    }
-+                    return null;
-+                }
-                 case NotPredicate.NAME -> {
-                     if (context.insideEqualOperand) {
-                         // Not a top-level expression but inside EQ operator.
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -135,8 +144,12 @@
                     }
                 }
                 default -> {
-                    for (Symbol arg : function.arguments()) {
-                        arg.accept(this, context);
+                    if (context.insideEqualOperand) {
+                        for (Symbol arg : function.arguments()) {
+                            arg.accept(this, context);
+                        }
+                    } else {
+                        return null;
                     }
                 }
             }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,15 +1 @@-@@ -135,8 +144,12 @@
-                     }
-                 }
-                 default -> {
--                    for (Symbol arg : function.arguments()) {
--                        arg.accept(this, context);
-+                    if (context.insideEqualOperand) {
-+                        for (Symbol arg : function.arguments()) {
-+                            arg.accept(this, context);
-+                        }
-+                    } else {
-+                        return null;
-                     }
-                 }
-             }
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
diff --git a/docs/appendices/release-notes/5.10.1.rst b/docs/appendices/release-notes/5.10.1.rst
index 45c8eb2195..72d2fb5feb 100644
--- a/docs/appendices/release-notes/5.10.1.rst
+++ b/docs/appendices/release-notes/5.10.1.rst
@@ -144,3 +144,14 @@ Fixes
   by the :ref:`sql-restore-snapshot` statement when only a concrete table was
   specified as to be restored. Only the partitioned table definition was falsely
   restored, but not the the actual data.
+
+- Fixed a regression introduced with :ref:`version_5.10.0` that would lead to
+  wrong results for ``LEFT JOIN`` queries when the join condition has a
+  :ref:`CASE<scalar-case-when-then-end>` with an equality condition inside.
+  Previously, the optimizer would use :ref:`Hash Join<available-join-algo_hash>`
+  instead of :ref:`Nested Loop<available-join-algo_nl>` leading to wrong
+  results. e.g.::
+
+    SELECT * FROM tlb
+    LEFT JOIN (SELECT 2 AS col2 FROM tbl) AS tbl2
+      ON (CASE t0.c0 WHEN sub0.col2 THEN t0.c1 ELSE t0.c1 END)
diff --git a/docs/general/dql/joins.rst b/docs/general/dql/joins.rst
index d6993be3c3..0e376eed9d 100644
--- a/docs/general/dql/joins.rst
+++ b/docs/general/dql/joins.rst
@@ -233,6 +233,7 @@ Example with ``within`` scalar function::
 Available join algorithms
 -------------------------
 
+.. _available-join-algo_nl:
 
 Nested loop join algorithm
 ..........................
@@ -246,6 +247,8 @@ table.
 This is the default algorithm used for all types of joins.
 
 
+.. _available-join-algo_hash:
+
 Block hash join algorithm
 .........................
 
diff --git a/server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java b/server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java
index ec1e36a7f7..d18a40b149 100644
--- a/server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java
+++ b/server/src/main/java/io/crate/planner/operators/EquiJoinDetector.java
@@ -25,9 +25,12 @@ import java.util.HashSet;
 import java.util.List;
 import java.util.Set;
 
+import io.crate.expression.operator.AndOperator;
 import io.crate.expression.operator.EqOperator;
 import io.crate.expression.operator.OrOperator;
 import io.crate.expression.predicate.NotPredicate;
+import io.crate.expression.scalar.cast.ExplicitCastFunction;
+import io.crate.expression.scalar.cast.ImplicitCastFunction;
 import io.crate.expression.symbol.Function;
 import io.crate.expression.symbol.ScopedSymbol;
 import io.crate.expression.symbol.Symbol;
@@ -82,6 +85,12 @@ public final class EquiJoinDetector {
             }
             String functionName = function.name();
             switch (functionName) {
+                case AndOperator.NAME, ExplicitCastFunction.NAME, ImplicitCastFunction.NAME -> {
+                    for (Symbol arg : function.arguments()) {
+                        arg.accept(this, context);
+                    }
+                    return null;
+                }
                 case NotPredicate.NAME -> {
                     if (context.insideEqualOperand) {
                         // Not a top-level expression but inside EQ operator.
@@ -135,8 +144,12 @@ public final class EquiJoinDetector {
                     }
                 }
                 default -> {
-                    for (Symbol arg : function.arguments()) {
-                        arg.accept(this, context);
+                    if (context.insideEqualOperand) {
+                        for (Symbol arg : function.arguments()) {
+                            arg.accept(this, context);
+                        }
+                    } else {
+                        return null;
                     }
                 }
             }
diff --git a/server/src/test/java/io/crate/planner/operators/EquiJoinDetectorTest.java b/server/src/test/java/io/crate/planner/operators/EquiJoinDetectorTest.java
index bdf2e97f4d..ea2588943e 100644
--- a/server/src/test/java/io/crate/planner/operators/EquiJoinDetectorTest.java
+++ b/server/src/test/java/io/crate/planner/operators/EquiJoinDetectorTest.java
@@ -46,6 +46,12 @@ public class EquiJoinDetectorTest extends CrateDummyClusterServiceUnitTest {
         assertThat(EquiJoinDetector.isEquiJoin(joinCondition)).isTrue();
     }
 
+    @Test
+    public void test_equality_condition_inside_cast() {
+        Symbol joinCondition = sqlExpressions.asSymbol("CAST(CAST(t1.a = t2.b AS STRING) AS BOOLEAN)");
+        assertThat(EquiJoinDetector.isEquiJoin(joinCondition)).isTrue();
+    }
+
     @Test
     public void testPossibleOnInnerContainingEqAndAnyCondition() {
         Symbol joinCondition = sqlExpressions.asSymbol("t1.x > t2.y and t1.a = t2.b and not(t1.i = t2.i)");
@@ -100,13 +106,29 @@ public class EquiJoinDetectorTest extends CrateDummyClusterServiceUnitTest {
         assertThat(EquiJoinDetector.isEquiJoin(joinCondition)).isFalse();
     }
 
-    // tracks a bug : https://github.com/crate/crate/issues/15613
+    // tracks a bug: https://github.com/crate/crate/issues/15613
     @Test
     public void test_equality_expression_followed_by_case_expression() {
         Symbol joinCondition = sqlExpressions.asSymbol("t1.a = t1.a AND CASE 1 WHEN t1.a THEN false ELSE t2.b in (t2.b) END");
         assertThat(EquiJoinDetector.isEquiJoin(joinCondition)).isFalse();
     }
 
+    // tracks a bug: https://github.com/crate/crate/issues/17380
+    @Test
+    public void test_case_expression_with_nested_equality() {
+        Symbol joinCondition = sqlExpressions.asSymbol("CASE WHEN t1.a = t2.b THEN t1.a ELSE t2.b END");
+        assertThat(EquiJoinDetector.isEquiJoin(joinCondition)).isFalse();
+        joinCondition = sqlExpressions.asSymbol("CASE t1.a WHEN t2.b THEN t1.a ELSE t2.b END");
+        assertThat(EquiJoinDetector.isEquiJoin(joinCondition)).isFalse();
+    }
+
+    // tracks a bug: https://github.com/crate/crate/issues/17380
+    @Test
+    public void test_if_expression_with_nested_equality() {
+        Symbol joinCondition = sqlExpressions.asSymbol("if(t1.a = t2.b, 1, 2)");
+        assertThat(EquiJoinDetector.isEquiJoin(joinCondition)).isFalse();
+    }
+
     @Test
     public void test_equality_and_many_relations_in_boolean_join_condition_hash_join_not_possible() {
         // Nested EQ operator.

```
