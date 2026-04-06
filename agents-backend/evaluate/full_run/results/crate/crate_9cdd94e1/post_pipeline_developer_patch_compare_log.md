# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/session/Session.java']
- Developer Java files: ['server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/session/Session.java']
- Overlap Java files: ['server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/session/Session.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/session/Session.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/session/Session.java']
- Mismatched files: ['server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -602,6 +602,8 @@
     private void handleBindMessage(ByteBuf buffer, Channel channel) {
         String portalName = readCString(buffer);
         String statementName = readCString(buffer);
+        assert portalName != null : "portalName cannot be null";
+        assert statementName != null : "statementName cannot be null";
 
         FormatCodes.FormatCode[] formatCodes = FormatCodes.fromBuffer(buffer);
 

```

Generated
```diff
@@ -603,6 +603,8 @@
         String portalName = readCString(buffer);
         String statementName = readCString(buffer);
 
+        assert portalName != null : "portalName cannot be null";
+        assert statementName != null : "statementName cannot be null";
         FormatCodes.FormatCode[] formatCodes = FormatCodes.fromBuffer(buffer);
 
         short numParams = buffer.readShort();

```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1,9 @@-@@ -602,6 +602,8 @@
-     private void handleBindMessage(ByteBuf buffer, Channel channel) {
+@@ -603,6 +603,8 @@
          String portalName = readCString(buffer);
          String statementName = readCString(buffer);
+ 
 +        assert portalName != null : "portalName cannot be null";
 +        assert statementName != null : "statementName cannot be null";
- 
          FormatCodes.FormatCode[] formatCodes = FormatCodes.fromBuffer(buffer);
  
+         short numParams = buffer.readShort();

```


### server/src/main/java/io/crate/session/Session.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -393,7 +393,7 @@
         try {
             preparedStmt = getSafeStmt(statementName);
         } catch (Throwable t) {
-            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), null, SQLExceptions.messageOf(t), sessionSettings.sessionUser());
+            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), statementName, SQLExceptions.messageOf(t), sessionSettings.sessionUser());
             throw t;
         }
 

```

Generated
```diff
@@ -393,7 +393,7 @@
         try {
             preparedStmt = getSafeStmt(statementName);
         } catch (Throwable t) {
-            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), null, SQLExceptions.messageOf(t), sessionSettings.sessionUser());
+            jobsLogs.logPreExecutionFailure(UUIDs.dirtyUUID(), statementName, SQLExceptions.messageOf(t), sessionSettings.sessionUser());
             throw t;
         }
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
index 4c40be2f5a..6dab15d258 100644
--- a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
+++ b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
@@ -603,6 +603,8 @@ public class PostgresWireProtocol {
         String portalName = readCString(buffer);
         String statementName = readCString(buffer);
 
+        assert portalName != null : "portalName cannot be null";
+        assert statementName != null : "statementName cannot be null";
         FormatCodes.FormatCode[] formatCodes = FormatCodes.fromBuffer(buffer);
 
         short numParams = buffer.readShort();
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
 

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
index 4c40be2f5a..6dab15d258 100644
--- a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
+++ b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
@@ -603,6 +603,8 @@ public class PostgresWireProtocol {
         String portalName = readCString(buffer);
         String statementName = readCString(buffer);
 
+        assert portalName != null : "portalName cannot be null";
+        assert statementName != null : "statementName cannot be null";
         FormatCodes.FormatCode[] formatCodes = FormatCodes.fromBuffer(buffer);
 
         short numParams = buffer.readShort();
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
 

```
## Full Developer Backport Patch (full commit diff)
```diff
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

```
