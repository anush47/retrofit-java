# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testRequestingModuleWithStackWalk']
- newly passing (10): ['org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=create_classloader}', 'org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=processBuilder_startPipeline}', 'org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=processBuilder_start}', 'org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=runtime_exit}', 'org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=runtime_halt}', 'org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=create_classloader}', 'org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=processBuilder_startPipeline}', 'org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=processBuilder_start}', 'org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=runtime_exit}', 'org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=runtime_halt}']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.entitlement.qa.EntitlementsDeniedIT', 'org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests']
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=create_classloader}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=processBuilder_startPipeline}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=processBuilder_start}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=runtime_exit}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied actionName=runtime_halt}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=create_classloader}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=processBuilder_startPipeline}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=processBuilder_start}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=runtime_exit}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.qa.EntitlementsDeniedIT#testCheckThrows {pathPrefix=denied_nonmodular actionName=runtime_halt}: baseline=absent, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testGetEntitlementsFailureIsCached: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testGetEntitlementsResultIsCached: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testGetEntitlementsReturnsEntitlementsForPluginModule: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testGetEntitlementsReturnsEntitlementsForPluginUnnamedModule: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testGetEntitlementsReturnsEntitlementsForServerModule: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testGetEntitlementsThrowsOnMissingPluginUnnamedModule: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testGetEntitlementsThrowsOnMissingPolicyForPlugin: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testGetEntitlementsThrowsOnMissingPolicyForServer: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testRequestingModuleFastPath: baseline=passed, patched=passed
  - org.elasticsearch.entitlement.runtime.policy.PolicyManagerTests#testRequestingModuleWithStackWalk: baseline=failed, patched=passed
