# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.metadata.cluster.AlterTableClusterStateExecutorTest#test_altering_settings_do_not_modify_version_created']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.metadata.cluster.AlterTableClusterStateExecutorTest']
  - io.crate.metadata.cluster.AlterTableClusterStateExecutorTest#testMarkArchivedSettings: baseline=passed, patched=passed
  - io.crate.metadata.cluster.AlterTableClusterStateExecutorTest#testPrivateSettingsAreRemovedOnUpdateTemplate: baseline=passed, patched=passed
  - io.crate.metadata.cluster.AlterTableClusterStateExecutorTest#test_altering_settings_do_not_modify_version_created: baseline=failed, patched=passed
  - io.crate.metadata.cluster.AlterTableClusterStateExecutorTest#test_group_settings_are_not_filtered_out: baseline=passed, patched=passed
