# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/analyze/CopyAnalyzer.java', 'server/src/main/java/io/crate/analyze/DeleteAnalyzer.java', 'server/src/main/java/io/crate/analyze/InsertAnalyzer.java', 'server/src/main/java/io/crate/analyze/UpdateAnalyzer.java', 'server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java']
- Developer Java files: ['server/src/main/java/io/crate/analyze/CopyAnalyzer.java', 'server/src/main/java/io/crate/analyze/DeleteAnalyzer.java', 'server/src/main/java/io/crate/analyze/InsertAnalyzer.java', 'server/src/main/java/io/crate/analyze/UpdateAnalyzer.java', 'server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java']
- Overlap Java files: ['server/src/main/java/io/crate/analyze/CopyAnalyzer.java', 'server/src/main/java/io/crate/analyze/DeleteAnalyzer.java', 'server/src/main/java/io/crate/analyze/InsertAnalyzer.java', 'server/src/main/java/io/crate/analyze/UpdateAnalyzer.java', 'server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/analyze/CopyAnalyzer.java', 'server/src/main/java/io/crate/analyze/DeleteAnalyzer.java', 'server/src/main/java/io/crate/analyze/InsertAnalyzer.java', 'server/src/main/java/io/crate/analyze/UpdateAnalyzer.java', 'server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/analyze/CopyAnalyzer.java', 'server/src/main/java/io/crate/analyze/DeleteAnalyzer.java', 'server/src/main/java/io/crate/analyze/InsertAnalyzer.java', 'server/src/main/java/io/crate/analyze/UpdateAnalyzer.java', 'server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/analyze/CopyAnalyzer.java

- Developer hunks: 2
- Generated hunks: 2

#### Hunk 1

Developer
```diff
@@ -73,7 +73,8 @@
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            new TableRelation(tableInfo));
+            new TableRelation(tableInfo),
+            f -> f.signature().isDeterministic());
 
         Table<Symbol> table = node.table().map(t -> exprAnalyzerWithFieldsAsString.convert(t, exprCtx));
         GenericProperties<Symbol> properties = node.properties().map(t -> exprAnalyzerWithoutFields.convert(t,

```

Generated
```diff
@@ -73,7 +73,8 @@
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            new TableRelation(tableInfo));
+            new TableRelation(tableInfo),
+            f -> f.signature().isDeterministic());
 
         Table<Symbol> table = node.table().map(t -> exprAnalyzerWithFieldsAsString.convert(t, exprCtx));
         GenericProperties<Symbol> properties = node.properties().map(t -> exprAnalyzerWithoutFields.convert(t,

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -116,7 +117,8 @@
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            tableRelation);
+            tableRelation,
+            f -> f.signature().isDeterministic());
 
         var exprCtx = new ExpressionAnalysisContext(txnCtx.sessionSettings());
         var expressionAnalyzer = new ExpressionAnalyzer(

```

Generated
```diff
@@ -116,7 +117,8 @@
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            tableRelation);
+            tableRelation,
+            f -> f.signature().isDeterministic());
 
         var exprCtx = new ExpressionAnalysisContext(txnCtx.sessionSettings());
         var expressionAnalyzer = new ExpressionAnalyzer(

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### server/src/main/java/io/crate/analyze/DeleteAnalyzer.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -60,11 +60,15 @@
         MaybeAliasedStatement maybeAliasedStatement = MaybeAliasedStatement.analyze(relation);
         relation = maybeAliasedStatement.nonAliasedRelation();
 
-        if (!(relation instanceof DocTableRelation)) {
+        if (!(relation instanceof DocTableRelation table)) {
             throw new UnsupportedOperationException("Cannot delete from relations other than base tables");
         }
-        DocTableRelation table = (DocTableRelation) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         ExpressionAnalyzer expressionAnalyzer = new ExpressionAnalyzer(
             txnContext,
             nodeCtx,

```

Generated
```diff
@@ -60,11 +60,15 @@
         MaybeAliasedStatement maybeAliasedStatement = MaybeAliasedStatement.analyze(relation);
         relation = maybeAliasedStatement.nonAliasedRelation();
 
-        if (!(relation instanceof DocTableRelation)) {
+        if (!(relation instanceof DocTableRelation table)) {
             throw new UnsupportedOperationException("Cannot delete from relations other than base tables");
         }
-        DocTableRelation table = (DocTableRelation) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         ExpressionAnalyzer expressionAnalyzer = new ExpressionAnalyzer(
             txnContext,
             nodeCtx,

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### server/src/main/java/io/crate/analyze/InsertAnalyzer.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -313,7 +313,12 @@
             fieldProvider = new NameFieldProvider(targetTable);
         }
         var expressionAnalyzer = new ExpressionAnalyzer(txnCtx, nodeCtx, paramTypeHints, fieldProvider, null);
-        var normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, targetTable);
+        var normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            targetTable,
+            f -> f.signature().isDeterministic());
         Map<Reference, Symbol> updateAssignments = new HashMap<>(duplicateKeyContext.getAssignments().size());
         for (Assignment<Expression> assignment : duplicateKeyContext.getAssignments()) {
             Reference targetCol = (Reference) exprAnalyzer.convert(assignment.columnName(), exprCtx);

```

Generated
```diff
@@ -313,7 +313,12 @@
             fieldProvider = new NameFieldProvider(targetTable);
         }
         var expressionAnalyzer = new ExpressionAnalyzer(txnCtx, nodeCtx, paramTypeHints, fieldProvider, null);
-        var normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, targetTable);
+        var normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            targetTable,
+            f -> f.signature().isDeterministic());
         Map<Reference, Symbol> updateAssignments = new HashMap<>(duplicateKeyContext.getAssignments().size());
         for (Assignment<Expression> assignment : duplicateKeyContext.getAssignments()) {
             Reference targetCol = (Reference) exprAnalyzer.convert(assignment.columnName(), exprCtx);

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### server/src/main/java/io/crate/analyze/UpdateAnalyzer.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -107,7 +107,12 @@
             throw new UnsupportedOperationException("UPDATE is only supported on base-tables");
         }
         AbstractTableRelation<?> table = (AbstractTableRelation<?>) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         SubqueryAnalyzer subqueryAnalyzer =
             new SubqueryAnalyzer(relationAnalyzer, new StatementAnalysisContext(typeHints, Operation.READ, txnCtx));
 

```

Generated
```diff
@@ -107,7 +107,12 @@
             throw new UnsupportedOperationException("UPDATE is only supported on base-tables");
         }
         AbstractTableRelation<?> table = (AbstractTableRelation<?>) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         SubqueryAnalyzer subqueryAnalyzer =
             new SubqueryAnalyzer(relationAnalyzer, new StatementAnalysisContext(typeHints, Operation.READ, txnCtx));
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -112,7 +112,11 @@
         PartitionReferenceResolver partitionReferenceResolver = preparePartitionResolver(
             tableInfo.partitionedByColumns());
         EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
-            nodeCtx, RowGranularity.PARTITION, partitionReferenceResolver, null);
+            nodeCtx,
+            RowGranularity.PARTITION,
+            partitionReferenceResolver,
+            null,
+            f -> f.signature().isDeterministic());
 
         Symbol normalized;
         Map<Symbol, List<Literal<?>>> queryPartitionMap = new HashMap<>();

```

Generated
```diff
@@ -112,7 +112,11 @@
         PartitionReferenceResolver partitionReferenceResolver = preparePartitionResolver(
             tableInfo.partitionedByColumns());
         EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
-            nodeCtx, RowGranularity.PARTITION, partitionReferenceResolver, null);
+            nodeCtx,
+            RowGranularity.PARTITION,
+            partitionReferenceResolver,
+            null,
+            f -> f.signature().isDeterministic());
 
         Symbol normalized;
         Map<Symbol, List<Literal<?>>> queryPartitionMap = new HashMap<>();

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/analyze/CopyAnalyzer.java b/server/src/main/java/io/crate/analyze/CopyAnalyzer.java
index 44e8093b31..9dcf9e91d7 100644
--- a/server/src/main/java/io/crate/analyze/CopyAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/CopyAnalyzer.java
@@ -73,7 +73,8 @@ class CopyAnalyzer {
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            new TableRelation(tableInfo));
+            new TableRelation(tableInfo),
+            f -> f.signature().isDeterministic());
 
         Table<Symbol> table = node.table().map(t -> exprAnalyzerWithFieldsAsString.convert(t, exprCtx));
         GenericProperties<Symbol> properties = node.properties().map(t -> exprAnalyzerWithoutFields.convert(t,
@@ -116,7 +117,8 @@ class CopyAnalyzer {
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            tableRelation);
+            tableRelation,
+            f -> f.signature().isDeterministic());
 
         var exprCtx = new ExpressionAnalysisContext(txnCtx.sessionSettings());
         var expressionAnalyzer = new ExpressionAnalyzer(
diff --git a/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java b/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java
index 24dbb8a508..d9a735d4b3 100644
--- a/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java
@@ -60,11 +60,15 @@ final class DeleteAnalyzer {
         MaybeAliasedStatement maybeAliasedStatement = MaybeAliasedStatement.analyze(relation);
         relation = maybeAliasedStatement.nonAliasedRelation();
 
-        if (!(relation instanceof DocTableRelation)) {
+        if (!(relation instanceof DocTableRelation table)) {
             throw new UnsupportedOperationException("Cannot delete from relations other than base tables");
         }
-        DocTableRelation table = (DocTableRelation) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         ExpressionAnalyzer expressionAnalyzer = new ExpressionAnalyzer(
             txnContext,
             nodeCtx,
diff --git a/server/src/main/java/io/crate/analyze/InsertAnalyzer.java b/server/src/main/java/io/crate/analyze/InsertAnalyzer.java
index 652ec1b289..6df8ca414e 100644
--- a/server/src/main/java/io/crate/analyze/InsertAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/InsertAnalyzer.java
@@ -313,7 +313,12 @@ class InsertAnalyzer {
             fieldProvider = new NameFieldProvider(targetTable);
         }
         var expressionAnalyzer = new ExpressionAnalyzer(txnCtx, nodeCtx, paramTypeHints, fieldProvider, null);
-        var normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, targetTable);
+        var normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            targetTable,
+            f -> f.signature().isDeterministic());
         Map<Reference, Symbol> updateAssignments = new HashMap<>(duplicateKeyContext.getAssignments().size());
         for (Assignment<Expression> assignment : duplicateKeyContext.getAssignments()) {
             Reference targetCol = (Reference) exprAnalyzer.convert(assignment.columnName(), exprCtx);
diff --git a/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java b/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java
index 10fb9e2fcf..da708dcfca 100644
--- a/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java
@@ -107,7 +107,12 @@ public final class UpdateAnalyzer {
             throw new UnsupportedOperationException("UPDATE is only supported on base-tables");
         }
         AbstractTableRelation<?> table = (AbstractTableRelation<?>) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         SubqueryAnalyzer subqueryAnalyzer =
             new SubqueryAnalyzer(relationAnalyzer, new StatementAnalysisContext(typeHints, Operation.READ, txnCtx));
 
diff --git a/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java b/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java
index 7b306d76d4..731eb7f9f3 100644
--- a/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java
@@ -112,7 +112,11 @@ public class WhereClauseAnalyzer {
         PartitionReferenceResolver partitionReferenceResolver = preparePartitionResolver(
             tableInfo.partitionedByColumns());
         EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
-            nodeCtx, RowGranularity.PARTITION, partitionReferenceResolver, null);
+            nodeCtx,
+            RowGranularity.PARTITION,
+            partitionReferenceResolver,
+            null,
+            f -> f.signature().isDeterministic());
 
         Symbol normalized;
         Map<Symbol, List<Literal<?>>> queryPartitionMap = new HashMap<>();

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/analyze/CopyAnalyzer.java b/server/src/main/java/io/crate/analyze/CopyAnalyzer.java
index 44e8093b31..9dcf9e91d7 100644
--- a/server/src/main/java/io/crate/analyze/CopyAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/CopyAnalyzer.java
@@ -73,7 +73,8 @@ class CopyAnalyzer {
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            new TableRelation(tableInfo));
+            new TableRelation(tableInfo),
+            f -> f.signature().isDeterministic());
 
         Table<Symbol> table = node.table().map(t -> exprAnalyzerWithFieldsAsString.convert(t, exprCtx));
         GenericProperties<Symbol> properties = node.properties().map(t -> exprAnalyzerWithoutFields.convert(t,
@@ -116,7 +117,8 @@ class CopyAnalyzer {
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            tableRelation);
+            tableRelation,
+            f -> f.signature().isDeterministic());
 
         var exprCtx = new ExpressionAnalysisContext(txnCtx.sessionSettings());
         var expressionAnalyzer = new ExpressionAnalyzer(
diff --git a/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java b/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java
index 24dbb8a508..d9a735d4b3 100644
--- a/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java
@@ -60,11 +60,15 @@ final class DeleteAnalyzer {
         MaybeAliasedStatement maybeAliasedStatement = MaybeAliasedStatement.analyze(relation);
         relation = maybeAliasedStatement.nonAliasedRelation();
 
-        if (!(relation instanceof DocTableRelation)) {
+        if (!(relation instanceof DocTableRelation table)) {
             throw new UnsupportedOperationException("Cannot delete from relations other than base tables");
         }
-        DocTableRelation table = (DocTableRelation) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         ExpressionAnalyzer expressionAnalyzer = new ExpressionAnalyzer(
             txnContext,
             nodeCtx,
diff --git a/server/src/main/java/io/crate/analyze/InsertAnalyzer.java b/server/src/main/java/io/crate/analyze/InsertAnalyzer.java
index 652ec1b289..6df8ca414e 100644
--- a/server/src/main/java/io/crate/analyze/InsertAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/InsertAnalyzer.java
@@ -313,7 +313,12 @@ class InsertAnalyzer {
             fieldProvider = new NameFieldProvider(targetTable);
         }
         var expressionAnalyzer = new ExpressionAnalyzer(txnCtx, nodeCtx, paramTypeHints, fieldProvider, null);
-        var normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, targetTable);
+        var normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            targetTable,
+            f -> f.signature().isDeterministic());
         Map<Reference, Symbol> updateAssignments = new HashMap<>(duplicateKeyContext.getAssignments().size());
         for (Assignment<Expression> assignment : duplicateKeyContext.getAssignments()) {
             Reference targetCol = (Reference) exprAnalyzer.convert(assignment.columnName(), exprCtx);
diff --git a/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java b/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java
index 10fb9e2fcf..da708dcfca 100644
--- a/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java
@@ -107,7 +107,12 @@ public final class UpdateAnalyzer {
             throw new UnsupportedOperationException("UPDATE is only supported on base-tables");
         }
         AbstractTableRelation<?> table = (AbstractTableRelation<?>) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         SubqueryAnalyzer subqueryAnalyzer =
             new SubqueryAnalyzer(relationAnalyzer, new StatementAnalysisContext(typeHints, Operation.READ, txnCtx));
 
diff --git a/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java b/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java
index 7b306d76d4..731eb7f9f3 100644
--- a/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java
@@ -112,7 +112,11 @@ public class WhereClauseAnalyzer {
         PartitionReferenceResolver partitionReferenceResolver = preparePartitionResolver(
             tableInfo.partitionedByColumns());
         EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
-            nodeCtx, RowGranularity.PARTITION, partitionReferenceResolver, null);
+            nodeCtx,
+            RowGranularity.PARTITION,
+            partitionReferenceResolver,
+            null,
+            f -> f.signature().isDeterministic());
 
         Symbol normalized;
         Map<Symbol, List<Literal<?>>> queryPartitionMap = new HashMap<>();

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/docs/appendices/release-notes/5.6.5.rst b/docs/appendices/release-notes/5.6.5.rst
index 07d378b634..24b3643ccf 100644
--- a/docs/appendices/release-notes/5.6.5.rst
+++ b/docs/appendices/release-notes/5.6.5.rst
@@ -80,3 +80,6 @@ Fixes
 - Fixed an issue that caused queries on partitioned tables via prepared
   statements to return invalid results if the partitions of the table changed
   after preparing the statements.
+
+- Fixed an issue that caused prepared statements to cache values of
+  non-deterministic functions and use the same value for each execution.
diff --git a/server/src/main/java/io/crate/analyze/CopyAnalyzer.java b/server/src/main/java/io/crate/analyze/CopyAnalyzer.java
index 44e8093b31..9dcf9e91d7 100644
--- a/server/src/main/java/io/crate/analyze/CopyAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/CopyAnalyzer.java
@@ -73,7 +73,8 @@ class CopyAnalyzer {
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            new TableRelation(tableInfo));
+            new TableRelation(tableInfo),
+            f -> f.signature().isDeterministic());
 
         Table<Symbol> table = node.table().map(t -> exprAnalyzerWithFieldsAsString.convert(t, exprCtx));
         GenericProperties<Symbol> properties = node.properties().map(t -> exprAnalyzerWithoutFields.convert(t,
@@ -116,7 +117,8 @@ class CopyAnalyzer {
             nodeCtx,
             RowGranularity.CLUSTER,
             null,
-            tableRelation);
+            tableRelation,
+            f -> f.signature().isDeterministic());
 
         var exprCtx = new ExpressionAnalysisContext(txnCtx.sessionSettings());
         var expressionAnalyzer = new ExpressionAnalyzer(
diff --git a/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java b/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java
index 24dbb8a508..d9a735d4b3 100644
--- a/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/DeleteAnalyzer.java
@@ -60,11 +60,15 @@ final class DeleteAnalyzer {
         MaybeAliasedStatement maybeAliasedStatement = MaybeAliasedStatement.analyze(relation);
         relation = maybeAliasedStatement.nonAliasedRelation();
 
-        if (!(relation instanceof DocTableRelation)) {
+        if (!(relation instanceof DocTableRelation table)) {
             throw new UnsupportedOperationException("Cannot delete from relations other than base tables");
         }
-        DocTableRelation table = (DocTableRelation) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         ExpressionAnalyzer expressionAnalyzer = new ExpressionAnalyzer(
             txnContext,
             nodeCtx,
diff --git a/server/src/main/java/io/crate/analyze/InsertAnalyzer.java b/server/src/main/java/io/crate/analyze/InsertAnalyzer.java
index 652ec1b289..6df8ca414e 100644
--- a/server/src/main/java/io/crate/analyze/InsertAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/InsertAnalyzer.java
@@ -313,7 +313,12 @@ class InsertAnalyzer {
             fieldProvider = new NameFieldProvider(targetTable);
         }
         var expressionAnalyzer = new ExpressionAnalyzer(txnCtx, nodeCtx, paramTypeHints, fieldProvider, null);
-        var normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, targetTable);
+        var normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            targetTable,
+            f -> f.signature().isDeterministic());
         Map<Reference, Symbol> updateAssignments = new HashMap<>(duplicateKeyContext.getAssignments().size());
         for (Assignment<Expression> assignment : duplicateKeyContext.getAssignments()) {
             Reference targetCol = (Reference) exprAnalyzer.convert(assignment.columnName(), exprCtx);
diff --git a/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java b/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java
index 10fb9e2fcf..da708dcfca 100644
--- a/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/UpdateAnalyzer.java
@@ -107,7 +107,12 @@ public final class UpdateAnalyzer {
             throw new UnsupportedOperationException("UPDATE is only supported on base-tables");
         }
         AbstractTableRelation<?> table = (AbstractTableRelation<?>) relation;
-        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(nodeCtx, RowGranularity.CLUSTER, null, table);
+        EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
+            nodeCtx,
+            RowGranularity.CLUSTER,
+            null,
+            table,
+            f -> f.signature().isDeterministic());
         SubqueryAnalyzer subqueryAnalyzer =
             new SubqueryAnalyzer(relationAnalyzer, new StatementAnalysisContext(typeHints, Operation.READ, txnCtx));
 
diff --git a/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java b/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java
index 7b306d76d4..731eb7f9f3 100644
--- a/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java
+++ b/server/src/main/java/io/crate/analyze/where/WhereClauseAnalyzer.java
@@ -112,7 +112,11 @@ public class WhereClauseAnalyzer {
         PartitionReferenceResolver partitionReferenceResolver = preparePartitionResolver(
             tableInfo.partitionedByColumns());
         EvaluatingNormalizer normalizer = new EvaluatingNormalizer(
-            nodeCtx, RowGranularity.PARTITION, partitionReferenceResolver, null);
+            nodeCtx,
+            RowGranularity.PARTITION,
+            partitionReferenceResolver,
+            null,
+            f -> f.signature().isDeterministic());
 
         Symbol normalized;
         Map<Symbol, List<Literal<?>>> queryPartitionMap = new HashMap<>();
diff --git a/server/src/test/java/io/crate/integrationtests/DeleteIntegrationTest.java b/server/src/test/java/io/crate/integrationtests/DeleteIntegrationTest.java
index 86db88e0bd..ed395563a5 100644
--- a/server/src/test/java/io/crate/integrationtests/DeleteIntegrationTest.java
+++ b/server/src/test/java/io/crate/integrationtests/DeleteIntegrationTest.java
@@ -24,9 +24,12 @@ package io.crate.integrationtests;
 
 import static io.crate.testing.Asserts.assertThat;
 
+import java.util.List;
+
 import org.elasticsearch.test.IntegTestCase;
 import org.junit.Test;
 
+import io.crate.action.sql.BaseResultReceiver;
 import io.crate.common.unit.TimeValue;
 import io.crate.execution.dsl.projection.AbstractIndexWriterProjection;
 import io.crate.testing.UseJdbc;
@@ -303,4 +306,31 @@ public class DeleteIntegrationTest extends IntegTestCase {
             "1"
         );
     }
+
+    @Test
+    public void test_can_reuse_prepared_statement_for_delete_containing_non_deterministic_function() throws Exception {
+        execute("CREATE TABLE doc.t (a timestamp with time zone)");
+
+        try (var session = sqlExecutor.newSession()) {
+            session.parse(
+                "preparedStatement",
+                "DELETE FROM doc.t WHERE a < now() - '3 minute'::INTERVAL",
+                List.of()
+            );
+
+            // insert a value that the prepared statement will delete
+            execute("INSERT INTO doc.t SELECT now() - '3 minute'::INTERVAL");
+            refresh();
+
+            // execute the prepared statement to delete the inserted value
+            session.bind("portalName", "preparedStatement", List.of(), null);
+            session.execute("portalName", 0, new BaseResultReceiver());
+            session.sync().get();
+        }
+        refresh();
+
+        // empty rows implies that the now() in the prepared statement is evaluated during execution
+        execute("SELECT * FROM doc.t");
+        assertThat(response).isEmpty();
+    }
 }

```
