# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.session.SessionTest#test_statement_timeout_schedule_is_removed_for_finished_jobs']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.session.SessionTest']
  - io.crate.session.SessionTest#testDeallocateAllClearsAllPortalsAndPreparedStatements: baseline=passed, patched=passed
  - io.crate.session.SessionTest#testDeallocatePreparedStatementClearsPreparedStatement: baseline=passed, patched=passed
  - io.crate.session.SessionTest#testProperCleanupOnSessionClose: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_binding_with_removed_prepared_statement_throws_sstatement_not_found_and_logs_error: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_bulk_operations_result_in_jobslog_entries: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_can_describe_cursor_created_using_declare: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_closing_a_statement_closes_related_portals: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_discard_all_discards_all_portals_and_prepared_statements: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_flush_triggers_deferred_executions_and_sets_active_execution: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_getParamType_returns_types_infered_from_statement: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_kills_query_if_not_completed_within_statement_timeout: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_out_of_bounds_getParamType_fails: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_parsing_throws_an_error_on_exceeding_statement_timeout: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_select_query_executed_on_session_execute_method: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_statement_timeout_previous_statement_time_is_not_accounted_for: baseline=passed, patched=passed
  - io.crate.session.SessionTest#test_statement_timeout_schedule_is_removed_for_finished_jobs: baseline=failed, patched=passed
