# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (5): ['io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_consecutive_retries_will_not_result_in_duplicate_reads', 'io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_iterator_closes_current_reader_and_throws_exception_on_fail_fast', 'io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_iterator_closes_current_reader_on_io_error', 'io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_loadNextBatch_implements_retry_with_backoff', 'io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_retry_from_one_uri_does_not_affect_reading_next_uri']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.execution.engine.collect.files.FileReadingIteratorTest']
  - io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_consecutive_retries_will_not_result_in_duplicate_reads: baseline=absent, patched=passed
  - io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_iterator_closes_current_reader_and_throws_exception_on_fail_fast: baseline=absent, patched=passed
  - io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_iterator_closes_current_reader_on_io_error: baseline=absent, patched=passed
  - io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_loadNextBatch_implements_retry_with_backoff: baseline=absent, patched=passed
  - io.crate.execution.engine.collect.files.FileReadingIteratorTest#test_retry_from_one_uri_does_not_affect_reading_next_uri: baseline=absent, patched=passed
