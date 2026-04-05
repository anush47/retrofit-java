# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.execution.IncrementalPageBucketReceiverTest#test_listener_doesnt_need_more_when_processRows_throws']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.IncrementalPageBucketReceiverTest']
  - io.crate.execution.IncrementalPageBucketReceiverTest#test_listener_doesnt_need_more_when_processRows_throws: baseline=failed, patched=passed
  - io.crate.execution.IncrementalPageBucketReceiverTest#test_processing_future_completed_when_finisher_throws: baseline=passed, patched=passed
