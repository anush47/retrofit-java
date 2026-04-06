# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.planner.ViewPlannerTest#test_push_filter_beyond_view_with_aliased_column']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.planner.ViewPlannerTest']
  - io.crate.planner.ViewPlannerTest#test_doc_table_operations_raise_helpful_error_on_views: baseline=passed, patched=passed
  - io.crate.planner.ViewPlannerTest#test_push_filter_beyond_view_with_aliased_column: baseline=failed, patched=passed
  - io.crate.planner.ViewPlannerTest#test_view_of_join_condition_containing_subscript_expressions: baseline=passed, patched=passed
