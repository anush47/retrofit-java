# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (25): ['io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnEqWithoutRelationFieldsOnBothSides', 'io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnInnerContainingEqOrAnyCondition', 'io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnInnerWithEqAndScalarOnMultipleRelations', 'io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnInnerWithoutAnyEqCondition', 'io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnNotWrappingEq', 'io.crate.planner.operators.EquiJoinDetectorTest#testPossibleOnInnerContainingEqAndAnyCondition', 'io.crate.planner.operators.EquiJoinDetectorTest#testPossibleOnInnerContainingEqCondition', 'io.crate.planner.operators.EquiJoinDetectorTest#testPossibleOnInnerWithEqAndScalarOnOneRelation', 'io.crate.planner.operators.EquiJoinDetectorTest#test_case_expression_with_nested_equality', 'io.crate.planner.operators.EquiJoinDetectorTest#test_detect_pure_equi_join', 'io.crate.planner.operators.EquiJoinDetectorTest#test_equality_and_many_relations_in_boolean_join_condition_hash_join_not_possible', 'io.crate.planner.operators.EquiJoinDetectorTest#test_equality_condition_inside_cast', 'io.crate.planner.operators.EquiJoinDetectorTest#test_equality_expression_followed_by_case_expression', 'io.crate.planner.operators.EquiJoinDetectorTest#test_if_expression_with_nested_equality', 'io.crate.planner.operators.EquiJoinDetectorTest#test_inequality_in_boolean_join_condition_hash_join_possible', 'io.crate.planner.operators.EquiJoinDetectorTest#test_not_hash_join_possible_if_join_condition_refers_to_columns_from_a_single_relation', 'io.crate.planner.operators.EquiJoinDetectorTest#test_or_in_boolean_join_condition_hash_join_possible', 'io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_complex_equi_join_conditions_are_not_supported', 'io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_filter_on_larger_side', 'io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_filter_on_smaller_side', 'io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_lookup_join_lhs_is_larger', 'io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_lookup_join_rhs_is_larger', 'io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_skip_if_source_is_not_a_collect', 'io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_skip_no_stats', 'io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_skip_non_equi_joins']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.planner.operators.EquiJoinDetectorTest', 'io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest']
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnEqWithoutRelationFieldsOnBothSides: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnInnerContainingEqOrAnyCondition: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnInnerWithEqAndScalarOnMultipleRelations: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnInnerWithoutAnyEqCondition: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnNotWrappingEq: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testPossibleOnInnerContainingEqAndAnyCondition: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testPossibleOnInnerContainingEqCondition: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testPossibleOnInnerWithEqAndScalarOnOneRelation: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_case_expression_with_nested_equality: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_detect_pure_equi_join: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_equality_and_many_relations_in_boolean_join_condition_hash_join_not_possible: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_equality_condition_inside_cast: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_equality_expression_followed_by_case_expression: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_if_expression_with_nested_equality: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_inequality_in_boolean_join_condition_hash_join_possible: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_not_hash_join_possible_if_join_condition_refers_to_columns_from_a_single_relation: baseline=absent, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_or_in_boolean_join_condition_hash_join_possible: baseline=absent, patched=passed
  - io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_complex_equi_join_conditions_are_not_supported: baseline=absent, patched=passed
  - io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_filter_on_larger_side: baseline=absent, patched=passed
  - io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_filter_on_smaller_side: baseline=absent, patched=passed
  - io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_lookup_join_lhs_is_larger: baseline=absent, patched=passed
  - io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_lookup_join_rhs_is_larger: baseline=absent, patched=passed
  - io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_skip_if_source_is_not_a_collect: baseline=absent, patched=passed
  - io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_skip_no_stats: baseline=absent, patched=passed
  - io.crate.planner.optimizer.rule.EquiJoinToLookupJoinTest#test_skip_non_equi_joins: baseline=absent, patched=passed
