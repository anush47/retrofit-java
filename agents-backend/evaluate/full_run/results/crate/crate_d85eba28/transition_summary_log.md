# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (2): ['io.crate.planner.operators.EquiJoinDetectorTest#test_case_expression_with_nested_equality', 'io.crate.planner.operators.EquiJoinDetectorTest#test_if_expression_with_nested_equality']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.planner.operators.EquiJoinDetectorTest']
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnEqWithoutRelationFieldsOnBothSides: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnInnerContainingEqOrAnyCondition: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnInnerWithEqAndScalarOnMultipleRelations: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnInnerWithoutAnyEqCondition: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testNotPossibleOnNotWrappingEq: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testPossibleOnInnerContainingEqAndAnyCondition: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testPossibleOnInnerContainingEqCondition: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#testPossibleOnInnerWithEqAndScalarOnOneRelation: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_case_expression_with_nested_equality: baseline=failed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_equality_and_many_relations_in_boolean_join_condition_hash_join_not_possible: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_equality_condition_inside_cast: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_equality_expression_followed_by_case_expression: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_if_expression_with_nested_equality: baseline=failed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_inequality_in_boolean_join_condition_hash_join_possible: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_not_hash_join_possible_if_join_condition_refers_to_columns_from_a_single_relation: baseline=passed, patched=passed
  - io.crate.planner.operators.EquiJoinDetectorTest#test_or_in_boolean_join_condition_hash_join_possible: baseline=passed, patched=passed
