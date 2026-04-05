# Phase 0 Inputs

- Mainline commit: 12169e594da08dde083bdacc28c35e3b7a520535
- Backport commit: 3b5050775d4457379150957ab11f4416aa668a4d
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 3

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java']
- Developer Java files: ['graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java']
- Overlap Java files: ['graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 12169e594da08dde083bdacc28c35e3b7a520535 Mon Sep 17 00:00:00 2001
From: Jan Heise <jan.heise@graylog.com>
Date: Tue, 30 Sep 2025 15:03:13 +0200
Subject: [PATCH] Adding support for `all time` in filter for paginated
 searches (#23789)

* adding support for all time

* adding changelog
---
 changelog/unreleased/pr-23789.toml              |  5 +++++
 .../filtering/inmemory/SingleFilterParser.java  |  5 ++++-
 .../inmemory/SingleFilterParserTest.java        | 17 +++++++++++++++++
 3 files changed, 26 insertions(+), 1 deletion(-)
 create mode 100644 changelog/unreleased/pr-23789.toml

diff --git a/changelog/unreleased/pr-23789.toml b/changelog/unreleased/pr-23789.toml
new file mode 100644
index 0000000000..a386edad0e
--- /dev/null
+++ b/changelog/unreleased/pr-23789.toml
@@ -0,0 +1,5 @@
+type = "f"
+message = "Fix search filters for 'Created At' and 'All time' in paginated searcheds."
+
+issues = ["23634"]
+pulls = ["23789"]
diff --git a/graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java b/graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java
index aa48167a93..5938bb4326 100644
--- a/graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java
+++ b/graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java
@@ -51,7 +51,10 @@ public class SingleFilterParser {
 
         final SearchQueryField.Type fieldType = attributeMetaData.type();
         if (isRangeValueExpression(valuePart, fieldType)) {
-            if (valuePart.startsWith(RANGE_VALUES_SEPARATOR)) {
+            if (valuePart.equals(RANGE_VALUES_SEPARATOR)) {
+                // could probably also return an empty BSON here, but just for consistency:
+                return new RangeFilter(attributeMetaData.id(), null, null);
+            } else if (valuePart.startsWith(RANGE_VALUES_SEPARATOR)) {
                 return new RangeFilter(attributeMetaData.id(),
                         null,
                         extractValue(fieldType, valuePart.substring(RANGE_VALUES_SEPARATOR.length()))
diff --git a/graylog2-server/src/test/java/org/graylog2/database/filtering/inmemory/SingleFilterParserTest.java b/graylog2-server/src/test/java/org/graylog2/database/filtering/inmemory/SingleFilterParserTest.java
index 1ce80cb3ff..52c1c56214 100644
--- a/graylog2-server/src/test/java/org/graylog2/database/filtering/inmemory/SingleFilterParserTest.java
+++ b/graylog2-server/src/test/java/org/graylog2/database/filtering/inmemory/SingleFilterParserTest.java
@@ -109,6 +109,23 @@ class SingleFilterParserTest {
                 ));
     }
 
+    @Test
+    void parsesFilterExpressionCorrectlyForAllTimeRange() {
+        final List<EntityAttribute> entityAttributes = List.of(EntityAttribute.builder()
+                .id("created_at")
+                .title("Creation Date")
+                .type(SearchQueryField.Type.DATE)
+                .filterable(true)
+                .build());
+
+        assertEquals(
+                new RangeFilter("created_at", null, null),
+
+                toTest.parseSingleExpression("created_at:" + RANGE_VALUES_SEPARATOR,
+                        entityAttributes
+                ));
+    }
+
     @Test
     void parsesFilterExpressionCorrectlyForDateRanges() {
         final String fromString = "2012-12-12 12:12:12";
-- 
2.43.0


```
