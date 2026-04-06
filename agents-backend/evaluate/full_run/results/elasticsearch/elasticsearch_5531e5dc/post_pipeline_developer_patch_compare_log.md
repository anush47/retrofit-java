# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java', 'server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java']
- Developer Java files: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java', 'server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java']
- Overlap Java files: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java', 'server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java', 'server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java']

## File State Comparison
- Compared files: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java', 'server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java']
- Mismatched files: ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -824,8 +824,8 @@
 
         // In synthetic source, if any array element requires storing its source as-is, it takes precedence over
         // elements from regular source loading that are then skipped from the synthesized array source.
-        // To prevent this, we track each array name, to check if it contains any sub-arrays in its elements.
-        context = context.cloneForArray(fullPath);
+        // To prevent this, we track that parsing sub-context is within array scope.
+        context = context.maybeCloneForArray(mapper);
 
         XContentParser parser = context.parser();
         XContentParser.Token token;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,11 +1 @@-@@ -824,8 +824,8 @@
- 
-         // In synthetic source, if any array element requires storing its source as-is, it takes precedence over
-         // elements from regular source loading that are then skipped from the synthesized array source.
--        // To prevent this, we track each array name, to check if it contains any sub-arrays in its elements.
--        context = context.cloneForArray(fullPath);
-+        // To prevent this, we track that parsing sub-context is within array scope.
-+        context = context.maybeCloneForArray(mapper);
- 
-         XContentParser parser = context.parser();
-         XContentParser.Token token;
+*No hunk*
```


### server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java

- Developer hunks: 7
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -111,7 +111,7 @@
     private final Set<String> ignoredFields;
     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues;
     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsMissingValues;
-    private String parentArrayField;
+    private boolean inArrayScope;
 
     private final Map<String, List<Mapper>> dynamicMappers;
     private final DynamicMapperSize dynamicMappersSize;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -111,7 +111,7 @@
-     private final Set<String> ignoredFields;
-     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues;
-     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsMissingValues;
--    private String parentArrayField;
-+    private boolean inArrayScope;
- 
-     private final Map<String, List<Mapper>> dynamicMappers;
-     private final DynamicMapperSize dynamicMappersSize;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -143,7 +143,7 @@
         Set<String> ignoreFields,
         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues,
         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsWithNoSource,
-        String parentArrayField,
+        boolean inArrayScope,
         Map<String, List<Mapper>> dynamicMappers,
         Map<String, ObjectMapper> dynamicObjectMappers,
         Map<String, List<RuntimeField>> dynamicRuntimeFields,

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -143,7 +143,7 @@
-         Set<String> ignoreFields,
-         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues,
-         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsWithNoSource,
--        String parentArrayField,
-+        boolean inArrayScope,
-         Map<String, List<Mapper>> dynamicMappers,
-         Map<String, ObjectMapper> dynamicObjectMappers,
-         Map<String, List<RuntimeField>> dynamicRuntimeFields,
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -164,7 +164,7 @@
         this.ignoredFields = ignoreFields;
         this.ignoredFieldValues = ignoredFieldValues;
         this.ignoredFieldsMissingValues = ignoredFieldsWithNoSource;
-        this.parentArrayField = parentArrayField;
+        this.inArrayScope = inArrayScope;
         this.dynamicMappers = dynamicMappers;
         this.dynamicObjectMappers = dynamicObjectMappers;
         this.dynamicRuntimeFields = dynamicRuntimeFields;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -164,7 +164,7 @@
-         this.ignoredFields = ignoreFields;
-         this.ignoredFieldValues = ignoredFieldValues;
-         this.ignoredFieldsMissingValues = ignoredFieldsWithNoSource;
--        this.parentArrayField = parentArrayField;
-+        this.inArrayScope = inArrayScope;
-         this.dynamicMappers = dynamicMappers;
-         this.dynamicObjectMappers = dynamicObjectMappers;
-         this.dynamicRuntimeFields = dynamicRuntimeFields;
+*No hunk*
```

#### Hunk 4

Developer
```diff
@@ -188,7 +188,7 @@
             in.ignoredFields,
             in.ignoredFieldValues,
             in.ignoredFieldsMissingValues,
-            in.parentArrayField,
+            in.inArrayScope,
             in.dynamicMappers,
             in.dynamicObjectMappers,
             in.dynamicRuntimeFields,

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -188,7 +188,7 @@
-             in.ignoredFields,
-             in.ignoredFieldValues,
-             in.ignoredFieldsMissingValues,
--            in.parentArrayField,
-+            in.inArrayScope,
-             in.dynamicMappers,
-             in.dynamicObjectMappers,
-             in.dynamicRuntimeFields,
+*No hunk*
```

#### Hunk 5

Developer
```diff
@@ -219,7 +219,7 @@
             new HashSet<>(),
             new ArrayList<>(),
             new ArrayList<>(),
-            null,
+            false,
             new HashMap<>(),
             new HashMap<>(),
             new HashMap<>(),

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -219,7 +219,7 @@
-             new HashSet<>(),
-             new ArrayList<>(),
-             new ArrayList<>(),
--            null,
-+            false,
-             new HashMap<>(),
-             new HashMap<>(),
-             new HashMap<>(),
+*No hunk*
```

#### Hunk 6

Developer
```diff
@@ -324,10 +324,7 @@
     public final DocumentParserContext addIgnoredFieldFromContext(IgnoredSourceFieldMapper.NameValue ignoredFieldWithNoSource)
         throws IOException {
         if (canAddIgnoredField()) {
-            if (parentArrayField != null
-                && parent != null
-                && parentArrayField.equals(parent.fullPath())
-                && parent instanceof NestedObjectMapper == false) {
+            if (inArrayScope) {
                 // The field is an array within an array, store all sub-array elements.
                 ignoredFieldsMissingValues.add(ignoredFieldWithNoSource);
                 return cloneWithRecordedSource();

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,12 +1 @@-@@ -324,10 +324,7 @@
-     public final DocumentParserContext addIgnoredFieldFromContext(IgnoredSourceFieldMapper.NameValue ignoredFieldWithNoSource)
-         throws IOException {
-         if (canAddIgnoredField()) {
--            if (parentArrayField != null
--                && parent != null
--                && parentArrayField.equals(parent.fullPath())
--                && parent instanceof NestedObjectMapper == false) {
-+            if (inArrayScope) {
-                 // The field is an array within an array, store all sub-array elements.
-                 ignoredFieldsMissingValues.add(ignoredFieldWithNoSource);
-                 return cloneWithRecordedSource();
+*No hunk*
```

#### Hunk 7

Developer
```diff
@@ -364,14 +361,17 @@
     }
 
     /**
-     * Clones the current context to mark it as an array. Records the full name of the array field, to check for sub-arrays.
+     * Clones the current context to mark it as an array, if it's not already marked, or restore it if it's within a nested object.
      * Applies to synthetic source only.
      */
-    public final DocumentParserContext cloneForArray(String fullName) throws IOException {
-        if (canAddIgnoredField()) {
-            DocumentParserContext subcontext = switchParser(parser());
-            subcontext.parentArrayField = fullName;
-            return subcontext;
+    public final DocumentParserContext maybeCloneForArray(Mapper mapper) throws IOException {
+        if (canAddIgnoredField() && mapper instanceof ObjectMapper) {
+            boolean isNested = mapper instanceof NestedObjectMapper;
+            if ((inArrayScope == false && isNested == false) || (inArrayScope && isNested)) {
+                DocumentParserContext subcontext = switchParser(parser());
+                subcontext.inArrayScope = inArrayScope == false;
+                return subcontext;
+            }
         }
         return this;
     }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,24 +1 @@-@@ -364,14 +361,17 @@
-     }
- 
-     /**
--     * Clones the current context to mark it as an array. Records the full name of the array field, to check for sub-arrays.
-+     * Clones the current context to mark it as an array, if it's not already marked, or restore it if it's within a nested object.
-      * Applies to synthetic source only.
-      */
--    public final DocumentParserContext cloneForArray(String fullName) throws IOException {
--        if (canAddIgnoredField()) {
--            DocumentParserContext subcontext = switchParser(parser());
--            subcontext.parentArrayField = fullName;
--            return subcontext;
-+    public final DocumentParserContext maybeCloneForArray(Mapper mapper) throws IOException {
-+        if (canAddIgnoredField() && mapper instanceof ObjectMapper) {
-+            boolean isNested = mapper instanceof NestedObjectMapper;
-+            if ((inArrayScope == false && isNested == false) || (inArrayScope && isNested)) {
-+                DocumentParserContext subcontext = switchParser(parser());
-+                subcontext.inArrayScope = inArrayScope == false;
-+                return subcontext;
-+            }
-         }
-         return this;
-     }
+*No hunk*
```


## Final Effective Hunk Comparison (agent + developer aux, code files)

### server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -824,8 +824,8 @@
 
         // In synthetic source, if any array element requires storing its source as-is, it takes precedence over
         // elements from regular source loading that are then skipped from the synthesized array source.
-        // To prevent this, we track each array name, to check if it contains any sub-arrays in its elements.
-        context = context.cloneForArray(fullPath);
+        // To prevent this, we track that parsing sub-context is within array scope.
+        context = context.maybeCloneForArray(mapper);
 
         XContentParser parser = context.parser();
         XContentParser.Token token;

```

Generated
```diff
@@ -824,8 +824,8 @@
 
         // In synthetic source, if any array element requires storing its source as-is, it takes precedence over
         // elements from regular source loading that are then skipped from the synthesized array source.
-        // To prevent this, we track each array name, to check if it contains any sub-arrays in its elements.
-        context = context.cloneForArray(fullPath);
+        // To prevent this, we track that parsing sub-context is within array scope.
+        context = context.maybeCloneForArray(mapper);
 
         XContentParser parser = context.parser();
         XContentParser.Token token;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java

- Developer hunks: 7
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -111,7 +111,7 @@
     private final Set<String> ignoredFields;
     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues;
     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsMissingValues;
-    private String parentArrayField;
+    private boolean inArrayScope;
 
     private final Map<String, List<Mapper>> dynamicMappers;
     private final DynamicMapperSize dynamicMappersSize;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -111,7 +111,7 @@
-     private final Set<String> ignoredFields;
-     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues;
-     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsMissingValues;
--    private String parentArrayField;
-+    private boolean inArrayScope;
- 
-     private final Map<String, List<Mapper>> dynamicMappers;
-     private final DynamicMapperSize dynamicMappersSize;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -143,7 +143,7 @@
         Set<String> ignoreFields,
         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues,
         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsWithNoSource,
-        String parentArrayField,
+        boolean inArrayScope,
         Map<String, List<Mapper>> dynamicMappers,
         Map<String, ObjectMapper> dynamicObjectMappers,
         Map<String, List<RuntimeField>> dynamicRuntimeFields,

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -143,7 +143,7 @@
-         Set<String> ignoreFields,
-         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues,
-         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsWithNoSource,
--        String parentArrayField,
-+        boolean inArrayScope,
-         Map<String, List<Mapper>> dynamicMappers,
-         Map<String, ObjectMapper> dynamicObjectMappers,
-         Map<String, List<RuntimeField>> dynamicRuntimeFields,
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -164,7 +164,7 @@
         this.ignoredFields = ignoreFields;
         this.ignoredFieldValues = ignoredFieldValues;
         this.ignoredFieldsMissingValues = ignoredFieldsWithNoSource;
-        this.parentArrayField = parentArrayField;
+        this.inArrayScope = inArrayScope;
         this.dynamicMappers = dynamicMappers;
         this.dynamicObjectMappers = dynamicObjectMappers;
         this.dynamicRuntimeFields = dynamicRuntimeFields;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -164,7 +164,7 @@
-         this.ignoredFields = ignoreFields;
-         this.ignoredFieldValues = ignoredFieldValues;
-         this.ignoredFieldsMissingValues = ignoredFieldsWithNoSource;
--        this.parentArrayField = parentArrayField;
-+        this.inArrayScope = inArrayScope;
-         this.dynamicMappers = dynamicMappers;
-         this.dynamicObjectMappers = dynamicObjectMappers;
-         this.dynamicRuntimeFields = dynamicRuntimeFields;
+*No hunk*
```

#### Hunk 4

Developer
```diff
@@ -188,7 +188,7 @@
             in.ignoredFields,
             in.ignoredFieldValues,
             in.ignoredFieldsMissingValues,
-            in.parentArrayField,
+            in.inArrayScope,
             in.dynamicMappers,
             in.dynamicObjectMappers,
             in.dynamicRuntimeFields,

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -188,7 +188,7 @@
-             in.ignoredFields,
-             in.ignoredFieldValues,
-             in.ignoredFieldsMissingValues,
--            in.parentArrayField,
-+            in.inArrayScope,
-             in.dynamicMappers,
-             in.dynamicObjectMappers,
-             in.dynamicRuntimeFields,
+*No hunk*
```

#### Hunk 5

Developer
```diff
@@ -219,7 +219,7 @@
             new HashSet<>(),
             new ArrayList<>(),
             new ArrayList<>(),
-            null,
+            false,
             new HashMap<>(),
             new HashMap<>(),
             new HashMap<>(),

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -219,7 +219,7 @@
-             new HashSet<>(),
-             new ArrayList<>(),
-             new ArrayList<>(),
--            null,
-+            false,
-             new HashMap<>(),
-             new HashMap<>(),
-             new HashMap<>(),
+*No hunk*
```

#### Hunk 6

Developer
```diff
@@ -324,10 +324,7 @@
     public final DocumentParserContext addIgnoredFieldFromContext(IgnoredSourceFieldMapper.NameValue ignoredFieldWithNoSource)
         throws IOException {
         if (canAddIgnoredField()) {
-            if (parentArrayField != null
-                && parent != null
-                && parentArrayField.equals(parent.fullPath())
-                && parent instanceof NestedObjectMapper == false) {
+            if (inArrayScope) {
                 // The field is an array within an array, store all sub-array elements.
                 ignoredFieldsMissingValues.add(ignoredFieldWithNoSource);
                 return cloneWithRecordedSource();

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,12 +1 @@-@@ -324,10 +324,7 @@
-     public final DocumentParserContext addIgnoredFieldFromContext(IgnoredSourceFieldMapper.NameValue ignoredFieldWithNoSource)
-         throws IOException {
-         if (canAddIgnoredField()) {
--            if (parentArrayField != null
--                && parent != null
--                && parentArrayField.equals(parent.fullPath())
--                && parent instanceof NestedObjectMapper == false) {
-+            if (inArrayScope) {
-                 // The field is an array within an array, store all sub-array elements.
-                 ignoredFieldsMissingValues.add(ignoredFieldWithNoSource);
-                 return cloneWithRecordedSource();
+*No hunk*
```

#### Hunk 7

Developer
```diff
@@ -364,14 +361,17 @@
     }
 
     /**
-     * Clones the current context to mark it as an array. Records the full name of the array field, to check for sub-arrays.
+     * Clones the current context to mark it as an array, if it's not already marked, or restore it if it's within a nested object.
      * Applies to synthetic source only.
      */
-    public final DocumentParserContext cloneForArray(String fullName) throws IOException {
-        if (canAddIgnoredField()) {
-            DocumentParserContext subcontext = switchParser(parser());
-            subcontext.parentArrayField = fullName;
-            return subcontext;
+    public final DocumentParserContext maybeCloneForArray(Mapper mapper) throws IOException {
+        if (canAddIgnoredField() && mapper instanceof ObjectMapper) {
+            boolean isNested = mapper instanceof NestedObjectMapper;
+            if ((inArrayScope == false && isNested == false) || (inArrayScope && isNested)) {
+                DocumentParserContext subcontext = switchParser(parser());
+                subcontext.inArrayScope = inArrayScope == false;
+                return subcontext;
+            }
         }
         return this;
     }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,24 +1 @@-@@ -364,14 +361,17 @@
-     }
- 
-     /**
--     * Clones the current context to mark it as an array. Records the full name of the array field, to check for sub-arrays.
-+     * Clones the current context to mark it as an array, if it's not already marked, or restore it if it's within a nested object.
-      * Applies to synthetic source only.
-      */
--    public final DocumentParserContext cloneForArray(String fullName) throws IOException {
--        if (canAddIgnoredField()) {
--            DocumentParserContext subcontext = switchParser(parser());
--            subcontext.parentArrayField = fullName;
--            return subcontext;
-+    public final DocumentParserContext maybeCloneForArray(Mapper mapper) throws IOException {
-+        if (canAddIgnoredField() && mapper instanceof ObjectMapper) {
-+            boolean isNested = mapper instanceof NestedObjectMapper;
-+            if ((inArrayScope == false && isNested == false) || (inArrayScope && isNested)) {
-+                DocumentParserContext subcontext = switchParser(parser());
-+                subcontext.inArrayScope = inArrayScope == false;
-+                return subcontext;
-+            }
-         }
-         return this;
-     }
+*No hunk*
```



## Full Generated Patch (Agent-Only, code-only)
```diff

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
--- a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
+++ b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
@@ -824,8 +824,8 @@
 
         // In synthetic source, if any array element requires storing its source as-is, it takes precedence over
         // elements from regular source loading that are then skipped from the synthesized array source.
-        // To prevent this, we track each array name, to check if it contains any sub-arrays in its elements.
-        context = context.cloneForArray(fullPath);
+        // To prevent this, we track that parsing sub-context is within array scope.
+        context = context.maybeCloneForArray(mapper);
 
         XContentParser parser = context.parser();
         XContentParser.Token token;

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
index 0f957baccf8..39b6a5b4faf 100644
--- a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
+++ b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java
@@ -824,8 +824,8 @@ public final class DocumentParser {
 
         // In synthetic source, if any array element requires storing its source as-is, it takes precedence over
         // elements from regular source loading that are then skipped from the synthesized array source.
-        // To prevent this, we track each array name, to check if it contains any sub-arrays in its elements.
-        context = context.cloneForArray(fullPath);
+        // To prevent this, we track that parsing sub-context is within array scope.
+        context = context.maybeCloneForArray(mapper);
 
         XContentParser parser = context.parser();
         XContentParser.Token token;
diff --git a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java
index ac6999f3d79..eebe95e260d 100644
--- a/server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java
+++ b/server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java
@@ -111,7 +111,7 @@ public abstract class DocumentParserContext {
     private final Set<String> ignoredFields;
     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues;
     private final List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsMissingValues;
-    private String parentArrayField;
+    private boolean inArrayScope;
 
     private final Map<String, List<Mapper>> dynamicMappers;
     private final DynamicMapperSize dynamicMappersSize;
@@ -143,7 +143,7 @@ public abstract class DocumentParserContext {
         Set<String> ignoreFields,
         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldValues,
         List<IgnoredSourceFieldMapper.NameValue> ignoredFieldsWithNoSource,
-        String parentArrayField,
+        boolean inArrayScope,
         Map<String, List<Mapper>> dynamicMappers,
         Map<String, ObjectMapper> dynamicObjectMappers,
         Map<String, List<RuntimeField>> dynamicRuntimeFields,
@@ -164,7 +164,7 @@ public abstract class DocumentParserContext {
         this.ignoredFields = ignoreFields;
         this.ignoredFieldValues = ignoredFieldValues;
         this.ignoredFieldsMissingValues = ignoredFieldsWithNoSource;
-        this.parentArrayField = parentArrayField;
+        this.inArrayScope = inArrayScope;
         this.dynamicMappers = dynamicMappers;
         this.dynamicObjectMappers = dynamicObjectMappers;
         this.dynamicRuntimeFields = dynamicRuntimeFields;
@@ -188,7 +188,7 @@ public abstract class DocumentParserContext {
             in.ignoredFields,
             in.ignoredFieldValues,
             in.ignoredFieldsMissingValues,
-            in.parentArrayField,
+            in.inArrayScope,
             in.dynamicMappers,
             in.dynamicObjectMappers,
             in.dynamicRuntimeFields,
@@ -219,7 +219,7 @@ public abstract class DocumentParserContext {
             new HashSet<>(),
             new ArrayList<>(),
             new ArrayList<>(),
-            null,
+            false,
             new HashMap<>(),
             new HashMap<>(),
             new HashMap<>(),
@@ -324,10 +324,7 @@ public abstract class DocumentParserContext {
     public final DocumentParserContext addIgnoredFieldFromContext(IgnoredSourceFieldMapper.NameValue ignoredFieldWithNoSource)
         throws IOException {
         if (canAddIgnoredField()) {
-            if (parentArrayField != null
-                && parent != null
-                && parentArrayField.equals(parent.fullPath())
-                && parent instanceof NestedObjectMapper == false) {
+            if (inArrayScope) {
                 // The field is an array within an array, store all sub-array elements.
                 ignoredFieldsMissingValues.add(ignoredFieldWithNoSource);
                 return cloneWithRecordedSource();
@@ -364,14 +361,17 @@ public abstract class DocumentParserContext {
     }
 
     /**
-     * Clones the current context to mark it as an array. Records the full name of the array field, to check for sub-arrays.
+     * Clones the current context to mark it as an array, if it's not already marked, or restore it if it's within a nested object.
      * Applies to synthetic source only.
      */
-    public final DocumentParserContext cloneForArray(String fullName) throws IOException {
-        if (canAddIgnoredField()) {
-            DocumentParserContext subcontext = switchParser(parser());
-            subcontext.parentArrayField = fullName;
-            return subcontext;
+    public final DocumentParserContext maybeCloneForArray(Mapper mapper) throws IOException {
+        if (canAddIgnoredField() && mapper instanceof ObjectMapper) {
+            boolean isNested = mapper instanceof NestedObjectMapper;
+            if ((inArrayScope == false && isNested == false) || (inArrayScope && isNested)) {
+                DocumentParserContext subcontext = switchParser(parser());
+                subcontext.inArrayScope = inArrayScope == false;
+                return subcontext;
+            }
         }
         return this;
     }
diff --git a/server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java b/server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java
index 0e65d60d05d..8c65424fb85 100644
--- a/server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java
+++ b/server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java
@@ -964,6 +964,79 @@ public class IgnoredSourceFieldMapperTests extends MapperServiceTestCase {
             {"path":{"stored":[{"leaf":10},{"leaf":20}]}}""", syntheticSource);
     }
 
+    public void testDeeplyNestedObjectArrayAndValue() throws IOException {
+        DocumentMapper documentMapper = createMapperService(syntheticSourceMapping(b -> {
+            b.startObject("path").startObject("properties").startObject("to").startObject("properties");
+            {
+                b.startObject("stored");
+                {
+                    b.field("type", "object").field("store_array_source", true);
+                    b.startObject("properties").startObject("leaf").field("type", "integer").endObject().endObject();
+                }
+                b.endObject();
+            }
+            b.endObject().endObject().endObject().endObject();
+        })).documentMapper();
+        var syntheticSource = syntheticSource(documentMapper, b -> {
+            b.startArray("path");
+            {
+                b.startObject();
+                {
+                    b.startObject("to").startArray("stored");
+                    {
+                        b.startObject().field("leaf", 10).endObject();
+                    }
+                    b.endArray().endObject();
+                }
+                b.endObject();
+                b.startObject();
+                {
+                    b.startObject("to").startObject("stored").field("leaf", 20).endObject().endObject();
+                }
+                b.endObject();
+            }
+            b.endArray();
+        });
+        assertEquals("""
+            {"path":{"to":{"stored":[{"leaf":10},{"leaf":20}]}}}""", syntheticSource);
+    }
+
+    public void testObjectArrayAndValueInNestedObject() throws IOException {
+        DocumentMapper documentMapper = createMapperService(syntheticSourceMapping(b -> {
+            b.startObject("path").startObject("properties").startObject("to").startObject("properties");
+            {
+                b.startObject("stored");
+                {
+                    b.field("type", "nested").field("dynamic", false);
+                }
+                b.endObject();
+            }
+            b.endObject().endObject().endObject().endObject();
+        })).documentMapper();
+        var syntheticSource = syntheticSource(documentMapper, b -> {
+            b.startArray("path");
+            {
+                b.startObject();
+                {
+                    b.startObject("to").startArray("stored");
+                    {
+                        b.startObject().field("leaf", 10).endObject();
+                    }
+                    b.endArray().endObject();
+                }
+                b.endObject();
+                b.startObject();
+                {
+                    b.startObject("to").startObject("stored").field("leaf", 20).endObject().endObject();
+                }
+                b.endObject();
+            }
+            b.endArray();
+        });
+        assertEquals("""
+            {"path":{"to":{"stored":[{"leaf":10},{"leaf":20}]}}}""", syntheticSource);
+    }
+
     public void testObjectArrayAndValueDisabledObject() throws IOException {
         DocumentMapper documentMapper = createMapperService(syntheticSourceMapping(b -> {
             b.startObject("path").field("type", "object").startObject("properties");

```
