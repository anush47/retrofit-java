# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (8): ['io.crate.replication.logical.action.GetFileChunkActionTest#test_bwc_can_resolve_shards_using_index_names_before_6_1', 'io.crate.replication.logical.action.GetStoreMetadataActionTest#test_bwc_can_resolve_shards_using_index_names_before_6_1', 'io.crate.replication.logical.action.ReleasePublisherResourcesActionTest#test_bwc_can_resolve_shards_using_index_names_before_6_1', 'io.crate.replication.logical.action.ShardChangesActionTest#test_bwc_can_resolve_shards_using_index_names_before_6_1', 'io.crate.replication.logical.seqno.RetentionLeaseHelperTest#test_retention_lease_id_for_shard', 'org.elasticsearch.action.support.single.shard.SingleShardRequestTest#test_streaming', 'org.elasticsearch.action.support.single.shard.SingleShardRequestTest#test_streaming_bwc_before_6_1', 'org.elasticsearch.index.seqno.RetentionLeaseActionsTest#test_bwc_can_resolve_shards_using_index_names_before_6_1']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['io.crate.replication.logical.action.GetFileChunkActionTest', 'io.crate.replication.logical.action.GetStoreMetadataActionTest', 'io.crate.replication.logical.action.ReleasePublisherResourcesActionTest', 'io.crate.replication.logical.action.ShardChangesActionTest', 'io.crate.replication.logical.seqno.RetentionLeaseHelperTest', 'org.elasticsearch.action.support.single.shard.SingleShardRequestTest', 'org.elasticsearch.index.seqno.RetentionLeaseActionsTest']
  - io.crate.replication.logical.action.GetFileChunkActionTest#test_bwc_can_resolve_shards_using_index_names_before_6_1: baseline=absent, patched=passed
  - io.crate.replication.logical.action.GetStoreMetadataActionTest#test_bwc_can_resolve_shards_using_index_names_before_6_1: baseline=absent, patched=passed
  - io.crate.replication.logical.action.ReleasePublisherResourcesActionTest#test_bwc_can_resolve_shards_using_index_names_before_6_1: baseline=absent, patched=passed
  - io.crate.replication.logical.action.ShardChangesActionTest#test_bwc_can_resolve_shards_using_index_names_before_6_1: baseline=absent, patched=passed
  - io.crate.replication.logical.seqno.RetentionLeaseHelperTest#test_retention_lease_id_for_shard: baseline=absent, patched=passed
  - org.elasticsearch.action.support.single.shard.SingleShardRequestTest#test_streaming: baseline=absent, patched=passed
  - org.elasticsearch.action.support.single.shard.SingleShardRequestTest#test_streaming_bwc_before_6_1: baseline=absent, patched=passed
  - org.elasticsearch.index.seqno.RetentionLeaseActionsTest#test_bwc_can_resolve_shards_using_index_names_before_6_1: baseline=absent, patched=passed
