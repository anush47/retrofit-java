# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.search.DefaultSearchContextTests#testDetermineMaximumNumberOfSlicesWithQueue']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.search.DefaultSearchContextTests']
  - org.elasticsearch.search.DefaultSearchContextTests#testClearQueryCancellationsOnClose: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testDetermineMaximumNumberOfSlicesEnableQueryPhaseParallelCollection: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testDetermineMaximumNumberOfSlicesNoExecutor: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testDetermineMaximumNumberOfSlicesNotThreadPoolExecutor: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testDetermineMaximumNumberOfSlicesSingleSortByField: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testDetermineMaximumNumberOfSlicesWithQueue: baseline=failed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testFieldHasValue: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testFieldHasValueWithEmptyFieldInfos: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testGetFieldCardinality: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testGetFieldCardinalityNoLeaves: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testGetFieldCardinalityNoLeavesNoGlobalOrdinals: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testGetFieldCardinalityNumeric: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testGetFieldCardinalityRuntimeField: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testGetFieldCardinalityUnmappedField: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testIsParallelCollectionSupportedForResults: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testNewIdLoader: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testNewIdLoaderWithTsdb: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testNewIdLoaderWithTsdbAndRoutingPathMatch: baseline=passed, patched=passed
  - org.elasticsearch.search.DefaultSearchContextTests#testPreProcess: baseline=passed, patched=passed
