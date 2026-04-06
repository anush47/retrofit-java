# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (4): ['org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[ArrayListRowsAndColumns]', 'org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[ColumnBasedFrameRowsAndColumns]', 'org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[CursorFactoryRowsAndColumns]', 'org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[RowBasedFrameRowsAndColumns]']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest']
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[ArrayListRowsAndColumns]: baseline=error, patched=passed
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[ColumnBasedFrameRowsAndColumns]: baseline=error, patched=passed
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[ConcatRowsAndColumns]: baseline=skipped, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[CursorFactoryRowsAndColumns]: baseline=error, patched=passed
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[MapOfColumnsRowsAndColumns]: baseline=skipped, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[NoAs-ArrayListRowsAndColumns]: baseline=skipped, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[NoAs-ColumnBasedFrameRowsAndColumns]: baseline=error, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[NoAs-ConcatRowsAndColumns]: baseline=skipped, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[NoAs-CursorFactoryRowsAndColumns]: baseline=error, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[NoAs-MapOfColumnsRowsAndColumns]: baseline=skipped, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[NoAs-RearrangedRowsAndColumns]: baseline=skipped, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[NoAs-RowBasedFrameRowsAndColumns]: baseline=failed, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[RearrangedRowsAndColumns]: baseline=skipped, patched=skipped
  - org.apache.druid.query.rowsandcols.semantic.EvaluateRowsAndColumnsTest#testMaterializeColumns[RowBasedFrameRowsAndColumns]: baseline=failed, patched=passed
