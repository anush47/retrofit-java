# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (2): ['io.crate.expression.predicate.FieldExistsQueryTest#test_not_function_does_not_match_empty_objects', 'io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_cast_on_object']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.expression.predicate.FieldExistsQueryTest', 'io.crate.lucene.ThreeValuedLogicQueryBuilderTest']
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_not_null_does_not_match_empty_arrays: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_not_null_does_not_match_empty_arrays_with_index_and_column_store_off: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_not_null_does_not_match_empty_arrays_with_index_off: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_not_null_matches_empty_objects: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_null_does_not_match_empty_arrays: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_null_does_not_match_empty_arrays_with_index_and_column_store_off: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_null_does_not_match_empty_arrays_with_index_off: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_null_does_not_match_empty_objects: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_null_on_columns_without_doc_values: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_is_null_with_values_on_geo_shape_array: baseline=passed, patched=passed
  - io.crate.expression.predicate.FieldExistsQueryTest#test_not_function_does_not_match_empty_objects: baseline=failed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#testComplexOperatorTreeWith3vlAndIgnore3vl: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#testNotAnyEqWith3vl: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#testNotAnyEqWithout3vl: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#testNullIsReplacedWithFalseToCreateOptimizedQuery: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_and_three_value_query: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_cast_on_object: baseline=failed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_concat_with_three_valued_logic: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_concat_ws_with_three_valued_logic: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_format_type_with_three_valued_logic: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_negated_or: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_current_setting: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_has_privilege_functions: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_pg_encoding_to_char: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_pg_get_function_result: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_not_on_pg_get_partkeydef: baseline=passed, patched=passed
  - io.crate.lucene.ThreeValuedLogicQueryBuilderTest#test_nullif: baseline=passed, patched=passed
