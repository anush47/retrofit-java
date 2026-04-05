# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java']
- Developer Java files: ['server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java']
- Overlap Java files: ['server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java']
- Mismatched files: ['server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -57,7 +57,7 @@
 
         private int size = 0;
         private BytesStreamOutput out;
-        private int prevOutSize = 0;
+        private long prevRamUsed = 0L;
 
         public Builder(Streamer<?>[] streamers, RamAccounting ramAccounting) {
             this.ramAccounting = requireNonNull(ramAccounting, "RamAccounting must not be null");

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,9 +1 @@-@@ -57,7 +57,7 @@
- 
-         private int size = 0;
-         private BytesStreamOutput out;
--        private int prevOutSize = 0;
-+        private long prevRamUsed = 0L;
- 
-         public Builder(Streamer<?>[] streamers, RamAccounting ramAccounting) {
-             this.ramAccounting = requireNonNull(ramAccounting, "RamAccounting must not be null");
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -78,8 +78,8 @@
                     throw new RuntimeException(e);
                 }
             }
-            ramAccounting.addBytes(out.size() - prevOutSize);
-            prevOutSize = out.size();
+            ramAccounting.addBytes(out.ramBytesUsed() - prevRamUsed);
+            prevRamUsed = out.ramBytesUsed();
         }
 
         public StreamBucket build() {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,11 +1 @@-@@ -78,8 +78,8 @@
-                     throw new RuntimeException(e);
-                 }
-             }
--            ramAccounting.addBytes(out.size() - prevOutSize);
--            prevOutSize = out.size();
-+            ramAccounting.addBytes(out.ramBytesUsed() - prevRamUsed);
-+            prevRamUsed = out.ramBytesUsed();
-         }
- 
-         public StreamBucket build() {
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
diff --git a/docs/appendices/release-notes/5.10.12.rst b/docs/appendices/release-notes/5.10.12.rst
index 0a0ec2c14e..c18e6b5051 100644
--- a/docs/appendices/release-notes/5.10.12.rst
+++ b/docs/appendices/release-notes/5.10.12.rst
@@ -65,3 +65,6 @@ Fixes
 
 - Fixed an issue that prevented users to change the value of the
   :ref:`indices.recovery.max_concurrent_file_chunks` setting.
+
+- Fixed an issue that could lead to an ``OutOfMemoryError`` when running a
+  query with aggregations under memory pressure in a multi-node cluster.
diff --git a/docs/appendices/release-notes/6.0.1.rst b/docs/appendices/release-notes/6.0.1.rst
index dc1c235473..aa9c4480c0 100644
--- a/docs/appendices/release-notes/6.0.1.rst
+++ b/docs/appendices/release-notes/6.0.1.rst
@@ -68,3 +68,6 @@ Fixes
 
 - Fixed an issue that prevented users to change the value of the
   :ref:`indices.recovery.max_concurrent_file_chunks` setting.
+
+- Fixed an issue that could lead to an ``OutOfMemoryError`` when running a
+  query with aggregations under memory pressure in a multi-node cluster.
diff --git a/server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java b/server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java
index 70236198c7..b4ab299664 100644
--- a/server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java
+++ b/server/src/main/java/io/crate/execution/engine/distribution/StreamBucket.java
@@ -57,7 +57,7 @@ public class StreamBucket implements Bucket, Writeable {
 
         private int size = 0;
         private BytesStreamOutput out;
-        private int prevOutSize = 0;
+        private long prevRamUsed = 0L;
 
         public Builder(Streamer<?>[] streamers, RamAccounting ramAccounting) {
             this.ramAccounting = requireNonNull(ramAccounting, "RamAccounting must not be null");
@@ -78,8 +78,8 @@ public class StreamBucket implements Bucket, Writeable {
                     throw new RuntimeException(e);
                 }
             }
-            ramAccounting.addBytes(out.size() - prevOutSize);
-            prevOutSize = out.size();
+            ramAccounting.addBytes(out.ramBytesUsed() - prevRamUsed);
+            prevRamUsed = out.ramBytesUsed();
         }
 
         public StreamBucket build() {
diff --git a/server/src/test/java/io/crate/execution/engine/distribution/StreamBucketTest.java b/server/src/test/java/io/crate/execution/engine/distribution/StreamBucketTest.java
new file mode 100644
index 0000000000..57bf5102c4
--- /dev/null
+++ b/server/src/test/java/io/crate/execution/engine/distribution/StreamBucketTest.java
@@ -0,0 +1,43 @@
+/*
+ * Licensed to Crate.io GmbH ("Crate") under one or more contributor
+ * license agreements.  See the NOTICE file distributed with this work for
+ * additional information regarding copyright ownership.  Crate licenses
+ * this file to you under the Apache License, Version 2.0 (the "License");
+ * you may not use this file except in compliance with the License.  You may
+ * obtain a copy of the License at
+ *
+ *     http://www.apache.org/licenses/LICENSE-2.0
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
+ * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
+ * License for the specific language governing permissions and limitations
+ * under the License.
+ *
+ * However, if you have executed another commercial license agreement
+ * with Crate these terms will supersede the license and you may use the
+ * software solely pursuant to the terms of the relevant commercial agreement.
+ */
+
+package io.crate.execution.engine.distribution;
+
+import static org.assertj.core.api.Assertions.assertThat;
+
+import org.junit.Test;
+
+import io.crate.Streamer;
+import io.crate.data.RowN;
+import io.crate.testing.PlainRamAccounting;
+import io.crate.types.DataTypes;
+
+public class StreamBucketTest {
+
+    @Test
+    public void test_accounting() {
+        Streamer<?>[] streamers = new Streamer[]{DataTypes.STRING.streamer()};
+        var ramAccounting = new PlainRamAccounting();
+        StreamBucket.Builder builder = new StreamBucket.Builder(streamers, ramAccounting);
+        builder.add(new RowN("0123456789"));
+        assertThat(builder.ramBytesUsed()).isEqualTo(1080L); //Used to be 12
+    }
+}

```
