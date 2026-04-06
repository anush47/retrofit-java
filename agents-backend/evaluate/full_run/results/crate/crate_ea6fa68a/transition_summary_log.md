# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.metadata.doc.DocTableInfoTest#test_add_columns_fails_eagerly_on_too_many_columns']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.metadata.doc.DocTableInfoTest']
  - io.crate.metadata.doc.DocTableInfoTest#testGetColumnInfo: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#testGetColumnInfoStrictParent: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_add_column_fixes_inner_types_of_all_its_parents: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_add_columns_fails_eagerly_on_too_many_columns: baseline=failed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_can_add_column_to_table: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_can_retrieve_all_parents_of_nested_object_column: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_cannot_add_child_column_without_defining_parents: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_drop_column_after_drop_column_preserves_previous_dropped_columns: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_drop_column_fixes_inner_types_of_all_its_parents: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_drop_column_updates_type_of_parent_ref: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_dropped_columns_are_included_in_oid_to_column_map: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_get_child_references: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_isIgnoredOrImmediateChildOfIgnored_method: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_lookup_name_by_source_with_columns_with_and_without_oids_added_to_table_created_before_5_5_0: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_rename_column_fixes_inner_types_of_all_its_parents: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_version_created_is_read_from_partitioned_template: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_version_created_is_set_to_current_version_if_unavailable_at_partitioned_template: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_write_to_preserves_indices: baseline=passed, patched=passed
  - io.crate.metadata.doc.DocTableInfoTest#test_write_to_preserves_number_of_shards_of_partitions: baseline=passed, patched=passed
