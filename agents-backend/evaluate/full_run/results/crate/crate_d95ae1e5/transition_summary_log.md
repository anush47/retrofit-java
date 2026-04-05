# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (23): ['io.crate.protocols.postgres.PostgresWireProtocolTest#testBindMessageCanBeReadIfTypeForParamsIsUnknown', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testDescribePortalMessage', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testDescribeStatementMessage', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleCancelRequestBody', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleEmptySimpleQuery', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleMultipleSimpleQueries', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleMultipleSimpleQueriesWithQueryFailure', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleSimpleQueryFailing', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testKeyDataSentDuringStartUp', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testKillExceptionSendsReadyForQuery', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testPasswordMessageAuthenticationProcess', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testSessionCloseOnTerminationMessage', 'io.crate.protocols.postgres.PostgresWireProtocolTest#testSslRejection', 'io.crate.protocols.postgres.PostgresWireProtocolTest#test_all_parameter_status_is_received_on_startup', 'io.crate.protocols.postgres.PostgresWireProtocolTest#test_channel_is_flushed_after_receiving_flush_request', 'io.crate.protocols.postgres.PostgresWireProtocolTest#test_row_description_for_statement_on_single_table_includes_table_oid', 'io.crate.protocols.postgres.PostgresWireProtocolTest#test_ssl_accepted', 'io.crate.protocols.postgres.PostgresWireProtocolTest#test_throw_error_on_if_startup_message_is_to_long', 'io.crate.protocols.postgres.PostgresWireProtocolTest#test_throw_error_on_if_startup_message_is_to_short', 'io.crate.protocols.postgres.PostgresWireProtocolTest#test_throw_error_on_invalid_request_code', 'io.crate.protocols.postgres.ResultSetReceiverTest#testChannelIsPeriodicallyFlushedToAvoidConsumingTooMuchMemory', 'io.crate.protocols.postgres.ResultSetReceiverTest#test_channel_is_flushed_if_not_writable_anymore', 'io.crate.protocols.postgres.ResultSetReceiverTest#test_sendNextRow_future_is_called_once_message_is_written']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.protocols.postgres.DelayableWriteChannelTest', 'io.crate.protocols.postgres.PostgresWireProtocolTest', 'io.crate.protocols.postgres.ResultSetReceiverTest']
  - io.crate.protocols.postgres.DelayableWriteChannelTest#test_can_add_and_unblock_from_different_threads: baseline=passed, patched=passed
  - io.crate.protocols.postgres.DelayableWriteChannelTest#test_delayed_writes_are_released_on_close: baseline=passed, patched=passed
  - io.crate.protocols.postgres.DelayableWriteChannelTest#test_write_pending_writes_in_correct_order: baseline=passed, patched=absent
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testBindMessageCanBeReadIfTypeForParamsIsUnknown: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testDescribePortalMessage: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testDescribeStatementMessage: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleCancelRequestBody: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleEmptySimpleQuery: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleMultipleSimpleQueries: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleMultipleSimpleQueriesWithQueryFailure: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testHandleSimpleQueryFailing: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testKeyDataSentDuringStartUp: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testKillExceptionSendsReadyForQuery: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testPasswordMessageAuthenticationProcess: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testSessionCloseOnTerminationMessage: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#testSslRejection: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#test_all_parameter_status_is_received_on_startup: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#test_channel_is_flushed_after_receiving_flush_request: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#test_row_description_for_statement_on_single_table_includes_table_oid: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#test_ssl_accepted: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#test_throw_error_on_if_startup_message_is_to_long: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#test_throw_error_on_if_startup_message_is_to_short: baseline=absent, patched=passed
  - io.crate.protocols.postgres.PostgresWireProtocolTest#test_throw_error_on_invalid_request_code: baseline=absent, patched=passed
  - io.crate.protocols.postgres.ResultSetReceiverTest#testChannelIsPeriodicallyFlushedToAvoidConsumingTooMuchMemory: baseline=absent, patched=passed
  - io.crate.protocols.postgres.ResultSetReceiverTest#test_channel_is_flushed_if_not_writable_anymore: baseline=absent, patched=passed
  - io.crate.protocols.postgres.ResultSetReceiverTest#test_sendNextRow_future_is_called_once_message_is_written: baseline=absent, patched=passed
