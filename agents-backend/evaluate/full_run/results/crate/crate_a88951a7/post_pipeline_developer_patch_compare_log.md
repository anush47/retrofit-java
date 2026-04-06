# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java']
- Developer Java files: ['extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java']
- Overlap Java files: ['extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java']

## File State Comparison
- Compared files: ['extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java']
- Mismatched files: ['extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java', 'server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java

- Developer hunks: 6
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -172,9 +172,17 @@
                                                        List<Reference> aggregationReferences,
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
-        if (aggregationReferences.stream().anyMatch(x -> !x.hasDocValues())) {
+        if (aggregationReferences.stream().anyMatch(x -> x != null && !x.hasDocValues())) {
             return null;
         }
+
+        final int precision;
+        if (optionalParams.isEmpty()) {
+            precision = HyperLogLogPlusPlus.DEFAULT_PRECISION;
+        } else {
+            Literal<?> value = optionalParams.getLast();
+            precision = value == null ? HyperLogLogPlusPlus.DEFAULT_PRECISION : (int) value.value();
+        }
         Reference reference = aggregationReferences.get(0);
         var dataType = reference.valueType();
         switch (dataType.id()) {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,19 +1 @@-@@ -172,9 +172,17 @@
-                                                        List<Reference> aggregationReferences,
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
--        if (aggregationReferences.stream().anyMatch(x -> !x.hasDocValues())) {
-+        if (aggregationReferences.stream().anyMatch(x -> x != null && !x.hasDocValues())) {
-             return null;
-         }
-+
-+        final int precision;
-+        if (optionalParams.isEmpty()) {
-+            precision = HyperLogLogPlusPlus.DEFAULT_PRECISION;
-+        } else {
-+            Literal<?> value = optionalParams.getLast();
-+            precision = value == null ? HyperLogLogPlusPlus.DEFAULT_PRECISION : (int) value.value();
-+        }
-         Reference reference = aggregationReferences.get(0);
-         var dataType = reference.valueType();
-         switch (dataType.id()) {
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -188,7 +196,6 @@
                     reference.storageIdent(),
                     (ramAccounting, memoryManager, minNodeVersion) -> {
                         var state = new HllState(dataType, minNodeVersion.onOrAfter(Version.V_4_1_0));
-                        var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
                         return initIfNeeded(state, memoryManager, precision);
                     },
                     (values, state) -> {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -188,7 +196,6 @@
-                     reference.storageIdent(),
-                     (ramAccounting, memoryManager, minNodeVersion) -> {
-                         var state = new HllState(dataType, minNodeVersion.onOrAfter(Version.V_4_1_0));
--                        var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
-                         return initIfNeeded(state, memoryManager, precision);
-                     },
-                     (values, state) -> {
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -201,7 +208,6 @@
                     reference.storageIdent(),
                     (ramAccounting, memoryManager, minNodeVersion) -> {
                         var state = new HllState(dataType, minNodeVersion.onOrAfter(Version.V_4_1_0));
-                        var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
                         return initIfNeeded(state, memoryManager, precision);
                     },
                     (values, state) -> {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -201,7 +208,6 @@
-                     reference.storageIdent(),
-                     (ramAccounting, memoryManager, minNodeVersion) -> {
-                         var state = new HllState(dataType, minNodeVersion.onOrAfter(Version.V_4_1_0));
--                        var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
-                         return initIfNeeded(state, memoryManager, precision);
-                     },
-                     (values, state) -> {
+*No hunk*
```

#### Hunk 4

Developer
```diff
@@ -220,7 +226,6 @@
                     reference.storageIdent(),
                     (ramAccounting, memoryManager, minNodeVersion) -> {
                         var state = new HllState(dataType, minNodeVersion.onOrAfter(Version.V_4_1_0));
-                        var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
                         return initIfNeeded(state, memoryManager, precision);
                     },
                     (values, state) -> {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -220,7 +226,6 @@
-                     reference.storageIdent(),
-                     (ramAccounting, memoryManager, minNodeVersion) -> {
-                         var state = new HllState(dataType, minNodeVersion.onOrAfter(Version.V_4_1_0));
--                        var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
-                         return initIfNeeded(state, memoryManager, precision);
-                     },
-                     (values, state) -> {
+*No hunk*
```

#### Hunk 5

Developer
```diff
@@ -235,7 +240,6 @@
                 );
             case StringType.ID:
             case CharacterType.ID:
-                var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
                 return new HllAggregator(reference.storageIdent(), dataType, precision) {
                     @Override
                     public void apply(RamAccounting ramAccounting, int doc, HllState state) throws IOException {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -235,7 +240,6 @@
-                 );
-             case StringType.ID:
-             case CharacterType.ID:
--                var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
-                 return new HllAggregator(reference.storageIdent(), dataType, precision) {
-                     @Override
-                     public void apply(RamAccounting ramAccounting, int doc, HllState state) throws IOException {
+*No hunk*
```

#### Hunk 6

Developer
```diff
@@ -250,8 +254,7 @@
                     }
                 };
             case IpType.ID:
-                var ipPrecision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
-                return new HllAggregator(reference.storageIdent(), dataType, ipPrecision) {
+                return new HllAggregator(reference.storageIdent(), dataType, precision) {
                     @Override
                     public void apply(RamAccounting ramAccounting, int doc, HllState state) throws IOException {
                         if (super.values.advanceExact(doc) && super.values.docValueCount() == 1) {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -250,8 +254,7 @@
-                     }
-                 };
-             case IpType.ID:
--                var ipPrecision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
--                return new HllAggregator(reference.storageIdent(), dataType, ipPrecision) {
-+                return new HllAggregator(reference.storageIdent(), dataType, precision) {
-                     @Override
-                     public void apply(RamAccounting ramAccounting, int doc, HllState state) throws IOException {
-                         if (super.values.advanceExact(doc) && super.values.docValueCount() == 1) {
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -117,6 +117,17 @@
                                                 "not removable cumulative");
     }
 
+    /**
+     * @param referenceResolver A LuceneReferenceResolver to resolve references.
+     * @param aggregationReferences contains a list of references of the size of the input values of the function.
+     *                              If the value at the position is not a reference in the inputs the value in
+     *                              the list is null.
+     * @param table DocTableInfo for the underlying table which is the source of the doc-values.
+     * @param optionalParams contains a list of literals of the size of the input values of the function.
+     *                       If the value at the position is not a literal in the inputs the value in the list is
+     *                       null.
+     * @return A DocValueAggregator or null if there is no doc-value support for the given input parameters.
+     */
     @Nullable
     public DocValueAggregator<?> getDocValueAggregator(LuceneReferenceResolver referenceResolver,
                                                        List<Reference> aggregationReferences,

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,18 +1 @@-@@ -117,6 +117,17 @@
-                                                 "not removable cumulative");
-     }
- 
-+    /**
-+     * @param referenceResolver A LuceneReferenceResolver to resolve references.
-+     * @param aggregationReferences contains a list of references of the size of the input values of the function.
-+     *                              If the value at the position is not a reference in the inputs the value in
-+     *                              the list is null.
-+     * @param table DocTableInfo for the underlying table which is the source of the doc-values.
-+     * @param optionalParams contains a list of literals of the size of the input values of the function.
-+     *                       If the value at the position is not a literal in the inputs the value in the list is
-+     *                       null.
-+     * @return A DocValueAggregator or null if there is no doc-value support for the given input parameters.
-+     */
-     @Nullable
-     public DocValueAggregator<?> getDocValueAggregator(LuceneReferenceResolver referenceResolver,
-                                                        List<Reference> aggregationReferences,
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -156,6 +156,9 @@
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference arg = aggregationReferences.get(0);
+        if (arg == null) {
+            return null;
+        }
         if (!arg.hasDocValues()) {
             return null;
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -156,6 +156,9 @@
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
-         Reference arg = aggregationReferences.get(0);
-+        if (arg == null) {
-+            return null;
-+        }
-         if (!arg.hasDocValues()) {
-             return null;
-         }
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -160,11 +160,19 @@
                                                        List<Reference> aggregationReferences,
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
-        Reference searchRef = aggregationReferences.get(1);
-        if (!searchRef.hasDocValues()) {
+        Reference returnField = aggregationReferences.getFirst();
+        Reference searchField = aggregationReferences.getLast();
+        if (returnField == null) {
             return null;
         }
-        DataType<?> searchType = searchRef.valueType();
+        if (searchField == null) {
+            return null;
+        }
+        if (!searchField.hasDocValues()) {
+            return null;
+        }
+
+        DataType<?> searchType = searchField.valueType();
         switch (searchType.id()) {
             case ByteType.ID:
             case ShortType.ID:

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,23 +1 @@-@@ -160,11 +160,19 @@
-                                                        List<Reference> aggregationReferences,
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
--        Reference searchRef = aggregationReferences.get(1);
--        if (!searchRef.hasDocValues()) {
-+        Reference returnField = aggregationReferences.getFirst();
-+        Reference searchField = aggregationReferences.getLast();
-+        if (returnField == null) {
-             return null;
-         }
--        DataType<?> searchType = searchRef.valueType();
-+        if (searchField == null) {
-+            return null;
-+        }
-+        if (!searchField.hasDocValues()) {
-+            return null;
-+        }
-+
-+        DataType<?> searchType = searchField.valueType();
-         switch (searchType.id()) {
-             case ByteType.ID:
-             case ShortType.ID:
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -172,17 +180,17 @@
             case LongType.ID:
             case TimestampType.ID_WITH_TZ:
             case TimestampType.ID_WITHOUT_TZ:
-                var resultExpression = referenceResolver.getImplementation(aggregationReferences.get(0));
+                var resultExpression = referenceResolver.getImplementation(returnField);
                 if (signature.getName().name().equalsIgnoreCase("min_by")) {
                     return new MinByLong(
-                        searchRef.storageIdent(),
+                        searchField.storageIdent(),
                         searchType,
                         resultExpression,
                         new CollectorContext(table.droppedColumns(), table.lookupNameBySourceKey())
                     );
                 } else {
                     return new MaxByLong(
-                        searchRef.storageIdent(),
+                        searchField.storageIdent(),
                         searchType,
                         resultExpression,
                         new CollectorContext(table.droppedColumns(), table.lookupNameBySourceKey())

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,21 +1 @@-@@ -172,17 +180,17 @@
-             case LongType.ID:
-             case TimestampType.ID_WITH_TZ:
-             case TimestampType.ID_WITHOUT_TZ:
--                var resultExpression = referenceResolver.getImplementation(aggregationReferences.get(0));
-+                var resultExpression = referenceResolver.getImplementation(returnField);
-                 if (signature.getName().name().equalsIgnoreCase("min_by")) {
-                     return new MinByLong(
--                        searchRef.storageIdent(),
-+                        searchField.storageIdent(),
-                         searchType,
-                         resultExpression,
-                         new CollectorContext(table.droppedColumns(), table.lookupNameBySourceKey())
-                     );
-                 } else {
-                     return new MaxByLong(
--                        searchRef.storageIdent(),
-+                        searchField.storageIdent(),
-                         searchType,
-                         resultExpression,
-                         new CollectorContext(table.droppedColumns(), table.lookupNameBySourceKey())
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -300,6 +300,9 @@
             return null;
         }
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (reference.valueType().id() == ObjectType.ID) {
             // Count on object would require loading the source just to check if there is a value.
             // Try to count on a non-null sub-column to be able to utilize doc-values.

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -300,6 +300,9 @@
-             return null;
-         }
-         Reference reference = aggregationReferences.get(0);
-+        if (reference == null) {
-+            return null;
-+        }
-         if (reference.valueType().id() == ObjectType.ID) {
-             // Count on object would require loading the source just to check if there is a value.
-             // Try to count on a non-null sub-column to be able to utilize doc-values.
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -307,6 +307,9 @@
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -307,6 +307,9 @@
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
-         Reference reference = aggregationReferences.get(0);
-+        if (reference == null) {
-+            return null;
-+        }
-         if (!reference.hasDocValues()) {
-             return null;
-         }
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -221,6 +221,11 @@
                                                            DocTableInfo table,
                                                            List<Literal<?>> optionalParams) {
             Reference reference = aggregationReferences.get(0);
+
+            if (reference == null) {
+                return null;
+            }
+
             if (!reference.hasDocValues()) {
                 return null;
             }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,12 +1 @@-@@ -221,6 +221,11 @@
-                                                            DocTableInfo table,
-                                                            List<Literal<?>> optionalParams) {
-             Reference reference = aggregationReferences.get(0);
-+
-+            if (reference == null) {
-+                return null;
-+            }
-+
-             if (!reference.hasDocValues()) {
-                 return null;
-             }
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -255,6 +255,9 @@
                                                            DocTableInfo table,
                                                            List<Literal<?>> optionalParams) {
             Reference reference = aggregationReferences.get(0);
+            if (reference == null) {
+                return null;
+            }
             if (!reference.hasDocValues()) {
                 return null;
             }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -255,6 +255,9 @@
-                                                            DocTableInfo table,
-                                                            List<Literal<?>> optionalParams) {
-             Reference reference = aggregationReferences.get(0);
-+            if (reference == null) {
-+                return null;
-+            }
-             if (!reference.hasDocValues()) {
-                 return null;
-             }
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -182,6 +182,9 @@
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -182,6 +182,9 @@
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
-         Reference reference = aggregationReferences.get(0);
-+        if (reference == null) {
-+            return null;
-+        }
-         if (!reference.hasDocValues()) {
-             return null;
-         }
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -229,6 +229,9 @@
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -229,6 +229,9 @@
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
-         Reference reference = aggregationReferences.get(0);
-+        if (reference == null) {
-+            return null;
-+        }
-         if (!reference.hasDocValues()) {
-             return null;
-         }
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -195,9 +195,15 @@
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+
+        if (reference == null) {
+            return null;
+        }
+
         if (!reference.hasDocValues()) {
             return null;
         }
+
         switch (reference.valueType().id()) {
             case ByteType.ID:
             case ShortType.ID:

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,16 +1 @@-@@ -195,9 +195,15 @@
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
-         Reference reference = aggregationReferences.get(0);
-+
-+        if (reference == null) {
-+            return null;
-+        }
-+
-         if (!reference.hasDocValues()) {
-             return null;
-         }
-+
-         switch (reference.valueType().id()) {
-             case ByteType.ID:
-             case ShortType.ID:
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -229,6 +229,9 @@
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -229,6 +229,9 @@
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
-         Reference reference = aggregationReferences.get(0);
-+        if (reference == null) {
-+            return null;
-+        }
-         if (!reference.hasDocValues()) {
-             return null;
-         }
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -311,6 +311,9 @@
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -311,6 +311,9 @@
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
-         Reference reference = aggregationReferences.get(0);
-+        if (reference == null) {
-+            return null;
-+        }
-         if (!reference.hasDocValues()) {
-             return null;
-         }
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -197,6 +197,9 @@
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,10 +1 @@-@@ -197,6 +197,9 @@
-                                                        DocTableInfo table,
-                                                        List<Literal<?>> optionalParams) {
-         Reference reference = aggregationReferences.get(0);
-+        if (reference == null) {
-+            return null;
-+        }
-         if (!reference.hasDocValues()) {
-             return null;
-         }
+*No hunk*
```


### server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java

- Developer hunks: 2
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -154,6 +154,7 @@
             for (var input : aggregation.inputs()) {
                 if (input instanceof Literal<?> literal) {
                     literals.add(literal);
+                    aggregationReferences.add(null);
                 } else {
                     var reference = input.accept(AggregationInputToReferenceResolver.INSTANCE, toCollect);
                     if (reference == null) {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -154,6 +154,7 @@
-             for (var input : aggregation.inputs()) {
-                 if (input instanceof Literal<?> literal) {
-                     literals.add(literal);
-+                    aggregationReferences.add(null);
-                 } else {
-                     var reference = input.accept(AggregationInputToReferenceResolver.INSTANCE, toCollect);
-                     if (reference == null) {
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -164,6 +165,7 @@
                     assert reference.ident().columnIdent().fqn().startsWith(DocSysColumns.Names.DOC) == false :
                         "Source look-up for Reference " + reference + " is not allowed in DocValuesAggregates.";
                     aggregationReferences.add(reference);
+                    literals.add(null);
                 }
             }
             FunctionImplementation func = functions.getQualified(aggregation);

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -164,6 +165,7 @@
-                     assert reference.ident().columnIdent().fqn().startsWith(DocSysColumns.Names.DOC) == false :
-                         "Source look-up for Reference " + reference + " is not allowed in DocValuesAggregates.";
-                     aggregationReferences.add(reference);
-+                    literals.add(null);
-                 }
-             }
-             FunctionImplementation func = functions.getQualified(aggregation);
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
diff --git a/docs/appendices/release-notes/5.7.4.rst b/docs/appendices/release-notes/5.7.4.rst
index 21a898905e..4429ac0d4b 100644
--- a/docs/appendices/release-notes/5.7.4.rst
+++ b/docs/appendices/release-notes/5.7.4.rst
@@ -48,6 +48,12 @@ See the :ref:`version_5.7.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- Fixed an issue that caused an ``IndexOutOfBoundsException`` when the
+  :ref:`max_by <aggregation-max_by>` aggregation was called with a literal
+  as searchfield parameter instead of a column e.g.::
+
+    SELECT MAX_BY(x, 1) from tbl;
+
 - Fixed an issue that caused write operations to fail if the table contained
   generated columns with a cast to ``geo_shape``.
 
diff --git a/docs/appendices/release-notes/5.8.1.rst b/docs/appendices/release-notes/5.8.1.rst
index 24db6836dc..6360ccc1db 100644
--- a/docs/appendices/release-notes/5.8.1.rst
+++ b/docs/appendices/release-notes/5.8.1.rst
@@ -47,6 +47,12 @@ See the :ref:`version_5.8.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- Fixed an issue that caused an ``IndexOutOfBoundsException`` when the
+  :ref:`max_by <aggregation-max_by>` aggregation was called with a literal
+  as searchfield parameter instead of a column e.g.::
+
+    SELECT MAX_BY(x, 1) from tbl;
+
 - Fixed an issue that caused write operations to fail if the table contained
   generated columns with a cast to ``geo_shape``.
 
diff --git a/extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java b/extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java
index 7ba72e8638..bf83272c3d 100644
--- a/extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java
+++ b/extensions/functions/src/main/java/io/crate/operation/aggregation/HyperLogLogDistinctAggregation.java
@@ -172,9 +172,17 @@ public class HyperLogLogDistinctAggregation extends AggregationFunction<HyperLog
                                                        List<Reference> aggregationReferences,
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
-        if (aggregationReferences.stream().anyMatch(x -> !x.hasDocValues())) {
+        if (aggregationReferences.stream().anyMatch(x -> x != null && !x.hasDocValues())) {
             return null;
         }
+
+        final int precision;
+        if (optionalParams.isEmpty()) {
+            precision = HyperLogLogPlusPlus.DEFAULT_PRECISION;
+        } else {
+            Literal<?> value = optionalParams.getLast();
+            precision = value == null ? HyperLogLogPlusPlus.DEFAULT_PRECISION : (int) value.value();
+        }
         Reference reference = aggregationReferences.get(0);
         var dataType = reference.valueType();
         switch (dataType.id()) {
@@ -188,7 +196,6 @@ public class HyperLogLogDistinctAggregation extends AggregationFunction<HyperLog
                     reference.storageIdent(),
                     (ramAccounting, memoryManager, minNodeVersion) -> {
                         var state = new HllState(dataType, minNodeVersion.onOrAfter(Version.V_4_1_0));
-                        var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
                         return initIfNeeded(state, memoryManager, precision);
                     },
                     (values, state) -> {
@@ -201,7 +208,6 @@ public class HyperLogLogDistinctAggregation extends AggregationFunction<HyperLog
                     reference.storageIdent(),
                     (ramAccounting, memoryManager, minNodeVersion) -> {
                         var state = new HllState(dataType, minNodeVersion.onOrAfter(Version.V_4_1_0));
-                        var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
                         return initIfNeeded(state, memoryManager, precision);
                     },
                     (values, state) -> {
@@ -220,7 +226,6 @@ public class HyperLogLogDistinctAggregation extends AggregationFunction<HyperLog
                     reference.storageIdent(),
                     (ramAccounting, memoryManager, minNodeVersion) -> {
                         var state = new HllState(dataType, minNodeVersion.onOrAfter(Version.V_4_1_0));
-                        var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
                         return initIfNeeded(state, memoryManager, precision);
                     },
                     (values, state) -> {
@@ -235,7 +240,6 @@ public class HyperLogLogDistinctAggregation extends AggregationFunction<HyperLog
                 );
             case StringType.ID:
             case CharacterType.ID:
-                var precision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
                 return new HllAggregator(reference.storageIdent(), dataType, precision) {
                     @Override
                     public void apply(RamAccounting ramAccounting, int doc, HllState state) throws IOException {
@@ -250,8 +254,7 @@ public class HyperLogLogDistinctAggregation extends AggregationFunction<HyperLog
                     }
                 };
             case IpType.ID:
-                var ipPrecision = optionalParams.size() == 1 ? (Integer) optionalParams.get(0).value() : HyperLogLogPlusPlus.DEFAULT_PRECISION;
-                return new HllAggregator(reference.storageIdent(), dataType, ipPrecision) {
+                return new HllAggregator(reference.storageIdent(), dataType, precision) {
                     @Override
                     public void apply(RamAccounting ramAccounting, int doc, HllState state) throws IOException {
                         if (super.values.advanceExact(doc) && super.values.docValueCount() == 1) {
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java b/server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java
index a1330b3b43..de8a47c59a 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/AggregationFunction.java
@@ -117,6 +117,17 @@ public abstract class AggregationFunction<TPartial, TFinal> implements FunctionI
                                                 "not removable cumulative");
     }
 
+    /**
+     * @param referenceResolver A LuceneReferenceResolver to resolve references.
+     * @param aggregationReferences contains a list of references of the size of the input values of the function.
+     *                              If the value at the position is not a reference in the inputs the value in
+     *                              the list is null.
+     * @param table DocTableInfo for the underlying table which is the source of the doc-values.
+     * @param optionalParams contains a list of literals of the size of the input values of the function.
+     *                       If the value at the position is not a literal in the inputs the value in the list is
+     *                       null.
+     * @return A DocValueAggregator or null if there is no doc-value support for the given input parameters.
+     */
     @Nullable
     public DocValueAggregator<?> getDocValueAggregator(LuceneReferenceResolver referenceResolver,
                                                        List<Reference> aggregationReferences,
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java
index d0be2602d5..c89ad62d7f 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/ArbitraryAggregation.java
@@ -156,6 +156,9 @@ public class ArbitraryAggregation extends AggregationFunction<Object, Object> {
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference arg = aggregationReferences.get(0);
+        if (arg == null) {
+            return null;
+        }
         if (!arg.hasDocValues()) {
             return null;
         }
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java
index 6fbd5ee644..ef853df673 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/CmpByAggregation.java
@@ -160,11 +160,19 @@ public final class CmpByAggregation extends AggregationFunction<CmpByAggregation
                                                        List<Reference> aggregationReferences,
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
-        Reference searchRef = aggregationReferences.get(1);
-        if (!searchRef.hasDocValues()) {
+        Reference returnField = aggregationReferences.getFirst();
+        Reference searchField = aggregationReferences.getLast();
+        if (returnField == null) {
             return null;
         }
-        DataType<?> searchType = searchRef.valueType();
+        if (searchField == null) {
+            return null;
+        }
+        if (!searchField.hasDocValues()) {
+            return null;
+        }
+
+        DataType<?> searchType = searchField.valueType();
         switch (searchType.id()) {
             case ByteType.ID:
             case ShortType.ID:
@@ -172,17 +180,17 @@ public final class CmpByAggregation extends AggregationFunction<CmpByAggregation
             case LongType.ID:
             case TimestampType.ID_WITH_TZ:
             case TimestampType.ID_WITHOUT_TZ:
-                var resultExpression = referenceResolver.getImplementation(aggregationReferences.get(0));
+                var resultExpression = referenceResolver.getImplementation(returnField);
                 if (signature.getName().name().equalsIgnoreCase("min_by")) {
                     return new MinByLong(
-                        searchRef.storageIdent(),
+                        searchField.storageIdent(),
                         searchType,
                         resultExpression,
                         new CollectorContext(table.droppedColumns(), table.lookupNameBySourceKey())
                     );
                 } else {
                     return new MaxByLong(
-                        searchRef.storageIdent(),
+                        searchField.storageIdent(),
                         searchType,
                         resultExpression,
                         new CollectorContext(table.droppedColumns(), table.lookupNameBySourceKey())
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java
index d9031f8daf..56d311ee73 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/CountAggregation.java
@@ -300,6 +300,9 @@ public class CountAggregation extends AggregationFunction<MutableLong, Long> {
             return null;
         }
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (reference.valueType().id() == ObjectType.ID) {
             // Count on object would require loading the source just to check if there is a value.
             // Try to count on a non-null sub-column to be able to utilize doc-values.
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java
index eab667637a..fe96393621 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/GeometricMeanAggregation.java
@@ -307,6 +307,9 @@ public class GeometricMeanAggregation extends AggregationFunction<GeometricMeanA
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java
index 02eac7e926..dcfa28583e 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/MaximumAggregation.java
@@ -221,6 +221,11 @@ public abstract class MaximumAggregation extends AggregationFunction<Object, Obj
                                                            DocTableInfo table,
                                                            List<Literal<?>> optionalParams) {
             Reference reference = aggregationReferences.get(0);
+
+            if (reference == null) {
+                return null;
+            }
+
             if (!reference.hasDocValues()) {
                 return null;
             }
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java
index b4069e7073..83df215867 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/MinimumAggregation.java
@@ -255,6 +255,9 @@ public abstract class MinimumAggregation extends AggregationFunction<Object, Obj
                                                            DocTableInfo table,
                                                            List<Literal<?>> optionalParams) {
             Reference reference = aggregationReferences.get(0);
+            if (reference == null) {
+                return null;
+            }
             if (!reference.hasDocValues()) {
                 return null;
             }
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java
index 6612fe9d59..4987ca72c4 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/NumericSumAggregation.java
@@ -182,6 +182,9 @@ public class NumericSumAggregation extends AggregationFunction<BigDecimal, BigDe
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java
index c82d442810..8c24fd04d7 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/StandardDeviationAggregation.java
@@ -229,6 +229,9 @@ public class StandardDeviationAggregation extends AggregationFunction<StandardDe
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java
index c6a35e3f8f..62b7196c9f 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/SumAggregation.java
@@ -195,9 +195,15 @@ public class SumAggregation<T extends Number> extends AggregationFunction<T, T>
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+
+        if (reference == null) {
+            return null;
+        }
+
         if (!reference.hasDocValues()) {
             return null;
         }
+
         switch (reference.valueType().id()) {
             case ByteType.ID:
             case ShortType.ID:
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java
index 7576839038..e6d1ad8f8a 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/VarianceAggregation.java
@@ -229,6 +229,9 @@ public class VarianceAggregation extends AggregationFunction<Variance, Double> {
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java
index c2f01eeaa8..e63e6a5dcd 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/AverageAggregation.java
@@ -311,6 +311,9 @@ public class AverageAggregation extends AggregationFunction<AverageAggregation.A
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java
index 37312ef250..77c221b05b 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageAggregation.java
@@ -197,6 +197,9 @@ public class NumericAverageAggregation extends AggregationFunction<NumericAverag
                                                        DocTableInfo table,
                                                        List<Literal<?>> optionalParams) {
         Reference reference = aggregationReferences.get(0);
+        if (reference == null) {
+            return null;
+        }
         if (!reference.hasDocValues()) {
             return null;
         }
diff --git a/server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java b/server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java
index 30f58aca25..3229d4f240 100644
--- a/server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java
+++ b/server/src/main/java/io/crate/execution/engine/collect/DocValuesAggregates.java
@@ -154,6 +154,7 @@ public final class DocValuesAggregates {
             for (var input : aggregation.inputs()) {
                 if (input instanceof Literal<?> literal) {
                     literals.add(literal);
+                    aggregationReferences.add(null);
                 } else {
                     var reference = input.accept(AggregationInputToReferenceResolver.INSTANCE, toCollect);
                     if (reference == null) {
@@ -164,6 +165,7 @@ public final class DocValuesAggregates {
                     assert reference.ident().columnIdent().fqn().startsWith(DocSysColumns.Names.DOC) == false :
                         "Source look-up for Reference " + reference + " is not allowed in DocValuesAggregates.";
                     aggregationReferences.add(reference);
+                    literals.add(null);
                 }
             }
             FunctionImplementation func = functions.getQualified(aggregation);
diff --git a/server/src/test/java/io/crate/integrationtests/AggregateExpressionIntegrationTest.java b/server/src/test/java/io/crate/integrationtests/AggregateExpressionIntegrationTest.java
index b40cd23259..e160536dfd 100644
--- a/server/src/test/java/io/crate/integrationtests/AggregateExpressionIntegrationTest.java
+++ b/server/src/test/java/io/crate/integrationtests/AggregateExpressionIntegrationTest.java
@@ -297,4 +297,12 @@ public class AggregateExpressionIntegrationTest extends IntegTestCase {
             "b",
             "c");
     }
+
+    public void test_assure_cmp_by_function_call_with_reference_and_literal_does_not_throw_exception() {
+        execute("create table tbl (name text, x int);");
+        execute("insert into tbl (name, x) values ('foo', 10)");
+        execute("refresh table tbl");
+        execute("select max_by(name, 1) from tbl;");
+        assertThat(response).hasRows("foo");
+    }
 }

```
