# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForAllTimeRange']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.graylog2.database.filtering.inmemory.SingleFilterParserTest']
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForAllTimeRange: baseline=error, patched=passed
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForBoolType: baseline=passed, patched=passed
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForDateRanges: baseline=passed, patched=passed
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForDateType: baseline=passed, patched=passed
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForIntRanges: baseline=passed, patched=passed
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForIntType: baseline=passed, patched=passed
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForObjectIdType: baseline=passed, patched=passed
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForOpenDateRanges: baseline=passed, patched=passed
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionCorrectlyForStringType: baseline=passed, patched=passed
  - org.graylog2.database.filtering.inmemory.SingleFilterParserTest#parsesFilterExpressionForStringFieldsCorrectlyEvenIfValueContainsRangeSeparator: baseline=passed, patched=passed
