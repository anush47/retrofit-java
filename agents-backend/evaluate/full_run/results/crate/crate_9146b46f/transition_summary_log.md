# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (2): ['io.crate.execution.dml.delete.TransportShardDeleteActionTest#test_deletion_failed_with_non_retryable_error_must_not_throw', 'io.crate.execution.dml.delete.TransportShardDeleteActionTest#test_deletion_failed_with_retryable_error_must_throw']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.dml.delete.TransportShardDeleteActionTest']
  - io.crate.execution.dml.delete.TransportShardDeleteActionTest#testKilledSetWhileProcessingItemsDoesNotThrowExceptionAndMustMarkItemPosition: baseline=passed, patched=passed
  - io.crate.execution.dml.delete.TransportShardDeleteActionTest#testReplicaOperationWillSkipItemsFromMarkedPositionOn: baseline=passed, patched=passed
  - io.crate.execution.dml.delete.TransportShardDeleteActionTest#test_deletion_failed_with_non_retryable_error_must_not_throw: baseline=error, patched=passed
  - io.crate.execution.dml.delete.TransportShardDeleteActionTest#test_deletion_failed_with_retryable_error_must_throw: baseline=failed, patched=passed
