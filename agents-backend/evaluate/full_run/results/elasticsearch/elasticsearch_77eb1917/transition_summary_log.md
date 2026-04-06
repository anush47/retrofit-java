# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (0): []
- newly passing (24): ['org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeDescriptionWithoutAttributes', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeIsCreatedWithHostFromInetAddress', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeIsRemoteClusterClientDefault', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeIsRemoteClusterClientSet', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeIsRemoteClusterClientUnset', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeMinReadOnlyVersionSerialization', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeRoleWithOldVersion', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeSerializationKeepsHost', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeToString', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeToXContent', 'org.elasticsearch.cluster.node.DiscoveryNodeTests#testRolesAreSorted', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructor', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructorClusterHealthStatusMustNotBeNull', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructorClusterMustNotBeNull', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructorClusterNameMustNotBeNull', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructorVersionMustNotBeNull', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testCreateMonitoringDoc', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testMonitoringNodeConstructor', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testMonitoringNodeEqualsAndHashcode', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testMonitoringNodeSerialization', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testMonitoringNodeToXContent', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testNodesHash', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testToXContent', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testToXContentContainsCommonFields']
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.action.admin.cluster.reroute.ClusterRerouteResponseTests', 'org.elasticsearch.cluster.ClusterStateTests', 'org.elasticsearch.cluster.node.DiscoveryNodeTests', 'org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests']
  - org.elasticsearch.action.admin.cluster.reroute.ClusterRerouteResponseTests: baseline=absent, patched=absent
  - org.elasticsearch.cluster.ClusterStateTests: baseline=absent, patched=absent
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeDescriptionWithoutAttributes: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeIsCreatedWithHostFromInetAddress: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeIsRemoteClusterClientDefault: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeIsRemoteClusterClientSet: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeIsRemoteClusterClientUnset: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeMinReadOnlyVersionSerialization: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeRoleWithOldVersion: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeSerializationKeepsHost: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeToString: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testDiscoveryNodeToXContent: baseline=absent, patched=passed
  - org.elasticsearch.cluster.node.DiscoveryNodeTests#testRolesAreSorted: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructor: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructorClusterHealthStatusMustNotBeNull: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructorClusterMustNotBeNull: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructorClusterNameMustNotBeNull: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testConstructorVersionMustNotBeNull: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testCreateMonitoringDoc: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testMonitoringNodeConstructor: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testMonitoringNodeEqualsAndHashcode: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testMonitoringNodeSerialization: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testMonitoringNodeToXContent: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testNodesHash: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testToXContent: baseline=absent, patched=passed
  - org.elasticsearch.xpack.monitoring.collector.cluster.ClusterStatsMonitoringDocTests#testToXContentContainsCommonFields: baseline=absent, patched=passed
