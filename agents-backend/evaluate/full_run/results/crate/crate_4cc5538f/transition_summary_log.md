# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (2): ['org.elasticsearch.index.snapshots.blobstore.BlobStoreIndexShardSnapshotsTest#test_bwc_streaming', 'org.elasticsearch.index.snapshots.blobstore.BlobStoreIndexShardSnapshotsTest#test_number_of_unique_files_across_snapshots_equal_to_number_of_files']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.index.snapshots.blobstore.BlobStoreIndexShardSnapshotsTest']
  - org.elasticsearch.index.snapshots.blobstore.BlobStoreIndexShardSnapshotsTest#test_bwc_streaming: baseline=absent, patched=passed
  - org.elasticsearch.index.snapshots.blobstore.BlobStoreIndexShardSnapshotsTest#test_number_of_unique_files_across_snapshots_equal_to_number_of_files: baseline=absent, patched=passed
