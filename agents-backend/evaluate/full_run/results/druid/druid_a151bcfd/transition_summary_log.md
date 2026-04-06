# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (4): ['org.apache.druid.msq.exec.MSQExportTest#testExport', 'org.apache.druid.msq.exec.MSQExportTest#testExport2', 'org.apache.druid.msq.exec.MSQExportTest#testNumberOfRowsPerFile', 'org.apache.druid.msq.querykit.results.ExportResultsFrameProcessorFactoryTest#testSerde']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.apache.druid.msq.exec.MSQExportTest', 'org.apache.druid.msq.querykit.results.ExportResultsFrameProcessorFactoryTest']
  - org.apache.druid.msq.exec.MSQExportTest#testExport: baseline=absent, patched=passed
  - org.apache.druid.msq.exec.MSQExportTest#testExport2: baseline=absent, patched=passed
  - org.apache.druid.msq.exec.MSQExportTest#testNumberOfRowsPerFile: baseline=absent, patched=passed
  - org.apache.druid.msq.querykit.results.ExportResultsFrameProcessorFactoryTest#testSerde: baseline=absent, patched=passed
