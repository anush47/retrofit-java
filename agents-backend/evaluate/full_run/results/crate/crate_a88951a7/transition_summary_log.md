# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.integrationtests.AggregateExpressionIntegrationTest#test_assure_cmp_by_function_call_with_reference_and_literal_does_not_throw_exception']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.integrationtests.AggregateExpressionIntegrationTest']
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_aggregation_in_order_by_without_having_them_in_the_select_list: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_assure_cmp_by_function_call_with_reference_and_literal_does_not_throw_exception: baseline=error, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_filter_in_aggregate_expr_for_global_aggregate: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_filter_in_aggregate_expr_with_group_by: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_filter_in_aggregate_expr_with_group_by_column_with_nulls: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_filter_in_aggregate_expr_with_group_by_single_number: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_filter_in_aggregate_expr_with_group_by_single_numeric_column_with_nulls: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_filter_in_count_star_aggregate_function: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_filter_with_group_by_low_cardinality_text_field: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_filter_with_subquery_in_aggregate_expr_for_global_aggregate: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_filter_with_subquery_in_aggregate_expr_for_group_by_aggregates: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_interval_avg: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_min_and_max_by: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_numeric_agg_with_numeric_cast: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_numeric_avg_with_on_floating_point_and_long_columns_with_doc_values: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_numeric_sum_with_on_floating_point_and_long_columns_with_doc_values: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_sum_int: baseline=passed, patched=passed
  - io.crate.integrationtests.AggregateExpressionIntegrationTest#test_sum_interval: baseline=passed, patched=passed
