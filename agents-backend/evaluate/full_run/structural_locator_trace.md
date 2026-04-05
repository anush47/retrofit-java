# Structural Locator Trace

## Blueprint Summary
- **Root Cause**: Deterministic inference: target branch diverges from mainline; adapt hunks with exact target context.

## Hunk Segregation
- Code files: 3
- Test files: 0

## Code File Mappings

### `graylog2-server/src/main/java/org/graylog2/Configuration.java`

**Hunks in this file**: 2

**Git Resolution**: Found `graylog2-server/src/main/java/org/graylog2/Configuration.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | core_fix | `maintainsStreamAwareFieldTypes` | `maintainsStreamAwareFieldTypes` | 295–295 |
| 2 | guard | `withInputs` | `withInputs` | 714–714 |
### `graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java`

**Hunks in this file**: 1

**Git Resolution**: Found `graylog2-server/src/main/java/org/graylog2/rest/resources/system/inputs/InputsResource.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | guard | `throwBadRequestIfNotGlobal` | `throwBadRequestIfNotGlobal` | 309–309 |
### `graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java`

**Hunks in this file**: 1

**Git Resolution**: Found `graylog2-server/src/main/java/org/graylog2/web/resources/AppConfigResource.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | core_fix | `hunk_1` | `None` | 105–105 |
## Test File Mappings


## Consistency Map

_No renames detected — identity mapping assumed._
