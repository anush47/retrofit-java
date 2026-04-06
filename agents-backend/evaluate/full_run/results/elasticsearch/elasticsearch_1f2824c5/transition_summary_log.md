# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testGetConfiguration']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests']
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testBuildInferenceRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testChunkInferSetsTokenization: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testChunkInfer_E5ChunkingSettingsSet: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testChunkInfer_E5WithNullChunkingSettings: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testChunkInfer_ElserWithChunkingSettingsSet: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testChunkInfer_ElserWithNullChunkingSettings: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testChunkInfer_FailsBatch: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testChunkInfer_SparseWithChunkingSettingsSet: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testChunkInfer_SparseWithNullChunkingSettings: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testChunkingLargeDocument: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testEmbeddingTypeFromTaskTypeAndSettings: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testGetConfiguration: baseline=failed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testIsDefaultId: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testModelVariantDoesNotMatchArchitecturesAndIsNotPlatformAgnostic: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParsePersistedConfig: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParsePersistedConfig_Rerank: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfig: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfigEland_PreservesTaskType: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfigEland_SetsDimensionsToOne: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfig_E5: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfig_Misconfigured: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfig_Rerank: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfig_Rerank_DefaultTaskSettings: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfig_SparseEmbeddingWithChunkingSettingsNotProvided: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfig_SparseEmbeddingWithChunkingSettingsProvided: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfig_SparseEmbeddingWithoutChunkingSettings: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testParseRequestConfig_elser: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.services.elasticsearch.ElasticsearchInternalServiceTests#testPutModel: baseline=passed, patched=passed
