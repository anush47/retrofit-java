# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java']
- Developer Java files: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java']
- Overlap Java files: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java']

## File State Comparison
- Compared files: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java

- Developer hunks: 4
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -57,6 +57,7 @@
     static final NodeFeature FIX_PARSING_SUBOBJECTS_FALSE_DYNAMIC_FALSE = new NodeFeature(
         "mapper.fix_parsing_subobjects_false_dynamic_false"
     );
+    private static final String NOOP_FIELD_MAPPER_NAME = "no-op";
 
     private final XContentParserConfiguration parserConfiguration;
     private final MappingParserContext mappingParserContext;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -57,6 +57,7 @@
-     static final NodeFeature FIX_PARSING_SUBOBJECTS_FALSE_DYNAMIC_FALSE = new NodeFeature(
-         "mapper.fix_parsing_subobjects_false_dynamic_false"
-     );
-+    private static final String NOOP_FIELD_MAPPER_NAME = "no-op";
- 
-     private final XContentParserConfiguration parserConfiguration;
-     private final MappingParserContext mappingParserContext;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -706,6 +707,8 @@
 
             canRemoveSingleLeafElement = mapper instanceof FieldMapper
                 && mode == Mapper.SourceKeepMode.ARRAYS
+                && context.inArrayScope() == false
+                && mapper.leafName().equals(NOOP_FIELD_MAPPER_NAME) == false
                 && fieldWithFallbackSyntheticSource == false
                 && copyToFieldHasValuesInDocument == false;
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -706,6 +707,8 @@
- 
-             canRemoveSingleLeafElement = mapper instanceof FieldMapper
-                 && mode == Mapper.SourceKeepMode.ARRAYS
-+                && context.inArrayScope() == false
-+                && mapper.leafName().equals(NOOP_FIELD_MAPPER_NAME) == false
-                 && fieldWithFallbackSyntheticSource == false
-                 && copyToFieldHasValuesInDocument == false;
- 
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -729,20 +732,28 @@
 
         XContentParser parser = context.parser();
         XContentParser.Token token;
+        int elements = 0;
         while ((token = parser.nextToken()) != XContentParser.Token.END_ARRAY) {
             if (token == XContentParser.Token.START_OBJECT) {
+                elements = 2;
                 parseObject(context, lastFieldName);
             } else if (token == XContentParser.Token.START_ARRAY) {
+                elements = 2;
                 parseArray(context, lastFieldName);
             } else if (token == XContentParser.Token.VALUE_NULL) {
+                elements++;
                 parseNullValue(context, lastFieldName);
             } else if (token == null) {
                 throwEOFOnParseArray(arrayFieldName, context);
             } else {
                 assert token.isValue();
+                elements++;
                 parseValue(context, lastFieldName);
             }
         }
+        if (elements <= 1 && canRemoveSingleLeafElement) {
+            context.removeLastIgnoredField(fullPath);
+        }
         postProcessDynamicArrayMapping(context, lastFieldName);
     }
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,29 +1 @@-@@ -729,20 +732,28 @@
- 
-         XContentParser parser = context.parser();
-         XContentParser.Token token;
-+        int elements = 0;
-         while ((token = parser.nextToken()) != XContentParser.Token.END_ARRAY) {
-             if (token == XContentParser.Token.START_OBJECT) {
-+                elements = 2;
-                 parseObject(context, lastFieldName);
-             } else if (token == XContentParser.Token.START_ARRAY) {
-+                elements = 2;
-                 parseArray(context, lastFieldName);
-             } else if (token == XContentParser.Token.VALUE_NULL) {
-+                elements++;
-                 parseNullValue(context, lastFieldName);
-             } else if (token == null) {
-                 throwEOFOnParseArray(arrayFieldName, context);
-             } else {
-                 assert token.isValue();
-+                elements++;
-                 parseValue(context, lastFieldName);
-             }
-         }
-+        if (elements <= 1 && canRemoveSingleLeafElement) {
-+            context.removeLastIgnoredField(fullPath);
-+        }
-         postProcessDynamicArrayMapping(context, lastFieldName);
-     }
- 
+*No hunk*
```

#### Hunk 4

Developer
```diff
@@ -917,22 +928,26 @@
     }
 
     private static FieldMapper noopFieldMapper(String path) {
-        return new FieldMapper("no-op", new MappedFieldType("no-op", false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
-            @Override
-            public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
-                throw new UnsupportedOperationException();
-            }
+        return new FieldMapper(
+            NOOP_FIELD_MAPPER_NAME,
+            new MappedFieldType(NOOP_FIELD_MAPPER_NAME, false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
+                @Override
+                public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public String typeName() {
-                throw new UnsupportedOperationException();
-            }
+                @Override
+                public String typeName() {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public Query termQuery(Object value, SearchExecutionContext context) {
-                throw new UnsupportedOperationException();
-            }
-        }, FieldMapper.BuilderParams.empty()) {
+                @Override
+                public Query termQuery(Object value, SearchExecutionContext context) {
+                    throw new UnsupportedOperationException();
+                }
+            },
+            FieldMapper.BuilderParams.empty()
+        ) {
 
             @Override
             protected void parseCreateField(DocumentParserContext context) {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,41 +1 @@-@@ -917,22 +928,26 @@
-     }
- 
-     private static FieldMapper noopFieldMapper(String path) {
--        return new FieldMapper("no-op", new MappedFieldType("no-op", false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
--            @Override
--            public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
--                throw new UnsupportedOperationException();
--            }
-+        return new FieldMapper(
-+            NOOP_FIELD_MAPPER_NAME,
-+            new MappedFieldType(NOOP_FIELD_MAPPER_NAME, false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
-+                @Override
-+                public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
-+                    throw new UnsupportedOperationException();
-+                }
- 
--            @Override
--            public String typeName() {
--                throw new UnsupportedOperationException();
--            }
-+                @Override
-+                public String typeName() {
-+                    throw new UnsupportedOperationException();
-+                }
- 
--            @Override
--            public Query termQuery(Object value, SearchExecutionContext context) {
--                throw new UnsupportedOperationException();
--            }
--        }, FieldMapper.BuilderParams.empty()) {
-+                @Override
-+                public Query termQuery(Object value, SearchExecutionContext context) {
-+                    throw new UnsupportedOperationException();
-+                }
-+            },
-+            FieldMapper.BuilderParams.empty()
-+        ) {
- 
-             @Override
-             protected void parseCreateField(DocumentParserContext context) {
+*No hunk*
```


## Final Effective Hunk Comparison (agent + developer aux, code files)

### server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java

- Developer hunks: 4
- Generated hunks: 4

#### Hunk 1

Developer
```diff
@@ -57,6 +57,7 @@
     static final NodeFeature FIX_PARSING_SUBOBJECTS_FALSE_DYNAMIC_FALSE = new NodeFeature(
         "mapper.fix_parsing_subobjects_false_dynamic_false"
     );
+    private static final String NOOP_FIELD_MAPPER_NAME = "no-op";
 
     private final XContentParserConfiguration parserConfiguration;
     private final MappingParserContext mappingParserContext;

```

Generated
```diff
@@ -57,6 +57,7 @@
     static final NodeFeature FIX_PARSING_SUBOBJECTS_FALSE_DYNAMIC_FALSE = new NodeFeature(
         "mapper.fix_parsing_subobjects_false_dynamic_false"
     );
+    private static final String NOOP_FIELD_MAPPER_NAME = "no-op";
 
     private final XContentParserConfiguration parserConfiguration;
     private final MappingParserContext mappingParserContext;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -706,6 +707,8 @@
 
             canRemoveSingleLeafElement = mapper instanceof FieldMapper
                 && mode == Mapper.SourceKeepMode.ARRAYS
+                && context.inArrayScope() == false
+                && mapper.leafName().equals(NOOP_FIELD_MAPPER_NAME) == false
                 && fieldWithFallbackSyntheticSource == false
                 && copyToFieldHasValuesInDocument == false;
 

```

Generated
```diff
@@ -706,6 +707,8 @@
 
             canRemoveSingleLeafElement = mapper instanceof FieldMapper
                 && mode == Mapper.SourceKeepMode.ARRAYS
+                && context.inArrayScope() == false
+                && mapper.leafName().equals(NOOP_FIELD_MAPPER_NAME) == false
                 && fieldWithFallbackSyntheticSource == false
                 && copyToFieldHasValuesInDocument == false;
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 3

Developer
```diff
@@ -729,20 +732,28 @@
 
         XContentParser parser = context.parser();
         XContentParser.Token token;
+        int elements = 0;
         while ((token = parser.nextToken()) != XContentParser.Token.END_ARRAY) {
             if (token == XContentParser.Token.START_OBJECT) {
+                elements = 2;
                 parseObject(context, lastFieldName);
             } else if (token == XContentParser.Token.START_ARRAY) {
+                elements = 2;
                 parseArray(context, lastFieldName);
             } else if (token == XContentParser.Token.VALUE_NULL) {
+                elements++;
                 parseNullValue(context, lastFieldName);
             } else if (token == null) {
                 throwEOFOnParseArray(arrayFieldName, context);
             } else {
                 assert token.isValue();
+                elements++;
                 parseValue(context, lastFieldName);
             }
         }
+        if (elements <= 1 && canRemoveSingleLeafElement) {
+            context.removeLastIgnoredField(fullPath);
+        }
         postProcessDynamicArrayMapping(context, lastFieldName);
     }
 

```

Generated
```diff
@@ -729,20 +732,28 @@
 
         XContentParser parser = context.parser();
         XContentParser.Token token;
+        int elements = 0;
         while ((token = parser.nextToken()) != XContentParser.Token.END_ARRAY) {
             if (token == XContentParser.Token.START_OBJECT) {
+                elements = 2;
                 parseObject(context, lastFieldName);
             } else if (token == XContentParser.Token.START_ARRAY) {
+                elements = 2;
                 parseArray(context, lastFieldName);
             } else if (token == XContentParser.Token.VALUE_NULL) {
+                elements++;
                 parseNullValue(context, lastFieldName);
             } else if (token == null) {
                 throwEOFOnParseArray(arrayFieldName, context);
             } else {
                 assert token.isValue();
+                elements++;
                 parseValue(context, lastFieldName);
             }
         }
+        if (elements <= 1 && canRemoveSingleLeafElement) {
+            context.removeLastIgnoredField(fullPath);
+        }
         postProcessDynamicArrayMapping(context, lastFieldName);
     }
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 4

Developer
```diff
@@ -917,22 +928,26 @@
     }
 
     private static FieldMapper noopFieldMapper(String path) {
-        return new FieldMapper("no-op", new MappedFieldType("no-op", false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
-            @Override
-            public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
-                throw new UnsupportedOperationException();
-            }
+        return new FieldMapper(
+            NOOP_FIELD_MAPPER_NAME,
+            new MappedFieldType(NOOP_FIELD_MAPPER_NAME, false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
+                @Override
+                public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public String typeName() {
-                throw new UnsupportedOperationException();
-            }
+                @Override
+                public String typeName() {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public Query termQuery(Object value, SearchExecutionContext context) {
-                throw new UnsupportedOperationException();
-            }
-        }, FieldMapper.BuilderParams.empty()) {
+                @Override
+                public Query termQuery(Object value, SearchExecutionContext context) {
+                    throw new UnsupportedOperationException();
+                }
+            },
+            FieldMapper.BuilderParams.empty()
+        ) {
 
             @Override
             protected void parseCreateField(DocumentParserContext context) {

```

Generated
```diff
@@ -917,22 +928,26 @@
     }
 
     private static FieldMapper noopFieldMapper(String path) {
-        return new FieldMapper("no-op", new MappedFieldType("no-op", false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
-            @Override
-            public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
-                throw new UnsupportedOperationException();
-            }
+        return new FieldMapper(
+            NOOP_FIELD_MAPPER_NAME,
+            new MappedFieldType(NOOP_FIELD_MAPPER_NAME, false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
+                @Override
+                public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public String typeName() {
-                throw new UnsupportedOperationException();
-            }
+                @Override
+                public String typeName() {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public Query termQuery(Object value, SearchExecutionContext context) {
-                throw new UnsupportedOperationException();
-            }
-        }, FieldMapper.BuilderParams.empty()) {
+                @Override
+                public Query termQuery(Object value, SearchExecutionContext context) {
+                    throw new UnsupportedOperationException();
+                }
+            },
+            FieldMapper.BuilderParams.empty()
+        ) {
 
             @Override
             protected void parseCreateField(DocumentParserContext context) {

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
diff --git a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
--- a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
+++ b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
@@ -57,6 +57,7 @@
     static final NodeFeature FIX_PARSING_SUBOBJECTS_FALSE_DYNAMIC_FALSE = new NodeFeature(
         "mapper.fix_parsing_subobjects_false_dynamic_false"
     );
+    private static final String NOOP_FIELD_MAPPER_NAME = "no-op";
 
     private final XContentParserConfiguration parserConfiguration;
     private final MappingParserContext mappingParserContext;
@@ -706,6 +707,8 @@
 
             canRemoveSingleLeafElement = mapper instanceof FieldMapper
                 && mode == Mapper.SourceKeepMode.ARRAYS
+                && context.inArrayScope() == false
+                && mapper.leafName().equals(NOOP_FIELD_MAPPER_NAME) == false
                 && fieldWithFallbackSyntheticSource == false
                 && copyToFieldHasValuesInDocument == false;
 
@@ -729,20 +732,28 @@
 
         XContentParser parser = context.parser();
         XContentParser.Token token;
+        int elements = 0;
         while ((token = parser.nextToken()) != XContentParser.Token.END_ARRAY) {
             if (token == XContentParser.Token.START_OBJECT) {
+                elements = 2;
                 parseObject(context, lastFieldName);
             } else if (token == XContentParser.Token.START_ARRAY) {
+                elements = 2;
                 parseArray(context, lastFieldName);
             } else if (token == XContentParser.Token.VALUE_NULL) {
+                elements++;
                 parseNullValue(context, lastFieldName);
             } else if (token == null) {
                 throwEOFOnParseArray(arrayFieldName, context);
             } else {
                 assert token.isValue();
+                elements++;
                 parseValue(context, lastFieldName);
             }
         }
+        if (elements <= 1 && canRemoveSingleLeafElement) {
+            context.removeLastIgnoredField(fullPath);
+        }
         postProcessDynamicArrayMapping(context, lastFieldName);
     }
 
@@ -917,22 +928,26 @@
     }
 
     private static FieldMapper noopFieldMapper(String path) {
-        return new FieldMapper("no-op", new MappedFieldType("no-op", false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
-            @Override
-            public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
-                throw new UnsupportedOperationException();
-            }
+        return new FieldMapper(
+            NOOP_FIELD_MAPPER_NAME,
+            new MappedFieldType(NOOP_FIELD_MAPPER_NAME, false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
+                @Override
+                public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public String typeName() {
-                throw new UnsupportedOperationException();
-            }
+                @Override
+                public String typeName() {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public Query termQuery(Object value, SearchExecutionContext context) {
-                throw new UnsupportedOperationException();
-            }
-        }, FieldMapper.BuilderParams.empty()) {
+                @Override
+                public Query termQuery(Object value, SearchExecutionContext context) {
+                    throw new UnsupportedOperationException();
+                }
+            },
+            FieldMapper.BuilderParams.empty()
+        ) {
 
             @Override
             protected void parseCreateField(DocumentParserContext context) {

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
index e48c116cebf..e2d0b7efa6b 100644
--- a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
+++ b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
@@ -57,6 +57,7 @@ public final class DocumentParser {
     static final NodeFeature FIX_PARSING_SUBOBJECTS_FALSE_DYNAMIC_FALSE = new NodeFeature(
         "mapper.fix_parsing_subobjects_false_dynamic_false"
     );
+    private static final String NOOP_FIELD_MAPPER_NAME = "no-op";
 
     private final XContentParserConfiguration parserConfiguration;
     private final MappingParserContext mappingParserContext;
@@ -706,6 +707,8 @@ public final class DocumentParser {
 
             canRemoveSingleLeafElement = mapper instanceof FieldMapper
                 && mode == Mapper.SourceKeepMode.ARRAYS
+                && context.inArrayScope() == false
+                && mapper.leafName().equals(NOOP_FIELD_MAPPER_NAME) == false
                 && fieldWithFallbackSyntheticSource == false
                 && copyToFieldHasValuesInDocument == false;
 
@@ -729,20 +732,28 @@ public final class DocumentParser {
 
         XContentParser parser = context.parser();
         XContentParser.Token token;
+        int elements = 0;
         while ((token = parser.nextToken()) != XContentParser.Token.END_ARRAY) {
             if (token == XContentParser.Token.START_OBJECT) {
+                elements = 2;
                 parseObject(context, lastFieldName);
             } else if (token == XContentParser.Token.START_ARRAY) {
+                elements = 2;
                 parseArray(context, lastFieldName);
             } else if (token == XContentParser.Token.VALUE_NULL) {
+                elements++;
                 parseNullValue(context, lastFieldName);
             } else if (token == null) {
                 throwEOFOnParseArray(arrayFieldName, context);
             } else {
                 assert token.isValue();
+                elements++;
                 parseValue(context, lastFieldName);
             }
         }
+        if (elements <= 1 && canRemoveSingleLeafElement) {
+            context.removeLastIgnoredField(fullPath);
+        }
         postProcessDynamicArrayMapping(context, lastFieldName);
     }
 
@@ -917,22 +928,26 @@ public final class DocumentParser {
     }
 
     private static FieldMapper noopFieldMapper(String path) {
-        return new FieldMapper("no-op", new MappedFieldType("no-op", false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
-            @Override
-            public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
-                throw new UnsupportedOperationException();
-            }
+        return new FieldMapper(
+            NOOP_FIELD_MAPPER_NAME,
+            new MappedFieldType(NOOP_FIELD_MAPPER_NAME, false, false, false, TextSearchInfo.NONE, Collections.emptyMap()) {
+                @Override
+                public ValueFetcher valueFetcher(SearchExecutionContext context, String format) {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public String typeName() {
-                throw new UnsupportedOperationException();
-            }
+                @Override
+                public String typeName() {
+                    throw new UnsupportedOperationException();
+                }
 
-            @Override
-            public Query termQuery(Object value, SearchExecutionContext context) {
-                throw new UnsupportedOperationException();
-            }
-        }, FieldMapper.BuilderParams.empty()) {
+                @Override
+                public Query termQuery(Object value, SearchExecutionContext context) {
+                    throw new UnsupportedOperationException();
+                }
+            },
+            FieldMapper.BuilderParams.empty()
+        ) {
 
             @Override
             protected void parseCreateField(DocumentParserContext context) {
diff --git a/server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java b/server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java
index 2b36c0ce0b5..d12bf5dc2e3 100644
--- a/server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java
+++ b/server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java
@@ -743,7 +743,9 @@ public class IgnoredSourceFieldMapperTests extends MapperServiceTestCase {
             b.startObject("int_value").field("type", "integer").endObject();
         })).documentMapper();
         var syntheticSource = syntheticSource(documentMapper, b -> b.array("int_value", new int[] { 10 }));
-        assertEquals("{\"int_value\":[10]}", syntheticSource);
+        assertEquals("{\"int_value\":10}", syntheticSource);
+        ParsedDocument doc = documentMapper.parse(source(syntheticSource));
+        assertNull(doc.rootDoc().getField("_ignored_source"));
     }
 
     public void testIndexStoredArraySourceSingleLeafElementAndNull() throws IOException {
@@ -754,6 +756,23 @@ public class IgnoredSourceFieldMapperTests extends MapperServiceTestCase {
         assertEquals("{\"value\":[\"foo\",null]}", syntheticSource);
     }
 
+    public void testIndexStoredArraySourceSingleLeafElementInObjectArray() throws IOException {
+        DocumentMapper documentMapper = createMapperServiceWithStoredArraySource(mapping(b -> {
+            b.startObject("path").field("synthetic_source_keep", "none").startObject("properties");
+            {
+                b.startObject("int_value").field("type", "integer").endObject();
+            }
+            b.endObject().endObject();
+        })).documentMapper();
+        var syntheticSource = syntheticSource(documentMapper, b -> {
+            b.startArray("path");
+            b.startObject().field("int_value", 10).endObject();
+            b.startObject().array("int_value", new int[] { 20 }).endObject();
+            b.endArray();
+        });
+        assertEquals("{\"path\":{\"int_value\":[10,20]}}", syntheticSource);
+    }
+
     public void testIndexStoredArraySourceSingleObjectElement() throws IOException {
         DocumentMapper documentMapper = createMapperServiceWithStoredArraySource(mapping(b -> {
             b.startObject("path").startObject("properties");

```
