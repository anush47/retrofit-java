# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java', 'server/src/main/java/io/crate/session/Session.java']
- Developer Java files: ['server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java', 'server/src/main/java/io/crate/session/Session.java']
- Overlap Java files: ['server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java', 'server/src/main/java/io/crate/session/Session.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java', 'server/src/main/java/io/crate/session/Session.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java', 'server/src/main/java/io/crate/session/Session.java']
- Mismatched files: ['server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java', 'server/src/main/java/io/crate/session/Session.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -32,6 +32,7 @@
 import java.util.function.LongSupplier;
 
 import org.jetbrains.annotations.Nullable;
+import org.jetbrains.annotations.VisibleForTesting;
 
 import io.crate.common.annotations.ThreadSafe;
 import io.crate.expression.reference.sys.job.JobContext;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -32,6 +32,7 @@
- import java.util.function.LongSupplier;
- 
- import org.jetbrains.annotations.Nullable;
-+import org.jetbrains.annotations.VisibleForTesting;
- 
- import io.crate.common.annotations.ThreadSafe;
- import io.crate.expression.reference.sys.job.JobContext;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -227,7 +228,8 @@
         }
     }
 
-    void updateJobsLog(LogSink<JobContextLog> sink) {
+    @VisibleForTesting
+    public void updateJobsLog(LogSink<JobContextLog> sink) {
         long stamp = jobsLogLock.writeLock();
         try {
             sink.addAll(jobsLog);

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -227,7 +228,8 @@
-         }
-     }
- 
--    void updateJobsLog(LogSink<JobContextLog> sink) {
-+    @VisibleForTesting
-+    public void updateJobsLog(LogSink<JobContextLog> sink) {
-         long stamp = jobsLogLock.writeLock();
-         try {
-             sink.addAll(jobsLog);
+*No hunk*
```


### server/src/main/java/io/crate/session/Session.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -393,7 +393,7 @@
         try {
             preparedStmt = getSafeStmt(statementName);
         } catch (Throwable t) {
-            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), statementName, SQLExceptions.messageOf(t), sessionSettings.sessionUser());
+            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), "", SQLExceptions.messageOf(t), sessionSettings.sessionUser());
             throw t;
         }
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -393,7 +393,7 @@
-         try {
-             preparedStmt = getSafeStmt(statementName);
-         } catch (Throwable t) {
--            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), statementName, SQLExceptions.messageOf(t), sessionSettings.sessionUser());
-+            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), "", SQLExceptions.messageOf(t), sessionSettings.sessionUser());
-             throw t;
-         }
- 
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
diff --git a/server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java b/server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java
index a38e021742..54185fc4c7 100644
--- a/server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java
+++ b/server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java
@@ -32,6 +32,7 @@ import java.util.function.BooleanSupplier;
 import java.util.function.LongSupplier;
 
 import org.jetbrains.annotations.Nullable;
+import org.jetbrains.annotations.VisibleForTesting;
 
 import io.crate.common.annotations.ThreadSafe;
 import io.crate.expression.reference.sys.job.JobContext;
@@ -227,7 +228,8 @@ public class JobsLogs {
         }
     }
 
-    void updateJobsLog(LogSink<JobContextLog> sink) {
+    @VisibleForTesting
+    public void updateJobsLog(LogSink<JobContextLog> sink) {
         long stamp = jobsLogLock.writeLock();
         try {
             sink.addAll(jobsLog);
diff --git a/server/src/main/java/io/crate/session/Session.java b/server/src/main/java/io/crate/session/Session.java
index 74844d5e60..256ceabb7f 100644
--- a/server/src/main/java/io/crate/session/Session.java
+++ b/server/src/main/java/io/crate/session/Session.java
@@ -393,7 +393,7 @@ public class Session implements AutoCloseable {
         try {
             preparedStmt = getSafeStmt(statementName);
         } catch (Throwable t) {
-            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), statementName, SQLExceptions.messageOf(t), sessionSettings.sessionUser());
+            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), "", SQLExceptions.messageOf(t), sessionSettings.sessionUser());
             throw t;
         }
 
diff --git a/server/src/test/java/io/crate/session/SessionTest.java b/server/src/test/java/io/crate/session/SessionTest.java
index f17dfefa70..df372cf85b 100644
--- a/server/src/test/java/io/crate/session/SessionTest.java
+++ b/server/src/test/java/io/crate/session/SessionTest.java
@@ -24,6 +24,7 @@ package io.crate.session;
 import static io.crate.session.Session.UNNAMED;
 import static io.crate.testing.Asserts.assertThat;
 import static java.util.concurrent.CompletableFuture.completedFuture;
+import static org.assertj.core.api.Assertions.assertThat;
 import static org.assertj.core.api.Assertions.assertThatThrownBy;
 import static org.mockito.ArgumentMatchers.any;
 import static org.mockito.ArgumentMatchers.anyInt;
@@ -52,11 +53,13 @@ import org.mockito.stubbing.Answer;
 
 import io.crate.analyze.AnalyzedStatement;
 import io.crate.analyze.where.EqualityExtractorTest;
+import io.crate.common.collections.BlockingEvictingQueue;
 import io.crate.common.unit.TimeValue;
 import io.crate.data.Row;
 import io.crate.data.RowConsumer;
 import io.crate.exceptions.JobKilledException;
 import io.crate.execution.dml.BulkResponse;
+import io.crate.execution.engine.collect.stats.QueueSink;
 import io.crate.execution.jobs.kill.KillJobsNodeAction;
 import io.crate.execution.jobs.kill.KillJobsNodeRequest;
 import io.crate.planner.DependencyCarrier;
@@ -435,14 +438,26 @@ public class SessionTest extends CrateDummyClusterServiceUnitTest {
     }
 
     @Test
-    public void test_binding_with_removed_prepared_statement_throws() {
-        SQLExecutor sqlExecutor = SQLExecutor.builder(clusterService).build();
+    public void test_binding_with_removed_prepared_statement_throws_sstatement_not_found_and_logs_error() {
+        SQLExecutor sqlExecutor = SQLExecutor.of(clusterService);
+        sqlExecutor.jobsLogsEnabled = true;
+        sqlExecutor.jobsLogs.updateJobsLog(new QueueSink<>(new BlockingEvictingQueue<>(1), () -> {}));
+
         try (Session session = sqlExecutor.createSession()) {
-            session.parse("", "SELECT 1", Collections.emptyList());
-            session.close((byte) 'S', "");
-            assertThatThrownBy(() -> session.bind("", "", List.of(), null))
+            session.parse("S1", "SELECT 1", Collections.emptyList());
+            assertThat(sqlExecutor.jobsLogs.activeJobs()).isEmpty();
+            session.close((byte) 'S', "S1");
+            assertThatThrownBy(() -> session.bind("", "S1", List.of(), null))
                 .isExactlyInstanceOf(IllegalArgumentException.class)
-                .hasMessage("No statement found with name: ");
+                .hasMessage("No statement found with name: S1");
+
+            assertThat(sqlExecutor.jobsLogs.activeJobs()).isEmpty();
+            assertThat(sqlExecutor.jobsLogs.jobsLog()).satisfiesExactly(
+                x -> {
+                    assertThat(x.statement()).isEqualTo("");
+                    assertThat(x.errorMessage()).isEqualTo("No statement found with name: S1");
+                }
+            );
         }
     }
 

```
