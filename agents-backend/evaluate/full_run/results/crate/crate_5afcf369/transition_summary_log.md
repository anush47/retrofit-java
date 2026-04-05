# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.protocols.postgres.DelayableWriteChannelTest#test_can_add_and_unblock_from_different_threads']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.protocols.postgres.DelayableWriteChannelTest']
  - io.crate.protocols.postgres.DelayableWriteChannelTest#test_can_add_and_unblock_from_different_threads: baseline=failed, patched=passed
  - io.crate.protocols.postgres.DelayableWriteChannelTest#test_delayed_writes_are_released_on_close: baseline=passed, patched=passed
