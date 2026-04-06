# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.repositories.azure.AzureStorageSettingsTest#test_raise_exception_on_endpoint_uri_without_valid_host']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.repositories.azure.AzureStorageServiceTests', 'org.elasticsearch.repositories.azure.AzureStorageSettingsTest']
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testBlobNameFromUri: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testCreateClientWithEndpoint: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testCreateClientWithEndpointSuffix: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testCreateClientWithSecondaryEndpoint: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testGetSelectedClientBackoffPolicy: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testGetSelectedClientBackoffPolicyNbRetries: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testGetSelectedClientDefaultTimeout: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testGetSelectedClientNoTimeout: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testMultipleProxies: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testNoProxy: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testProxyHttp: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testProxyNoHost: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testProxyNoPort: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testProxyNoType: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testProxySocks: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#testProxyWrongHost: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#test_cannot_set_endpoint_and_endpoint_suffix: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageServiceTests#test_cannot_set_secondary_endpoint_without_endpoint: baseline=passed, patched=passed
  - org.elasticsearch.repositories.azure.AzureStorageSettingsTest#test_raise_exception_on_endpoint_uri_without_valid_host: baseline=failed, patched=passed
