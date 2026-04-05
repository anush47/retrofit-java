# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (1): ['io.crate.execution.engine.indexing.ShardUpsertExecutorTest#test_will_pause_on_memory_threshold_with_unknown_target_rtt']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.engine.indexing.ShardUpsertExecutorTest']
  - io.crate.execution.engine.indexing.ShardUpsertExecutorTest#test_will_pause_on_memory_threshold_with_unknown_target_rtt: baseline=absent, patched=passed
