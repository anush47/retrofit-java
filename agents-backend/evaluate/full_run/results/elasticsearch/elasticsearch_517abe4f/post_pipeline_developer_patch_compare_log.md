# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java']
- Developer Java files: ['server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java']
- Overlap Java files: ['server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java']

## File State Comparison
- Compared files: ['server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java']
- Mismatched files: ['server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -13,6 +13,7 @@
 import org.elasticsearch.cluster.node.DiscoveryNode;
 import org.elasticsearch.common.io.stream.StreamInput;
 import org.elasticsearch.common.io.stream.StreamOutput;
+import org.elasticsearch.rest.RestStatus;
 
 import java.io.IOException;
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -13,6 +13,7 @@
- import org.elasticsearch.cluster.node.DiscoveryNode;
- import org.elasticsearch.common.io.stream.StreamInput;
- import org.elasticsearch.common.io.stream.StreamOutput;
-+import org.elasticsearch.rest.RestStatus;
- 
- import java.io.IOException;
- 
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -41,6 +42,18 @@
         }
     }
 
+    /**
+     * The ES REST API is a gateway to a single or multiple clusters. If there is an error connecting to other servers, then we should
+     * return a 502 BAD_GATEWAY status code instead of the parent class' 500 INTERNAL_SERVER_ERROR. Clients tend to retry on a 502 but not
+     * on a 500, and retrying may help on a connection error.
+     *
+     * @return a {@link RestStatus#BAD_GATEWAY} code
+     */
+    @Override
+    public final RestStatus status() {
+        return RestStatus.BAD_GATEWAY;
+    }
+
     @Override
     protected void writeTo(StreamOutput out, Writer<Throwable> nestedExceptionsWriter) throws IOException {
         super.writeTo(out, nestedExceptionsWriter);

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,19 +1 @@-@@ -41,6 +42,18 @@
-         }
-     }
- 
-+    /**
-+     * The ES REST API is a gateway to a single or multiple clusters. If there is an error connecting to other servers, then we should
-+     * return a 502 BAD_GATEWAY status code instead of the parent class' 500 INTERNAL_SERVER_ERROR. Clients tend to retry on a 502 but not
-+     * on a 500, and retrying may help on a connection error.
-+     *
-+     * @return a {@link RestStatus#BAD_GATEWAY} code
-+     */
-+    @Override
-+    public final RestStatus status() {
-+        return RestStatus.BAD_GATEWAY;
-+    }
-+
-     @Override
-     protected void writeTo(StreamOutput out, Writer<Throwable> nestedExceptionsWriter) throws IOException {
-         super.writeTo(out, nestedExceptionsWriter);
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
diff --git a/docs/changelog/118681.yaml b/docs/changelog/118681.yaml
new file mode 100644
index 00000000000..a186c05e6cd
--- /dev/null
+++ b/docs/changelog/118681.yaml
@@ -0,0 +1,6 @@
+pr: 118681
+summary: '`ConnectTransportException` returns retryable BAD_GATEWAY'
+area: Network
+type: enhancement
+issues:
+ - 118320
diff --git a/server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java b/server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java
index 648d27c8858..302175cc4f5 100644
--- a/server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java
+++ b/server/src/main/java/org/elasticsearch/transport/ConnectTransportException.java
@@ -13,6 +13,7 @@ import org.elasticsearch.TransportVersions;
 import org.elasticsearch.cluster.node.DiscoveryNode;
 import org.elasticsearch.common.io.stream.StreamInput;
 import org.elasticsearch.common.io.stream.StreamOutput;
+import org.elasticsearch.rest.RestStatus;
 
 import java.io.IOException;
 
@@ -41,6 +42,18 @@ public class ConnectTransportException extends ActionTransportException {
         }
     }
 
+    /**
+     * The ES REST API is a gateway to a single or multiple clusters. If there is an error connecting to other servers, then we should
+     * return a 502 BAD_GATEWAY status code instead of the parent class' 500 INTERNAL_SERVER_ERROR. Clients tend to retry on a 502 but not
+     * on a 500, and retrying may help on a connection error.
+     *
+     * @return a {@link RestStatus#BAD_GATEWAY} code
+     */
+    @Override
+    public final RestStatus status() {
+        return RestStatus.BAD_GATEWAY;
+    }
+
     @Override
     protected void writeTo(StreamOutput out, Writer<Throwable> nestedExceptionsWriter) throws IOException {
         super.writeTo(out, nestedExceptionsWriter);
diff --git a/server/src/test/java/org/elasticsearch/ExceptionSerializationTests.java b/server/src/test/java/org/elasticsearch/ExceptionSerializationTests.java
index 31739850e2d..412513051b3 100644
--- a/server/src/test/java/org/elasticsearch/ExceptionSerializationTests.java
+++ b/server/src/test/java/org/elasticsearch/ExceptionSerializationTests.java
@@ -410,6 +410,7 @@ public class ExceptionSerializationTests extends ESTestCase {
         ex = serialize(new ConnectTransportException(node, "msg", "action", new NullPointerException()));
         assertEquals("[][" + transportAddress + "][action] msg", ex.getMessage());
         assertThat(ex.getCause(), instanceOf(NullPointerException.class));
+        assertEquals(RestStatus.BAD_GATEWAY, ex.status());
     }
 
     public void testSearchPhaseExecutionException() throws IOException {

```
