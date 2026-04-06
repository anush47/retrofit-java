# Transition Summary

- Source: phase_outputs
- Valid backport signal: False
- Reason: Invalid: No fail-to-pass or newly passing relevant tests were observed.
- fail->pass (0): []
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.integrationtests.AlterTableIntegrationTest']
  - io.crate.integrationtests.AlterTableIntegrationTest#test_add_sub_column_to_ignored_parent_if_table_is_not_empty_logs_warning: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_partitioned_table_drop_column_can_add_again: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_partitioned_table_drop_simple_column: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_table_can_add_column_after_dropping_column_with_max_known_position: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_table_drop_column_can_add_again: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_table_drop_column_dropped_meanwhile: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_table_drop_leaf_subcolumn: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_table_drop_leaf_subcolumn_with_parent_object_array: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_table_drop_simple_column: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_table_drop_simple_column_view_updated: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_alter_table_drop_subcolumn_with_children: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_can_add_sub_column_to_ignored_parent_if_table_is_empty: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_can_add_sub_column_to_ignored_parent_if_table_is_not_empty_and_can_query_data_of_different_type: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_create_soft_delete_setting_for_partitioned_tables: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_drop_sub_column_readd_and_update: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_increase_num_shards_does_not_delete_source_index_on_alloc_failures: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_rename_columns: baseline=passed, patched=passed
  - io.crate.integrationtests.AlterTableIntegrationTest#test_reset_setting_on_complete_partitioned_table: baseline=passed, patched=passed
