# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.xpack.search.AsyncSearchTaskTests#testDelayedOnListShardsShouldNotResultInExceptions']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.search.AsyncSearchTaskTests']
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testAddCompletionListenerScheduleErrorInitListenerExecutedImmediately: baseline=passed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testAddCompletionListenerScheduleErrorWaitForInitListener: baseline=passed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testDelayedOnListShardsShouldNotResultInExceptions: baseline=failed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testFatalFailureDuringFetch: baseline=passed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testFatalFailureWithNoCause: baseline=passed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testTaskDescription: baseline=passed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testWaitForCompletion: baseline=passed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testWaitForInit: baseline=passed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testWithFailure: baseline=passed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testWithFailureAndGetResponseFailureDuringReduction: baseline=passed, patched=passed
  - org.elasticsearch.xpack.search.AsyncSearchTaskTests#testWithFetchFailures: baseline=passed, patched=passed
