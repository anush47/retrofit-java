# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.types.ObjectTypeTest#test_valueForInsert_on_nested_object']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.types.ObjectTypeTest']
  - io.crate.types.ObjectTypeTest#testResolveInnerType: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#testStreamingOfNullValueWithInnerTypes: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#testStreamingOfNullValueWithoutInnerTypes: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#testStreamingOfValueWithInnerTypes: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#testStreamingOfValueWithoutInnerTypes: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#testStreamingWithEmptyInnerTypes: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#testStreamingWithInnerTypes: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#testStreamingWithoutInnerTypes: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#test_object_type_to_signature_to_object_type_round_trip: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#test_raises_conversion_exception_on_string_parsing_errors: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#test_reference_resolver: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#test_reference_resolver_docvalues_off: baseline=skipped, patched=skipped
  - io.crate.types.ObjectTypeTest#test_reference_resolver_index_and_docvalues_off: baseline=skipped, patched=skipped
  - io.crate.types.ObjectTypeTest#test_reference_resolver_index_off: baseline=skipped, patched=skipped
  - io.crate.types.ObjectTypeTest#test_reference_resolver_with_list: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#test_translog_streaming_roundtrip: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#test_type_streaming_roundtrip: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#test_valueForInsert_on_nested_object: baseline=failed, patched=passed
  - io.crate.types.ObjectTypeTest#test_value_bytes_accounts_for_deep_objects: baseline=passed, patched=passed
  - io.crate.types.ObjectTypeTest#test_value_streaming_roundtrip: baseline=passed, patched=passed
