# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (14): ['io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_column_from_single_partition', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_nested_column_to_target_name_with_different_depths', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_nested_column_to_target_name_with_different_parent', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_to_name_in_use', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_unknown_column', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_rename_nested_column', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_rename_nested_column_record_subscripts', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_rename_top_level_column', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_renaming_column_from_old_table_is_not_allowed', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_renaming_index_columns_to_subscript_expressions_is_not_allowed', 'io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_renaming_to_or_from_system_columns_is_not_allowed', 'io.crate.metadata.doc.DocTableInfoFactoryTest#testNoTableInfoFromOrphanedPartition', 'io.crate.metadata.doc.DocTableInfoFactoryTest#test_sets_created_version_based_on_oldest_partition', 'io.crate.metadata.doc.DocTableInfoFactoryTest#test_uses_5_4_0_as_version_if_mapping_has_no_oid']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.analyze.AlterTableRenameColumnAnalyzerTest', 'io.crate.metadata.doc.DocTableInfoFactoryTest']
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_column_from_single_partition: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_nested_column_to_target_name_with_different_depths: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_nested_column_to_target_name_with_different_parent: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_to_name_in_use: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_cannot_rename_unknown_column: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_rename_nested_column: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_rename_nested_column_record_subscripts: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_rename_top_level_column: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_renaming_column_from_old_table_is_not_allowed: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_renaming_index_columns_to_subscript_expressions_is_not_allowed: baseline=absent, patched=passed
  - io.crate.analyze.AlterTableRenameColumnAnalyzerTest#test_renaming_to_or_from_system_columns_is_not_allowed: baseline=absent, patched=passed
  - io.crate.metadata.doc.DocTableInfoFactoryTest#testNoTableInfoFromOrphanedPartition: baseline=absent, patched=passed
  - io.crate.metadata.doc.DocTableInfoFactoryTest#test_sets_created_version_based_on_oldest_partition: baseline=absent, patched=passed
  - io.crate.metadata.doc.DocTableInfoFactoryTest#test_uses_5_4_0_as_version_if_mapping_has_no_oid: baseline=absent, patched=passed
