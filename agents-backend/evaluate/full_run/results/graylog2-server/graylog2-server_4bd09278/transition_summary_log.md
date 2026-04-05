# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (8): ['org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateCloudCompatibleInputInCloud', 'org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateInput', 'org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateNotCloudCompatibleInputInCloud', 'org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateNotGlobalInputInCloud', 'org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateNotGlobalInputWhenIsGlobalInputOnly', 'org.graylog2.rest.resources.system.inputs.InputsResourceTest#testPipelineReferences', 'org.graylog2.rest.resources.system.inputs.InputsResourceTest#testStreamReferences', 'org.graylog2.rest.resources.system.inputs.InputsResourceTest#testStreamReferencesPermissionFailsIfNotPermitted']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.graylog2.rest.resources.system.inputs.InputsResourceTest']
  - org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateCloudCompatibleInputInCloud: baseline=absent, patched=passed
  - org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateInput: baseline=absent, patched=passed
  - org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateNotCloudCompatibleInputInCloud: baseline=absent, patched=passed
  - org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateNotGlobalInputInCloud: baseline=absent, patched=passed
  - org.graylog2.rest.resources.system.inputs.InputsResourceTest#testCreateNotGlobalInputWhenIsGlobalInputOnly: baseline=absent, patched=passed
  - org.graylog2.rest.resources.system.inputs.InputsResourceTest#testPipelineReferences: baseline=absent, patched=passed
  - org.graylog2.rest.resources.system.inputs.InputsResourceTest#testStreamReferences: baseline=absent, patched=passed
  - org.graylog2.rest.resources.system.inputs.InputsResourceTest#testStreamReferencesPermissionFailsIfNotPermitted: baseline=absent, patched=passed
