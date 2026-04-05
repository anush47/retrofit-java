# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (6): ['io.crate.rest.action.RestActionReceiversTest#testRestBulkRowCountReceiver', 'io.crate.rest.action.RestActionReceiversTest#testRestResultSetReceiver', 'io.crate.rest.action.RestActionReceiversTest#testRestRowCountReceiver', 'io.crate.rest.action.RestActionReceiversTest#test_ram_accounting_of_the_result_set_receiver', 'io.crate.rest.action.RestActionReceiversTest#test_rest_bulk_row_count_receiver_supports_single_column_row_on_single_bulk_arg', 'io.crate.rest.action.RestActionReceiversTest#test_result_receiver_future_is_not_completed_on_cbe']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.rest.action.RestActionReceiversTest']
  - io.crate.rest.action.RestActionReceiversTest#testRestBulkRowCountReceiver: baseline=absent, patched=passed
  - io.crate.rest.action.RestActionReceiversTest#testRestResultSetReceiver: baseline=absent, patched=passed
  - io.crate.rest.action.RestActionReceiversTest#testRestRowCountReceiver: baseline=absent, patched=passed
  - io.crate.rest.action.RestActionReceiversTest#test_ram_accounting_of_the_result_set_receiver: baseline=absent, patched=passed
  - io.crate.rest.action.RestActionReceiversTest#test_rest_bulk_row_count_receiver_supports_single_column_row_on_single_bulk_arg: baseline=absent, patched=passed
  - io.crate.rest.action.RestActionReceiversTest#test_result_receiver_future_is_not_completed_on_cbe: baseline=absent, patched=passed
