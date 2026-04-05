# Structural Locator Trace

## Blueprint Summary
- **Root Cause**: Deterministic inference: target branch diverges from mainline; adapt hunks with exact target context.

## Hunk Segregation
- Code files: 2
- Test files: 0

## Code File Mappings

### `server/src/main/java/io/crate/rest/action/RestResultSetReceiver.java`

**Hunks in this file**: 4

**Git Resolution**: Found `server/src/main/java/io/crate/rest/action/RestResultSetReceiver.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | propagation | `hunk_1` | `None` | 34–34 |
| 2 | propagation | `hunk_2` | `None` | 42–42 |
| 3 | propagation | `hunk_3` | `None` | 50–50 |
| 4 | core_fix | `setNextRow` | `setNextRow` | 67–67 |
### `server/src/main/java/io/crate/rest/action/SqlHttpHandler.java`

**Hunks in this file**: 4

**Git Resolution**: Found `server/src/main/java/io/crate/rest/action/SqlHttpHandler.java`

**Deterministic Mode**: raw-diff anchor mapping succeeded (no LLM call).

| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | declaration | `<import>` | `<import>` | 29–29 |
| 2 | propagation | `hunk_2` | `None` | 59–59 |
| 3 | core_fix | `hunk_3` | `None` | 262–262 |
| 4 | declaration | `<class_declaration>` | `<class_declaration>` | 336–336 |
## Test File Mappings


## Consistency Map

_No renames detected — identity mapping assumed._
