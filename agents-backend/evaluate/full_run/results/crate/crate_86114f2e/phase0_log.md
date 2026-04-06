# Phase 0 Inputs

- Mainline commit: 86114f2ec05fea5c5ab56a9cfbe07c6cab131fb4
- Backport commit: bdeaef7f4e12e362f1da67fd7c13fc68e999bff6
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 2

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/analyze/where/EqualityExtractor.java']
- Developer Java files: ['server/src/main/java/io/crate/analyze/where/EqualityExtractor.java']
- Overlap Java files: ['server/src/main/java/io/crate/analyze/where/EqualityExtractor.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 86114f2ec05fea5c5ab56a9cfbe07c6cab131fb4 Mon Sep 17 00:00:00 2001
From: Mathias Fussenegger <f.mathias@zignar.net>
Date: Mon, 13 Jan 2025 12:28:09 +0100
Subject: [PATCH] Fix NPE in EqualityExtractor for pk/non-pk mixes

A query like `WHERE (recorddesc ='user documents' OR recordid=110 ) AND
(...)`
caused a NPE because `visitFunction` returned a `NULL` if first seeing a
non-pk followed by a PK.
---
 docs/appendices/release-notes/5.9.7.rst                  | 4 ++++
 .../java/io/crate/analyze/where/EqualityExtractor.java   | 2 +-
 .../io/crate/analyze/where/EqualityExtractorTest.java    | 9 +++++++++
 3 files changed, 14 insertions(+), 1 deletion(-)

diff --git a/docs/appendices/release-notes/5.9.7.rst b/docs/appendices/release-notes/5.9.7.rst
index de3d645921..6dca320174 100644
--- a/docs/appendices/release-notes/5.9.7.rst
+++ b/docs/appendices/release-notes/5.9.7.rst
@@ -47,6 +47,10 @@ See the :ref:`version_5.9.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- Fixed an issue that could cause queries to run into a ``NullPointerException``
+  if having a query condition like ``(nonPrimaryKey = ? AND primaryKeyPart =
+  ?)``
+
 - Fixed an issue that caused ``FILTER`` clauses on non-aggregate window
   functions to be ignored instead of raising an unsupported error.
 
diff --git a/server/src/main/java/io/crate/analyze/where/EqualityExtractor.java b/server/src/main/java/io/crate/analyze/where/EqualityExtractor.java
index e78038eaf2..04c9c3ba57 100644
--- a/server/src/main/java/io/crate/analyze/where/EqualityExtractor.java
+++ b/server/src/main/java/io/crate/analyze/where/EqualityExtractor.java
@@ -485,7 +485,7 @@ public class EqualityExtractor {
                     proxyBelowPost = ctx.proxyBelow || proxyBelowPost;
                 }
                 if ((ctx.foundPKColumnUnderOr && ctx.foundNonPKColumnUnderOr) || ctx.foundPKColumnUnderNot) {
-                    return null;
+                    return Literal.BOOLEAN_FALSE;
                 }
                 ctx.isUnderNotPredicate = prevIsUnderNotPredicate;
                 ctx.proxyBelow = proxyBelowPost;
diff --git a/server/src/test/java/io/crate/analyze/where/EqualityExtractorTest.java b/server/src/test/java/io/crate/analyze/where/EqualityExtractorTest.java
index a12c9d0157..d43a37e5e5 100644
--- a/server/src/test/java/io/crate/analyze/where/EqualityExtractorTest.java
+++ b/server/src/test/java/io/crate/analyze/where/EqualityExtractorTest.java
@@ -477,6 +477,15 @@ public class EqualityExtractorTest extends CrateDummyClusterServiceUnitTest {
             .hasMessage("Job killed. statement_timeout (10ms)");
     }
 
+    @Test
+    public void test_no_exact_result_on_partial_match() throws Exception {
+        // https://github.com/crate/crate/issues/17197
+        // It is important that the query first hits a non-pk column
+        Symbol query = query("(i = 1 or x = 2) and (i = 2 and a = 'foo')");
+        List<List<Symbol>> analyzeExact = analyzeExact(query, List.of(ColumnIdent.of("x")));
+        assertThat(analyzeExact).isNull();
+    }
+
     public static class TestToken extends Session.TimeoutToken {
 
         private final int maxChecks;
-- 
2.43.0


```
