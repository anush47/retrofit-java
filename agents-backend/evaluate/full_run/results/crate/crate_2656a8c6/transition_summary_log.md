# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.lucene.NestedArrayLuceneQueryBuilderTest#test_subscript_nested_array_equals']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.lucene.NestedArrayLuceneQueryBuilderTest']
  - io.crate.lucene.NestedArrayLuceneQueryBuilderTest#test_empty_nested_array_equals: baseline=passed, patched=passed
  - io.crate.lucene.NestedArrayLuceneQueryBuilderTest#test_nested_array_equals: baseline=passed, patched=passed
  - io.crate.lucene.NestedArrayLuceneQueryBuilderTest#test_subscript_nested_array_equals: baseline=error, patched=passed
