# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.analyze.where.WhereClauseAnalyzerTest#test_delete_from_partition_by_column_involving_non_deterministic_function']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.analyze.where.WhereClauseAnalyzerTest']
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testAnyILikeArrayLiteral: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testAnyInvalidArrayType: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testAnyLikeArrayLiteral: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testColumnReferencedTwiceInGeneratedColumnPartitioned: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testEqualGenColOptimization: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testGenColRangeOptimization: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testGenColRoundingFunctionNoSwappingOperatorOptimization: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testGtGenColOptimization: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testInConvertedToAnyIfOnlyLiterals: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testMultipleColumnsOptimization: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testMultiplicationGenColNoOptimization: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testNonPartitionedNotOptimized: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testOptimizationNonRoundingFunctionGreater: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testPrimaryTermOnlySupportedWithEqualOperator: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testRawNotAllowedInQuery: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testSelectFromPartitionedTable: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testSelectWherePartitionedByColumn: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testSeqNoAndPrimaryTermAreRequired: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testSeqNoOnlySupportedWithEqualOperator: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testUpdateWherePartitionedByColumn: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testVersionOnlySupportedWithEqualOperator: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#testVersioningMechanismsCannotBeMixed: baseline=passed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#test_delete_from_partition_by_column_involving_non_deterministic_function: baseline=failed, patched=passed
  - io.crate.analyze.where.WhereClauseAnalyzerTest#test_where_on_date_with_null_partition_or_id_can_match_all_partitions: baseline=passed, patched=passed
