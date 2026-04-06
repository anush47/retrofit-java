# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.xpack.ml.aggs.changepoint.SpikeAndDipDetectorTests#testSpikeAtTail']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.ml.aggs.changepoint.SpikeAndDipDetectorTests']
  - org.elasticsearch.xpack.ml.aggs.changepoint.SpikeAndDipDetectorTests#testDetection: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.aggs.changepoint.SpikeAndDipDetectorTests#testExludedValues: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.aggs.changepoint.SpikeAndDipDetectorTests#testMissingBuckets: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.aggs.changepoint.SpikeAndDipDetectorTests#testSpikeAndDipValues: baseline=passed, patched=passed
  - org.elasticsearch.xpack.ml.aggs.changepoint.SpikeAndDipDetectorTests#testSpikeAtTail: baseline=failed, patched=passed
  - org.elasticsearch.xpack.ml.aggs.changepoint.SpikeAndDipDetectorTests#testTooLittleData: baseline=passed, patched=passed
