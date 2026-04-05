# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.types.GeoPointTypeTest#test_return_null_when_converting_values_containing_null_to_geo_point']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.types.GeoPointTypeTest']
  - io.crate.types.GeoPointTypeTest#testConversionFromIntegerArray: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#testConversionFromObjectArrayOfIntegers: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#testInvalidWktToGeoPointValue: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#testStreaming: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#testValueConversionFromList: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#testWktToGeoPointValue: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#test_cast_double_geo_point_value_with_invalid_latitude_throws_exception: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#test_cast_double_geo_point_value_with_invalid_longitude_throws_exception: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#test_reference_resolver: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#test_reference_resolver_docvalues_off: baseline=skipped, patched=skipped
  - io.crate.types.GeoPointTypeTest#test_reference_resolver_index_and_docvalues_off: baseline=skipped, patched=skipped
  - io.crate.types.GeoPointTypeTest#test_reference_resolver_index_off: baseline=skipped, patched=skipped
  - io.crate.types.GeoPointTypeTest#test_reference_resolver_with_list: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#test_return_null_when_converting_values_containing_null_to_geo_point: baseline=error, patched=passed
  - io.crate.types.GeoPointTypeTest#test_sanitize_list_of_doubles_value: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#test_translog_streaming_roundtrip: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#test_type_streaming_roundtrip: baseline=passed, patched=passed
  - io.crate.types.GeoPointTypeTest#test_value_streaming_roundtrip: baseline=passed, patched=passed
