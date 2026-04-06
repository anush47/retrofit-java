# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/role/Role.java']
- Developer Java files: ['server/src/main/java/io/crate/role/Role.java']
- Overlap Java files: ['server/src/main/java/io/crate/role/Role.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/role/Role.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/role/Role.java']
- Mismatched files: ['server/src/main/java/io/crate/role/Role.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/role/Role.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -118,7 +118,7 @@
             boolean login = false;
             SecureHash secureHash = null;
             JwtProperties jwtProperties = null;
-            Map<String, Object> sessionSettings = null;
+            Map<String, Object> sessionSettings = new HashMap<>();
             while (parser.nextToken() == XContentParser.Token.FIELD_NAME) {
                 switch (parser.currentName()) {
                     case "login":

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -118,7 +118,7 @@
-             boolean login = false;
-             SecureHash secureHash = null;
-             JwtProperties jwtProperties = null;
--            Map<String, Object> sessionSettings = null;
-+            Map<String, Object> sessionSettings = new HashMap<>();
-             while (parser.nextToken() == XContentParser.Token.FIELD_NAME) {
-                 switch (parser.currentName()) {
-                     case "login":
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
diff --git a/docs/appendices/release-notes/5.9.2.rst b/docs/appendices/release-notes/5.9.2.rst
index 04c0ed8766..f479951498 100644
--- a/docs/appendices/release-notes/5.9.2.rst
+++ b/docs/appendices/release-notes/5.9.2.rst
@@ -47,4 +47,5 @@ See the :ref:`version_5.9.0` release notes for a full list of changes in the
 Fixes
 =====
 
-None
+- Fixed a BWC issue resulting in an exception when using custom user/roles
+  created on a CrateDB version < :ref:`version_5.9.0`.
diff --git a/server/src/main/java/io/crate/role/Role.java b/server/src/main/java/io/crate/role/Role.java
index e1f1a50657..6fa7376430 100644
--- a/server/src/main/java/io/crate/role/Role.java
+++ b/server/src/main/java/io/crate/role/Role.java
@@ -118,7 +118,7 @@ public class Role implements Writeable, ToXContent {
             boolean login = false;
             SecureHash secureHash = null;
             JwtProperties jwtProperties = null;
-            Map<String, Object> sessionSettings = null;
+            Map<String, Object> sessionSettings = new HashMap<>();
             while (parser.nextToken() == XContentParser.Token.FIELD_NAME) {
                 switch (parser.currentName()) {
                     case "login":
diff --git a/server/src/test/java/io/crate/role/RolePropertiesTest.java b/server/src/test/java/io/crate/role/RolePropertiesTest.java
index a7c1ab54cf..bcf7186372 100644
--- a/server/src/test/java/io/crate/role/RolePropertiesTest.java
+++ b/server/src/test/java/io/crate/role/RolePropertiesTest.java
@@ -24,13 +24,20 @@ package io.crate.role;
 import static org.assertj.core.api.Assertions.assertThat;
 import static org.assertj.core.api.Assertions.assertThatThrownBy;
 
+import java.io.IOException;
 import java.util.Map;
 import java.util.Set;
 
 import org.elasticsearch.Version;
+import org.elasticsearch.common.Strings;
 import org.elasticsearch.common.io.stream.BytesStreamOutput;
 import org.elasticsearch.common.io.stream.StreamInput;
 import org.elasticsearch.common.settings.SecureString;
+import org.elasticsearch.common.xcontent.DeprecationHandler;
+import org.elasticsearch.common.xcontent.NamedXContentRegistry;
+import org.elasticsearch.common.xcontent.XContentBuilder;
+import org.elasticsearch.common.xcontent.XContentParser;
+import org.elasticsearch.common.xcontent.json.JsonXContent;
 import org.junit.Test;
 
 import io.crate.metadata.settings.session.SessionSettingRegistry;
@@ -117,4 +124,21 @@ public class RolePropertiesTest {
         assertThat(actual.jwtProperties()).isNull();
         assertThat(actual.sessionSettings()).isEqualTo(Map.of());
     }
+
+    @Test
+    public void test_can_read_empty_role_properties_from_x_content() throws IOException {
+        XContentBuilder xContentBuilder = JsonXContent.builder();
+        xContentBuilder.startObject();
+        xContentBuilder.endObject();
+
+        XContentParser parser = JsonXContent.JSON_XCONTENT.createParser(
+            NamedXContentRegistry.EMPTY,
+            DeprecationHandler.THROW_UNSUPPORTED_OPERATION,
+            Strings.toString(xContentBuilder));
+        Role.Properties properties = Role.Properties.fromXContent(parser);
+
+        assertThat(properties.jwtProperties()).isNull();
+        assertThat(properties.password()).isNull();
+        assertThat(properties.sessionSettings()).isEqualTo(Map.of()); 
+    }
 }

```
