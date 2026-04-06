# Structural Locator Trace

## Blueprint Summary
- **Root Cause**: Deterministic inference: target branch diverges from mainline; adapt hunks with exact target context.

## Hunk Segregation
- Code files: 4
- Test files: 0

## Code File Mappings

### `server/src/main/java/org/elasticsearch/index/codec/vectors/ES814ScalarQuantizedVectorsFormat.java`

**Hunks in this file**: 2

**Git Resolution**: Found `server/src/main/java/org/elasticsearch/index/codec/vectors/ES814ScalarQuantizedVectorsFormat.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | declaration | `<import>` | `<import>` | 41–41 |
| 2 | guard | `getMaxDimensions` | `getMaxDimensions` | 274–274 |
### `server/src/main/java/org/elasticsearch/index/codec/vectors/ES815BitFlatVectorsFormat.java`

**Hunks in this file**: 2

**Git Resolution**: Found `server/src/main/java/org/elasticsearch/index/codec/vectors/ES815BitFlatVectorsFormat.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | declaration | `<import>` | `<import>` | 26–26 |
| 2 | guard | `getMaxDimensions` | `getMaxDimensions` | 43–43 |
### `server/src/main/java/org/elasticsearch/index/mapper/vectors/DenseVectorFieldMapper.java`

**Hunks in this file**: 1

**Git Resolution**: Found `server/src/main/java/org/elasticsearch/index/mapper/vectors/DenseVectorFieldMapper.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | core_fix | `hunk_1` | `None` | 2033–2033 |
### `server/src/main/java/org/elasticsearch/rest/action/search/SearchCapabilities.java`

**Hunks in this file**: 1

**Git Resolution**: Found `server/src/main/java/org/elasticsearch/rest/action/search/SearchCapabilities.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | declaration | `<class_declaration>` | `<class_declaration>` | 24–24 |
## Test File Mappings


## Consistency Map

_No renames detected — identity mapping assumed._
