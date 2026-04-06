# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (4): ['org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testMultipleHyphensInDataStreamName', 'org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testNonMatchingTemplateIndexPattern', 'org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testWithCustomComponentTemplatesOnly', 'org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testWithoutLogsComponentTemplate']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests']
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testBeforeAndAFterSettingUpdate: baseline=passed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testCaseSensitivity: baseline=passed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testLogsDbDisabled: baseline=passed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testMultipleHyphensInDataStreamName: baseline=failed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testNonLogsDataStream: baseline=passed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testNonMatchingTemplateIndexPattern: baseline=failed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testOnExplicitStandardIndex: baseline=passed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testOnExplicitTimeSeriesIndex: baseline=passed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testOnIndexCreation: baseline=passed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testWithCustomComponentTemplatesOnly: baseline=failed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testWithLogsComponentTemplate: baseline=passed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testWithMultipleComponentTemplates: baseline=passed, patched=passed
  - org.elasticsearch.xpack.logsdb.LogsdbIndexModeSettingsProviderTests#testWithoutLogsComponentTemplate: baseline=failed, patched=passed
