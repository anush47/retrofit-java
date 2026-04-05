# Phase 0 Inputs

- Mainline commit: fe2b6ad7429fcb7e909d2f2007b1b0ed66814322
- Backport commit: 62e69b530a0ae95f724b7004f17468bfcfb510cd
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 2

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/analyze/TableInfoToAST.java']
- Developer Java files: ['server/src/main/java/io/crate/analyze/TableInfoToAST.java']
- Overlap Java files: ['server/src/main/java/io/crate/analyze/TableInfoToAST.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From fe2b6ad7429fcb7e909d2f2007b1b0ed66814322 Mon Sep 17 00:00:00 2001
From: Sebastian Utz <su@rtme.net>
Date: Fri, 27 Jun 2025 13:18:49 +0200
Subject: [PATCH] Fix the table AST parsing of group table settings to strip
 index prefix

The `index.` prefix was not stripped for group settings like e.g.
`index.routing.allocation.exclude.`.

Fixes #18072.
---
 docs/appendices/release-notes/5.10.10.rst     |  4 +++
 .../java/io/crate/analyze/TableInfoToAST.java |  6 +++--
 .../io/crate/analyze/TableInfoToASTTest.java  | 25 +++++++++++++++++++
 3 files changed, 33 insertions(+), 2 deletions(-)

diff --git a/docs/appendices/release-notes/5.10.10.rst b/docs/appendices/release-notes/5.10.10.rst
index e6b6ea0a48..05602ee488 100644
--- a/docs/appendices/release-notes/5.10.10.rst
+++ b/docs/appendices/release-notes/5.10.10.rst
@@ -65,3 +65,7 @@ Fixes
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
index daef47dd2a..faf424cf09 100644
--- a/server/src/test/java/io/crate/analyze/TableInfoToASTTest.java
+++ b/server/src/test/java/io/crate/analyze/TableInfoToASTTest.java
@@ -391,4 +391,29 @@ public class TableInfoToASTTest extends CrateDummyClusterServiceUnitTest {
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
-- 
2.43.0


```
