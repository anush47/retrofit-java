# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/metadata/doc/DocTableInfo.java']
- Developer Java files: ['server/src/main/java/io/crate/metadata/doc/DocTableInfo.java']
- Overlap Java files: ['server/src/main/java/io/crate/metadata/doc/DocTableInfo.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/metadata/doc/DocTableInfo.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/metadata/doc/DocTableInfo.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/metadata/doc/DocTableInfo.java

- Developer hunks: 15
- Generated hunks: 15

#### Hunk 1

Developer
```diff
@@ -180,14 +180,17 @@
     public static final Setting<Long> DEPTH_LIMIT_SETTING =
         Setting.longSetting("index.mapping.depth.limit", 20L, 1, Property.Dynamic, Property.IndexScope);
 
-    private final List<Reference> columns;
+    private final List<Reference> topLevelColumns;
     private final Set<Reference> droppedColumns;
     private final List<GeneratedReference> generatedColumns;
     private final List<Reference> partitionedByColumns;
     private final List<Reference> defaultExpressionColumns;
     private final Collection<ColumnIdent> notNullColumns;
     private final Map<ColumnIdent, IndexReference> indexColumns;
-    private final Map<ColumnIdent, Reference> references;
+    /**
+     * Top level and nested columns, including system columns. Excludes dropped columns
+     **/
+    private final Map<ColumnIdent, Reference> allColumns;
     private final Map<String, String> leafNamesByOid;
     private final RelationName ident;
     @Nullable

```

Generated
```diff
@@ -180,14 +180,17 @@
     public static final Setting<Long> DEPTH_LIMIT_SETTING =
         Setting.longSetting("index.mapping.depth.limit", 20L, 1, Property.Dynamic, Property.IndexScope);
 
-    private final List<Reference> columns;
+    private final List<Reference> topLevelColumns;
     private final Set<Reference> droppedColumns;
     private final List<GeneratedReference> generatedColumns;
     private final List<Reference> partitionedByColumns;
     private final List<Reference> defaultExpressionColumns;
     private final Collection<ColumnIdent> notNullColumns;
     private final Map<ColumnIdent, IndexReference> indexColumns;
-    private final Map<ColumnIdent, Reference> references;
+    /**
+     * Top level and nested columns, including system columns. Excludes dropped columns
+     **/
+    private final Map<ColumnIdent, Reference> allColumns;
     private final Map<String, String> leafNamesByOid;
     private final RelationName ident;
     @Nullable

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -235,27 +238,27 @@
         this.droppedColumns = references.values().stream()
             .filter(Reference::isDropped)
             .collect(Collectors.toSet());
-        this.references = references.entrySet().stream()
+        this.allColumns = references.entrySet().stream()
             .filter(entry -> !entry.getValue().isDropped())
             .collect(Collectors.toMap(Entry::getKey, Entry::getValue));
-        SysColumns.forTable(ident, this.references::put);
-        this.columns = this.references.values().stream()
+        this.topLevelColumns = this.allColumns.values().stream()
             .filter(r -> !r.column().isSystemColumn())
             .filter(r -> r.column().isRoot())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .toList();
+        SysColumns.forTable(ident, this.allColumns::put);
         this.partitionedByColumns = Lists.map(partitionedBy, x -> {
-            Reference ref = this.references.get(x);
+            Reference ref = this.allColumns.get(x);
             assert ref != null : "Column in `partitionedBy` must be present in `references`";
             return ref;
         });
-        this.generatedColumns = this.references.values().stream()
+        this.generatedColumns = this.allColumns.values().stream()
             .filter(r -> r instanceof GeneratedReference && !r.isDropped())
             .map(r -> (GeneratedReference) r)
             .toList();
         this.indexColumns = indexColumns;
         leafNamesByOid = new HashMap<>();
-        Stream.concat(Stream.concat(this.references.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
+        Stream.concat(Stream.concat(this.allColumns.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
             .filter(r -> r.oid() != Metadata.COLUMN_OID_UNASSIGNED)
             .forEach(r -> leafNamesByOid.put(Long.toString(r.oid()), r.column().leafName()));
         this.ident = ident;

```

Generated
```diff
@@ -235,27 +238,27 @@
         this.droppedColumns = references.values().stream()
             .filter(Reference::isDropped)
             .collect(Collectors.toSet());
-        this.references = references.entrySet().stream()
+        this.allColumns = references.entrySet().stream()
             .filter(entry -> !entry.getValue().isDropped())
             .collect(Collectors.toMap(Entry::getKey, Entry::getValue));
-        SysColumns.forTable(ident, this.references::put);
-        this.columns = this.references.values().stream()
+        this.topLevelColumns = this.allColumns.values().stream()
             .filter(r -> !r.column().isSystemColumn())
             .filter(r -> r.column().isRoot())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .toList();
+        SysColumns.forTable(ident, this.allColumns::put);
         this.partitionedByColumns = Lists.map(partitionedBy, x -> {
-            Reference ref = this.references.get(x);
+            Reference ref = this.allColumns.get(x);
             assert ref != null : "Column in `partitionedBy` must be present in `references`";
             return ref;
         });
-        this.generatedColumns = this.references.values().stream()
+        this.generatedColumns = this.allColumns.values().stream()
             .filter(r -> r instanceof GeneratedReference && !r.isDropped())
             .map(r -> (GeneratedReference) r)
             .toList();
         this.indexColumns = indexColumns;
         leafNamesByOid = new HashMap<>();
-        Stream.concat(Stream.concat(this.references.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
+        Stream.concat(Stream.concat(this.allColumns.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
             .filter(r -> r.oid() != Metadata.COLUMN_OID_UNASSIGNED)
             .forEach(r -> leafNamesByOid.put(Long.toString(r.oid()), r.column().leafName()));
         this.ident = ident;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 3

Developer
```diff
@@ -291,8 +294,8 @@
         this.versionUpgraded = versionUpgraded;
         this.closed = closed;
         this.supportedOperations = supportedOperations;
-        this.docColumn = new TableColumn(SysColumns.DOC, this.references);
-        this.defaultExpressionColumns = this.references.values()
+        this.docColumn = new TableColumn(SysColumns.DOC, this.allColumns);
+        this.defaultExpressionColumns = this.allColumns.values()
             .stream()
             .filter(r -> r.defaultExpression() != null)
             .toList();

```

Generated
```diff
@@ -291,8 +294,8 @@
         this.versionUpgraded = versionUpgraded;
         this.closed = closed;
         this.supportedOperations = supportedOperations;
-        this.docColumn = new TableColumn(SysColumns.DOC, this.references);
-        this.defaultExpressionColumns = this.references.values()
+        this.docColumn = new TableColumn(SysColumns.DOC, this.allColumns);
+        this.defaultExpressionColumns = this.allColumns.values()
             .stream()
             .filter(r -> r.defaultExpression() != null)
             .toList();

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 4

Developer
```diff
@@ -308,7 +311,7 @@
 
     @Nullable
     public Reference getReference(ColumnIdent columnIdent) {
-        Reference reference = references.get(columnIdent);
+        Reference reference = allColumns.get(columnIdent);
         if (reference == null) {
             return docColumn.getReference(ident(), columnIdent);
         }

```

Generated
```diff
@@ -308,7 +311,7 @@
 
     @Nullable
     public Reference getReference(ColumnIdent columnIdent) {
-        Reference reference = references.get(columnIdent);
+        Reference reference = allColumns.get(columnIdent);
         if (reference == null) {
             return docColumn.getReference(ident(), columnIdent);
         }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 5

Developer
```diff
@@ -319,7 +322,7 @@
     public Reference getReference(String storageIdent) {
         try {
             long oid = Long.parseLong(storageIdent);
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.oid() == oid) {
                     return ref;
                 }

```

Generated
```diff
@@ -319,7 +322,7 @@
     public Reference getReference(String storageIdent) {
         try {
             long oid = Long.parseLong(storageIdent);
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.oid() == oid) {
                     return ref;
                 }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 6

Developer
```diff
@@ -369,14 +372,14 @@
 
     private ReferenceTree referenceTree() {
         if (refTree == null) {
-            refTree = ReferenceTree.of(references.values());
+            refTree = ReferenceTree.of(allColumns.values());
         }
         return refTree;
     }
 
     @Override
     public List<Reference> columns() {
-        return columns;
+        return topLevelColumns;
     }
 
     @Override

```

Generated
```diff
@@ -369,14 +372,14 @@
 
     private ReferenceTree referenceTree() {
         if (refTree == null) {
-            refTree = ReferenceTree.of(references.values());
+            refTree = ReferenceTree.of(allColumns.values());
         }
         return refTree;
     }
 
     @Override
     public List<Reference> columns() {
-        return columns;
+        return topLevelColumns;
     }
 
     @Override

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 7

Developer
```diff
@@ -386,7 +389,7 @@
 
     public int maxPosition() {
         return Math.max(
-            references.values().stream()
+            allColumns.values().stream()
                 .filter(ref -> !ref.column().isSystemColumn())
                 .mapToInt(Reference::position)
                 .max()

```

Generated
```diff
@@ -386,7 +389,7 @@
 
     public int maxPosition() {
         return Math.max(
-            references.values().stream()
+            allColumns.values().stream()
                 .filter(ref -> !ref.column().isSystemColumn())
                 .mapToInt(Reference::position)
                 .max()

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 8

Developer
```diff
@@ -610,7 +613,7 @@
 
     @Override
     public Iterator<Reference> iterator() {
-        return references.values().stream()
+        return allColumns.values().stream()
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .iterator();
     }

```

Generated
```diff
@@ -610,7 +613,7 @@
 
     @Override
     public Iterator<Reference> iterator() {
-        return references.values().stream()
+        return allColumns.values().stream()
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .iterator();
     }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 9

Developer
```diff
@@ -662,7 +665,7 @@
 
     @Nullable
     public String getAnalyzerForColumnIdent(ColumnIdent ident) {
-        Reference reference = references.get(ident);
+        Reference reference = allColumns.get(ident);
         if (reference instanceof GeneratedReference gen) {
             reference = gen.reference();
         }

```

Generated
```diff
@@ -662,7 +665,7 @@
 
     @Nullable
     public String getAnalyzerForColumnIdent(ColumnIdent ident) {
-        Reference reference = references.get(ident);
+        Reference reference = allColumns.get(ident);
         if (reference instanceof GeneratedReference gen) {
             reference = gen.reference();
         }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 10

Developer
```diff
@@ -853,7 +856,7 @@
         }
         return new DocTableInfo(
             ident,
-            references,
+            allColumns,
             indexColumns,
             pkConstraintName,
             primaryKeys,

```

Generated
```diff
@@ -853,7 +856,7 @@
         }
         return new DocTableInfo(
             ident,
-            references,
+            allColumns,
             indexColumns,
             pkConstraintName,
             primaryKeys,

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 11

Developer
```diff
@@ -873,11 +876,11 @@
     public DocTableInfo dropColumns(List<DropColumn> columns) {
         validateDropColumns(columns);
         HashSet<Reference> toDrop = HashSet.newHashSet(columns.size());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         for (var column : columns) {
             ColumnIdent columnIdent = column.ref().column();
-            Reference reference = references.get(columnIdent);
+            Reference reference = allColumns.get(columnIdent);
             if (toDrop.contains(reference)) {
                 continue;
             }

```

Generated
```diff
@@ -873,11 +876,11 @@
     public DocTableInfo dropColumns(List<DropColumn> columns) {
         validateDropColumns(columns);
         HashSet<Reference> toDrop = HashSet.newHashSet(columns.size());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         for (var column : columns) {
             ColumnIdent columnIdent = column.ref().column();
-            Reference reference = references.get(columnIdent);
+            Reference reference = allColumns.get(columnIdent);
             if (toDrop.contains(reference)) {
                 continue;
             }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 12

Developer
```diff
@@ -894,7 +897,7 @@
             }
             toDrop.add(reference.withDropped(true));
             newReferences.replace(columnIdent, reference.withDropped(true));
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.column().isChildOf(columnIdent)) {
                     toDrop.add(ref);
                     newReferences.remove(ref.column());

```

Generated
```diff
@@ -894,7 +897,7 @@
             }
             toDrop.add(reference.withDropped(true));
             newReferences.replace(columnIdent, reference.withDropped(true));
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.column().isChildOf(columnIdent)) {
                     toDrop.add(ref);
                     newReferences.remove(ref.column());

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 13

Developer
```diff
@@ -963,7 +966,7 @@
         // where 1) is used to perform 2).
 
         Map<ColumnIdent, Reference> oldNameToRenamedRefs = new HashMap<>();
-        for (var ref : references.values()) {
+        for (var ref : allColumns.values()) {
             ColumnIdent column = ref.column();
             if (toBeRenamed.test(column)) {
                 var renamedRef = ref.withReferenceIdent(

```

Generated
```diff
@@ -963,7 +966,7 @@
         // where 1) is used to perform 2).
 
         Map<ColumnIdent, Reference> oldNameToRenamedRefs = new HashMap<>();
-        for (var ref : references.values()) {
+        for (var ref : allColumns.values()) {
             ColumnIdent column = ref.column();
             if (toBeRenamed.test(column)) {
                 var renamedRef = ref.withReferenceIdent(

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 14

Developer
```diff
@@ -1047,7 +1050,7 @@
                     droppedColumns.stream(),
                     indexColumns.values().stream()
                 ),
-                references.values().stream()
+                this.allColumns.values().stream()
             )
             .filter(ref -> !ref.column().isSystemColumn())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)

```

Generated
```diff
@@ -1047,7 +1050,7 @@
                     droppedColumns.stream(),
                     indexColumns.values().stream()
                 ),
-                references.values().stream()
+                this.allColumns.values().stream()
             )
             .filter(ref -> !ref.column().isSystemColumn())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 15

Developer
```diff
@@ -1205,7 +1208,12 @@
                                    IntArrayList pKeyIndices,
                                    Map<String, String> newCheckConstraints) {
         newColumns.forEach(ref -> ref.column().validForCreate());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        long allowedTotalColumns = TOTAL_COLUMNS_LIMIT.get(tableParameters);
+        int numSysColumns = SysColumns.COLUMN_IDENTS.size();
+        if (newColumns.size() + allColumns.size() - numSysColumns > allowedTotalColumns) {
+            throw new IllegalArgumentException("Limit of total columns [" + allowedTotalColumns + "] in table [" + ident + "] exceeded");
+        }
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         int maxPosition = maxPosition();
         AtomicInteger positions = new AtomicInteger(maxPosition);

```

Generated
```diff
@@ -1205,7 +1208,12 @@
                                    IntArrayList pKeyIndices,
                                    Map<String, String> newCheckConstraints) {
         newColumns.forEach(ref -> ref.column().validForCreate());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        long allowedTotalColumns = TOTAL_COLUMNS_LIMIT.get(tableParameters);
+        int numSysColumns = SysColumns.COLUMN_IDENTS.size();
+        if (newColumns.size() + allColumns.size() - numSysColumns > allowedTotalColumns) {
+            throw new IllegalArgumentException("Limit of total columns [" + allowedTotalColumns + "] in table [" + ident + "] exceeded");
+        }
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         int maxPosition = maxPosition();
         AtomicInteger positions = new AtomicInteger(maxPosition);

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java b/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java
index 27db907606..cde9e8430b 100644
--- a/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java
+++ b/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java
@@ -180,14 +180,17 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
     public static final Setting<Long> DEPTH_LIMIT_SETTING =
         Setting.longSetting("index.mapping.depth.limit", 20L, 1, Property.Dynamic, Property.IndexScope);
 
-    private final List<Reference> columns;
+    private final List<Reference> topLevelColumns;
     private final Set<Reference> droppedColumns;
     private final List<GeneratedReference> generatedColumns;
     private final List<Reference> partitionedByColumns;
     private final List<Reference> defaultExpressionColumns;
     private final Collection<ColumnIdent> notNullColumns;
     private final Map<ColumnIdent, IndexReference> indexColumns;
-    private final Map<ColumnIdent, Reference> references;
+    /**
+     * Top level and nested columns, including system columns. Excludes dropped columns
+     **/
+    private final Map<ColumnIdent, Reference> allColumns;
     private final Map<String, String> leafNamesByOid;
     private final RelationName ident;
     @Nullable
@@ -235,27 +238,27 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         this.droppedColumns = references.values().stream()
             .filter(Reference::isDropped)
             .collect(Collectors.toSet());
-        this.references = references.entrySet().stream()
+        this.allColumns = references.entrySet().stream()
             .filter(entry -> !entry.getValue().isDropped())
             .collect(Collectors.toMap(Entry::getKey, Entry::getValue));
-        SysColumns.forTable(ident, this.references::put);
-        this.columns = this.references.values().stream()
+        this.topLevelColumns = this.allColumns.values().stream()
             .filter(r -> !r.column().isSystemColumn())
             .filter(r -> r.column().isRoot())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .toList();
+        SysColumns.forTable(ident, this.allColumns::put);
         this.partitionedByColumns = Lists.map(partitionedBy, x -> {
-            Reference ref = this.references.get(x);
+            Reference ref = this.allColumns.get(x);
             assert ref != null : "Column in `partitionedBy` must be present in `references`";
             return ref;
         });
-        this.generatedColumns = this.references.values().stream()
+        this.generatedColumns = this.allColumns.values().stream()
             .filter(r -> r instanceof GeneratedReference && !r.isDropped())
             .map(r -> (GeneratedReference) r)
             .toList();
         this.indexColumns = indexColumns;
         leafNamesByOid = new HashMap<>();
-        Stream.concat(Stream.concat(this.references.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
+        Stream.concat(Stream.concat(this.allColumns.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
             .filter(r -> r.oid() != Metadata.COLUMN_OID_UNASSIGNED)
             .forEach(r -> leafNamesByOid.put(Long.toString(r.oid()), r.column().leafName()));
         this.ident = ident;
@@ -291,8 +294,8 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         this.versionUpgraded = versionUpgraded;
         this.closed = closed;
         this.supportedOperations = supportedOperations;
-        this.docColumn = new TableColumn(SysColumns.DOC, this.references);
-        this.defaultExpressionColumns = this.references.values()
+        this.docColumn = new TableColumn(SysColumns.DOC, this.allColumns);
+        this.defaultExpressionColumns = this.allColumns.values()
             .stream()
             .filter(r -> r.defaultExpression() != null)
             .toList();
@@ -308,7 +311,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     @Nullable
     public Reference getReference(ColumnIdent columnIdent) {
-        Reference reference = references.get(columnIdent);
+        Reference reference = allColumns.get(columnIdent);
         if (reference == null) {
             return docColumn.getReference(ident(), columnIdent);
         }
@@ -319,7 +322,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
     public Reference getReference(String storageIdent) {
         try {
             long oid = Long.parseLong(storageIdent);
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.oid() == oid) {
                     return ref;
                 }
@@ -369,14 +372,14 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     private ReferenceTree referenceTree() {
         if (refTree == null) {
-            refTree = ReferenceTree.of(references.values());
+            refTree = ReferenceTree.of(allColumns.values());
         }
         return refTree;
     }
 
     @Override
     public List<Reference> columns() {
-        return columns;
+        return topLevelColumns;
     }
 
     @Override
@@ -386,7 +389,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     public int maxPosition() {
         return Math.max(
-            references.values().stream()
+            allColumns.values().stream()
                 .filter(ref -> !ref.column().isSystemColumn())
                 .mapToInt(Reference::position)
                 .max()
@@ -610,7 +613,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     @Override
     public Iterator<Reference> iterator() {
-        return references.values().stream()
+        return allColumns.values().stream()
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .iterator();
     }
@@ -662,7 +665,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     @Nullable
     public String getAnalyzerForColumnIdent(ColumnIdent ident) {
-        Reference reference = references.get(ident);
+        Reference reference = allColumns.get(ident);
         if (reference instanceof GeneratedReference gen) {
             reference = gen.reference();
         }
@@ -853,7 +856,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         }
         return new DocTableInfo(
             ident,
-            references,
+            allColumns,
             indexColumns,
             pkConstraintName,
             primaryKeys,
@@ -873,11 +876,11 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
     public DocTableInfo dropColumns(List<DropColumn> columns) {
         validateDropColumns(columns);
         HashSet<Reference> toDrop = HashSet.newHashSet(columns.size());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         for (var column : columns) {
             ColumnIdent columnIdent = column.ref().column();
-            Reference reference = references.get(columnIdent);
+            Reference reference = allColumns.get(columnIdent);
             if (toDrop.contains(reference)) {
                 continue;
             }
@@ -894,7 +897,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
             }
             toDrop.add(reference.withDropped(true));
             newReferences.replace(columnIdent, reference.withDropped(true));
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.column().isChildOf(columnIdent)) {
                     toDrop.add(ref);
                     newReferences.remove(ref.column());
@@ -963,7 +966,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         // where 1) is used to perform 2).
 
         Map<ColumnIdent, Reference> oldNameToRenamedRefs = new HashMap<>();
-        for (var ref : references.values()) {
+        for (var ref : allColumns.values()) {
             ColumnIdent column = ref.column();
             if (toBeRenamed.test(column)) {
                 var renamedRef = ref.withReferenceIdent(
@@ -1047,7 +1050,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
                     droppedColumns.stream(),
                     indexColumns.values().stream()
                 ),
-                references.values().stream()
+                this.allColumns.values().stream()
             )
             .filter(ref -> !ref.column().isSystemColumn())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
@@ -1205,7 +1208,12 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
                                    IntArrayList pKeyIndices,
                                    Map<String, String> newCheckConstraints) {
         newColumns.forEach(ref -> ref.column().validForCreate());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        long allowedTotalColumns = TOTAL_COLUMNS_LIMIT.get(tableParameters);
+        int numSysColumns = SysColumns.COLUMN_IDENTS.size();
+        if (newColumns.size() + allColumns.size() - numSysColumns > allowedTotalColumns) {
+            throw new IllegalArgumentException("Limit of total columns [" + allowedTotalColumns + "] in table [" + ident + "] exceeded");
+        }
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         int maxPosition = maxPosition();
         AtomicInteger positions = new AtomicInteger(maxPosition);

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java b/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java
index 27db907606..cde9e8430b 100644
--- a/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java
+++ b/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java
@@ -180,14 +180,17 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
     public static final Setting<Long> DEPTH_LIMIT_SETTING =
         Setting.longSetting("index.mapping.depth.limit", 20L, 1, Property.Dynamic, Property.IndexScope);
 
-    private final List<Reference> columns;
+    private final List<Reference> topLevelColumns;
     private final Set<Reference> droppedColumns;
     private final List<GeneratedReference> generatedColumns;
     private final List<Reference> partitionedByColumns;
     private final List<Reference> defaultExpressionColumns;
     private final Collection<ColumnIdent> notNullColumns;
     private final Map<ColumnIdent, IndexReference> indexColumns;
-    private final Map<ColumnIdent, Reference> references;
+    /**
+     * Top level and nested columns, including system columns. Excludes dropped columns
+     **/
+    private final Map<ColumnIdent, Reference> allColumns;
     private final Map<String, String> leafNamesByOid;
     private final RelationName ident;
     @Nullable
@@ -235,27 +238,27 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         this.droppedColumns = references.values().stream()
             .filter(Reference::isDropped)
             .collect(Collectors.toSet());
-        this.references = references.entrySet().stream()
+        this.allColumns = references.entrySet().stream()
             .filter(entry -> !entry.getValue().isDropped())
             .collect(Collectors.toMap(Entry::getKey, Entry::getValue));
-        SysColumns.forTable(ident, this.references::put);
-        this.columns = this.references.values().stream()
+        this.topLevelColumns = this.allColumns.values().stream()
             .filter(r -> !r.column().isSystemColumn())
             .filter(r -> r.column().isRoot())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .toList();
+        SysColumns.forTable(ident, this.allColumns::put);
         this.partitionedByColumns = Lists.map(partitionedBy, x -> {
-            Reference ref = this.references.get(x);
+            Reference ref = this.allColumns.get(x);
             assert ref != null : "Column in `partitionedBy` must be present in `references`";
             return ref;
         });
-        this.generatedColumns = this.references.values().stream()
+        this.generatedColumns = this.allColumns.values().stream()
             .filter(r -> r instanceof GeneratedReference && !r.isDropped())
             .map(r -> (GeneratedReference) r)
             .toList();
         this.indexColumns = indexColumns;
         leafNamesByOid = new HashMap<>();
-        Stream.concat(Stream.concat(this.references.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
+        Stream.concat(Stream.concat(this.allColumns.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
             .filter(r -> r.oid() != Metadata.COLUMN_OID_UNASSIGNED)
             .forEach(r -> leafNamesByOid.put(Long.toString(r.oid()), r.column().leafName()));
         this.ident = ident;
@@ -291,8 +294,8 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         this.versionUpgraded = versionUpgraded;
         this.closed = closed;
         this.supportedOperations = supportedOperations;
-        this.docColumn = new TableColumn(SysColumns.DOC, this.references);
-        this.defaultExpressionColumns = this.references.values()
+        this.docColumn = new TableColumn(SysColumns.DOC, this.allColumns);
+        this.defaultExpressionColumns = this.allColumns.values()
             .stream()
             .filter(r -> r.defaultExpression() != null)
             .toList();
@@ -308,7 +311,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     @Nullable
     public Reference getReference(ColumnIdent columnIdent) {
-        Reference reference = references.get(columnIdent);
+        Reference reference = allColumns.get(columnIdent);
         if (reference == null) {
             return docColumn.getReference(ident(), columnIdent);
         }
@@ -319,7 +322,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
     public Reference getReference(String storageIdent) {
         try {
             long oid = Long.parseLong(storageIdent);
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.oid() == oid) {
                     return ref;
                 }
@@ -369,14 +372,14 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     private ReferenceTree referenceTree() {
         if (refTree == null) {
-            refTree = ReferenceTree.of(references.values());
+            refTree = ReferenceTree.of(allColumns.values());
         }
         return refTree;
     }
 
     @Override
     public List<Reference> columns() {
-        return columns;
+        return topLevelColumns;
     }
 
     @Override
@@ -386,7 +389,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     public int maxPosition() {
         return Math.max(
-            references.values().stream()
+            allColumns.values().stream()
                 .filter(ref -> !ref.column().isSystemColumn())
                 .mapToInt(Reference::position)
                 .max()
@@ -610,7 +613,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     @Override
     public Iterator<Reference> iterator() {
-        return references.values().stream()
+        return allColumns.values().stream()
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .iterator();
     }
@@ -662,7 +665,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     @Nullable
     public String getAnalyzerForColumnIdent(ColumnIdent ident) {
-        Reference reference = references.get(ident);
+        Reference reference = allColumns.get(ident);
         if (reference instanceof GeneratedReference gen) {
             reference = gen.reference();
         }
@@ -853,7 +856,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         }
         return new DocTableInfo(
             ident,
-            references,
+            allColumns,
             indexColumns,
             pkConstraintName,
             primaryKeys,
@@ -873,11 +876,11 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
     public DocTableInfo dropColumns(List<DropColumn> columns) {
         validateDropColumns(columns);
         HashSet<Reference> toDrop = HashSet.newHashSet(columns.size());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         for (var column : columns) {
             ColumnIdent columnIdent = column.ref().column();
-            Reference reference = references.get(columnIdent);
+            Reference reference = allColumns.get(columnIdent);
             if (toDrop.contains(reference)) {
                 continue;
             }
@@ -894,7 +897,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
             }
             toDrop.add(reference.withDropped(true));
             newReferences.replace(columnIdent, reference.withDropped(true));
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.column().isChildOf(columnIdent)) {
                     toDrop.add(ref);
                     newReferences.remove(ref.column());
@@ -963,7 +966,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         // where 1) is used to perform 2).
 
         Map<ColumnIdent, Reference> oldNameToRenamedRefs = new HashMap<>();
-        for (var ref : references.values()) {
+        for (var ref : allColumns.values()) {
             ColumnIdent column = ref.column();
             if (toBeRenamed.test(column)) {
                 var renamedRef = ref.withReferenceIdent(
@@ -1047,7 +1050,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
                     droppedColumns.stream(),
                     indexColumns.values().stream()
                 ),
-                references.values().stream()
+                this.allColumns.values().stream()
             )
             .filter(ref -> !ref.column().isSystemColumn())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
@@ -1205,7 +1208,12 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
                                    IntArrayList pKeyIndices,
                                    Map<String, String> newCheckConstraints) {
         newColumns.forEach(ref -> ref.column().validForCreate());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        long allowedTotalColumns = TOTAL_COLUMNS_LIMIT.get(tableParameters);
+        int numSysColumns = SysColumns.COLUMN_IDENTS.size();
+        if (newColumns.size() + allColumns.size() - numSysColumns > allowedTotalColumns) {
+            throw new IllegalArgumentException("Limit of total columns [" + allowedTotalColumns + "] in table [" + ident + "] exceeded");
+        }
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         int maxPosition = maxPosition();
         AtomicInteger positions = new AtomicInteger(maxPosition);

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/docs/appendices/release-notes/5.10.4.rst b/docs/appendices/release-notes/5.10.4.rst
index 3d2cc461d9..1734f1ff6b 100644
--- a/docs/appendices/release-notes/5.10.4.rst
+++ b/docs/appendices/release-notes/5.10.4.rst
@@ -44,6 +44,11 @@ See the :ref:`version_5.10.0` release notes for a full list of changes in the
 Fixes
 =====
 
+- Fixed an issue that could cause ``INSERT INTO`` statements which dynamically
+  create thousands of columns to overload the cluster state update process
+  before running into the ``mapping.total_fields.limit`` limit, causing other
+  statements trying to update the cluster state to timeout.
+
 - Fixed NPE when querying the :ref:`sys.allocations <sys-allocations>` table
   while no master node has been discovered. A proper exception is now thrown
   instead of an NPE.
diff --git a/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java b/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java
index 27db907606..cde9e8430b 100644
--- a/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java
+++ b/server/src/main/java/io/crate/metadata/doc/DocTableInfo.java
@@ -180,14 +180,17 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
     public static final Setting<Long> DEPTH_LIMIT_SETTING =
         Setting.longSetting("index.mapping.depth.limit", 20L, 1, Property.Dynamic, Property.IndexScope);
 
-    private final List<Reference> columns;
+    private final List<Reference> topLevelColumns;
     private final Set<Reference> droppedColumns;
     private final List<GeneratedReference> generatedColumns;
     private final List<Reference> partitionedByColumns;
     private final List<Reference> defaultExpressionColumns;
     private final Collection<ColumnIdent> notNullColumns;
     private final Map<ColumnIdent, IndexReference> indexColumns;
-    private final Map<ColumnIdent, Reference> references;
+    /**
+     * Top level and nested columns, including system columns. Excludes dropped columns
+     **/
+    private final Map<ColumnIdent, Reference> allColumns;
     private final Map<String, String> leafNamesByOid;
     private final RelationName ident;
     @Nullable
@@ -235,27 +238,27 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         this.droppedColumns = references.values().stream()
             .filter(Reference::isDropped)
             .collect(Collectors.toSet());
-        this.references = references.entrySet().stream()
+        this.allColumns = references.entrySet().stream()
             .filter(entry -> !entry.getValue().isDropped())
             .collect(Collectors.toMap(Entry::getKey, Entry::getValue));
-        SysColumns.forTable(ident, this.references::put);
-        this.columns = this.references.values().stream()
+        this.topLevelColumns = this.allColumns.values().stream()
             .filter(r -> !r.column().isSystemColumn())
             .filter(r -> r.column().isRoot())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .toList();
+        SysColumns.forTable(ident, this.allColumns::put);
         this.partitionedByColumns = Lists.map(partitionedBy, x -> {
-            Reference ref = this.references.get(x);
+            Reference ref = this.allColumns.get(x);
             assert ref != null : "Column in `partitionedBy` must be present in `references`";
             return ref;
         });
-        this.generatedColumns = this.references.values().stream()
+        this.generatedColumns = this.allColumns.values().stream()
             .filter(r -> r instanceof GeneratedReference && !r.isDropped())
             .map(r -> (GeneratedReference) r)
             .toList();
         this.indexColumns = indexColumns;
         leafNamesByOid = new HashMap<>();
-        Stream.concat(Stream.concat(this.references.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
+        Stream.concat(Stream.concat(this.allColumns.values().stream(), indexColumns.values().stream()), droppedColumns.stream())
             .filter(r -> r.oid() != Metadata.COLUMN_OID_UNASSIGNED)
             .forEach(r -> leafNamesByOid.put(Long.toString(r.oid()), r.column().leafName()));
         this.ident = ident;
@@ -291,8 +294,8 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         this.versionUpgraded = versionUpgraded;
         this.closed = closed;
         this.supportedOperations = supportedOperations;
-        this.docColumn = new TableColumn(SysColumns.DOC, this.references);
-        this.defaultExpressionColumns = this.references.values()
+        this.docColumn = new TableColumn(SysColumns.DOC, this.allColumns);
+        this.defaultExpressionColumns = this.allColumns.values()
             .stream()
             .filter(r -> r.defaultExpression() != null)
             .toList();
@@ -308,7 +311,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     @Nullable
     public Reference getReference(ColumnIdent columnIdent) {
-        Reference reference = references.get(columnIdent);
+        Reference reference = allColumns.get(columnIdent);
         if (reference == null) {
             return docColumn.getReference(ident(), columnIdent);
         }
@@ -319,7 +322,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
     public Reference getReference(String storageIdent) {
         try {
             long oid = Long.parseLong(storageIdent);
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.oid() == oid) {
                     return ref;
                 }
@@ -369,14 +372,14 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     private ReferenceTree referenceTree() {
         if (refTree == null) {
-            refTree = ReferenceTree.of(references.values());
+            refTree = ReferenceTree.of(allColumns.values());
         }
         return refTree;
     }
 
     @Override
     public List<Reference> columns() {
-        return columns;
+        return topLevelColumns;
     }
 
     @Override
@@ -386,7 +389,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     public int maxPosition() {
         return Math.max(
-            references.values().stream()
+            allColumns.values().stream()
                 .filter(ref -> !ref.column().isSystemColumn())
                 .mapToInt(Reference::position)
                 .max()
@@ -610,7 +613,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     @Override
     public Iterator<Reference> iterator() {
-        return references.values().stream()
+        return allColumns.values().stream()
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
             .iterator();
     }
@@ -662,7 +665,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
 
     @Nullable
     public String getAnalyzerForColumnIdent(ColumnIdent ident) {
-        Reference reference = references.get(ident);
+        Reference reference = allColumns.get(ident);
         if (reference instanceof GeneratedReference gen) {
             reference = gen.reference();
         }
@@ -853,7 +856,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         }
         return new DocTableInfo(
             ident,
-            references,
+            allColumns,
             indexColumns,
             pkConstraintName,
             primaryKeys,
@@ -873,11 +876,11 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
     public DocTableInfo dropColumns(List<DropColumn> columns) {
         validateDropColumns(columns);
         HashSet<Reference> toDrop = HashSet.newHashSet(columns.size());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         for (var column : columns) {
             ColumnIdent columnIdent = column.ref().column();
-            Reference reference = references.get(columnIdent);
+            Reference reference = allColumns.get(columnIdent);
             if (toDrop.contains(reference)) {
                 continue;
             }
@@ -894,7 +897,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
             }
             toDrop.add(reference.withDropped(true));
             newReferences.replace(columnIdent, reference.withDropped(true));
-            for (var ref : references.values()) {
+            for (var ref : allColumns.values()) {
                 if (ref.column().isChildOf(columnIdent)) {
                     toDrop.add(ref);
                     newReferences.remove(ref.column());
@@ -963,7 +966,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
         // where 1) is used to perform 2).
 
         Map<ColumnIdent, Reference> oldNameToRenamedRefs = new HashMap<>();
-        for (var ref : references.values()) {
+        for (var ref : allColumns.values()) {
             ColumnIdent column = ref.column();
             if (toBeRenamed.test(column)) {
                 var renamedRef = ref.withReferenceIdent(
@@ -1047,7 +1050,7 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
                     droppedColumns.stream(),
                     indexColumns.values().stream()
                 ),
-                references.values().stream()
+                this.allColumns.values().stream()
             )
             .filter(ref -> !ref.column().isSystemColumn())
             .sorted(Reference.CMP_BY_POSITION_THEN_NAME)
@@ -1205,7 +1208,12 @@ public class DocTableInfo implements TableInfo, ShardedTable, StoredTable {
                                    IntArrayList pKeyIndices,
                                    Map<String, String> newCheckConstraints) {
         newColumns.forEach(ref -> ref.column().validForCreate());
-        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(references);
+        long allowedTotalColumns = TOTAL_COLUMNS_LIMIT.get(tableParameters);
+        int numSysColumns = SysColumns.COLUMN_IDENTS.size();
+        if (newColumns.size() + allColumns.size() - numSysColumns > allowedTotalColumns) {
+            throw new IllegalArgumentException("Limit of total columns [" + allowedTotalColumns + "] in table [" + ident + "] exceeded");
+        }
+        HashMap<ColumnIdent, Reference> newReferences = new HashMap<>(allColumns);
         droppedColumns.forEach(ref -> newReferences.put(ref.column(), ref));
         int maxPosition = maxPosition();
         AtomicInteger positions = new AtomicInteger(maxPosition);
diff --git a/server/src/test/java/io/crate/metadata/doc/DocTableInfoTest.java b/server/src/test/java/io/crate/metadata/doc/DocTableInfoTest.java
index 204714b02b..28339fe06d 100644
--- a/server/src/test/java/io/crate/metadata/doc/DocTableInfoTest.java
+++ b/server/src/test/java/io/crate/metadata/doc/DocTableInfoTest.java
@@ -23,6 +23,7 @@ package io.crate.metadata.doc;
 
 import static io.crate.testing.Asserts.assertThat;
 import static java.util.Collections.singletonList;
+import static org.assertj.core.api.Assertions.assertThat;
 import static org.assertj.core.api.Assertions.assertThatThrownBy;
 import static org.elasticsearch.cluster.metadata.Metadata.COLUMN_OID_UNASSIGNED;
 
@@ -32,6 +33,7 @@ import java.util.Collections;
 import java.util.List;
 import java.util.Map;
 import java.util.concurrent.atomic.AtomicLong;
+import java.util.function.Function;
 
 import org.assertj.core.api.Assertions;
 import org.elasticsearch.Version;
@@ -565,6 +567,31 @@ public class DocTableInfoTest extends CrateDummyClusterServiceUnitTest {
             .hasType(oType);
     }
 
+    @Test
+    public void test_add_columns_fails_eagerly_on_too_many_columns() throws Exception {
+        SQLExecutor e = SQLExecutor.of(clusterService)
+            .addTable("create table tbl (x int) with (\"mapping.total_fields.limit\" = 3)");
+        DocTableInfo table = e.resolveTableInfo("tbl");
+        Function<String, Reference> newRef = name -> new SimpleReference(
+            new ReferenceIdent(table.ident(), ColumnIdent.of(name)),
+            RowGranularity.DOC,
+            DataTypes.INTEGER,
+            -1,
+            null
+        );
+        Reference a = newRef.apply("a");
+        Reference b = newRef.apply("b");
+        Reference c = newRef.apply("c");
+        assertThatThrownBy(() -> table.addColumns(
+            e.nodeCtx,
+            e.fulltextAnalyzerResolver(),
+            () -> 1,
+            List.of(a, b, c),
+            new IntArrayList(),
+            Map.of()
+        )).hasMessage("Limit of total columns [3] in table [doc.tbl] exceeded");
+    }
+
     @Test
     public void test_drop_column_fixes_inner_types_of_all_its_parents() throws Exception {
         SQLExecutor e = SQLExecutor.of(clusterService)

```
