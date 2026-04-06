# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_array_position']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.lucene.ThreeValuedLogicQueryBuilderTest']
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#testComplexOperatorTreeWith3vlAndIgnore3vl: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#testNotAnyEqWith3vl: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#testNotAnyEqWithout3vl: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#testNullIsReplacedWithFalseToCreateOptimizedQuery: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_and_three_value_query: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_cast_on_object: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_concat_with_three_valued_logic: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_concat_ws_with_three_valued_logic: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_format_type_with_three_valued_logic: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_or: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_array_position: baseline=failed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_current_setting: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_has_privilege_functions: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_pg_encoding_to_char: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_pg_get_function_result: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_pg_get_partkeydef: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_nullif: baseline=passed, patched=passed
