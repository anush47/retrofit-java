# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/metadata/Routing.java', 'server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java', 'server/src/main/java/io/crate/planner/operators/LogicalPlanner.java']
- Developer Java files: ['server/src/main/java/io/crate/metadata/Routing.java', 'server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java', 'server/src/main/java/io/crate/planner/operators/LogicalPlanner.java']
- Overlap Java files: ['server/src/main/java/io/crate/metadata/Routing.java', 'server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java', 'server/src/main/java/io/crate/planner/operators/LogicalPlanner.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/metadata/Routing.java', 'server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java', 'server/src/main/java/io/crate/planner/operators/LogicalPlanner.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/metadata/Routing.java', 'server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java', 'server/src/main/java/io/crate/planner/operators/LogicalPlanner.java']
- Mismatched files: ['server/src/main/java/io/crate/metadata/Routing.java', 'server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java', 'server/src/main/java/io/crate/planner/operators/LogicalPlanner.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/metadata/Routing.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -27,11 +27,13 @@
 import java.util.Set;
 import java.util.TreeMap;
 
+import org.elasticsearch.cluster.ClusterState;
 import org.elasticsearch.cluster.node.DiscoveryNode;
 import org.elasticsearch.cluster.node.DiscoveryNodes;
 import org.elasticsearch.common.io.stream.StreamInput;
 import org.elasticsearch.common.io.stream.StreamOutput;
 import org.elasticsearch.common.io.stream.Writeable;
+import org.elasticsearch.discovery.MasterNotDiscoveredException;
 
 import com.carrotsearch.hppc.IntArrayList;
 import com.carrotsearch.hppc.IntIndexedContainer;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,14 +1 @@-@@ -27,11 +27,13 @@
- import java.util.Set;
- import java.util.TreeMap;
- 
-+import org.elasticsearch.cluster.ClusterState;
- import org.elasticsearch.cluster.node.DiscoveryNode;
- import org.elasticsearch.cluster.node.DiscoveryNodes;
- import org.elasticsearch.common.io.stream.StreamInput;
- import org.elasticsearch.common.io.stream.StreamOutput;
- import org.elasticsearch.common.io.stream.Writeable;
-+import org.elasticsearch.discovery.MasterNotDiscoveredException;
- 
- import com.carrotsearch.hppc.IntArrayList;
- import com.carrotsearch.hppc.IntIndexedContainer;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -207,6 +209,14 @@
         return new Routing(indicesByNode);
     }
 
+    public static Routing forMasterNode(RelationName relationName, ClusterState clusterState) {
+        String masterNodeId = clusterState.nodes().getMasterNodeId();
+        if (masterNodeId == null) {
+            throw new MasterNotDiscoveredException();
+        }
+        return forTableOnSingleNode(relationName, masterNodeId);
+    }
+
     @Override
     public boolean equals(Object o) {
         if (this == o) return true;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,15 +1 @@-@@ -207,6 +209,14 @@
-         return new Routing(indicesByNode);
-     }
- 
-+    public static Routing forMasterNode(RelationName relationName, ClusterState clusterState) {
-+        String masterNodeId = clusterState.nodes().getMasterNodeId();
-+        if (masterNodeId == null) {
-+            throw new MasterNotDiscoveredException();
-+        }
-+        return forTableOnSingleNode(relationName, masterNodeId);
-+    }
-+
-     @Override
-     public boolean equals(Object o) {
-         if (this == o) return true;
+*No hunk*
```


### server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -56,6 +56,6 @@
             ColumnIdent.of("partition_ident"),
             ColumnIdent.of("shard_id")
         )
-        .withRouting((state, ignored, ignored2) -> Routing.forTableOnSingleNode(IDENT, state.nodes().getMasterNodeId()))
+        .withRouting((state, ignored, ignored2) -> Routing.forMasterNode(IDENT, state))
         .build();
 }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -56,6 +56,6 @@
-             ColumnIdent.of("partition_ident"),
-             ColumnIdent.of("shard_id")
-         )
--        .withRouting((state, ignored, ignored2) -> Routing.forTableOnSingleNode(IDENT, state.nodes().getMasterNodeId()))
-+        .withRouting((state, ignored, ignored2) -> Routing.forMasterNode(IDENT, state))
-         .build();
- }
+*No hunk*
```


### server/src/main/java/io/crate/planner/operators/LogicalPlanner.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -32,6 +32,7 @@
 import java.util.function.Supplier;
 import java.util.function.UnaryOperator;
 
+import org.elasticsearch.ElasticsearchException;
 import org.elasticsearch.Version;
 import org.elasticsearch.cluster.ClusterState;
 import org.elasticsearch.cluster.metadata.Metadata;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -32,6 +32,7 @@
- import java.util.function.Supplier;
- import java.util.function.UnaryOperator;
- 
-+import org.elasticsearch.ElasticsearchException;
- import org.elasticsearch.Version;
- import org.elasticsearch.cluster.ClusterState;
- import org.elasticsearch.cluster.metadata.Metadata;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -632,7 +633,7 @@
         } catch (ConversionException e) {
             throw e;
         } catch (Exception e) {
-            if (e instanceof CrateException) {
+            if (e instanceof CrateException || e instanceof ElasticsearchException) {
                 // Don't hide errors like MissingShardOperationsException, UnavailableShardsException
                 throw e;
             }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -632,7 +633,7 @@
-         } catch (ConversionException e) {
-             throw e;
-         } catch (Exception e) {
--            if (e instanceof CrateException) {
-+            if (e instanceof CrateException || e instanceof ElasticsearchException) {
-                 // Don't hide errors like MissingShardOperationsException, UnavailableShardsException
-                 throw e;
-             }
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
diff --git a/docs/appendices/release-notes/5.10.4.rst b/docs/appendices/release-notes/5.10.4.rst
index cb7dfae9d4..31f6463990 100644
--- a/docs/appendices/release-notes/5.10.4.rst
+++ b/docs/appendices/release-notes/5.10.4.rst
@@ -43,3 +43,7 @@ See the :ref:`version_5.10.0` release notes for a full list of changes in the
 
 Fixes
 =====
+
+- Fixed NPE when querying the :ref:`sys.allocations <sys-allocations>` table
+  while no master node has been discovered. A proper exception is now thrown
+  instead of an NPE.
diff --git a/docs/appendices/release-notes/5.9.13.rst b/docs/appendices/release-notes/5.9.13.rst
index e74963a3c8..a280478f47 100644
--- a/docs/appendices/release-notes/5.9.13.rst
+++ b/docs/appendices/release-notes/5.9.13.rst
@@ -47,4 +47,6 @@ See the :ref:`version_5.9.0` release notes for a full list of changes in the
 Fixes
 =====
 
-None
+- Fixed NPE when querying the :ref:`sys.allocations <sys-allocations>` table
+  while no master node has been discovered. A proper exception is now thrown
+  instead of an NPE.
diff --git a/server/src/main/java/io/crate/metadata/Routing.java b/server/src/main/java/io/crate/metadata/Routing.java
index a2d99e2123..e649ff8ab3 100644
--- a/server/src/main/java/io/crate/metadata/Routing.java
+++ b/server/src/main/java/io/crate/metadata/Routing.java
@@ -27,11 +27,13 @@ import java.util.Map;
 import java.util.Set;
 import java.util.TreeMap;
 
+import org.elasticsearch.cluster.ClusterState;
 import org.elasticsearch.cluster.node.DiscoveryNode;
 import org.elasticsearch.cluster.node.DiscoveryNodes;
 import org.elasticsearch.common.io.stream.StreamInput;
 import org.elasticsearch.common.io.stream.StreamOutput;
 import org.elasticsearch.common.io.stream.Writeable;
+import org.elasticsearch.discovery.MasterNotDiscoveredException;
 
 import com.carrotsearch.hppc.IntArrayList;
 import com.carrotsearch.hppc.IntIndexedContainer;
@@ -207,6 +209,14 @@ public class Routing implements Writeable {
         return new Routing(indicesByNode);
     }
 
+    public static Routing forMasterNode(RelationName relationName, ClusterState clusterState) {
+        String masterNodeId = clusterState.nodes().getMasterNodeId();
+        if (masterNodeId == null) {
+            throw new MasterNotDiscoveredException();
+        }
+        return forTableOnSingleNode(relationName, masterNodeId);
+    }
+
     @Override
     public boolean equals(Object o) {
         if (this == o) return true;
diff --git a/server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java b/server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java
index ed78890185..47b47d6cf3 100644
--- a/server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java
+++ b/server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java
@@ -56,6 +56,6 @@ public class SysAllocationsTableInfo {
             ColumnIdent.of("partition_ident"),
             ColumnIdent.of("shard_id")
         )
-        .withRouting((state, ignored, ignored2) -> Routing.forTableOnSingleNode(IDENT, state.nodes().getMasterNodeId()))
+        .withRouting((state, ignored, ignored2) -> Routing.forMasterNode(IDENT, state))
         .build();
 }
diff --git a/server/src/main/java/io/crate/planner/operators/LogicalPlanner.java b/server/src/main/java/io/crate/planner/operators/LogicalPlanner.java
index 2d31b5424f..487615658c 100644
--- a/server/src/main/java/io/crate/planner/operators/LogicalPlanner.java
+++ b/server/src/main/java/io/crate/planner/operators/LogicalPlanner.java
@@ -32,6 +32,7 @@ import java.util.function.Predicate;
 import java.util.function.Supplier;
 import java.util.function.UnaryOperator;
 
+import org.elasticsearch.ElasticsearchException;
 import org.elasticsearch.Version;
 import org.elasticsearch.cluster.ClusterState;
 import org.elasticsearch.cluster.metadata.Metadata;
@@ -632,7 +633,7 @@ public class LogicalPlanner {
         } catch (ConversionException e) {
             throw e;
         } catch (Exception e) {
-            if (e instanceof CrateException) {
+            if (e instanceof CrateException || e instanceof ElasticsearchException) {
                 // Don't hide errors like MissingShardOperationsException, UnavailableShardsException
                 throw e;
             }
diff --git a/server/src/test/java/io/crate/metadata/sys/SysAllocationsTableInfoTest.java b/server/src/test/java/io/crate/metadata/sys/SysAllocationsTableInfoTest.java
index 975bf5ac41..34bd793271 100644
--- a/server/src/test/java/io/crate/metadata/sys/SysAllocationsTableInfoTest.java
+++ b/server/src/test/java/io/crate/metadata/sys/SysAllocationsTableInfoTest.java
@@ -23,6 +23,7 @@ package io.crate.metadata.sys;
 
 
 import static org.assertj.core.api.Assertions.assertThat;
+import static org.assertj.core.api.Assertions.assertThatThrownBy;
 import static org.elasticsearch.cluster.node.DiscoveryNodeRole.DATA_ROLE;
 import static org.elasticsearch.test.ClusterServiceUtils.setState;
 
@@ -33,6 +34,7 @@ import org.elasticsearch.Version;
 import org.elasticsearch.cluster.ClusterState;
 import org.elasticsearch.cluster.node.DiscoveryNode;
 import org.elasticsearch.cluster.node.DiscoveryNodes;
+import org.elasticsearch.discovery.MasterNotDiscoveredException;
 import org.junit.Before;
 import org.junit.Test;
 
@@ -64,4 +66,11 @@ public class SysAllocationsTableInfoTest extends CrateDummyClusterServiceUnitTes
         var routing = allocationsTable.getRouting(clusterService.state(), null, null, null, null);
         assertThat(routing.nodes()).contains(NODE_ID);
     }
+
+    @Test
+    public void test_exception_is_thrown_when_no_master_is_discovered() {
+        var allocationsTable = SysAllocationsTableInfo.INSTANCE;
+        assertThatThrownBy(() -> allocationsTable.getRouting(ClusterState.EMPTY_STATE, null, null, null, null))
+            .isInstanceOf(MasterNotDiscoveredException.class);
+    }
 }

```
