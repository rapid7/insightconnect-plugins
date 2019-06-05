
# Recorded Future

## About

[Recorded Future](https://www.recordedfuture.com/) arms threat analysts, security operators, and incident responders to rapidly connect the dots and reveal unknown threats by automatically collecting and analyzing threat intelligence from technical, open, and dark web sources.
This plugin utilizes the [Recorded Future API](https://api.recordedfuture.com/v2).

When an action that causes a file to be downloaded is invoked, the file data is parsed internally and returned in the [STIX](https://stixproject.github.io/about/) format.

## Actions

### List IP Addresses Risk Rules

This action is used to list available filtration rules for IP address risk lists.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|None|

### Search Domains

This action is used to search for results related to a specific parent domain.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Firstseen', 'Lastseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|parent|string|None|False|Parent domain|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|None|

### List Domain Risk Rules

This action is used to list available filtration rules for domain risk lists.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|None|

### Search Malware

This action is used to search for data related to malware.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|freetext|string|None|False|Freetext search|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|None|

### Search Entity Lists

This action is used to perform a freetext search across all Recorded Future entity types (IP address, domain, hash, malware, and vulnerability).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|freetext|string|None|True|Freetext search|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|False|None|

### Download Domain Risk List

This action returns a risk list of domains matching a filtration rule.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|list|string|None|False|The risk list to retrieve|['active_phishing_url', 'blacklisted_dns_name', 'cc_dns_name', 'cc_nameserver', 'cc_url', 'compromised_url', 'historical_malware_analysis_dns_name', 'historically_linked_to_cyber_attack', 'large', 'ransomware_distribution_url', 'ransomware_payment_dns_name', 'recent_fast_flux_dns_name', 'recent_malware_analysis_dns_name', 'recently_linked_to_cyber_attack', 'recently_resolved_to_host_of_many_ddns_names', 'recently_resolved_to_malicious_ip', 'recently_resolved_to_suspicious_ip', 'recently_resolved_to_unusual_ip', 'recently_resolved_to_very_malicious_ip', 'sinkhole_dns_name', 'typosquat_similarity__dns_sandwich', 'typosquat_similarity__typo_or_homograph']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|None|

### Search Vulnerabilities

This action is used to search for data related to vulnerabilities.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|freetext|string|None|False|Text query|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|vulnerability_search_data|False|None|

### Search IP Addresses

This action is used to for data related to a specified IP range.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|ip_range|string|None|False|IP address range to search|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|None|

### List Vulnerability Risk Rules

This action is used to retrieve available filtration rules for vulnerability risk lists.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|None|

### Download Hash Risk List

This action is used to returns a list of hashes matching a specified risk rule.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|list|string|None|False|The risk list to retrieve|['large', 'linked_to_attack_vector', 'linked_to_cyber_attack', 'linked_to_malware', 'linked_to_vulnerability', 'positive_malware_verdict', 'threat_researcher']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|None|

### Search Hashes

This action is used to search for data related to hashes of a specified type.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Lastseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|algorithm|string|None|False|Hashing algorithm to search by|['MD5', 'SHA-256', 'SHA-1']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|None|

### Lookup Entity List

This action is used to fetch a specified entity list by ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|entity_list_id|string|None|True|Entity list ID, obtained from the 'Search Entity lists' action|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|False|None|

### Lookup Malware

This action is used to return information about a specific malware entry by ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|malware_ID|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamps|timestamps|False|None|
|entity|entity|False|None|

### Lookup Domain

This action is used to return information about a specific domain entry.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamps|timestamps|False|None|
|entity|entity|False|None|

### Lookup Hash

This action is used to retrieve information about a specified hash.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamps|timestamps|False|None|
|entity|entity|False|None|

### Download IP Addresses Risk List

This action is used to fetch a risk list of the IP addresses that match a specified filtration rule.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|list|string|None|False|The risk list to retrieve|['current_cc_server', 'cyber_exploit_signal_medium', 'historical_bad_ssl_association', 'historical_botnet_traffic', 'historical_cc_server', 'historical_honeypot_sighting', 'historical_multicategory_blacklist', 'historical_open_proxies', 'historical_positive_malware_verdict', 'historical_spam_source', 'historical_sshdictionary_attacker', 'historical_threat_researcher', 'historically_linked_to_apt', 'historically_linked_to_cyber_attack', 'historically_linked_to_intrusion_method', 'honeypot_host', 'inside_possible_bogus_bgp_route', 'large', 'malicious_packet_source', 'malware_delivery', 'nameserver_for_cc_server', 'phishing_host', 'recent_botnet_traffic', 'recent_cc_server', 'recent_honeypot_sighting', 'recent_host_of_many_ddns_names', 'recent_multicategory_blacklist', 'recent_open_proxies', 'recent_positive_malware_verdict', 'recent_spam_source', 'recent_sshdictionary_attacker', 'recent_threat_researcher', 'recently_linked_to_apt', 'recently_linked_to_cyber_attack', 'recently_linked_to_intrusion_method', 'resolution_of_fast_flux_dns_name', 'tor_node', 'unusual_ip', 'vulnerable_host']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|None|

### Lookup IP Address

This action is used to query for data related to a specific IP address.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|IP_address|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamps|timestamps|False|None|
|entity|entity|False|None|

### Download Vulnerability Risk List

This action is used to fetch a risk list of vulnerabilities matching a specified filtration rule.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|list|string|None|False|The risk list to retrieve|['cyber_exploit_signal_critical', 'cyber_exploit_signal_important', 'cyber_exploit_signal_medium', 'historical_scanner_uptake', 'historically_linked_to_exploit_kit', 'historically_linked_to_malware', 'historically_linked_to_ransomware', 'historically_linked_to_remote_access_trojan', 'large', 'linked_to_recent_cyber_exploit', 'nist_severity_critical', 'nist_severity_high', 'nist_severity_low', 'nist_severity_medium', 'recent_scanner_uptake', 'recently_linked_to_exploit_kit', 'recently_linked_to_malware', 'recently_linked_to_ransomware', 'recently_linked_to_remote_access_trojan', 'web_reporting_prior_to_nvd_disclosure']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|None|

### List Hash Risk Rules

This action is used to list available filtration rules for hash risk lists.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|None|

### Lookup Vulnerability

This action is used to fetch information about a specific vulnerability by CVE or RF ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|CVE or RF ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|vulnerability_search_data|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|string|None|False|API Key|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* [Related Domains](https://market.komand.com/snippets/jschipp/related-domains/0.1.0)

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture
* 1.0.1 - Support web server mode | Use new credential types
* 1.0.2 - Fix typo in plugin spec

## References

* [Recorded Future](https://recordedfuture.com)
* [Recorded Future API](https://api.recordedfuture.com/v2)
