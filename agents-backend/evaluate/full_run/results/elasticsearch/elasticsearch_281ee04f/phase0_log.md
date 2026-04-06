# Phase 0 Inputs

- Mainline commit: 281ee04f7aa227df3d734b3593232dca23b30d0a
- Backport commit: 25dbb58f01876c64a07ea5c085e73ca275c66a98
- Java-only files for agentic phases: 2
- Developer auxiliary hunks (test + non-Java): 4

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['libs/x-content/impl/src/main/java/org/elasticsearch/xcontent/provider/json/JsonXContentParser.java', 'server/src/main/java/org/elasticsearch/index/mapper/IpFieldMapper.java']
- Developer Java files: ['libs/x-content/impl/src/main/java/org/elasticsearch/xcontent/provider/json/JsonXContentParser.java', 'server/src/main/java/org/elasticsearch/index/mapper/IpFieldMapper.java']
- Overlap Java files: ['libs/x-content/impl/src/main/java/org/elasticsearch/xcontent/provider/json/JsonXContentParser.java', 'server/src/main/java/org/elasticsearch/index/mapper/IpFieldMapper.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 281ee04f7aa227df3d734b3593232dca23b30d0a Mon Sep 17 00:00:00 2001
From: Benjamin Trent <ben.w.trent@gmail.com>
Date: Wed, 11 Sep 2024 10:15:56 -0400
Subject: [PATCH] JSON parse failures should be 4xx codes (#112703)

It seemed if there wasn't any text to parse, this is not an internal
issue but instead an argument issue.

I simply changed the exception thrown. If we don't agree with this, I
can adjust `query` parsing directly, but this seemed like the better
choice.

closes: https://github.com/elastic/elasticsearch/issues/112296
---
 docs/changelog/112703.yaml                           |  5 +++++
 .../xcontent/provider/json/JsonXContentParser.java   |  2 +-
 .../elasticsearch/index/mapper/IpFieldMapper.java    | 12 ++----------
 .../org/elasticsearch/common/ReferenceDocsTests.java |  2 +-
 .../index/query/MatchQueryBuilderTests.java          |  2 +-
 5 files changed, 10 insertions(+), 13 deletions(-)
 create mode 100644 docs/changelog/112703.yaml

diff --git a/docs/changelog/112703.yaml b/docs/changelog/112703.yaml
new file mode 100644
index 00000000000..a428e8c4e23
--- /dev/null
+++ b/docs/changelog/112703.yaml
@@ -0,0 +1,5 @@
+pr: 112703
+summary: JSON parse failures should be 4xx codes
+area: Infra/Core
+type: bug
+issues: []
diff --git a/libs/x-content/impl/src/main/java/org/elasticsearch/xcontent/provider/json/JsonXContentParser.java b/libs/x-content/impl/src/main/java/org/elasticsearch/xcontent/provider/json/JsonXContentParser.java
index c59f003d9cb..63191084ca8 100644
--- a/libs/x-content/impl/src/main/java/org/elasticsearch/xcontent/provider/json/JsonXContentParser.java
+++ b/libs/x-content/impl/src/main/java/org/elasticsearch/xcontent/provider/json/JsonXContentParser.java
@@ -111,7 +111,7 @@ public class JsonXContentParser extends AbstractXContentParser {
     }
 
     private void throwOnNoText() {
-        throw new IllegalStateException("Can't get text on a " + currentToken() + " at " + getTokenLocation());
+        throw new IllegalArgumentException("Expected text at " + getTokenLocation() + " but found " + currentToken());
     }
 
     @Override
diff --git a/server/src/main/java/org/elasticsearch/index/mapper/IpFieldMapper.java b/server/src/main/java/org/elasticsearch/index/mapper/IpFieldMapper.java
index 062e7551a53..638af1a1053 100644
--- a/server/src/main/java/org/elasticsearch/index/mapper/IpFieldMapper.java
+++ b/server/src/main/java/org/elasticsearch/index/mapper/IpFieldMapper.java
@@ -42,7 +42,6 @@ import org.elasticsearch.search.DocValueFormat;
 import org.elasticsearch.search.aggregations.support.CoreValuesSourceType;
 import org.elasticsearch.search.lookup.FieldValues;
 import org.elasticsearch.search.lookup.SearchLookup;
-import org.elasticsearch.xcontent.XContentParser;
 
 import java.io.IOException;
 import java.net.InetAddress;
@@ -545,8 +544,9 @@ public class IpFieldMapper extends FieldMapper {
     @Override
     protected void parseCreateField(DocumentParserContext context) throws IOException {
         InetAddress address;
+        String value = context.parser().textOrNull();
         try {
-            address = value(context.parser(), nullValue);
+            address = value == null ? nullValue : InetAddresses.forString(value);
         } catch (IllegalArgumentException e) {
             if (ignoreMalformed) {
                 context.addIgnoredField(fieldType().name());
@@ -564,14 +564,6 @@ public class IpFieldMapper extends FieldMapper {
         }
     }
 
-    private static InetAddress value(XContentParser parser, InetAddress nullValue) throws IOException {
-        String value = parser.textOrNull();
-        if (value == null) {
-            return nullValue;
-        }
-        return InetAddresses.forString(value);
-    }
-
     private void indexValue(DocumentParserContext context, InetAddress address) {
         if (dimension) {
             context.getDimensions().addIp(fieldType().name(), address).validate(context.indexSettings());
diff --git a/server/src/test/java/org/elasticsearch/common/ReferenceDocsTests.java b/server/src/test/java/org/elasticsearch/common/ReferenceDocsTests.java
index 0fabf780173..49208f23417 100644
--- a/server/src/test/java/org/elasticsearch/common/ReferenceDocsTests.java
+++ b/server/src/test/java/org/elasticsearch/common/ReferenceDocsTests.java
@@ -66,7 +66,7 @@ public class ReferenceDocsTests extends ESTestCase {
             builder.startObject("UNEXPECTED").endObject().endObject();
 
             try (var stream = BytesReference.bytes(builder).streamInput()) {
-                expectThrows(IllegalStateException.class, () -> ReferenceDocs.readLinksBySymbol(stream));
+                expectThrows(IllegalArgumentException.class, () -> ReferenceDocs.readLinksBySymbol(stream));
             }
         }
 
diff --git a/server/src/test/java/org/elasticsearch/index/query/MatchQueryBuilderTests.java b/server/src/test/java/org/elasticsearch/index/query/MatchQueryBuilderTests.java
index 278d4ae505b..48e8f0ef116 100644
--- a/server/src/test/java/org/elasticsearch/index/query/MatchQueryBuilderTests.java
+++ b/server/src/test/java/org/elasticsearch/index/query/MatchQueryBuilderTests.java
@@ -373,7 +373,7 @@ public class MatchQueryBuilderTests extends AbstractQueryTestCase<MatchQueryBuil
                 "message1" : ["term1", "term2"]
               }
             }""";
-        expectThrows(IllegalStateException.class, () -> parseQuery(json2));
+        expectThrows(IllegalArgumentException.class, () -> parseQuery(json2));
     }
 
     public void testExceptionUsingAnalyzerOnNumericField() {
-- 
2.43.0


```
