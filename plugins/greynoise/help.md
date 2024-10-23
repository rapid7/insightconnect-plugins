# Description

GreyNoise helps analysts recognize events not worth their attention. Indicators in GreyNoise are likely associated with opportunistic internet scanning or common business services, not targeted threats. This context helps analysts focus on what matters most

# Key Features

* Perform a GreyNoise IP Context Lookup
* Perform a GreyNoise IP Quick Lookup
* Perform a GreyNoise IP RIOT Lookup
* Query for additional Tag details
* Perform a GreyNoise Community IP Lookup
* Perform a GreyNoise Vulnerability Lookup

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
|metadata|metadata|False|GreyNoise IP Metadata|None|
|raw_data|raw_data|False|GreyNoise IP Raw Data|None|
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
    "ASN": "",
    "Category": {},
    "City": {},
    "Country": {},
    "Country Code": {},
    "Destination Countries": [
      {}
    ],
    "Destination Country Codes": {},
    "OS": {},
    "Organization": {},
    "Region": {},
    "Sensor Count": 0,
    "Sensor Hits": {},
    "Source Country": {},
    "Source Country Code": {},
    "TOR": "true",
    "rDNS": {}
  },
  "raw_data": {
    "HASSH": [
      {
        "Fingerprint": "",
        "Port": 0
      }
    ],
    "JA3": [
      {
        "Fingerprint": {},
        "Port": {}
      }
    ],
    "Scan": [
      {
        "Port": {},
        "Protocol": {}
      }
    ],
    "Web": {
      "User Agents": {}
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
|related_tags|[]string|False|Tags that are related to this tag|BingBot Scanner|
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
  "related_tags": "BingBot Scanner",
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
|data|[]data|False|GreyNoise Data Object, Contains IP Object for each IP returned by the query||
|message|string|False|GreyNoise Query Message, indicates if there were issues with the query|ok|
|query|string|False|GreyNoise Query Sent to API|sample query|
  
Example output:

```
{
  "complete": true,
  "count": 10,
  "data": "",
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
|ip|ip_sim|False|IP Similarity Metadata|None|
|similar_ips|[]similar_ip|False|Similar IPs|None|
|total|integer|False|Total Number of Similar IPs returned|None|
  
Example output:

```
{
  "ip": {
    "ASN": {},
    "Actor": "",
    "City": {},
    "Classification": {},
    "Country": {},
    "Country Code": {},
    "First Seen": {},
    "IP Address": {},
    "Last Seen": {},
    "Organization": {}
  },
  "similar_ips": [
    {
      "ASN": {},
      "Actor": "",
      "City": {},
      "Classification": {},
      "Country": {},
      "Country Code": {},
      "Features Matched": [
        {}
      ],
      "First Seen": {},
      "IP Address": {},
      "Last Seen": {},
      "Organization": {},
      "Similarity Score": 0.0
    }
  ],
  "total": 0
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
|activity|[]timeline_activity|False|IP Timeline Activity Events|None|
|ip|string|False|Value that was Queried|1.2.3.4|
|metadata|timeline_metadata|False|IP Timeline Metadata|None|
  
Example output:

```
{
  "activity": [
    {
      "ASN": "",
      "Category": {},
      "City": {},
      "Country": {},
      "Country Code": {},
      "Destinations": [
        {
          "Country": {},
          "Country Code": {}
        }
      ],
      "Event Timestamp": "",
      "GreyNoise Classification": {},
      "HASSH Fingerprints": [
        {}
      ],
      "HTTP User Agents": {},
      "HTTP Web Paths": {},
      "JA3 Fingerprints": {},
      "Organization": {},
      "Protocols": [
        {
          "App Protocol": {},
          "Port": 0,
          "Transport Protocol": {}
        }
      ],
      "Region": {},
      "Spoofable": "true",
      "Tags": [
        {
          "Tag Category": {},
          "Tag Description": {},
          "Tag Intention": {},
          "Tag Name": {}
        }
      ],
      "Tor Exit Node": {},
      "VPN": {},
      "VPN Service": {},
      "rDNS": {}
    }
  ],
  "ip": "1.2.3.4",
  "metadata": {
    "Cursor Value": {},
    "Event Limit": 0,
    "IP Address": "",
    "Timeline Period End Time": "",
    "Timeline Period Start Time": {}
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
|details|vuln_details|False|GreyNoise Vulnerability Details|None|
|exploitation_activity|vuln_exploitation_activity|False|GreyNoise Vulnerability Exploitation Activity|None|
|exploitation_details|vuln_exploitation_details|False|GreyNoise Vulnerability Exploitation Details|None|
|exploitation_stats|vuln_exploitation_stats|False|GreyNoise Vulnerability Exploitation Stats|None|
|id|string|False|Value that was searched|CVE-2020-12345|
|timeline|vuln_timeline|False|GreyNoise Vulnerability Timeline|None|
  
Example output:

```
{
  "details": {
    "CVE CVSS Score": 0.0,
    "Is CVE Published in NIST NVD": "true",
    "Product Name": "",
    "Vendor Name": {},
    "Vulnerability Description": {},
    "Vulnerability Name": {}
  },
  "exploitation_activity": {
    "Benign IP Count - 1 day": {},
    "Benign IP Count - 10 days": 0,
    "Benign IP Count - 30 days": {},
    "GreyNoise Observed Activity": "true",
    "Threat IP Count - 1 day": {},
    "Threat IP Count - 10 days": {},
    "Threat IP Count - 30 days": {}
  },
  "exploitation_details": {
    "Attack Vector": "",
    "EPSS Score": 0.0,
    "Exploit Found": "true",
    "Exploitation Registered in KEV": {}
  },
  "exploitation_stats": {
    "Number of Associated Botnets": {},
    "Number of Available Exploits": 0,
    "Number of Threat Actors Exploiting Vulnerability": {}
  },
  "id": "CVE-2020-12345",
  "timeline": {
    "Date Added to CISA KEV": "",
    "Date CVE was Last Updated": {},
    "Date CVE was Published": {},
    "Date of First Published POC": {}
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ASN|string|None|False|ASN|None|
|Category|string|None|False|Category|None|
|City|string|None|False|City|None|
|Country|string|None|False|Country|None|
|Country Code|string|None|False|Country Code|None|
|Destination Countries|[]string|None|False|List of countries with GreyNoise sensors that observed this IP|None|
|Destination Country Codes|[]string|None|False|List of countries (by code) with GreyNoise sensors that observed this IP|None|
|Organization|string|None|False|Organization|None|
|OS|string|None|False|OS|None|
|rDNS|string|None|False|rDNS|None|
|Region|string|None|False|Region|None|
|Sensor Count|integer|None|False|Count of Sensors that observed traffic from this IP|None|
|Sensor Hits|integer|None|False|Count of Sensor events observed from this IP|None|
|Source Country|string|None|False|Source country where this IP is located|None|
|Source Country Code|string|None|False|Source country (by code) where this IP is located|None|
|TOR|boolean|None|False|TOR|None|
  
**web**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|User Agents|[]string|None|False|User Agents|None|
|User Agents|[]string|None|False|User Agents|None|
  
**scan**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Port|integer|None|False|Port|None|
|Protocol|string|None|False|Protocol|None|
  
**hassh**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Fingerprint|string|None|False|Fingerprint|None|
|Port|integer|None|False|Port|None|
  
**ja3**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Fingerprint|string|None|False|Fingerprint|None|
|Port|integer|None|False|Port|None|
  
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
|GreyNoise Actor|string|None|False|GreyNoise Actor Associated with IP|None|
|GreyNoise Bot|boolean|None|False|GreyNoise has identified this as a Bot|None|
|GreyNoise Classification|string|None|False|GreyNoise Classification|None|
|GreyNoise CVEs|[]string|None|False|CVEs associated with GreyNoise Tags|None|
|GreyNoise First Seen|date|None|False|First Seen By GreyNoise|None|
|IP Address|string|None|False|IP Address|None|
|GreyNoise Last Seen|string|None|False|Last Seen By GreyNoise|None|
|GreyNoise Metadata|metadata|None|False|GreyNoise IP Metadata|None|
|GreyNoise Raw Data|raw_data|None|False|GreyNoise IP Raw Data|None|
|GreyNoise Seen|boolean|None|False|Has this IP been Seen by GreyNoise|None|
|GreyNoise Spoofable|boolean|None|False|IP address may be spoofed|None|
|GreyNoise Tags|[]string|None|False|GreyNoise Tags Associated with IP|None|
|GreyNoise VPN|boolean|None|False|GreyNoise has identified this as a VPN|None|
|GreyNoise VPN Service|string|None|False|Name of VPN Service|None|
  
**vuln_timeline**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Date Added to CISA KEV|string|None|False|Date Added to CISA KEV|None|
|Date CVE was Last Updated|string|None|False|Date CVE was Last Updated|None|
|Date CVE was Published|string|None|False|Date CVE was Published|None|
|Date of First Published POC|string|None|False|Date of First Published POC|None|
  
**vuln_exploitation_stats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Number of Available Exploits|integer|None|False|Number of Available Exploits|None|
|Number of Associated Botnets|integer|None|False|Number of Associated Botnets|None|
|Number of Threat Actors Exploiting Vulnerability|integer|None|False|Number of Threat Actors Exploiting Vulnerability|None|
  
**vuln_exploitation_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attack Vector|string|None|False|Attack Vector|None|
|EPSS Score|float|None|False|EPSS Score|None|
|Exploit Found|boolean|None|False|Exploit Found|None|
|Exploitation Registered in KEV|boolean|None|False|Exploitation Registered in KEV|None|
  
**vuln_exploitation_activity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|GreyNoise Observed Activity|boolean|None|False|GreyNoise Observed Activity|None|
|Benign IP Count - 10 days|integer|None|False|Benign IP Count - 10 days|None|
|Benign IP Count - 1 day|integer|None|False|Benign IP Count - 1 day|None|
|Benign IP Count - 30 days|integer|None|False|Benign IP Count - 30 days|None|
|Threat IP Count - 10 days|integer|None|False|Threat IP Count - 10 days|None|
|Threat IP Count - 1 day|integer|None|False|Threat IP Count - 1 day|None|
|Threat IP Count - 30 days|integer|None|False|Threat IP Count - 30 days|None|
  
**vuln_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVE CVSS Score|float|None|False|CVE CVSS Score|None|
|Product Name|string|None|False|Product Name|None|
|Is CVE Published in NIST NVD|boolean|None|False|Is CVE Published in NIST NVD|None|
|Vendor Name|string|None|False|Vendor Name|None|
|Vulnerability Description|string|None|False|Vulnerability Description|None|
|Vulnerability Name|string|None|False|Vulnerability Name|None|
  
**timeline_metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Timeline Period End Time|date|None|False|Timeline Period End Time|None|
|IP Address|string|None|False|IP Queried|None|
|Event Limit|integer|None|False|Max number of events to return|None|
|Cursor Value|string|None|False|Cursor value for additional pages of details|None|
|Timeline Period Start Time|date|None|False|Timeline Period Start Time|None|
  
**timeline_activity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ASN|string|None|False|ASN|None|
|Category|string|None|False|Category|None|
|City|string|None|False|City|None|
|GreyNoise Classification|string|None|False|GreyNoise Classification|None|
|Country|string|None|False|Country|None|
|Country Code|string|None|False|Country Code|None|
|Destinations|[]destinations|None|False|Destinations|None|
|HASSH Fingerprints|[]string|None|False|HASSH Fingerprints|None|
|HTTP Web Paths|[]string|None|False|HTTP Web Paths|None|
|HTTP User Agents|[]string|None|False|HTTP User Agents|None|
|JA3 Fingerprints|[]string|None|False|JA3 Fingerprints|None|
|Organization|string|None|False|Organization|None|
|Protocols|[]protocols|None|False|Destinations|None|
|rDNS|string|None|False|rDNS|None|
|Region|string|None|False|Region|None|
|Spoofable|boolean|None|False|Spoofable|None|
|Tags|[]tags|None|False|Tags|None|
|Event Timestamp|date|None|False|Event Timestamp|None|
|Tor Exit Node|boolean|None|False|Tor Exit Node|None|
|VPN|boolean|None|False|VPN|None|
|VPN Service|string|None|False|VPN Service|None|
  
**destinations**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Country|string|None|False|Country|None|
|Country Code|string|None|False|Country Code|None|
  
**protocols**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|App Protocol|string|None|False|App Protocol|None|
|Port|integer|None|False|Port|None|
|Transport Protocol|string|None|False|Transport Protocol|None|
  
**tags**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Tag Category|string|None|False|Tag Category|None|
|Tag Description|string|None|False|Tag Description|None|
|Tag Intention|string|None|False|Tag Intention|None|
|Tag Name|string|None|False|Tag Name|None|
  
**ip_sim**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actor|string|None|False|Actor|None|
|ASN|string|None|False|ASN|None|
|City|string|None|False|City|None|
|Classification|string|None|False|Classification|None|
|Country|string|None|False|Country|None|
|Country Code|string|None|False|Country Code|None|
|First Seen|string|None|False|First Seen|None|
|IP Address|string|None|False|IP Address|None|
|Last Seen|string|None|False|Last Seen|None|
|Organization|string|None|False|Organization|None|
  
**similar_ip**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actor|string|None|False|Actor|None|
|ASN|string|None|False|ASN|None|
|City|string|None|False|City|None|
|Classification|string|None|False|Classification|None|
|Country|string|None|False|Country|None|
|Country Code|string|None|False|Country Code|None|
|Features Matched|[]string|None|False|Features Matched|None|
|First Seen|string|None|False|First Seen|None|
|IP Address|string|None|False|IP Address|None|
|Last Seen|string|None|False|Last Seen|None|
|Organization|string|None|False|Organization|None|
|Similarity Score|float|None|False|Similarity Score|None|


## Troubleshooting

Ensure that the GreyNoise API key used has appropriate access for the actions being used.

# Version History

* 2.0.0 - Upgrade GreyNoise SDK v2.3.0, Fix Action Outputs, Add `vulnerability_lookup` action, Add `timeline_lookup` action
* 1.0.1 - Fix bug with connection parameters
* 1.0.0 - Initial plugin.

# Links

* [GreyNoise](https://greynoise.io)

## References

* [GreyNoise Documentation](https://docs.greynoise.io)
* [GreyNoise Free Trial Signup](https://viz.greynoise.io/signup)
* [GreyNoise Account Info](https://viz.greynoise.io/account)