# Phase 0 Inputs

- Mainline commit: 9cdd94e1c1bd2b594bb9546aa86188c61cdd695a
- Backport commit: 8de35b2287cf3e7fe63a33c26f06168f4353ebfe
- Java-only files for agentic phases: 2
- Developer auxiliary hunks (test + non-Java): 2

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/session/Session.java']
- Developer Java files: ['server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/session/Session.java']
- Overlap Java files: ['server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/session/Session.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 9cdd94e1c1bd2b594bb9546aa86188c61cdd695a Mon Sep 17 00:00:00 2001
From: jeeminso <jeeminso@gmail.com>
Date: Thu, 20 Feb 2025 16:48:29 +0900
Subject: [PATCH] Fix NPE due to JobContext.stmt incorrectly set to null

---
 docs/appendices/release-notes/5.10.2.rst             |  3 +++
 .../protocols/postgres/PostgresWireProtocol.java     |  2 ++
 server/src/main/java/io/crate/session/Session.java   |  2 +-
 .../src/test/java/io/crate/session/SessionTest.java  | 12 ++++++++++++
 4 files changed, 18 insertions(+), 1 deletion(-)

diff --git a/docs/appendices/release-notes/5.10.2.rst b/docs/appendices/release-notes/5.10.2.rst
index e582a0c0cc..a57deb0641 100644
--- a/docs/appendices/release-notes/5.10.2.rst
+++ b/docs/appendices/release-notes/5.10.2.rst
@@ -59,3 +59,6 @@ Fixes
     DELETE FROM t WHERE day < now() - INTERVAL '3 days';
 
   where 'day' is ``TIMESTAMP`` type that is also the ``PARTITIONED BY`` column.
+
+- Fixed an issue that caused a ``NullPointerException`` when binding to a
+  non-existing prepared statement via PostgreSQL wire protocol.
diff --git a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
index 4c40be2f5a..4286060220 100644
--- a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
+++ b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
@@ -602,6 +602,8 @@ public class PostgresWireProtocol {
     private void handleBindMessage(ByteBuf buffer, Channel channel) {
         String portalName = readCString(buffer);
         String statementName = readCString(buffer);
+        assert portalName != null : "portalName cannot be null";
+        assert statementName != null : "statementName cannot be null";
 
         FormatCodes.FormatCode[] formatCodes = FormatCodes.fromBuffer(buffer);
 
diff --git a/server/src/main/java/io/crate/session/Session.java b/server/src/main/java/io/crate/session/Session.java
index fd5640333b..74844d5e60 100644
--- a/server/src/main/java/io/crate/session/Session.java
+++ b/server/src/main/java/io/crate/session/Session.java
@@ -393,7 +393,7 @@ public class Session implements AutoCloseable {
         try {
             preparedStmt = getSafeStmt(statementName);
         } catch (Throwable t) {
-            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), null, SQLExceptions.messageOf(t), sessionSettings.sessionUser());
+            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), statementName, SQLExceptions.messageOf(t), sessionSettings.sessionUser());
             throw t;
         }
 
diff --git a/server/src/test/java/io/crate/session/SessionTest.java b/server/src/test/java/io/crate/session/SessionTest.java
index b9de91dfe6..f17dfefa70 100644
--- a/server/src/test/java/io/crate/session/SessionTest.java
+++ b/server/src/test/java/io/crate/session/SessionTest.java
@@ -434,4 +434,16 @@ public class SessionTest extends CrateDummyClusterServiceUnitTest {
         }
     }
 
+    @Test
+    public void test_binding_with_removed_prepared_statement_throws() {
+        SQLExecutor sqlExecutor = SQLExecutor.builder(clusterService).build();
+        try (Session session = sqlExecutor.createSession()) {
+            session.parse("", "SELECT 1", Collections.emptyList());
+            session.close((byte) 'S', "");
+            assertThatThrownBy(() -> session.bind("", "", List.of(), null))
+                .isExactlyInstanceOf(IllegalArgumentException.class)
+                .hasMessage("No statement found with name: ");
+        }
+    }
+
 }
-- 
2.43.0


```
