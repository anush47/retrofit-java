# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.node.InternalSettingsPreparerTests#testReplacePlaceholderFailure']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.node.InternalSettingsPreparerTests']
  - org.elasticsearch.node.InternalSettingsPreparerTests#testDefaultPropertiesDoNothing: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testEmptySettings: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testExplicitClusterName: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testGarbageIsNotSwallowed: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testOverridesEmpty: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testOverridesMultiple: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testOverridesNew: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testOverridesOverride: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testReplacePlaceholderFailure: baseline=failed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testSecureSettings: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testSubstitutionBrokenLenient: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testSubstitutionEntireLine: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testSubstitutionFirstLine: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testSubstitutionLastLine: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testSubstitutionMissingLenient: baseline=passed, patched=passed
  - org.elasticsearch.node.InternalSettingsPreparerTests#testSubstitutionMultiple: baseline=passed, patched=passed
