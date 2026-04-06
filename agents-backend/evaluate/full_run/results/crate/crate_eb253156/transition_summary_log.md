# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.execution.dml.upsert.TransportShardUpsertActionTest#test_primary_aborted_remaining_items_must_be_skipped_on_replica']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.dml.upsert.TransportShardUpsertActionTest']
  - io.crate.execution.dml.upsert.TransportShardUpsertActionTest#testExceptionWhileProcessingItemsContinueOnError: baseline=passed, patched=passed
  - io.crate.execution.dml.upsert.TransportShardUpsertActionTest#testExceptionWhileProcessingItemsNotContinueOnError: baseline=passed, patched=passed
  - io.crate.execution.dml.upsert.TransportShardUpsertActionTest#testItemsWithoutSourceAreSkippedOnReplicaOperation: baseline=passed, patched=passed
  - io.crate.execution.dml.upsert.TransportShardUpsertActionTest#testKilledSetWhileProcessingItemsDoesNotThrowException: baseline=passed, patched=passed
  - io.crate.execution.dml.upsert.TransportShardUpsertActionTest#test_dynamic_insert_of_integer_upcasted_to_long_can_be_replicated: baseline=passed, patched=passed
  - io.crate.execution.dml.upsert.TransportShardUpsertActionTest#test_primary_aborted_remaining_items_must_be_skipped_on_replica: baseline=failed, patched=passed
