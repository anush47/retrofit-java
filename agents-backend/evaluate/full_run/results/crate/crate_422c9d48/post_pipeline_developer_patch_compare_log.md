# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java']
- Developer Java files: ['server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java']
- Overlap Java files: ['server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -231,6 +231,12 @@
                     return offender;
                 }
             }
+            for (Symbol partition : function.windowDefinition().partitions()) {
+                Symbol offender = partition.accept(this, groupBy);
+                if (offender != null) {
+                    return offender;
+                }
+            }
             return null;
         }
 

```

Generated
```diff
@@ -231,6 +231,12 @@
                     return offender;
                 }
             }
+            for (Symbol partition : function.windowDefinition().partitions()) {
+                Symbol offender = partition.accept(this, groupBy);
+                if (offender != null) {
+                    return offender;
+                }
+            }
             return null;
         }
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java b/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java
index 5424e6f310..13a0ab2758 100644
--- a/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java
+++ b/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java
@@ -231,6 +231,12 @@ public final class GroupAndAggregateSemantics {
                     return offender;
                 }
             }
+            for (Symbol partition : function.windowDefinition().partitions()) {
+                Symbol offender = partition.accept(this, groupBy);
+                if (offender != null) {
+                    return offender;
+                }
+            }
             return null;
         }
 

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java b/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java
index 5424e6f310..13a0ab2758 100644
--- a/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java
+++ b/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java
@@ -231,6 +231,12 @@ public final class GroupAndAggregateSemantics {
                     return offender;
                 }
             }
+            for (Symbol partition : function.windowDefinition().partitions()) {
+                Symbol offender = partition.accept(this, groupBy);
+                if (offender != null) {
+                    return offender;
+                }
+            }
             return null;
         }
 

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/docs/appendices/release-notes/5.10.12.rst b/docs/appendices/release-notes/5.10.12.rst
index c18e6b5051..78d1480a10 100644
--- a/docs/appendices/release-notes/5.10.12.rst
+++ b/docs/appendices/release-notes/5.10.12.rst
@@ -68,3 +68,11 @@ Fixes
 
 - Fixed an issue that could lead to an ``OutOfMemoryError`` when running a
   query with aggregations under memory pressure in a multi-node cluster.
+
+- Improved error message when attempting to use a column in ``PARTITION BY``
+  clause of a :ref:`window function <window-functions>`, which is not also
+  included in the ``GROUP BY``, e.g.::
+
+    SELECT sum(x) OVER(PARTITION BY x, y)
+    FROM unnest([1], [6]) AS t (x, y)
+    GROUP BY x
diff --git a/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java b/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java
index 5424e6f310..13a0ab2758 100644
--- a/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java
+++ b/server/src/main/java/io/crate/expression/symbol/GroupAndAggregateSemantics.java
@@ -231,6 +231,12 @@ public final class GroupAndAggregateSemantics {
                     return offender;
                 }
             }
+            for (Symbol partition : function.windowDefinition().partitions()) {
+                Symbol offender = partition.accept(this, groupBy);
+                if (offender != null) {
+                    return offender;
+                }
+            }
             return null;
         }
 
diff --git a/server/src/test/java/io/crate/analyze/SelectWindowFunctionAnalyzerTest.java b/server/src/test/java/io/crate/analyze/SelectWindowFunctionAnalyzerTest.java
index ad6a85dda0..9051eab805 100644
--- a/server/src/test/java/io/crate/analyze/SelectWindowFunctionAnalyzerTest.java
+++ b/server/src/test/java/io/crate/analyze/SelectWindowFunctionAnalyzerTest.java
@@ -209,4 +209,14 @@ public class SelectWindowFunctionAnalyzerTest extends CrateDummyClusterServiceUn
             .isExactlyInstanceOf(IllegalArgumentException.class)
             .hasMessageStartingWith("'x' must appear in the GROUP BY clause or be used in an aggregation function.");
     }
+
+    @Test
+    public void test_window_function_partition_symbols_not_in_grouping_raises_an_error() {
+        assertThatThrownBy(() -> e.analyze(
+            "select sum(x) over(partition by x, y) " +
+                "FROM unnest([1], [6]) as t (x, y) " +
+                "group by x"))
+            .isExactlyInstanceOf(IllegalArgumentException.class)
+            .hasMessageStartingWith("'y' must appear in the GROUP BY clause or be used in an aggregation function.");
+    }
 }

```
