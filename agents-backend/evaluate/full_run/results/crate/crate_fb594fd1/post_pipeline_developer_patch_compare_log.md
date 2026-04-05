# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

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
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/execution/dml/Indexer.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -1055,6 +1055,9 @@
 
     public Object[] addGeneratedValues(IndexItem item) {
         Object[] insertValues = item.insertValues();
+        if (onConflictIndexer() == null && undeterministic.isEmpty()) {
+            return insertValues;
+        }
         assert onConflictIndexer() == null || new HashSet<>(onConflictIndexer().insertColumns().stream().map(Reference::column).toList())
             .containsAll(insertColumns().stream().map(Reference::column).toList()) : "onConflictIndexer().insertColumns() is a superset of this.insertColumns()";
         List<Reference> insertColumns = onConflictIndexer() == null ? insertColumns() : onConflictIndexer().insertColumns();

```

Generated
```diff
@@ -1055,6 +1055,9 @@
 
     public Object[] addGeneratedValues(IndexItem item) {
         Object[] insertValues = item.insertValues();
+        if (onConflictIndexer() == null && undeterministic.isEmpty()) {
+            return insertValues;
+        }
         assert onConflictIndexer() == null || new HashSet<>(onConflictIndexer().insertColumns().stream().map(Reference::column).toList())
             .containsAll(insertColumns().stream().map(Reference::column).toList()) : "onConflictIndexer().insertColumns() is a superset of this.insertColumns()";
         List<Reference> insertColumns = onConflictIndexer() == null ? insertColumns() : onConflictIndexer().insertColumns();

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/execution/dml/Indexer.java b/server/src/main/java/io/crate/execution/dml/Indexer.java
index a3b6bee9de..70b2d8bb38 100644
--- a/server/src/main/java/io/crate/execution/dml/Indexer.java
+++ b/server/src/main/java/io/crate/execution/dml/Indexer.java
@@ -1055,6 +1055,9 @@ public class Indexer {
 
     public Object[] addGeneratedValues(IndexItem item) {
         Object[] insertValues = item.insertValues();
+        if (onConflictIndexer() == null && undeterministic.isEmpty()) {
+            return insertValues;
+        }
         assert onConflictIndexer() == null || new HashSet<>(onConflictIndexer().insertColumns().stream().map(Reference::column).toList())
             .containsAll(insertColumns().stream().map(Reference::column).toList()) : "onConflictIndexer().insertColumns() is a superset of this.insertColumns()";
         List<Reference> insertColumns = onConflictIndexer() == null ? insertColumns() : onConflictIndexer().insertColumns();

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/execution/dml/Indexer.java b/server/src/main/java/io/crate/execution/dml/Indexer.java
index a3b6bee9de..70b2d8bb38 100644
--- a/server/src/main/java/io/crate/execution/dml/Indexer.java
+++ b/server/src/main/java/io/crate/execution/dml/Indexer.java
@@ -1055,6 +1055,9 @@ public class Indexer {
 
     public Object[] addGeneratedValues(IndexItem item) {
         Object[] insertValues = item.insertValues();
+        if (onConflictIndexer() == null && undeterministic.isEmpty()) {
+            return insertValues;
+        }
         assert onConflictIndexer() == null || new HashSet<>(onConflictIndexer().insertColumns().stream().map(Reference::column).toList())
             .containsAll(insertColumns().stream().map(Reference::column).toList()) : "onConflictIndexer().insertColumns() is a superset of this.insertColumns()";
         List<Reference> insertColumns = onConflictIndexer() == null ? insertColumns() : onConflictIndexer().insertColumns();

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/server/src/main/java/io/crate/execution/dml/Indexer.java b/server/src/main/java/io/crate/execution/dml/Indexer.java
index a3b6bee9de..70b2d8bb38 100644
--- a/server/src/main/java/io/crate/execution/dml/Indexer.java
+++ b/server/src/main/java/io/crate/execution/dml/Indexer.java
@@ -1055,6 +1055,9 @@ public class Indexer {
 
     public Object[] addGeneratedValues(IndexItem item) {
         Object[] insertValues = item.insertValues();
+        if (onConflictIndexer() == null && undeterministic.isEmpty()) {
+            return insertValues;
+        }
         assert onConflictIndexer() == null || new HashSet<>(onConflictIndexer().insertColumns().stream().map(Reference::column).toList())
             .containsAll(insertColumns().stream().map(Reference::column).toList()) : "onConflictIndexer().insertColumns() is a superset of this.insertColumns()";
         List<Reference> insertColumns = onConflictIndexer() == null ? insertColumns() : onConflictIndexer().insertColumns();
diff --git a/server/src/test/java/io/crate/integrationtests/InsertIntoIntegrationTest.java b/server/src/test/java/io/crate/integrationtests/InsertIntoIntegrationTest.java
index b019997a5d..345421267c 100644
--- a/server/src/test/java/io/crate/integrationtests/InsertIntoIntegrationTest.java
+++ b/server/src/test/java/io/crate/integrationtests/InsertIntoIntegrationTest.java
@@ -2415,6 +2415,26 @@ public class InsertIntoIntegrationTest extends IntegTestCase {
         assertThat(response.rows()[0][2]).isEqualTo(oob);
     }
 
+    @Test
+    public void test_insert_on_conflict_does_not_modify_unassigned_deterministic_default_columns() {
+        execute("""
+            create table t (
+                a int default -1,
+                i int,
+                c int primary key
+            )
+            """);
+        execute("insert into t(c,i) values (0, 1) on conflict (c) do update set i=11");
+        execute("refresh table t");
+        execute("select c, i, a from t");
+        assertThat(response).hasRows("0| 1| -1");
+
+        execute("insert into t(c,i) values (6, 7), (0, 1), (5, 6) on conflict (c) do update set i=11");
+        execute("refresh table t");
+        execute("select c, i, a from t order by c");
+        assertThat(response).hasRows("0| 11| -1", "5| 6| -1", "6| 7| -1");
+    }
+
     @Test
     public void test_insert_on_conflict_can_assign_to_default_columns() {
         execute("""

```
