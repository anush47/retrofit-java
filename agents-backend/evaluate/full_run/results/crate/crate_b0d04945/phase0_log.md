# Phase 0 Inputs

- Mainline commit: b0d0494589f281cc6794c318dacb4d02cbbfc465
- Backport commit: de5f0a0d967e0a5d1695906ccc953b383caf90b5
- Java-only files for agentic phases: 2
- Developer auxiliary hunks (test + non-Java): 3

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java', 'server/src/main/java/io/crate/session/Session.java']
- Developer Java files: ['server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java', 'server/src/main/java/io/crate/session/Session.java']
- Overlap Java files: ['server/src/main/java/io/crate/execution/engine/collect/stats/JobsLogs.java', 'server/src/main/java/io/crate/session/Session.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From b0d0494589f281cc6794c318dacb4d02cbbfc465 Mon Sep 17 00:00:00 2001
From: Mathias Fussenegger <f.mathias@zignar.net>
Date: Mon, 24 Feb 2025 13:36:47 +0100
Subject: [PATCH] Use empty statement for jobs logs entry on missing prepared
 statements

Follow up to https://github.com/crate/crate/pull/17480
---
 .../engine/collect/stats/JobsLogs.java        |  4 ++-
 .../main/java/io/crate/session/Session.java   |  2 +-
 .../java/io/crate/session/SessionTest.java    | 27 ++++++++++++++-----
 3 files changed, 25 insertions(+), 8 deletions(-)

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
 
-- 
2.43.0


```
