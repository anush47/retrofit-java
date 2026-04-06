# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java']
- Developer Java files: ['x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java']
- Overlap Java files: ['x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java']

## File State Comparison
- Compared files: ['x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java']
- Mismatched files: ['x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java

- Developer hunks: 2
- Generated hunks: 2

#### Hunk 1

Developer
```diff
@@ -31,7 +31,6 @@
 import org.elasticsearch.xpack.esql.core.util.CollectionUtils;
 import org.elasticsearch.xpack.esql.core.util.Queries;
 import org.elasticsearch.xpack.esql.expression.function.fulltext.FullTextFunction;
-import org.elasticsearch.xpack.esql.expression.function.fulltext.Term;
 import org.elasticsearch.xpack.esql.expression.function.scalar.ip.CIDRMatch;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.BinarySpatialFunction;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.SpatialRelatesFunction;

```

Generated
```diff
@@ -31,7 +31,7 @@
 import org.elasticsearch.xpack.esql.core.util.CollectionUtils;
 import org.elasticsearch.xpack.esql.core.util.Queries;
 import org.elasticsearch.xpack.esql.expression.function.fulltext.FullTextFunction;
-import org.elasticsearch.xpack.esql.expression.function.fulltext.Term;
+
 import org.elasticsearch.xpack.esql.expression.function.scalar.ip.CIDRMatch;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.BinarySpatialFunction;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.SpatialRelatesFunction;

```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1,9 @@-@@ -31,7 +31,6 @@
+@@ -31,7 +31,7 @@
  import org.elasticsearch.xpack.esql.core.util.CollectionUtils;
  import org.elasticsearch.xpack.esql.core.util.Queries;
  import org.elasticsearch.xpack.esql.expression.function.fulltext.FullTextFunction;
 -import org.elasticsearch.xpack.esql.expression.function.fulltext.Term;
++
  import org.elasticsearch.xpack.esql.expression.function.scalar.ip.CIDRMatch;
  import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.BinarySpatialFunction;
  import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.SpatialRelatesFunction;

```

#### Hunk 2

Developer
```diff
@@ -252,8 +251,6 @@
                 && Expressions.foldable(cidrMatch.matches());
         } else if (exp instanceof SpatialRelatesFunction spatial) {
             return canPushSpatialFunctionToSource(spatial, lucenePushdownPredicates);
-        } else if (exp instanceof Term term) {
-            return term.field() instanceof FieldAttribute && DataType.isString(term.field().dataType());
         } else if (exp instanceof FullTextFunction) {
             return true;
         }

```

Generated
```diff
@@ -252,8 +252,7 @@
                 && Expressions.foldable(cidrMatch.matches());
         } else if (exp instanceof SpatialRelatesFunction spatial) {
             return canPushSpatialFunctionToSource(spatial, lucenePushdownPredicates);
-        } else if (exp instanceof Term term) {
-            return term.field() instanceof FieldAttribute && DataType.isString(term.field().dataType());
+
         } else if (exp instanceof FullTextFunction) {
             return true;
         }

```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1,10 @@-@@ -252,8 +251,6 @@
+@@ -252,8 +252,7 @@
                  && Expressions.foldable(cidrMatch.matches());
          } else if (exp instanceof SpatialRelatesFunction spatial) {
              return canPushSpatialFunctionToSource(spatial, lucenePushdownPredicates);
 -        } else if (exp instanceof Term term) {
 -            return term.field() instanceof FieldAttribute && DataType.isString(term.field().dataType());
++
          } else if (exp instanceof FullTextFunction) {
              return true;
          }

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java b/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java
index 6fcdd538fdf..703be33de13 100644
--- a/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java
+++ b/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java
@@ -31,7 +31,7 @@ import org.elasticsearch.xpack.esql.core.type.DataType;
 import org.elasticsearch.xpack.esql.core.util.CollectionUtils;
 import org.elasticsearch.xpack.esql.core.util.Queries;
 import org.elasticsearch.xpack.esql.expression.function.fulltext.FullTextFunction;
-import org.elasticsearch.xpack.esql.expression.function.fulltext.Term;
+
 import org.elasticsearch.xpack.esql.expression.function.scalar.ip.CIDRMatch;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.BinarySpatialFunction;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.SpatialRelatesFunction;
@@ -252,8 +252,7 @@ public class PushFiltersToSource extends PhysicalOptimizerRules.ParameterizedOpt
                 && Expressions.foldable(cidrMatch.matches());
         } else if (exp instanceof SpatialRelatesFunction spatial) {
             return canPushSpatialFunctionToSource(spatial, lucenePushdownPredicates);
-        } else if (exp instanceof Term term) {
-            return term.field() instanceof FieldAttribute && DataType.isString(term.field().dataType());
+
         } else if (exp instanceof FullTextFunction) {
             return true;
         }

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java b/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java
index 6fcdd538fdf..703be33de13 100644
--- a/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java
+++ b/x-pack/plugin/esql/src/main/java/org/elasticsearch/xpack/esql/optimizer/rules/physical/local/PushFiltersToSource.java
@@ -31,7 +31,7 @@ import org.elasticsearch.xpack.esql.core.type.DataType;
 import org.elasticsearch.xpack.esql.core.util.CollectionUtils;
 import org.elasticsearch.xpack.esql.core.util.Queries;
 import org.elasticsearch.xpack.esql.expression.function.fulltext.FullTextFunction;
-import org.elasticsearch.xpack.esql.expression.function.fulltext.Term;
+
 import org.elasticsearch.xpack.esql.expression.function.scalar.ip.CIDRMatch;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.BinarySpatialFunction;
 import org.elasticsearch.xpack.esql.expression.function.scalar.spatial.SpatialRelatesFunction;
@@ -252,8 +252,7 @@ public class PushFiltersToSource extends PhysicalOptimizerRules.ParameterizedOpt
                 && Expressions.foldable(cidrMatch.matches());
         } else if (exp instanceof SpatialRelatesFunction spatial) {
             return canPushSpatialFunctionToSource(spatial, lucenePushdownPredicates);
-        } else if (exp instanceof Term term) {
-            return term.field() instanceof FieldAttribute && DataType.isString(term.field().dataType());
+
         } else if (exp instanceof FullTextFunction) {
             return true;
         }

```
## Full Developer Backport Patch (full commit diff)
```diff
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
index 2226b8a6468..f092a67b84e 100644
--- a/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LocalPhysicalPlanOptimizerTests.java
+++ b/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/optimizer/LocalPhysicalPlanOptimizerTests.java
@@ -1401,11 +1401,6 @@ public class LocalPhysicalPlanOptimizerTests extends MapperServiceTestCase {
         var analyzer = makeAnalyzer("mapping-all-types.json", new EnrichResolution());
         // Check for every possible query data type
         for (DataType fieldDataType : fieldDataTypes) {
-            // TODO: semantic_text is not present in mapping-all-types.json so we skip it for now
-            if (fieldDataType == DataType.SEMANTIC_TEXT) {
-                continue;
-            }
-
             var queryValue = randomQueryValue(fieldDataType);
 
             String fieldName = fieldDataType == DataType.DATETIME ? "date" : fieldDataType.name().toLowerCase(Locale.ROOT);

```
