# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.role.TransportRoleActionTest#test_alter_user_change_or_reset_password_and_keep_jwt']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.role.TransportRoleActionTest']
  - io.crate.role.TransportRoleActionTest#testCreateFirstUser: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#testCreateUser: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#testCreateUserAlreadyExists: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#testDropNonExistingUser: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#testDropUser: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#testDropUserNoUsersAtAll: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_alter_user_cannot_set_jwt_to_role: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_alter_user_cannot_set_password_to_role: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_alter_user_change_jwt_and_keep_password: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_alter_user_change_or_reset_password_and_keep_jwt: baseline=error, patched=passed
  - io.crate.role.TransportRoleActionTest#test_alter_user_reset_jwt_and_password: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_alter_user_throws_error_on_jwt_properties_clash: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_alter_user_with_old_users_metadata: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_cannot_drop_user_mapped_to_foreign_servers: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_create_user_with_existing_name_but_different_jwt_props: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_create_user_with_matching_jwt_props_exists: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_create_user_with_old_users_metadata: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_drop_role_with_children_is_not_allowed: baseline=passed, patched=passed
  - io.crate.role.TransportRoleActionTest#test_drop_user_with_old_users_metadata: baseline=passed, patched=passed
