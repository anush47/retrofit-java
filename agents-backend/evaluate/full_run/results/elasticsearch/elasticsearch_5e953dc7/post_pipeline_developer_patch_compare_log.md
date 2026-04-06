# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java']
- Developer Java files: ['x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java']
- Overlap Java files: ['x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java']

## File State Comparison
- Compared files: ['x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java

- Developer hunks: 3
- Generated hunks: 3

#### Hunk 1

Developer
```diff
@@ -266,7 +266,9 @@
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidate(keys);
                     }
-                    keys.forEach(apiKeyAuthCache::invalidate);
+                    if (apiKeyAuthCache != null) {
+                        keys.forEach(apiKeyAuthCache::invalidate);
+                    }
                 }
 
                 @Override

```

Generated
```diff
@@ -266,7 +266,9 @@
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidate(keys);
                     }
-                    keys.forEach(apiKeyAuthCache::invalidate);
+                    if (apiKeyAuthCache != null) {
+                        keys.forEach(apiKeyAuthCache::invalidate);
+                    }
                 }
 
                 @Override

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -274,7 +276,9 @@
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidateAll();
                     }
-                    apiKeyAuthCache.invalidateAll();
+                    if (apiKeyAuthCache != null) {
+                        apiKeyAuthCache.invalidateAll();
+                    }
                 }
             });
             cacheInvalidatorRegistry.registerCacheInvalidator("api_key_doc", new CacheInvalidatorRegistry.CacheInvalidator() {

```

Generated
```diff
@@ -274,7 +276,9 @@
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidateAll();
                     }
-                    apiKeyAuthCache.invalidateAll();
+                    if (apiKeyAuthCache != null) {
+                        apiKeyAuthCache.invalidateAll();
+                    }
                 }
             });
             cacheInvalidatorRegistry.registerCacheInvalidator("api_key_doc", new CacheInvalidatorRegistry.CacheInvalidator() {

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 3

Developer
```diff
@@ -589,9 +593,11 @@
                                     + "])";
                             assert indexResponse.getResult() == DocWriteResponse.Result.CREATED
                                 : "Index response was [" + indexResponse.getResult() + "]";
-                            final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
-                            listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
-                            apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            if (apiKeyAuthCache != null) {
+                                final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
+                                listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
+                                apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            }
                             listener.onResponse(new CreateApiKeyResponse(request.getName(), request.getId(), apiKey, expiration));
                         }, listener::onFailure))
                     )

```

Generated
```diff
@@ -589,9 +593,11 @@
                                     + "])";
                             assert indexResponse.getResult() == DocWriteResponse.Result.CREATED
                                 : "Index response was [" + indexResponse.getResult() + "]";
-                            final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
-                            listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
-                            apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            if (apiKeyAuthCache != null) {
+                                final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
+                                listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
+                                apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            }
                             listener.onResponse(new CreateApiKeyResponse(request.getName(), request.getId(), apiKey, expiration));
                         }, listener::onFailure))
                     )

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java b/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java
index 3c63ec71e74..1e80c01b8e7 100644
--- a/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java
+++ b/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java
@@ -266,7 +266,9 @@ public class ApiKeyService implements Closeable {
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidate(keys);
                     }
-                    keys.forEach(apiKeyAuthCache::invalidate);
+                    if (apiKeyAuthCache != null) {
+                        keys.forEach(apiKeyAuthCache::invalidate);
+                    }
                 }
 
                 @Override
@@ -274,7 +276,9 @@ public class ApiKeyService implements Closeable {
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidateAll();
                     }
-                    apiKeyAuthCache.invalidateAll();
+                    if (apiKeyAuthCache != null) {
+                        apiKeyAuthCache.invalidateAll();
+                    }
                 }
             });
             cacheInvalidatorRegistry.registerCacheInvalidator("api_key_doc", new CacheInvalidatorRegistry.CacheInvalidator() {
@@ -589,9 +593,11 @@ public class ApiKeyService implements Closeable {
                                     + "])";
                             assert indexResponse.getResult() == DocWriteResponse.Result.CREATED
                                 : "Index response was [" + indexResponse.getResult() + "]";
-                            final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
-                            listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
-                            apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            if (apiKeyAuthCache != null) {
+                                final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
+                                listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
+                                apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            }
                             listener.onResponse(new CreateApiKeyResponse(request.getName(), request.getId(), apiKey, expiration));
                         }, listener::onFailure))
                     )

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java b/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java
index 3c63ec71e74..1e80c01b8e7 100644
--- a/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java
+++ b/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java
@@ -266,7 +266,9 @@ public class ApiKeyService implements Closeable {
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidate(keys);
                     }
-                    keys.forEach(apiKeyAuthCache::invalidate);
+                    if (apiKeyAuthCache != null) {
+                        keys.forEach(apiKeyAuthCache::invalidate);
+                    }
                 }
 
                 @Override
@@ -274,7 +276,9 @@ public class ApiKeyService implements Closeable {
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidateAll();
                     }
-                    apiKeyAuthCache.invalidateAll();
+                    if (apiKeyAuthCache != null) {
+                        apiKeyAuthCache.invalidateAll();
+                    }
                 }
             });
             cacheInvalidatorRegistry.registerCacheInvalidator("api_key_doc", new CacheInvalidatorRegistry.CacheInvalidator() {
@@ -589,9 +593,11 @@ public class ApiKeyService implements Closeable {
                                     + "])";
                             assert indexResponse.getResult() == DocWriteResponse.Result.CREATED
                                 : "Index response was [" + indexResponse.getResult() + "]";
-                            final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
-                            listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
-                            apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            if (apiKeyAuthCache != null) {
+                                final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
+                                listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
+                                apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            }
                             listener.onResponse(new CreateApiKeyResponse(request.getName(), request.getId(), apiKey, expiration));
                         }, listener::onFailure))
                     )

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/docs/changelog/120483.yaml b/docs/changelog/120483.yaml
new file mode 100644
index 00000000000..20da3b9ab4e
--- /dev/null
+++ b/docs/changelog/120483.yaml
@@ -0,0 +1,5 @@
+pr: 120483
+summary: Fix NPE on disabled API auth key cache
+area: Authentication
+type: bug
+issues: []
diff --git a/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java b/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java
index 3c63ec71e74..1e80c01b8e7 100644
--- a/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java
+++ b/x-pack/plugin/security/src/main/java/org/elasticsearch/xpack/security/authc/ApiKeyService.java
@@ -266,7 +266,9 @@ public class ApiKeyService implements Closeable {
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidate(keys);
                     }
-                    keys.forEach(apiKeyAuthCache::invalidate);
+                    if (apiKeyAuthCache != null) {
+                        keys.forEach(apiKeyAuthCache::invalidate);
+                    }
                 }
 
                 @Override
@@ -274,7 +276,9 @@ public class ApiKeyService implements Closeable {
                     if (apiKeyDocCache != null) {
                         apiKeyDocCache.invalidateAll();
                     }
-                    apiKeyAuthCache.invalidateAll();
+                    if (apiKeyAuthCache != null) {
+                        apiKeyAuthCache.invalidateAll();
+                    }
                 }
             });
             cacheInvalidatorRegistry.registerCacheInvalidator("api_key_doc", new CacheInvalidatorRegistry.CacheInvalidator() {
@@ -589,9 +593,11 @@ public class ApiKeyService implements Closeable {
                                     + "])";
                             assert indexResponse.getResult() == DocWriteResponse.Result.CREATED
                                 : "Index response was [" + indexResponse.getResult() + "]";
-                            final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
-                            listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
-                            apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            if (apiKeyAuthCache != null) {
+                                final ListenableFuture<CachedApiKeyHashResult> listenableFuture = new ListenableFuture<>();
+                                listenableFuture.onResponse(new CachedApiKeyHashResult(true, apiKey));
+                                apiKeyAuthCache.put(request.getId(), listenableFuture);
+                            }
                             listener.onResponse(new CreateApiKeyResponse(request.getName(), request.getId(), apiKey, expiration));
                         }, listener::onFailure))
                     )
diff --git a/x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/ApiKeyServiceTests.java b/x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/ApiKeyServiceTests.java
index 996291c52c7..185669a6a20 100644
--- a/x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/ApiKeyServiceTests.java
+++ b/x-pack/plugin/security/src/test/java/org/elasticsearch/xpack/security/authc/ApiKeyServiceTests.java
@@ -2367,6 +2367,50 @@ public class ApiKeyServiceTests extends ESTestCase {
         assertNull(service.getApiKeyAuthCache().get(docId));
     }
 
+    public void testCanCreateApiKeyWithAuthCacheDisabled() {
+        final ApiKeyService service = createApiKeyService(
+            Settings.builder()
+                .put(XPackSettings.API_KEY_SERVICE_ENABLED_SETTING.getKey(), true)
+                .put("xpack.security.authc.api_key.cache.ttl", "0s")
+                .build()
+        );
+        final Authentication authentication = AuthenticationTestHelper.builder()
+            .user(new User(randomAlphaOfLengthBetween(8, 16), "superuser"))
+            .realmRef(new RealmRef(randomAlphaOfLengthBetween(3, 8), randomAlphaOfLengthBetween(3, 8), randomAlphaOfLengthBetween(3, 8)))
+            .build(false);
+        final CreateApiKeyRequest createApiKeyRequest = new CreateApiKeyRequest(randomAlphaOfLengthBetween(3, 8), null, null);
+        when(client.prepareIndex(anyString())).thenReturn(new IndexRequestBuilder(client));
+        when(client.prepareBulk()).thenReturn(new BulkRequestBuilder(client));
+        when(client.threadPool()).thenReturn(threadPool);
+        doAnswer(inv -> {
+            final Object[] args = inv.getArguments();
+            @SuppressWarnings("unchecked")
+            final ActionListener<BulkResponse> listener = (ActionListener<BulkResponse>) args[2];
+            final IndexResponse indexResponse = new IndexResponse(
+                new ShardId(INTERNAL_SECURITY_MAIN_INDEX_7, randomAlphaOfLength(22), randomIntBetween(0, 1)),
+                createApiKeyRequest.getId(),
+                randomLongBetween(1, 99),
+                randomLongBetween(1, 99),
+                randomIntBetween(1, 99),
+                true
+            );
+            listener.onResponse(
+                new BulkResponse(
+                    new BulkItemResponse[] { BulkItemResponse.success(randomInt(), DocWriteRequest.OpType.INDEX, indexResponse) },
+                    randomLongBetween(0, 100)
+                )
+            );
+            return null;
+        }).when(client).execute(eq(TransportBulkAction.TYPE), any(BulkRequest.class), any());
+
+        assertThat(service.getFromCache(createApiKeyRequest.getId()), is(nullValue()));
+        final PlainActionFuture<CreateApiKeyResponse> listener = new PlainActionFuture<>();
+        service.createApiKey(authentication, createApiKeyRequest, Set.of(), listener);
+        final CreateApiKeyResponse createApiKeyResponse = listener.actionGet();
+        assertThat(createApiKeyResponse.getId(), equalTo(createApiKeyRequest.getId()));
+        assertThat(service.getFromCache(createApiKeyResponse.getId()), is(nullValue()));
+    }
+
     public void testGetCreatorRealm() {
         final User user = AuthenticationTests.randomUser();
 

```
