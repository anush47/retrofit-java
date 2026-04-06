# Structural Locator Trace

## Blueprint Summary
- **Root Cause**: Deterministic inference: target branch diverges from mainline; adapt hunks with exact target context.

## Hunk Segregation
- Code files: 2
- Test files: 0

## Code File Mappings

### `x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java`

**Hunks in this file**: 2

**Git Resolution**: Found `x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/MigratePlugin.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | declaration | `<import>` | `<import>` | 59–59 |
| 2 | core_fix | `getSettings` | `getSettings` | 160–160 |
### `x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java`

**Hunks in this file**: 4

**Git Resolution**: Found `x-pack/plugin/migrate/src/main/java/org/elasticsearch/xpack/migrate/action/ReindexDataStreamIndexTransportAction.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | declaration | `<import>` | `<import>` | 24–24 |
| 2 | guard | `hunk_2` | `None` | 46–46 |
| 3 | core_fix | `reindex` | `reindex` | 179–179 |
| 4 | core_fix | `hunk_4` | `None` | 184–184 |
## Test File Mappings


## Consistency Map

_No renames detected — identity mapping assumed._
