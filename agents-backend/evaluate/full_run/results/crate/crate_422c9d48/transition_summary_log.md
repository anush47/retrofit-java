# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (15): ['io.crate.analyze.SelectWindowFunctionAnalyzerTest#testAggregatesCannotAcceptIgnoreOrRespectNullsFlag', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#testEmptyOverClause', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#testInvalidOrderByField', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#testInvalidPartitionByField', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#testNonAggregateAndNonWindowFunctionCannotAcceptIgnoreOrRespectNullsFlag', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOnlyAggregatesAndWindowFunctionsAreAllowedWithOver', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOverWithFrameDefinition', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOverWithOrderByClause', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOverWithPartitionAndOrderByClauses', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOverWithPartitionByClause', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_over_references_not_defined_window', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_over_references_window_that_references_subsequent_window', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_over_with_order_by_references_window_with_partition_by', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_window_function_partition_symbols_not_in_grouping_raises_an_error', 'io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_window_function_symbols_not_in_grouping_raises_an_error']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.analyze.SelectWindowFunctionAnalyzerTest']
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testAggregatesCannotAcceptIgnoreOrRespectNullsFlag: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testEmptyOverClause: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testInvalidOrderByField: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testInvalidPartitionByField: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testNonAggregateAndNonWindowFunctionCannotAcceptIgnoreOrRespectNullsFlag: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOnlyAggregatesAndWindowFunctionsAreAllowedWithOver: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOverWithFrameDefinition: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOverWithOrderByClause: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOverWithPartitionAndOrderByClauses: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#testOverWithPartitionByClause: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_over_references_not_defined_window: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_over_references_window_that_references_subsequent_window: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_over_with_order_by_references_window_with_partition_by: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_window_function_partition_symbols_not_in_grouping_raises_an_error: baseline=absent, patched=passed
  - io.crate.analyze.SelectWindowFunctionAnalyzerTest#test_window_function_symbols_not_in_grouping_raises_an_error: baseline=absent, patched=passed
