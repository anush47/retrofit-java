# Structural Locator Trace

## Blueprint Summary
- **Root Cause**: Deterministic inference: target branch diverges from mainline; adapt hunks with exact target context.

## Hunk Segregation
- Code files: 4
- Test files: 0

## Code File Mappings

### `server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java`

**Hunks in this file**: 10

**Git Resolution**: Found `server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | core_fix | `hunk_1` | `None` | 138–138 |
| 2 | core_fix | `hunk_2` | `None` | 239–239 |
| 3 | core_fix | `hunk_3` | `None` | 405–405 |
| 4 | core_fix | `hunk_4` | `None` | 655–655 |
| 5 | core_fix | `hunk_5` | `None` | 660–660 |
| 6 | core_fix | `hunk_6` | `None` | 660–660 |
| 7 | core_fix | `hunk_7` | `None` | 134–134 |
| 8 | core_fix | `hunk_8` | `None` | 660–660 |
| 9 | core_fix | `hunk_9` | `None` | 660–660 |
| 10 | core_fix | `hunk_10` | `None` | 1047–1047 |
### `server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java`

**Hunks in this file**: 2

**Git Resolution**: Found `server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | declaration | `<import>` | `<import>` | 12–12 |
| 2 | guard | `hunk_2` | `None` | 341–341 |
### `server/src/main/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapper.java`

**Hunks in this file**: 1

**Git Resolution**: Found `server/src/main/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapper.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | core_fix | `hunk_1` | `None` | 57–57 |
### `server/src/main/java/org/elasticsearch/index/mapper/MapperFeatures.java`

**Hunks in this file**: 1

**Git Resolution**: Found `server/src/main/java/org/elasticsearch/index/mapper/MapperFeatures.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | guard | `getTestFeatures` | `getTestFeatures` | 55–55 |
## Test File Mappings


## Consistency Map

_No renames detected — identity mapping assumed._
