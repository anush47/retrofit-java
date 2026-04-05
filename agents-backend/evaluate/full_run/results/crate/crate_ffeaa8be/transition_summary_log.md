# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (3): ['org.elasticsearch.transport.InboundHandlerTests#testRequestFullyReadButMoreDataIsAvailable', 'org.elasticsearch.transport.InboundHandlerTests#testResponseFullyReadButMoreDataIsAvailable', 'org.elasticsearch.transport.InboundHandlerTests#testResponseNotFullyRead']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.transport.InboundHandlerTests']
  - org.elasticsearch.transport.InboundHandlerTests#testClosesChannelOnErrorInHandshakeWithIncompatibleVersion: baseline=passed, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#testLogsSlowInboundProcessing: baseline=passed, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#testPing: baseline=passed, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#testRequestAndResponse: baseline=passed, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#testRequestFullyReadButMoreDataIsAvailable: baseline=failed, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#testRequestNotFullyRead: baseline=passed, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#testResponseFullyReadButMoreDataIsAvailable: baseline=error, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#testResponseNotFullyRead: baseline=error, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#testSendsErrorResponseToHandshakeFromCompatibleVersion: baseline=passed, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#test_handshake_checks_minimum_compatible_version_if_normal_version_is_not_compatible: baseline=passed, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#test_handshake_error_if_version_and_minimum_compatible_version_is_not_compatible: baseline=passed, patched=passed
  - org.elasticsearch.transport.InboundHandlerTests#test_handshake_precedes_stream_version_for_compatibility: baseline=passed, patched=passed
