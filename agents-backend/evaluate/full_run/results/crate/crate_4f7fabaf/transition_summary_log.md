# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (5): ['org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#testCreateBulkIndicesSimple', 'org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#testCreateInvalidName', 'org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#testEmpty', 'org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#test_creation_of_a_new_partition_upgrades_template_and_does_it_once', 'org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#test_insert_into_existing_partition_does_not_recreate_it']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest']
  - org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#testCreateBulkIndicesSimple: baseline=absent, patched=passed
  - org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#testCreateInvalidName: baseline=absent, patched=passed
  - org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#testEmpty: baseline=absent, patched=passed
  - org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#test_creation_of_a_new_partition_upgrades_template_and_does_it_once: baseline=absent, patched=passed
  - org.elasticsearch.action.admin.indices.create.TransportCreatePartitionsActionTest#test_insert_into_existing_partition_does_not_recreate_it: baseline=absent, patched=passed
