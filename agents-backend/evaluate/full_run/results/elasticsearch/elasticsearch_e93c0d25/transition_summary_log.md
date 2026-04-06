# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.index.mapper.IpPrefixAutomatonUtilTests#testBuildPrefixAutomaton']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.index.mapper.IpPrefixAutomatonUtilTests']
  - org.elasticsearch.index.mapper.IpPrefixAutomatonUtilTests#testAutomatonFromIPv6Group: baseline=passed, patched=passed
  - org.elasticsearch.index.mapper.IpPrefixAutomatonUtilTests#testBuildPrefixAutomaton: baseline=failed, patched=passed
  - org.elasticsearch.index.mapper.IpPrefixAutomatonUtilTests#testCreateIp4PrefixAutomaton: baseline=passed, patched=passed
  - org.elasticsearch.index.mapper.IpPrefixAutomatonUtilTests#testIncompleteDecimalGroupAutomaton: baseline=passed, patched=passed
  - org.elasticsearch.index.mapper.IpPrefixAutomatonUtilTests#testParseIp6Prefix: baseline=passed, patched=passed
