# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.execution.engine.aggregation.impl.TDigestStateTest#testStreaming']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.engine.aggregation.impl.TDigestStateTest']
  - io.crate.execution.engine.aggregation.impl.TDigestStateTest#testStreaming: baseline=error, patched=passed
  - io.crate.execution.engine.aggregation.impl.TDigestStateTest#testStreaming_on_or_before_6_1_1: baseline=passed, patched=passed
