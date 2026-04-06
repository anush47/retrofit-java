# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java']
- Developer Java files: ['server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java']
- Overlap Java files: ['server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java

- Developer hunks: 4
- Generated hunks: 4

#### Hunk 1

Developer
```diff
@@ -54,7 +54,7 @@
                                 TypeSignature.parse("T"))
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
 

```

Generated
```diff
@@ -54,7 +54,7 @@
                                 TypeSignature.parse("T"))
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -65,15 +65,15 @@
                                 DataTypes.INTEGER.getTypeSignature())
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
     }
 
     @Override
-    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input[] args) {
+    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input<List<Object>>[] args) {
 
-        List<Object> elements = (List<Object>) args[0].value();
+        List<Object> elements = args[0].value();
         if (elements == null || elements.isEmpty()) {
             return null;
         }

```

Generated
```diff
@@ -65,15 +65,15 @@
                                 DataTypes.INTEGER.getTypeSignature())
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
     }
 
     @Override
-    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input[] args) {
+    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input<List<Object>>[] args) {
 
-        List<Object> elements = (List<Object>) args[0].value();
+        List<Object> elements = args[0].value();
         if (elements == null || elements.isEmpty()) {
             return null;
         }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 3

Developer
```diff
@@ -90,7 +90,7 @@
             return null;
         }
 
-        Object element = null;
+        Object element;
         for (int i = beginIndex; i < elements.size(); i++) {
             element = elements.get(i);
             if (Objects.equals(targetValue, element)) {

```

Generated
```diff
@@ -90,7 +90,7 @@
             return null;
         }
 
-        Object element = null;
+        Object element;
         for (int i = beginIndex; i < elements.size(); i++) {
             element = elements.get(i);
             if (Objects.equals(targetValue, element)) {

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 4

Developer
```diff
@@ -107,7 +107,7 @@
             return 0;
         }
 
-        Integer beginPosition = (Integer) position;
+        int beginPosition = (Integer) position;
         if (beginPosition < 1 || beginPosition > elementsSize) {
             return null;
         }

```

Generated
```diff
@@ -107,7 +107,7 @@
             return 0;
         }
 
-        Integer beginPosition = (Integer) position;
+        int beginPosition = (Integer) position;
         if (beginPosition < 1 || beginPosition > elementsSize) {
             return null;
         }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java b/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java
index 1e8dbafdfc..b978f5d419 100644
--- a/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java
+++ b/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java
@@ -54,7 +54,7 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
                                 TypeSignature.parse("T"))
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
 
@@ -65,15 +65,15 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
                                 DataTypes.INTEGER.getTypeSignature())
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
     }
 
     @Override
-    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input[] args) {
+    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input<List<Object>>[] args) {
 
-        List<Object> elements = (List<Object>) args[0].value();
+        List<Object> elements = args[0].value();
         if (elements == null || elements.isEmpty()) {
             return null;
         }
@@ -90,7 +90,7 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
             return null;
         }
 
-        Object element = null;
+        Object element;
         for (int i = beginIndex; i < elements.size(); i++) {
             element = elements.get(i);
             if (Objects.equals(targetValue, element)) {
@@ -107,7 +107,7 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
             return 0;
         }
 
-        Integer beginPosition = (Integer) position;
+        int beginPosition = (Integer) position;
         if (beginPosition < 1 || beginPosition > elementsSize) {
             return null;
         }

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java b/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java
index 1e8dbafdfc..b978f5d419 100644
--- a/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java
+++ b/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java
@@ -54,7 +54,7 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
                                 TypeSignature.parse("T"))
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
 
@@ -65,15 +65,15 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
                                 DataTypes.INTEGER.getTypeSignature())
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
     }
 
     @Override
-    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input[] args) {
+    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input<List<Object>>[] args) {
 
-        List<Object> elements = (List<Object>) args[0].value();
+        List<Object> elements = args[0].value();
         if (elements == null || elements.isEmpty()) {
             return null;
         }
@@ -90,7 +90,7 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
             return null;
         }
 
-        Object element = null;
+        Object element;
         for (int i = beginIndex; i < elements.size(); i++) {
             element = elements.get(i);
             if (Objects.equals(targetValue, element)) {
@@ -107,7 +107,7 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
             return 0;
         }
 
-        Integer beginPosition = (Integer) position;
+        int beginPosition = (Integer) position;
         if (beginPosition < 1 || beginPosition > elementsSize) {
             return null;
         }

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/docs/appendices/release-notes/5.9.10.rst b/docs/appendices/release-notes/5.9.10.rst
index f20fc79c5c..b563a636ae 100644
--- a/docs/appendices/release-notes/5.9.10.rst
+++ b/docs/appendices/release-notes/5.9.10.rst
@@ -98,3 +98,9 @@ Fixes
   :ref:`information_schema_key_column_usage` and ``pg_class`` tables,
   ``<table_name>_pk`` and ``<table_name>_pkey`` respectively, when a custom
   name is not explicitly provided during table creation.
+
+- Fixed an issue that would cause :ref:`array_position<scalar-array_position>`
+  to return wrong results when used on a column with NULL values in the
+  ``WHERE`` combined with a ``NOT`` predicate. e.g.::
+
+    SELECT * FROM tbl WHERE NOT array_position(string_array_col, 'foo');
diff --git a/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java b/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java
index 1e8dbafdfc..b978f5d419 100644
--- a/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java
+++ b/server/src/main/java/io/crate/expression/scalar/ArrayPositionFunction.java
@@ -54,7 +54,7 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
                                 TypeSignature.parse("T"))
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
 
@@ -65,15 +65,15 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
                                 DataTypes.INTEGER.getTypeSignature())
                         .returnType(DataTypes.INTEGER.getTypeSignature())
                         .typeVariableConstraints(typeVariable("T"))
-                        .features(Feature.DETERMINISTIC, Feature.STRICTNULL)
+                        .features(Feature.DETERMINISTIC)
                         .build(),
                 ArrayPositionFunction::new);
     }
 
     @Override
-    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input[] args) {
+    public Integer evaluate(TransactionContext txnCtx, NodeContext nodeContext, Input<List<Object>>[] args) {
 
-        List<Object> elements = (List<Object>) args[0].value();
+        List<Object> elements = args[0].value();
         if (elements == null || elements.isEmpty()) {
             return null;
         }
@@ -90,7 +90,7 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
             return null;
         }
 
-        Object element = null;
+        Object element;
         for (int i = beginIndex; i < elements.size(); i++) {
             element = elements.get(i);
             if (Objects.equals(targetValue, element)) {
@@ -107,7 +107,7 @@ public class ArrayPositionFunction extends Scalar<Integer, List<Object>> {
             return 0;
         }
 
-        Integer beginPosition = (Integer) position;
+        int beginPosition = (Integer) position;
         if (beginPosition < 1 || beginPosition > elementsSize) {
             return null;
         }
diff --git a/server/src/test/java/io/crate/lucene/ThreeValuedLogicQueryBuilderTest.java b/server/src/test/java/io/crate/lucene/ThreeValuedLogicQueryBuilderTest.java
index 23484a7bdb..aa81411885 100644
--- a/server/src/test/java/io/crate/lucene/ThreeValuedLogicQueryBuilderTest.java
+++ b/server/src/test/java/io/crate/lucene/ThreeValuedLogicQueryBuilderTest.java
@@ -141,4 +141,12 @@ public class ThreeValuedLogicQueryBuilderTest extends LuceneQueryBuilderTest {
         assertThat(convert("NOT (cast(obj as string))")).hasToString(
             "+(+*:* -cast(obj AS TEXT)) #(NOT cast(obj AS TEXT))");
     }
+
+    @Test
+    public void test_not_on_array_position() {
+        assertThat(convert("NOT (array_position(string_array, 'foo'))")).hasToString(
+            "+(+*:* -array_position(string_array, 'foo')) #(NOT array_position(string_array, 'foo'))");
+        assertThat(convert("NOT (array_position(string_array, 'foo', 10))")).hasToString(
+            "+(+*:* -array_position(string_array, 'foo', 10)) #(NOT array_position(string_array, 'foo', 10))");
+    }
 }

```
