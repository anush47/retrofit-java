# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.xpack.ml.inference.ltr.QueryFeatureExtractorTests#testEmptyDisiPriorityQueue']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.ml.inference.ltr.QueryFeatureExtractorTests']
  - org.elasticsearch.xpack.ml.inference.ltr.QueryFeatureExtractorTests#testEmptyDisiPriorityQueue: baseline=failed, patched=passed
  - org.elasticsearch.xpack.ml.inference.ltr.QueryFeatureExtractorTests#testQueryExtractor: baseline=skipped, patched=skipped
