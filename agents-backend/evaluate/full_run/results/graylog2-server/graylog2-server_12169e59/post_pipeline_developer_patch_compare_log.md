# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java']
- Developer Java files: ['graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java']
- Overlap Java files: ['graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java']

## File State Comparison
- Compared files: ['graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -51,7 +51,10 @@
 
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

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,12 +1 @@-@@ -51,7 +51,10 @@
- 
-         final SearchQueryField.Type fieldType = attributeMetaData.type();
-         if (isRangeValueExpression(valuePart, fieldType)) {
--            if (valuePart.startsWith(RANGE_VALUES_SEPARATOR)) {
-+            if (valuePart.equals(RANGE_VALUES_SEPARATOR)) {
-+                // could probably also return an empty BSON here, but just for consistency:
-+                return new RangeFilter(attributeMetaData.id(), null, null);
-+            } else if (valuePart.startsWith(RANGE_VALUES_SEPARATOR)) {
-                 return new RangeFilter(attributeMetaData.id(),
-                         null,
-                         extractValue(fieldType, valuePart.substring(RANGE_VALUES_SEPARATOR.length()))
+*No hunk*
```


## Final Effective Hunk Comparison (agent + developer aux, code files)

### graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -51,7 +51,10 @@
 
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

```

Generated
```diff
@@ -51,7 +51,10 @@
 
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

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java b/graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java
--- a/graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java
+++ b/graylog2-server/src/main/java/org/graylog2/database/filtering/inmemory/SingleFilterParser.java
@@ -51,7 +51,10 @@
 
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

```
## Full Developer Backport Patch (full commit diff)
```diff
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
index 8fa9b26bdf..f1be66a862 100644
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

```
