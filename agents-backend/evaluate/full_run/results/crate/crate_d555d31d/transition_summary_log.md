# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (10): ['io.crate.role.metadata.RolesMetadataTest#test_add_old_users_metadata_to_roles_metadata', 'io.crate.role.metadata.RolesMetadataTest#test_cannot_grant_already_granted_role_by_different_grantor', 'io.crate.role.metadata.RolesMetadataTest#test_grant_roles_do_not_loose_existing_privileges', 'io.crate.role.metadata.RolesMetadataTest#test_grant_roles_to_user', 'io.crate.role.metadata.RolesMetadataTest#test_jwt_properties_from_invalid_x_content', 'io.crate.role.metadata.RolesMetadataTest#test_revoke_roles_from_user', 'io.crate.role.metadata.RolesMetadataTest#test_roles_metadata_from_cluster_state', 'io.crate.role.metadata.RolesMetadataTest#test_roles_metadata_streaming', 'io.crate.role.metadata.RolesMetadataTest#test_roles_metadata_with_attributes_streaming', 'io.crate.role.metadata.RolesMetadataTest#test_superuser_crate_can_revoke_any_granted_roles']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.role.metadata.RolesMetadataTest']
  - io.crate.role.metadata.RolesMetadataTest#test_add_old_users_metadata_to_roles_metadata: baseline=absent, patched=passed
  - io.crate.role.metadata.RolesMetadataTest#test_cannot_grant_already_granted_role_by_different_grantor: baseline=absent, patched=passed
  - io.crate.role.metadata.RolesMetadataTest#test_grant_roles_do_not_loose_existing_privileges: baseline=absent, patched=passed
  - io.crate.role.metadata.RolesMetadataTest#test_grant_roles_to_user: baseline=absent, patched=passed
  - io.crate.role.metadata.RolesMetadataTest#test_jwt_properties_from_invalid_x_content: baseline=absent, patched=passed
  - io.crate.role.metadata.RolesMetadataTest#test_revoke_roles_from_user: baseline=absent, patched=passed
  - io.crate.role.metadata.RolesMetadataTest#test_roles_metadata_from_cluster_state: baseline=absent, patched=passed
  - io.crate.role.metadata.RolesMetadataTest#test_roles_metadata_streaming: baseline=absent, patched=passed
  - io.crate.role.metadata.RolesMetadataTest#test_roles_metadata_with_attributes_streaming: baseline=absent, patched=passed
  - io.crate.role.metadata.RolesMetadataTest#test_superuser_crate_can_revoke_any_granted_roles: baseline=absent, patched=passed
