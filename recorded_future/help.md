# Description

[Recorded Future](https://www.recordedfuture.com/) arms threat analysts, security operators, and incident
  responders to rapidly connect the dots and reveal unknown threats. Using the Recorded Future plugin for Rapid7
InsightConnect, users can search domain lists, entity lists, and more.

Use Recorded Future within an automation workflow to quickly assist with threat analysis, incident response, and
vulnerability management.

Note: When a plugin action that causes a file to be downloaded is invoked, the file data is parsed internally and
returned in the [STIX](https://stixproject.github.io/about/) format.

# Key Features

* Search domain lists
* Download risk lists
* Lookup and search hashes

# Requirements

* Recorded Future API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|string|None|False|API Key|None|

## Technical Details

### Actions

#### List IP Addresses Risk Rules

This action is used to list available filtration rules for IP address risk lists.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|None|

#### Search Domains

This action is used to search for results related to a specific parent domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Firstseen', 'Lastseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|parent|string|None|False|Parent domain|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|None|

#### List Domain Risk Rules

This action is used to list available filtration rules for domain risk lists.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|None|

#### Search Malware

This action is used to search for data related to malware.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|freetext|string|None|False|Freetext search|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|None|

#### Search Entity Lists

This action is used to perform a freetext search across all Recorded Future entity types (IP address, domain, hash, malware, and vulnerability).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|freetext|string|None|True|Freetext search|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|False|None|

#### Download Domain Risk List

This action returns a risk list of domains matching a filtration rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|list|string|None|False|The risk list to retrieve|['active_phishing_url', 'blacklisted_dns_name', 'cc_dns_name', 'cc_nameserver', 'cc_url', 'compromised_url', 'historical_malware_analysis_dns_name', 'historically_linked_to_cyber_attack', 'large', 'ransomware_distribution_url', 'ransomware_payment_dns_name', 'recent_fast_flux_dns_name', 'recent_malware_analysis_dns_name', 'recently_linked_to_cyber_attack', 'recently_resolved_to_host_of_many_ddns_names', 'recently_resolved_to_malicious_ip', 'recently_resolved_to_suspicious_ip', 'recently_resolved_to_unusual_ip', 'recently_resolved_to_very_malicious_ip', 'sinkhole_dns_name', 'typosquat_similarity__dns_sandwich', 'typosquat_similarity__typo_or_homograph']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|None|

#### Search Vulnerabilities

This action is used to search for data related to vulnerabilities.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|freetext|string|None|False|Text query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|vulnerability_search_data|False|None|

#### Search IP Addresses

This action is used to for data related to a specified IP range.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|ip_range|string|None|False|IP address range to search|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|None|

#### List Vulnerability Risk Rules

This action is used to retrieve available filtration rules for vulnerability risk lists.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|None|

#### Download Hash Risk List

This action is used to returns a list of hashes matching a specified risk rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|list|string|None|False|The risk list to retrieve|['large', 'linked_to_attack_vector', 'linked_to_cyber_attack', 'linked_to_malware', 'linked_to_vulnerability', 'positive_malware_verdict', 'threat_researcher']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|None|

#### Search Hashes

This action is used to search for data related to hashes of a specified type.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Lastseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|
|limit|number|None|True|Number of results to retrieve, up to 100|None|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|
|from|number|None|True|What number record to start from|None|
|algorithm|string|None|False|Hashing algorithm to search by|['MD5', 'SHA-256', 'SHA-1']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|None|

#### Lookup Entity List

This action is used to fetch a specified entity list by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|entity_list_id|string|None|True|Entity list ID, obtained from the 'Search Entity lists' action|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|False|None|

#### Lookup Malware

This action is used to return information about a specific malware entry by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|malware_ID|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamps|timestamps|False|None|
|entity|entity|False|None|

#### Lookup Domain

This action is used to return information about a specific domain entry.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|Add a comment to a domain|None|
|domain|string|None|True|Domain|None|
|fields|[]string|None|False|List of fields to include with results e.g ["sightings", "threatLists", "analystNotes", "counts", "entity", "intelCard", "metrics", "relatedEntities" , "risk" , "timestamps"]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analystNotes|[]string|False|Notes from an analyst|
|counts|[]counts|False|Counts|
|entity|entity|False|Entity|
|intelCard|string|False|Intel card|
|metrics|[]metrics|False|Metrics|
|relatedEntities|[]relatedEntities|False|Related entities|
|risk|risk|False|Risk|
|sightings|[]sightings|False|Sightings|
|threatLists|[]string|False|Threat lists|
|timestamps|timestamps|False|Timestamps|

Example output:

```
{
  "data": {
    "entity": {
      "id": "idn:google.com",
      "name": "google.com",
      "type": "InternetDomainName"
    },
    "timestamps": {
      "firstSeen": "2009-01-23T02:00:08.000Z",
      "lastSeen": "2019-07-25T15:44:00.328Z"
    }
  }
}
```

#### Lookup Hash

This action is used to retrieve information about a specified hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|Add a comment to a hash|None|
|fields|[]string|None|False|List of fields to include with results e.g ["timestamps", "sightings", "threatLists", "analystNotes", "counts", "entity", "hashAlgorithm", "intelCard", "metrics", "relatedEntities", "risk", "timestamps"]|None|
|hash|string|None|True|Hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analystNotes|[]string|False|Notes from an analyst|
|counts|[]counts|False|Counts|
|entity|entity|False|Entity|
|hashAlgorithm|string|False|Hash Algorithm|
|intelCard|string|False|Intel card|
|metrics|[]metrics|False|Metrics|
|relatedEntities|[]relatedEntities|False|Related entities|
|risk|risk|False|Risk|
|sightings|[]sightings|False|Sightings|
|threatLists|[]string|False|Threat Lists|
|timestamps|timestamps|False|Timestamps|

Example output:

```
{
  "data": {
    "risk": {
      "criticalityLabel": "Malicious",
      "score": 68,
      "evidenceDetails": [
        {
          "timestamp": "2015-06-17T15:09:38.000Z",
          "criticalityLabel": "Unusual",
          "evidenceString": "3 sightings on 1 source: Kaspersky Securelist and Lab. Most recent link (Jun 17, 2015): https://securelist.ru/blog/issledovaniya/25905/modul-duqu-2-0-soxranyayushhij-prisutstvie-v-seti/",
          "rule": "Threat Researcher",
          "criticality": 1
        },
        {
          "timestamp": "2015-06-17T15:09:38.000Z",
          "criticalityLabel": "Suspicious",
          "evidenceString": "6 sightings on 3 sources: Kaspersky Securelist and Lab, Hei Shou, www.hx95.com. 2 related malwares: Duqu2, Computer Worm. Most recent link (Jun 17, 2015): https://securelist.ru/blog/issledovaniya/25905/modul-duqu-2-0-soxranyayushhij-prisutstvie-v-seti/",
          "rule": "Linked to Malware",
          "criticality": 2
        },
        {
          "timestamp": "2015-06-14T00:00:00.000Z",
          "criticalityLabel": "Malicious",
          "evidenceString": "1 sighting on 1 source: VirusTotal. Most recent link (Jun 14, 2015): https://www.virustotal.com/en/file/bc4ae56434b45818f57724f4cd19354a13e5964fd097d1933a30e2e31c9bdfa5/analysis/",
          "rule": "Positive Malware Verdict",
          "criticality": 3
        }
      ],
      "riskString": "3/12",
      "rules": 3,
      "criticality": 3,
      "riskSummary": "3 of 12 Risk Rules currently observed."
    },
    "analystNotes": []
  },
  "warnings": [
    "Unknown field nope"
  ]
}
```

#### Lookup URL

This action is used to retrieve information about a specified URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|Add a comment to an IP address lookup for Recorded Future|None|
|fields|[]string|None|False|List of fields to include with results e.g ["sightings", "analystNotes", "counts", "entity", "metrics", "relatedEntities", "risk", "timestamps"]|None|
|url|string|None|True|URL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analystNotes|[]string|False|Notes from an analyst|
|counts|[]counts|False|Counts|
|entity|entity|False|Entity|
|metrics|[]metrics|False|Metrics|
|relatedEntities|[]relatedEntities|False|Related entities|
|risk|risk|False|Risk|
|sightings|[]sightings|False|Sightings|
|timestamps|timestamps|False|Timestamps|

Example output:

```
{
  "entity": {
    "id": "url:http://www.google.com",
    "name": "http://www.google.com",
    "type": "URL"
  },
  "timestamps": {
    "firstSeen": "2019-07-26T00:00:00.000Z",
    "lastSeen": "2019-07-26T23:59:59.000Z"
  }
}

```

#### Download IP Addresses Risk List

This action is used to fetch a risk list of the IP addresses that match a specified filtration rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|list|string|None|False|The risk list to retrieve|['current_cc_server', 'cyber_exploit_signal_medium', 'historical_bad_ssl_association', 'historical_botnet_traffic', 'historical_cc_server', 'historical_honeypot_sighting', 'historical_multicategory_blacklist', 'historical_open_proxies', 'historical_positive_malware_verdict', 'historical_spam_source', 'historical_sshdictionary_attacker', 'historical_threat_researcher', 'historically_linked_to_apt', 'historically_linked_to_cyber_attack', 'historically_linked_to_intrusion_method', 'honeypot_host', 'inside_possible_bogus_bgp_route', 'large', 'malicious_packet_source', 'malware_delivery', 'nameserver_for_cc_server', 'phishing_host', 'recent_botnet_traffic', 'recent_cc_server', 'recent_honeypot_sighting', 'recent_host_of_many_ddns_names', 'recent_multicategory_blacklist', 'recent_open_proxies', 'recent_positive_malware_verdict', 'recent_spam_source', 'recent_sshdictionary_attacker', 'recent_threat_researcher', 'recently_linked_to_apt', 'recently_linked_to_cyber_attack', 'recently_linked_to_intrusion_method', 'resolution_of_fast_flux_dns_name', 'tor_node', 'unusual_ip', 'vulnerable_host']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|None|

#### Lookup IP Address

This action is used to query for data related to a specific IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|IP_address|string|None|True|IP address|None|
|comment|string|None|False|Add comment to IP address lookup for Recorded Future|None|
|fields|[]string|None|False|List of fields to include with results e.g ["sightings", "threatLists", "analystNotes", "counts", "entity", "intelCard", "metrics", "relatedEntities", "riskyCIDRIPs","risk", "location", "timestamps"]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analystNotes|[]string|False|Notes from an analyst|
|counts|[]counts|False|Counts|
|entity|entity|False|Entity|
|intelCard|string|False|Intel card|
|location|location|False|Location|
|metrics|[]metrics|False|Metrics|
|relatedEntities|[]relatedEntities|False|Related entities|
|risk|risk|False|Risk|
|riskyCIDRIPs|[]riskyCIDRIP|False|Risky CIDR IPs|
|sightings|[]sightings|False|Sightings|
|threatLists|[]string|False|Threat lists|
|timestamps|timestamps|False|Timestamps|
|found|boolean|False|Has the IP been found in Recorded Future|

Example output:

```
{
  "entity": {
    "id": "ip:8.8.8.8",
    "name": "8.8.8.8",
    "type": "IpAddress"
  },
  "timestamps": {
    "firstSeen": "2010-04-27T12:46:51.000Z",
    "lastSeen": "2019-07-26T15:26:50.084Z"
  }
}
```

#### Download Vulnerability Risk List

This action is used to fetch a risk list of vulnerabilities matching a specified filtration rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|list|string|None|False|The risk list to retrieve|['cyber_exploit_signal_critical', 'cyber_exploit_signal_important', 'cyber_exploit_signal_medium', 'historical_scanner_uptake', 'historically_linked_to_exploit_kit', 'historically_linked_to_malware', 'historically_linked_to_ransomware', 'historically_linked_to_remote_access_trojan', 'large', 'linked_to_recent_cyber_exploit', 'nist_severity_critical', 'nist_severity_high', 'nist_severity_low', 'nist_severity_medium', 'recent_scanner_uptake', 'recently_linked_to_exploit_kit', 'recently_linked_to_malware', 'recently_linked_to_ransomware', 'recently_linked_to_remote_access_trojan', 'web_reporting_prior_to_nvd_disclosure']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|None|

#### List Hash Risk Rules

This action is used to list available filtration rules for hash risk lists.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|None|

#### Lookup Vulnerability

This action is used to fetch information about a specific vulnerability by CVE or RF ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|CVE or RF ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|vulnerability_search_data|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.5.3 - New spec and help.md format for the Hub
* 1.5.2 - Fix issue where timestamp for evidenceDetails was set to integer, timestamp is now expected as datetime from RecordedFuture
* 1.5.1 - Fix issue where parameter timestamp in evidenceDetails was set as a string in Lookup IP Address action, timestamp is now an integer
* 1.5.0 - Add support for handling IP addresses not found for action Lookup IP Address | Add found parameter to  action Lookup IP Address
* 1.4.1 - Add missing output and remove extra output for actions Lookup Hash, Lookup Domain, Lookup IP Address and Lookup URL
* 1.4.0 - New action Lookup URL | Add input comment to actions Lookup Hash and Lookup Domain
* 1.3.0 - Add additional output for action Lookup IP Address | Add input fields to action Lookup IP Address
* 1.2.0 - Add additional output for action Lookup Domain | Add input fields to action Lookup Domain
* 1.1.0 - Add additional output for action Lookup Hash | Add input fields to action Lookup Hash
* 1.0.2 - Fix typo in plugin spec
* 1.0.1 - Support web server mode | Use new credential types
* 1.0.0 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Recorded Future](https://recordedfuture.com)
* [Recorded Future API](https://api.recordedfuture.com/v2)

