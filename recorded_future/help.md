# Description

[Recorded Future](https://www.recordedfuture.com/) arms threat analysts, security operators, and incident
  responders to rapidly connect the dots and reveal unknown threats. Using the Recorded Future plugin for Rapid7
InsightConnect, users can search domain lists, entity lists, and more.

Use Recorded Future within an automation workflow to quickly assist with threat analysis, incident response, and
vulnerability management.

Note: When a plugin action that causes a file to be downloaded is invoked, the file data is parsed internally and
returned in the [STIX](https://stixproject.github.io/about/) format.

# Key Features

* Search domain and IP lists
* Download risk lists
* Lookup and search hashes

# Requirements

* Recorded Future API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API Key|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions

#### List IP Addresses Risk Rules

This action is used to list available filtration rules for IP address risk lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|Risk Rules|

Example output:

```
{
  "risk_rules": [
    {
      "count": 75508,
      "criticality": 1,
      "criticalityLabel": "Unusual",
      "description": "Historical Threat Researcher",
      "name": "threatResearcher",
      "relatedEntities": []
    },
    {
      "count": 517,
      "criticality": 2,
      "criticalityLabel": "Suspicious",
      "description": "Recently Reported as a Defanged IP",
      "name": "recentDefanged",
      "relatedEntities": []
    },
    {
      "count": 102959,
      "criticality": 1,
      "criticalityLabel": "Unusual",
      "description": "Vulnerable Host",
      "name": "vulnerableHost",
      "relatedEntities": []
    }
  ]
}
```

#### Search Domains

This action is used to search for results related to a specific parent domain.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|from|number|0|True|Number of initial records to skip|None|0|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Firstseen', 'Lastseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Riskscore|
|parent|string|None|True|Parent domain, if any|None|example.com|

Example input:

```
{
  "direction": "asc",
  "from": 0,
  "limit": 10,
  "orderby": "Riskscore",
  "parent": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|Data|

Example output:

```
{
  "counts": {
    "returned": 10,
    "total": 10
  },
  "data": {
    "results": [
      {
        "entity": {
          "id": "idn:blog.recordedfuture.com",
          "name": "blog.recordedfuture.com",
          "type": "InternetDomainName"
        },
        "timestamps": {
          "firstSeen": "2015-09-25T19:27:11.627Z",
          "lastSeen": "2016-11-27T19:53:27.582Z"
        }
      },
      {
        "entity": {
          "id": "idn:api.recordedfuture.com",
          "name": "api.recordedfuture.com",
          "type": "InternetDomainName"
        },
        "timestamps": {
          "firstSeen": "2016-12-19T16:49:10.381Z",
          "lastSeen": "2020-03-25T18:55:20.407Z"
        }
      }
    ]
  }
}
```

#### List Domain Risk Rules

This action is used to list available filtration rules for domain risk lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|Risk Rules|

Example output:

```

{
  "risk_rules": [
    {
      "count": 1473,
      "criticality": 3,
      "criticalityLabel": "Malicious",
      "description": "COVID-19-Related Domain Lure",
      "name": "covidLure",
      "relatedEntities": []
    },
    {
      "count": 21739,
      "criticality": 2,
      "criticalityLabel": "Suspicious",
      "description": "Newly Registered Certificate With Potential for Abuse - DNS Sandwich",
      "name": "certTyposquatSandwich",
      "relatedEntities": []
    },
    {
      "count": 134360,
      "criticality": 2,
      "criticalityLabel": "Suspicious",
      "description": "Newly Registered Certificate With Potential for Abuse - Typo or Homograph",
      "name": "certTyposquatTypo",
      "relatedEntities": []
    }
  ]
}

```

#### Search Malware

This action is used to search for data related to malware.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|freetext|string|None|False|Freetext search|None|example|
|from|number|0|True|Number of initial records to skip|None|0|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Riskscore|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|Data|

Example output:

```
{
  "counts": {
    "returned": 9,
    "total": 9
  },
  "data": {
    "results": [
      {
        "timestamps": {
          "firstSeen": "2017-03-14T09:00:46.277Z",
          "lastSeen": "2020-03-27T14:01:41.045Z"
        },
        "entity": {
          "id": "S0Vzwu",
          "name": "PetrWrap",
          "type": "Malware"
        }
      },
      {
        "entity": {
          "id": "QyiNON",
          "name": "Green Petya",
          "type": "Malware"
        },
        "timestamps": {
          "firstSeen": "2016-05-19T08:04:12.603Z",
          "lastSeen": "2020-03-27T14:01:41.045Z"
        }
      }
    ]
  }
}
```

#### Search Entity Lists

This action is used to perform a freetext search across all Recorded Future entity types (IP address, domain, hash, malware, and vulnerability).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|freetext|string|None|True|Freetext search|None|example|

Example input:

```
{
  "freetext": "example"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|False|Entities|

Example output:

```
{
  "data": {
    "results": [
      {
        "entity": {
          "description": "Honeypot detections for malware IRC network traffi...",
          "id": "report:OjanJ0",
          "name": "Nothink.org: Malware IRC Network Traffic Blacklist",
          "type": "EntityList"
        }
      },
      {
        "entity": {
          "type": "EntityList",
          "description": "All domains on this list should be considered dang...",
          "id": "report:Oe5eg5",
          "name": "MalwareDomainList: Malicious URL Reports"
        }
      }
    ]
  },
  "counts": {
    "returned": 5,
    "total": 5
  }
}
```

#### Download Domain Risk List

This action returns a risk list of domains matching a filtration rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve|['active_phishing_url', 'blacklisted_dns_name', 'cc_dns_name', 'cc_nameserver', 'cc_url', 'compromised_url', 'historical_malware_analysis_dns_name', 'historically_linked_to_cyber_attack', 'large', 'ransomware_distribution_url', 'ransomware_payment_dns_name', 'recent_fast_flux_dns_name', 'recent_malware_analysis_dns_name', 'recently_linked_to_cyber_attack', 'recently_resolved_to_host_of_many_ddns_names', 'recently_resolved_to_malicious_ip', 'recently_resolved_to_suspicious_ip', 'recently_resolved_to_unusual_ip', 'recently_resolved_to_very_malicious_ip', 'sinkhole_dns_name', 'typosquat_similarity__dns_sandwich', 'typosquat_similarity__typo_or_homograph']|active_phishing_url|

Example input:

```
{
  "list": "active_phishing_url"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|Risk List|

#### Search Vulnerabilities

This action is used to search for data related to vulnerabilities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|freetext|string|None|True|Text query|None|example|
|from|number|0|True|Number of initial records to skip|None|0|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Riskscore|

Example input:

```
{
  "direction": "asc",
  "freetext": "example",
  "from": 0,
  "limit": 10,
  "orderby": "Riskscore"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|vulnerability_search_data|False|Data|

Example output:

```
{
  "data": {
    "results": [
      {
        "entity": {
          "description": "Microsoft .NET Framework 2.0, 3.5, 3.5.1, 4.5.2, 4...",
          "id": "UDtzUu",
          "name": "CVE-2017-8759",
          "type": "CyberVulnerability"
        },
        "timestamps": {
          "firstSeen": "2017-09-12T17:04:02.573Z",
          "lastSeen": "2020-04-05T16:49:09.358Z"
        }
      },
      {
        "entity": {
          "id": "JI5lb_",
          "name": "CVE-2012-0158",
          "type": "CyberVulnerability",
          "description": "The (1) ListView, (2) ListView2, (3) TreeView, and..."
        },
        "timestamps": {
          "lastSeen": "2020-04-06T08:25:41.231Z",
          "firstSeen": "2012-04-10T21:55:01.687Z"
        }
      }
    ]
  },
  "counts": {
    "returned": 10,
    "total": 10
  }
}
```

#### Search IP Addresses

This action is used to for data related to a specified IP range.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|from|number|0|True|Number of initial records to skip|None|0|
|ip_range|string|None|True|IP address range to search|None|198.51.100.0/24|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Lastseen|

Example input:

```
{
  "direction": "asc",
  "from": 0,
  "ip_range": "198.51.100.0/24",
  "limit": 10,
  "orderby": "Lastseen"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|Data|

Example output:

```
{
  "data": {
    "results": [
      {
        "entity": {
          "name": "209.0.0.0/15",
          "type": "IpAddress",
          "id": "ip:209.0.0.0/15"
        },
        "timestamps": {
          "firstSeen": "2020-01-29T10:04:41.359Z",
          "lastSeen": "2020-01-29T10:04:41.359Z"
        }
      },
      {
        "entity": {
          "id": "ip:209.0.0.230",
          "name": "209.0.0.230",
          "type": "IpAddress"
        },
        "timestamps": {
          "firstSeen": "2019-04-27T11:24:53.497Z",
          "lastSeen": "2019-09-22T09:23:53.397Z"
        }
      }
    ]
  },
  "counts": {
    "returned": 10,
    "total": 230
  }
}
```

#### List Vulnerability Risk Rules

This action is used to retrieve available filtration rules for vulnerability risk lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|Risk Rules|

Example output:

```
{
  "risk_rules": [
    {
      "count": 4127,
      "criticality": 2,
      "criticalityLabel": "Medium",
      "description": "Historical Verified Proof of Concept Available Usi...",
      "name": "pocVerifiedRemote",
      "relatedEntities": []
    },
    {
      "count": 3,
      "criticality": 3,
      "criticalityLabel": "High",
      "description": "Recent Verified Proof of Concept Available",
      "name": "recentPocVerified",
      "relatedEntities": []
    }
  ]
}
```

#### Download Hash Risk List

This action is used to returns a list of hashes matching a specified risk rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve|['large', 'linked_to_attack_vector', 'linked_to_cyber_attack', 'linked_to_malware', 'linked_to_vulnerability', 'positive_malware_verdict', 'threat_researcher']|positive_malware_verdict|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|Risk List|

#### Search Hashes

This action is used to search for data related to hashes of a specified type.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|algorithm|string|None|True|Hashing algorithm to search by|['MD5', 'SHA-1', 'SHA-256']|SHA-1|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|from|number|0|True|Number of initial records to skip|None|0|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Riskscore|

Example input:

```
{
  "algorithm": "SHA-1",
  "direction": "asc",
  "from": 0,
  "limit": 10,
  "orderby": "Riskscore"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search_data|False|Data|

#### Lookup Entity List

This action is used to fetch a specified entity list by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|entity_list_id|string|None|True|Entity list ID, obtained from the 'Search Entity lists' action|None|report:Oe5eg5|

Example input:

```
{
  "entity_list_id": "report:Oe5eg5"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|False|Entities|

Example output:

```
{
  "counts": {
    "returned": 10,
    "total": 2223
  },
  "data": {
    "results": [
      {
        "entity": {
          "id": "url:http://203.172.131.99/personal/?name=download&...",
          "name": "http://203.172.131.99/personal/?name=download&file...",
          "type": "URL"
        }
      },
      {
        "entity": {
          "id": "url:http://188.95.159.100/phpbb/image2/cp.php?i=15",
          "name": "http://188.95.159.100/phpbb/image2/cp.php?i=15",
          "type": "URL"
        }
      }
    ]
  }
}
```

#### Lookup Malware

This action is used to return information about a specific malware entry by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|malware_ID|string|None|True|Malware ID|None|ShciZX|

Example input:

```
{
  "malware_ID": "ShciZX"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entity|entity|False|Entity|
|timestamps|timestamps|False|Timestamps|

Example output:

```
{
  "data": {
    "entity": {
      "id": "ShciZX",
      "name": "AfterMidnight",
      "type": "Malware"
    },
    "timestamps": {
      "firstSeen": "2013-09-02T21:10:52.988Z",
      "lastSeen": "2020-03-11T12:10:48.788Z"
    }
  }
}
```

#### Lookup Domain

This action is used to return information about a specific domain entry.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Add a comment to a domain|None|Domain look up performed by InsightConnect|
|domain|string|None|True|Domain|None|example.com|
|fields|[]string|None|False|List of fields to include with results e.g ["sightings", "threatLists", "analystNotes", "counts", "entity", "intelCard", "metrics", "relatedEntities" , "risk" , "timestamps"]|None|["sightings", "threatLists", "intelCard"]|

Example input:

```
{
  "comment": "Domain look up performed by InsightConnect",
  "domain": "example.com",
  "fields": [
    "sightings",
    "threatLists",
    "intelCard"
  ]
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Add a comment to a hash|None|Hash look up performed by InsightConnect|
|fields|[]string|None|False|List of fields to include with results e.g ["timestamps", "sightings", "threatLists", "analystNotes", "counts", "entity", "hashAlgorithm", "intelCard", "metrics", "relatedEntities", "risk", "timestamps"]|None|["risk", "timestamps", "sightings"]|
|hash|string|None|True|Hash|None|44d88612fea8a8f36de82e1278abb02f|

Example input:

```
{
  "comment": "Hash look up performed by InsightConnect",
  "fields": [
    "risk",
    "timestamps",
    "sightings"
  ],
  "hash": "44d88612fea8a8f36de82e1278abb02f"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Add a comment to an IP address lookup for Recorded Future|None|URL look up performed by InsightConnect|
|fields|[]string|None|False|List of fields to include with results e.g ["sightings", "analystNotes", "counts", "entity", "metrics", "relatedEntities", "risk", "timestamps"]|None|["relatedEntities", "risk", "sightings"]|
|url|string|None|True|URL|None|https://example.com|

Example input:

```
{
  "comment": "URL look up performed by InsightConnect",
  "fields": [
    "relatedEntities",
    "risk",
    "sightings"
  ],
  "url": "https://example.com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve|['current_cc_server', 'cyber_exploit_signal_medium', 'historical_bad_ssl_association', 'historical_botnet_traffic', 'historical_cc_server', 'historical_honeypot_sighting', 'historical_multicategory_blacklist', 'historical_open_proxies', 'historical_positive_malware_verdict', 'historical_spam_source', 'historical_sshdictionary_attacker', 'historical_threat_researcher', 'historically_linked_to_apt', 'historically_linked_to_cyber_attack', 'historically_linked_to_intrusion_method', 'honeypot_host', 'inside_possible_bogus_bgp_route', 'large', 'malicious_packet_source', 'malware_delivery', 'nameserver_for_cc_server', 'phishing_host', 'recent_botnet_traffic', 'recent_cc_server', 'recent_honeypot_sighting', 'recent_host_of_many_ddns_names', 'recent_multicategory_blacklist', 'recent_open_proxies', 'recent_positive_malware_verdict', 'recent_spam_source', 'recent_sshdictionary_attacker', 'recent_threat_researcher', 'recently_linked_to_apt', 'recently_linked_to_cyber_attack', 'recently_linked_to_intrusion_method', 'resolution_of_fast_flux_dns_name', 'tor_node', 'unusual_ip', 'vulnerable_host']|malware_delivery|

Example input:

```
{
  "list": "malware_delivery"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|Risk List|

Example output:

```
{
  "stix:STIX_Package": {
    "@xmlns": "http://xml/metadataSharing.xsd",
    "@xmlns:indicator": "http://stix.mitre.org/Indicator-2",
    "@xmlns:stix": "http://stix.mitre.org/stix-1",
    "@xmlns:ttp": "http://stix.mitre.org/TTP-1",
    "stix:STIX_Header": {
      "stix:Description": "Recorded Future STIX"
    },
    "@id": "RF:Package-9144eafb-a082-49d1-97a1-e7ceb4d8e955",
    "@timestamp": "2020-04-01T12:10:12.058Z",
    "@xmlns:FileObj": "http://cybox.mitre.org/objects#FileObject-2",
    "@xmlns:stixCommon": "http://stix.mitre.org/common-1",
    "stix:Indicators": {
      "stix:Indicator": [
        {
          "@timestamp": "2020-04-06T16:10:17.739Z",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "@xsi:type": "indicator:IndicatorType",
          "indicator:Description": "Current risk: Suspicious.Triggers 1 of 51 rules",
          "indicator:Indicated_TTP": {
            "stixCommon:Confidence": {
              "stixCommon:Value": {
                "#text": "Medium",
                "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
              }
            },
            "stixCommon:TTP": {
              "ttp:Title": "Risk Rule: Current C&C Server",
              "@id": "RF:TTP-42014977-2178-3d3e-b3d1-a3d39961ebca",
              "@timestamp": "2020-04-04T17:31:26.032Z",
              "@xsi:type": "ttp:TTPType",
              "ttp:Description": "1 sighting on 1 source: Cobalt Strike Default Cert..."
            }
          },
          "indicator:Observable": {
            "@id": "RF:Observable-19894357-b884-3cd8-bd49-54540862a4a0",
            "cybox:Object": {
              "@id": "RF:Address-81ec9700-57ba-3f8d-aeb9-f00418d5f31c",
              "cybox:Properties": {
                "@category": "ipv4-addr",
                "@xsi:type": "AddressObj:AddressObjectType",
                "AddressObj:Address_Value": {
                  "#text": "3.10.20.157",
                  "@condition": "Equals"
                }
              }
            }
          },
          "indicator:Producer": {
            "stixCommon:References": {
              "stixCommon:Reference": "https://app.recordedfuture.com/live/sc/entity/ip%!..."
            },
            "stixCommon:Description": "Recorded Future"
          },
          "indicator:Type": {
            "#text": "IP Watchlist",
            "@xsi:type": "stixVocabs:IndicatorTypeVocab-1.1"
          },
          "@id": "RF:Indicator-02ff9864-3b18-332c-be33-35449baed75a",
          "indicator:Confidence": {
            "stixCommon:Description": "Recorded Future Risk Score",
            "stixCommon:Value": "25"
          },
          "indicator:Title": "IP Address 3.10.20.157",
          "indicator:Valid_Time_Position": {
            "indicator:Start_Time": {
              "#text": "2020-04-04T00:00:00.000Z",
              "@precision": "second"
            },
            "indicator:End_Time": {
              "#text": "2020-04-04T23:59:59.000Z",
              "@precision": "second"
            }
          }
        },
        {
          "@timestamp": "2020-04-06T16:10:17.739Z",
          "@xsi:type": "indicator:IndicatorType",
          "indicator:Observable": {
            "@id": "RF:Observable-72d63012-ab31-3324-b994-1dc391fe9299",
            "cybox:Object": {
              "@id": "RF:Address-7aa0590a-8d24-36cc-aee3-a93d4200b564",
              "cybox:Properties": {
                "@category": "ipv4-addr",
                "@xsi:type": "AddressObj:AddressObjectType",
                "AddressObj:Address_Value": {
                  "#text": "5.34.180.206",
                  "@condition": "Equals"
                }
              }
            }
          },
          "indicator:Producer": {
            "stixCommon:Description": "Recorded Future",
            "stixCommon:References": {
              "stixCommon:Reference": "https://app.recordedfuture.com/live/sc/entity/ip%!..."
            }
          },
          "@id": "RF:Indicator-eafa3166-7abc-33af-8789-ede692bf230a",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "indicator:Confidence": {
            "stixCommon:Value": "96",
            "stixCommon:Description": "Recorded Future Risk Score"
          },
          "indicator:Description": "Current risk: Very Malicious.Triggers 3 of 51 rule...",
          "indicator:Indicated_TTP": [
            {
              "stixCommon:Confidence": {
                "stixCommon:Value": {
                  "#text": "Low",
                  "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                }
              },
              "stixCommon:TTP": {
                "@xsi:type": "ttp:TTPType",
                "ttp:Description": "Previous sightings on 1 source: Cobalt Strike Defa...",
                "ttp:Title": "Risk Rule: Historically Reported in Threat List",
                "@id": "RF:TTP-538a4df0-0f1f-3a66-82c1-2bb9f030d044",
                "@timestamp": "2020-04-04T18:49:02.868Z"
              }
            },
            {
              "stixCommon:Confidence": {
                "stixCommon:Value": {
                  "#text": "High",
                  "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                }
              },
              "stixCommon:TTP": {
                "@id": "RF:TTP-373ddb7d-61ac-36a4-8f30-31e2650ea421",
                "@timestamp": "2020-01-11T08:02:27.884Z",
                "@xsi:type": "ttp:TTPType",
                "ttp:Description": "1 sighting on 1 source: Recorded Future Command & ...",
                "ttp:Title": "Risk Rule: Current C&C Server"
              }
            }
          ],
          "indicator:Title": "IP Address 5.34.180.206",
          "indicator:Type": {
            "#text": "IP Watchlist",
            "@xsi:type": "stixVocabs:IndicatorTypeVocab-1.1"
          },
          "indicator:Valid_Time_Position": {
            "indicator:End_Time": {
              "#text": "2020-01-11T08:02:27.884Z",
              "@precision": "second"
            },
            "indicator:Start_Time": {
              "#text": "2020-01-11T08:02:27.884Z",
              "@precision": "second"
            }
          }
        }
      ]
    },
    "@xmlns:RF": "http://stix.recordedfuture.com/",
    "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
    "@xmlns:cyboxCommon": "http://cybox.mitre.org/common-2",
    "@xmlns:stixVocabs": "http://stix.mitre.org/default_vocabularies-1",
    "@version": "1.2",
    "@xmlns:AddressObj": "http://cybox.mitre.org/objects#AddressObject-2",
    "@xmlns:cyboxVocabs": "http://cybox.mitre.org/default_vocabularies-2"
  }
}
```

#### Lookup IP Address

This action is used to query for data related to a specific IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|IP_address|string|None|True|IP address|None|198.51.100.100|
|comment|string|None|False|Add comment to IP address lookup for Recorded Future|None|IP look up performed by InsightConnect|
|fields|[]string|None|False|List of fields to include with results e.g ["sightings", "threatLists", "analystNotes", "counts", "entity", "intelCard", "metrics", "relatedEntities", "riskyCIDRIPs","risk", "location", "timestamps"]|None|["riskyCIDRIPs", "risk", "sightings"]|

Example input:

```
{
  "IP_address": "198.51.100.100",
  "comment": "IP look up performed by InsightConnect",
  "fields": [
    "riskyCIDRIPs",
    "risk",
    "sightings"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analystNotes|[]string|False|Notes from an analyst|
|counts|[]counts|False|Counts|
|entity|entity|False|Entity|
|found|boolean|False|Has the IP been found in Recorded Future|
|intelCard|string|False|Intel card|
|location|location|False|Location|
|metrics|[]metrics|False|Metrics|
|relatedEntities|[]relatedEntities|False|Related entities|
|risk|risk|False|Risk|
|riskyCIDRIPs|[]riskyCIDRIP|False|Risky CIDR IPs|
|sightings|[]sightings|False|Sightings|
|threatLists|[]string|False|Threat lists|
|timestamps|timestamps|False|Timestamps|

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve|['cyber_exploit_signal_critical', 'cyber_exploit_signal_important', 'cyber_exploit_signal_medium', 'historical_scanner_uptake', 'historically_linked_to_exploit_kit', 'historically_linked_to_malware', 'historically_linked_to_ransomware', 'historically_linked_to_remote_access_trojan', 'large', 'linked_to_recent_cyber_exploit', 'nist_severity_critical', 'nist_severity_high', 'nist_severity_low', 'nist_severity_medium', 'recent_scanner_uptake', 'recently_linked_to_exploit_kit', 'recently_linked_to_malware', 'recently_linked_to_ransomware', 'recently_linked_to_remote_access_trojan', 'web_reporting_prior_to_nvd_disclosure']|nist_severity_critical|

Example input:

```
{
  "list": "nist_severity_critical"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|Risk List|

Example output:

```
{
  "stix:STIX_Package": {
    "@xmlns": "http://xml/metadataSharing.xsd",
    "@xmlns:RF": "http://stix.recordedfuture.com/",
    "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
    "@xmlns:et": "http://stix.mitre.org/ExploitTarget-1",
    "@xmlns:stix": "http://stix.mitre.org/stix-1",
    "@xmlns:stixCommon": "http://stix.mitre.org/common-1",
    "stix:Exploit_Targets": {
      "stixCommon:Exploit_Target": [
        {
          "@id": "RF:et-f786d327-c403-3a5a-92c9-cc4678f6289a",
          "@timestamp": "2020-04-06T16:04:47.047Z",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "@xsi:type": "et:ExploitTargetType",
          "et:Description": "(Risk Score: 89. Risk Rules: Linked to Historical ...",
          "et:Title": "Vulnerability CVE-2020-6819",
          "et:Vulnerability": {
            "et:CVE_ID": "CVE-2020-6819",
            "et:References": {
              "stixCommon:Reference": "https://app.recordedfuture.com/live/sc/entity/dXhB..."
            }
          }
        },
        {
          "et:Vulnerability": {
            "et:CVE_ID": "CVE-2020-6820",
            "et:References": {
              "stixCommon:Reference": "https://app.recordedfuture.com/live/sc/entity/dXhB..."
            }
          },
          "@id": "RF:et-159738b9-a6c0-3ff8-bef1-fdc9b8a66491",
          "@timestamp": "2020-04-06T16:06:54.652Z",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "@xsi:type": "et:ExploitTargetType",
          "et:Description": "(Risk Score: 89. Risk Rules: Linked to Historical ...",
          "et:Title": "Vulnerability CVE-2020-6820"
        }
      ]
    },
    "@id": "RF:Package-0db848e9-1de9-4605-b3b3-1bfe6dfc8721",
    "stix:STIX_Header": {
      "stix:Description": "Recorded Future STIX"
    },
    "@version": "1.2",
    "@timestamp": "2020-04-01T12:45:02.780Z"
  }
}
```

#### List Hash Risk Rules

This action is used to list available filtration rules for hash risk lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|False|Risk Rules|

Example output:

```
{
  "risk_rules": [
    {
      "name": "recentActiveMalware",
      "relatedEntities": [
        "aHTyRv"
      ],
      "count": 16164,
      "criticality": 3,
      "criticalityLabel": "Malicious",
      "description": "Recently Active Targeting Vulnerabilities in the W..."
    },
    {
      "criticality": 3,
      "criticalityLabel": "Malicious",
      "description": "Observed in Underground Virus Testing Sites",
      "name": "observedMalwareTesting",
      "relatedEntities": [],
      "count": 1158
    }
  ]
}
```

#### Lookup Vulnerability

This action is used to fetch information about a specific vulnerability by CVE or RF ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|CVE or RF ID|None|CVE-2014-0160|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|vulnerability_search_data|False|Data|

Example output:

```
{
  "data": {
    "timestamps": {
      "firstSeen": "2017-03-14T16:59:26.413Z",
      "lastSeen": "2020-04-06T10:05:19.883Z"
    },
    "entity": {
      "description": "The SMBv1 server in Microsoft Windows Vista SP2; W...",
      "id": "S0eb_5",
      "name": "CVE-2017-0147",
      "type": "CyberVulnerability"
    }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Add risk output to Lookup Vulnerability
* 1.5.5 - Fix NoneType has no len() | Fix enums in search hashes
* 1.5.4 - Add example inputs | Fix schema bug where `criticality` output was improperly defined as an integer in List Domain Risk Rules, List Hash Risk Rules, List IP Addresses Risk Rules and List Vulnerability Risk Rules actions
* 1.5.3 - New spec and help.md format for the Extension Library
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
