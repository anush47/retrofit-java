# Full Trace of Agentic File Edits

## Attempt #1

### ReAct Agent Actions
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "center_line": 10,
  "radius": 20
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `find_method_definitions`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "symbol": "putRolloverInfos"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `find_method_definitions`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "symbol": "putRolloverInfos"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "center_line": 100,
  "radius": 20
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "center_line": 150,
  "radius": 20
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "center_line": 180,
  "radius": 20
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "center_line": 190,
  "radius": 20
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `edit_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "old_string": "        @Override\n        public boolean equals(Object o) {\n            if (this == o) return true;\n            if (o == null || getClass() != o.getClass()) return false;\n            Request request = (Request) o;\n            return Objects.equals(sourceIndex, request.sourceIndex)\n                && Objects.equals(destIndex, request.destIndex)\n                && Objects.equals(settingsOverride, request.settingsOverride)\n                && Objects.equals(mappingsOverride, request.mappingsOverride)\n                && removeIndexBlocks == request.removeIndexBlocks;\n\n        }",
  "new_string": "        @Override\n        public boolean equals(Object o) {\n            if (this == o) return true;\n            if (o == null || getClass() != o.getClass()) return false;\n            Request request = (Request) o;\n            return Objects.equals(sourceIndex, request.sourceIndex)\n                && Objects.equals(destIndex, request.destIndex)\n                && Objects.equals(settingsOverride, request.settingsOverride)\n                && Objects.equals(mappingsOverride, request.mappingsOverride)\n                && removeIndexBlocks == request.removeIndexBlocks;\n        }"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `insert_import`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "import_statement": "import org.elasticsearch.cluster.metadata.IndexMetadata;"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "center_line": 30,
  "radius": 20
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `edit_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "old_string": "import java.util.Objects;\n\npublic class CreateIndexFromSourceAction extends ActionType<AcknowledgedResponse> {\n",
  "new_string": "import java.util.Objects;\nimport org.elasticsearch.cluster.metadata.IndexMetadata;\n\npublic class CreateIndexFromSourceAction extends ActionType<AcknowledgedResponse> {\n"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `replace_method_body`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "method_signature": "public void fromXContent(XContentParser parser) throws IOException",
  "new_body": "        {\n            PARSER.parse(parser, this, null);\n        }"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `edit_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "old_string": "        public void fromXContent(XContentParser parser) throws IOException {\n            PARSER.parse(parser, this, null);\n        }",
  "new_string": "        public void fromXContent(XContentParser parser) throws IOException {\n            PARSER.parse(parser, this, null);\n        }"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "center_line": 50,
  "radius": 20
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `replace_method_body`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "method_signature": "public void fromXContent(XContentParser parser) throws IOException",
  "new_body": "        {\n            PARSER.parse(parser, this, null);\n        }"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `replace_method_body`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "method_signature": "public boolean equals(Object o)",
  "new_body": "        {\n            if (this == o) return true;\n            if (o == null || getClass() != o.getClass()) return false;\n            Request request = (Request) o;\n            return Objects.equals(sourceIndex, request.sourceIndex)\n                && Objects.equals(destIndex, request.destIndex)\n                && Objects.equals(settingsOverride, request.settingsOverride)\n                && Objects.equals(mappingsOverride, request.mappingsOverride)\n                && removeIndexBlocks == request.removeIndexBlocks;\n        }"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `grep_in_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "search_text": "equals"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `grep_in_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "search_text": "putRolloverInfos"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "center_line": 1,
  "radius": 20
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "center_line": 60,
  "radius": 20
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java**: Called `edit_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java",
  "old_string": "    public static class Request extends ActionRequest implements IndicesRequest, ToXContent {\n        private final String sourceIndex;\n        private final String destIndex;\n        private Settings settingsOverride;\n        private Map<String, Object> mappingsOverride;\n        private boolean removeIndexBlocks;\n        private static final ParseField SETTINGS_OVERRIDE_FIELD = new ParseField(\"settings_override\");\n        private static final ParseField MAPPINGS_OVERRIDE_FIELD = new ParseField(\"mappings_override\");\n        private static final ParseField REMOVE_INDEX_BLOCKS_FIELD = new ParseField(\"remove_index_blocks\");\n        private static final ObjectParser<Request, Void> PARSER = new ObjectParser<>(\"create_index_from_source_request\");\n\n        static {\n            PARSER.declareField(\n                (parser, request, context) -> request.settingsOverride(Settings.fromXContent(parser)),\n                SETTINGS_OVERRIDE_FIELD,\n                ObjectParser.ValueType.OBJECT\n            );\n            PARSER.declareField(\n                (parser, request, context) -> request.mappingsOverride(Map.of(\"_doc\", parser.map())),\n                MAPPINGS_OVERRIDE_FIELD,\n                ObjectParser.ValueType.OBJECT\n            );\n            PARSER.declareField(\n                (parser, request, context) -> request.removeIndexBlocks(parser.booleanValue()),\n                REMOVE_INDEX_BLOCKS_FIELD,\n                ObjectParser.ValueType.BOOLEAN\n            );\n        }",
  "new_string": "    public static class Request extends ActionRequest implements IndicesRequest, ToXContent {\n        private final String sourceIndex;\n        private final String destIndex;\n        private Settings settingsOverride;\n        private Map<String, Object> mappingsOverride;\n        private boolean removeIndexBlocks;\n        private static final ParseField SETTINGS_OVERRIDE_FIELD = new ParseField(\"settings_override\");\n        private static final ParseField MAPPINGS_OVERRIDE_FIELD = new ParseField(\"mappings_override\");\n        private static final ParseField REMOVE_INDEX_BLOCKS_FIELD = new ParseField(\"remove_index_blocks\");\n        private static final ObjectParser<Request, Void> PARSER = new ObjectParser<>(\"create_index_from_source_request\");\n\n        static {\n            PARSER.declareField(\n                (parser, request, context) -> request.settingsOverride(Settings.fromXContent(parser)),\n                SETTINGS_OVERRIDE_FIELD,\n                ObjectParser.ValueType.OBJECT\n            );\n            PARSER.declareField(\n                (parser, request, context) -> request.mappingsOverride(Map.of(\"_doc\", parser.map())),\n                MAPPINGS_OVERRIDE_FIELD,\n                ObjectParser.ValueType.OBJECT\n            );\n            PARSER.declareField(\n                (parser, request, context) -> request.removeIndexBlocks(parser.booleanValue()),\n                REMOVE_INDEX_BLOCKS_FIELD,\n                ObjectParser.ValueType.BOOLEAN\n            );\n        }\n\n        public Request(String sourceIndex, String destIndex) {\n            this(sourceIndex, destIndex, Settings.EMPTY, Map.of(), true);\n        }\n\n        public Request(\n            String sourceIndex,\n            String destIndex,\n            Settings settingsOverride,\n            Map<String, Object> mappingsOverride,\n            boolean removeIndexBlocks\n        ) {\n            Objects.requireNonNull(settingsOverride);\n            Objects.requireNonNull(mappingsOverride);\n            this.sourceIndex = sourceIndex;\n            this.destIndex = destIndex;\n            this.settingsOverride = settingsOverride;\n            this.mappingsOverride = mappingsOverride;\n            this.removeIndexBlocks = removeIndexBlocks;\n        }"
}
```
- **x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java",
  "center_line": 1,
  "radius": 20
}
```
- **x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java**: Called `find_method_definitions`
```json
{
  "file_path": "x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java",
  "symbol": "putRolloverInfos"
}
```
- **x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java**: Called `find_method_definitions`
```json
{
  "file_path": "x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java",
  "symbol": "putRolloverInfos"
}
```
- **x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java**: Called `grep_in_file`
```json
{
  "file_path": "x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java",
  "search_text": "putRolloverInfos"
}
```
- **x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java**: Called `find_method_definitions`
```json
{
  "file_path": "x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java",
  "limit": 20
}
```
- **x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java",
  "center_line": 90,
  "radius": 20
}
```

### Final Output Diff
**server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java** [replace]
```java
// --- OLD ---
<developer patch fast path>
// --- NEW ---
diff --git a/server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java b/server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java
index ae4b16b0886..33dd20c50e1 100644
--- a/server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java
+++ b/server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java
@@ -2122,6 +2122,12 @@ public class IndexMetadata implements Diffable<IndexMetadata>, ToXContentFragmen
             return this;
         }
 
+        public Builder putRolloverInfos(Map<String, RolloverInfo> rolloverInfos) {
+            this.rolloverInfos.clear();
+            this.rolloverInfos.putAllFromMap(rolloverInfos);
+            return this;
+        }
+
         public long version() {
             return this.version;
         }
```
**x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java** [replace]
```java
// --- OLD ---
<developer patch fast path>
// --- NEW ---
diff --git a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java
index 587d10292ca..534671cc3d6 100644
--- a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java
+++ b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java
@@ -208,6 +208,7 @@ public class InternalUsers {
                         TransportDeleteIndexAction.TYPE.name(),
                         "indices:admin/data_stream/index/reindex",
                         "indices:admin/index/create_from_source",
+                        "indices:admin/index/copy_lifecycle_index_metadata",
                         TransportAddIndexBlockAction.TYPE.name(),
                         OpenIndexAction.NAME,
                         TransportCloseIndexAction.NAME,
```
**x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java** [replace]
```java
// --- OLD ---
<developer patch fast path>
// --- NEW ---
diff --git a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java
index 7811e84ac9f..0c2f7e56129 100644
--- a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java
+++ b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java
@@ -36,6 +36,8 @@ import org.elasticsearch.xcontent.NamedXContentRegistry;
 import org.elasticsearch.xcontent.ParseField;
 import org.elasticsearch.xpack.migrate.action.CancelReindexDataStreamAction;
 import org.elasticsearch.xpack.migrate.action.CancelReindexDataStreamTransportAction;
+import org.elasticsearch.xpack.migrate.action.CopyLifecycleIndexMetadataAction;
+import org.elasticsearch.xpack.migrate.action.CopyLifecycleIndexMetadataTransportAction;
 import org.elasticsearch.xpack.migrate.action.CreateIndexFromSourceAction;
 import org.elasticsearch.xpack.migrate.action.CreateIndexFromSourceTransportAction;
 import org.elasticsearch.xpack.migrate.action.GetMigrationReindexStatusAction;
@@ -106,6 +108,7 @@ public class MigratePlugin extends Plugin implements ActionPlugin, PersistentTas
         actions.add(new ActionHandler<>(CancelReindexDataStreamAction.INSTANCE, CancelReindexDataStreamTransportAction.class));
         actions.add(new ActionHandler<>(ReindexDataStreamIndexAction.INSTANCE, ReindexDataStreamIndexTransportAction.class));
         actions.add(new ActionHandler<>(CreateIndexFromSourceAction.INSTANCE, CreateIndexFromSourceTransportAction.class));
+        actions.add(new ActionHandler<>(CopyLifecycleIndexMetadataAction.INSTANCE, CopyLifecycleIndexMetadataTransportAction.class));
         return actions;
     }
```
**x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java** [replace]
```diff
diff --git a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java
index 5ab009decd3..676cf943544 100644
--- a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java
+++ b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/CreateIndexFromSourceAction.java
@@ -27,6 +27,7 @@ import org.elasticsearch.xcontent.XContentParser;
 import java.io.IOException;
 import java.util.Map;
 import java.util.Objects;
+import org.elasticsearch.cluster.metadata.IndexMetadata;
 
 public class CreateIndexFromSourceAction extends ActionType<AcknowledgedResponse> {
 
@@ -87,6 +88,26 @@ public class CreateIndexFromSourceAction extends ActionType<AcknowledgedResponse
             this.removeIndexBlocks = removeIndexBlocks;
         }
 
+        public Request(String sourceIndex, String destIndex) {
+            this(sourceIndex, destIndex, Settings.EMPTY, Map.of(), true);
+        }
+
+        public Request(
+            String sourceIndex,
+            String destIndex,
+            Settings settingsOverride,
+            Map<String, Object> mappingsOverride,
+            boolean removeIndexBlocks
+        ) {
+            Objects.requireNonNull(settingsOverride);
+            Objects.requireNonNull(mappingsOverride);
+            this.sourceIndex = sourceIndex;
+            this.destIndex = destIndex;
+            this.settingsOverride = settingsOverride;
+            this.mappingsOverride = mappingsOverride;
+            this.removeIndexBlocks = removeIndexBlocks;
+        }
+
         @SuppressWarnings("unchecked")
         public Request(StreamInput in) throws IOException {
             super(in);
@@ -177,7 +198,6 @@ public class CreateIndexFromSourceAction extends ActionType<AcknowledgedResponse
                 && Objects.equals(settingsOverride, request.settingsOverride)
                 && Objects.equals(mappingsOverride, request.mappingsOverride)
                 && removeIndexBlocks == request.removeIndexBlocks;
-
         }
 
         @Override
```
**x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java** [replace]
```java
// --- OLD ---
<developer patch fast path>
// --- NEW ---
diff --git a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java
index b5edfc198e3..5ffcc98255b 100644
--- a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java
+++ b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java
@@ -168,6 +168,7 @@ public class ReindexDataStreamIndexTransportAction extends HandledTransportActio
             .<AcknowledgedResponse>andThen(l -> createIndex(sourceIndex, destIndexName, l, taskId))
             .<BulkByScrollResponse>andThen(l -> reindex(sourceIndexName, destIndexName, l, taskId))
             .<AcknowledgedResponse>andThen(l -> copyOldSourceSettingsToDest(settingsBefore, destIndexName, l, taskId))
+            .<AcknowledgedResponse>andThen(l -> copyIndexMetadataToDest(sourceIndexName, destIndexName, l, taskId))
             .<AcknowledgedResponse>andThen(l -> sanityCheck(sourceIndexName, destIndexName, l, taskId))
             .<CloseIndexResponse>andThen(l -> closeIndexIfWasClosed(destIndexName, wasClosed, l, taskId))
             .andThenApply(ignored -> new ReindexDataStreamIndexAction.Response(destIndexName))
@@ -355,6 +356,24 @@ public class ReindexDataStreamIndexTransportAction extends HandledTransportActio
         updateSettings(destIndexName, settings, listener, parentTaskId);
     }
 
+    private void copyIndexMetadataToDest(
+        String sourceIndexName,
+        String destIndexName,
+        ActionListener<AcknowledgedResponse> listener,
+        TaskId parentTaskId
+    ) {
+        logger.debug("Copying index metadata to destination index [{}] from source index [{}]", destIndexName, sourceIndexName);
+        var request = new CopyLifecycleIndexMetadataAction.Request(TimeValue.MAX_VALUE, sourceIndexName, destIndexName);
+        request.setParentTask(parentTaskId);
+        var errorMessage = String.format(
+            Locale.ROOT,
+            "Failed to acknowledge copying index metadata from source [%s] to dest [%s]",
+            sourceIndexName,
+            destIndexName
+        );
+        client.execute(CopyLifecycleIndexMetadataAction.INSTANCE, request, failIfNotAcknowledged(listener, errorMessage));
+    }
+
     private static void copySettingOrUnset(Settings settingsBefore, Settings.Builder builder, String setting) {
         // if setting was explicitly added to the source index
         if (settingsBefore.get(setting) != null) {
```

## Attempt #2

### ReAct Agent Actions
- **x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java",
  "center_line": 20,
  "radius": 20
}
```
- **x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java",
  "center_line": 80,
  "radius": 20
}
```
- **x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java**: Called `read_file_window`
```json
{
  "file_path": "x-pack/plugin/ml/src/main/java/org/elasticsearch/xpack/ml/action/TransportUpdateModelSnapshotAction.java",
  "center_line": 120,
  "radius": 20
}
```

### Final Output Diff

## Attempt #3

### ReAct Agent Actions
- **server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java**: Called `str_replace_in_file`
```json
{
  "file_path": "server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java",
  "edit_type": "insert_before",
  "resolution_reason": "exact",
  "resolved_old_preview": "        public long version() {",
  "resolved_new_preview": "        public Builder putRolloverInfos(Map<String, RolloverInfo> rolloverInfos) {\n            this.rolloverInfos.clear();\n            this.rolloverInfos.putAllFromMap(rolloverInfos);\n            retu"
}
```
- **x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java**: Called `str_replace_in_file`
```json
{
  "file_path": "x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java",
  "edit_type": "insert_before",
  "resolution_reason": "exact",
  "resolved_old_preview": "                        TransportAddIndexBlockAction.TYPE.name(),",
  "resolved_new_preview": "                        \"indices:admin/index/copy_lifecycle_index_metadata\",\n                        TransportAddIndexBlockAction.TYPE.name(),"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java**: Called `str_replace_in_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java",
  "edit_type": "insert_before",
  "resolution_reason": "exact",
  "resolved_old_preview": "import org.elasticsearch.xpack.migrate.action.CreateIndexFromSourceAction;",
  "resolved_new_preview": "import org.elasticsearch.xpack.migrate.action.CopyLifecycleIndexMetadataAction;\nimport org.elasticsearch.xpack.migrate.action.CopyLifecycleIndexMetadataTransportAction;\nimport org.elasticsearch.xpack."
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java**: Called `str_replace_in_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java",
  "edit_type": "insert_before",
  "resolution_reason": "exact",
  "resolved_old_preview": "        return actions;",
  "resolved_new_preview": "        actions.add(new ActionHandler<>(CopyLifecycleIndexMetadataAction.INSTANCE, CopyLifecycleIndexMetadataTransportAction.class));\n        return actions;"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java**: Called `str_replace_in_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java",
  "edit_type": "insert_before",
  "resolution_reason": "exact",
  "resolved_old_preview": "            .<AcknowledgedResponse>andThen(l -> sanityCheck(sourceIndexName, destIndexName, l, taskId))",
  "resolved_new_preview": "            .<AcknowledgedResponse>andThen(l -> copyIndexMetadataToDest(sourceIndexName, destIndexName, l, taskId))\n            .<AcknowledgedResponse>andThen(l -> sanityCheck(sourceIndexName, destInd"
}
```
- **x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java**: Called `str_replace_in_file`
```json
{
  "file_path": "x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java",
  "edit_type": "insert_before",
  "resolution_reason": "exact",
  "resolved_old_preview": "    private static void copySettingOrUnset(Settings settingsBefore, Settings.Builder builder, String setting) {",
  "resolved_new_preview": "    private void copyIndexMetadataToDest(\n        String sourceIndexName,\n        String destIndexName,\n        ActionListener<AcknowledgedResponse> listener,\n        TaskId parentTaskId\n    ) {\n     "
}
```

### Final Output Diff
**server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java** [replace]
```java
// --- OLD ---
<deterministic file-editor diff>
// --- NEW ---
diff --git a/server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java b/server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java
index ae4b16b0886..33dd20c50e1 100644
--- a/server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java
+++ b/server/src/main/java/org/elasticsearch/cluster/metadata/IndexMetadata.java
@@ -2122,6 +2122,12 @@ public class IndexMetadata implements Diffable<IndexMetadata>, ToXContentFragmen
             return this;
         }
 
+        public Builder putRolloverInfos(Map<String, RolloverInfo> rolloverInfos) {
+            this.rolloverInfos.clear();
+            this.rolloverInfos.putAllFromMap(rolloverInfos);
+            return this;
+        }
+
         public long version() {
             return this.version;
         }
```
**x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java** [replace]
```java
// --- OLD ---
<deterministic file-editor diff>
// --- NEW ---
diff --git a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java
index 587d10292ca..534671cc3d6 100644
--- a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java
+++ b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/security/user/InternalUsers.java
@@ -208,6 +208,7 @@ public class InternalUsers {
                         TransportDeleteIndexAction.TYPE.name(),
                         "indices:admin/data_stream/index/reindex",
                         "indices:admin/index/create_from_source",
+                        "indices:admin/index/copy_lifecycle_index_metadata",
                         TransportAddIndexBlockAction.TYPE.name(),
                         OpenIndexAction.NAME,
                         TransportCloseIndexAction.NAME,
```
**x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java** [replace]
```java
// --- OLD ---
<deterministic file-editor diff>
// --- NEW ---
diff --git a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java
index 7811e84ac9f..0c2f7e56129 100644
--- a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java
+++ b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java
@@ -36,6 +36,8 @@ import org.elasticsearch.xcontent.NamedXContentRegistry;
 import org.elasticsearch.xcontent.ParseField;
 import org.elasticsearch.xpack.migrate.action.CancelReindexDataStreamAction;
 import org.elasticsearch.xpack.migrate.action.CancelReindexDataStreamTransportAction;
+import org.elasticsearch.xpack.migrate.action.CopyLifecycleIndexMetadataAction;
+import org.elasticsearch.xpack.migrate.action.CopyLifecycleIndexMetadataTransportAction;
 import org.elasticsearch.xpack.migrate.action.CreateIndexFromSourceAction;
 import org.elasticsearch.xpack.migrate.action.CreateIndexFromSourceTransportAction;
 import org.elasticsearch.xpack.migrate.action.GetMigrationReindexStatusAction;
@@ -106,6 +108,7 @@ public class MigratePlugin extends Plugin implements ActionPlugin, PersistentTas
         actions.add(new ActionHandler<>(CancelReindexDataStreamAction.INSTANCE, CancelReindexDataStreamTransportAction.class));
         actions.add(new ActionHandler<>(ReindexDataStreamIndexAction.INSTANCE, ReindexDataStreamIndexTransportAction.class));
         actions.add(new ActionHandler<>(CreateIndexFromSourceAction.INSTANCE, CreateIndexFromSourceTransportAction.class));
+        actions.add(new ActionHandler<>(CopyLifecycleIndexMetadataAction.INSTANCE, CopyLifecycleIndexMetadataTransportAction.class));
         return actions;
     }
```
**x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java** [replace]
```java
// --- OLD ---
<deterministic file-editor diff>
// --- NEW ---
diff --git a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java
index b5edfc198e3..5ffcc98255b 100644
--- a/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java
+++ b/x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java
@@ -168,6 +168,7 @@ public class ReindexDataStreamIndexTransportAction extends HandledTransportActio
             .<AcknowledgedResponse>andThen(l -> createIndex(sourceIndex, destIndexName, l, taskId))
             .<BulkByScrollResponse>andThen(l -> reindex(sourceIndexName, destIndexName, l, taskId))
             .<AcknowledgedResponse>andThen(l -> copyOldSourceSettingsToDest(settingsBefore, destIndexName, l, taskId))
+            .<AcknowledgedResponse>andThen(l -> copyIndexMetadataToDest(sourceIndexName, destIndexName, l, taskId))
             .<AcknowledgedResponse>andThen(l -> sanityCheck(sourceIndexName, destIndexName, l, taskId))
             .<CloseIndexResponse>andThen(l -> closeIndexIfWasClosed(destIndexName, wasClosed, l, taskId))
             .andThenApply(ignored -> new ReindexDataStreamIndexAction.Response(destIndexName))
@@ -355,6 +356,24 @@ public class ReindexDataStreamIndexTransportAction extends HandledTransportActio
         updateSettings(destIndexName, settings, listener, parentTaskId);
     }
 
+    private void copyIndexMetadataToDest(
+        String sourceIndexName,
+        String destIndexName,
+        ActionListener<AcknowledgedResponse> listener,
+        TaskId parentTaskId
+    ) {
+        logger.debug("Copying index metadata to destination index [{}] from source index [{}]", destIndexName, sourceIndexName);
+        var request = new CopyLifecycleIndexMetadataAction.Request(TimeValue.MAX_VALUE, sourceIndexName, destIndexName);
+        request.setParentTask(parentTaskId);
+        var errorMessage = String.format(
+            Locale.ROOT,
+            "Failed to acknowledge copying index metadata from source [%s] to dest [%s]",
+            sourceIndexName,
+            destIndexName
+        );
+        client.execute(CopyLifecycleIndexMetadataAction.INSTANCE, request, failIfNotAcknowledged(listener, errorMessage));
+    }
+
     private static void copySettingOrUnset(Settings settingsBefore, Settings.Builder builder, String setting) {
         // if setting was explicitly added to the source index
         if (settingsBefore.get(setting) != null) {
```