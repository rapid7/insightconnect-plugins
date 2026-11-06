# Description

GreyNoise helps analysts recognize events not worth their attention. Indicators in GreyNoise are likely associated with opportunistic internet scanning or common business services, not targeted threats. This context helps analysts focus on what matters most

# Key Features

* Perform a GreyNoise IP Lookup
* Perform a GreyNoise IP Quick Lookup
* Query for additional Tag details
* Perform a GreyNoise Community IP Lookup
* Perform a GreyNoise Vulnerability Lookup
* Perform a GreyNoise IP Timeline Lookup
* Look up a GreyNoise Callback IP
* Query a list of IPs on a Trigger

# Requirements

* A GreyNoise API key

# Supported Product Versions

* GreyNoise API v3

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_secret_key|None|True|API key from GreyNoise Account|None|abcdefghijklmnopqrstuvwxyz0123456789|None|None|

Example input:

```
{
  "credentials": "abcdefghijklmnopqrstuvwxyz0123456789"
}
```

## Technical Details

### Actions


#### Callback IP Lookup

This action is used to look up a callback IP in the GreyNoise C2 detection dataset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|Callback IPv4 address to query|None|198.51.100.42|None|None|
|source_workspace|string|all|False|Workspace filter. Use all, or a workspace name such as GreyNoise, UserWorkspace, or Community|None|all|None|None|
  
Example input:

```
{
  "ip_address": "198.51.100.42",
  "source_workspace": "all"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|active_files|[]callback_file|False|Malware files associated with this callback IP|[{"sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "file_name": "payload.bin", "type": "application/x-executable"}]|
|file_count|integer|False|Number of malware files associated with this IP|3|
|first_seen|string|False|When this IP was first observed|2025-03-01T00:00:00Z|
|ip|string|False|Callback IP address|198.51.100.42|
|is_stage_1|boolean|False|Whether a file was successfully downloaded from this IP|False|
|is_stage_2|boolean|False|Whether this IP is suspected command and control|False|
|last_seen|string|False|When this IP was most recently observed|2025-03-15T12:30:00Z|
|message|string|False|Status message when the IP is not found in the requested workspace||
|scanner_count|integer|False|Number of distinct scanners associated with this IP|5|
|scanner_ips|[]string|False|Scanner IPs that delivered payloads referencing this callback IP|["203.0.113.7", "192.0.2.99"]|
|source_workspaces|[]string|False|Workspace sources where this IP was observed|["GreyNoise", "UserWorkspace"]|
  
Example output:

```
{
  "active_files": [
    {
      "file_name": "payload.bin",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "type": "application/x-executable"
    }
  ],
  "file_count": 3,
  "first_seen": "2025-03-01T00:00:00Z",
  "ip": "198.51.100.42",
  "is_stage_1": false,
  "is_stage_2": false,
  "last_seen": "2025-03-15T12:30:00Z",
  "message": "",
  "scanner_count": 5,
  "scanner_ips": [
    "203.0.113.7",
    "192.0.2.99"
  ],
  "source_workspaces": [
    "GreyNoise",
    "UserWorkspace"
  ]
}
```

#### Community IP Lookup

This action is used to query a routable IPv4 address in the GreyNoise Community API

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|None|None|
  
Example input:

```
{
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|classification|string|False|GreyNoise Classification|benign|
|ip|string|False|Value that was Queried|1.2.3.4|
|last_seen|string|False|Last Seen By GreyNoise|2024-01-01|
|link|string|False|Link to GreyNoise Visualizer for IP Details|https://viz.greynoise.io/ip/1.1.1.1|
|message|string|False|GreyNoise Community API Status Message|IP found|
|name|string|False|GreyNoise Actor or Service Name Associated with IP|Acme Inc.|
|noise|boolean|False|Defines if IP is Internet Noise|True|
|riot|boolean|False|Defines if IP is part of GreyNoise RIOT dataset|True|
  
Example output:

```
{
  "classification": "benign",
  "ip": "1.2.3.4",
  "last_seen": "2024-01-01",
  "link": "https://viz.greynoise.io/ip/1.1.1.1",
  "message": "IP found",
  "name": "Acme Inc.",
  "noise": true,
  "riot": true
}
```

#### Context IP Lookup

This action is used to look up a routable IPv4 address with the GreyNoise IP Lookup API. Kept for existing workflows 
that call Context IP Lookup

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|None|None|
  
Example input:

```
{
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|business_service_intelligence|business_service_intelligence|False|Business Service Intelligence for the IP|{'found': True, 'category': 'public_dns', 'trust_level': '1', 'name': 'Acme Inc', 'description': 'Acme Inc is an example service.', 'explanation': 'This IP provides a common business service.', 'last_updated': '2024-01-01', 'reference': 'https://example.com'}|
|internet_scanner_intelligence|internet_scanner_intelligence|False|Internet Scanner Intelligence for the IP|{'found': True, 'actor': 'unknown', 'classification': 'suspicious', 'first_seen': '2025-10-14', 'last_seen': '2026-10-30', 'last_seen_timestamp': '2026-10-30 19:31:39', 'spoofable': True, 'vpn': False, 'vpn_service': '', 'tor': False, 'cves': [], 'callback_ips': [], 'tags': [{'id': '13503954-9a41-447f-b7a1-8f82fe2258bd', 'slug': 'snmp-protocol', 'name': 'SNMP Protocol', 'category': 'protocol', 'intention': 'unknown', 'recommend_block': False}], 'tag_volumes': [{'tag_id': '13503954-9a41-447f-b7a1-8f82fe2258bd', 'session_count': 200}], 'metadata': {'asn': 'AS14618', 'source_country': 'United States', 'organization': 'Amazon.com, Inc.', 'longitude': -77.4875, 'latitude': 39.0437}}|
|ip|string|False|Value that was Queried|1.2.3.4|
|viz_url|string|False|Link to GreyNoise Visualizer for IP Details|https://viz.greynoise.io/ip/1.2.3.4|
  
Example output:

```
{
  "business_service_intelligence": {
    "category": "public_dns",
    "description": "Acme Inc is an example service.",
    "explanation": "This IP provides a common business service.",
    "found": true,
    "last_updated": "2024-01-01",
    "name": "Acme Inc",
    "reference": "https://example.com",
    "trust_level": "1"
  },
  "internet_scanner_intelligence": {
    "actor": "unknown",
    "callback_ips": [],
    "classification": "suspicious",
    "cves": [],
    "first_seen": "2025-10-14",
    "found": true,
    "last_seen": "2026-10-30",
    "last_seen_timestamp": "2026-10-30 19:31:39",
    "metadata": {
      "asn": "AS14618",
      "latitude": 39.0437,
      "longitude": -77.4875,
      "organization": "Amazon.com, Inc.",
      "source_country": "United States"
    },
    "spoofable": true,
    "tag_volumes": [
      {
        "session_count": 200,
        "tag_id": "13503954-9a41-447f-b7a1-8f82fe2258bd"
      }
    ],
    "tags": [
      {
        "category": "protocol",
        "id": "13503954-9a41-447f-b7a1-8f82fe2258bd",
        "intention": "unknown",
        "name": "SNMP Protocol",
        "recommend_block": false,
        "slug": "snmp-protocol"
      }
    ],
    "tor": false,
    "vpn": false,
    "vpn_service": ""
  },
  "ip": "1.2.3.4",
  "viz_url": "https://viz.greynoise.io/ip/1.2.3.4"
}
```

#### Get Tag Details

This action is used to get details of a GreyNoise tag from the Tags API

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|tag_name|string|None|True|Tag Name to get additional Details From|None|BingBot|None|None|
  
Example input:

```
{
  "tag_name": "BingBot"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|category|string|False|Tag Category|activity|
|created_at|string|False|The date the tag was added to GreyNoise tag library|2024-01-01|
|cves|[]string|False|CVEs associate with Tag|CVE-2020-1234,CVE-1241-23521|
|description|string|False|Description of the Tag|This is a tag description|
|id|string|False|The unique ID for the tag|aa-bb-cc-dd|
|intention|string|False|Tag Intention|malicious|
|label|string|False|The unique label for the tag|BINGBOT_SCANNER|
|name|string|False|Name of GreyNoise Tag|BingBot|
|recommend_block|boolean|False|GreyNoise Recommends Blocking IPs associated with this Tag|False|
|references|[]string|False|References|https://thisisareference.url|
|related_tags|[]related_tag|False|Tags that are related to this tag|[{"id": "da78f2eb-fe6b-4e84-913c-cdab4ff067c2", "name": "Oracle WebLogic RCE CVE-2020-14882", "intention": "malicious", "category": "activity", "slug": "oracle-weblogic-rce-cve-2020-14882"}]|
|slug|string|False|The unique slug for the tag|bingbot-scanner|
  
Example output:

```
{
  "category": "activity",
  "created_at": "2024-01-01",
  "cves": "CVE-2020-1234,CVE-1241-23521",
  "description": "This is a tag description",
  "id": "aa-bb-cc-dd",
  "intention": "malicious",
  "label": "BINGBOT_SCANNER",
  "name": "BingBot",
  "recommend_block": false,
  "references": "https://thisisareference.url",
  "related_tags": [
    {
      "category": "activity",
      "id": "da78f2eb-fe6b-4e84-913c-cdab4ff067c2",
      "intention": "malicious",
      "name": "Oracle WebLogic RCE CVE-2020-14882",
      "slug": "oracle-weblogic-rce-cve-2020-14882"
    }
  ],
  "slug": "bingbot-scanner"
}
```

#### GreyNoise Query

This action is used to perform a GreyNoise GNQL Query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Query in GreyNoise Query Language (GNQL) Syntax|None|last_seen:1d classification:'malicious' metadata.asn:'AS8452'|None|None|
|scroll|string|None|False|Token from a previous query response used to fetch the next page|None||None|None|
|size|string|10|False|Max Number of IPs to Return Data For|None|10|None|None|
  
Example input:

```
{
  "query": "last_seen:1d classification:'malicious' metadata.asn:'AS8452'",
  "scroll": "",
  "size": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]gnql_ip|False|IP results matching the GNQL query|[{"ip": "1.2.3.4", "internet_scanner_intelligence": {"found": True, "classification": "malicious"}, "business_service_intelligence": {"found": False, "trust_level": ""}}]|
|request_metadata|gnql_request_metadata|False|Pagination and status details for the GNQL query|{'complete': False, 'count': 147, 'message': 'ok', 'query': 'classification:malicious', 'adjusted_query': '(classification:malicious) last_seen:90d', 'scroll': '', 'restricted_fields': []}|
  
Example output:

```
{
  "data": [
    {
      "business_service_intelligence": {
        "found": false,
        "trust_level": ""
      },
      "internet_scanner_intelligence": {
        "classification": "malicious",
        "found": true
      },
      "ip": "1.2.3.4"
    }
  ],
  "request_metadata": {
    "adjusted_query": "(classification:malicious) last_seen:90d",
    "complete": false,
    "count": 147,
    "message": "ok",
    "query": "classification:malicious",
    "restricted_fields": [],
    "scroll": ""
  }
}
```

#### IP Lookup

This action is used to query a routable IPv4 address in the GreyNoise IP Lookup API

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|None|None|
  
Example input:

```
{
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|business_service_intelligence|business_service_intelligence|False|Business Service Intelligence for the IP|{'found': True, 'category': 'public_dns', 'trust_level': '1', 'name': 'Acme Inc', 'description': 'Acme Inc is an example service.', 'explanation': 'This IP provides a common business service.', 'last_updated': '2024-01-01', 'reference': 'https://example.com'}|
|internet_scanner_intelligence|internet_scanner_intelligence|False|Internet Scanner Intelligence for the IP|{'found': True, 'actor': 'unknown', 'classification': 'suspicious', 'first_seen': '2025-10-14', 'last_seen': '2026-10-30', 'last_seen_timestamp': '2026-10-30 19:31:39', 'spoofable': True, 'vpn': False, 'vpn_service': '', 'tor': False, 'cves': [], 'callback_ips': [], 'tags': [{'id': '13503954-9a41-447f-b7a1-8f82fe2258bd', 'slug': 'snmp-protocol', 'name': 'SNMP Protocol', 'category': 'protocol', 'intention': 'unknown', 'recommend_block': False}], 'tag_volumes': [{'tag_id': '13503954-9a41-447f-b7a1-8f82fe2258bd', 'session_count': 200}], 'metadata': {'asn': 'AS14618', 'source_country': 'United States', 'organization': 'Amazon.com, Inc.', 'longitude': -77.4875, 'latitude': 39.0437}}|
|ip|string|False|Value that was Queried|1.2.3.4|
|viz_url|string|False|Link to GreyNoise Visualizer for IP Details|https://viz.greynoise.io/ip/1.2.3.4|
  
Example output:

```
{
  "business_service_intelligence": {
    "category": "public_dns",
    "description": "Acme Inc is an example service.",
    "explanation": "This IP provides a common business service.",
    "found": true,
    "last_updated": "2024-01-01",
    "name": "Acme Inc",
    "reference": "https://example.com",
    "trust_level": "1"
  },
  "internet_scanner_intelligence": {
    "actor": "unknown",
    "callback_ips": [],
    "classification": "suspicious",
    "cves": [],
    "first_seen": "2025-10-14",
    "found": true,
    "last_seen": "2026-10-30",
    "last_seen_timestamp": "2026-10-30 19:31:39",
    "metadata": {
      "asn": "AS14618",
      "latitude": 39.0437,
      "longitude": -77.4875,
      "organization": "Amazon.com, Inc.",
      "source_country": "United States"
    },
    "spoofable": true,
    "tag_volumes": [
      {
        "session_count": 200,
        "tag_id": "13503954-9a41-447f-b7a1-8f82fe2258bd"
      }
    ],
    "tags": [
      {
        "category": "protocol",
        "id": "13503954-9a41-447f-b7a1-8f82fe2258bd",
        "intention": "unknown",
        "name": "SNMP Protocol",
        "recommend_block": false,
        "slug": "snmp-protocol"
      }
    ],
    "tor": false,
    "vpn": false,
    "vpn_service": ""
  },
  "ip": "1.2.3.4",
  "viz_url": "https://viz.greynoise.io/ip/1.2.3.4"
}
```

#### Quick IP Lookup

This action is used to query a routable IPv4 address in the GreyNoise Quick IP Lookup API

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|None|None|
  
Example input:

```
{
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|business_service_intelligence|business_service_intelligence|False|Whether the IP is a known business service, and its trust level|{'found': False, 'trust_level': '1'}|
|internet_scanner_intelligence|internet_scanner_intelligence|False|Whether the IP was found scanning the internet, and its classification|{'found': True, 'classification': 'malicious'}|
|ip|string|False|Value that was Queried|1.2.3.4|
  
Example output:

```
{
  "business_service_intelligence": {
    "found": false,
    "trust_level": "1"
  },
  "internet_scanner_intelligence": {
    "classification": "malicious",
    "found": true
  },
  "ip": "1.2.3.4"
}
```

#### RIOT IP Lookup

This action is used to look up a routable IPv4 address and return Internet Scanner Intelligence and Business Service 
Intelligence. Kept for existing workflows that call RIOT IP Lookup

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|None|None|
  
Example input:

```
{
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|business_service_intelligence|business_service_intelligence|False|Business Service Intelligence for the IP|{'found': True, 'category': 'public_dns', 'trust_level': '1', 'name': 'Acme Inc', 'description': 'Acme Inc is an example service.', 'explanation': 'This IP provides a common business service.', 'last_updated': '2024-01-01', 'reference': 'https://example.com'}|
|internet_scanner_intelligence|internet_scanner_intelligence|False|Internet Scanner Intelligence for the IP|{'found': True, 'actor': 'unknown', 'classification': 'suspicious', 'first_seen': '2025-10-14', 'last_seen': '2026-10-30', 'last_seen_timestamp': '2026-10-30 19:31:39', 'spoofable': True, 'vpn': False, 'vpn_service': '', 'tor': False, 'cves': [], 'callback_ips': [], 'tags': [{'id': '13503954-9a41-447f-b7a1-8f82fe2258bd', 'slug': 'snmp-protocol', 'name': 'SNMP Protocol', 'category': 'protocol', 'intention': 'unknown', 'recommend_block': False}], 'tag_volumes': [{'tag_id': '13503954-9a41-447f-b7a1-8f82fe2258bd', 'session_count': 200}], 'metadata': {'asn': 'AS14618', 'source_country': 'United States', 'organization': 'Amazon.com, Inc.', 'longitude': -77.4875, 'latitude': 39.0437}}|
|ip|string|False|Value that was Queried|1.2.3.4|
|viz_url|string|False|Link to GreyNoise Visualizer for IP Details|https://viz.greynoise.io/ip/1.2.3.4|
  
Example output:

```
{
  "business_service_intelligence": {
    "category": "public_dns",
    "description": "Acme Inc is an example service.",
    "explanation": "This IP provides a common business service.",
    "found": true,
    "last_updated": "2024-01-01",
    "name": "Acme Inc",
    "reference": "https://example.com",
    "trust_level": "1"
  },
  "internet_scanner_intelligence": {
    "actor": "unknown",
    "callback_ips": [],
    "classification": "suspicious",
    "cves": [],
    "first_seen": "2025-10-14",
    "found": true,
    "last_seen": "2026-10-30",
    "last_seen_timestamp": "2026-10-30 19:31:39",
    "metadata": {
      "asn": "AS14618",
      "latitude": 39.0437,
      "longitude": -77.4875,
      "organization": "Amazon.com, Inc.",
      "source_country": "United States"
    },
    "spoofable": true,
    "tag_volumes": [
      {
        "session_count": 200,
        "tag_id": "13503954-9a41-447f-b7a1-8f82fe2258bd"
      }
    ],
    "tags": [
      {
        "category": "protocol",
        "id": "13503954-9a41-447f-b7a1-8f82fe2258bd",
        "intention": "unknown",
        "name": "SNMP Protocol",
        "recommend_block": false,
        "slug": "snmp-protocol"
      }
    ],
    "tor": false,
    "vpn": false,
    "vpn_service": ""
  },
  "ip": "1.2.3.4",
  "viz_url": "https://viz.greynoise.io/ip/1.2.3.4"
}
```

#### IP Timeline Lookup

This action is used to query a routable IPv4 address for GreyNoise daily timeline details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days|integer|7|False|Number of days of daily timeline data to return|None|1|None|None|
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|None|None|
  
Example input:

```
{
  "days": 7,
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]timeline_day|False|Daily timeline records consolidated by the GreyNoise SDK|[{"date": "2026-10-30T00:00:00Z", "asns": ["AS14618"], "organizations": ["Amazon.com, Inc."], "tags": ["DNS Protocol"], "classification": ["unknown"], "rdns": ["ec2-100-29-192-92.compute-1.amazonaws.com"], "ports": ["80", "443"]}]|
|ip|string|False|Value that was Queried|100.29.192.92|
|metadata|timeline_metadata|False|Metadata returned by the GreyNoise daily timeline|{'ip': '100.29.192.92', 'days': 1, 'granularity': '1d', 'field': 'classification'}|
  
Example output:

```
{
  "data": [
    {
      "asns": [
        "AS14618"
      ],
      "classification": [
        "unknown"
      ],
      "date": "2026-10-30T00:00:00Z",
      "organizations": [
        "Amazon.com, Inc."
      ],
      "ports": [
        "80",
        "443"
      ],
      "rdns": [
        "ec2-100-29-192-92.compute-1.amazonaws.com"
      ],
      "tags": [
        "DNS Protocol"
      ]
    }
  ],
  "ip": "100.29.192.92",
  "metadata": {
    "days": 1,
    "field": "classification",
    "granularity": "1d",
    "ip": "100.29.192.92"
  }
}
```

#### Vulnerability Lookup

This action is used to look up a CVE in the GreyNoise v3 CVE API

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cve_id|string|None|True|A CVE ID to look up in GreyNoise|None|CVE-2020-12345|None|None|
  
Example input:

```
{
  "cve_id": "CVE-2020-12345"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|details|vuln_details|False|GreyNoise Vulnerability Details|{'cve_cvss_score': 9.8, 'product': 'Product Name', 'published_to_nist_nvd': False, 'vendor': 'Acme Inc', 'vulnerability_description': 'This is a product description.', 'vulnerability_name': 'This is a vuln name.'}|
|exploitation_activity|vuln_exploitation_activity|False|GreyNoise Vulnerability Exploitation Activity|{'activity_seen': True, 'benign_ip_count_10d': 5, 'benign_ip_count_1d': 5, 'benign_ip_count_30d': 5, 'threat_ip_count_10d': 5, 'threat_ip_count_1d': 5, 'threat_ip_count_30d': 5}|
|exploitation_details|vuln_exploitation_details|False|GreyNoise Vulnerability Exploitation Details|{'attack_vector': 'NETWORK', 'epss_score': 0.0, 'exploit_found': True, 'exploitation_registered_in_kev': False}|
|exploitation_stats|vuln_exploitation_stats|False|GreyNoise Vulnerability Exploitation Stats|{'number_of_available_exploits': 1, 'number_of_botnets_exploiting_vulnerability': 1, 'number_of_threat_actors_exploiting_vulnerability': 1}|
|id|string|False|Value that was searched|CVE-2020-12345|
|timeline|vuln_timeline|False|GreyNoise Vulnerability Timeline|{'cisa_kev_date_added': '2020-07-08T17:15:10Z', 'cve_last_updated_date': '2020-07-08T17:15:10Z', 'cve_published_date': '2020-07-08T17:15:10Z', 'first_known_published_date': '2020-07-08T17:15:10Z'}|
  
Example output:

```
{
  "details": {
    "cve_cvss_score": 9.8,
    "product": "Product Name",
    "published_to_nist_nvd": false,
    "vendor": "Acme Inc",
    "vulnerability_description": "This is a product description.",
    "vulnerability_name": "This is a vuln name."
  },
  "exploitation_activity": {
    "activity_seen": true,
    "benign_ip_count_10d": 5,
    "benign_ip_count_1d": 5,
    "benign_ip_count_30d": 5,
    "threat_ip_count_10d": 5,
    "threat_ip_count_1d": 5,
    "threat_ip_count_30d": 5
  },
  "exploitation_details": {
    "attack_vector": "NETWORK",
    "epss_score": 0.0,
    "exploit_found": true,
    "exploitation_registered_in_kev": false
  },
  "exploitation_stats": {
    "number_of_available_exploits": 1,
    "number_of_botnets_exploiting_vulnerability": 1,
    "number_of_threat_actors_exploiting_vulnerability": 1
  },
  "id": "CVE-2020-12345",
  "timeline": {
    "cisa_kev_date_added": "2020-07-08T17:15:10Z",
    "cve_last_updated_date": "2020-07-08T17:15:10Z",
    "cve_published_date": "2020-07-08T17:15:10Z",
    "first_known_published_date": "2020-07-08T17:15:10Z"
  }
}
```
### Triggers


#### Monitor IP List in GreyNoise

This trigger is used to query a list of IPs in GreyNoise based on IP List every interval to identify if any of them are
 actively scanning the internet

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|3600|True|How frequently, in seconds, to check the IP list|None|3600|None|None|
|ip_list|[]string|None|True|List of IP Addresses or CIDR blocks to check for scanning activity|None|[1.2.3.4,5.2.3.0/24]|None|None|
|lookback_days|integer|1|True|Number of Days to look back for scanning activity. Recommended "1", Max "90"|None|1|None|None|
  
Example input:

```
{
  "interval": 3600,
  "ip_list": "[1.2.3.4,5.2.3.0/24]",
  "lookback_days": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert_ip_list|[]string|False|The list of IPs that were found scanning|1.2.3.4,5.2.3.5|
  
Example output:

```
{
  "alert_ip_list": "1.2.3.4,5.2.3.5"
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ASN|string|None|False|ASN|AS12345|
|Category|string|None|False|Category|isp|
|City|string|None|False|City|Reno|
|Country|string|None|False|Country|Brazil|
|Country Code|string|None|False|Country Code|BZ|
|Destination Countries|[]string|None|False|List of countries with GreyNoise sensors that observed this IP|["Brazil", "Spain"]|
|Destination Country Codes|[]string|None|False|List of countries (by code) with GreyNoise sensors that observed this IP|["BZ", "ES"]|
|Organization|string|None|False|Organization|Acme Inc.|
|OS|string|None|False|OS|Windows XP|
|rDNS|string|None|False|rDNS|scanner.example.io|
|Region|string|None|False|Region|Arizona|
|Sensor Count|integer|None|False|Count of Sensors that observed traffic from this IP|5|
|Sensor Hits|integer|None|False|Count of Sensor events observed from this IP|5|
|Source Country|string|None|False|Source country where this IP is located|Brazil|
|Source Country Code|string|None|False|Source country (by code) where this IP is located|BE|
|TOR|boolean|None|False|TOR|False|
  
**web**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Web Paths|[]string|None|False|User Agents|["/", "/robots.txt"]|
|User Agents|[]string|None|False|User Agents|["user-agent"]|
  
**scan**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Port|integer|None|False|Port|22|
|Protocol|string|None|False|Protocol|TCP|
  
**hassh**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Fingerprint|string|None|False|Fingerprint|abcdefg1234567|
|Port|integer|None|False|Port|22|
  
**ja3**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Fingerprint|string|None|False|Fingerprint|abcdefg1234567|
|Port|integer|None|False|Port|22|
  
**raw_data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HASSH|[]hassh|None|False|HASSH|None|
|JA3|[]ja3|None|False|Ja3|None|
|Scan|[]scan|None|False|Scan|None|
|Web|web|None|False|Web|None|
  
**data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|GreyNoise Actor|string|None|False|GreyNoise Actor Associated with IP|Actor Name|
|GreyNoise Bot|boolean|None|False|GreyNoise has identified this as a Bot|False|
|GreyNoise Classification|string|None|False|GreyNoise Classification|benign|
|GreyNoise CVEs|[]string|None|False|CVEs associated with GreyNoise Tags|CVE-1234-12345|
|GreyNoise First Seen|date|None|False|First Seen By GreyNoise|2024-01-01|
|IP Address|string|None|False|IP Address|1.2.4.5|
|GreyNoise Last Seen|string|None|False|Last Seen By GreyNoise|2024-01-01|
|GreyNoise Metadata|metadata|None|False|GreyNoise IP Metadata|{'ASN': 'AS12345', 'Category': 'isp', 'City': 'Reno', 'Country': 'Brazil', 'Country Code': 'BZ', 'Destination Countries': ['Brazil', 'Spain'], 'Destination Country Codes': ['BZ', 'ES'], 'Organization': 'Acme Inc.', 'OS': 'Windows XP', 'rDNS': 'scanner.example.io', 'Region': 'Arizona', 'Sensor Count': 5, 'Sensor Hits': 5, 'Source Country': 'Brazil', 'Source Country Code': 'BE', 'TOR': False}|
|GreyNoise Raw Data|raw_data|None|False|GreyNoise IP Raw Data|{'HASSH': [{'Fingerprint': 'abcdefg1234567', 'Port': 22}], 'JA3': [{'Fingerprint': 'abcdefg1234567', 'Port': 22}], 'Scan': [{'Port': 22, 'Protocol': 'TCP'}], 'Web': {'Web Paths': ['/', '/robots.txt'], 'User Agents': ['user-agent']}}|
|GreyNoise Seen|boolean|None|False|Has this IP been Seen by GreyNoise|False|
|GreyNoise Spoofable|boolean|None|False|IP address may be spoofed|False|
|GreyNoise Tags|[]string|None|False|GreyNoise Tags Associated with IP|["tag1", "tag2"]|
|GreyNoise VPN|boolean|None|False|GreyNoise has identified this as a VPN|False|
|GreyNoise VPN Service|string|None|False|Name of VPN Service|VPN Name|
  
**vuln_timeline**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Date Added to CISA KEV|string|None|False|Date Added to CISA KEV|2020-07-08T17:15:10Z|
|Date CVE was Last Updated|string|None|False|Date CVE was Last Updated|2020-07-08T17:15:10Z|
|Date CVE was Published|string|None|False|Date CVE was Published|2020-07-08T17:15:10Z|
|Date of First Published POC|string|None|False|Date of First Published POC|2020-07-08T17:15:10Z|
  
**vuln_exploitation_stats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Number of Available Exploits|integer|None|False|Number of Available Exploits|1|
|Number of Associated Botnets|integer|None|False|Number of Associated Botnets|1|
|Number of Threat Actors Exploiting Vulnerability|integer|None|False|Number of Threat Actors Exploiting Vulnerability|1|
  
**vuln_exploitation_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attack Vector|string|None|False|Attack Vector|NETWORK|
|EPSS Score|float|None|False|EPSS Score|0.0|
|Exploit Found|boolean|None|False|Exploit Found|False|
|Exploitation Registered in KEV|boolean|None|False|Exploitation Registered in KEV|False|
  
**vuln_exploitation_activity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|GreyNoise Observed Activity|boolean|None|False|GreyNoise Observed Activity|True|
|Benign IP Count - 10 days|integer|None|False|Benign IP Count - 10 days|5|
|Benign IP Count - 1 day|integer|None|False|Benign IP Count - 1 day|5|
|Benign IP Count - 30 days|integer|None|False|Benign IP Count - 30 days|5|
|Last Seen|string|None|False|When GreyNoise last observed activity for this vulnerability|2026-11-03T15:19:43Z|
|Threat IP Count - 10 days|integer|None|False|Threat IP Count - 10 days|5|
|Threat IP Count - 1 day|integer|None|False|Threat IP Count - 1 day|5|
|Threat IP Count - 30 days|integer|None|False|Threat IP Count - 30 days|5|
  
**vuln_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVE CVSS Score|float|None|False|CVE CVSS Score|9.8|
|Product Name|string|None|False|Product Name|Product Name|
|Is CVE Published in NIST NVD|boolean|None|False|Is CVE Published in NIST NVD|False|
|Vendor Name|string|None|False|Vendor Name|Acme Inc|
|Vulnerability Description|string|None|False|Vulnerability Description|This is a product description.|
|Vulnerability Name|string|None|False|Vulnerability Name|This is a vuln name.|
  
**timeline_metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Days|integer|None|False|Number of days requested|1|
|Field|string|None|False|Timeline field included in the SDK metadata|classification|
|Granularity|string|None|False|Time bucket size used for the timeline|1d|
|IP Address|string|None|False|IP queried|100.29.192.92|
  
**timeline_day**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ASNs|[]string|None|False|ASNs observed on this day|["AS14618"]|
|Classification|[]string|None|False|Classifications observed on this day|["unknown"]|
|Date|date|None|False|Start of the daily timeline bucket|2026-10-30T00:00:00Z|
|Organizations|[]string|None|False|Organizations observed on this day|["Amazon.com, Inc."]|
|Ports|[]string|None|False|Destination ports observed on this day|["80", "443"]|
|rDNS|[]string|None|False|Reverse DNS values observed on this day|["ec2-100-29-192-92.compute-1.amazonaws.com"]|
|Tags|[]string|None|False|GreyNoise tags observed on this day|["DNS Protocol"]|
|User Agents|[]string|None|False|HTTP user agents observed on this day|["Mozilla/5.0"]|
|Web Paths|[]string|None|False|HTTP paths observed on this day|["/"]|
  
**timeline_activity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ASN|string|None|False|ASN|AS12345|
|Category|string|None|False|Category|isp|
|City|string|None|False|City|Seattle|
|GreyNoise Classification|string|None|False|GreyNoise Classification|benign|
|Country|string|None|False|Country|Spain|
|Country Code|string|None|False|Country Code|ES|
|Destinations|[]destinations|None|False|Destinations|None|
|HASSH Fingerprints|[]string|None|False|HASSH Fingerprints|["asdfa1412", "asasdf2125"]|
|HTTP Web Paths|[]string|None|False|HTTP Web Paths|["/", "/robots.txt"]|
|HTTP User Agents|[]string|None|False|HTTP User Agents|["/", "/robots.txt"]|
|JA3 Fingerprints|[]string|None|False|JA3 Fingerprints|["abasdfas", "abasdfasdf"]|
|Organization|string|None|False|Organization|Acme Inc|
|Protocols|[]protocols|None|False|Destinations|None|
|rDNS|string|None|False|rDNS|scanner.acme.io|
|Region|string|None|False|Region|Arizona|
|Spoofable|boolean|None|False|Spoofable|False|
|Tags|[]tags|None|False|Tags|None|
|Event Timestamp|date|None|False|Event Timestamp|2020-07-08T17:15:10Z|
|Tor Exit Node|boolean|None|False|Tor Exit Node|False|
|VPN|boolean|None|False|VPN|False|
|VPN Service|string|None|False|VPN Service|VPN Name|
  
**destinations**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Country|string|None|False|Country|Brazil|
|Country Code|string|None|False|Country Code|BE|
  
**protocols**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|App Protocol|string|None|False|App Protocol|http|
|Port|integer|None|False|Port|22|
|Transport Protocol|string|None|False|Transport Protocol|TCP|
  
**tags**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Tag Category|string|None|None|Category for given tag|protocol|
|Tag Created|string|None|False|When the tag was created|2024-01-01T00:00:00Z|
|Tag CVEs|[]string|None|False|CVEs associated with the tag|["CVE-2024-1234"]|
|Tag Description|string|None|None|Description for given tag|IP addresses with this tag have been observed sending SNMP traffic.|
|Tag ID|string|None|False|Unique identifier for the tag|13503954-9a41-447f-b7a1-8f82fe2258bd|
|Tag Intention|string|None|None|Intention for given tag|unknown|
|Tag Name|string|None|None|Name for given tag|SNMP Protocol|
|Recommend Block|boolean|None|False|Whether GreyNoise recommends blocking IPs with this tag|False|
|Tag References|[]string|None|False|Reference links associated with the tag|["https://datatracker.ietf.org/doc/html/rfc1157"]|
|Tag Slug|string|None|False|URL-safe slug for the tag|snmp-protocol|
|Tag Updated At|string|None|False|When the tag was last updated|2026-03-12T16:28:32Z|
  
**related_tag**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Tag Category|string|None|False|Category of the related tag|activity|
|Tag ID|string|None|False|Unique identifier for the related tag|da78f2eb-fe6b-4e84-913c-cdab4ff067c2|
|Tag Intention|string|None|False|Intention of the related tag|malicious|
|Tag Name|string|None|False|Name of the related tag|Oracle WebLogic RCE CVE-2020-14882|
|Tag Slug|string|None|False|URL-safe slug for the related tag|oracle-weblogic-rce-cve-2020-14882|
  
**tag_volume**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Session Count|integer|None|False|Number of sessions observed for the tag|200|
|Tag ID|string|None|False|Identifier of the tag this volume refers to|13503954-9a41-447f-b7a1-8f82fe2258bd|
  
**scanner_metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ASN|string|None|None|ASN for given IP|AS63949|
|ASN Subnet|string|None|False|Subnet associated with the ASN|100.24.0.0/13|
|Carrier|string|None|False|Carrier associated with the IP||
|Category|string|None|None|Category for IP|hosting|
|Datacenter|string|None|False|Datacenter associated with the IP||
|Destination ASNs|[]string|None|False|ASNs of destinations scanned by the IP|["AS14618"]|
|Destination Cities|[]string|None|False|Cities of destinations scanned by the IP|["Ashburn"]|
|Destination Countries|[]string|None|None|Destination Countries for given IP|["United States"]|
|Destination Country Codes|[]string|None|False|Country codes of destinations scanned by the IP|["US"]|
|Domain|string|None|False|Domain associated with the IP|amazon.com|
|Latitude|float|None|False|Latitude of the IP|39.0437|
|Longitude|float|None|False|Longitude of the IP|-77.4875|
|Mobile|boolean|None|False|Whether the IP is associated with a mobile network|False|
|Organization|string|None|None|Organization for given IP|Amazon.com, Inc.|
|OS|string|None|None|OS for given IP|Linux 2.2-3.x|
|rDNS|string|None|None|rDNS for given IP|ec2-100-29-192-92.compute-1.amazonaws.com|
|rDNS Parent|string|None|False|Parent domain of the reverse DNS record|amazonaws.com|
|rDNS Validated|boolean|None|False|Whether the reverse DNS record has been validated|False|
|Region|string|None|None|Region for given IP|Virginia|
|Sensor Count|integer|None|False|Number of sensors that observed the IP|6417|
|Sensor Hits|integer|None|False|Number of sensor hits for the IP|33850|
|Single Destination|boolean|None|False|Whether the IP was observed targeting a single destination|False|
|City|string|None|None|City for given IP|Ashburn|
|Country|string|None|None|Country for given IP|United States|
|Country Code|string|None|None|Country Code for given IP|US|
  
**scanner_http**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HTTP Cookie Keys|[]string|None|False|Cookie keys observed in HTTP requests|[]|
|JA4H|[]string|None|False|JA4H fingerprints observed for the IP|[]|
|HTTP MD5|[]string|None|False|MD5 hashes of observed HTTP payloads|[]|
|HTTP Methods|[]string|None|False|HTTP methods observed for the IP|["GET"]|
|HTTP Paths|[]string|None|None|HTTP paths observed for the IP|["/"]|
|HTTP Authorization|[]string|None|False|Authorization header values observed in HTTP requests|[]|
|HTTP Cookies|[]string|None|False|Cookie values observed in HTTP requests|[]|
|HTTP Headers|[]string|None|False|HTTP request headers observed for the IP|[]|
|HTTP Origin|[]string|None|False|Origin header values observed in HTTP requests|[]|
|HTTP User Agents|[]string|None|None|HTTP user agents observed for the IP|["Mozilla/5.0"]|
  
**scanner_tls**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|TLS Ciphers|[]string|None|False|TLS ciphers observed for the IP|[]|
|JA4|[]string|None|None|JA4 fingerprints observed for the IP|["t13d1516h2_8daaf6152771_e5627efa2ab1"]|
  
**scanner_source**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Bytes|integer|None|False|Bytes observed from the source IP|1822448|
|Sessions|integer|None|False|Sessions observed from the source IP|40000|
  
**scanner_ssh**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|JA4SSH|[]string|None|False|JA4SSH fingerprints observed for the IP|[]|
|SSH Keys|[]string|None|False|SSH keys observed for the IP|[]|
  
**scanner_tcp**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|JA4L|[]string|None|False|JA4L fingerprints observed for the IP|[]|
|JA4T|[]string|None|False|JA4T fingerprints observed for the IP|["65535_2_1460_00"]|
  
**scanner_raw_data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HASSH|[]hassh|None|False|HASSH fingerprints observed for the IP|None|
|HTTP|scanner_http|None|False|HTTP metadata observed for the IP|None|
|JA3|[]ja3|None|False|JA3 fingerprints observed for the IP|None|
|Scan Data|[]scan|None|False|Ports and protocols scanned by the IP|None|
|Source|scanner_source|None|False|Source traffic volume observed for the IP|None|
|SSH|scanner_ssh|None|False|SSH metadata observed for the IP|None|
|TCP|scanner_tcp|None|False|TCP fingerprint metadata observed for the IP|None|
|TLS|scanner_tls|None|False|TLS metadata observed for the IP|None|
  
**internet_scanner_intelligence**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actor|string|None|False|Actor associated with the IP|unknown|
|BOT|boolean|None|False|Whether the IP is associated with known BOT activity|False|
|Callback IPs|[]string|None|False|Callback IP addresses associated with the IP|[]|
|IP Classification|string|None|False|Whether the IP is malicious, benign, or unknown|suspicious|
|CVEs|[]string|None|False|CVEs associated with the IP|["CVE-2024-1234"]|
|First Seen|string|None|False|Date the IP was first observed by GreyNoise|2025-10-14|
|IP Found|boolean|None|False|Whether the IP was found in GreyNoise|True|
|Last Seen|string|None|False|Date the IP was last observed by GreyNoise|2026-10-30|
|Last Seen Benign|string|None|False|When the IP was last seen classified as benign||
|Last Seen Malicious|string|None|False|When the IP was last seen classified as malicious||
|Last Seen Suspicious|string|None|False|When the IP was last seen classified as suspicious|2026-10-01T15:09:57Z|
|Last Seen Timestamp|string|None|False|Timestamp the IP was last observed by GreyNoise|2026-10-30 19:31:39|
|Metadata|scanner_metadata|None|False|Metadata for the IP address|None|
|Raw Data|scanner_raw_data|None|False|Raw scanning data observed for the IP|{'scan': [{'port': 22, 'protocol': 'TCP'}]}|
|Spoofable|boolean|None|False|Whether the traffic from the IP can be spoofed|True|
|Tag Volumes|[]tag_volume|None|False|Session counts for tags associated with the IP|None|
|Tags|[]tags|None|False|GreyNoise tags associated with the IP|None|
|TOR|boolean|None|False|Whether the IP is a known TOR exit node|False|
|VPN|boolean|None|False|Whether the IP is associated with a known VPN service|False|
|VPN Service|string|None|False|VPN service associated with the IP, when known||
  
**business_service_intelligence**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|False|Business service category|public_dns|
|Description|string|None|False|Business service description|Acme Inc is an example service.|
|Explanation|string|None|False|Explanation for why this is a common business service|This IP provides a common business service.|
|Found|boolean|None|False|IP was found in Business Service Intelligence|True|
|Last Updated|string|None|False|Last time this IP was updated in Business Service Intelligence|2024-01-01|
|Name|string|None|False|Business service name|Acme Inc|
|Reference|string|None|False|Reference for the business service|https://example.com|
|Trust Level|string|None|False|Business service trust level|1|
  
**gnql_ip**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Business Service Intelligence|business_service_intelligence|None|False|Business Service Intelligence for the IP|{'found': False, 'trust_level': ''}|
|Internet Scanner Intelligence|internet_scanner_intelligence|None|False|Internet Scanner Intelligence for the IP|{'found': True, 'classification': 'malicious'}|
|IP Address|string|None|False|IP address returned by the query|1.2.3.4|
  
**gnql_request_metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Adjusted Query|string|None|False|Query after GreyNoise applied plan or default adjustments|(classification:malicious) last_seen:90d|
|Complete|boolean|None|False|Whether all query results have been returned|False|
|Count|integer|None|False|Total number of IPs matching the query|147|
|Message|string|None|False|Status message for the query|ok|
|Query|string|None|False|GNQL query that was executed|classification:malicious|
|Restricted Fields|[]string|None|False|Fields omitted because of the account plan|[]|
|Scroll Token|string|None|False|Token to request the next page of results||
  
**callback_file**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|File Name|string|None|False|Original file name, when known|payload.bin|
|MD5|string|None|False|MD5 hash of the file|795bc7ce13f60d61e9ac03611dd36d90|
|SHA1|string|None|False|SHA-1 hash of the file|da39a3ee5e6b4b0d3255bfef95601890afd80709|
|SHA256|string|None|False|SHA-256 hash of the file|e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855|
|File Size|integer|None|False|File size in bytes|24576|
|Threat Name|string|None|False|VirusTotal threat name, when available|Trojan.GenericKD.46542|
|File Type|string|None|False|File MIME type|application/x-executable|
|VirusTotal Detection Count|integer|None|False|Number of VirusTotal engines that flagged the file|42|
|VirusTotal Engine Count|integer|None|False|Number of VirusTotal engines that scanned the file|71|


## Troubleshooting


# Version History

* 3.0.0 - Upgrade GreyNoise SDK v3.1.0 | Add `ip_lookup` and `callback_ip_lookup` | Keep `context_lookup` and `riot_lookup` as aliases that call `ip_lookup` | Update `quick_lookup`, `gnql_query`, `get_tag_details`, and `monitor_ips_in_greynoise` for the v3 API | Remove `similar_lookup` | Updated SDK to the latest version (6.6.1)
* 2.0.0 - Upgrade GreyNoise SDK v2.3.0 | Fix Action Outputs | New actions:`vulnerability_lookup`, `timeline_lookup`, `similar_lookup` | New trigger: `greynoise_alert`
* 1.0.1 - Fix bug with connection parameters
* 1.0.0 - Initial plugin.

# Links

* [GreyNoise](https://greynoise.io)

## References

* [GreyNoise Documentation](https://docs.greynoise.io)
* [GreyNoise Free Trial Signup](https://viz.greynoise.io/signup)
* [GreyNoise Account Info](https://viz.greynoise.io/account)