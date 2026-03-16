# Structural Locator Trace

## Blueprint Summary
- **Root Cause**: The controller built the list of worker IDs from *all* Druid servers, including non‑historical types (e.g., broker, coordinator). Those servers cannot execute query stages, causing task assignment failures or runtime errors.

## Hunk Segregation
- Code files: 1
- Test files: 1

## Code File Mappings

### `extensions-core/multi-stage-query/src/main/java/org/apache/druid/msq/dart/controller/DartControllerContext.java`

❌ Failed to extract mapping.

## Test File Mappings

- `extensions-core/multi-stage-query/src/test/java/org/apache/druid/msq/dart/controller/DartControllerContextTest.java` → **null** (test synthesis required by Agent 4) ⚠️

## Consistency Map

_No renames detected — identity mapping assumed._
