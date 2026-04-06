# Phase 0 Inputs

- Mainline commit: a97d13e1e2771a86646938fc969ddf7bbdd124bd
- Backport commit: 68019c3f5a14ab4cec07d35a983cea6fea8a3606
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 3

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/expression/predicate/NotPredicate.java']
- Developer Java files: ['server/src/main/java/io/crate/expression/predicate/NotPredicate.java']
- Overlap Java files: ['server/src/main/java/io/crate/expression/predicate/NotPredicate.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From a97d13e1e2771a86646938fc969ddf7bbdd124bd Mon Sep 17 00:00:00 2001
From: Marios Trivyzas <matriv@gmail.com>
Date: Tue, 3 Sep 2024 14:00:33 +0300
Subject: [PATCH] Fix nullability issue for CAST on object columns

Previously, when using `CAST` on an object column in the WHERE clause,
it would falsly match and return back rows for which the value for the
object column was `null`. Set `enforceThreeValuedLogic` flag to true
to correctly produce the lucene query to filter out the nulls.

Fixes: #16556
---
 docs/appendices/release-notes/5.8.3.rst                   | 8 ++++++++
 .../java/io/crate/expression/predicate/NotPredicate.java  | 1 +
 .../crate/expression/predicate/FieldExistsQueryTest.java  | 3 +--
 .../io/crate/lucene/ThreeValuedLogicQueryBuilderTest.java | 6 ++++++
 4 files changed, 16 insertions(+), 2 deletions(-)

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
index b0a1fc614f..d4597a79df 100644
--- a/server/src/main/java/io/crate/expression/predicate/NotPredicate.java
+++ b/server/src/main/java/io/crate/expression/predicate/NotPredicate.java
@@ -153,6 +153,7 @@ public class NotPredicate extends Scalar<Boolean, Boolean> {
                 var b = function.arguments().get(1);
                 if (a instanceof Reference ref && b instanceof Literal<?>) {
                     if (ref.valueType().id() == DataTypes.UNTYPED_OBJECT.id()) {
+                        context.enforceThreeValuedLogic = true;
                         return null;
                     }
                 }
diff --git a/server/src/test/java/io/crate/expression/predicate/FieldExistsQueryTest.java b/server/src/test/java/io/crate/expression/predicate/FieldExistsQueryTest.java
index ebb1b03774..addf16b31a 100644
--- a/server/src/test/java/io/crate/expression/predicate/FieldExistsQueryTest.java
+++ b/server/src/test/java/io/crate/expression/predicate/FieldExistsQueryTest.java
@@ -102,10 +102,9 @@ public class FieldExistsQueryTest extends LuceneQueryBuilderTest {
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
index 6a07d9fc07..ead33445d4 100644
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
-- 
2.43.0


```
