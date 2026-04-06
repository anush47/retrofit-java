# Phase 0 Inputs

- Mainline commit: eed650ec63b27609c3512be487f9d2f50a988739
- Backport commit: 0e0b4fbec2ebfd153fa18c9e665e4e51713a41b7
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 6

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapper.java']
- Developer Java files: ['server/src/main/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapper.java']
- Overlap Java files: ['server/src/main/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapper.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From eed650ec63b27609c3512be487f9d2f50a988739 Mon Sep 17 00:00:00 2001
From: Gal Lalouche <gal.lalouche@elastic.co>
Date: Thu, 26 Dec 2024 13:39:40 +0200
Subject: [PATCH] ESQL: Fix AbstractShapeGeometryFieldMapperTests (#119265)

Fixed a bug in AbstractShapeGeometryFieldMapperTests when the directory reader would contain multiple leaves.

Resolves #119201.
---
 docs/changelog/119265.yaml                    |  6 ++++
 .../AbstractShapeGeometryFieldMapper.java     |  5 ++-
 ...AbstractShapeGeometryFieldMapperTests.java | 33 ++++++++++++++-----
 3 files changed, 35 insertions(+), 9 deletions(-)
 create mode 100644 docs/changelog/119265.yaml

diff --git a/docs/changelog/119265.yaml b/docs/changelog/119265.yaml
new file mode 100644
index 00000000000..296106b9c01
--- /dev/null
+++ b/docs/changelog/119265.yaml
@@ -0,0 +1,6 @@
+pr: 119265
+summary: Fix `AbstractShapeGeometryFieldMapperTests`
+area: "ES|QL"
+type: bug
+issues:
+ - 119201
diff --git a/server/src/main/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapper.java b/server/src/main/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapper.java
index 4b0542f7f7b..318e877c7eb 100644
--- a/server/src/main/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapper.java
+++ b/server/src/main/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapper.java
@@ -124,7 +124,10 @@ public abstract class AbstractShapeGeometryFieldMapper<T> extends AbstractGeomet
 
                     private void read(BinaryDocValues binaryDocValues, int doc, GeometryDocValueReader reader, BytesRefBuilder builder)
                         throws IOException {
-                        binaryDocValues.advanceExact(doc);
+                        if (binaryDocValues.advanceExact(doc) == false) {
+                            builder.appendNull();
+                            return;
+                        }
                         reader.reset(binaryDocValues.binaryValue());
                         var extent = reader.getExtent();
                         // This is rather silly: an extent is already encoded as ints, but we convert it to Rectangle to
diff --git a/server/src/test/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapperTests.java b/server/src/test/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapperTests.java
index bd58f4d443d..9d344a31905 100644
--- a/server/src/test/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapperTests.java
+++ b/server/src/test/java/org/elasticsearch/index/mapper/AbstractShapeGeometryFieldMapperTests.java
@@ -11,7 +11,7 @@ package org.elasticsearch.index.mapper;
 
 import org.apache.lucene.document.Document;
 import org.apache.lucene.index.DirectoryReader;
-import org.apache.lucene.index.LeafReaderContext;
+import org.apache.lucene.index.LeafReader;
 import org.apache.lucene.store.Directory;
 import org.apache.lucene.tests.index.RandomIndexWriter;
 import org.apache.lucene.util.BytesRef;
@@ -30,6 +30,7 @@ import org.elasticsearch.test.hamcrest.RectangleMatcher;
 import org.elasticsearch.test.hamcrest.WellKnownBinaryBytesRefMatcher;
 
 import java.io.IOException;
+import java.util.ArrayList;
 import java.util.Optional;
 import java.util.function.Function;
 import java.util.function.Supplier;
@@ -61,7 +62,7 @@ public class AbstractShapeGeometryFieldMapperTests extends ESTestCase {
         Function<String, ShapeIndexer> indexerFactory,
         Function<Geometry, Optional<Rectangle>> visitor
     ) throws IOException {
-        var geometries = IntStream.range(0, 20).mapToObj(i -> generator.get()).toList();
+        var geometries = IntStream.range(0, 50).mapToObj(i -> generator.get()).toList();
         var loader = new AbstractShapeGeometryFieldMapper.AbstractShapeGeometryFieldType.BoundsBlockLoader("field", encoder);
         try (Directory directory = newDirectory()) {
             try (var iw = new RandomIndexWriter(random(), directory)) {
@@ -73,23 +74,39 @@ public class AbstractShapeGeometryFieldMapperTests extends ESTestCase {
                     iw.addDocument(doc);
                 }
             }
-            var indices = IntStream.range(0, geometries.size() / 2).map(x -> x * 2).toArray();
+            // We specifically check just the even indices, to verify the loader can skip documents correctly.
+            var evenIndices = evenArray(geometries.size());
             try (DirectoryReader reader = DirectoryReader.open(directory)) {
-                LeafReaderContext ctx = reader.leaves().get(0);
-                TestBlock block = (TestBlock) loader.reader(ctx).read(TestBlock.factory(ctx.reader().numDocs()), TestBlock.docs(indices));
-                for (int i = 0; i < indices.length; i++) {
-                    var idx = indices[i];
+                var byteRefResults = new ArrayList<BytesRef>();
+                for (var leaf : reader.leaves()) {
+                    LeafReader leafReader = leaf.reader();
+                    int numDocs = leafReader.numDocs();
+                    try (
+                        TestBlock block = (TestBlock) loader.reader(leaf)
+                            .read(TestBlock.factory(leafReader.numDocs()), TestBlock.docs(evenArray(numDocs)))
+                    ) {
+                        for (int i = 0; i < block.size(); i++) {
+                            byteRefResults.add((BytesRef) block.get(i));
+                        }
+                    }
+                }
+                for (int i = 0; i < evenIndices.length; i++) {
+                    var idx = evenIndices[i];
                     var geometry = geometries.get(idx);
                     var geoString = geometry.toString();
                     var geometryString = geoString.length() > 200 ? geoString.substring(0, 200) + "..." : geoString;
                     Rectangle r = visitor.apply(geometry).get();
                     assertThat(
                         Strings.format("geometries[%d] ('%s') wasn't extracted correctly", idx, geometryString),
-                        (BytesRef) block.get(i),
+                        byteRefResults.get(i),
                         WellKnownBinaryBytesRefMatcher.encodes(RectangleMatcher.closeToFloat(r, 1e-3, encoder))
                     );
                 }
             }
         }
     }
+
+    private static int[] evenArray(int maxIndex) {
+        return IntStream.range(0, maxIndex / 2).map(x -> x * 2).toArray();
+    }
 }
-- 
2.43.0


```
