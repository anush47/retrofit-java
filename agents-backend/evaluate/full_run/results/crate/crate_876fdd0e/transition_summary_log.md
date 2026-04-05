# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.execution.dml.MixedVersionStorageTest#test_writing_null_subcolumn_to_ignored_object_in_table_without_oids']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.dml.MixedVersionStorageTest']
  - io.crate.execution.dml.MixedVersionStorageTest#test_reading_5_9_tables_with_raw: baseline=passed, patched=passed
  - io.crate.execution.dml.MixedVersionStorageTest#test_writing_null_subcolumn_to_ignored_object_in_table_without_oids: baseline=error, patched=passed
