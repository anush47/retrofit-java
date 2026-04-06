# Phase 0 Inputs

- Mainline commit: e1451997b1bbbf3f22b4b552352e65dc62e6a947
- Backport commit: fc63a614ee3059cc361458efb02aed6eb68d6629
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 2

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilder.java']
- Developer Java files: ['x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilder.java']
- Overlap Java files: ['x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilder.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From e1451997b1bbbf3f22b4b552352e65dc62e6a947 Mon Sep 17 00:00:00 2001
From: Dan Rubinstein <daniel.rubinstein@elastic.co>
Date: Mon, 14 Oct 2024 10:51:50 -0400
Subject: [PATCH] [ML] Switch default chunking strategy to sentence (#114453)

---
 docs/changelog/114453.yaml                                   | 5 +++++
 .../xpack/inference/chunking/ChunkingSettingsBuilder.java    | 2 +-
 .../inference/chunking/ChunkingSettingsBuilderTests.java     | 2 +-
 3 files changed, 7 insertions(+), 2 deletions(-)
 create mode 100644 docs/changelog/114453.yaml

diff --git a/docs/changelog/114453.yaml b/docs/changelog/114453.yaml
new file mode 100644
index 00000000000..0d5345ad9d2
--- /dev/null
+++ b/docs/changelog/114453.yaml
@@ -0,0 +1,5 @@
+pr: 114453
+summary: Switch default chunking strategy to sentence
+area: Machine Learning
+type: enhancement
+issues: []
diff --git a/x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilder.java b/x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilder.java
index 477c3ea6352..20520ca8292 100644
--- a/x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilder.java
+++ b/x-pack/plugin/inference/src/main/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilder.java
@@ -13,7 +13,7 @@ import org.elasticsearch.inference.ChunkingStrategy;
 import java.util.Map;
 
 public class ChunkingSettingsBuilder {
-    public static final WordBoundaryChunkingSettings DEFAULT_SETTINGS = new WordBoundaryChunkingSettings(250, 100);
+    public static final SentenceBoundaryChunkingSettings DEFAULT_SETTINGS = new SentenceBoundaryChunkingSettings(250, 1);
 
     public static ChunkingSettings fromMap(Map<String, Object> settings) {
         if (settings.isEmpty()) {
diff --git a/x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilderTests.java b/x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilderTests.java
index 3c09984ac01..5b9625073e6 100644
--- a/x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilderTests.java
+++ b/x-pack/plugin/inference/src/test/java/org/elasticsearch/xpack/inference/chunking/ChunkingSettingsBuilderTests.java
@@ -17,7 +17,7 @@ import java.util.Map;
 
 public class ChunkingSettingsBuilderTests extends ESTestCase {
 
-    public static final WordBoundaryChunkingSettings DEFAULT_SETTINGS = new WordBoundaryChunkingSettings(250, 100);
+    public static final SentenceBoundaryChunkingSettings DEFAULT_SETTINGS = new SentenceBoundaryChunkingSettings(250, 1);
 
     public void testEmptyChunkingSettingsMap() {
         ChunkingSettings chunkingSettings = ChunkingSettingsBuilder.fromMap(Collections.emptyMap());
-- 
2.43.0


```
