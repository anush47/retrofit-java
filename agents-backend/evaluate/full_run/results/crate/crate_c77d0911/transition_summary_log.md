# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.integrationtests.DeleteIntegrationTest#test_can_reuse_prepared_statement_for_delete_containing_non_deterministic_function']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.integrationtests.DeleteIntegrationTest']
  - io.crate.integrationtests.DeleteIntegrationTest#testBulkDeleteNullAndSingleKey: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteByIdWithMultiplePrimaryKey: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteByQueryWithMultiplePrimaryKey: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteExceedingInternalDefaultBulkSize: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteFromAlias: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteOnIpType: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteOnPKNoMatch: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteTableWithoutWhere: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteToDeleteRequestByPlanner: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteToRoutedRequestByPlannerWhereIn: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteToRoutedRequestByPlannerWhereOr: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteWhereIsNull: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteWithNullArg: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteWithSubQuery: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteWithSubQueryOnPartition: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#testDeleteWithWhereDeletesCorrectRecord: baseline=passed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#test_can_reuse_prepared_statement_for_delete_containing_non_deterministic_function: baseline=failed, patched=passed
  - io.crate.integrationtests.DeleteIntegrationTest#test_delete_partitions_from_subquery_does_not_leave_empty_orphan_partitions: baseline=passed, patched=passed
