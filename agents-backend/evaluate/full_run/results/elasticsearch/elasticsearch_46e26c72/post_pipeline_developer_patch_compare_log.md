# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java']
- Developer Java files: ['server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java']
- Overlap Java files: ['server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java']

## File State Comparison
- Compared files: ['server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java']
- Mismatched files: ['server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -54,7 +54,11 @@
         loadOverrides(output, properties);
         output.put(input);
         replaceForcedSettings(output);
-        output.replacePropertyPlaceholders();
+        try {
+            output.replacePropertyPlaceholders();
+        } catch (Exception e) {
+            throw new SettingsException("Failed to replace property placeholders from [" + configFile.getFileName() + "]", e);
+        }
         ensureSpecialSettingsExist(output, defaultNodeName);
 
         return new Environment(output.build(), configDir);

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,13 +1 @@-@@ -54,7 +54,11 @@
-         loadOverrides(output, properties);
-         output.put(input);
-         replaceForcedSettings(output);
--        output.replacePropertyPlaceholders();
-+        try {
-+            output.replacePropertyPlaceholders();
-+        } catch (Exception e) {
-+            throw new SettingsException("Failed to replace property placeholders from [" + configFile.getFileName() + "]", e);
-+        }
-         ensureSpecialSettingsExist(output, defaultNodeName);
- 
-         return new Environment(output.build(), configDir);
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
diff --git a/docs/changelog/114552.yaml b/docs/changelog/114552.yaml
new file mode 100644
index 00000000000..00e2f95b503
--- /dev/null
+++ b/docs/changelog/114552.yaml
@@ -0,0 +1,5 @@
+pr: 114552
+summary: Improve exception message for bad environment variable placeholders in settings
+area: Infra/Settings
+type: enhancement
+issues: [110858]
diff --git a/server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java b/server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java
index 2e606f7b83e..94227aed40d 100644
--- a/server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java
+++ b/server/src/main/java/org/elasticsearch/node/InternalSettingsPreparer.java
@@ -54,7 +54,11 @@ public class InternalSettingsPreparer {
         loadOverrides(output, properties);
         output.put(input);
         replaceForcedSettings(output);
-        output.replacePropertyPlaceholders();
+        try {
+            output.replacePropertyPlaceholders();
+        } catch (Exception e) {
+            throw new SettingsException("Failed to replace property placeholders from [" + configFile.getFileName() + "]", e);
+        }
         ensureSpecialSettingsExist(output, defaultNodeName);
 
         return new Environment(output.build(), configDir);
diff --git a/server/src/test/java/org/elasticsearch/node/InternalSettingsPreparerTests.java b/server/src/test/java/org/elasticsearch/node/InternalSettingsPreparerTests.java
index 3d406fff79e..32edcc0ad82 100644
--- a/server/src/test/java/org/elasticsearch/node/InternalSettingsPreparerTests.java
+++ b/server/src/test/java/org/elasticsearch/node/InternalSettingsPreparerTests.java
@@ -86,6 +86,20 @@ public class InternalSettingsPreparerTests extends ESTestCase {
         }
     }
 
+    public void testReplacePlaceholderFailure() {
+        try {
+            InternalSettingsPreparer.prepareEnvironment(
+                Settings.builder().put(baseEnvSettings).put("cluster.name", "${ES_CLUSTER_NAME}").build(),
+                emptyMap(),
+                null,
+                () -> "default_node_name"
+            );
+            fail("Expected SettingsException");
+        } catch (SettingsException e) {
+            assertEquals("Failed to replace property placeholders from [elasticsearch.yml]", e.getMessage());
+        }
+    }
+
     public void testSecureSettings() {
         MockSecureSettings secureSettings = new MockSecureSettings();
         secureSettings.setString("foo", "secret");

```
