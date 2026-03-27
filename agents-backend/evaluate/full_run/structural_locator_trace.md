# Structural Locator Trace

## Blueprint Summary
- **Root Cause**: Non-equi join conditions were being incorrectly treated as join edges, potentially leading to incorrect join graph construction and query planning.

## Hunk Segregation
- Code files: 1
- Test files: 0

## Code File Mappings

### `server/src/main/java/io/crate/planner/optimizer/joinorder/JoinGraph.java`

**Hunks in this file**: 2

**Git Resolution**: Found `server/src/main/java/io/crate/planner/optimizer/joinorder/JoinGraph.java`

**Agent Tool Steps:**


| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | declaration | `<import>` | `<import>` | 24–24 |
| 2 | core_fix | `createJoinGraph` | `createJoinGraph` | 191–196 |
## Test File Mappings


## Consistency Map

_No renames detected — identity mapping assumed._
