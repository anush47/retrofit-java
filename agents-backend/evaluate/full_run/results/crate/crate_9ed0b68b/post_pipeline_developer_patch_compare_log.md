# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/types/ObjectType.java']
- Developer Java files: ['server/src/main/java/io/crate/types/ObjectType.java']
- Overlap Java files: ['server/src/main/java/io/crate/types/ObjectType.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/types/ObjectType.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/types/ObjectType.java']
- Mismatched files: ['server/src/main/java/io/crate/types/ObjectType.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/types/ObjectType.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -200,6 +200,12 @@
         }
     }
 
+    @Override
+    @SuppressWarnings("unchecked")
+    public Map<String, Object> valueForInsert(Map<String, Object> value) {
+        return convert(value, (dataType, v) -> ((DataType<Object>) dataType).valueForInsert(v));
+    }
+
     @SuppressWarnings("unchecked")
     private Map<String, Object> convert(Object value,
                                         BiFunction<DataType<?>, Object, Object> innerType) {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,13 +1 @@-@@ -200,6 +200,12 @@
-         }
-     }
- 
-+    @Override
-+    @SuppressWarnings("unchecked")
-+    public Map<String, Object> valueForInsert(Map<String, Object> value) {
-+        return convert(value, (dataType, v) -> ((DataType<Object>) dataType).valueForInsert(v));
-+    }
-+
-     @SuppressWarnings("unchecked")
-     private Map<String, Object> convert(Object value,
-                                         BiFunction<DataType<?>, Object, Object> innerType) {
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
diff --git a/docs/appendices/release-notes/5.10.9.rst b/docs/appendices/release-notes/5.10.9.rst
index 85d075158a..31684871b9 100644
--- a/docs/appendices/release-notes/5.10.9.rst
+++ b/docs/appendices/release-notes/5.10.9.rst
@@ -47,4 +47,11 @@ See the :ref:`version_5.10.0` release notes for a full list of changes in the
 Fixes
 =====
 
-None
+- Fixed an issue where length limits were not enforced during insertion.
+  e.g.::
+
+    CREATE TABLE t (o OBJECT AS (c CHAR(3)));
+    INSERT INTO t VALUES ({c='abcd'});
+
+  The insert succeeded before, but now it will cause an
+  ``IllegalArgumentException``.
diff --git a/server/src/main/java/io/crate/types/ObjectType.java b/server/src/main/java/io/crate/types/ObjectType.java
index 2aa5215b57..7aec5a61c8 100644
--- a/server/src/main/java/io/crate/types/ObjectType.java
+++ b/server/src/main/java/io/crate/types/ObjectType.java
@@ -200,6 +200,12 @@ public class ObjectType extends DataType<Map<String, Object>> implements Streame
         }
     }
 
+    @Override
+    @SuppressWarnings("unchecked")
+    public Map<String, Object> valueForInsert(Map<String, Object> value) {
+        return convert(value, (dataType, v) -> ((DataType<Object>) dataType).valueForInsert(v));
+    }
+
     @SuppressWarnings("unchecked")
     private Map<String, Object> convert(Object value,
                                         BiFunction<DataType<?>, Object, Object> innerType) {
diff --git a/server/src/test/java/io/crate/types/ObjectTypeTest.java b/server/src/test/java/io/crate/types/ObjectTypeTest.java
index b7d1b5fe1a..e860220db5 100644
--- a/server/src/test/java/io/crate/types/ObjectTypeTest.java
+++ b/server/src/test/java/io/crate/types/ObjectTypeTest.java
@@ -233,4 +233,16 @@ public class ObjectTypeTest extends DataTypeTestCase<Map<String, Object>> {
         );
         assertThat(valueBytes).isEqualTo(2504L);
     }
+
+    @Test
+    public void test_valueForInsert_on_nested_object() {
+        Map<String, Object> map = new HashMap<>();
+        map.put("c", "abcd");
+        var type = ObjectType.of(ColumnPolicy.DYNAMIC)
+            .setInnerType("c", CharacterType.of(3))
+            .build();
+        assertThatThrownBy(() -> type.valueForInsert(map))
+            .isExactlyInstanceOf(ConversionException.class)
+            .hasMessage("Cannot cast object element `c` with value `abcd` to type `text(3)`");
+    }
 }

```
