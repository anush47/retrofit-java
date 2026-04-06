# Phase 0 Inputs

- Mainline commit: 8c5d5fa9168e253a340abd6fba604c27603e9275
- Backport commit: a16dcd521ff8c7323830590a23db43c6466ddbfb
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 3

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/role/TransportAlterRoleAction.java']
- Developer Java files: ['server/src/main/java/io/crate/role/TransportAlterRoleAction.java']
- Overlap Java files: ['server/src/main/java/io/crate/role/TransportAlterRoleAction.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 8c5d5fa9168e253a340abd6fba604c27603e9275 Mon Sep 17 00:00:00 2001
From: baur <baurzhansahariev@gmail.com>
Date: Thu, 29 Aug 2024 11:19:45 +0200
Subject: [PATCH] Fix an issue preventing to update password for users with jwt
 properties

---
 docs/appendices/release-notes/5.8.3.rst       |  4 +-
 .../crate/role/TransportAlterRoleAction.java  |  4 +-
 .../crate/role/TransportRoleActionTest.java   | 62 ++++++++++++++++++-
 3 files changed, 67 insertions(+), 3 deletions(-)

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
index 8ebddb6bfa..4e823792da 100644
--- a/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
+++ b/server/src/main/java/io/crate/role/TransportAlterRoleAction.java
@@ -156,7 +156,9 @@ public class TransportAlterRoleAction extends TransportMasterNodeAction<AlterRol
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
index 163fb9ef0f..9783fa7307 100644
--- a/server/src/test/java/io/crate/role/TransportRoleActionTest.java
+++ b/server/src/test/java/io/crate/role/TransportRoleActionTest.java
@@ -353,6 +353,66 @@ public class TransportRoleActionTest extends CrateDummyClusterServiceUnitTest {
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
+            false, // No reset, keep jwt
+            Map.of()
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
+            false, // No reset, keep jwt
+            Map.of()
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
@@ -598,6 +658,6 @@ public class TransportRoleActionTest extends CrateDummyClusterServiceUnitTest {
     }
 
     private static Map<String, Role> roles(Metadata.Builder mdBuilder) {
-        return ((RolesMetadata) mdBuilder.build().custom(RolesMetadata.TYPE)).roles();
+        return ((RolesMetadata) mdBuilder.getCustom(RolesMetadata.TYPE)).roles();
     }
 }
-- 
2.43.0


```
