# Full Trace of Agentic File Edits

## Attempt #1

### Final Output Diff
**server/src/main/java/io/crate/execution/dml/Indexer.java** [replace]
```java
// --- OLD ---
<developer patch fast path>
// --- NEW ---
diff --git a/server/src/main/java/io/crate/execution/dml/Indexer.java b/server/src/main/java/io/crate/execution/dml/Indexer.java
index 216fcf3062..6e9b21a35d 100644
--- a/server/src/main/java/io/crate/execution/dml/Indexer.java
+++ b/server/src/main/java/io/crate/execution/dml/Indexer.java
@@ -31,6 +31,7 @@ import java.util.Collection;
 import java.util.Collections;
 import java.util.Comparator;
 import java.util.HashMap;
+import java.util.LinkedHashSet;
 import java.util.List;
 import java.util.Locale;
 import java.util.Map;
@@ -678,7 +679,7 @@ public class Indexer {
      * Looks for new columns in the values of the given IndexItem and returns them.
      */
     public List<Reference> collectSchemaUpdates(IndexItem item) throws IOException {
-        ArrayList<Reference> newColumns = new ArrayList<>();
+        LinkedHashSet<Reference> newColumns = new LinkedHashSet<>();
         Consumer<? super Reference> onDynamicColumn = ref -> {
             ref.column().validForCreate();
             newColumns.add(ref);
@@ -717,7 +718,7 @@ public class Indexer {
                 synthetics::get
             );
         }
-        return newColumns;
+        return newColumns.stream().toList();
     }
 
     /**
```