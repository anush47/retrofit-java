# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (19): ['io.crate.integrationtests.CorrelatedSubqueryITest#test_can_mix_correlated_subquery_and_sub_select', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_can_mix_correlated_subquery_and_sub_selects_with_sub_select', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_can_use_column_in_query_paired_with_correlation_that_is_not_selected', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_can_use_correlated_subquery_in_where_clause', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_can_use_outer_column_in_where_clause', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_together_with_join', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_used_in_virtual_table_with_union', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_with_join_on_primary_key', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_within_case_using_outer_column_in_where_clause', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_without_table_alias_within_join_condition', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_without_table_alias_within_join_condition_and_additional_condition', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_multiple_correlated_subqueries_in_selectlist', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_query_fails_if_correlated_subquery_returns_more_than_1_row', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_scalar_in_projection_with_correlated_sub_query', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_simple_correlated_subquery', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_simple_correlated_subquery_with_order_by', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_simple_correlated_subquery_with_user_table_as_input', 'io.crate.integrationtests.CorrelatedSubqueryITest#test_where_exists_with_correlated_subquery', 'io.crate.planner.operators.SubQueryResultsTest#test_merges_values_of_both_sides']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.integrationtests.CorrelatedSubqueryITest', 'io.crate.planner.operators.SubQueryResultsTest']
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_can_mix_correlated_subquery_and_sub_select: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_can_mix_correlated_subquery_and_sub_selects_with_sub_select: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_can_use_column_in_query_paired_with_correlation_that_is_not_selected: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_can_use_correlated_subquery_in_where_clause: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_can_use_outer_column_in_where_clause: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_together_with_join: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_used_in_virtual_table_with_union: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_with_join_on_primary_key: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_within_case_using_outer_column_in_where_clause: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_without_table_alias_within_join_condition: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_without_table_alias_within_join_condition_and_additional_condition: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_multiple_correlated_subqueries_in_selectlist: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_query_fails_if_correlated_subquery_returns_more_than_1_row: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_scalar_in_projection_with_correlated_sub_query: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_simple_correlated_subquery: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_simple_correlated_subquery_with_order_by: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_simple_correlated_subquery_with_user_table_as_input: baseline=absent, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_where_exists_with_correlated_subquery: baseline=absent, patched=passed
  - io.crate.planner.operators.SubQueryResultsTest#test_merges_values_of_both_sides: baseline=absent, patched=passed
