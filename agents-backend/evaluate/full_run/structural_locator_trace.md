# Structural Locator Trace

## Blueprint Summary
- **Root Cause**: Deterministic inference: target branch diverges from mainline; adapt hunks with exact target context.

## Hunk Segregation
- Code files: 1
- Test files: 0

## Code File Mappings

### `x-pack/plugin/logsdb/src/main/java/org/elasticsearch/xpack/logsdb/LogsdbIndexModeSettingsProvider.java`

**Hunks in this file**: 3

**Git Resolution**: Found `x-pack/plugin/logsdb/src/main/java/org/elasticsearch/xpack/logsdb/LogsdbIndexModeSettingsProvider.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | propagation | `hunk_1` | `None` | 10–10 |
| 2 | guard | `hunk_2` | `None` | 57–57 |
| 3 | core_fix | `usesLogsAtSettingsComponentTemplate` | `usesLogsAtSettingsComponentTemplate` | 72–72 |
## Test File Mappings


## Consistency Map

_No renames detected — identity mapping assumed._
