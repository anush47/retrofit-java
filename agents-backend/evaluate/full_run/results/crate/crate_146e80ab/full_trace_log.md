# Full Trace of Agentic File Edits

## Attempt #1

### Final Output Diff
**server/src/main/java/io/crate/execution/engine/aggregation/impl/average/numeric/NumericAverageState.java** [replace]
```java
// --- OLD ---
<developer patch fast path>
// --- NEW ---
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