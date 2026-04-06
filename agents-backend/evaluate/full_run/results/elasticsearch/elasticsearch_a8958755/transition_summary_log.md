# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (1): ['org.elasticsearch.cluster.metadata.IndexAbstractionResolverTests#testIsNetNewSystemIndexVisible']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.cluster.metadata.IndexAbstractionResolverTests', 'org.elasticsearch.ingest.geoip.FullClusterRestartIT']
  - org.elasticsearch.cluster.metadata.IndexAbstractionResolverTests#testIsIndexVisible: baseline=passed, patched=passed
  - org.elasticsearch.cluster.metadata.IndexAbstractionResolverTests#testIsNetNewSystemIndexVisible: baseline=failed, patched=passed
  - org.elasticsearch.cluster.metadata.IndexAbstractionResolverTests#testResolveIndexAbstractions: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.FullClusterRestartIT: baseline=absent, patched=absent
