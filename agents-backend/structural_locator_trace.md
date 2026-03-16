# Structural Locator Trace

## Blueprint Summary
- **Root Cause**: The code previously added all server types to the workerIds list, potentially including non-historical servers, which could lead to incorrect worker assignment or processing errors.

## Hunk Segregation
- Code files: 1
- Test files: 0

## Code File Mappings

### `extensions-core/multi-stage-query/src/main/java/org/apache/druid/msq/dart/controller/DartControllerContext.java`

**Hunks in this file**: 2

**Git Resolution**: Found `extensions-core/multi-stage-query/src/main/java/org/apache/druid/msq/dart/controller/DartControllerContext.java`

**Agent Tool Steps:**


| Hunk Idx | Role | Mainline Method | Target Method | Lines |
|---|---|---|---|---|
| 1 | declaration | `<import>` | `<import>` | 49–49 |
| 2 | core_fix | `None` | `someMethodContainingWorkerIdsLoop` | 124–128 |
## Test File Mappings


## Consistency Map

_No renames detected — identity mapping assumed._
