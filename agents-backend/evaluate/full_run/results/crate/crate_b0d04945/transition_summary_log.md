# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (15): ['io.crate.session.SessionTest#testDeallocateAllClearsAllPortalsAndPreparedStatements', 'io.crate.session.SessionTest#testDeallocatePreparedStatementClearsPreparedStatement', 'io.crate.session.SessionTest#testProperCleanupOnSessionClose', 'io.crate.session.SessionTest#test_binding_with_removed_prepared_statement_throws_sstatement_not_found_and_logs_error', 'io.crate.session.SessionTest#test_bulk_operations_result_in_jobslog_entries', 'io.crate.session.SessionTest#test_can_describe_cursor_created_using_declare', 'io.crate.session.SessionTest#test_closing_a_statement_closes_related_portals', 'io.crate.session.SessionTest#test_discard_all_discards_all_portals_and_prepared_statements', 'io.crate.session.SessionTest#test_flush_triggers_deferred_executions_and_sets_active_execution', 'io.crate.session.SessionTest#test_getParamType_returns_types_infered_from_statement', 'io.crate.session.SessionTest#test_kills_query_if_not_completed_within_statement_timeout', 'io.crate.session.SessionTest#test_out_of_bounds_getParamType_fails', 'io.crate.session.SessionTest#test_parsing_throws_an_error_on_exceeding_statement_timeout', 'io.crate.session.SessionTest#test_select_query_executed_on_session_execute_method', 'io.crate.session.SessionTest#test_statement_timeout_previous_statement_time_is_not_accounted_for']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.session.SessionTest']
  - io.crate.session.SessionTest#testDeallocateAllClearsAllPortalsAndPreparedStatements: baseline=absent, patched=passed
  - io.crate.session.SessionTest#testDeallocatePreparedStatementClearsPreparedStatement: baseline=absent, patched=passed
  - io.crate.session.SessionTest#testProperCleanupOnSessionClose: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_binding_with_removed_prepared_statement_throws_sstatement_not_found_and_logs_error: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_bulk_operations_result_in_jobslog_entries: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_can_describe_cursor_created_using_declare: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_closing_a_statement_closes_related_portals: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_discard_all_discards_all_portals_and_prepared_statements: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_flush_triggers_deferred_executions_and_sets_active_execution: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_getParamType_returns_types_infered_from_statement: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_kills_query_if_not_completed_within_statement_timeout: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_out_of_bounds_getParamType_fails: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_parsing_throws_an_error_on_exceeding_statement_timeout: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_select_query_executed_on_session_execute_method: baseline=absent, patched=passed
  - io.crate.session.SessionTest#test_statement_timeout_previous_statement_time_is_not_accounted_for: baseline=absent, patched=passed
