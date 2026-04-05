# Phase 0 Inputs

- Mainline commit: 4bd09278693c5b2bf7349f5d3f5ec3836f32ae9f
- Backport commit: 5d168a4e9e16572a304e5530dcb9f9dadfc23216
- Java-only files for agentic phases: 3
- Developer auxiliary hunks (test + non-Java): 7

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['graylog2-server/src/main/java/org/graylog2/Configuration.java', 'graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java', 'graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java']
- Developer Java files: ['graylog2-server/src/main/java/org/graylog2/Configuration.java', 'graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java', 'graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java']
- Overlap Java files: ['graylog2-server/src/main/java/org/graylog2/Configuration.java', 'graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java', 'graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 4bd09278693c5b2bf7349f5d3f5ec3836f32ae9f Mon Sep 17 00:00:00 2001
From: Anton Ebel <anton.ebel@graylog.com>
Date: Tue, 30 Sep 2025 09:18:04 +0200
Subject: [PATCH] introduce global_inputs_only config to enforce global inputs
 (#23769)
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit

* introduce config to enforce global inputs

* add changelog

---------

Co-authored-by: Laura Bergenthal-Grotlüschen <laura.bergenthalgrotlueschen@graylog.com>
---
 changelog/unreleased/pr-23769.toml                        | 4 ++++
 .../src/main/java/org/graylog2/Configuration.java         | 7 +++++++
 .../rest/resources/system/inputs/InputsResource.java      | 4 ++--
 .../org/graylog2/web/resources/AppConfigResource.java     | 1 +
 .../src/main/resources/web-interface/config.js.template   | 3 ++-
 .../rest/resources/system/inputs/InputsResourceTest.java  | 8 ++++++++
 .../src/components/inputs/InputForm.tsx                   | 4 ++--
 graylog2-web-interface/src/util/AppConfig.ts              | 5 +++++
 8 files changed, 31 insertions(+), 5 deletions(-)
 create mode 100644 changelog/unreleased/pr-23769.toml

diff --git a/changelog/unreleased/pr-23769.toml b/changelog/unreleased/pr-23769.toml
new file mode 100644
index 0000000000..14a0bc3899
--- /dev/null
+++ b/changelog/unreleased/pr-23769.toml
@@ -0,0 +1,4 @@
+type = "a"
+message = "Introduce global_inputs_only config to enforce global inputs."
+
+pulls = ["23769"]
diff --git a/graylog2-server/src/main/java/org/graylog2/Configuration.java b/graylog2-server/src/main/java/org/graylog2/Configuration.java
index 9d894f659c..b30533dfc0 100644
--- a/graylog2-server/src/main/java/org/graylog2/Configuration.java
+++ b/graylog2-server/src/main/java/org/graylog2/Configuration.java
@@ -298,6 +298,9 @@ public class Configuration extends CaConfiguration implements CommonNodeConfigur
     @Parameter(value = INSTALL_OUTPUT_BUFFER_DRAINING_MAX_RETRIES, validators = PositiveIntegerValidator.class)
     private int installOutputBufferDrainingMaxRetries = DEFAULT_INSTALL_RETRIES;
 
+    @Parameter(value = "global_inputs_only")
+    private boolean globalInputsOnly = false;
+
     public boolean maintainsStreamAwareFieldTypes() {
         return streamAwareFieldTypes;
     }
@@ -721,4 +724,8 @@ public class Configuration extends CaConfiguration implements CommonNodeConfigur
     public boolean withInputs() {
         return true;
     }
+
+    public boolean isGlobalInputsOnly() {
+        return globalInputsOnly;
+    }
 }
diff --git a/graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java b/graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java
index a5ecab6537..c35d311622 100644
--- a/graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java
+++ b/graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java
@@ -306,8 +306,8 @@ public class InputsResource extends AbstractInputsResource {
     }
 
     private void throwBadRequestIfNotGlobal(InputCreateRequest lr) {
-        if (config.isCloud() && !lr.global()) {
-            throw new BadRequestException("Only global inputs are allowed in the cloud environment!");
+        if ((config.isCloud() || config.isGlobalInputsOnly()) && !lr.global()) {
+            throw new BadRequestException("Only global inputs are allowed!");
         }
     }
 }
diff --git a/graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java b/graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java
index e12648630d..29ea387d0d 100644
--- a/graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java
+++ b/graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java
@@ -105,6 +105,7 @@ public class AppConfigResource {
                 .put("telemetry", toPrettyJsonString(telemetryConfiguration.telemetryFrontendSettings()))
                 .put("contentStream", toPrettyJsonString((contentStreamConfiguration.contentStreamFrontendSettings())))
                 .put("branding", toPrettyJsonString(customizationConfig))
+                .put("globalInputsOnly", configuration.isGlobalInputsOnly())
                 .build();
         return templateEngine.transform(template, model);
     }
diff --git a/graylog2-server/src/main/resources/web-interface/config.js.template b/graylog2-server/src/main/resources/web-interface/config.js.template
index ab18a86dd4..48c38faf31 100644
--- a/graylog2-server/src/main/resources/web-interface/config.js.template
+++ b/graylog2-server/src/main/resources/web-interface/config.js.template
@@ -7,5 +7,6 @@ window.appConfig = {
   featureFlags: ${featureFlags},
   telemetry: ${telemetry},
   contentStream: ${contentStream},
-  branding: ${branding}
+  branding: ${branding},
+  globalInputsOnly: ${globalInputsOnly}
 };
diff --git a/graylog2-server/src/test/java/org/graylog2/rest/resources/system/inputs/InputsResourceTest.java b/graylog2-server/src/test/java/org/graylog2/rest/resources/system/inputs/InputsResourceTest.java
index d3d3ea91e5..259b491f25 100644
--- a/graylog2-server/src/test/java/org/graylog2/rest/resources/system/inputs/InputsResourceTest.java
+++ b/graylog2-server/src/test/java/org/graylog2/rest/resources/system/inputs/InputsResourceTest.java
@@ -102,6 +102,14 @@ class InputsResourceTest {
                 .hasMessageContaining("Only global inputs");
     }
 
+    @Test
+    void testCreateNotGlobalInputWhenIsGlobalInputOnly() {
+        when(configuration.isGlobalInputsOnly()).thenReturn(true);
+
+        assertThatThrownBy(() -> inputsResource.create(false, getCR(false))).isInstanceOf(BadRequestException.class)
+                .hasMessageContaining("Only global inputs");
+    }
+
     @Test
     void testCreateNotCloudCompatibleInputInCloud() throws Exception {
         when(configuration.isCloud()).thenReturn(true);
diff --git a/graylog2-web-interface/src/components/inputs/InputForm.tsx b/graylog2-web-interface/src/components/inputs/InputForm.tsx
index be05067224..cba00b7919 100644
--- a/graylog2-web-interface/src/components/inputs/InputForm.tsx
+++ b/graylog2-web-interface/src/components/inputs/InputForm.tsx
@@ -80,7 +80,7 @@ const InputForm = ({
     const newData = {
       ...data,
       ...{
-        global: AppConfig.isCloud() || global,
+        global: AppConfig.isCloud() || AppConfig.globalInputsOnly() || global,
         node: node,
       },
     };
@@ -135,7 +135,7 @@ const InputForm = ({
       cancelAction={onCancel}>
       {description && <Alert bsStyle="info">{description}</Alert>}
       <HideOnCloud>
-        <NodeOrGlobalSelect onChange={handleChange} global={global} node={node} />
+        {!AppConfig.globalInputsOnly() && (<NodeOrGlobalSelect onChange={handleChange} global={global} node={node} />)}
       </HideOnCloud>
     </ConfigurationForm>
   );
diff --git a/graylog2-web-interface/src/util/AppConfig.ts b/graylog2-web-interface/src/util/AppConfig.ts
index 91ae8f7101..5644cc436a 100644
--- a/graylog2-web-interface/src/util/AppConfig.ts
+++ b/graylog2-web-interface/src/util/AppConfig.ts
@@ -69,6 +69,7 @@ export type AppConfigs = {
   telemetry: { api_key: string; host: string; enabled: boolean };
   contentStream: { refresh_interval: string; rss_url: string };
   branding: Branding | undefined;
+  globalInputsOnly: boolean;
 };
 
 declare global {
@@ -142,6 +143,10 @@ const AppConfig = {
   branding(): Branding | undefined {
     return appConfig()?.branding;
   },
+
+  globalInputsOnly():boolean {
+    return appConfig().globalInputsOnly;
+  },
 };
 
 export default AppConfig;
-- 
2.43.0


```
