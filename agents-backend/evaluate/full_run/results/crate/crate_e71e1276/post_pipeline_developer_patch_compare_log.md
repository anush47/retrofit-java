# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/session/Session.java']
- Developer Java files: ['server/src/main/java/io/crate/session/Session.java']
- Overlap Java files: ['server/src/main/java/io/crate/session/Session.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/session/Session.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/session/Session.java']
- Mismatched files: ['server/src/main/java/io/crate/session/Session.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/session/Session.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -32,6 +32,7 @@
 import java.util.UUID;
 import java.util.concurrent.CompletableFuture;
 import java.util.concurrent.ScheduledExecutorService;
+import java.util.concurrent.ScheduledFuture;
 import java.util.concurrent.ThreadLocalRandom;
 import java.util.concurrent.TimeUnit;
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -32,6 +32,7 @@
- import java.util.UUID;
- import java.util.concurrent.CompletableFuture;
- import java.util.concurrent.ScheduledExecutorService;
-+import java.util.concurrent.ScheduledFuture;
- import java.util.concurrent.ThreadLocalRandom;
- import java.util.concurrent.TimeUnit;
- 
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -654,7 +655,8 @@
             executor.client().execute(KillJobsNodeAction.INSTANCE, request);
         };
         ScheduledExecutorService scheduler = executor.scheduler();
-        scheduler.schedule(kill, remainingTimeoutMs, TimeUnit.MILLISECONDS);
+        ScheduledFuture<?> schedule = scheduler.schedule(kill, remainingTimeoutMs, TimeUnit.MILLISECONDS);
+        result.whenComplete((_, _) -> schedule.cancel(false));
     }
 
     private CompletableFuture<?> triggerDeferredExecutions() {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -654,7 +655,8 @@
-             executor.client().execute(KillJobsNodeAction.INSTANCE, request);
-         };
-         ScheduledExecutorService scheduler = executor.scheduler();
--        scheduler.schedule(kill, remainingTimeoutMs, TimeUnit.MILLISECONDS);
-+        ScheduledFuture<?> schedule = scheduler.schedule(kill, remainingTimeoutMs, TimeUnit.MILLISECONDS);
-+        result.whenComplete((_, _) -> schedule.cancel(false));
-     }
- 
-     private CompletableFuture<?> triggerDeferredExecutions() {
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
diff --git a/docs/appendices/release-notes/5.10.5.rst b/docs/appendices/release-notes/5.10.5.rst
index 83626685f7..d334ed9241 100644
--- a/docs/appendices/release-notes/5.10.5.rst
+++ b/docs/appendices/release-notes/5.10.5.rst
@@ -44,6 +44,11 @@ See the :ref:`version_5.10.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- Improved the handling of ``statement_timeout`` to reduce memory consumption.
+  Before it would consume extra memory per executed query for the full
+  ``statement_duration`` even if the query finished early. Now the memory is
+  released once a query finishes.
+
 - Fixed an issue that prevented ``MATCH (geo_shape_column, ...)`` from matching
   any records if ``geo_shape_column`` is a generated column.
 
diff --git a/server/src/main/java/io/crate/session/Session.java b/server/src/main/java/io/crate/session/Session.java
index 2b6a5dfe87..5c86ca3a5f 100644
--- a/server/src/main/java/io/crate/session/Session.java
+++ b/server/src/main/java/io/crate/session/Session.java
@@ -32,6 +32,7 @@ import java.util.Map;
 import java.util.UUID;
 import java.util.concurrent.CompletableFuture;
 import java.util.concurrent.ScheduledExecutorService;
+import java.util.concurrent.ScheduledFuture;
 import java.util.concurrent.ThreadLocalRandom;
 import java.util.concurrent.TimeUnit;
 
@@ -654,7 +655,8 @@ public class Session implements AutoCloseable {
             executor.client().execute(KillJobsNodeAction.INSTANCE, request);
         };
         ScheduledExecutorService scheduler = executor.scheduler();
-        scheduler.schedule(kill, remainingTimeoutMs, TimeUnit.MILLISECONDS);
+        ScheduledFuture<?> schedule = scheduler.schedule(kill, remainingTimeoutMs, TimeUnit.MILLISECONDS);
+        result.whenComplete((_, _) -> schedule.cancel(false));
     }
 
     private CompletableFuture<?> triggerDeferredExecutions() {
diff --git a/server/src/test/java/io/crate/session/SessionTest.java b/server/src/test/java/io/crate/session/SessionTest.java
index df372cf85b..ca570501b3 100644
--- a/server/src/test/java/io/crate/session/SessionTest.java
+++ b/server/src/test/java/io/crate/session/SessionTest.java
@@ -38,9 +38,11 @@ import static org.mockito.Mockito.when;
 
 import java.util.Collections;
 import java.util.List;
+import java.util.concurrent.BlockingQueue;
 import java.util.concurrent.CompletableFuture;
 import java.util.concurrent.ScheduledExecutorService;
 import java.util.concurrent.ScheduledFuture;
+import java.util.concurrent.ScheduledThreadPoolExecutor;
 import java.util.concurrent.TimeUnit;
 
 import org.elasticsearch.client.ElasticsearchClient;
@@ -55,6 +57,7 @@ import io.crate.analyze.AnalyzedStatement;
 import io.crate.analyze.where.EqualityExtractorTest;
 import io.crate.common.collections.BlockingEvictingQueue;
 import io.crate.common.unit.TimeValue;
+import io.crate.data.InMemoryBatchIterator;
 import io.crate.data.Row;
 import io.crate.data.RowConsumer;
 import io.crate.exceptions.JobKilledException;
@@ -393,6 +396,55 @@ public class SessionTest extends CrateDummyClusterServiceUnitTest {
             .execute(eq(KillJobsNodeAction.INSTANCE), any(KillJobsNodeRequest.class));
     }
 
+    @Test
+    public void test_statement_timeout_schedule_is_removed_for_finished_jobs() throws Exception {
+        Planner planner = mock(Planner.class, Answers.RETURNS_MOCKS);
+        SQLExecutor sqlExecutor = SQLExecutor.builder(clusterService)
+            .setPlanner(planner)
+            .build();
+        when(planner.plan(any(AnalyzedStatement.class), any(PlannerContext.class)))
+            .thenReturn(
+                new Plan() {
+                    @Override
+                    public StatementType type() {
+                        return StatementType.INSERT;
+                    }
+
+                    @Override
+                    public void executeOrFail(DependencyCarrier dependencies,
+                                              PlannerContext plannerContext,
+                                              RowConsumer consumer,
+                                              Row params,
+                                              SubQueryResults subQueryResults) throws Exception {
+                        consumer.accept(InMemoryBatchIterator.empty(null), null);
+                    }
+
+                    @Override
+                    public CompletableFuture<BulkResponse> executeBulk(DependencyCarrier executor,
+                                                                       PlannerContext plannerContext,
+                                                                       List<Row> bulkParams,
+                                                                       SubQueryResults subQueryResults) {
+                        return new CompletableFuture<>();
+                    }
+                }
+            );
+
+        DependencyCarrier dependencies = sqlExecutor.dependencyMock;
+        when(dependencies.scheduler()).thenReturn(THREAD_POOL.scheduler());
+        Session session = sqlExecutor.createSession();
+        session.sessionSettings().statementTimeout(TimeValue.timeValueMinutes(30));
+
+        for (int i = 0; i < 10; i++) {
+            session.parse("S_1", "SELECT 1", List.of());
+            session.bind("P_1", "S_1", List.of(), null);
+            session.execute("P_1", 0, new BaseResultReceiver());
+            session.sync();
+        }
+
+        BlockingQueue<Runnable> queue = ((ScheduledThreadPoolExecutor) THREAD_POOL.scheduler()).getQueue();
+        assertThat(queue).isEmpty();
+    }
+
     @Test
     public void test_parsing_throws_an_error_on_exceeding_statement_timeout() throws Exception {
         Planner planner = mock(Planner.class, Answers.RETURNS_MOCKS);

```
