# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java']
- Developer Java files: ['modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java']
- Overlap Java files: ['modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java']

## File State Comparison
- Compared files: ['modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java']
- Mismatched files: ['modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -11,7 +11,6 @@
 
 import org.apache.logging.log4j.LogManager;
 import org.apache.logging.log4j.Logger;
-import org.elasticsearch.ElasticsearchException;
 import org.elasticsearch.action.ActionListener;
 import org.elasticsearch.action.admin.indices.flush.FlushRequest;
 import org.elasticsearch.action.admin.indices.refresh.RefreshRequest;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -11,7 +11,6 @@
- 
- import org.apache.logging.log4j.LogManager;
- import org.apache.logging.log4j.Logger;
--import org.elasticsearch.ElasticsearchException;
- import org.elasticsearch.action.ActionListener;
- import org.elasticsearch.action.admin.indices.flush.FlushRequest;
- import org.elasticsearch.action.admin.indices.refresh.RefreshRequest;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -139,11 +138,18 @@
         if (geoipIndex != null) {
             logger.trace("The {} index is not null", GeoIpDownloader.DATABASES_INDEX);
             if (clusterState.getRoutingTable().index(geoipIndex.getWriteIndex()).allPrimaryShardsActive() == false) {
-                throw new ElasticsearchException("not all primary shards of [" + DATABASES_INDEX + "] index are active");
+                logger.debug(
+                    "Not updating geoip database because not all primary shards of the [" + DATABASES_INDEX + "] index are active."
+                );
+                return;
             }
             var blockException = clusterState.blocks().indexBlockedException(ClusterBlockLevel.WRITE, geoipIndex.getWriteIndex().getName());
             if (blockException != null) {
-                throw blockException;
+                logger.debug(
+                    "Not updating geoip database because there is a write block on the " + geoipIndex.getWriteIndex().getName() + " index",
+                    blockException
+                );
+                return;
             }
         }
         if (eagerDownloadSupplier.get() || atLeastOneGeoipProcessorSupplier.get()) {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,21 +1 @@-@@ -139,11 +138,18 @@
-         if (geoipIndex != null) {
-             logger.trace("The {} index is not null", GeoIpDownloader.DATABASES_INDEX);
-             if (clusterState.getRoutingTable().index(geoipIndex.getWriteIndex()).allPrimaryShardsActive() == false) {
--                throw new ElasticsearchException("not all primary shards of [" + DATABASES_INDEX + "] index are active");
-+                logger.debug(
-+                    "Not updating geoip database because not all primary shards of the [" + DATABASES_INDEX + "] index are active."
-+                );
-+                return;
-             }
-             var blockException = clusterState.blocks().indexBlockedException(ClusterBlockLevel.WRITE, geoipIndex.getWriteIndex().getName());
-             if (blockException != null) {
--                throw blockException;
-+                logger.debug(
-+                    "Not updating geoip database because there is a write block on the " + geoipIndex.getWriteIndex().getName() + " index",
-+                    blockException
-+                );
-+                return;
-             }
-         }
-         if (eagerDownloadSupplier.get() || atLeastOneGeoipProcessorSupplier.get()) {
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
diff --git a/docs/changelog/114924.yaml b/docs/changelog/114924.yaml
new file mode 100644
index 00000000000..536f446ef79
--- /dev/null
+++ b/docs/changelog/114924.yaml
@@ -0,0 +1,5 @@
+pr: 114924
+summary: Reducing error-level stack trace logging for normal events in `GeoIpDownloader`
+area: Ingest Node
+type: bug
+issues: []
diff --git a/modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java b/modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java
index dcaa8f6f2fb..ae562d3c735 100644
--- a/modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java
+++ b/modules/ingest-geoip/src/main/java/org/elasticsearch/ingest/geoip/GeoIpDownloader.java
@@ -11,7 +11,6 @@ package org.elasticsearch.ingest.geoip;
 
 import org.apache.logging.log4j.LogManager;
 import org.apache.logging.log4j.Logger;
-import org.elasticsearch.ElasticsearchException;
 import org.elasticsearch.action.ActionListener;
 import org.elasticsearch.action.admin.indices.flush.FlushRequest;
 import org.elasticsearch.action.admin.indices.refresh.RefreshRequest;
@@ -139,11 +138,18 @@ public class GeoIpDownloader extends AllocatedPersistentTask {
         if (geoipIndex != null) {
             logger.trace("The {} index is not null", GeoIpDownloader.DATABASES_INDEX);
             if (clusterState.getRoutingTable().index(geoipIndex.getWriteIndex()).allPrimaryShardsActive() == false) {
-                throw new ElasticsearchException("not all primary shards of [" + DATABASES_INDEX + "] index are active");
+                logger.debug(
+                    "Not updating geoip database because not all primary shards of the [" + DATABASES_INDEX + "] index are active."
+                );
+                return;
             }
             var blockException = clusterState.blocks().indexBlockedException(ClusterBlockLevel.WRITE, geoipIndex.getWriteIndex().getName());
             if (blockException != null) {
-                throw blockException;
+                logger.debug(
+                    "Not updating geoip database because there is a write block on the " + geoipIndex.getWriteIndex().getName() + " index",
+                    blockException
+                );
+                return;
             }
         }
         if (eagerDownloadSupplier.get() || atLeastOneGeoipProcessorSupplier.get()) {
diff --git a/modules/ingest-geoip/src/test/java/org/elasticsearch/ingest/geoip/GeoIpDownloaderTests.java b/modules/ingest-geoip/src/test/java/org/elasticsearch/ingest/geoip/GeoIpDownloaderTests.java
index e73f0a36cc6..56983287927 100644
--- a/modules/ingest-geoip/src/test/java/org/elasticsearch/ingest/geoip/GeoIpDownloaderTests.java
+++ b/modules/ingest-geoip/src/test/java/org/elasticsearch/ingest/geoip/GeoIpDownloaderTests.java
@@ -9,7 +9,6 @@
 
 package org.elasticsearch.ingest.geoip;
 
-import org.elasticsearch.ElasticsearchException;
 import org.elasticsearch.action.ActionListener;
 import org.elasticsearch.action.ActionRequest;
 import org.elasticsearch.action.ActionResponse;
@@ -25,11 +24,9 @@ import org.elasticsearch.action.index.IndexResponse;
 import org.elasticsearch.action.index.TransportIndexAction;
 import org.elasticsearch.action.support.broadcast.BroadcastResponse;
 import org.elasticsearch.cluster.ClusterState;
-import org.elasticsearch.cluster.block.ClusterBlockException;
 import org.elasticsearch.cluster.block.ClusterBlocks;
 import org.elasticsearch.cluster.metadata.IndexMetadata;
 import org.elasticsearch.cluster.service.ClusterService;
-import org.elasticsearch.common.ReferenceDocs;
 import org.elasticsearch.common.settings.ClusterSettings;
 import org.elasticsearch.common.settings.Settings;
 import org.elasticsearch.index.reindex.BulkByScrollResponse;
@@ -583,37 +580,28 @@ public class GeoIpDownloaderTests extends ESTestCase {
         assertFalse(it.hasNext());
     }
 
-    public void testUpdateDatabasesWriteBlock() {
+    public void testUpdateDatabasesWriteBlock() throws IOException {
+        /*
+         * Here we make sure that we bail out before making an httpClient request if there is write block on the .geoip_databases index
+         */
         ClusterState state = createClusterState(new PersistentTasksCustomMetadata(1L, Map.of()));
         var geoIpIndex = state.getMetadata().getIndicesLookup().get(GeoIpDownloader.DATABASES_INDEX).getWriteIndex().getName();
         state = ClusterState.builder(state)
             .blocks(new ClusterBlocks.Builder().addIndexBlock(geoIpIndex, IndexMetadata.INDEX_READ_ONLY_ALLOW_DELETE_BLOCK))
             .build();
         when(clusterService.state()).thenReturn(state);
-        var e = expectThrows(ClusterBlockException.class, () -> geoIpDownloader.updateDatabases());
-        assertThat(
-            e.getMessage(),
-            equalTo(
-                "index ["
-                    + geoIpIndex
-                    + "] blocked by: [TOO_MANY_REQUESTS/12/disk usage exceeded flood-stage watermark, "
-                    + "index has read-only-allow-delete block; for more information, see "
-                    + ReferenceDocs.FLOOD_STAGE_WATERMARK
-                    + "];"
-            )
-        );
+        geoIpDownloader.updateDatabases();
         verifyNoInteractions(httpClient);
     }
 
-    public void testUpdateDatabasesIndexNotReady() {
+    public void testUpdateDatabasesIndexNotReady() throws IOException {
+        /*
+         * Here we make sure that we bail out before making an httpClient request if there are unallocated shards on the .geoip_databases
+         * index
+         */
         ClusterState state = createClusterState(new PersistentTasksCustomMetadata(1L, Map.of()), true);
-        var geoIpIndex = state.getMetadata().getIndicesLookup().get(GeoIpDownloader.DATABASES_INDEX).getWriteIndex().getName();
-        state = ClusterState.builder(state)
-            .blocks(new ClusterBlocks.Builder().addIndexBlock(geoIpIndex, IndexMetadata.INDEX_READ_ONLY_ALLOW_DELETE_BLOCK))
-            .build();
         when(clusterService.state()).thenReturn(state);
-        var e = expectThrows(ElasticsearchException.class, () -> geoIpDownloader.updateDatabases());
-        assertThat(e.getMessage(), equalTo("not all primary shards of [.geoip_databases] index are active"));
+        geoIpDownloader.updateDatabases();
         verifyNoInteractions(httpClient);
     }
 

```
