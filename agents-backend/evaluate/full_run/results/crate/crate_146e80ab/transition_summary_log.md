# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.execution.engine.aggregation.impl.AverageAggregationTest#test_avg_numeric_can_handle_non_terminating_decimal_expansion']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.engine.aggregation.impl.AverageAggregationTest']
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#testDouble: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#testFloat: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#testInteger: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#testInterval: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#testLong: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#testReturnType: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#testShort: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#testUnsupportedType: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#test_avg_numeric_can_handle_non_terminating_decimal_expansion: baseline=error, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#test_avg_numeric_on_double_non_doc_values: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#test_avg_numeric_on_long_non_doc_values_does_not_overflow: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#test_avg_numeric_with_precision_and_scale_on_double_non_doc_values: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#test_avg_with_byte_argument_type: baseline=passed, patched=passed
  - io.crate.execution.engine.aggregation.impl.AverageAggregationTest#test_function_implements_doc_values_aggregator_for_numeric_types: baseline=passed, patched=passed
