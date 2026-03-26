# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (6): ['io.crate.rest.action.SqlHttpHandlerTest#testDefaultUserIfHttpHeaderNotPresent', 'io.crate.rest.action.SqlHttpHandlerTest#testSessionSettingsArePreservedAcrossRequests', 'io.crate.rest.action.SqlHttpHandlerTest#testSettingUserIfHttpHeaderNotPresent', 'io.crate.rest.action.SqlHttpHandlerTest#testUserIfHttpBasicAuthIsPresent', 'io.crate.rest.action.SqlHttpHandlerTest#test_partial_result_is_cleared_when_sending_an_error', 'io.crate.rest.action.SqlHttpHandlerTest#test_resolve_user_from_jwt_token']
- pass->fail (0): []
