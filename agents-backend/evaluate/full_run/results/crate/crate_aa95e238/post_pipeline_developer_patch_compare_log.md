# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/expression/InputFactory.java']
- Developer Java files: ['server/src/main/java/io/crate/expression/InputFactory.java']
- Overlap Java files: ['server/src/main/java/io/crate/expression/InputFactory.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/expression/InputFactory.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/expression/InputFactory.java']
- Mismatched files: ['server/src/main/java/io/crate/expression/InputFactory.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/expression/InputFactory.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -45,6 +45,7 @@
 import io.crate.metadata.FunctionImplementation;
 import io.crate.metadata.NodeContext;
 import io.crate.metadata.Reference;
+import io.crate.metadata.Schemas;
 import io.crate.metadata.TransactionContext;
 
 /**

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -45,6 +45,7 @@
- import io.crate.metadata.FunctionImplementation;
- import io.crate.metadata.NodeContext;
- import io.crate.metadata.Reference;
-+import io.crate.metadata.Schemas;
- import io.crate.metadata.TransactionContext;
- 
- /**
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -238,7 +239,12 @@
             }
             implementation = referenceResolver.getImplementation(ref);
             if (implementation == null) {
-                throw new IllegalArgumentException("Column implementation not found for: " + ref);
+                String schema = ref.ident().tableIdent().schema();
+                String msg = Schemas.READ_ONLY_SYSTEM_SCHEMAS.contains(schema)
+                    ? "Column implementation not found for: " + ref + ". This can happen in mixed clusters when using " +
+                        "`SELECT *`; Declare the column list explicitly instead"
+                    : "Column implementation not found for: " + ref;
+                throw new IllegalArgumentException(msg);
             }
             referenceMap.put(ref, implementation);
             return implementation;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,14 +1 @@-@@ -238,7 +239,12 @@
-             }
-             implementation = referenceResolver.getImplementation(ref);
-             if (implementation == null) {
--                throw new IllegalArgumentException("Column implementation not found for: " + ref);
-+                String schema = ref.ident().tableIdent().schema();
-+                String msg = Schemas.READ_ONLY_SYSTEM_SCHEMAS.contains(schema)
-+                    ? "Column implementation not found for: " + ref + ". This can happen in mixed clusters when using " +
-+                        "`SELECT *`; Declare the column list explicitly instead"
-+                    : "Column implementation not found for: " + ref;
-+                throw new IllegalArgumentException(msg);
-             }
-             referenceMap.put(ref, implementation);
-             return implementation;
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
diff --git a/docs/admin/system-information.rst b/docs/admin/system-information.rst
index 53a4e5125b..cf198f12f0 100644
--- a/docs/admin/system-information.rst
+++ b/docs/admin/system-information.rst
@@ -7,7 +7,15 @@ System information
 
 CrateDB provides the ``sys`` schema which contains virtual tables. These tables
 are read-only and can be queried to get statistical real-time information about
-the cluster, its nodes and their shards:
+the cluster, its nodes and their shards.
+
+.. NOTE::
+
+    During a rolling upgrade of the cluster to a newer version, while the
+    cluster is in a mixed state with nodes on the older and on the new version,
+    avoid querying the ``sys`` tables using ``SELECT *``, as new columns could
+    have been added, removed or modified between versions. Instead, use a
+    defined list of the columns that you need to return from the query.
 
 .. rubric:: Table of contents
 
diff --git a/docs/appendices/release-notes/5.10.7.rst b/docs/appendices/release-notes/5.10.7.rst
index abcd4c8781..5c03861e05 100644
--- a/docs/appendices/release-notes/5.10.7.rst
+++ b/docs/appendices/release-notes/5.10.7.rst
@@ -47,6 +47,11 @@ See the :ref:`version_5.10.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- Improved error message thrown when using a ``SELECT *``` on
+  :ref:`system tables <system-information>`, during a rolling upgrade, when
+  columns on the ``sys`` table queried differ between the old and the new
+  cluster nodes.
+
 - Fixed an issue that would cause wrong column data type to be used when adding
   parent and child object sub-columns in one
   :ref:`ALTER TABLE <alter-table-add-column>` statement, e.g.::
diff --git a/docs/general/information-schema.rst b/docs/general/information-schema.rst
index 92e2c81d9c..07e9f4e353 100644
--- a/docs/general/information-schema.rst
+++ b/docs/general/information-schema.rst
@@ -31,6 +31,14 @@ but no privilege at all on ``doc.locations``, when ``john`` issues a ``SELECT *
 FROM information_schema.tables`` statement, the tables information related to
 the ``doc.locations`` table will not be returned.
 
+.. NOTE::
+
+    During a rolling upgrade of the cluster to a newer version, while the
+    cluster is in a mixed state with nodes on the older and on the new version,
+    avoid querying the ``sys`` tables using ``SELECT *``, as new columns could
+    have been added, removed or modified between versions. Instead, use a
+    defined list of the columns that you need to return from the query.
+
 Virtual tables
 ==============
 
diff --git a/server/src/main/java/io/crate/expression/InputFactory.java b/server/src/main/java/io/crate/expression/InputFactory.java
index 09b3b6e4cd..cd1acb0670 100644
--- a/server/src/main/java/io/crate/expression/InputFactory.java
+++ b/server/src/main/java/io/crate/expression/InputFactory.java
@@ -45,6 +45,7 @@ import io.crate.expression.symbol.SymbolVisitor;
 import io.crate.metadata.FunctionImplementation;
 import io.crate.metadata.NodeContext;
 import io.crate.metadata.Reference;
+import io.crate.metadata.Schemas;
 import io.crate.metadata.TransactionContext;
 
 /**
@@ -238,7 +239,12 @@ public class InputFactory {
             }
             implementation = referenceResolver.getImplementation(ref);
             if (implementation == null) {
-                throw new IllegalArgumentException("Column implementation not found for: " + ref);
+                String schema = ref.ident().tableIdent().schema();
+                String msg = Schemas.READ_ONLY_SYSTEM_SCHEMAS.contains(schema)
+                    ? "Column implementation not found for: " + ref + ". This can happen in mixed clusters when using " +
+                        "`SELECT *`; Declare the column list explicitly instead"
+                    : "Column implementation not found for: " + ref;
+                throw new IllegalArgumentException(msg);
             }
             referenceMap.put(ref, implementation);
             return implementation;
diff --git a/server/src/test/java/io/crate/expression/InputFactoryTest.java b/server/src/test/java/io/crate/expression/InputFactoryTest.java
index 0990fdd0ed..9ba921eb45 100644
--- a/server/src/test/java/io/crate/expression/InputFactoryTest.java
+++ b/server/src/test/java/io/crate/expression/InputFactoryTest.java
@@ -21,7 +21,9 @@
 
 package io.crate.expression;
 
+import static io.crate.testing.TestingHelpers.refInfo;
 import static org.assertj.core.api.Assertions.assertThat;
+import static org.assertj.core.api.Assertions.assertThatThrownBy;
 
 import java.util.ArrayList;
 import java.util.Arrays;
@@ -47,7 +49,9 @@ import io.crate.expression.symbol.Symbol;
 import io.crate.metadata.CoordinatorTxnCtx;
 import io.crate.metadata.FunctionImplementation;
 import io.crate.metadata.FunctionType;
+import io.crate.metadata.Reference;
 import io.crate.metadata.RelationName;
+import io.crate.metadata.RowGranularity;
 import io.crate.metadata.Scalar;
 import io.crate.metadata.Scalar.Feature;
 import io.crate.metadata.TransactionContext;
@@ -184,10 +188,10 @@ public class InputFactoryTest extends CrateDummyClusterServiceUnitTest {
     @Test
     public void testCompiled() throws Exception {
         Function function = (Function) expressions.normalize(expressions.asSymbol("a like 'f%'"));
-        InputFactory.Context<Input<?>> ctx = factory.ctxForRefs(txnCtx, i -> Literal.of("foo"));
+        InputFactory.Context<Input<?>> ctx = factory.ctxForRefs(txnCtx, _ -> Literal.of("foo"));
         Input<?> input = ctx.add(function);
 
-        FunctionExpression expression = (FunctionExpression) input;
+        FunctionExpression<?, ?> expression = (FunctionExpression<?, ?>) input;
         java.lang.reflect.Field f = FunctionExpression.class.getDeclaredField("scalar");
         f.setAccessible(true);
         FunctionImplementation impl = (FunctionImplementation) f.get(expression);
@@ -206,4 +210,19 @@ public class InputFactoryTest extends CrateDummyClusterServiceUnitTest {
 
         assertThat(input1).isSameAs(input2);
     }
+
+    @Test
+    public void test_missing_reference() throws Exception {
+        InputFactory.Context<Input<?>> ctx = factory.ctxForRefs(txnCtx, _ -> null);
+
+        Reference refInfo = refInfo("doc.tbl.id", DataTypes.INTEGER, RowGranularity.SHARD);
+        assertThatThrownBy(() -> ctx.add(refInfo))
+            .isExactlyInstanceOf(IllegalArgumentException.class)
+            .hasMessage("Column implementation not found for: id");
+
+        Reference sysRefInfo = refInfo("sys.shards.id", DataTypes.INTEGER, RowGranularity.SHARD);
+        assertThatThrownBy(() -> ctx.add(sysRefInfo))
+            .isExactlyInstanceOf(IllegalArgumentException.class)
+            .hasMessage("Column implementation not found for: id. This can happen in mixed clusters when using `SELECT *`; Declare the column list explicitly instead");
+    }
 }

```
