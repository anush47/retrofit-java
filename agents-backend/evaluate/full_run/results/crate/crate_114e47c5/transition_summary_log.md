# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.integrationtests.AnalyzeITest#test_analyze_statement_refreshes_table_stats_and_stats_are_visible_in_pg_class_and_pg_stats_also_after_restart']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.integrationtests.AnalyzeITest']
  - io.crate.integrationtests.AnalyzeITest#test_analyze_statement_refreshes_table_stats_and_stats_are_visible_in_pg_class_and_pg_stats_also_after_restart: baseline=failed, patched=passed
  - io.crate.integrationtests.AnalyzeITest#test_analyze_statement_works_on_tables_with_object_arrays: baseline=passed, patched=passed
  - io.crate.integrationtests.AnalyzeITest#test_analyze_works_on_data_with_different_type_than_defined: baseline=passed, patched=passed
  - io.crate.integrationtests.AnalyzeITest#test_select_from_pg_stats_when_most_common_vals_is_array_type_value: baseline=passed, patched=passed
