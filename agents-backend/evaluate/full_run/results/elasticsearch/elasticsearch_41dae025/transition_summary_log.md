# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (3): ['org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testCheckBlockForDataStreamFailureStores', 'org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testCheckBlockForDataStreams', 'org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testErrorRecordingOnRetention']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests', 'org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT']
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testCheckBlockForDataStreamFailureStores: baseline=failed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testCheckBlockForDataStreams: baseline=failed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testCheckBlockForIndices: baseline=passed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testConditionEvaluationWhenAliasToWriteAndReadIndicesConsidersOnlyPrimariesFromWriteIndex: baseline=passed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testDocStatsSelectionFromPrimariesOnly: baseline=passed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testEvaluateConditions: baseline=passed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testEvaluateWithoutMetadata: baseline=passed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testEvaluateWithoutStats: baseline=passed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testLazyRollover: baseline=passed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testLazyRolloverFails: baseline=passed, patched=passed
  - org.elasticsearch.action.admin.indices.rollover.TransportRolloverActionTests#testRolloverAliasToDataStreamFails: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testAutomaticForceMerge: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testDataLifecycleServiceConfiguresTheMergePolicy: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testErrorRecordingOnRetention: baseline=failed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testErrorRecordingOnRollover: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testLifecycleAppliedToFailureStore: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testOriginationDate: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testReenableDataStreamLifecycle: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testRolloverAndRetention: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testRolloverLifecycle: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testSystemDataStreamRetention: baseline=passed, patched=passed
  - org.elasticsearch.datastreams.lifecycle.DataStreamLifecycleServiceIT#testUpdatingLifecycleAppliesToAllBackingIndices: baseline=passed, patched=passed
