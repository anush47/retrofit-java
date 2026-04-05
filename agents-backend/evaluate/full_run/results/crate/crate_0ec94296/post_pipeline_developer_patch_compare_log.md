# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/execution/dml/Indexer.java']
- Developer Java files: ['server/src/main/java/io/crate/execution/dml/Indexer.java']
- Overlap Java files: ['server/src/main/java/io/crate/execution/dml/Indexer.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/execution/dml/Indexer.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/execution/dml/Indexer.java']
- Mismatched files: ['server/src/main/java/io/crate/execution/dml/Indexer.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/execution/dml/Indexer.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -947,6 +947,10 @@
                     assert valueIdx < insertValues.length : "Target columns and values must have the same size";
                     root = (Map<String, Object>) insertValues[valueIdx];
                 }
+                // When a null is assigned to a parent object, do not generate nondeterministic children
+                if (root == null) {
+                    continue;
+                }
                 ColumnIdent child = column.shiftRight();
                 Object value = synthetic.value();
                 // We don't override value if it exists.

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,11 +1 @@-@@ -947,6 +947,10 @@
-                     assert valueIdx < insertValues.length : "Target columns and values must have the same size";
-                     root = (Map<String, Object>) insertValues[valueIdx];
-                 }
-+                // When a null is assigned to a parent object, do not generate nondeterministic children
-+                if (root == null) {
-+                    continue;
-+                }
-                 ColumnIdent child = column.shiftRight();
-                 Object value = synthetic.value();
-                 // We don't override value if it exists.
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
index 78d1480a10..a531615eaf 100644
--- a/docs/appendices/release-notes/5.10.12.rst
+++ b/docs/appendices/release-notes/5.10.12.rst
@@ -76,3 +76,6 @@ Fixes
     SELECT sum(x) OVER(PARTITION BY x, y)
     FROM unnest([1], [6]) AS t (x, y)
     GROUP BY x
+
+- Fixed an issue that caused a ``NullPointerException`` when inserting ``NULL``
+  to an object column with a non-deterministic sub-column.
diff --git a/docs/appendices/release-notes/6.0.1.rst b/docs/appendices/release-notes/6.0.1.rst
index 1f37ff73ec..1b597ff44d 100644
--- a/docs/appendices/release-notes/6.0.1.rst
+++ b/docs/appendices/release-notes/6.0.1.rst
@@ -79,3 +79,6 @@ Fixes
     SELECT sum(x) OVER(PARTITION BY x, y)
     FROM unnest([1], [6]) AS t (x, y)
     GROUP BY x
+
+- Fixed an issue that caused a ``NullPointerException`` when inserting ``NULL``
+  to an object column with a non-deterministic sub-column.
diff --git a/server/src/main/java/io/crate/execution/dml/Indexer.java b/server/src/main/java/io/crate/execution/dml/Indexer.java
index a611db6fc9..5aa5eeb04f 100644
--- a/server/src/main/java/io/crate/execution/dml/Indexer.java
+++ b/server/src/main/java/io/crate/execution/dml/Indexer.java
@@ -947,6 +947,10 @@ public class Indexer {
                     assert valueIdx < insertValues.length : "Target columns and values must have the same size";
                     root = (Map<String, Object>) insertValues[valueIdx];
                 }
+                // When a null is assigned to a parent object, do not generate nondeterministic children
+                if (root == null) {
+                    continue;
+                }
                 ColumnIdent child = column.shiftRight();
                 Object value = synthetic.value();
                 // We don't override value if it exists.
diff --git a/server/src/test/java/io/crate/execution/dml/IndexerTest.java b/server/src/test/java/io/crate/execution/dml/IndexerTest.java
index 3c070f46b9..1982886aa9 100644
--- a/server/src/test/java/io/crate/execution/dml/IndexerTest.java
+++ b/server/src/test/java/io/crate/execution/dml/IndexerTest.java
@@ -1096,6 +1096,24 @@ public class IndexerTest extends CrateDummyClusterServiceUnitTest {
         assertThat((int) object.get("x")).isGreaterThan(0);
     }
 
+    public void test_does_not_add_non_deterministic_child_when_parent_is_assigned_to_null() throws Exception {
+        SQLExecutor e = SQLExecutor.of(clusterService)
+            .addTable("""
+                create table tbl (
+                    o object as (
+                        x int as round((random() + 1) * 100)
+                    )
+                )
+                """);
+
+        // insert into tbl values (null)
+        Indexer indexer = getIndexer(e, "tbl", "o");
+        IndexItem item = item((Object) null);
+
+        Object[] insertValues = indexer.addGeneratedValues(item);
+        assertThat(insertValues).containsExactly((Object) null);
+    }
+
     @Test
     public void test_fields_order_in_source_is_deterministic() throws Exception {
         SQLExecutor e = SQLExecutor.of(clusterService)

```
