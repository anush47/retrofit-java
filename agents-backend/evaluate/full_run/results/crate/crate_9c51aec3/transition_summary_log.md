# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (10): ['org.elasticsearch.cluster.metadata.MetadataIndexUpgradeServiceTest#test_upgradeIndexMetadata_ensure_UDFs_are_loaded_before_checkMappingsCompatibility_is_called', 'org.elasticsearch.gateway.GatewayMetaStateTests#testAddCustomMetadataOnUpgrade', 'org.elasticsearch.gateway.GatewayMetaStateTests#testCustomMetadataNoChange', 'org.elasticsearch.gateway.GatewayMetaStateTests#testCustomMetadataValidation', 'org.elasticsearch.gateway.GatewayMetaStateTests#testIndexMetadataUpgrade', 'org.elasticsearch.gateway.GatewayMetaStateTests#testIndexTemplateValidation', 'org.elasticsearch.gateway.GatewayMetaStateTests#testMultipleIndexTemplateUpgrade', 'org.elasticsearch.gateway.GatewayMetaStateTests#testNoMetadataUpgrade', 'org.elasticsearch.gateway.GatewayMetaStateTests#testRemoveCustomMetadataOnUpgrade', 'org.elasticsearch.gateway.GatewayMetaStateTests#testUpdateCustomMetadataOnUpgrade']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.cluster.metadata.MetadataIndexUpgradeServiceTest', 'org.elasticsearch.gateway.GatewayMetaStateTests']
  - org.elasticsearch.cluster.metadata.MetadataIndexUpgradeServiceTest#test_upgradeIndexMetadata_ensure_UDFs_are_loaded_before_checkMappingsCompatibility_is_called: baseline=absent, patched=passed
  - org.elasticsearch.gateway.GatewayMetaStateTests#testAddCustomMetadataOnUpgrade: baseline=absent, patched=passed
  - org.elasticsearch.gateway.GatewayMetaStateTests#testCustomMetadataNoChange: baseline=absent, patched=passed
  - org.elasticsearch.gateway.GatewayMetaStateTests#testCustomMetadataValidation: baseline=absent, patched=passed
  - org.elasticsearch.gateway.GatewayMetaStateTests#testIndexMetadataUpgrade: baseline=absent, patched=passed
  - org.elasticsearch.gateway.GatewayMetaStateTests#testIndexTemplateValidation: baseline=absent, patched=passed
  - org.elasticsearch.gateway.GatewayMetaStateTests#testMultipleIndexTemplateUpgrade: baseline=absent, patched=passed
  - org.elasticsearch.gateway.GatewayMetaStateTests#testNoMetadataUpgrade: baseline=absent, patched=passed
  - org.elasticsearch.gateway.GatewayMetaStateTests#testRemoveCustomMetadataOnUpgrade: baseline=absent, patched=passed
  - org.elasticsearch.gateway.GatewayMetaStateTests#testUpdateCustomMetadataOnUpgrade: baseline=absent, patched=passed
