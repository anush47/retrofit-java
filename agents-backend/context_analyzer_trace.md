# Context Analyzer Trace

## File: `extensions-core/multi-stage-query/src/main/java/org/apache/druid/msq/exec/ControllerImpl.java`

**Method focused**: `Unknown`
**Hunk count**: 1

**Status**: LLM extraction failed — using fallback blueprint.

## File: `extensions-core/multi-stage-query/src/main/java/org/apache/druid/msq/querykit/results/ExportResultsFrameProcessor.java`

**Method focused**: `createRowSignatureForExport`
**Hunk count**: 9

**Status**: LLM extraction failed — using fallback blueprint.

## File: `extensions-core/multi-stage-query/src/main/java/org/apache/druid/msq/querykit/results/ExportResultsFrameProcessorFactory.java`

**Method focused**: `getColumnMappings`
**Hunk count**: 5

**Status**: LLM extraction failed — using fallback blueprint.


## Consolidated Blueprint

**Patch Intent**: [Fallback] LLM extraction failed.

- **Root Cause**: [Fallback] Patch modifies extensions-core/multi-stage-query/src/main/java/org/apache/druid/msq/exec/ControllerImpl.java. LLM extraction failed. | [Fallback] Patch modifies extensions-core/multi-stage-query/src/main/java/org/apache/druid/msq/querykit/results/ExportResultsFrameProcessor.java. LLM extraction failed. | [Fallback] Patch modifies extensions-core/multi-stage-query/src/main/java/org/apache/druid/msq/querykit/results/ExportResultsFrameProcessorFactory.java. LLM extraction failed.
- **Fix Logic**: [Fallback] Added lines: ['resultFormat,', 'columnMappings'] | [Fallback] Added lines: ['import it.unimi.dsi.fastutil.objects.Object2IntMap;', 'import it.unimi.dsi.fastutil.objects.Object2IntOpenHashMap;', 'import org.apache.druid.sql.calcite.planner.ColumnMapping;'] | [Fallback] Added lines: ['import com.fasterxml.jackson.annotation.JsonInclude;', 'import org.apache.druid.sql.calcite.planner.ColumnMappings;', 'private final ColumnMappings columnMappings;']
- **Dependent APIs**: []

### Full Hunk Chain (Cross-File)


