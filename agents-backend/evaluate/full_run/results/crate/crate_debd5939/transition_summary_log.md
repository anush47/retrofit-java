# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.types.ResultSetParserTest#test_can_query_char_column_via_jdbc_from_foreign_table']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.types.ResultSetParserTest']
  - io.crate.types.ResultSetParserTest#test_can_query_char_column_via_jdbc_from_foreign_table: baseline=error, patched=passed
