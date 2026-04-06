# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (2): ['org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testUpdateDatabasesIndexNotReady', 'org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testUpdateDatabasesWriteBlock']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.ingest.geoip.GeoIpDownloaderTests']
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testCleanDatabases: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testGetChunkEndOfStream: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testGetChunkExactlyChunkSize: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testGetChunkLessThanChunkSize: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testGetChunkMoreThanChunkSize: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testGetChunkRethrowsIOException: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testIndexChunks: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testIndexChunksMd5Mismatch: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testIndexChunksNoData: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testProcessDatabaseNew: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testProcessDatabaseSame: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testProcessDatabaseUpdate: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testThatRunDownloaderDeletesExpiredDatabases: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testUpdateDatabases: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testUpdateDatabasesIndexNotReady: baseline=failed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testUpdateDatabasesWriteBlock: baseline=failed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testUpdateTaskState: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.GeoIpDownloaderTests#testUpdateTaskStateError: baseline=passed, patched=passed
