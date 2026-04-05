# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.replication.logical.action.PublicationsStateActionTest#test_ensure_streaming_response_received_from_5_10_can_be_forwarded_to_5_10']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.replication.logical.action.PublicationsStateActionTest']
  - io.crate.replication.logical.action.PublicationsStateActionTest#test_bwc_streaming_5: baseline=passed, patched=passed
  - io.crate.replication.logical.action.PublicationsStateActionTest#test_ensure_streaming_response_received_from_5_10_can_be_forwarded_to_5_10: baseline=failed, patched=passed
  - io.crate.replication.logical.action.PublicationsStateActionTest#test_resolve_relation_names_for_all_tables_ignores_table_when_pub_owner_doesnt_have_read_write_define_permissions: baseline=passed, patched=passed
  - io.crate.replication.logical.action.PublicationsStateActionTest#test_resolve_relation_names_for_all_tables_ignores_table_when_subscriber_doesnt_have_read_permissions: baseline=passed, patched=passed
  - io.crate.replication.logical.action.PublicationsStateActionTest#test_resolve_relation_names_for_all_tables_ignores_table_with_non_active_primary_shards: baseline=passed, patched=passed
  - io.crate.replication.logical.action.PublicationsStateActionTest#test_resolve_relation_names_for_all_tables_marks_partition_with_non_active_primary_shards: baseline=passed, patched=passed
  - io.crate.replication.logical.action.PublicationsStateActionTest#test_resolve_relation_names_for_concrete_tables_marks_partition_with_non_active_primary_shards: baseline=passed, patched=passed
  - io.crate.replication.logical.action.PublicationsStateActionTest#test_resolve_relation_names_for_concrete_tables_marks_table_with_non_active_primary_shards: baseline=passed, patched=passed
  - io.crate.replication.logical.action.PublicationsStateActionTest#test_resolve_relation_names_for_fixed_tables_ignores_table_when_subscriber_doesnt_have_read_permissions: baseline=passed, patched=passed
