# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/expression/predicate/NotPredicate.java']
- Developer Java files: ['server/src/main/java/io/crate/expression/predicate/NotPredicate.java']
- Overlap Java files: ['server/src/main/java/io/crate/expression/predicate/NotPredicate.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/expression/predicate/NotPredicate.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/expression/predicate/NotPredicate.java']
- Mismatched files: ['server/src/main/java/io/crate/expression/predicate/NotPredicate.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/expression/predicate/NotPredicate.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -149,6 +149,7 @@
                 var b = function.arguments().get(1);
                 if (a instanceof Reference ref && b instanceof Literal<?>) {
                     if (ref.valueType().id() == DataTypes.UNTYPED_OBJECT.id()) {
+                        context.enforceThreeValuedLogic = true;
                         return null;
                     }
                 }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -149,6 +149,7 @@
-                 var b = function.arguments().get(1);
-                 if (a instanceof Reference ref && b instanceof Literal<?>) {
-                     if (ref.valueType().id() == DataTypes.UNTYPED_OBJECT.id()) {
-+                        context.enforceThreeValuedLogic = true;
-                         return null;
-                     }
-                 }
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
diff --git a/docs/appendices/release-notes/5.8.3.rst b/docs/appendices/release-notes/5.8.3.rst
index ecf51f53b2..fa9a779d2b 100644
--- a/docs/appendices/release-notes/5.8.3.rst
+++ b/docs/appendices/release-notes/5.8.3.rst
@@ -47,6 +47,14 @@ See the :ref:`version_5.8.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- Fixed an issue that caused ``WHERE`` clause to fail to filter rows when
+  the clause contained casts on null object columns under ``NOT`` operator.
+  e.g.::
+
+    CREATE  TABLE  t1(c0 OBJECT NULL);
+    INSERT INTO t1(c0) VALUES (NULL);
+    SELECT * FROM t1 WHERE NOT (CAST(t1.c0 AS STRING) ='');
+
 - Fixed an issue that could cause errors like ``ClassCastException`` if using
   column aliases in a Subquery that lead to ambiguous column names.
 
diff --git a/server/src/main/java/io/crate/expression/predicate/NotPredicate.java b/server/src/main/java/io/crate/expression/predicate/NotPredicate.java
index 1343e2e356..b5bb66984d 100644
--- a/server/src/main/java/io/crate/expression/predicate/NotPredicate.java
+++ b/server/src/main/java/io/crate/expression/predicate/NotPredicate.java
@@ -149,6 +149,7 @@ public class NotPredicate extends Scalar<Boolean, Boolean> {
                 var b = function.arguments().get(1);
                 if (a instanceof Reference ref && b instanceof Literal<?>) {
                     if (ref.valueType().id() == DataTypes.UNTYPED_OBJECT.id()) {
+                        context.enforceThreeValuedLogic = true;
                         return null;
                     }
                 }
diff --git a/server/src/test/java/io/crate/expression/predicate/FieldExistsQueryTest.java b/server/src/test/java/io/crate/expression/predicate/FieldExistsQueryTest.java
index d43727feae..c235be3841 100644
--- a/server/src/test/java/io/crate/expression/predicate/FieldExistsQueryTest.java
+++ b/server/src/test/java/io/crate/expression/predicate/FieldExistsQueryTest.java
@@ -98,10 +98,9 @@ public class FieldExistsQueryTest extends CrateDummyClusterServiceUnitTest {
             if (values == null) {
                 assertThat(results).isEmpty();
             } else {
-                assertThat(results).hasSize(2);
+                assertThat(results).hasSize(1);
                 assertThat(results.get(0)).isInstanceOf(Map.class);
                 assertThat((Map<?, ?>) results.get(0)).isEmpty();
-                assertThat(results.get(1)).isNull();
             }
         }
     }
diff --git a/server/src/test/java/io/crate/lucene/ThreeValuedLogicQueryBuilderTest.java b/server/src/test/java/io/crate/lucene/ThreeValuedLogicQueryBuilderTest.java
index 5127220025..51d70d787a 100644
--- a/server/src/test/java/io/crate/lucene/ThreeValuedLogicQueryBuilderTest.java
+++ b/server/src/test/java/io/crate/lucene/ThreeValuedLogicQueryBuilderTest.java
@@ -135,4 +135,10 @@ public class ThreeValuedLogicQueryBuilderTest extends LuceneQueryBuilderTest {
         assertThat(convert("NOT pg_catalog.format_type(x, null)")).hasToString(
             "+(+*:* -pg_catalog.format_type(x, NULL)) #(NOT pg_catalog.format_type(x, NULL))");
     }
+
+    @Test
+    public void test_negated_cast_on_object() {
+        assertThat(convert("NOT (cast(obj as string))")).hasToString(
+            "+(+*:* -cast(obj AS text)) #(NOT cast(obj AS text))");
+    }
 }

```
