# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java']
- Developer Java files: ['libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java']
- Overlap Java files: ['libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java']

## File State Comparison
- Compared files: ['libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java']
- Mismatched files: ['libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -32,7 +32,7 @@
     void check$java_net_URLClassLoader$(Class<?> callerClass, String name, URL[] urls, ClassLoader parent, URLStreamHandlerFactory factory);
 
     // Process creation
-    void check$$start(Class<?> callerClass, ProcessBuilder that, ProcessBuilder.Redirect[] redirects);
+    void check$$start(Class<?> callerClass, ProcessBuilder that);
 
     void check$java_lang_ProcessBuilder$startPipeline(Class<?> callerClass, List<ProcessBuilder> builders);
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -32,7 +32,7 @@
-     void check$java_net_URLClassLoader$(Class<?> callerClass, String name, URL[] urls, ClassLoader parent, URLStreamHandlerFactory factory);
- 
-     // Process creation
--    void check$$start(Class<?> callerClass, ProcessBuilder that, ProcessBuilder.Redirect[] redirects);
-+    void check$$start(Class<?> callerClass, ProcessBuilder that);
- 
-     void check$java_lang_ProcessBuilder$startPipeline(Class<?> callerClass, List<ProcessBuilder> builders);
- 
+*No hunk*
```


### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -70,7 +70,7 @@
     }
 
     @Override
-    public void check$$start(Class<?> callerClass, ProcessBuilder processBuilder, ProcessBuilder.Redirect[] redirects) {
+    public void check$$start(Class<?> callerClass, ProcessBuilder processBuilder) {
         policyManager.checkStartProcess(callerClass);
     }
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -70,7 +70,7 @@
-     }
- 
-     @Override
--    public void check$$start(Class<?> callerClass, ProcessBuilder processBuilder, ProcessBuilder.Redirect[] redirects) {
-+    public void check$$start(Class<?> callerClass, ProcessBuilder processBuilder) {
-         policyManager.checkStartProcess(callerClass);
-     }
- 
+*No hunk*
```


### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java

- Developer hunks: 7
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -10,7 +10,6 @@
 package org.elasticsearch.entitlement.runtime.policy;
 
 import org.elasticsearch.core.Strings;
-import org.elasticsearch.entitlement.runtime.api.ElasticsearchEntitlementChecker;
 import org.elasticsearch.entitlement.runtime.api.NotEntitledException;
 import org.elasticsearch.logging.LogManager;
 import org.elasticsearch.logging.Logger;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -10,7 +10,6 @@
- package org.elasticsearch.entitlement.runtime.policy;
- 
- import org.elasticsearch.core.Strings;
--import org.elasticsearch.entitlement.runtime.api.ElasticsearchEntitlementChecker;
- import org.elasticsearch.entitlement.runtime.api.NotEntitledException;
- import org.elasticsearch.logging.LogManager;
- import org.elasticsearch.logging.Logger;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -32,10 +31,9 @@
 
 import static java.lang.StackWalker.Option.RETAIN_CLASS_REFERENCE;
 import static java.util.Objects.requireNonNull;
-import static java.util.function.Predicate.not;
 
 public class PolicyManager {
-    private static final Logger logger = LogManager.getLogger(ElasticsearchEntitlementChecker.class);
+    private static final Logger logger = LogManager.getLogger(PolicyManager.class);
 
     static class ModuleEntitlements {
         public static final ModuleEntitlements NONE = new ModuleEntitlements(List.of());

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,12 +1 @@-@@ -32,10 +31,9 @@
- 
- import static java.lang.StackWalker.Option.RETAIN_CLASS_REFERENCE;
- import static java.util.Objects.requireNonNull;
--import static java.util.function.Predicate.not;
- 
- public class PolicyManager {
--    private static final Logger logger = LogManager.getLogger(ElasticsearchEntitlementChecker.class);
-+    private static final Logger logger = LogManager.getLogger(PolicyManager.class);
- 
-     static class ModuleEntitlements {
-         public static final ModuleEntitlements NONE = new ModuleEntitlements(List.of());
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -68,18 +66,12 @@
 
     private static final Set<Module> systemModules = findSystemModules();
 
-    /**
-     * Frames originating from this module are ignored in the permission logic.
-     */
-    private final Module entitlementsModule;
-
     private static Set<Module> findSystemModules() {
         var systemModulesDescriptors = ModuleFinder.ofSystem()
             .findAll()
             .stream()
             .map(ModuleReference::descriptor)
             .collect(Collectors.toUnmodifiableSet());
-
         return ModuleLayer.boot()
             .modules()
             .stream()

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,19 +1 @@-@@ -68,18 +66,12 @@
- 
-     private static final Set<Module> systemModules = findSystemModules();
- 
--    /**
--     * Frames originating from this module are ignored in the permission logic.
--     */
--    private final Module entitlementsModule;
--
-     private static Set<Module> findSystemModules() {
-         var systemModulesDescriptors = ModuleFinder.ofSystem()
-             .findAll()
-             .stream()
-             .map(ModuleReference::descriptor)
-             .collect(Collectors.toUnmodifiableSet());
--
-         return ModuleLayer.boot()
-             .modules()
-             .stream()
+*No hunk*
```

#### Hunk 4

Developer
```diff
@@ -87,6 +79,11 @@
             .collect(Collectors.toUnmodifiableSet());
     }
 
+    /**
+     * Frames originating from this module are ignored in the permission logic.
+     */
+    private final Module entitlementsModule;
+
     public PolicyManager(
         Policy defaultPolicy,
         Map<String, Policy> pluginPolicies,

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,12 +1 @@-@@ -87,6 +79,11 @@
-             .collect(Collectors.toUnmodifiableSet());
-     }
- 
-+    /**
-+     * Frames originating from this module are ignored in the permission logic.
-+     */
-+    private final Module entitlementsModule;
-+
-     public PolicyManager(
-         Policy defaultPolicy,
-         Map<String, Policy> pluginPolicies,
+*No hunk*
```

#### Hunk 5

Developer
```diff
@@ -227,12 +224,12 @@
      *                    this is a fast-path check that can avoid the stack walk
      *                    in cases where the caller class is available.
      * @return the requesting module, or {@code null} if the entire call stack
-     * comes from modules that are trusted.
+     * comes from the entitlement library itself.
      */
     Module requestingModule(Class<?> callerClass) {
         if (callerClass != null) {
-            Module callerModule = callerClass.getModule();
-            if (systemModules.contains(callerModule) == false) {
+            var callerModule = callerClass.getModule();
+            if (callerModule != null && entitlementsModule.equals(callerModule) == false) {
                 // fast path
                 return callerModule;
             }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,16 +1 @@-@@ -227,12 +224,12 @@
-      *                    this is a fast-path check that can avoid the stack walk
-      *                    in cases where the caller class is available.
-      * @return the requesting module, or {@code null} if the entire call stack
--     * comes from modules that are trusted.
-+     * comes from the entitlement library itself.
-      */
-     Module requestingModule(Class<?> callerClass) {
-         if (callerClass != null) {
--            Module callerModule = callerClass.getModule();
--            if (systemModules.contains(callerModule) == false) {
-+            var callerModule = callerClass.getModule();
-+            if (callerModule != null && entitlementsModule.equals(callerModule) == false) {
-                 // fast path
-                 return callerModule;
-             }
+*No hunk*
```

#### Hunk 6

Developer
```diff
@@ -251,8 +248,8 @@
     Optional<Module> findRequestingModule(Stream<Class<?>> classes) {
         return classes.map(Objects::requireNonNull)
             .map(PolicyManager::moduleOf)
-            .filter(m -> m != entitlementsModule)  // Ignore the entitlements library itself
-            .filter(not(systemModules::contains))  // Skip trusted JDK modules
+            .filter(m -> m != entitlementsModule)  // Ignore the entitlements library itself entirely
+            .skip(1)                            // Skip the sensitive method itself
             .findFirst();
     }
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,11 +1 @@-@@ -251,8 +248,8 @@
-     Optional<Module> findRequestingModule(Stream<Class<?>> classes) {
-         return classes.map(Objects::requireNonNull)
-             .map(PolicyManager::moduleOf)
--            .filter(m -> m != entitlementsModule)  // Ignore the entitlements library itself
--            .filter(not(systemModules::contains))  // Skip trusted JDK modules
-+            .filter(m -> m != entitlementsModule)  // Ignore the entitlements library itself entirely
-+            .skip(1)                            // Skip the sensitive method itself
-             .findFirst();
-     }
- 
+*No hunk*
```

#### Hunk 7

Developer
```diff
@@ -266,8 +263,15 @@
     }
 
     private static boolean isTriviallyAllowed(Module requestingModule) {
+        if (logger.isTraceEnabled()) {
+            logger.trace("Stack trace for upcoming trivially-allowed check", new Exception());
+        }
         if (requestingModule == null) {
-            logger.debug("Entitlement trivially allowed: entire call stack is in composed of classes in system modules");
+            logger.debug("Entitlement trivially allowed: no caller frames outside the entitlement library");
+            return true;
+        }
+        if (systemModules.contains(requestingModule)) {
+            logger.debug("Entitlement trivially allowed from system module [{}]", requestingModule.getName());
             return true;
         }
         logger.trace("Entitlement not trivially allowed");

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,17 +1 @@-@@ -266,8 +263,15 @@
-     }
- 
-     private static boolean isTriviallyAllowed(Module requestingModule) {
-+        if (logger.isTraceEnabled()) {
-+            logger.trace("Stack trace for upcoming trivially-allowed check", new Exception());
-+        }
-         if (requestingModule == null) {
--            logger.debug("Entitlement trivially allowed: entire call stack is in composed of classes in system modules");
-+            logger.debug("Entitlement trivially allowed: no caller frames outside the entitlement library");
-+            return true;
-+        }
-+        if (systemModules.contains(requestingModule)) {
-+            logger.debug("Entitlement trivially allowed from system module [{}]", requestingModule.getName());
-             return true;
-         }
-         logger.trace("Entitlement not trivially allowed");
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
diff --git a/libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java b/libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java
index 25f4e97bd12..d549c0d8906 100644
--- a/libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java
+++ b/libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java
@@ -32,7 +32,7 @@ public interface EntitlementChecker {
     void check$java_net_URLClassLoader$(Class<?> callerClass, String name, URL[] urls, ClassLoader parent, URLStreamHandlerFactory factory);
 
     // Process creation
-    void check$$start(Class<?> callerClass, ProcessBuilder that, ProcessBuilder.Redirect[] redirects);
+    void check$$start(Class<?> callerClass, ProcessBuilder that);
 
     void check$java_lang_ProcessBuilder$startPipeline(Class<?> callerClass, List<ProcessBuilder> builders);
 
diff --git a/libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsDeniedIT.java b/libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsDeniedIT.java
index 9f55a7c9e89..7f2bf792ac0 100644
--- a/libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsDeniedIT.java
+++ b/libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsDeniedIT.java
@@ -31,6 +31,8 @@ public class EntitlementsDeniedIT extends ESRestTestCase {
         .plugin("entitlement-denied-nonmodular")
         .systemProperty("es.entitlements.enabled", "true")
         .setting("xpack.security.enabled", "false")
+        // Logs in libs/entitlement/qa/build/test-results/javaRestTest/TEST-org.elasticsearch.entitlement.qa.EntitlementsDeniedIT.xml
+        // .setting("logger.org.elasticsearch.entitlement", "TRACE")
         .build();
 
     @Override
diff --git a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java
index 75365fbb74d..7c72e0335a3 100644
--- a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java
+++ b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java
@@ -70,7 +70,7 @@ public class ElasticsearchEntitlementChecker implements EntitlementChecker {
     }
 
     @Override
-    public void check$$start(Class<?> callerClass, ProcessBuilder processBuilder, ProcessBuilder.Redirect[] redirects) {
+    public void check$$start(Class<?> callerClass, ProcessBuilder processBuilder) {
         policyManager.checkStartProcess(callerClass);
     }
 
diff --git a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java
index e06f7768eb8..527a9472a7c 100644
--- a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java
+++ b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java
@@ -10,7 +10,6 @@
 package org.elasticsearch.entitlement.runtime.policy;
 
 import org.elasticsearch.core.Strings;
-import org.elasticsearch.entitlement.runtime.api.ElasticsearchEntitlementChecker;
 import org.elasticsearch.entitlement.runtime.api.NotEntitledException;
 import org.elasticsearch.logging.LogManager;
 import org.elasticsearch.logging.Logger;
@@ -32,10 +31,9 @@ import java.util.stream.Stream;
 
 import static java.lang.StackWalker.Option.RETAIN_CLASS_REFERENCE;
 import static java.util.Objects.requireNonNull;
-import static java.util.function.Predicate.not;
 
 public class PolicyManager {
-    private static final Logger logger = LogManager.getLogger(ElasticsearchEntitlementChecker.class);
+    private static final Logger logger = LogManager.getLogger(PolicyManager.class);
 
     static class ModuleEntitlements {
         public static final ModuleEntitlements NONE = new ModuleEntitlements(List.of());
@@ -68,18 +66,12 @@ public class PolicyManager {
 
     private static final Set<Module> systemModules = findSystemModules();
 
-    /**
-     * Frames originating from this module are ignored in the permission logic.
-     */
-    private final Module entitlementsModule;
-
     private static Set<Module> findSystemModules() {
         var systemModulesDescriptors = ModuleFinder.ofSystem()
             .findAll()
             .stream()
             .map(ModuleReference::descriptor)
             .collect(Collectors.toUnmodifiableSet());
-
         return ModuleLayer.boot()
             .modules()
             .stream()
@@ -87,6 +79,11 @@ public class PolicyManager {
             .collect(Collectors.toUnmodifiableSet());
     }
 
+    /**
+     * Frames originating from this module are ignored in the permission logic.
+     */
+    private final Module entitlementsModule;
+
     public PolicyManager(
         Policy defaultPolicy,
         Map<String, Policy> pluginPolicies,
@@ -227,12 +224,12 @@ public class PolicyManager {
      *                    this is a fast-path check that can avoid the stack walk
      *                    in cases where the caller class is available.
      * @return the requesting module, or {@code null} if the entire call stack
-     * comes from modules that are trusted.
+     * comes from the entitlement library itself.
      */
     Module requestingModule(Class<?> callerClass) {
         if (callerClass != null) {
-            Module callerModule = callerClass.getModule();
-            if (systemModules.contains(callerModule) == false) {
+            var callerModule = callerClass.getModule();
+            if (callerModule != null && entitlementsModule.equals(callerModule) == false) {
                 // fast path
                 return callerModule;
             }
@@ -251,8 +248,8 @@ public class PolicyManager {
     Optional<Module> findRequestingModule(Stream<Class<?>> classes) {
         return classes.map(Objects::requireNonNull)
             .map(PolicyManager::moduleOf)
-            .filter(m -> m != entitlementsModule)  // Ignore the entitlements library itself
-            .filter(not(systemModules::contains))  // Skip trusted JDK modules
+            .filter(m -> m != entitlementsModule)  // Ignore the entitlements library itself entirely
+            .skip(1)                            // Skip the sensitive method itself
             .findFirst();
     }
 
@@ -266,8 +263,15 @@ public class PolicyManager {
     }
 
     private static boolean isTriviallyAllowed(Module requestingModule) {
+        if (logger.isTraceEnabled()) {
+            logger.trace("Stack trace for upcoming trivially-allowed check", new Exception());
+        }
         if (requestingModule == null) {
-            logger.debug("Entitlement trivially allowed: entire call stack is in composed of classes in system modules");
+            logger.debug("Entitlement trivially allowed: no caller frames outside the entitlement library");
+            return true;
+        }
+        if (systemModules.contains(requestingModule)) {
+            logger.debug("Entitlement trivially allowed from system module [{}]", requestingModule.getName());
             return true;
         }
         logger.trace("Entitlement not trivially allowed");
diff --git a/libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyManagerTests.java b/libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyManagerTests.java
index 0789fcc8dc7..31e3e62f56b 100644
--- a/libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyManagerTests.java
+++ b/libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyManagerTests.java
@@ -13,6 +13,7 @@ import org.elasticsearch.entitlement.runtime.api.NotEntitledException;
 import org.elasticsearch.test.ESTestCase;
 import org.elasticsearch.test.compiler.InMemoryJavaCompiler;
 import org.elasticsearch.test.jar.JarUtils;
+import org.junit.BeforeClass;
 
 import java.io.IOException;
 import java.lang.module.Configuration;
@@ -37,8 +38,22 @@ import static org.hamcrest.Matchers.sameInstance;
 
 @ESTestCase.WithoutSecurityManager
 public class PolicyManagerTests extends ESTestCase {
+    /**
+     * A module you can use for test cases that don't actually care about the
+     * entitlements module.
+     */
+    private static Module NO_ENTITLEMENTS_MODULE;
+
+    @BeforeClass
+    public static void beforeClass() {
+        try {
+            // Any old module will do for tests using NO_ENTITLEMENTS_MODULE
+            NO_ENTITLEMENTS_MODULE = makeClassInItsOwnModule().getModule();
+        } catch (Exception e) {
+            throw new IllegalStateException(e);
+        }
 
-    private static final Module NO_ENTITLEMENTS_MODULE = null;
+    }
 
     public void testGetEntitlementsThrowsOnMissingPluginUnnamedModule() {
         var policyManager = new PolicyManager(
@@ -210,53 +225,31 @@ public class PolicyManagerTests extends ESTestCase {
     }
 
     public void testRequestingModuleWithStackWalk() throws IOException, ClassNotFoundException {
-        var requestingClass = makeClassInItsOwnModule();
-        var runtimeClass = makeClassInItsOwnModule(); // A class in the entitlements library itself
+        var entitlementsClass = makeClassInItsOwnModule();    // A class in the entitlements library itself
+        var requestingClass = makeClassInItsOwnModule();      // This guy is always the right answer
+        var instrumentedClass = makeClassInItsOwnModule();    // The class that called the check method
         var ignorableClass = makeClassInItsOwnModule();
-        var systemClass = Object.class;
 
-        var policyManager = policyManagerWithEntitlementsModule(runtimeClass.getModule());
+        var policyManager = policyManagerWithEntitlementsModule(entitlementsClass.getModule());
 
         var requestingModule = requestingClass.getModule();
 
         assertEquals(
-            "Skip one system frame",
-            requestingModule,
-            policyManager.findRequestingModule(Stream.of(systemClass, requestingClass, ignorableClass)).orElse(null)
-        );
-        assertEquals(
-            "Skip multiple system frames",
-            requestingModule,
-            policyManager.findRequestingModule(Stream.of(systemClass, systemClass, systemClass, requestingClass, ignorableClass))
-                .orElse(null)
-        );
-        assertEquals(
-            "Skip system frame between runtime frames",
+            "Skip entitlement library and the instrumented method",
             requestingModule,
-            policyManager.findRequestingModule(Stream.of(runtimeClass, systemClass, runtimeClass, requestingClass, ignorableClass))
+            policyManager.findRequestingModule(Stream.of(entitlementsClass, instrumentedClass, requestingClass, ignorableClass))
                 .orElse(null)
         );
         assertEquals(
-            "Skip runtime frame between system frames",
-            requestingModule,
-            policyManager.findRequestingModule(Stream.of(systemClass, runtimeClass, systemClass, requestingClass, ignorableClass))
-                .orElse(null)
-        );
-        assertEquals(
-            "No system frames",
-            requestingModule,
-            policyManager.findRequestingModule(Stream.of(requestingClass, ignorableClass)).orElse(null)
-        );
-        assertEquals(
-            "Skip runtime frames up to the first system frame",
+            "Skip multiple library frames",
             requestingModule,
-            policyManager.findRequestingModule(Stream.of(runtimeClass, runtimeClass, systemClass, requestingClass, ignorableClass))
+            policyManager.findRequestingModule(Stream.of(entitlementsClass, entitlementsClass, instrumentedClass, requestingClass))
                 .orElse(null)
         );
         assertThrows(
             "Non-modular caller frames are not supported",
             NullPointerException.class,
-            () -> policyManager.findRequestingModule(Stream.of(systemClass, null))
+            () -> policyManager.findRequestingModule(Stream.of(entitlementsClass, null))
         );
     }
 

```
