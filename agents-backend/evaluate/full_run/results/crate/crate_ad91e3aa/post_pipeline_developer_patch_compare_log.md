# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java']
- Developer Java files: ['server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java']
- Overlap Java files: ['server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java']

## File State Comparison
- Compared files: ['server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java']
- Mismatched files: ['server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java

- Developer hunks: 3
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -145,7 +145,7 @@
             new ScalingExecutorBuilder(Names.WARMER, 1, halfProcMaxAt5, TimeValue.timeValueMinutes(5)),
             new ScalingExecutorBuilder(Names.SNAPSHOT, 1, halfProcMaxAt5, TimeValue.timeValueMinutes(5)),
             new ScalingExecutorBuilder(Names.FETCH_SHARD_STARTED, 1, 2 * availableProcessors, TimeValue.timeValueMinutes(5)),
-            new FixedExecutorBuilder(settings, Names.FORCE_MERGE, 1, -1),
+            new FixedExecutorBuilder(settings, Names.FORCE_MERGE, oneEightOfProcessors(availableProcessors), -1),
             new ScalingExecutorBuilder(Names.FETCH_SHARD_STORE, 1, 2 * availableProcessors, TimeValue.timeValueMinutes(5)),
             new FixedExecutorBuilder(settings, Names.LOGICAL_REPLICATION, searchThreadPoolSize(availableProcessors), 100)
         );

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -145,7 +145,7 @@
-             new ScalingExecutorBuilder(Names.WARMER, 1, halfProcMaxAt5, TimeValue.timeValueMinutes(5)),
-             new ScalingExecutorBuilder(Names.SNAPSHOT, 1, halfProcMaxAt5, TimeValue.timeValueMinutes(5)),
-             new ScalingExecutorBuilder(Names.FETCH_SHARD_STARTED, 1, 2 * availableProcessors, TimeValue.timeValueMinutes(5)),
--            new FixedExecutorBuilder(settings, Names.FORCE_MERGE, 1, -1),
-+            new FixedExecutorBuilder(settings, Names.FORCE_MERGE, oneEightOfProcessors(availableProcessors), -1),
-             new ScalingExecutorBuilder(Names.FETCH_SHARD_STORE, 1, 2 * availableProcessors, TimeValue.timeValueMinutes(5)),
-             new FixedExecutorBuilder(settings, Names.LOGICAL_REPLICATION, searchThreadPoolSize(availableProcessors), 100)
-         );
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -229,6 +229,15 @@
         return new ThreadPoolStats.Stats(name, -1, -1, -1, -1, -1, -1);
     }
 
+    @Nullable
+    public ThreadPool.Info info(String name) {
+        ExecutorHolder holder = executors.get(name);
+        if (holder == null) {
+            return null;
+        }
+        return holder.info();
+    }
+
     /**
      * Get the generic {@link ExecutorService}. This executor service
      * {@link Executor#execute(Runnable)} method will run the {@link Runnable} it is given in the

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,16 +1 @@-@@ -229,6 +229,15 @@
-         return new ThreadPoolStats.Stats(name, -1, -1, -1, -1, -1, -1);
-     }
- 
-+    @Nullable
-+    public ThreadPool.Info info(String name) {
-+        ExecutorHolder holder = executors.get(name);
-+        if (holder == null) {
-+            return null;
-+        }
-+        return holder.info();
-+    }
-+
-     /**
-      * Get the generic {@link ExecutorService}. This executor service
-      * {@link Executor#execute(Runnable)} method will run the {@link Runnable} it is given in the
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -373,6 +382,10 @@
         return boundedBy((numberOfProcessors + 1) / 2, 1, 10);
     }
 
+    static int oneEightOfProcessors(int numberOfProcessors) {
+        return boundedBy(numberOfProcessors / 8, 1, Integer.MAX_VALUE);
+    }
+
     public static int searchThreadPoolSize(int availableProcessors) {
         return ((availableProcessors * 3) / 2) + 1;
     }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,11 +1 @@-@@ -373,6 +382,10 @@
-         return boundedBy((numberOfProcessors + 1) / 2, 1, 10);
-     }
- 
-+    static int oneEightOfProcessors(int numberOfProcessors) {
-+        return boundedBy(numberOfProcessors / 8, 1, Integer.MAX_VALUE);
-+    }
-+
-     public static int searchThreadPoolSize(int availableProcessors) {
-         return ((availableProcessors * 3) / 2) + 1;
-     }
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
diff --git a/docs/appendices/release-notes/6.1.0.rst b/docs/appendices/release-notes/6.1.0.rst
index c09b088a23..e1c59004d8 100644
--- a/docs/appendices/release-notes/6.1.0.rst
+++ b/docs/appendices/release-notes/6.1.0.rst
@@ -57,6 +57,10 @@ Breaking Changes
   the relative paths are resolved, thus conforming to the behavior already
   described in the :ref:`documentation <conf-node-settings_paths>`.
 
+- Increased the ``FORCE_MERGE`` default thread pool size from ``1`` to ``1/8``
+  of the available processors, improving the performance of the :ref:`optimize`
+  operation on machines with more than ``15`` cores.
+
 Deprecations
 ============
 
diff --git a/server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java b/server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java
index 77edd21b5a..ab4a87422c 100644
--- a/server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java
+++ b/server/src/main/java/org/elasticsearch/threadpool/ThreadPool.java
@@ -145,7 +145,7 @@ public class ThreadPool implements Scheduler {
             new ScalingExecutorBuilder(Names.WARMER, 1, halfProcMaxAt5, TimeValue.timeValueMinutes(5)),
             new ScalingExecutorBuilder(Names.SNAPSHOT, 1, halfProcMaxAt5, TimeValue.timeValueMinutes(5)),
             new ScalingExecutorBuilder(Names.FETCH_SHARD_STARTED, 1, 2 * availableProcessors, TimeValue.timeValueMinutes(5)),
-            new FixedExecutorBuilder(settings, Names.FORCE_MERGE, 1, -1),
+            new FixedExecutorBuilder(settings, Names.FORCE_MERGE, oneEightOfProcessors(availableProcessors), -1),
             new ScalingExecutorBuilder(Names.FETCH_SHARD_STORE, 1, 2 * availableProcessors, TimeValue.timeValueMinutes(5)),
             new FixedExecutorBuilder(settings, Names.LOGICAL_REPLICATION, searchThreadPoolSize(availableProcessors), 100)
         );
@@ -229,6 +229,15 @@ public class ThreadPool implements Scheduler {
         return new ThreadPoolStats.Stats(name, -1, -1, -1, -1, -1, -1);
     }
 
+    @Nullable
+    public ThreadPool.Info info(String name) {
+        ExecutorHolder holder = executors.get(name);
+        if (holder == null) {
+            return null;
+        }
+        return holder.info();
+    }
+
     /**
      * Get the generic {@link ExecutorService}. This executor service
      * {@link Executor#execute(Runnable)} method will run the {@link Runnable} it is given in the
@@ -373,6 +382,10 @@ public class ThreadPool implements Scheduler {
         return boundedBy((numberOfProcessors + 1) / 2, 1, 10);
     }
 
+    static int oneEightOfProcessors(int numberOfProcessors) {
+        return boundedBy(numberOfProcessors / 8, 1, Integer.MAX_VALUE);
+    }
+
     public static int searchThreadPoolSize(int availableProcessors) {
         return ((availableProcessors * 3) / 2) + 1;
     }
diff --git a/server/src/test/java/org/elasticsearch/threadpool/ThreadPoolTest.java b/server/src/test/java/org/elasticsearch/threadpool/ThreadPoolTest.java
new file mode 100644
index 0000000000..764f1f98de
--- /dev/null
+++ b/server/src/test/java/org/elasticsearch/threadpool/ThreadPoolTest.java
@@ -0,0 +1,60 @@
+/*
+ * Licensed to Crate.io GmbH ("Crate") under one or more contributor
+ * license agreements.  See the NOTICE file distributed with this work for
+ * additional information regarding copyright ownership.  Crate licenses
+ * this file to you under the Apache License, Version 2.0 (the "License");
+ * you may not use this file except in compliance with the License.  You may
+ * obtain a copy of the License at
+ *
+ *     http://www.apache.org/licenses/LICENSE-2.0
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
+ * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
+ * License for the specific language governing permissions and limitations
+ * under the License.
+ *
+ * However, if you have executed another commercial license agreement
+ * with Crate these terms will supersede the license and you may use the
+ * software solely pursuant to the terms of the relevant commercial agreement.
+ */
+
+package org.elasticsearch.threadpool;
+
+import static org.assertj.core.api.Assertions.assertThat;
+
+import org.elasticsearch.common.settings.Settings;
+import org.elasticsearch.common.util.concurrent.EsExecutors;
+import org.elasticsearch.test.ESTestCase;
+import org.junit.Test;
+
+public class ThreadPoolTest extends ESTestCase {
+
+    @Test
+    public void test_one_eight_of_processors() {
+        assertThat(ThreadPool.oneEightOfProcessors(1)).isEqualTo(1);
+        assertThat(ThreadPool.oneEightOfProcessors(3)).isEqualTo(1);
+        assertThat(ThreadPool.oneEightOfProcessors(8)).isEqualTo(1);
+        assertThat(ThreadPool.oneEightOfProcessors(16)).isEqualTo(2);
+    }
+
+
+    @Test
+    public void test_force_merge_pool_size() {
+        final int processors = randomIntBetween(1, EsExecutors.numberOfProcessors(Settings.EMPTY));
+        final ThreadPool threadPool = new TestThreadPool(
+            "test",
+            Settings.builder().put(EsExecutors.PROCESSORS_SETTING.getKey(), processors).build()
+        );
+        try {
+            final int expectedSize = Math.max(1, processors / 8);
+            ThreadPool.Info info = threadPool.info(ThreadPool.Names.FORCE_MERGE);
+            assertThat(info).isNotNull();
+            assertThat(info.min()).isEqualTo(expectedSize);
+            assertThat(info.max()).isEqualTo(expectedSize);
+        } finally {
+            terminate(threadPool);
+        }
+
+    }
+}

```
