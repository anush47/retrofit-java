# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.analyze.AlterTableAddColumnAnalyzerTest#test_add_parent_and_child_columns_within_one_statement']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.analyze.AlterTableAddColumnAnalyzerTest']
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#add_multiple_columns_adding_same_name_primitive_throws_an_exception: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#add_multiple_columns_pkey_indices_referring_to_correct_ref_indices: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#testAddColumnOnSinglePartitionNotAllowed: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#testAddColumnOnSystemTableIsNotAllowed: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#testAddColumnThatExistsAlready: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#testAddColumnWithAnalyzerAndNonStringType: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#testAddColumnWithCheckConstraintFailsBecauseItRefersToAnotherColumn: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#testAddFulltextIndex: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#testAddPrimaryKeyColumnWithArrayTypeUnsupported: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#testAlterTableAddColumnWithNullConstraint: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#test_add_parent_and_child_columns_within_one_statement: baseline=failed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#test_cannot_add_named_primary_key_constraint_to_existing_table: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#test_cannot_alter_table_to_add_a_column_definition_of_type_time: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#test_check_constraint_cannot_be_added_to_nested_object_sub_column_without_full_path: baseline=passed, patched=passed
  - io.crate.analyze.AlterTableAddColumnAnalyzerTest#test_check_constraint_on_nested_object_sub_column_has_correct_type_and_expression: baseline=passed, patched=passed
