# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.execution.engine.distribution.StreamBucketTest#test_accounting']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.engine.distribution.StreamBucketTest']
  - io.crate.execution.engine.distribution.StreamBucketTest#test_accounting: baseline=failed, patched=passed
