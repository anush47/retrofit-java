# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: True

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java']
- Developer Java files: ['server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java']
- Overlap Java files: ['server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java']
- Mismatched files: []
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java

- Developer hunks: 3
- Generated hunks: 3

#### Hunk 1

Developer
```diff
@@ -27,6 +27,8 @@
 import java.io.IOException;
 import java.io.InputStream;
 import java.io.UncheckedIOException;
+import java.math.BigDecimal;
+import java.math.BigInteger;
 import java.util.ArrayList;
 import java.util.BitSet;
 import java.util.HashMap;

```

Generated
```diff
@@ -27,6 +27,8 @@
 import java.io.IOException;
 import java.io.InputStream;
 import java.io.UncheckedIOException;
+import java.math.BigDecimal;
+import java.math.BigInteger;
 import java.util.ArrayList;
 import java.util.BitSet;
 import java.util.HashMap;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -288,7 +290,7 @@
             case START_ARRAY -> parseArray(parser, type, requiredColumns, colPath);
             case START_OBJECT -> parseObject(parser, requiredColumns, colPath, includeUnknown);
             case VALUE_STRING -> isUndefined(type) ? parser.text() : parseByType(parser, type);
-            case VALUE_NUMBER -> isUndefined(type) ? parser.numberValue() : parseByType(parser, type);
+            case VALUE_NUMBER -> isUndefined(type) ? numberValue(parser.numberValue()) : parseByType(parser, type);
             case VALUE_BOOLEAN -> isUndefined(type) ? parser.booleanValue() : parseByType(parser, type);
             case VALUE_EMBEDDED_OBJECT -> isUndefined(type) ? parser.binaryValue() : parseByType(parser, type);
             default -> throw new UnsupportedOperationException("Unsupported token encountered, expected a value, got "

```

Generated
```diff
@@ -288,7 +290,7 @@
             case START_ARRAY -> parseArray(parser, type, requiredColumns, colPath);
             case START_OBJECT -> parseObject(parser, requiredColumns, colPath, includeUnknown);
             case VALUE_STRING -> isUndefined(type) ? parser.text() : parseByType(parser, type);
-            case VALUE_NUMBER -> isUndefined(type) ? parser.numberValue() : parseByType(parser, type);
+            case VALUE_NUMBER -> isUndefined(type) ? numberValue(parser.numberValue()) : parseByType(parser, type);
             case VALUE_BOOLEAN -> isUndefined(type) ? parser.booleanValue() : parseByType(parser, type);
             case VALUE_EMBEDDED_OBJECT -> isUndefined(type) ? parser.binaryValue() : parseByType(parser, type);
             default -> throw new UnsupportedOperationException("Unsupported token encountered, expected a value, got "

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 3

Developer
```diff
@@ -296,6 +298,20 @@
         };
     }
 
+    /**
+     * For the undefined case, Number's concrete types is guessed by the parser.
+     * ParserBase.getNumberValue always returns BigInteger for integral big numbers.
+     * We must use BigDecimal for NUMERIC even for integral values, otherwise streaming will be broken.
+     * @param number is a Number returned by the parser.
+     */
+    private static Number numberValue(Number number) {
+        if (number instanceof BigInteger bigInt) {
+            return new BigDecimal(bigInt);
+        }
+        return number;
+    }
+
+
     private static boolean isUndefined(@Nullable DataType<?> type) {
         return type == null || type.id() == DataTypes.UNDEFINED.id();
     }

```

Generated
```diff
@@ -296,6 +298,20 @@
         };
     }
 
+    /**
+     * For the undefined case, Number's concrete types is guessed by the parser.
+     * ParserBase.getNumberValue always returns BigInteger for integral big numbers.
+     * We must use BigDecimal for NUMERIC even for integral values, otherwise streaming will be broken.
+     * @param number is a Number returned by the parser.
+     */
+    private static Number numberValue(Number number) {
+        if (number instanceof BigInteger bigInt) {
+            return new BigDecimal(bigInt);
+        }
+        return number;
+    }
+
+
     private static boolean isUndefined(@Nullable DataType<?> type) {
         return type == null || type.id() == DataTypes.UNDEFINED.id();
     }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java b/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java
index b3f57a89c1..d7e77b924f 100644
--- a/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java
+++ b/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java
@@ -27,6 +27,8 @@ import static org.elasticsearch.common.xcontent.XContentParser.Token.VALUE_NULL;
 import java.io.IOException;
 import java.io.InputStream;
 import java.io.UncheckedIOException;
+import java.math.BigDecimal;
+import java.math.BigInteger;
 import java.util.ArrayList;
 import java.util.BitSet;
 import java.util.HashMap;
@@ -288,7 +290,7 @@ public final class SourceParser {
             case START_ARRAY -> parseArray(parser, type, requiredColumns, colPath);
             case START_OBJECT -> parseObject(parser, requiredColumns, colPath, includeUnknown);
             case VALUE_STRING -> isUndefined(type) ? parser.text() : parseByType(parser, type);
-            case VALUE_NUMBER -> isUndefined(type) ? parser.numberValue() : parseByType(parser, type);
+            case VALUE_NUMBER -> isUndefined(type) ? numberValue(parser.numberValue()) : parseByType(parser, type);
             case VALUE_BOOLEAN -> isUndefined(type) ? parser.booleanValue() : parseByType(parser, type);
             case VALUE_EMBEDDED_OBJECT -> isUndefined(type) ? parser.binaryValue() : parseByType(parser, type);
             default -> throw new UnsupportedOperationException("Unsupported token encountered, expected a value, got "
@@ -296,6 +298,20 @@ public final class SourceParser {
         };
     }
 
+    /**
+     * For the undefined case, Number's concrete types is guessed by the parser.
+     * ParserBase.getNumberValue always returns BigInteger for integral big numbers.
+     * We must use BigDecimal for NUMERIC even for integral values, otherwise streaming will be broken.
+     * @param number is a Number returned by the parser.
+     */
+    private static Number numberValue(Number number) {
+        if (number instanceof BigInteger bigInt) {
+            return new BigDecimal(bigInt);
+        }
+        return number;
+    }
+
+
     private static boolean isUndefined(@Nullable DataType<?> type) {
         return type == null || type.id() == DataTypes.UNDEFINED.id();
     }

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java b/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java
index b3f57a89c1..d7e77b924f 100644
--- a/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java
+++ b/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java
@@ -27,6 +27,8 @@ import static org.elasticsearch.common.xcontent.XContentParser.Token.VALUE_NULL;
 import java.io.IOException;
 import java.io.InputStream;
 import java.io.UncheckedIOException;
+import java.math.BigDecimal;
+import java.math.BigInteger;
 import java.util.ArrayList;
 import java.util.BitSet;
 import java.util.HashMap;
@@ -288,7 +290,7 @@ public final class SourceParser {
             case START_ARRAY -> parseArray(parser, type, requiredColumns, colPath);
             case START_OBJECT -> parseObject(parser, requiredColumns, colPath, includeUnknown);
             case VALUE_STRING -> isUndefined(type) ? parser.text() : parseByType(parser, type);
-            case VALUE_NUMBER -> isUndefined(type) ? parser.numberValue() : parseByType(parser, type);
+            case VALUE_NUMBER -> isUndefined(type) ? numberValue(parser.numberValue()) : parseByType(parser, type);
             case VALUE_BOOLEAN -> isUndefined(type) ? parser.booleanValue() : parseByType(parser, type);
             case VALUE_EMBEDDED_OBJECT -> isUndefined(type) ? parser.binaryValue() : parseByType(parser, type);
             default -> throw new UnsupportedOperationException("Unsupported token encountered, expected a value, got "
@@ -296,6 +298,20 @@ public final class SourceParser {
         };
     }
 
+    /**
+     * For the undefined case, Number's concrete types is guessed by the parser.
+     * ParserBase.getNumberValue always returns BigInteger for integral big numbers.
+     * We must use BigDecimal for NUMERIC even for integral values, otherwise streaming will be broken.
+     * @param number is a Number returned by the parser.
+     */
+    private static Number numberValue(Number number) {
+        if (number instanceof BigInteger bigInt) {
+            return new BigDecimal(bigInt);
+        }
+        return number;
+    }
+
+
     private static boolean isUndefined(@Nullable DataType<?> type) {
         return type == null || type.id() == DataTypes.UNDEFINED.id();
     }

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java b/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java
index b3f57a89c1..d7e77b924f 100644
--- a/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java
+++ b/server/src/main/java/io/crate/expression/reference/doc/lucene/SourceParser.java
@@ -27,6 +27,8 @@ import static org.elasticsearch.common.xcontent.XContentParser.Token.VALUE_NULL;
 import java.io.IOException;
 import java.io.InputStream;
 import java.io.UncheckedIOException;
+import java.math.BigDecimal;
+import java.math.BigInteger;
 import java.util.ArrayList;
 import java.util.BitSet;
 import java.util.HashMap;
@@ -288,7 +290,7 @@ public final class SourceParser {
             case START_ARRAY -> parseArray(parser, type, requiredColumns, colPath);
             case START_OBJECT -> parseObject(parser, requiredColumns, colPath, includeUnknown);
             case VALUE_STRING -> isUndefined(type) ? parser.text() : parseByType(parser, type);
-            case VALUE_NUMBER -> isUndefined(type) ? parser.numberValue() : parseByType(parser, type);
+            case VALUE_NUMBER -> isUndefined(type) ? numberValue(parser.numberValue()) : parseByType(parser, type);
             case VALUE_BOOLEAN -> isUndefined(type) ? parser.booleanValue() : parseByType(parser, type);
             case VALUE_EMBEDDED_OBJECT -> isUndefined(type) ? parser.binaryValue() : parseByType(parser, type);
             default -> throw new UnsupportedOperationException("Unsupported token encountered, expected a value, got "
@@ -296,6 +298,20 @@ public final class SourceParser {
         };
     }
 
+    /**
+     * For the undefined case, Number's concrete types is guessed by the parser.
+     * ParserBase.getNumberValue always returns BigInteger for integral big numbers.
+     * We must use BigDecimal for NUMERIC even for integral values, otherwise streaming will be broken.
+     * @param number is a Number returned by the parser.
+     */
+    private static Number numberValue(Number number) {
+        if (number instanceof BigInteger bigInt) {
+            return new BigDecimal(bigInt);
+        }
+        return number;
+    }
+
+
     private static boolean isUndefined(@Nullable DataType<?> type) {
         return type == null || type.id() == DataTypes.UNDEFINED.id();
     }
diff --git a/server/src/test/java/io/crate/expression/reference/doc/lucene/SourceParserTest.java b/server/src/test/java/io/crate/expression/reference/doc/lucene/SourceParserTest.java
index 15c4236f5e..93ef60337a 100644
--- a/server/src/test/java/io/crate/expression/reference/doc/lucene/SourceParserTest.java
+++ b/server/src/test/java/io/crate/expression/reference/doc/lucene/SourceParserTest.java
@@ -24,6 +24,7 @@ package io.crate.expression.reference.doc.lucene;
 import static io.crate.testing.TestingHelpers.createReference;
 import static org.assertj.core.api.Assertions.assertThat;
 
+import java.math.BigDecimal;
 import java.util.HashMap;
 import java.util.List;
 import java.util.Map;
@@ -527,4 +528,21 @@ public class SourceParserTest extends ESTestCase {
 
         assertThat(result.get("x")).isNull();
     }
+
+    @Test
+    public void test_ignored_object_with_big_integral_number_is_parsed_as_bigdecimal() throws Exception {
+        SourceParser sourceParser = new SourceParser(Set.of(), UnaryOperator.identity(), true);
+        ObjectType objectType = ObjectType.of(ColumnPolicy.IGNORED).build();
+        sourceParser.register(ColumnIdent.of("_doc", List.of("o")), objectType);
+        Map<String, Object> result = sourceParser.parse(new BytesArray(
+            """
+                {
+                    "o": {
+                        "x": 30000000000000000000000000000000
+                    }
+                }
+            """
+        ));
+        assertThat(Maps.getByPath(result, "o.x")).isInstanceOf(BigDecimal.class);
+    }
 }

```
