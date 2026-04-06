# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (3): ['io.crate.analysis.common.CommonAnalyzerITest#testSelectFromRoutines', 'io.crate.analysis.common.CommonAnalyzerITest#testShingleFilterWithGraphOutput', 'io.crate.analysis.common.CommonAnalyzerITest#test_select_from_information_schema_with_custom_analyzer']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.analysis.common.CommonAnalyzerITest']
  - io.crate.analysis.common.CommonAnalyzerITest#testSelectFromRoutines: baseline=absent, patched=passed
  - io.crate.analysis.common.CommonAnalyzerITest#testShingleFilterWithGraphOutput: baseline=absent, patched=passed
  - io.crate.analysis.common.CommonAnalyzerITest#test_select_from_information_schema_with_custom_analyzer: baseline=absent, patched=passed
