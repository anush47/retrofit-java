# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (2): ['io.crate.netty.AccountedByteBufTest#test_delegate_direct_buffer_throws_cbe_on_OOM', 'io.crate.netty.AccountedByteBufTest#test_single_buffer_cant_exceed_given_threshold']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.netty.AccountedByteBufTest']
  - io.crate.netty.AccountedByteBufTest#test_delegate_direct_buffer_throws_cbe_on_OOM: baseline=absent, patched=passed
  - io.crate.netty.AccountedByteBufTest#test_single_buffer_cant_exceed_given_threshold: baseline=absent, patched=passed
