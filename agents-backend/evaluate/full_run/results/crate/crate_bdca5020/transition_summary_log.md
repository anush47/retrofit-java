# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.types.FloatVectorTypeTest#test_cannot_create_float_vector_type_exceeding_max_length']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.types.FloatVectorTypeTest']
  - io.crate.types.FloatVectorTypeTest#test_cannot_create_float_vector_type_exceeding_max_length: baseline=failed, patched=passed
  - io.crate.types.FloatVectorTypeTest#test_cannot_insert_nulls_into_float_vector: baseline=passed, patched=passed
  - io.crate.types.FloatVectorTypeTest#test_reference_resolver: baseline=passed, patched=passed
  - io.crate.types.FloatVectorTypeTest#test_reference_resolver_docvalues_off: baseline=passed, patched=passed
  - io.crate.types.FloatVectorTypeTest#test_reference_resolver_index_and_docvalues_off: baseline=passed, patched=passed
  - io.crate.types.FloatVectorTypeTest#test_reference_resolver_index_off: baseline=passed, patched=passed
  - io.crate.types.FloatVectorTypeTest#test_reference_resolver_with_list: baseline=skipped, patched=skipped
  - io.crate.types.FloatVectorTypeTest#test_translog_streaming_roundtrip: baseline=passed, patched=passed
  - io.crate.types.FloatVectorTypeTest#test_type_streaming_roundtrip: baseline=passed, patched=passed
  - io.crate.types.FloatVectorTypeTest#test_value_streaming_roundtrip: baseline=passed, patched=passed
