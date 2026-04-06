# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testEarlyTermination']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.compute.lucene.LuceneSourceOperatorTests']
  - org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testEarlyTermination: baseline=failed, patched=passed
  - org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testEmpty: baseline=passed, patched=passed
  - org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testEmptyWithCranky: baseline=passed, patched=passed
  - org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testOperatorStatus: baseline=passed, patched=passed
  - org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testShardDataPartitioning: baseline=passed, patched=passed
  - org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testShardDataPartitioningWithCranky: baseline=passed, patched=passed
  - org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testSimpleDescription: baseline=passed, patched=passed
  - org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testSimpleToString: baseline=passed, patched=passed
  - org.elasticsearch.compute.lucene.LuceneSourceOperatorTests#testWithCranky: baseline=passed, patched=passed
