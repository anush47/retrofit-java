# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (2): ['org.elasticsearch.threadpool.ThreadPoolTest#test_force_merge_pool_size', 'org.elasticsearch.threadpool.ThreadPoolTest#test_one_eight_of_processors']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.threadpool.ThreadPoolTest']
  - org.elasticsearch.threadpool.ThreadPoolTest#test_force_merge_pool_size: baseline=absent, patched=passed
  - org.elasticsearch.threadpool.ThreadPoolTest#test_one_eight_of_processors: baseline=absent, patched=passed
