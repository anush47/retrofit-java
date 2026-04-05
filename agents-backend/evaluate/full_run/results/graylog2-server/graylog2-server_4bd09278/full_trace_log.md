# Full Trace of Agentic File Edits

## Attempt #1

### Final Output Diff
**graylog2-server/src/main/java/org/graylog2/Configuration.java** [replace]
```java
// --- OLD ---
<developer patch fast path>
// --- NEW ---
diff --git a/graylog2-server/src/main/java/org/graylog2/Configuration.java b/graylog2-server/src/main/java/org/graylog2/Configuration.java
index 2420fd9b9a..2e5a01d8ac 100644
--- a/graylog2-server/src/main/java/org/graylog2/Configuration.java
+++ b/graylog2-server/src/main/java/org/graylog2/Configuration.java
@@ -295,6 +295,9 @@ public class Configuration extends CaConfiguration implements CommonNodeConfigur
     @Parameter(value = INSTALL_OUTPUT_BUFFER_DRAINING_MAX_RETRIES, validators = PositiveIntegerValidator.class)
     private int installOutputBufferDrainingMaxRetries = DEFAULT_INSTALL_RETRIES;
 
+    @Parameter(value = "global_inputs_only")
+    private boolean globalInputsOnly = false;
+
     public boolean maintainsStreamAwareFieldTypes() {
         return streamAwareFieldTypes;
     }
@@ -714,4 +717,8 @@ public class Configuration extends CaConfiguration implements CommonNodeConfigur
     public boolean withInputs() {
         return true;
     }
+
+    public boolean isGlobalInputsOnly() {
+        return globalInputsOnly;
+    }
 }
```
**graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java** [replace]
```java
// --- OLD ---
<developer patch fast path>
// --- NEW ---
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
```
**graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java** [replace]
```java
// --- OLD ---
<developer patch fast path>
// --- NEW ---
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
```