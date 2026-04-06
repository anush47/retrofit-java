# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testErrorBeforeRequest']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests']
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testApacheCancelWhileRunningAfterRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testApacheCancelWhileRunningBeforeRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testCancelAfterRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testCancelBeforeRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testCancelBreaksInfiniteLoop: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testCancelIsIdempotent: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testCloseAfterRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testCloseBeforeRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testCloseIsIdempotent: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testCloseWhileRunningAfterRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testCloseWhileRunningBeforeRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testDoubleSubscribeFails: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testErrorBeforeRequest: baseline=failed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testErrorWhileRunningAfterRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testErrorWhileRunningBeforeRequest: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testFailedIsIdempotent: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testFirstResponseCallsListener: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testNon200Response: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testNonEmptyFirstResponseCallsListener: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testOnlyRunOneAtATime: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testPauseApache: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testRequestingANegativeNumberFails: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testRequestingZeroFails: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testResumeApache: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testReuseMlThread: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testSubscriberAndPublisherExchange: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.external.http.StreamingHttpResultPublisherTests#testTotalBytesDecrement: baseline=passed, patched=passed
