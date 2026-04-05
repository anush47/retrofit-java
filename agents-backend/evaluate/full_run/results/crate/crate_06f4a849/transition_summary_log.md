# Transition Summary

- Source: phase_outputs
- Valid backport signal: False
- Reason: Invalid: Build failed after patch apply.
- fail->pass (0): []
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.IncrementalPageBucketReceiverTest']
  - io.crate.execution.IncrementalPageBucketReceiverTest#test_processing_future_completed_when_finisher_throws: baseline=failed, patched=passed
