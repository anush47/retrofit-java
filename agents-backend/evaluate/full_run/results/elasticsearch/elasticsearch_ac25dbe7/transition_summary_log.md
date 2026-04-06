# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (8): ['org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testAsnFree', 'org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testAsnStandard', 'org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testCountryFree', 'org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testDatabaseTypeParsing', 'org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testGeolocationInvariants', 'org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testGeolocationStandard', 'org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testPrivacyDetectionStandard', 'org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testPrivacyDetectionStandardNonEmptyService']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.ingest.geoip.GeoIpProcessorTests', 'org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests']
  - org.elasticsearch.ingest.geoip.GeoIpProcessorTests: baseline=absent, patched=absent
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testAsnFree: baseline=failed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testAsnInvariants: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testAsnStandard: baseline=failed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testCountryFree: baseline=failed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testDatabaseTypeParsing: baseline=failed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testGeolocationInvariants: baseline=failed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testGeolocationStandard: baseline=failed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testIpinfoTypeCleanup: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testParseAsn: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testParseBoolean: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testParseLocationDouble: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testPrivacyDetectionInvariants: baseline=passed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testPrivacyDetectionStandard: baseline=failed, patched=passed
  - org.elasticsearch.ingest.geoip.IpinfoIpDataLookupsTests#testPrivacyDetectionStandardNonEmptyService: baseline=failed, patched=passed
