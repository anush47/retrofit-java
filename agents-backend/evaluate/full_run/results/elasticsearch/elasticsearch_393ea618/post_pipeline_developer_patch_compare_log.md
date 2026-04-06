# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java']
- Developer Java files: ['x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java']
- Overlap Java files: ['x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java']

## File State Comparison
- Compared files: ['x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java']
- Mismatched files: ['x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -858,7 +858,7 @@
         );
         chunksField.dynamic(ObjectMapper.Dynamic.FALSE);
         if (modelSettings != null) {
-            chunksField.add(createEmbeddingsField(indexSettings.getIndexVersionCreated(), modelSettings));
+            chunksField.add(createEmbeddingsField(indexSettings.getIndexVersionCreated(), modelSettings, useLegacyFormat));
         }
         if (useLegacyFormat) {
             var chunkTextField = new KeywordFieldMapper.Builder(TEXT_FIELD, indexVersionCreated).indexed(false).docValues(false);

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -858,7 +858,7 @@
-         );
-         chunksField.dynamic(ObjectMapper.Dynamic.FALSE);
-         if (modelSettings != null) {
--            chunksField.add(createEmbeddingsField(indexSettings.getIndexVersionCreated(), modelSettings));
-+            chunksField.add(createEmbeddingsField(indexSettings.getIndexVersionCreated(), modelSettings, useLegacyFormat));
-         }
-         if (useLegacyFormat) {
-             var chunkTextField = new KeywordFieldMapper.Builder(TEXT_FIELD, indexVersionCreated).indexed(false).docValues(false);
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -869,9 +869,13 @@
         return chunksField;
     }
 
-    private static Mapper.Builder createEmbeddingsField(IndexVersion indexVersionCreated, SemanticTextField.ModelSettings modelSettings) {
+    private static Mapper.Builder createEmbeddingsField(
+        IndexVersion indexVersionCreated,
+        SemanticTextField.ModelSettings modelSettings,
+        boolean useLegacyFormat
+    ) {
         return switch (modelSettings.taskType()) {
-            case SPARSE_EMBEDDING -> new SparseVectorFieldMapper.Builder(CHUNKED_EMBEDDINGS_FIELD).setStored(true);
+            case SPARSE_EMBEDDING -> new SparseVectorFieldMapper.Builder(CHUNKED_EMBEDDINGS_FIELD).setStored(useLegacyFormat == false);
             case TEXT_EMBEDDING -> {
                 DenseVectorFieldMapper.Builder denseVectorMapperBuilder = new DenseVectorFieldMapper.Builder(
                     CHUNKED_EMBEDDINGS_FIELD,

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,16 +1 @@-@@ -869,9 +869,13 @@
-         return chunksField;
-     }
- 
--    private static Mapper.Builder createEmbeddingsField(IndexVersion indexVersionCreated, SemanticTextField.ModelSettings modelSettings) {
-+    private static Mapper.Builder createEmbeddingsField(
-+        IndexVersion indexVersionCreated,
-+        SemanticTextField.ModelSettings modelSettings,
-+        boolean useLegacyFormat
-+    ) {
-         return switch (modelSettings.taskType()) {
--            case SPARSE_EMBEDDING -> new SparseVectorFieldMapper.Builder(CHUNKED_EMBEDDINGS_FIELD).setStored(true);
-+            case SPARSE_EMBEDDING -> new SparseVectorFieldMapper.Builder(CHUNKED_EMBEDDINGS_FIELD).setStored(useLegacyFormat == false);
-             case TEXT_EMBEDDING -> {
-                 DenseVectorFieldMapper.Builder denseVectorMapperBuilder = new DenseVectorFieldMapper.Builder(
-                     CHUNKED_EMBEDDINGS_FIELD,
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
diff --git a/x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java b/x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java
index 690a136c566..9126fd78cad 100644
--- a/x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java
+++ b/x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapper.java
@@ -858,7 +858,7 @@ public class SemanticTextFieldMapper extends FieldMapper implements InferenceFie
         );
         chunksField.dynamic(ObjectMapper.Dynamic.FALSE);
         if (modelSettings != null) {
-            chunksField.add(createEmbeddingsField(indexSettings.getIndexVersionCreated(), modelSettings));
+            chunksField.add(createEmbeddingsField(indexSettings.getIndexVersionCreated(), modelSettings, useLegacyFormat));
         }
         if (useLegacyFormat) {
             var chunkTextField = new KeywordFieldMapper.Builder(TEXT_FIELD, indexVersionCreated).indexed(false).docValues(false);
@@ -869,9 +869,13 @@ public class SemanticTextFieldMapper extends FieldMapper implements InferenceFie
         return chunksField;
     }
 
-    private static Mapper.Builder createEmbeddingsField(IndexVersion indexVersionCreated, SemanticTextField.ModelSettings modelSettings) {
+    private static Mapper.Builder createEmbeddingsField(
+        IndexVersion indexVersionCreated,
+        SemanticTextField.ModelSettings modelSettings,
+        boolean useLegacyFormat
+    ) {
         return switch (modelSettings.taskType()) {
-            case SPARSE_EMBEDDING -> new SparseVectorFieldMapper.Builder(CHUNKED_EMBEDDINGS_FIELD).setStored(true);
+            case SPARSE_EMBEDDING -> new SparseVectorFieldMapper.Builder(CHUNKED_EMBEDDINGS_FIELD).setStored(useLegacyFormat == false);
             case TEXT_EMBEDDING -> {
                 DenseVectorFieldMapper.Builder denseVectorMapperBuilder = new DenseVectorFieldMapper.Builder(
                     CHUNKED_EMBEDDINGS_FIELD,
diff --git a/x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapperTests.java b/x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapperTests.java
index ddc697881ec..857038439b0 100644
--- a/x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapperTests.java
+++ b/x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/mapper/SemanticTextFieldMapperTests.java
@@ -531,7 +531,11 @@ public class SemanticTextFieldMapperTests extends MapperTestCase {
             assertTrue(embeddingsFieldMapper.fieldType() == mapperService.mappingLookup().getFieldType(getEmbeddingsFieldName(fieldName)));
             assertThat(embeddingsMapper.fullPath(), equalTo(getEmbeddingsFieldName(fieldName)));
             switch (semanticFieldMapper.fieldType().getModelSettings().taskType()) {
-                case SPARSE_EMBEDDING -> assertThat(embeddingsMapper, instanceOf(SparseVectorFieldMapper.class));
+                case SPARSE_EMBEDDING -> {
+                    assertThat(embeddingsMapper, instanceOf(SparseVectorFieldMapper.class));
+                    SparseVectorFieldMapper sparseMapper = (SparseVectorFieldMapper) embeddingsMapper;
+                    assertEquals(sparseMapper.fieldType().isStored(), semanticTextFieldType.useLegacyFormat() == false);
+                }
                 case TEXT_EMBEDDING -> assertThat(embeddingsMapper, instanceOf(DenseVectorFieldMapper.class));
                 default -> throw new AssertionError("Invalid task type");
             }

```
