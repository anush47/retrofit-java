# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (1): ['io.crate.execution.engine.FirstColumnConsumersTest#test_accounting_for_all_consumer']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.engine.FirstColumnConsumersTest']
  - io.crate.execution.engine.FirstColumnConsumersTest#test_accounting_for_all_consumer: baseline=absent, patched=passed
