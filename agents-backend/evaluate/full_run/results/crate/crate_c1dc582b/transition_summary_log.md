# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.integrationtests.ViewsITest#test_view_on_top_level_columns_sub_columns_are_shown_in_information_schema']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.integrationtests.ViewsITest']
  - io.crate.integrationtests.ViewsITest#testCreatePartitionedTableFailsIfNameConflictsWithView: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testCreateTableFailsIfNameConflictsWithView: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testCreateViewFailsIfNameConflictsWithPartitionedTable: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testCreateViewFailsIfNameConflictsWithTable: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testCreateViewFailsIfViewAlreadyExists: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testDropViewDoesNotFailIfViewIsMissingAndIfExistsIsUsed: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testDropViewFailsIfViewIsMissing: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testSubscriptOnViews: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testViewCanBeCreatedAndThenReplaced: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testViewCanBeCreatedSelectedAndThenDropped: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#testViewCanBeUsedForJoins: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#test_can_rename_existing_view: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#test_cannot_rename_view_if_target_already_exists: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#test_creating_a_self_referencing_view_is_not_allowed: baseline=passed, patched=passed
  - io.crate.integrationtests.ViewsITest#test_view_on_top_level_columns_sub_columns_are_shown_in_information_schema: baseline=failed, patched=passed
  - io.crate.integrationtests.ViewsITest#test_where_clause_on_view_normalized_on_coordinator_node: baseline=passed, patched=passed
