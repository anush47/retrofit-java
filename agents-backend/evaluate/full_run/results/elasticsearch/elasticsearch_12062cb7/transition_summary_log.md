# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (2): ['org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsIgnoreThreadsOfModelWithZeroAllocations', 'org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleDownForModelWithZeroAllocations']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests']
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testCheckIfJobsCanBeMovedInLeastEfficientWayMemoryOnly: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testCheckIfJobsCanBeMovedInLeastEfficientWayProcessorsAndMemory: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testCheckIfOneNodeCouldBeRemovedMemoryOnly: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testCheckIfOneNodeCouldBeRemovedProcessorAndMemory: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessors: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsIgnoreThreadsOfModelWithZeroAllocations: baseline=failed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleDown: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleDownForModelWithZeroAllocations: baseline=failed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleDownNotPreventedByDummyEntityAsMemoryTooLow: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleDownNotPreventedByDummyEntityProcessors: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleDownPreventedByDummyEntityMemory: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleDownPreventedByMinNodes: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleDownToZero: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleUpGivenAwaitingLazyAssignment: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testGetMemoryAndProcessorsScaleUpGivenAwaitingLazyAssignmentButFailed: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testScaleUpByProcessorsWhenAlreadyStarted: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.autoscaling.MlAutoscalingResourceTrackerTests#testScaleUpByProcessorsWhenStarting: baseline=passed, patched=passed
