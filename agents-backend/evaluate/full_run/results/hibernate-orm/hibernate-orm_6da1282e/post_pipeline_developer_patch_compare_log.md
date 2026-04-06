# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java']
- Developer Java files: ['hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java']
- Overlap Java files: ['hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java']

## File State Comparison
- Compared files: ['hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java']
- Mismatched files: ['hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -33,10 +33,10 @@
 
 	@Override
 	public CharSequence subSequence(int start, int end) {
-		if ( start < 0 || start >= length ) {
+		if ( start < 0 || start > length ) {
 			throw new StringIndexOutOfBoundsException( start );
 		}
-		if ( end > length ) {
+		if ( end < start || end > length ) {
 			throw new StringIndexOutOfBoundsException( end );
 		}
 		return sequence.subSequence( this.start + start, this.start + end );

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,13 +1 @@-@@ -33,10 +33,10 @@
- 
- 	@Override
- 	public CharSequence subSequence(int start, int end) {
--		if ( start < 0 || start >= length ) {
-+		if ( start < 0 || start > length ) {
- 			throw new StringIndexOutOfBoundsException( start );
- 		}
--		if ( end > length ) {
-+		if ( end < start || end > length ) {
- 			throw new StringIndexOutOfBoundsException( end );
- 		}
- 		return sequence.subSequence( this.start + start, this.start + end );
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
diff --git a/hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java b/hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java
index f670f73be4..eacf855b5b 100644
--- a/hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java
+++ b/hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java
@@ -33,10 +33,10 @@ public char charAt(int index) {
 
 	@Override
 	public CharSequence subSequence(int start, int end) {
-		if ( start < 0 || start >= length ) {
+		if ( start < 0 || start > length ) {
 			throw new StringIndexOutOfBoundsException( start );
 		}
-		if ( end > length ) {
+		if ( end < start || end > length ) {
 			throw new StringIndexOutOfBoundsException( end );
 		}
 		return sequence.subSequence( this.start + start, this.start + end );
diff --git a/hibernate-core/src/test/java/org/hibernate/internal/util/SubSequenceTest.java b/hibernate-core/src/test/java/org/hibernate/internal/util/SubSequenceTest.java
new file mode 100644
index 0000000000..9aa0e18bbb
--- /dev/null
+++ b/hibernate-core/src/test/java/org/hibernate/internal/util/SubSequenceTest.java
@@ -0,0 +1,29 @@
+/*
+ * SPDX-License-Identifier: Apache-2.0
+ * Copyright Red Hat Inc. and Hibernate Authors
+ */
+package org.hibernate.internal.util;
+
+import org.junit.jupiter.api.Test;
+
+import static org.assertj.core.api.Assertions.assertThat;
+import static org.assertj.core.api.Assertions.assertThatThrownBy;
+
+public class SubSequenceTest {
+	@Test
+	public void subSequenceAllowsEmptyAtEnd() {
+		CharSequence sequence = new SubSequence("abc", 0, 3);
+		CharSequence empty = sequence.subSequence(3, 3);
+
+		assertThat(empty.toString()).isEmpty();
+		assertThat(empty.length()).isZero();
+	}
+
+	@Test
+	public void subSequenceRejectsEndBeforeStart() {
+		CharSequence sequence = new SubSequence("abc", 0, 3);
+
+		assertThatThrownBy(() -> sequence.subSequence(2, 1))
+				.isInstanceOf(StringIndexOutOfBoundsException.class);
+	}
+}

```
