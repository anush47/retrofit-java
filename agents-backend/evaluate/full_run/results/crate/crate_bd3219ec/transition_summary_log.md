# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.rest.action.RestActionReceiversTest#test_result_reciever_future_is_not_completed_on_cbe']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.rest.action.RestActionReceiversTest']
  - io.crate.rest.action.RestActionReceiversTest#testRestBulkRowCountReceiver: baseline=passed, patched=passed
  - io.crate.rest.action.RestActionReceiversTest#testRestResultSetReceiver: baseline=passed, patched=passed
  - io.crate.rest.action.RestActionReceiversTest#testRestRowCountReceiver: baseline=passed, patched=passed
  - io.crate.rest.action.RestActionReceiversTest#test_rest_bulk_row_count_receiver_supports_single_column_row_on_single_bulk_arg: baseline=passed, patched=passed
  - io.crate.rest.action.RestActionReceiversTest#test_result_reciever_future_is_not_completed_on_cbe: baseline=failed, patched=passed
