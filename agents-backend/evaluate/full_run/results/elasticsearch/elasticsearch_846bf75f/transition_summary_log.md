# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.xpack.redact.RedactProcessorTests#testMatchRedact']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.redact.RedactProcessorTests']
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testDifferentStartAndEnd: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testIgnoreMissing: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testLicenseChanges: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testLicenseChecks: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testMatchRedact: baseline=failed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testMatchRedactMultipleGroks: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testMergeLongestRegion: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testMergeLongestRegion_smallRegionSubsumed: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testMergeOverlappingReplacements_singleItem: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testMergeOverlappingReplacements_sortedByStartPositionNoOverlaps: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testMergeOverlappingReplacements_transitiveOverlaps: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testRedact: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testRedactWithPatternNamesRedacted: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testTraceRedact: baseline=passed, patched=passed
  - org.elasticsearch.xpack.redact.RedactProcessorTests#testTraceRedactMultipleProcessors: baseline=passed, patched=passed
