# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (15): ['org.elasticsearch.search.functionscore.QueryRescorerIT#testEnforceWindowSize', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testEquivalence', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testExplain', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testFromSize', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testMoreDocs', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testMultipleRescores', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testRescoreAfterCollapse', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testRescoreAfterCollapseRandom', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testRescorePhaseWithInvalidSort', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testRescorePhrase', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testRescoreWithTimeout', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testRescorerMadeScoresWorse', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testScoring', 'org.elasticsearch.search.functionscore.QueryRescorerIT#testSmallRescoreWindow', 'org.elasticsearch.search.rescore.RescorePhaseTests#testRescorePhaseCancellation']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.search.functionscore.QueryRescorerIT', 'org.elasticsearch.search.rescore.RescorePhaseTests']
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testEnforceWindowSize: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testEquivalence: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testExplain: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testFromSize: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testMoreDocs: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testMultipleRescores: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testRescoreAfterCollapse: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testRescoreAfterCollapseRandom: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testRescorePhaseWithInvalidSort: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testRescorePhrase: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testRescoreWithTimeout: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testRescorerMadeScoresWorse: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testScoring: baseline=absent, patched=passed
  - org.elasticsearch.search.functionscore.QueryRescorerIT#testSmallRescoreWindow: baseline=absent, patched=passed
  - org.elasticsearch.search.rescore.RescorePhaseTests#testRescorePhaseCancellation: baseline=absent, patched=passed
