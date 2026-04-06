# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.integrationtests.CorrelatedSubqueryITest#test_can_mix_correlated_qubquery_and_sub_select']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.integrationtests.CorrelatedSubqueryITest']
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_can_mix_correlated_qubquery_and_sub_select: baseline=error, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_can_use_column_in_query_paired_with_correlation_that_is_not_selected: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_can_use_correlated_subquery_in_where_clause: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_can_use_outer_column_in_where_clause: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_together_with_join: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_used_in_virtual_table_with_union: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_within_case_using_outer_column_in_where_clause: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_without_table_alias_within_join_condition: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_correlated_subquery_without_table_alias_within_join_condition_and_additional_condition: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_multiple_correlated_subqueries_in_selectlist: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_query_fails_if_correlated_subquery_returns_more_than_1_row: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_simple_correlated_subquery: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_simple_correlated_subquery_with_order_by: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_simple_correlated_subquery_with_user_table_as_input: baseline=passed, patched=passed
  - io.crate.integrationtests.CorrelatedSubqueryITest#test_where_exists_with_correlated_subquery: baseline=passed, patched=passed
