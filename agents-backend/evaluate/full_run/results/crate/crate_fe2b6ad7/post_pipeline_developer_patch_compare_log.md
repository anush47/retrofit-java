# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/analyze/TableInfoToAST.java']
- Developer Java files: ['server/src/main/java/io/crate/analyze/TableInfoToAST.java']
- Overlap Java files: ['server/src/main/java/io/crate/analyze/TableInfoToAST.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/analyze/TableInfoToAST.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/analyze/TableInfoToAST.java']
- Mismatched files: ['server/src/main/java/io/crate/analyze/TableInfoToAST.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/analyze/TableInfoToAST.java

- Developer hunks: 3
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -22,6 +22,8 @@
 package io.crate.analyze;
 
 
+import static io.crate.analyze.TableParameters.stripIndexPrefix;
+
 import java.util.ArrayList;
 import java.util.Collection;
 import java.util.HashMap;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -22,6 +22,8 @@
- package io.crate.analyze;
- 
- 
-+import static io.crate.analyze.TableParameters.stripIndexPrefix;
-+
- import java.util.ArrayList;
- import java.util.Collection;
- import java.util.HashMap;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -305,7 +307,7 @@
     private GenericProperties<Expression> extractTableProperties() {
         // WITH ( key = value, ... )
         Map<String, Expression> properties = new HashMap<>();
-        String numberOfReplicasKey = TableParameters.stripIndexPrefix(NumberOfReplicas.SETTING.getKey());
+        String numberOfReplicasKey = stripIndexPrefix(NumberOfReplicas.SETTING.getKey());
         if (tableInfo instanceof DocTableInfo docTable) {
             Expression numReplicas = new StringLiteral(docTable.numberOfReplicas());
             properties.put(numberOfReplicasKey, numReplicas);

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -305,7 +307,7 @@
-     private GenericProperties<Expression> extractTableProperties() {
-         // WITH ( key = value, ... )
-         Map<String, Expression> properties = new HashMap<>();
--        String numberOfReplicasKey = TableParameters.stripIndexPrefix(NumberOfReplicas.SETTING.getKey());
-+        String numberOfReplicasKey = stripIndexPrefix(NumberOfReplicas.SETTING.getKey());
-         if (tableInfo instanceof DocTableInfo docTable) {
-             Expression numReplicas = new StringLiteral(docTable.numberOfReplicas());
-             properties.put(numberOfReplicasKey, numReplicas);
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -326,7 +328,7 @@
                 for (String namespace : namespaces) {
                     String key = prefix + namespace;
                     Object value = affixSetting.getConcreteSetting(key).get(parameters);
-                    properties.put(key, literalOfSettingValue(value));
+                    properties.put(stripIndexPrefix(key), literalOfSettingValue(value));
                 }
             } else if (parameters.hasValue(setting.getKey())) {
                 Object value = setting.get(parameters);

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -326,7 +328,7 @@
-                 for (String namespace : namespaces) {
-                     String key = prefix + namespace;
-                     Object value = affixSetting.getConcreteSetting(key).get(parameters);
--                    properties.put(key, literalOfSettingValue(value));
-+                    properties.put(stripIndexPrefix(key), literalOfSettingValue(value));
-                 }
-             } else if (parameters.hasValue(setting.getKey())) {
-                 Object value = setting.get(parameters);
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
diff --git a/docs/appendices/release-notes/5.10.10.rst b/docs/appendices/release-notes/5.10.10.rst
index 63b021d804..247f900130 100644
--- a/docs/appendices/release-notes/5.10.10.rst
+++ b/docs/appendices/release-notes/5.10.10.rst
@@ -61,3 +61,7 @@ Fixes
 - Fixed an issue that caused queries with aggregations to continue despite
   ``CircuitBreakerException`` being thrown and return incorrect (partial)
   results under memory pressure.
+
+- Fixed the table parameter namings of the :ref:`ref-show-create-table`
+  statement output, some parameters were wrongly prefixed with
+  ``index.``.
diff --git a/server/src/main/java/io/crate/analyze/TableInfoToAST.java b/server/src/main/java/io/crate/analyze/TableInfoToAST.java
index 477cbc8b10..27b97e2eef 100644
--- a/server/src/main/java/io/crate/analyze/TableInfoToAST.java
+++ b/server/src/main/java/io/crate/analyze/TableInfoToAST.java
@@ -22,6 +22,8 @@
 package io.crate.analyze;
 
 
+import static io.crate.analyze.TableParameters.stripIndexPrefix;
+
 import java.util.ArrayList;
 import java.util.Collection;
 import java.util.HashMap;
@@ -305,7 +307,7 @@ public class TableInfoToAST {
     private GenericProperties<Expression> extractTableProperties() {
         // WITH ( key = value, ... )
         Map<String, Expression> properties = new HashMap<>();
-        String numberOfReplicasKey = TableParameters.stripIndexPrefix(NumberOfReplicas.SETTING.getKey());
+        String numberOfReplicasKey = stripIndexPrefix(NumberOfReplicas.SETTING.getKey());
         if (tableInfo instanceof DocTableInfo docTable) {
             Expression numReplicas = new StringLiteral(docTable.numberOfReplicas());
             properties.put(numberOfReplicasKey, numReplicas);
@@ -326,7 +328,7 @@ public class TableInfoToAST {
                 for (String namespace : namespaces) {
                     String key = prefix + namespace;
                     Object value = affixSetting.getConcreteSetting(key).get(parameters);
-                    properties.put(key, literalOfSettingValue(value));
+                    properties.put(stripIndexPrefix(key), literalOfSettingValue(value));
                 }
             } else if (parameters.hasValue(setting.getKey())) {
                 Object value = setting.get(parameters);
diff --git a/server/src/test/java/io/crate/analyze/TableInfoToASTTest.java b/server/src/test/java/io/crate/analyze/TableInfoToASTTest.java
index f4c3d8bf08..e382ccca86 100644
--- a/server/src/test/java/io/crate/analyze/TableInfoToASTTest.java
+++ b/server/src/test/java/io/crate/analyze/TableInfoToASTTest.java
@@ -393,4 +393,29 @@ public class TableInfoToASTTest extends CrateDummyClusterServiceUnitTest {
         assertThat(geoRef.precision()).isEqualTo("1m");
         assertThat(geoRef.distanceErrorPct()).isEqualTo(0.25);
     }
+
+    /**
+     * Ensures that the index prefix for table parameters, including group settings, is stripped
+     * when printing the table definition.
+     */
+    @Test
+    public void test_table_parameters_index_prefix_stripped() throws Exception {
+        SQLExecutor e = SQLExecutor.of(clusterService)
+            .addTable("CREATE TABLE t1 (id int) CLUSTERED INTO 1 SHARDS " +
+                "WITH (\"blocks.read_only_allow_delete\" = true, \"routing.allocation.exclude._name\" = 'node-1')");
+        DocTableInfo table = e.resolveTableInfo("t1");
+        var node = new TableInfoToAST(table).toStatement();
+        assertThat(SqlFormatter.formatSql(node)).isEqualTo("""
+              CREATE TABLE IF NOT EXISTS "doc"."t1" (
+                 "id" INTEGER
+              )
+              CLUSTERED INTO 1 SHARDS
+              WITH (
+                 "blocks.read_only_allow_delete" = true,
+                 column_policy = 'strict',
+                 number_of_replicas = '0-1',
+                 "routing.allocation.exclude._name" = 'node-1'
+              )""");
+
+    }
 }

```
