# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (3): ['org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleEmptyIndex', 'org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleOfDownsample', 'org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDuplicateDownsampleRequest']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests']
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testCancelDownsampleIndexer: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testCannotDownsampleMissingIndex: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testCannotDownsampleToExistingIndex: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testCannotDownsampleWhileOtherDownsampleInProgress: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testCannotDownsampleWriteableIndex: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testConcurrentDownsample: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testCopyIndexSettings: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleBulkFailed: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleDatastream: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleEmptyIndex: baseline=failed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleIndex: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleIndexWithFlattenedAndMultiFieldDimensions: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleIndexWithNoMetrics: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleOfDownsample: baseline=failed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleSparseMetrics: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDownsampleStats: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testDuplicateDownsampleRequest: baseline=failed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testNullDownsampleConfig: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testNullDownsampleIndexName: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testNullSourceIndexName: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testResumeDownsample: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testResumeDownsamplePartial: baseline=passed, patched=passed
  - org.elasticsearch.xpack.downsample.DownsampleActionSingleNodeTests#testTooManyBytesInFlight: baseline=passed, patched=passed
