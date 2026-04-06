# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (21): ['org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testGenerateDestIndexName_noDotPrefix', 'org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testGenerateDestIndexName_withDotPrefix', 'org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testGenerateDestIndexName_withHyphen', 'org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testGenerateDestIndexName_withUnderscore', 'org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testReindexIncludesInfiniteRateLimit', 'org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testReindexIncludesRateLimit', 'org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testReindexNegativeRateLimitThrowsError', 'org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testReindexZeroRateLimitThrowsError', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testDestIndexContainsDocs', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testDestIndexDeletedIfExists', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testDestIndexNameSet_noDotPrefix', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testDestIndexNameSet_withDotPrefix', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testFailIfMetadataBlockSet', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testFailIfReadBlockSet', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testMappingsAddedToDestIndex', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testReadOnlyBlocksNotAddedBack', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testSetSourceToBlockWrites', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testSettingsAddedBeforeReindex', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testSettingsAndMappingsFromTemplate', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testTsdbStartEndSet', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testUpdateSettingsDefaultsRestored']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests', 'org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT']
  - org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testGenerateDestIndexName_noDotPrefix: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testGenerateDestIndexName_withDotPrefix: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testGenerateDestIndexName_withHyphen: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testGenerateDestIndexName_withUnderscore: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testReindexIncludesInfiniteRateLimit: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testReindexIncludesRateLimit: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testReindexNegativeRateLimitThrowsError: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDataStreamIndexTransportActionTests#testReindexZeroRateLimitThrowsError: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testDestIndexContainsDocs: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testDestIndexDeletedIfExists: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testDestIndexNameSet_noDotPrefix: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testDestIndexNameSet_withDotPrefix: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testFailIfMetadataBlockSet: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testFailIfReadBlockSet: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testMappingsAddedToDestIndex: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testReadOnlyBlocksNotAddedBack: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testSetSourceToBlockWrites: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testSettingsAddedBeforeReindex: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testSettingsAndMappingsFromTemplate: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testTsdbStartEndSet: baseline=absent, patched=passed
  - org.elasticsearch.xpack.migrate.action.ReindexDatastreamIndexTransportActionIT#testUpdateSettingsDefaultsRestored: baseline=absent, patched=passed
