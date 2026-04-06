# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (2): ['org.elasticsearch.entitlement.runtime.policy.PolicyParserTests#testParseCreateClassloader', 'org.elasticsearch.entitlement.runtime.policy.PolicyParserTests#testParseSetHttpsConnectionProperties']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.entitlement.runtime.policy.PolicyParserTests']
  - org.elasticsearch.entitlement.runtime.policy.PolicyParserTests#testGetEntitlementTypeName: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyParserTests#testParseCreateClassloader: baseline=failed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyParserTests#testParseSetHttpsConnectionProperties: baseline=failed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyParserTests#testPolicyBuilder: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyParserTests#testPolicyBuilderOnExternalPlugin: baseline=passed, patched=passed
