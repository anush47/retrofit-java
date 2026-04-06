# Phase 0 Inputs

- Mainline commit: 355aed7fc80c1e9a2ce58ffd45615ed110312f0f
- Backport commit: a04d2466697536ff423c8aa7c9b81d26dda6aa07
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 2

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java']
- Developer Java files: ['x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java']
- Overlap Java files: ['x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 355aed7fc80c1e9a2ce58ffd45615ed110312f0f Mon Sep 17 00:00:00 2001
From: Ioana Tagirta <ioanatia@users.noreply.github.com>
Date: Tue, 7 Jan 2025 12:19:19 +0100
Subject: [PATCH] Add semantic_text to mapping_all_types and switch to
 TranslationAware in PushFiltersToSource (#118982)

* Add semantic_text to mapping-all-types.json and switch to TranslationAware in PushFiltersToSource

* Continue to use FullTextFunction for now

---------

Co-authored-by: Elastic Machine <elasticmachine@users.noreply.github.com>
---
 .../testFixtures/src/main/resources/mapping-all-types.json   | 4 ++++
 .../optimizer/rules/physical/local/PushFiltersToSource.java  | 3 ---
 .../esql/optimizer/LocalPhysicalPlanOptimizerTests.java      | 5 -----
 3 files changed, 4 insertions(+), 8 deletions(-)

diff --git a/x-pack/plugin/esql/qa/testFixtures/src/main/resources/mapping-all-types.json b/x-pack/plugin/esql/qa/testFixtures/src/main/resources/mapping-all-types.json
index 04b59f347eb..17348adb6af 100644
--- a/x-pack/plugin/esql/qa/testFixtures/src/main/resources/mapping-all-types.json
+++ b/x-pack/plugin/esql/qa/testFixtures/src/main/resources/mapping-all-types.json
@@ -59,6 +59,10 @@
         },
         "wildcard": {
             "type": "wildcard"
+        },
+        "semantic_text": {
+            "type": "semantic_text",
+            "inference_id": "foo_inference_id"
         }
     }
 }
diff --git a/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java b/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java
index 6fcdd538fdf..dae84bb6b64 100644
--- a/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java
+++ b/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java
@@ -31,7 +31,6 @@ import org.elasticsearch.xpack.esql.core.type.DataType;
 import org.elasticsearch.xpack.esql.core.util.CollectionUtils;
 import org.elasticsearch.xpack.esql.core.util.Queries;
 import org.elasticsearch.xpack.esql.expression.function.fulltext.FullTextFunction;
-import org.elasticsearch.xpack.esql.expression.function.fulltext.Term;
 import org.elasticsearch.xpack.esql.expression.function.scalar.ip.CIDRMatch;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.BinarySpatialFunction;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.SpatialRelatesFunction;
@@ -252,8 +251,6 @@ public class PushFiltersToSource extends PhysicalOptimizerRules.ParameterizedOpt
                 && Expressions.foldable(cidrMatch.matches());
         } else if (exp instanceof SpatialRelatesFunction spatial) {
             return canPushSpatialFunctionToSource(spatial, lucenePushdownPredicates);
-        } else if (exp instanceof Term term) {
-            return term.field() instanceof FieldAttribute && DataType.isString(term.field().dataType());
         } else if (exp instanceof FullTextFunction) {
             return true;
         }
diff --git a/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LocalPhysicalPlanOptimizerTests.java b/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LocalPhysicalPlanOptimizerTests.java
index 928c849b847..fc2f6320274 100644
--- a/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LocalPhysicalPlanOptimizerTests.java
+++ b/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LocalPhysicalPlanOptimizerTests.java
@@ -1450,11 +1450,6 @@ public class LocalPhysicalPlanOptimizerTests extends MapperServiceTestCase {
         var analyzer = makeAnalyzer("mapping-all-types.json");
         // Check for every possible query data type
         for (DataType fieldDataType : fieldDataTypes) {
-            // TODO: semantic_text is not present in mapping-all-types.json so we skip it for now
-            if (fieldDataType == DataType.SEMANTIC_TEXT) {
-                continue;
-            }
-
             var queryValue = randomQueryValue(fieldDataType);
 
             String fieldName = fieldDataType == DataType.DATETIME ? "date" : fieldDataType.name().toLowerCase(Locale.ROOT);
-- 
2.43.0


```
