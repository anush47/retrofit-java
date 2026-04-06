# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.expression.InputFactoryTest#test_missing_reference']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.expression.InputFactoryTest']
  - io.crate.expression.InputFactoryTest#testAggregationSymbolsInputReuse: baseline=passed, patched=passed
  - io.crate.expression.InputFactoryTest#testCompiled: baseline=passed, patched=passed
  - io.crate.expression.InputFactoryTest#testProcessGroupByProjectionSymbols: baseline=passed, patched=passed
  - io.crate.expression.InputFactoryTest#testProcessGroupByProjectionSymbolsAggregation: baseline=passed, patched=passed
  - io.crate.expression.InputFactoryTest#testSameReferenceResultsInSameExpressionInstance: baseline=passed, patched=passed
  - io.crate.expression.InputFactoryTest#test_missing_reference: baseline=failed, patched=passed
