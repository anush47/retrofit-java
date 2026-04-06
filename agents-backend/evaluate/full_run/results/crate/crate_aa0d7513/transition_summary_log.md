# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.planner.operators.WindowAggTest#test_window_functions_do_not_support_filter_clause']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.planner.operators.WindowAggTest']
  - io.crate.planner.operators.WindowAggTest#testNoOrderByIfNoPartitionsAndNoOrderBy: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#testOrderByIsMergedWithPartitionByWithFullColumnOverlap: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#testOrderByIsMergedWithPartitionByWithNoOverlap: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#testOrderByIsMergedWithPartitionByWithPartialColumnOverlap: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#testOrderByIsMergedWithPartitionByWithPartialColumnOverlapButReverseOrder: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#testOrderByIsOverOrderByWithoutPartitions: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#testOrderByIsPartitionByWithoutExplicitOrderBy: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#testTwoWindowFunctionsWithDifferentWindowDefinitionResultsInTwoOperators: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#test_window_agg_is_removed_if_unused_in_upper_select: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#test_window_agg_output_for_select_with_standalone_ref_and_window_func_with_filter: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#test_window_agg_with_filter_that_contains_column_that_is_not_in_outputs: baseline=passed, patched=passed
  - io.crate.planner.operators.WindowAggTest#test_window_functions_do_not_support_filter_clause: baseline=failed, patched=passed
