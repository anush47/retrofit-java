# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (2): ['io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_function_registered_under_pg_catalog', 'io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_function_registered_under_pg_catalog']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest', 'io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest']
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_at_least_one_arg_is_null_returns_null: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_create_privilege: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_function_registered_under_pg_catalog: baseline=error, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_no_privilege_for_db_other_than_crate: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_no_privilege_other_than_connect: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_no_user_compile_gets_new_instance: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_same_results_for_name_and_oid: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_throws_error_when_invalid_privilege: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_throws_error_when_user_is_not_found: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_throws_error_when_user_is_not_super_user_checking_for_other_user: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_throws_error_when_user_is_not_super_user_checking_for_other_user_for_compiled: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasDatabasePrivilegeFunctionTest#test_user_is_literal_compile_gets_new_instance: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_at_least_one_arg_is_null_returns_null: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_function_registered_under_pg_catalog: baseline=error, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_no_user_compile_gets_new_instance: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_same_results_for_name_and_oid: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_throws_error_when_invalid_privilege: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_throws_error_when_user_is_not_found: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_throws_error_when_user_without_related_privileges_is_checking_for_other_user: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_throws_error_when_user_without_related_privileges_is_checking_for_other_user_for_compiled: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_user_is_literal_compile_gets_new_instance: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_user_with_DDL_permission_has_CREATE_but_not_USAGE_privilege_for_regular_schema: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_user_with_DQL_permission_has_USAGE_but_not_CREATE_privilege_for_regular_schema: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_user_without_permission_doesnt_have_privilege_for_regular_schema: baseline=passed, patched=passed
  - io.crate.expression.scalar.HasSchemaPrivilegeFunctionTest#test_user_without_permission_has_USAGE_but_not_CREATE_privilege_for_public_schemas: baseline=passed, patched=passed
