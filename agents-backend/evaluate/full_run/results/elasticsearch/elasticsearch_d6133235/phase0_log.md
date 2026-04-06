# Phase 0 Inputs

- Mainline commit: d6133235a339eb99a146a6ff3ad6958fe0d63cf6
- Backport commit: 1f572ad4d393cb5dae04467c33f293553ae1dacd
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 3

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexService.java']
- Developer Java files: ['server/src/main/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexService.java']
- Overlap Java files: ['server/src/main/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexService.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From d6133235a339eb99a146a6ff3ad6958fe0d63cf6 Mon Sep 17 00:00:00 2001
From: Craig Taverner <craig@amanzi.com>
Date: Mon, 13 Jan 2025 16:12:34 +0100
Subject: [PATCH] Add index name validation rule for empty index names
 (#119960)

* Add index name validation rule for empty index names

* Created negative tests for ES|QL index names with only exclusion character

* Added test for `*-`
---
 .../cluster/metadata/MetadataCreateIndexService.java      | 3 +++
 .../cluster/metadata/MetadataCreateIndexServiceTests.java | 3 +++
 .../xpack/esql/parser/AbstractStatementParserTests.java   | 8 ++++++--
 .../xpack/esql/parser/StatementParserTests.java           | 3 +++
 4 files changed, 15 insertions(+), 2 deletions(-)

diff --git a/server/src/main/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexService.java b/server/src/main/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexService.java
index 7fc8a8693dc..fb19a3f04fc 100644
--- a/server/src/main/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexService.java
+++ b/server/src/main/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexService.java
@@ -237,6 +237,9 @@ public class MetadataCreateIndexService {
      * Validate the name for an index or alias against some static rules.
      */
     public static void validateIndexOrAliasName(String index, BiFunction<String, String, ? extends RuntimeException> exceptionCtor) {
+        if (index == null || index.isEmpty()) {
+            throw exceptionCtor.apply(index, "must not be empty");
+        }
         if (Strings.validFileName(index) == false) {
             throw exceptionCtor.apply(index, "must not contain the following characters " + Strings.INVALID_FILENAME_CHARS);
         }
diff --git a/server/src/test/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexServiceTests.java b/server/src/test/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexServiceTests.java
index 3623683532c..3ed74392f74 100644
--- a/server/src/test/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexServiceTests.java
+++ b/server/src/test/java/org/elasticsearch/cluster/metadata/MetadataCreateIndexServiceTests.java
@@ -561,6 +561,9 @@ public class MetadataCreateIndexServiceTests extends ESTestCase {
             validateIndexName(checkerService, "..", "must not be '.' or '..'");
 
             validateIndexName(checkerService, "foo:bar", "must not contain ':'");
+
+            validateIndexName(checkerService, "", "must not be empty");
+            validateIndexName(checkerService, null, "must not be empty");
         }));
     }
 
diff --git a/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/AbstractStatementParserTests.java b/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/AbstractStatementParserTests.java
index e6fef186721..99a04b6ed8f 100644
--- a/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/AbstractStatementParserTests.java
+++ b/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/AbstractStatementParserTests.java
@@ -151,8 +151,12 @@ abstract class AbstractStatementParserTests extends ESTestCase {
         expectInvalidIndexNameErrorWithLineNumber(query, "\"" + indexString + "\"", lineNumber, indexString);
     }
 
-    void expectInvalidIndexNameErrorWithLineNumber(String query, String indexString, String lineNumber, String error) {
-        expectError(LoggerMessageFormat.format(null, query, indexString), lineNumber + "Invalid index name [" + error);
+    void expectInvalidIndexNameErrorWithLineNumber(String query, String indexString, String lineNumber, String name) {
+        expectError(LoggerMessageFormat.format(null, query, indexString), lineNumber + "Invalid index name [" + name);
+    }
+
+    void expectInvalidIndexNameErrorWithLineNumber(String query, String indexString, String lineNumber, String name, String error) {
+        expectError(LoggerMessageFormat.format(null, query, indexString), lineNumber + "Invalid index name [" + name + "], " + error);
     }
 
     void expectDateMathErrorWithLineNumber(String query, String arg, String lineNumber, String error) {
diff --git a/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/StatementParserTests.java b/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/StatementParserTests.java
index 49f03e9b8bc..a4712ae77b5 100644
--- a/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/StatementParserTests.java
+++ b/x-pack/plugin/esql/src/test/java/org/elasticsearch/xpack/esql/parser/StatementParserTests.java
@@ -578,6 +578,9 @@ public class StatementParserTests extends AbstractStatementParserTests {
             expectInvalidIndexNameErrorWithLineNumber(command, "indexpattern, --indexpattern", lineNumber, "-indexpattern");
             expectInvalidIndexNameErrorWithLineNumber(command, "indexpattern, \"--indexpattern\"", lineNumber, "-indexpattern");
             expectInvalidIndexNameErrorWithLineNumber(command, "\"indexpattern, --indexpattern\"", commands.get(command), "-indexpattern");
+            expectInvalidIndexNameErrorWithLineNumber(command, "\"- , -\"", commands.get(command), "", "must not be empty");
+            expectInvalidIndexNameErrorWithLineNumber(command, "\"indexpattern,-\"", commands.get(command), "", "must not be empty");
+            clustersAndIndices(command, "indexpattern", "*-");
             clustersAndIndices(command, "indexpattern", "-indexpattern");
         }
 
-- 
2.43.0


```
