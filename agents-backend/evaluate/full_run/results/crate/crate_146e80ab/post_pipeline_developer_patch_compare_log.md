# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java']
- Developer Java files: ['server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java']
- Overlap Java files: ['server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java

- Developer hunks: 2
- Generated hunks: 2

#### Hunk 1

Developer
```diff
@@ -22,6 +22,7 @@
 package io.crate.execution.engine.aggregation.impl.average.numeric;
 
 import java.math.BigDecimal;
+import java.math.MathContext;
 import java.util.Objects;
 
 import org.jetbrains.annotations.NotNull;

```

Generated
```diff
@@ -22,6 +22,7 @@
 package io.crate.execution.engine.aggregation.impl.average.numeric;
 
 import java.math.BigDecimal;
+import java.math.MathContext;
 import java.util.Objects;
 
 import org.jetbrains.annotations.NotNull;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -44,7 +45,10 @@
 
     public BigDecimal value() {
         if (count > 0) {
-            return sum.value().divide(BigDecimal.valueOf(count));
+            // We need to use divide with a MathContext to avoid ArithmeticException on infinite fractions.
+            // Using best (finite) precision as we want to compute final result with the best precision.
+            // If users want to reduce the precision of the final result, they can use explicit cast.
+            return sum.value().divide(BigDecimal.valueOf(count), MathContext.DECIMAL128);
         } else {
             return null;
         }

```

Generated
```diff
@@ -44,7 +45,10 @@
 
     public BigDecimal value() {
         if (count > 0) {
-            return sum.value().divide(BigDecimal.valueOf(count));
+            // We need to use divide with a MathContext to avoid ArithmeticException on infinite fractions.
+            // Using best (finite) precision as we want to compute final result with the best precision.
+            // If users want to reduce the precision of the final result, they can use explicit cast.
+            return sum.value().divide(BigDecimal.valueOf(count), MathContext.DECIMAL128);
         } else {
             return null;
         }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java
index 8fba81072e..468a19123b 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java
@@ -22,6 +22,7 @@
 package io.crate.execution.engine.aggregation.impl.average.numeric;
 
 import java.math.BigDecimal;
+import java.math.MathContext;
 import java.util.Objects;
 
 import org.jetbrains.annotations.NotNull;
@@ -44,7 +45,10 @@ public class NumericAverageState<T extends NumericValueHolder> implements Compar
 
     public BigDecimal value() {
         if (count > 0) {
-            return sum.value().divide(BigDecimal.valueOf(count));
+            // We need to use divide with a MathContext to avoid ArithmeticException on infinite fractions.
+            // Using best (finite) precision as we want to compute final result with the best precision.
+            // If users want to reduce the precision of the final result, they can use explicit cast.
+            return sum.value().divide(BigDecimal.valueOf(count), MathContext.DECIMAL128);
         } else {
             return null;
         }

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java
index 8fba81072e..468a19123b 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java
@@ -22,6 +22,7 @@
 package io.crate.execution.engine.aggregation.impl.average.numeric;
 
 import java.math.BigDecimal;
+import java.math.MathContext;
 import java.util.Objects;
 
 import org.jetbrains.annotations.NotNull;
@@ -44,7 +45,10 @@ public class NumericAverageState<T extends NumericValueHolder> implements Compar
 
     public BigDecimal value() {
         if (count > 0) {
-            return sum.value().divide(BigDecimal.valueOf(count));
+            // We need to use divide with a MathContext to avoid ArithmeticException on infinite fractions.
+            // Using best (finite) precision as we want to compute final result with the best precision.
+            // If users want to reduce the precision of the final result, they can use explicit cast.
+            return sum.value().divide(BigDecimal.valueOf(count), MathContext.DECIMAL128);
         } else {
             return null;
         }

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/docs/appendices/release-notes/5.10.1.rst b/docs/appendices/release-notes/5.10.1.rst
index 2c87d3db18..89fe39918d 100644
--- a/docs/appendices/release-notes/5.10.1.rst
+++ b/docs/appendices/release-notes/5.10.1.rst
@@ -112,3 +112,7 @@ Fixes
   :ref:`numeric <type-numeric>` values. Previously, the values where implicitly
   casted to ``STRING`` and the aggregations where using alphanumeric ordering,
   instead of numeric ordering.
+
+- Fixed an issue that led to ``ArithmeticException`` when using
+  :ref:`AVG <aggregation-avg>` with ``NUMERIC`` type and result was an infinite
+  fraction, like 1/3.
diff --git a/docs/appendices/release-notes/5.9.10.rst b/docs/appendices/release-notes/5.9.10.rst
index 54c9b3d018..ab2ddf863d 100644
--- a/docs/appendices/release-notes/5.9.10.rst
+++ b/docs/appendices/release-notes/5.9.10.rst
@@ -84,3 +84,6 @@ Fixes
   casted to ``STRING`` and the aggregations where using alphanumeric ordering,
   instead of numeric ordering.
 
+- Fixed an issue that led to ``ArithmeticException`` when using
+  :ref:`AVG <aggregation-avg>` with ``NUMERIC`` type and result was an infinite
+  fraction, like 1/3.
diff --git a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java
index 8fba81072e..468a19123b 100644
--- a/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java
+++ b/server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java
@@ -22,6 +22,7 @@
 package io.crate.execution.engine.aggregation.impl.average.numeric;
 
 import java.math.BigDecimal;
+import java.math.MathContext;
 import java.util.Objects;
 
 import org.jetbrains.annotations.NotNull;
@@ -44,7 +45,10 @@ public class NumericAverageState<T extends NumericValueHolder> implements Compar
 
     public BigDecimal value() {
         if (count > 0) {
-            return sum.value().divide(BigDecimal.valueOf(count));
+            // We need to use divide with a MathContext to avoid ArithmeticException on infinite fractions.
+            // Using best (finite) precision as we want to compute final result with the best precision.
+            // If users want to reduce the precision of the final result, they can use explicit cast.
+            return sum.value().divide(BigDecimal.valueOf(count), MathContext.DECIMAL128);
         } else {
             return null;
         }
diff --git a/server/src/test/java/io/crate/execution/engine/aggregation/impl/AverageAggregationTest.java b/server/src/test/java/io/crate/execution/engine/aggregation/impl/AverageAggregationTest.java
index f45a7f3960..0ec6601e7b 100644
--- a/server/src/test/java/io/crate/execution/engine/aggregation/impl/AverageAggregationTest.java
+++ b/server/src/test/java/io/crate/execution/engine/aggregation/impl/AverageAggregationTest.java
@@ -241,4 +241,11 @@ public class AverageAggregationTest extends AggregationTestCase {
         );
         assertThat(((NumericAverageState<?>) result).value().toString()).isEqualTo(expected.toString());
     }
+
+    @Test
+    public void test_avg_numeric_can_handle_non_terminating_decimal_expansion() throws Exception {
+        assertThat(executeAvgAgg(
+            new NumericType(18, 3), new Object[][]{{BigDecimal.valueOf(6.00)}, {BigDecimal.valueOf(2.0)}, {BigDecimal.valueOf(2.0)}})
+        ).isEqualTo(new BigDecimal("3.333333333333333333333333333333333"));
+    }
 }

```
