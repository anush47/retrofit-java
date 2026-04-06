# Transition Summary

- Source: phase0_cache
- Valid backport signal: False
- Reason: Invalid: git apply --check failed. error: patch failed: x-pack/plugin/migrate/build.gradle:17
error: x-pack/plugin/migrate/build.gradle: patch does not apply

- fail->pass (0): []
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.migrate.action.CopyLifecycleIndexMetadataTransportActionIT']
  - org.elasticsearch.xpack.migrate.action.CopyLifecycleIndexMetadataTransportActionIT: baseline=absent, patched=unknown
