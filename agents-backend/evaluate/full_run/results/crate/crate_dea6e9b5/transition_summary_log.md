# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.role.RolePropertiesTest#test_can_read_empty_role_properties_from_x_content']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.role.RolePropertiesTest']
  - io.crate.role.RolePropertiesTest#test_bwc_streaming: baseline=passed, patched=passed
  - io.crate.role.RolePropertiesTest#test_can_read_empty_role_properties_from_x_content: baseline=failed, patched=passed
  - io.crate.role.RolePropertiesTest#test_empty_password_string_is_rejected: baseline=passed, patched=passed
  - io.crate.role.RolePropertiesTest#test_invalid_jwt_property: baseline=passed, patched=passed
  - io.crate.role.RolePropertiesTest#test_invalid_property: baseline=passed, patched=passed
  - io.crate.role.RolePropertiesTest#test_session_property_which_is_read_only: baseline=passed, patched=passed
  - io.crate.role.RolePropertiesTest#test_session_property_with_invalid_value: baseline=passed, patched=passed
  - io.crate.role.RolePropertiesTest#test_session_setting_reset_invalid_session_setting: baseline=passed, patched=passed
