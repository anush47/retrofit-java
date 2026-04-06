# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java']
- Developer Java files: ['server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java']
- Overlap Java files: ['server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java']

## File State Comparison
- Compared files: ['server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java']
- Mismatched files: ['server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -359,6 +359,7 @@
         if (mustClauses.size() == 0
             && filterClauses.size() == 0
             && shouldClauses.size() > 0
+            && mustNotClauses.size() == 0
             && newBuilder.shouldClauses.stream().allMatch(b -> b instanceof MatchNoneQueryBuilder)) {
             return new MatchNoneQueryBuilder("The \"" + getName() + "\" query was rewritten to a \"match_none\" query.");
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -359,6 +359,7 @@
-         if (mustClauses.size() == 0
-             && filterClauses.size() == 0
-             && shouldClauses.size() > 0
-+            && mustNotClauses.size() == 0
-             && newBuilder.shouldClauses.stream().allMatch(b -> b instanceof MatchNoneQueryBuilder)) {
-             return new MatchNoneQueryBuilder("The \"" + getName() + "\" query was rewritten to a \"match_none\" query.");
-         }
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
diff --git a/docs/changelog/115031.yaml b/docs/changelog/115031.yaml
new file mode 100644
index 00000000000..d8d6e1a3f81
--- /dev/null
+++ b/docs/changelog/115031.yaml
@@ -0,0 +1,5 @@
+pr: 115031
+summary: Bool query early termination should also consider `must_not` clauses
+area: Search
+type: enhancement
+issues: []
diff --git a/server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java b/server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java
index a7b3b9145d2..d61e69208cf 100644
--- a/server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java
+++ b/server/src/main/java/org/elasticsearch/index/query/BoolQueryBuilder.java
@@ -359,6 +359,7 @@ public class BoolQueryBuilder extends AbstractQueryBuilder<BoolQueryBuilder> {
         if (mustClauses.size() == 0
             && filterClauses.size() == 0
             && shouldClauses.size() > 0
+            && mustNotClauses.size() == 0
             && newBuilder.shouldClauses.stream().allMatch(b -> b instanceof MatchNoneQueryBuilder)) {
             return new MatchNoneQueryBuilder("The \"" + getName() + "\" query was rewritten to a \"match_none\" query.");
         }
diff --git a/server/src/test/java/org/elasticsearch/index/query/BoolQueryBuilderTests.java b/server/src/test/java/org/elasticsearch/index/query/BoolQueryBuilderTests.java
index 25d4c1008ba..0fa8f70525e 100644
--- a/server/src/test/java/org/elasticsearch/index/query/BoolQueryBuilderTests.java
+++ b/server/src/test/java/org/elasticsearch/index/query/BoolQueryBuilderTests.java
@@ -449,6 +449,12 @@ public class BoolQueryBuilderTests extends AbstractQueryTestCase<BoolQueryBuilde
         rewritten = Rewriteable.rewrite(boolQueryBuilder, createSearchExecutionContext());
         assertNotEquals(new MatchNoneQueryBuilder(), rewritten);
 
+        boolQueryBuilder = new BoolQueryBuilder();
+        boolQueryBuilder.should(new WrapperQueryBuilder(new MatchNoneQueryBuilder().toString()));
+        boolQueryBuilder.mustNot(new TermQueryBuilder(TEXT_FIELD_NAME, "bar"));
+        rewritten = Rewriteable.rewrite(boolQueryBuilder, createSearchExecutionContext());
+        assertNotEquals(new MatchNoneQueryBuilder(), rewritten);
+
         boolQueryBuilder = new BoolQueryBuilder();
         boolQueryBuilder.filter(new TermQueryBuilder(TEXT_FIELD_NAME, "bar"));
         boolQueryBuilder.mustNot(new WrapperQueryBuilder(new WrapperQueryBuilder(new MatchAllQueryBuilder().toString()).toString()));

```
