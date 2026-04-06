# Phase 0 Inputs

- Mainline commit: 6da1282e7030eb4539a31783172c75c9d04ca568
- Backport commit: eafaf38201a0fcaa5e20c448b1ec21531be697a4
- Java-only files for agentic phases: 1
- Developer auxiliary hunks (test + non-Java): 1

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java']
- Developer Java files: ['hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java']
- Overlap Java files: ['hibernate-core/src/main/java/org/hibernate/internal/util/SubSequence.java']
- Overlap ratio (mainline): 1.0

## Mainline Patch
```diff
From 6da1282e7030eb4539a31783172c75c9d04ca568 Mon Sep 17 00:00:00 2001
From: Terry Tao <yueyang.tao@gmail.com>
Date: Sun, 4 Jan 2026 04:34:10 -0500
Subject: [PATCH] HHH-20032: Fix SubSequence.subSequence bounds checks

SubSequence implements CharSequence but rejected the valid boundary case
start == end == length()
by throwing StringIndexOutOfBoundsException when
start == length.

Relax the start bound check to allow
start == length
and add validation for
end < start
to match the CharSequence contract.

Add a regression test.
---
 .../hibernate/internal/util/SubSequence.java  |  4 +--
 .../internal/util/SubSequenceTest.java        | 29 +++++++++++++++++++
 2 files changed, 31 insertions(+), 2 deletions(-)
 create mode 100644 hibernate-core/src/test/java/org/hibernate/internal/util/SubSequenceTest.java

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
-- 
2.43.0


```
