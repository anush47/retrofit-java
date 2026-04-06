# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['xds/src/main/java/io/grpc/xds/XdsClusterResource.java', 'xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java', 'xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java']
- Developer Java files: ['xds/src/main/java/io/grpc/xds/XdsClusterResource.java', 'xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java', 'xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java']
- Overlap Java files: ['xds/src/main/java/io/grpc/xds/XdsClusterResource.java', 'xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java', 'xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['xds/src/main/java/io/grpc/xds/XdsClusterResource.java', 'xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java', 'xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java']

## File State Comparison
- Compared files: ['xds/src/main/java/io/grpc/xds/XdsClusterResource.java', 'xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java', 'xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java']
- Mismatched files: ['xds/src/main/java/io/grpc/xds/XdsClusterResource.java', 'xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java', 'xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### xds/src/main/java/io/grpc/xds/XdsClusterResource.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -541,7 +541,12 @@
     if (commonTlsContext.hasTlsCertificateProviderInstance()) {
       return commonTlsContext.getTlsCertificateProviderInstance().getInstanceName();
     }
-    return null;
+    // Fall back to deprecated field (field 11) for backward compatibility with Istio
+    @SuppressWarnings("deprecation")
+    String instanceName = commonTlsContext.hasTlsCertificateCertificateProviderInstance()
+        ? commonTlsContext.getTlsCertificateCertificateProviderInstance().getInstanceName()
+        : null;
+    return instanceName;
   }
 
   private static String getRootCertInstanceName(CommonTlsContext commonTlsContext) {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,14 +1 @@-@@ -541,7 +541,12 @@
-     if (commonTlsContext.hasTlsCertificateProviderInstance()) {
-       return commonTlsContext.getTlsCertificateProviderInstance().getInstanceName();
-     }
--    return null;
-+    // Fall back to deprecated field (field 11) for backward compatibility with Istio
-+    @SuppressWarnings("deprecation")
-+    String instanceName = commonTlsContext.hasTlsCertificateCertificateProviderInstance()
-+        ? commonTlsContext.getTlsCertificateCertificateProviderInstance().getInstanceName()
-+        : null;
-+    return instanceName;
-   }
- 
-   private static String getRootCertInstanceName(CommonTlsContext commonTlsContext) {
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -559,6 +564,16 @@
         return combinedCertificateValidationContext.getDefaultValidationContext()
             .getCaCertificateProviderInstance().getInstanceName();
       }
+      // Fall back to deprecated field (field 4) in CombinedValidationContext
+      @SuppressWarnings("deprecation")
+      String instanceName = combinedCertificateValidationContext
+          .hasValidationContextCertificateProviderInstance()
+          ? combinedCertificateValidationContext.getValidationContextCertificateProviderInstance()
+              .getInstanceName()
+          : null;
+      if (instanceName != null) {
+        return instanceName;
+      }
     }
     return null;
   }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,17 +1 @@-@@ -559,6 +564,16 @@
-         return combinedCertificateValidationContext.getDefaultValidationContext()
-             .getCaCertificateProviderInstance().getInstanceName();
-       }
-+      // Fall back to deprecated field (field 4) in CombinedValidationContext
-+      @SuppressWarnings("deprecation")
-+      String instanceName = combinedCertificateValidationContext
-+          .hasValidationContextCertificateProviderInstance()
-+          ? combinedCertificateValidationContext.getValidationContextCertificateProviderInstance()
-+              .getInstanceName()
-+          : null;
-+      if (instanceName != null) {
-+        return instanceName;
-+      }
-     }
-     return null;
-   }
+*No hunk*
```


### xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -28,7 +28,10 @@
     if (commonTlsContext == null) {
       return false;
     }
+    @SuppressWarnings("deprecation")
+    boolean hasDeprecatedField = commonTlsContext.hasTlsCertificateCertificateProviderInstance();
     return commonTlsContext.hasTlsCertificateProviderInstance()
+        || hasDeprecatedField
         || hasValidationProviderInstance(commonTlsContext);
   }
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,11 +1 @@-@@ -28,7 +28,10 @@
-     if (commonTlsContext == null) {
-       return false;
-     }
-+    @SuppressWarnings("deprecation")
-+    boolean hasDeprecatedField = commonTlsContext.hasTlsCertificateCertificateProviderInstance();
-     return commonTlsContext.hasTlsCertificateProviderInstance()
-+        || hasDeprecatedField
-         || hasValidationProviderInstance(commonTlsContext);
-   }
- 
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -37,9 +40,19 @@
         .hasCaCertificateProviderInstance()) {
       return true;
     }
-    return commonTlsContext.hasCombinedValidationContext()
-        && commonTlsContext.getCombinedValidationContext().getDefaultValidationContext()
-          .hasCaCertificateProviderInstance();
+    if (commonTlsContext.hasCombinedValidationContext()) {
+      CommonTlsContext.CombinedCertificateValidationContext combined =
+          commonTlsContext.getCombinedValidationContext();
+      if (combined.hasDefaultValidationContext()
+          && combined.getDefaultValidationContext().hasCaCertificateProviderInstance()) {
+        return true;
+      }
+      // Check deprecated field (field 4) in CombinedValidationContext
+      @SuppressWarnings("deprecation")
+      boolean hasDeprecatedField = combined.hasValidationContextCertificateProviderInstance();
+      return hasDeprecatedField;
+    }
+    return false;
   }
 
   /**

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,23 +1 @@-@@ -37,9 +40,19 @@
-         .hasCaCertificateProviderInstance()) {
-       return true;
-     }
--    return commonTlsContext.hasCombinedValidationContext()
--        && commonTlsContext.getCombinedValidationContext().getDefaultValidationContext()
--          .hasCaCertificateProviderInstance();
-+    if (commonTlsContext.hasCombinedValidationContext()) {
-+      CommonTlsContext.CombinedCertificateValidationContext combined =
-+          commonTlsContext.getCombinedValidationContext();
-+      if (combined.hasDefaultValidationContext()
-+          && combined.getDefaultValidationContext().hasCaCertificateProviderInstance()) {
-+        return true;
-+      }
-+      // Check deprecated field (field 4) in CombinedValidationContext
-+      @SuppressWarnings("deprecation")
-+      boolean hasDeprecatedField = combined.hasValidationContextCertificateProviderInstance();
-+      return hasDeprecatedField;
-+    }
-+    return false;
-   }
- 
-   /**
+*No hunk*
```


### xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -113,7 +113,13 @@
     if (commonTlsContext.hasTlsCertificateProviderInstance()) {
       return CommonTlsContextUtil.convert(commonTlsContext.getTlsCertificateProviderInstance());
     }
-    return null;
+    // Fall back to deprecated field for backward compatibility with Istio
+    @SuppressWarnings("deprecation")
+    CertificateProviderInstance deprecatedInstance =
+        commonTlsContext.hasTlsCertificateCertificateProviderInstance()
+            ? commonTlsContext.getTlsCertificateCertificateProviderInstance()
+            : null;
+    return deprecatedInstance;
   }
 
   @Nullable

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,15 +1 @@-@@ -113,7 +113,13 @@
-     if (commonTlsContext.hasTlsCertificateProviderInstance()) {
-       return CommonTlsContextUtil.convert(commonTlsContext.getTlsCertificateProviderInstance());
-     }
--    return null;
-+    // Fall back to deprecated field for backward compatibility with Istio
-+    @SuppressWarnings("deprecation")
-+    CertificateProviderInstance deprecatedInstance =
-+        commonTlsContext.hasTlsCertificateCertificateProviderInstance()
-+            ? commonTlsContext.getTlsCertificateCertificateProviderInstance()
-+            : null;
-+    return deprecatedInstance;
-   }
- 
-   @Nullable
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
diff --git a/xds/src/main/java/io/grpc/xds/XdsClusterResource.java b/xds/src/main/java/io/grpc/xds/XdsClusterResource.java
index 593aed4ef..d9848d970 100644
--- a/xds/src/main/java/io/grpc/xds/XdsClusterResource.java
+++ b/xds/src/main/java/io/grpc/xds/XdsClusterResource.java
@@ -541,7 +541,12 @@ class XdsClusterResource extends XdsResourceType<CdsUpdate> {
     if (commonTlsContext.hasTlsCertificateProviderInstance()) {
       return commonTlsContext.getTlsCertificateProviderInstance().getInstanceName();
     }
-    return null;
+    // Fall back to deprecated field (field 11) for backward compatibility with Istio
+    @SuppressWarnings("deprecation")
+    String instanceName = commonTlsContext.hasTlsCertificateCertificateProviderInstance()
+        ? commonTlsContext.getTlsCertificateCertificateProviderInstance().getInstanceName()
+        : null;
+    return instanceName;
   }
 
   private static String getRootCertInstanceName(CommonTlsContext commonTlsContext) {
@@ -559,6 +564,16 @@ class XdsClusterResource extends XdsResourceType<CdsUpdate> {
         return combinedCertificateValidationContext.getDefaultValidationContext()
             .getCaCertificateProviderInstance().getInstanceName();
       }
+      // Fall back to deprecated field (field 4) in CombinedValidationContext
+      @SuppressWarnings("deprecation")
+      String instanceName = combinedCertificateValidationContext
+          .hasValidationContextCertificateProviderInstance()
+          ? combinedCertificateValidationContext.getValidationContextCertificateProviderInstance()
+              .getInstanceName()
+          : null;
+      if (instanceName != null) {
+        return instanceName;
+      }
     }
     return null;
   }
diff --git a/xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java b/xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java
index 50fa18b64..bd8a423e6 100644
--- a/xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java
+++ b/xds/src/main/java/io/grpc/xds/internal/security/CommonTlsContextUtil.java
@@ -28,7 +28,10 @@ public final class CommonTlsContextUtil {
     if (commonTlsContext == null) {
       return false;
     }
+    @SuppressWarnings("deprecation")
+    boolean hasDeprecatedField = commonTlsContext.hasTlsCertificateCertificateProviderInstance();
     return commonTlsContext.hasTlsCertificateProviderInstance()
+        || hasDeprecatedField
         || hasValidationProviderInstance(commonTlsContext);
   }
 
@@ -37,9 +40,19 @@ public final class CommonTlsContextUtil {
         .hasCaCertificateProviderInstance()) {
       return true;
     }
-    return commonTlsContext.hasCombinedValidationContext()
-        && commonTlsContext.getCombinedValidationContext().getDefaultValidationContext()
-          .hasCaCertificateProviderInstance();
+    if (commonTlsContext.hasCombinedValidationContext()) {
+      CommonTlsContext.CombinedCertificateValidationContext combined =
+          commonTlsContext.getCombinedValidationContext();
+      if (combined.hasDefaultValidationContext()
+          && combined.getDefaultValidationContext().hasCaCertificateProviderInstance()) {
+        return true;
+      }
+      // Check deprecated field (field 4) in CombinedValidationContext
+      @SuppressWarnings("deprecation")
+      boolean hasDeprecatedField = combined.hasValidationContextCertificateProviderInstance();
+      return hasDeprecatedField;
+    }
+    return false;
   }
 
   /**
diff --git a/xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java b/xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java
index 2570dcb73..cb99ca6ad 100644
--- a/xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java
+++ b/xds/src/main/java/io/grpc/xds/internal/security/certprovider/CertProviderSslContextProvider.java
@@ -113,7 +113,13 @@ abstract class CertProviderSslContextProvider extends DynamicSslContextProvider
     if (commonTlsContext.hasTlsCertificateProviderInstance()) {
       return CommonTlsContextUtil.convert(commonTlsContext.getTlsCertificateProviderInstance());
     }
-    return null;
+    // Fall back to deprecated field for backward compatibility with Istio
+    @SuppressWarnings("deprecation")
+    CertificateProviderInstance deprecatedInstance =
+        commonTlsContext.hasTlsCertificateCertificateProviderInstance()
+            ? commonTlsContext.getTlsCertificateCertificateProviderInstance()
+            : null;
+    return deprecatedInstance;
   }
 
   @Nullable
diff --git a/xds/src/test/java/io/grpc/xds/GrpcXdsClientImplDataTest.java b/xds/src/test/java/io/grpc/xds/GrpcXdsClientImplDataTest.java
index 0af647559..975570d82 100644
--- a/xds/src/test/java/io/grpc/xds/GrpcXdsClientImplDataTest.java
+++ b/xds/src/test/java/io/grpc/xds/GrpcXdsClientImplDataTest.java
@@ -3134,6 +3134,18 @@ public class GrpcXdsClientImplDataTest {
         .validateCommonTlsContext(commonTlsContext, ImmutableSet.of("name1", "name2"), true);
   }
 
+  @Test
+  @SuppressWarnings("deprecation")
+  public void validateCommonTlsContext_tlsDeprecatedCertificateProviderInstance()
+      throws ResourceInvalidException {
+    CommonTlsContext commonTlsContext = CommonTlsContext.newBuilder()
+        .setTlsCertificateCertificateProviderInstance(
+            CommonTlsContext.CertificateProviderInstance.newBuilder().setInstanceName("name1"))
+        .build();
+    XdsClusterResource
+        .validateCommonTlsContext(commonTlsContext, ImmutableSet.of("name1", "name2"), true);
+  }
+
   @Test
   public void validateCommonTlsContext_tlsCertificateProviderInstance()
       throws ResourceInvalidException {
@@ -3218,6 +3230,24 @@ public class GrpcXdsClientImplDataTest {
         .validateCommonTlsContext(commonTlsContext, ImmutableSet.of(), false);
   }
 
+  @Test
+  @SuppressWarnings("deprecation")
+  public void validateCommonTlsContext_combinedValidationContextDeprecatedCertProvider()
+      throws ResourceInvalidException {
+    CommonTlsContext commonTlsContext = CommonTlsContext.newBuilder()
+        .setTlsCertificateProviderInstance(
+            CertificateProviderPluginInstance.newBuilder().setInstanceName("cert1"))
+        .setCombinedValidationContext(
+            CommonTlsContext.CombinedCertificateValidationContext.newBuilder()
+                .setValidationContextCertificateProviderInstance(
+                    CommonTlsContext.CertificateProviderInstance.newBuilder()
+                        .setInstanceName("root1"))
+                .build())
+        .build();
+    XdsClusterResource
+        .validateCommonTlsContext(commonTlsContext, ImmutableSet.of("cert1", "root1"), true);
+  }
+
   @Test
   public void validateCommonTlsContext_validationContextSystemRootCerts_envVarNotSet_throws() {
     XdsClusterResource.enableSystemRootCerts = false;
diff --git a/xds/src/test/java/io/grpc/xds/internal/security/CommonTlsContextTestsUtil.java b/xds/src/test/java/io/grpc/xds/internal/security/CommonTlsContextTestsUtil.java
index 80a8083fb..abacd2038 100644
--- a/xds/src/test/java/io/grpc/xds/internal/security/CommonTlsContextTestsUtil.java
+++ b/xds/src/test/java/io/grpc/xds/internal/security/CommonTlsContextTestsUtil.java
@@ -232,6 +232,33 @@ public class CommonTlsContextTestsUtil {
     return builder.build();
   }
 
+  /** Helper method to build CommonTlsContext using deprecated certificate provider field. */
+  @SuppressWarnings("deprecation")
+  public static CommonTlsContext buildCommonTlsContextWithDeprecatedCertProviderInstance(
+      String certInstanceName,
+      String certName,
+      String rootInstanceName,
+      String rootCertName,
+      Iterable<String> alpnProtocols,
+      CertificateValidationContext staticCertValidationContext) {
+    CommonTlsContext.Builder builder = CommonTlsContext.newBuilder();
+    if (certInstanceName != null) {
+      // Use deprecated field (field 11) instead of current field (field 14)
+      builder =
+              builder.setTlsCertificateCertificateProviderInstance(
+                      CommonTlsContext.CertificateProviderInstance.newBuilder()
+                              .setInstanceName(certInstanceName)
+                              .setCertificateName(certName));
+    }
+    builder =
+        addCertificateValidationContext(
+            builder, rootInstanceName, rootCertName, staticCertValidationContext);
+    if (alpnProtocols != null) {
+      builder.addAllAlpnProtocols(alpnProtocols);
+    }
+    return builder.build();
+  }
+
   private static CommonTlsContext buildNewCommonTlsContextForCertProviderInstance(
           String certInstanceName,
           String certName,
diff --git a/xds/src/test/java/io/grpc/xds/internal/security/certprovider/CertProviderClientSslContextProviderTest.java b/xds/src/test/java/io/grpc/xds/internal/security/certprovider/CertProviderClientSslContextProviderTest.java
index 875a57b8f..91f02863c 100644
--- a/xds/src/test/java/io/grpc/xds/internal/security/certprovider/CertProviderClientSslContextProviderTest.java
+++ b/xds/src/test/java/io/grpc/xds/internal/security/certprovider/CertProviderClientSslContextProviderTest.java
@@ -470,6 +470,58 @@ public class CertProviderClientSslContextProviderTest {
             .build(), false);
   }
 
+  @Test
+  public void testProviderForClient_deprecatedCertProviderField() throws Exception {
+    final CertificateProvider.DistributorWatcher[] watcherCaptor =
+        new CertificateProvider.DistributorWatcher[1];
+    TestCertificateProvider.createAndRegisterProviderProvider(
+        certificateProviderRegistry, watcherCaptor, "testca", 0);
+    
+    // Build UpstreamTlsContext using deprecated field
+    EnvoyServerProtoData.UpstreamTlsContext upstreamTlsContext =
+        new EnvoyServerProtoData.UpstreamTlsContext(
+            CommonTlsContextTestsUtil.buildCommonTlsContextWithDeprecatedCertProviderInstance(
+                "gcp_id",
+                "cert-default",
+                "gcp_id",
+                "root-default",
+                /* alpnProtocols= */ null,
+                /* staticCertValidationContext= */ null));
+    
+    Bootstrapper.BootstrapInfo bootstrapInfo = CommonBootstrapperTestUtils.getTestBootstrapInfo();
+    CertProviderClientSslContextProvider provider =
+        (CertProviderClientSslContextProvider)
+            certProviderClientSslContextProviderFactory.getProvider(
+                upstreamTlsContext,
+                bootstrapInfo.node().toEnvoyProtoNode(),
+                bootstrapInfo.certProviders());
+
+    assertThat(provider.savedKey).isNull();
+    assertThat(provider.savedCertChain).isNull();
+    assertThat(provider.savedTrustedRoots).isNull();
+    assertThat(provider.getSslContextAndTrustManager()).isNull();
+
+    // Generate cert update
+    watcherCaptor[0].updateCertificate(
+        CommonCertProviderTestUtils.getPrivateKey(CLIENT_KEY_FILE),
+        ImmutableList.of(getCertFromResourceName(CLIENT_PEM_FILE)));
+    assertThat(provider.savedKey).isNotNull();
+    assertThat(provider.savedCertChain).isNotNull();
+    assertThat(provider.getSslContextAndTrustManager()).isNull();
+
+    // Generate root cert update
+    watcherCaptor[0].updateTrustedRoots(ImmutableList.of(getCertFromResourceName(CA_PEM_FILE)));
+    assertThat(provider.getSslContextAndTrustManager()).isNotNull();
+    assertThat(provider.savedKey).isNull();
+    assertThat(provider.savedCertChain).isNull();
+    assertThat(provider.savedTrustedRoots).isNull();
+
+    TestCallback testCallback =
+        CommonTlsContextTestsUtil.getValueThruCallback(provider);
+
+    doChecksOnSslContext(false, testCallback.updatedSslContext, /* expectedApnProtos= */ null);
+  }
+
   static class QueuedExecutor implements Executor {
     /** A list of Runnables to be run in order. */
     @VisibleForTesting final Queue<Runnable> runQueue = new ConcurrentLinkedQueue<>();

```
