# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/role/TransportAlterRoleAction.java']
- Developer Java files: ['server/src/main/java/io/crate/role/TransportAlterRoleAction.java']
- Overlap Java files: ['server/src/main/java/io/crate/role/TransportAlterRoleAction.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/role/TransportAlterRoleAction.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/role/TransportAlterRoleAction.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/role/TransportAlterRoleAction.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -147,7 +147,9 @@
             var newSecureHash = secureHash != null ? secureHash : (resetPassword ? null : role.password());
             var newJwtProperties = jwtProperties != null ? jwtProperties : (resetJwtProperties ? null : role.jwtProperties());
 
-            if (newMetadata.contains(newJwtProperties)) {
+            if (jwtProperties != null && newMetadata.contains(newJwtProperties)) {
+                // If we have a clash it could be that we tried to keep jwt and update another property.
+                // We throw only if we actually tried to update JWT properties.
                 throw new RoleAlreadyExistsException(
                     "Another role with the same combination of iss/username jwt properties already exists"
                 );

```

Generated
```diff
@@ -147,7 +147,9 @@
             var newSecureHash = secureHash != null ? secureHash : (resetPassword ? null : role.password());
             var newJwtProperties = jwtProperties != null ? jwtProperties : (resetJwtProperties ? null : role.jwtProperties());
 
-            if (newMetadata.contains(newJwtProperties)) {
+            if (jwtProperties != null && newMetadata.contains(newJwtProperties)) {
+                // If we have a clash it could be that we tried to keep jwt and update another property.
+                // We throw only if we actually tried to update JWT properties.
                 throw new RoleAlreadyExistsException(
                     "Another role with the same combination of iss/username jwt properties already exists"
                 );

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/role/TransportAlterRoleAction.java b/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
index e78d08a628..8aa2bf74a2 100644
--- a/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
+++ b/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
@@ -147,7 +147,9 @@ public class TransportAlterRoleAction extends TransportMasterNodeAction<AlterRol
             var newSecureHash = secureHash != null ? secureHash : (resetPassword ? null : role.password());
             var newJwtProperties = jwtProperties != null ? jwtProperties : (resetJwtProperties ? null : role.jwtProperties());
 
-            if (newMetadata.contains(newJwtProperties)) {
+            if (jwtProperties != null && newMetadata.contains(newJwtProperties)) {
+                // If we have a clash it could be that we tried to keep jwt and update another property.
+                // We throw only if we actually tried to update JWT properties.
                 throw new RoleAlreadyExistsException(
                     "Another role with the same combination of iss/username jwt properties already exists"
                 );

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/role/TransportAlterRoleAction.java b/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
index e78d08a628..8aa2bf74a2 100644
--- a/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
+++ b/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
@@ -147,7 +147,9 @@ public class TransportAlterRoleAction extends TransportMasterNodeAction<AlterRol
             var newSecureHash = secureHash != null ? secureHash : (resetPassword ? null : role.password());
             var newJwtProperties = jwtProperties != null ? jwtProperties : (resetJwtProperties ? null : role.jwtProperties());
 
-            if (newMetadata.contains(newJwtProperties)) {
+            if (jwtProperties != null && newMetadata.contains(newJwtProperties)) {
+                // If we have a clash it could be that we tried to keep jwt and update another property.
+                // We throw only if we actually tried to update JWT properties.
                 throw new RoleAlreadyExistsException(
                     "Another role with the same combination of iss/username jwt properties already exists"
                 );

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/docs/appendices/release-notes/5.8.3.rst b/docs/appendices/release-notes/5.8.3.rst
index 413e3b80da..bdee7738e6 100644
--- a/docs/appendices/release-notes/5.8.3.rst
+++ b/docs/appendices/release-notes/5.8.3.rst
@@ -47,4 +47,6 @@ See the :ref:`version_5.8.0` release notes for a full list of changes in the
 Fixes
 =====
 
-None
+- Fixed an issue that caused failure of ``ALTER ROLE`` statements updating or
+  resetting password of a user with specified :ref:`JWT <create-user-jwt>`
+  properties.
diff --git a/server/src/main/java/io/crate/role/TransportAlterRoleAction.java b/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
index e78d08a628..8aa2bf74a2 100644
--- a/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
+++ b/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
@@ -147,7 +147,9 @@ public class TransportAlterRoleAction extends TransportMasterNodeAction<AlterRol
             var newSecureHash = secureHash != null ? secureHash : (resetPassword ? null : role.password());
             var newJwtProperties = jwtProperties != null ? jwtProperties : (resetJwtProperties ? null : role.jwtProperties());
 
-            if (newMetadata.contains(newJwtProperties)) {
+            if (jwtProperties != null && newMetadata.contains(newJwtProperties)) {
+                // If we have a clash it could be that we tried to keep jwt and update another property.
+                // We throw only if we actually tried to update JWT properties.
                 throw new RoleAlreadyExistsException(
                     "Another role with the same combination of iss/username jwt properties already exists"
                 );
diff --git a/server/src/test/java/io/crate/role/TransportRoleActionTest.java b/server/src/test/java/io/crate/role/TransportRoleActionTest.java
index 067b3b9d48..bd221c9637 100644
--- a/server/src/test/java/io/crate/role/TransportRoleActionTest.java
+++ b/server/src/test/java/io/crate/role/TransportRoleActionTest.java
@@ -341,6 +341,64 @@ public class TransportRoleActionTest extends CrateDummyClusterServiceUnitTest {
         );
     }
 
+    @Test
+    public void test_alter_user_change_or_reset_password_and_keep_jwt() {
+        Map<String, Role> roleWithJwtAndPassword = new HashMap<>();
+        var oldJwtProperties = new JwtProperties("https:dummy.org", "test", null);
+        roleWithJwtAndPassword.put("John", userOf(
+            "John",
+            Set.of(),
+            new HashSet<>(),
+            getSecureHash("old-pwd"),
+            oldJwtProperties
+           )
+        );
+        var oldRolesMetadata = new RolesMetadata(roleWithJwtAndPassword);
+        Metadata.Builder mdBuilder = Metadata.builder()
+            .putCustom(RolesMetadata.TYPE, oldRolesMetadata);
+        var newPwd = getSecureHash("new-pwd");
+
+        // Update password
+        boolean exists = TransportAlterRoleAction.alterRole(
+            mdBuilder,
+            "John",
+            newPwd,
+            null,
+            false,
+            false // No reset, keep jwt
+        );
+        assertThat(exists).isTrue();
+        assertThat(roles(mdBuilder)).containsExactlyInAnyOrderEntriesOf(
+            Map.of("John", userOf(
+                "John",
+                Set.of(),
+                new HashSet<>(),
+                newPwd,
+                oldJwtProperties)
+            )
+        );
+
+        // Reset password
+        exists = TransportAlterRoleAction.alterRole(
+            mdBuilder,
+            "John",
+            null,
+            null,
+            true, // Reset password
+            false // No reset, keep jwt
+        );
+        assertThat(exists).isTrue();
+        assertThat(roles(mdBuilder)).containsExactlyInAnyOrderEntriesOf(
+            Map.of("John", userOf(
+                "John",
+                Set.of(),
+                new HashSet<>(),
+                null, // Password has been reset
+                oldJwtProperties)
+            )
+        );
+    }
+
     @Test
     public void test_alter_user_reset_jwt_and_password() throws Exception {
         Map<String, Role> roleWithJwtAndPassword = new HashMap<>();
@@ -410,6 +468,6 @@ public class TransportRoleActionTest extends CrateDummyClusterServiceUnitTest {
 
 
     private static Map<String, Role> roles(Metadata.Builder mdBuilder) {
-        return ((RolesMetadata) mdBuilder.build().custom(RolesMetadata.TYPE)).roles();
+        return ((RolesMetadata) mdBuilder.getCustom(RolesMetadata.TYPE)).roles();
     }
 }

```
