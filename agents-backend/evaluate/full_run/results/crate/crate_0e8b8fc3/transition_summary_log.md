# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.execution.ddl.tables.DropColumnTaskTest#test_can_drop_generated_column']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.ddl.tables.DropColumnTaskTest']
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_can_drop_generated_column: baseline=failed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_can_drop_simple_column: baseline=passed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_can_drop_subcolumn: baseline=passed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_can_drop_subcolumn_and_parent_together: baseline=passed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_cannot_drop_column_used_in_generated_expression: baseline=passed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_drop_column_with_check_constraint: baseline=passed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_drop_column_with_check_constraint_from_partitioned_table: baseline=passed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_drop_column_with_table_level_check_constraint: baseline=passed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_drop_subcolumn_with_check_constraint: baseline=passed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_drop_subcolumn_with_check_constraint_on_children: baseline=passed, patched=passed
  - io.crate.execution.ddl.tables.DropColumnTaskTest#test_is_no_op_if_columns_exist: baseline=passed, patched=passed
