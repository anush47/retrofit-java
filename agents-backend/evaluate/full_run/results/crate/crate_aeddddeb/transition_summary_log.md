# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['io.crate.metadata.sys.SysAllocationsTableInfoTest#test_exception_is_thrown_when_no_master_is_discovered']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.metadata.sys.SysAllocationsTableInfoTest']
  - io.crate.metadata.sys.SysAllocationsTableInfoTest#test_exception_is_thrown_when_no_master_is_discovered: baseline=failed, patched=passed
  - io.crate.metadata.sys.SysAllocationsTableInfoTest#test_table_is_routed_to_master_node: baseline=passed, patched=passed
