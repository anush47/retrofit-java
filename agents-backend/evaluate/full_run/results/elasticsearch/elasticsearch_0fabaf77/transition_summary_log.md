# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsRolledDataStream']
- newly passing (4): ['org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsClosedBackingIndexDataStream', 'org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsExistingDataStream', 'org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsMultipleDataStreams', 'org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsNoDataStream']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.datastreams.DataStreamsStatsTests']
  - org.elasticsearch.datastreams.DataStreamsStatsTests#classMethod: baseline=failed, patched=absent
  - org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsClosedBackingIndexDataStream: baseline=absent, patched=passed
  - org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsEmptyDataStream: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsExistingDataStream: baseline=absent, patched=passed
  - org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsExistingDataStreamWithFailureStores: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsExistingHiddenDataStream: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsMultipleDataStreams: baseline=absent, patched=passed
  - org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsNoDataStream: baseline=absent, patched=passed
  - org.elasticsearch.datastreams.DataStreamsStatsTests#testStatsRolledDataStream: baseline=failed, patched=passed
