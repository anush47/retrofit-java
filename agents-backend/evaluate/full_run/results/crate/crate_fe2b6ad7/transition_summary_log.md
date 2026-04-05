# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.analyze.TableInfoToASTTest#test_table_parameters_index_prefix_stripped']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.analyze.TableInfoToASTTest']
  - io.crate.analyze.TableInfoToASTTest#testBuildCreateTableCheckConstraints: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#testBuildCreateTableClusteredByPartitionedBy: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#testBuildCreateTableColumnDefaultClause: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#testBuildCreateTableColumns: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#testBuildCreateTableIndexes: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#testBuildCreateTableNotNull: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#testBuildCreateTablePrimaryKey: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#testBuildCreateTableStorageDefinitions: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#test_bit_string_length_is_shown_in_show_create_table_output: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#test_generated_expression_on_geo_shape_in_show_create_table_output: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#test_geo_shape_array_index_definition_is_preserved_in_cluster_state: baseline=passed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#test_table_parameters_index_prefix_stripped: baseline=failed, patched=passed
  - io.crate.analyze.TableInfoToASTTest#test_varchar_with_length_limit_is_printed_as_varchar_with_length_in_show_create_table: baseline=passed, patched=passed
