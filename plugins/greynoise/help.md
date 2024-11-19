# Description

GreyNoise helps analysts recognize events not worth their attention. Indicators in GreyNoise are likely associated with opportunistic internet scanning or common business services, not targeted threats. This context helps analysts focus on what matters most

# Key Features

* Perform a GreyNoise IP Context Lookup
* Perform a GreyNoise IP Quick Lookup
* Perform a GreyNoise IP RIOT Lookup
* Query for additional Tag details
* Perform a GreyNoise Community IP Lookup
* Perform a GreyNoise Vulnerability Lookup
* Perform a GreyNoise IP Timeline Lookup
* Perform a GreyNoise IP Similarity Lookup
* Query a list of IPs on a Trigger

# Requirements

* A GreyNoise API key

# Supported Product Versions

* GreyNoise API v1/2/3

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

This action is used to query a routable IPv4 address in the GreyNoise Context API endpoint

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
|actor|string|False|GreyNoise Actor Associated with IP|Acme, Inc|
|bot|boolean|False|GreyNoise has identified this as a Bot|False|
|classification|string|False|GreyNoise Classification|malicious|
|cve|[]string|False|CVEs associated with GreyNoise Tags|["CVE-1111-1111", "CVE-2222-2222"]|
|first_seen|date|False|First Seen By GreyNoise|2024-01-01|
|ip|string|False|Value that was Queried|1.2.3.4|
|last_seen|string|False|Last Seen By GreyNoise|2024-01-01|
|metadata|metadata|False|GreyNoise IP Metadata|{'asn': 'AS12345', 'category': 'isp', 'city': 'Reno', 'country': 'Brazil', 'country_code': 'BZ', 'destination_countries': ['Brazil', 'Spain'], 'destination_country_codes': ['BZ', 'ES'], 'organization': 'Acme Inc.', 'os': 'Windows XP', 'rdns': 'scanner.example.io', 'region': 'Arizona', 'sensor_count': 5, 'sensor_hits': 5, 'source_country': 'Brazil', 'source_country_code': 'BE', 'tor': False}|
|raw_data|raw_data|False|GreyNoise IP Raw Data|{'hassh': [{'fingerprint': 'abcdefg1234567', 'port': 22}], 'ja3': [{'fingerprint': 'abcdefg1234567', 'port': 22}], 'scan': [{'port': 22, 'protocol': 'TCP'}], 'web': {'paths': ['/', '/robots.txt'], 'useragents': ['user-agent']}}|
|seen|boolean|False|Has this IP been Seen by GreyNoise|True|
|spoofable|boolean|False|IP address may be spoofed|False|
|tags|[]string|False|GreyNoise Tags Associated with IP|Tag 1, Tag2|
|viz_url|string|False|Link to GreyNoise Visualizer for IP Details|https://viz.greynoise.io/ip/1.1.1.1|
|vpn|boolean|False|GreyNoise has identified this as a VPN|False|
|vpn_service|string|False|Name of VPN Service|My VPN|
  
Example output:

```
{
  "actor": "Acme, Inc",
  "bot": false,
  "classification": "malicious",
  "cve": [
    "CVE-1111-1111",
    "CVE-2222-2222"
  ],
  "first_seen": "2024-01-01",
  "ip": "1.2.3.4",
  "last_seen": "2024-01-01",
  "metadata": {
    "asn": "AS12345",
    "category": "isp",
    "city": "Reno",
    "country": "Brazil",
    "country_code": "BZ",
    "destination_countries": [
      "Brazil",
      "Spain"
    ],
    "destination_country_codes": [
      "BZ",
      "ES"
    ],
    "organization": "Acme Inc.",
    "os": "Windows XP",
    "rdns": "scanner.example.io",
    "region": "Arizona",
    "sensor_count": 5,
    "sensor_hits": 5,
    "source_country": "Brazil",
    "source_country_code": "BE",
    "tor": false
  },
  "raw_data": {
    "hassh": [
      {
        "fingerprint": "abcdefg1234567",
        "port": 22
      }
    ],
    "ja3": [
      {
        "fingerprint": "abcdefg1234567",
        "port": 22
      }
    ],
    "scan": [
      {
        "port": 22,
        "protocol": "TCP"
      }
    ],
    "web": {
      "paths": [
        "/",
        "/robots.txt"
      ],
      "useragents": [
        "user-agent"
      ]
    }
  },
  "seen": true,
  "spoofable": false,
  "tags": "Tag 1, Tag2",
  "viz_url": "https://viz.greynoise.io/ip/1.1.1.1",
  "vpn": false,
  "vpn_service": "My VPN"
}
```

#### Get Tag Details

This action is used to get Details of a GreyNoise Tag

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
|related_tags|[]string|False|Tags that are related to this tag|["BingBot Scanner"]|
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
    "BingBot Scanner"
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
|size|string|10|False|Max Number of IPs to Return Data For|None|10|None|None|
  
Example input:

```
{
  "query": "last_seen:1d classification:'malicious' metadata.asn:'AS8452'",
  "size": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|complete|boolean|False|Indicates if all pages of the query have been returned by the API|True|
|count|integer|False|Total count of IPs returned Query|10|
|data|[]data|False|GreyNoise Data Object, Contains IP Object for each IP returned by the query|[{"actor": "Acme, Inc", "bot": false, "classification": "malicious", "cve": ["CVE-1111-1111", "CVE-2222-2222"], "first_seen": "2024-01-01", "ip": "1.2.3.4", "last_seen": "2024-01-01", "metadata": {"asn": "AS12345", "category": "isp", "city": "Reno", "country": "Brazil", "country_code": "BZ", "destination_countries": ["Brazil", "Spain"], "destination_country_codes": ["BZ", "ES"], "organization": "Acme Inc.", "os": "Windows XP", "rdns": "scanner.example.io", "region": "Arizona", "sensor_count": 5, "sensor_hits": 5, "source_country": "Brazil", "source_country_code": "BE", "tor": false}, "raw_data": {"hassh": [{"fingerprint": "abcdefg1234567", "port": 22}], "ja3": [{"fingerprint": "abcdefg1234567", "port": 22}], "scan": [{"port": 22, "protocol": "TCP"}], "web": {"paths": ["/", "/robots.txt"], "useragents": ["user-agent"]}}, "seen": true, "spoofable": false, "tags": "Tag 1, Tag2", "vpn": false, "vpn_service": "My VPN"}]|
|message|string|False|GreyNoise Query Message, indicates if there were issues with the query|ok|
|query|string|False|GreyNoise Query Sent to API|sample query|
  
Example output:

```
{
  "complete": true,
  "count": 10,
  "data": [
    {
      "actor": "Acme, Inc",
      "bot": false,
      "classification": "malicious",
      "cve": [
        "CVE-1111-1111",
        "CVE-2222-2222"
      ],
      "first_seen": "2024-01-01",
      "ip": "1.2.3.4",
      "last_seen": "2024-01-01",
      "metadata": {
        "asn": "AS12345",
        "category": "isp",
        "city": "Reno",
        "country": "Brazil",
        "country_code": "BZ",
        "destination_countries": [
          "Brazil",
          "Spain"
        ],
        "destination_country_codes": [
          "BZ",
          "ES"
        ],
        "organization": "Acme Inc.",
        "os": "Windows XP",
        "rdns": "scanner.example.io",
        "region": "Arizona",
        "sensor_count": 5,
        "sensor_hits": 5,
        "source_country": "Brazil",
        "source_country_code": "BE",
        "tor": false
      },
      "raw_data": {
        "hassh": [
          {
            "fingerprint": "abcdefg1234567",
            "port": 22
          }
        ],
        "ja3": [
          {
            "fingerprint": "abcdefg1234567",
            "port": 22
          }
        ],
        "scan": [
          {
            "port": 22,
            "protocol": "TCP"
          }
        ],
        "web": {
          "paths": [
            "/",
            "/robots.txt"
          ],
          "useragents": [
            "user-agent"
          ]
        }
      },
      "seen": true,
      "spoofable": false,
      "tags": "Tag 1, Tag2",
      "vpn": false,
      "vpn_service": "My VPN"
    }
  ],
  "message": "ok",
  "query": "sample query"
}
```

#### Quick IP Lookup

This action is used to query a routable IPv4 address in the GreyNoise Quick API endpoint

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
|code|string|False|Response Code from Quick API endpoint|00x0|
|code_message|string|False|Response Code Message from Quick API endpoint|Internet noise found|
|ip|string|False|Value that was Queried|1.2.3.4|
|noise|boolean|False|Defines if IP is Internet Noise|True|
|riot|boolean|False|Defines if IP is a Common Business Service|True|
  
Example output:

```
{
  "code": "00x0",
  "code_message": "Internet noise found",
  "ip": "1.2.3.4",
  "noise": true,
  "riot": true
}
```

#### RIOT IP Lookup

This action is used to query a routable IPv4 address in the GreyNoise RIOT API endpoint

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
|category|string|False|RIOT Category IP is part of|cdn|
|description|string|False|Description of the IP service|Acme Inc is just an example.|
|explanation|string|False|Explanation for why this is likely a common service|This is an explanation.|
|ip|string|False|Value that was Queried|1.2.3.4|
|last_updated|date|False|Last time this IP was updated in RIOT dataset|2024-01-01|
|name|string|False|Vendor Name IP belongs to|Acme Inc.|
|reference|string|False|Additional reference information|http://one.one.one.one|
|riot|boolean|False|Defines if IP is part of GreyNoise RIOT dataset|True|
|trust_level|string|False|IP Trust Level information|1|
|viz_url|string|False|Link to GreyNoise Visualizer for IP Details|https://viz.greynoise.io/ip/1.1.1.1|
  
Example output:

```
{
  "category": "cdn",
  "description": "Acme Inc is just an example.",
  "explanation": "This is an explanation.",
  "ip": "1.2.3.4",
  "last_updated": "2024-01-01",
  "name": "Acme Inc.",
  "reference": "http://one.one.one.one",
  "riot": true,
  "trust_level": 1,
  "viz_url": "https://viz.greynoise.io/ip/1.1.1.1"
}
```

#### IP Similarity Lookup

This action is used to query a routable IPv4 address in the GreyNoise for similar IPs

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
|ip|ip_sim|False|IP Similarity Metadata|{'actor': 'Acme Inc.', 'asn': 'AS12345', 'city': 'Seattle', 'classification': 'benign', 'country': 'Brazil', 'country_code': 'BE', 'first_seen': '2020-07-08T17:15:10Z', 'ip': '1.2.3.4', 'last_seen': '2020-07-08T17:15:10Z', 'organization': 'Acme Inc'}|
|similar_ips|[]similar_ip|False|Similar IPs|[{"actor": "Acme Inc", "asn": "AS12345", "city": "New York", "classification": "benign", "country": "Ukraine", "country_code": "UK", "features_matched": ["feature-1", "feature-2"], "first_seen": "2020-07-08T17:15:10Z", "ip": "1.2.3.4", "last_seen": "2020-07-08T17:15:10Z", "organization": "Acme Inc", "score": 0.83}]|
|total|integer|False|Total Number of Similar IPs returned|5|
  
Example output:

```
{
  "ip": {
    "actor": "Acme Inc.",
    "asn": "AS12345",
    "city": "Seattle",
    "classification": "benign",
    "country": "Brazil",
    "country_code": "BE",
    "first_seen": "2020-07-08T17:15:10Z",
    "ip": "1.2.3.4",
    "last_seen": "2020-07-08T17:15:10Z",
    "organization": "Acme Inc"
  },
  "similar_ips": [
    {
      "actor": "Acme Inc",
      "asn": "AS12345",
      "city": "New York",
      "classification": "benign",
      "country": "Ukraine",
      "country_code": "UK",
      "features_matched": [
        "feature-1",
        "feature-2"
      ],
      "first_seen": "2020-07-08T17:15:10Z",
      "ip": "1.2.3.4",
      "last_seen": "2020-07-08T17:15:10Z",
      "organization": "Acme Inc",
      "score": 0.83
    }
  ],
  "total": 5
}
```

#### IP Timeline Lookup

This action is used to query a routable IPv4 address in the GreyNoise for Scanner Daily Timeline details

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
|activity|[]timeline_activity|False|IP Timeline Activity Events|[{"asn": "AS12345", "category": "isp", "city": "Seattle", "classification": "benign", "country": "Spain", "country_code": "ES", "destinations": [{"country": "Brazil", "country_code": "BE"}], "hassh_fingerprints": ["asdfa1412", "asasdf2125"], "http_web_paths": ["robots.txt"], "http_user_agents": ["Hello World"], "ja3_fingerprints": ["abasdfas", "abasdfasdf"], "organization": "Acme Inc", "protocols": [{"port": 22, "transport_protocol": "TCP", "app_protocol": "TCP"}], "rdns": "scanner.acme.io", "region": "Arizona", "spoofable": false, "tags": [{"tag_category": "activity", "tag_description": "This is a description of the tag.", "tag_intention": "malicious", "tag_name": "IoT Bot Tag"}], "timestampe": "2020-07-08T17:15:10Z", "tor": false, "vpn": false, "vpn_service": "VPN Name"}]|
|ip|string|False|Value that was Queried|1.2.3.4|
|metadata|timeline_metadata|False|IP Timeline Metadata|{'end_time': '2020-07-08T17:15:10Z', 'ip': '1.2.3.4', 'limit': 5, 'next_cursor': 'asdf142qas3241asdf234sfa', 'start_time': '2020-07-08T17:15:10Z'}|
  
Example output:

```
{
  "activity": [
    {
      "asn": "AS12345",
      "category": "isp",
      "city": "Seattle",
      "classification": "benign",
      "country": "Spain",
      "country_code": "ES",
      "destinations": [
        {
          "country": "Brazil",
          "country_code": "BE"
        }
      ],
      "hassh_fingerprints": [
        "asdfa1412",
        "asasdf2125"
      ],
      "http_user_agents": [
        "Hello World"
      ],
      "http_web_paths": [
        "robots.txt"
      ],
      "ja3_fingerprints": [
        "abasdfas",
        "abasdfasdf"
      ],
      "organization": "Acme Inc",
      "protocols": [
        {
          "app_protocol": "TCP",
          "port": 22,
          "transport_protocol": "TCP"
        }
      ],
      "rdns": "scanner.acme.io",
      "region": "Arizona",
      "spoofable": false,
      "tags": [
        {
          "tag_category": "activity",
          "tag_description": "This is a description of the tag.",
          "tag_intention": "malicious",
          "tag_name": "IoT Bot Tag"
        }
      ],
      "timestampe": "2020-07-08T17:15:10Z",
      "tor": false,
      "vpn": false,
      "vpn_service": "VPN Name"
    }
  ],
  "ip": "1.2.3.4",
  "metadata": {
    "end_time": "2020-07-08T17:15:10Z",
    "ip": "1.2.3.4",
    "limit": 5,
    "next_cursor": "asdf142qas3241asdf234sfa",
    "start_time": "2020-07-08T17:15:10Z"
  }
}
```

#### Vulnerability Lookup

This action is used to check GreyNoise for Vulnerability information

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
|interval|integer|3600|True|How frequently (in seconds) to trigger a greeting|None|3600|None|None|
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
|Timeline Period End Time|date|None|False|Timeline Period End Time|2020-07-08T17:15:10Z|
|IP Address|string|None|False|IP Queried|1.2.3.4|
|Event Limit|integer|None|False|Max number of events to return|5|
|Cursor Value|string|None|False|Cursor value for additional pages of details|asdf142qas3241asdf234sfa|
|Timeline Period Start Time|date|None|False|Timeline Period Start Time|2020-07-08T17:15:10Z|
  
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
|Tag Category|string|None|False|Tag Category|activity|
|Tag Description|string|None|False|Tag Description|This is a description of the tag.|
|Tag Intention|string|None|False|Tag Intention|malicious|
|Tag Name|string|None|False|Tag Name|IoT Bot Tag|
  
**ip_sim**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actor|string|None|False|Actor|Acme Inc.|
|ASN|string|None|False|ASN|AS12345|
|City|string|None|False|City|Seattle|
|Classification|string|None|False|Classification|benign|
|Country|string|None|False|Country|Brazil|
|Country Code|string|None|False|Country Code|BE|
|First Seen|string|None|False|First Seen|2020-07-08T17:15:10Z|
|IP Address|string|None|False|IP Address|1.2.3.4|
|Last Seen|string|None|False|Last Seen|2020-07-08T17:15:10Z|
|Organization|string|None|False|Organization|Acme Inc|
  
**similar_ip**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actor|string|None|False|Actor|Acme Inc|
|ASN|string|None|False|ASN|AS12345|
|City|string|None|False|City|New York|
|Classification|string|None|False|Classification|benign|
|Country|string|None|False|Country|Ukraine|
|Country Code|string|None|False|Country Code|UK|
|Features Matched|[]string|None|False|Features Matched|["feature-1", "feature-2"]|
|First Seen|string|None|False|First Seen|2020-07-08T17:15:10Z|
|IP Address|string|None|False|IP Address|1.2.3.4|
|Last Seen|string|None|False|Last Seen|2020-07-08T17:15:10Z|
|Organization|string|None|False|Organization|Acme Inc|
|Similarity Score|float|None|False|Similarity Score|0.83|


## Troubleshooting

Ensure that the GreyNoise API key used has appropriate access for the actions being used.

# Version History

* 2.0.0 - Upgrade GreyNoise SDK v2.3.0 | Fix Action Outputs | New actions:`vulnerability_lookup`, `timeline_lookup`, `similar_lookup` | New trigger: `greynoise_alert`
* 1.0.1 - Fix bug with connection parameters
* 1.0.0 - Initial plugin.

# Links

* [GreyNoise](https://greynoise.io)

## References

* [GreyNoise Documentation](https://docs.greynoise.io)
* [GreyNoise Free Trial Signup](https://viz.greynoise.io/signup)
* [GreyNoise Account Info](https://viz.greynoise.io/account)