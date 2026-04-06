# Phase 0 Inputs

- Mainline commit: aeddddeba6a7f487891cc8b131fc87bfdf157623
- Backport commit: 1f3ed5c7b64bc1850a6c4bc2c21c09e26cb469af
- Java-only files for agentic phases: 3
- Developer auxiliary hunks (test + non-Java): 5

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/metadata/Routing.java', 'server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java', 'server/src/main/java/io/crate/planner/operators/LogicalPlanner.java']
- Developer Java files: ['server/src/main/java/io/crate/metadata/Routing.java', 'server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java', 'server/src/main/java/io/crate/planner/operators/LogicalPlanner.java']
- Overlap Java files: ['server/src/main/java/io/crate/metadata/Routing.java', 'server/src/main/java/io/crate/metadata/sys/SysAllocationsTableInfo.java', 'server/src/main/java/io/crate/planner/operators/LogicalPlanner.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From aeddddeba6a7f487891cc8b131fc87bfdf157623 Mon Sep 17 00:00:00 2001
From: Sebastian Utz <su@rtme.net>
Date: Tue, 18 Mar 2025 17:21:58 +0100
Subject: [PATCH] Fix NPE queries on `sys.allocations` if no master is
 discovered

If the master is not discovered, `getMasterNodeId()` will
return NULL which causes the `forTableOnSingleNode` to fail.

Adding a new `Routing.forMasterNode()` method which catches this
and throws the related exceptions fixes this.
---
 docs/appendices/release-notes/5.10.4.rst               |  4 ++++
 docs/appendices/release-notes/5.9.13.rst               |  4 +++-
 server/src/main/java/io/crate/metadata/Routing.java    | 10 ++++++++++
 .../io/crate/metadata/sys/SysAllocationsTableInfo.java |  2 +-
 .../io/crate/planner/operators/LogicalPlanner.java     |  3 ++-
 .../metadata/sys/SysAllocationsTableInfoTest.java      |  9 +++++++++
 6 files changed, 29 insertions(+), 3 deletions(-)

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
index 0294d5791f..31c5038da1 100644
--- a/server/src/main/java/io/crate/planner/operators/LogicalPlanner.java
+++ b/server/src/main/java/io/crate/planner/operators/LogicalPlanner.java
@@ -34,6 +34,7 @@ import java.util.function.Predicate;
 import java.util.function.Supplier;
 import java.util.function.UnaryOperator;
 
+import org.elasticsearch.ElasticsearchException;
 import org.elasticsearch.Version;
 import org.elasticsearch.cluster.ClusterState;
 import org.elasticsearch.cluster.metadata.Metadata;
@@ -701,7 +702,7 @@ public class LogicalPlanner {
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
-- 
2.43.0


```
