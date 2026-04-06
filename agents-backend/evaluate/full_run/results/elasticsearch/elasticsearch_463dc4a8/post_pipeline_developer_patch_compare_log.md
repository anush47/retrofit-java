# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java', 'x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java']
- Developer Java files: ['x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java', 'x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java']
- Overlap Java files: ['x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java', 'x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java', 'x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java']

## File State Comparison
- Compared files: ['x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java', 'x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -49,10 +49,15 @@
      */
     public static boolean reindexRequired(IndexMetadata indexMetadata, boolean filterToBlockedStatus) {
         return creationVersionBeforeMinimumWritableVersion(indexMetadata)
+            && isNotSystem(indexMetadata)
             && isNotSearchableSnapshot(indexMetadata)
             && matchBlockedStatus(indexMetadata, filterToBlockedStatus);
     }
 
+    private static boolean isNotSystem(IndexMetadata indexMetadata) {
+        return indexMetadata.isSystem() == false;
+    }
+
     private static boolean isNotSearchableSnapshot(IndexMetadata indexMetadata) {
         return indexMetadata.isSearchableSnapshot() == false;
     }

```

Generated
```diff
@@ -49,10 +49,15 @@
      */
     public static boolean reindexRequired(IndexMetadata indexMetadata, boolean filterToBlockedStatus) {
         return creationVersionBeforeMinimumWritableVersion(indexMetadata)
+            && isNotSystem(indexMetadata)
             && isNotSearchableSnapshot(indexMetadata)
             && matchBlockedStatus(indexMetadata, filterToBlockedStatus);
     }
 
+    private static boolean isNotSystem(IndexMetadata indexMetadata) {
+        return indexMetadata.isSystem() == false;
+    }
+
     private static boolean isNotSearchableSnapshot(IndexMetadata indexMetadata) {
         return indexMetadata.isSearchableSnapshot() == false;
     }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -72,12 +72,14 @@
         Map<String, List<DeprecationIssue>> dataStreamIssues = new HashMap<>();
         for (String dataStreamName : dataStreamNames) {
             DataStream dataStream = clusterState.metadata().dataStreams().get(dataStreamName);
-            List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
-                .map(c -> c.apply(dataStream, clusterState))
-                .filter(Objects::nonNull)
-                .toList();
-            if (issuesForSingleDataStream.isEmpty() == false) {
-                dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+            if (dataStream.isSystem() == false) {
+                List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
+                    .map(c -> c.apply(dataStream, clusterState))
+                    .filter(Objects::nonNull)
+                    .toList();
+                if (issuesForSingleDataStream.isEmpty() == false) {
+                    dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+                }
             }
         }
         return dataStreamIssues.isEmpty() ? Map.of() : dataStreamIssues;

```

Generated
```diff
@@ -72,12 +72,14 @@
         Map<String, List<DeprecationIssue>> dataStreamIssues = new HashMap<>();
         for (String dataStreamName : dataStreamNames) {
             DataStream dataStream = clusterState.metadata().dataStreams().get(dataStreamName);
-            List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
-                .map(c -> c.apply(dataStream, clusterState))
-                .filter(Objects::nonNull)
-                .toList();
-            if (issuesForSingleDataStream.isEmpty() == false) {
-                dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+            if (dataStream.isSystem() == false) {
+                List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
+                    .map(c -> c.apply(dataStream, clusterState))
+                    .filter(Objects::nonNull)
+                    .toList();
+                if (issuesForSingleDataStream.isEmpty() == false) {
+                    dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+                }
             }
         }
         return dataStreamIssues.isEmpty() ? Map.of() : dataStreamIssues;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java
index 84091a40fb2..5380e23c462 100644
--- a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java
+++ b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java
@@ -49,10 +49,15 @@ public class DeprecatedIndexPredicate {
      */
     public static boolean reindexRequired(IndexMetadata indexMetadata, boolean filterToBlockedStatus) {
         return creationVersionBeforeMinimumWritableVersion(indexMetadata)
+            && isNotSystem(indexMetadata)
             && isNotSearchableSnapshot(indexMetadata)
             && matchBlockedStatus(indexMetadata, filterToBlockedStatus);
     }
 
+    private static boolean isNotSystem(IndexMetadata indexMetadata) {
+        return indexMetadata.isSystem() == false;
+    }
+
     private static boolean isNotSearchableSnapshot(IndexMetadata indexMetadata) {
         return indexMetadata.isSearchableSnapshot() == false;
     }
diff --git a/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java b/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java
index a67d8960e78..7f7c4d98584 100644
--- a/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java
+++ b/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java
@@ -72,12 +72,14 @@ public class DataStreamDeprecationChecker implements ResourceDeprecationChecker
         Map<String, List<DeprecationIssue>> dataStreamIssues = new HashMap<>();
         for (String dataStreamName : dataStreamNames) {
             DataStream dataStream = clusterState.metadata().dataStreams().get(dataStreamName);
-            List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
-                .map(c -> c.apply(dataStream, clusterState))
-                .filter(Objects::nonNull)
-                .toList();
-            if (issuesForSingleDataStream.isEmpty() == false) {
-                dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+            if (dataStream.isSystem() == false) {
+                List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
+                    .map(c -> c.apply(dataStream, clusterState))
+                    .filter(Objects::nonNull)
+                    .toList();
+                if (issuesForSingleDataStream.isEmpty() == false) {
+                    dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+                }
             }
         }
         return dataStreamIssues.isEmpty() ? Map.of() : dataStreamIssues;

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java
index 84091a40fb2..5380e23c462 100644
--- a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java
+++ b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java
@@ -49,10 +49,15 @@ public class DeprecatedIndexPredicate {
      */
     public static boolean reindexRequired(IndexMetadata indexMetadata, boolean filterToBlockedStatus) {
         return creationVersionBeforeMinimumWritableVersion(indexMetadata)
+            && isNotSystem(indexMetadata)
             && isNotSearchableSnapshot(indexMetadata)
             && matchBlockedStatus(indexMetadata, filterToBlockedStatus);
     }
 
+    private static boolean isNotSystem(IndexMetadata indexMetadata) {
+        return indexMetadata.isSystem() == false;
+    }
+
     private static boolean isNotSearchableSnapshot(IndexMetadata indexMetadata) {
         return indexMetadata.isSearchableSnapshot() == false;
     }
diff --git a/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java b/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java
index a67d8960e78..7f7c4d98584 100644
--- a/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java
+++ b/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java
@@ -72,12 +72,14 @@ public class DataStreamDeprecationChecker implements ResourceDeprecationChecker
         Map<String, List<DeprecationIssue>> dataStreamIssues = new HashMap<>();
         for (String dataStreamName : dataStreamNames) {
             DataStream dataStream = clusterState.metadata().dataStreams().get(dataStreamName);
-            List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
-                .map(c -> c.apply(dataStream, clusterState))
-                .filter(Objects::nonNull)
-                .toList();
-            if (issuesForSingleDataStream.isEmpty() == false) {
-                dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+            if (dataStream.isSystem() == false) {
+                List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
+                    .map(c -> c.apply(dataStream, clusterState))
+                    .filter(Objects::nonNull)
+                    .toList();
+                if (issuesForSingleDataStream.isEmpty() == false) {
+                    dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+                }
             }
         }
         return dataStreamIssues.isEmpty() ? Map.of() : dataStreamIssues;

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/docs/changelog/122951.yaml b/docs/changelog/122951.yaml
new file mode 100644
index 00000000000..b84e05d758f
--- /dev/null
+++ b/docs/changelog/122951.yaml
@@ -0,0 +1,6 @@
+pr: 122951
+summary: Updates the deprecation info API to not warn about system indices and data
+  streams
+area: Indices APIs
+type: bug
+issues: []
diff --git a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java
index 84091a40fb2..5380e23c462 100644
--- a/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java
+++ b/x-pack/plugin/core/src/main/java/org/elasticsearch/xpack/core/deprecation/DeprecatedIndexPredicate.java
@@ -49,10 +49,15 @@ public class DeprecatedIndexPredicate {
      */
     public static boolean reindexRequired(IndexMetadata indexMetadata, boolean filterToBlockedStatus) {
         return creationVersionBeforeMinimumWritableVersion(indexMetadata)
+            && isNotSystem(indexMetadata)
             && isNotSearchableSnapshot(indexMetadata)
             && matchBlockedStatus(indexMetadata, filterToBlockedStatus);
     }
 
+    private static boolean isNotSystem(IndexMetadata indexMetadata) {
+        return indexMetadata.isSystem() == false;
+    }
+
     private static boolean isNotSearchableSnapshot(IndexMetadata indexMetadata) {
         return indexMetadata.isSearchableSnapshot() == false;
     }
diff --git a/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java b/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java
index a67d8960e78..7f7c4d98584 100644
--- a/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java
+++ b/x-pack/plugin/deprecation/src/main/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationChecker.java
@@ -72,12 +72,14 @@ public class DataStreamDeprecationChecker implements ResourceDeprecationChecker
         Map<String, List<DeprecationIssue>> dataStreamIssues = new HashMap<>();
         for (String dataStreamName : dataStreamNames) {
             DataStream dataStream = clusterState.metadata().dataStreams().get(dataStreamName);
-            List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
-                .map(c -> c.apply(dataStream, clusterState))
-                .filter(Objects::nonNull)
-                .toList();
-            if (issuesForSingleDataStream.isEmpty() == false) {
-                dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+            if (dataStream.isSystem() == false) {
+                List<DeprecationIssue> issuesForSingleDataStream = DATA_STREAM_CHECKS.stream()
+                    .map(c -> c.apply(dataStream, clusterState))
+                    .filter(Objects::nonNull)
+                    .toList();
+                if (issuesForSingleDataStream.isEmpty() == false) {
+                    dataStreamIssues.put(dataStreamName, issuesForSingleDataStream);
+                }
             }
         }
         return dataStreamIssues.isEmpty() ? Map.of() : dataStreamIssues;
diff --git a/x-pack/plugin/deprecation/src/test/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationCheckerTests.java b/x-pack/plugin/deprecation/src/test/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationCheckerTests.java
index 718e5bb1da3..3c0ef84cb61 100644
--- a/x-pack/plugin/deprecation/src/test/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationCheckerTests.java
+++ b/x-pack/plugin/deprecation/src/test/java/org/elasticsearch/xpack/deprecation/DataStreamDeprecationCheckerTests.java
@@ -302,4 +302,52 @@ public class DataStreamDeprecationCheckerTests extends ESTestCase {
         assertThat(issuesByDataStream.get(dataStream.getName()), equalTo(List.of(expected)));
     }
 
+    public void testOldSystemDataStreamIgnored() {
+        // We do not want system data streams coming back in the deprecation info API
+        int oldIndexCount = randomIntBetween(1, 100);
+        int newIndexCount = randomIntBetween(1, 100);
+        List<Index> allIndices = new ArrayList<>();
+        Map<String, IndexMetadata> nameToIndexMetadata = new HashMap<>();
+        for (int i = 0; i < oldIndexCount; i++) {
+            Settings.Builder settings = settings(IndexVersion.fromId(7170099));
+
+            String indexName = "old-data-stream-index-" + i;
+            settings.put(MetadataIndexStateService.VERIFIED_READ_ONLY_SETTING.getKey(), true);
+
+            IndexMetadata oldIndexMetadata = IndexMetadata.builder(indexName)
+                .settings(settings)
+                .numberOfShards(1)
+                .numberOfReplicas(0)
+                .build();
+            allIndices.add(oldIndexMetadata.getIndex());
+            nameToIndexMetadata.put(oldIndexMetadata.getIndex().getName(), oldIndexMetadata);
+        }
+        for (int i = 0; i < newIndexCount; i++) {
+            Index newIndex = createNewIndex(i, false, nameToIndexMetadata);
+            allIndices.add(newIndex);
+        }
+        DataStream dataStream = new DataStream(
+            randomAlphaOfLength(10),
+            allIndices,
+            randomNonNegativeLong(),
+            Map.of(),
+            true,
+            false,
+            true,
+            randomBoolean(),
+            randomFrom(IndexMode.values()),
+            null,
+            randomFrom(DataStreamOptions.EMPTY, DataStreamOptions.FAILURE_STORE_DISABLED, DataStreamOptions.FAILURE_STORE_ENABLED, null),
+            List.of(),
+            randomBoolean(),
+            null
+        );
+        Metadata metadata = Metadata.builder()
+            .indices(nameToIndexMetadata)
+            .dataStreams(Map.of(dataStream.getName(), dataStream), Map.of())
+            .build();
+        ClusterState clusterState = ClusterState.builder(ClusterName.DEFAULT).metadata(metadata).build();
+        assertThat(checker.check(clusterState), equalTo(Map.of()));
+    }
+
 }
diff --git a/x-pack/plugin/deprecation/src/test/java/org/elasticsearch/xpack/deprecation/IndexDeprecationCheckerTests.java b/x-pack/plugin/deprecation/src/test/java/org/elasticsearch/xpack/deprecation/IndexDeprecationCheckerTests.java
index 65abe958ffb..b67cedf7224 100644
--- a/x-pack/plugin/deprecation/src/test/java/org/elasticsearch/xpack/deprecation/IndexDeprecationCheckerTests.java
+++ b/x-pack/plugin/deprecation/src/test/java/org/elasticsearch/xpack/deprecation/IndexDeprecationCheckerTests.java
@@ -299,6 +299,28 @@ public class IndexDeprecationCheckerTests extends ESTestCase {
         assertEquals(List.of(expected), issuesByIndex.get("test"));
     }
 
+    public void testOldSystemIndicesIgnored() {
+        // We do not want system indices coming back in the deprecation info API
+        Settings.Builder settings = settings(OLD_VERSION).put(MetadataIndexStateService.VERIFIED_READ_ONLY_SETTING.getKey(), true);
+        IndexMetadata indexMetadata = IndexMetadata.builder("test")
+            .system(true)
+            .settings(settings)
+            .numberOfShards(1)
+            .numberOfReplicas(0)
+            .state(indexMetdataState)
+            .build();
+        ClusterState clusterState = ClusterState.builder(ClusterState.EMPTY_STATE)
+            .metadata(Metadata.builder().put(indexMetadata, true))
+            .blocks(clusterBlocksForIndices(indexMetadata))
+            .build();
+        Map<String, List<DeprecationIssue>> issuesByIndex = checker.check(
+            clusterState,
+            new DeprecationInfoAction.Request(TimeValue.THIRTY_SECONDS),
+            emptyPrecomputedData
+        );
+        assertThat(issuesByIndex, equalTo(Map.of()));
+    }
+
     private IndexMetadata readonlyIndexMetadata(String indexName, IndexVersion indexVersion) {
         Settings.Builder settings = settings(indexVersion).put(MetadataIndexStateService.VERIFIED_READ_ONLY_SETTING.getKey(), true);
         return IndexMetadata.builder(indexName).settings(settings).numberOfShards(1).numberOfReplicas(0).state(indexMetdataState).build();

```
