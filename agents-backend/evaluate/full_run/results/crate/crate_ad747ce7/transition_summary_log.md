# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.session.RowConsumerToResultReceiverTest#test_consumer_aborts_if_write_future_fails']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.session.RowConsumerToResultReceiverTest']
  - io.crate.session.RowConsumerToResultReceiverTest#testBatchedIteratorConsumption: baseline=passed, patched=passed
  - io.crate.session.RowConsumerToResultReceiverTest#testExceptionOnAllLoadedCallIsForwardedToResultReceiver: baseline=passed, patched=passed
  - io.crate.session.RowConsumerToResultReceiverTest#test_consumer_aborts_if_write_future_fails: baseline=failed, patched=passed
  - io.crate.session.RowConsumerToResultReceiverTest#test_consumer_pauses_and_resume_based_on_receivers_writablility: baseline=passed, patched=passed
  - io.crate.session.RowConsumerToResultReceiverTest#test_does_not_suspend_consumer_on_last_row: baseline=passed, patched=passed
