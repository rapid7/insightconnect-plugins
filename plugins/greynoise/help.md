# Description

GreyNoise helps analysts recognize events not worth their attention. Indicators in GreyNoise are likely associated with opportunistic internet scanning or common business services, not targeted threats. This context helps analysts focus on what matters most

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
*This plugin does not contain any supported product versions.*

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
|classification|string|False|GreyNoise Classification|None|
|ip|string|False|Value that was Queried|None|
|last_seen|string|False|Last Seen By GreyNoise|None|
|link|string|False|Link to GreyNoise Visualizer for IP Details|None|
|message|string|False|GreyNoise Community API Status Message|None|
|name|string|False|GreyNoise Actor or Service Name Associated with IP|None|
|noise|boolean|False|Defines if IP is Internet Noise|None|
|riot|boolean|False|Defines if IP is part of GreyNoise RIOT dataset|None|
  
Example output:

```
{
  "classification": "",
  "ip": "",
  "last_seen": "",
  "link": "",
  "message": "",
  "name": "",
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
|actor|string|False|GreyNoise Actor Associated with IP|None|
|bot|boolean|False|GreyNoise has identified this as a Bot|None|
|classification|string|False|GreyNoise Classification|None|
|cve|[]string|False|CVEs associated with GreyNoise Tags|None|
|first_seen|date|False|First Seen By GreyNoise|None|
|ip|string|False|Value that was Queried|None|
|last_seen|string|False|Last Seen By GreyNoise|None|
|metadata|metadata|False|GreyNoise IP Metadata|None|
|raw_data|raw_data|False|GreyNoise IP Raw Data|None|
|seen|boolean|False|Has this IP been Seen by GreyNoise|None|
|spoofable|boolean|False|IP address may be spoofed|None|
|tags|[]string|False|GreyNoise Tags Associated with IP|None|
|viz_url|string|False|Link to GreyNoise Visualizer for IP Details|None|
|vpn|boolean|False|GreyNoise has identified this as a VPN|None|
|vpn_service|string|False|Name of VPN Service|None|
  
Example output:

```
{
  "actor": "",
  "bot": true,
  "classification": "",
  "cve": [
    ""
  ],
  "first_seen": "",
  "ip": "",
  "last_seen": "",
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
  "spoofable": true,
  "tags": [
    ""
  ],
  "viz_url": "",
  "vpn": true,
  "vpn_service": ""
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
|category|string|False|Tag Category|None|
|cves|[]object|False|CVEs associate with Tag|None|
|description|string|False|Description of the Tag|None|
|intention|string|False|Tag Intention|None|
|name|string|False|Name of GreyNoise Tag|None|
|recommend_block|boolean|False|GreyNoise Recommends Blocking IPs associated with this Tag|None|
|references|[]object|False|References|None|
  
Example output:

```
{
  "category": "",
  "cves": [
    {}
  ],
  "description": "",
  "intention": "",
  "name": "",
  "recommend_block": true,
  "references": [
    {}
  ]
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
|complete|boolean|False|Indicates if all pages of the query have been returned by the API|None|
|count|integer|False|Total count of IPs returned Query|None|
|data|[]data|False|GreyNoise Data Object, Contains IP Object for each IP returned by the query|None|
|message|string|False|GreyNoise Query Message, indicates if there were issues with the query|None|
|query|string|False|GreyNoise Query Sent to API|None|
  
Example output:

```
{
  "complete": true,
  "count": 0,
  "data": [
    {
      "GreyNoise Actor": {},
      "GreyNoise Bot": {},
      "GreyNoise CVEs": {},
      "GreyNoise Classification": {},
      "GreyNoise First Seen": "",
      "GreyNoise Last Seen": {},
      "GreyNoise Metadata": {
        "ASN": {},
        "Category": {},
        "City": {},
        "Country": {},
        "Country Code": {},
        "Destination Countries": {},
        "Destination Country Codes": {},
        "OS": {},
        "Organization": {},
        "Region": {},
        "Sensor Count": 0,
        "Sensor Hits": {},
        "Source Country": {},
        "Source Country Code": {},
        "TOR": {},
        "rDNS": {}
      },
      "GreyNoise Raw Data": {
        "HASSH": [
          {
            "Fingerprint": {},
            "Port": {}
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
      "GreyNoise Seen": "true",
      "GreyNoise Spoofable": {},
      "GreyNoise Tags": [
        {}
      ],
      "GreyNoise VPN": {},
      "GreyNoise VPN Service": {},
      "IP Address": ""
    }
  ],
  "message": "",
  "query": ""
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
|code|string|False|Response Code from Quick API endpoint|None|
|code_message|string|False|Response Code Message from Quick API endpoint|None|
|ip|string|False|Value that was Queried|None|
|noise|boolean|False|Defines if IP is Internet Noise|None|
  
Example output:

```
{
  "code": "",
  "code_message": "",
  "ip": "",
  "noise": true
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
|category|string|False|RIOT Category IP is part of|None|
|description|string|False|Description of the IP service|None|
|explanation|string|False|Explanation for why this is likely benign|None|
|ip|string|False|Value that was Queried|None|
|last_updated|date|False|Last time this IP was updated in RIOT dataset|None|
|name|string|False|Vendor Name IP belongs to|None|
|reference|string|False|Additional reference information|None|
|riot|boolean|False|Defines if IP is part of GreyNoise RIOT dataset|None|
|trust_level|string|False|IP Trust Level information|None|
|viz_url|string|False|Link to GreyNoise Visualizer for IP Details|None|
  
Example output:

```
{
  "category": "",
  "description": "",
  "explanation": "",
  "ip": "",
  "last_updated": "",
  "name": "",
  "reference": "",
  "riot": true,
  "trust_level": "",
  "viz_url": ""
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


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History
  
*This plugin does not contain a version history.*

# Links
  
*This plugin does not contain any links.*

## References
  
*This plugin does not contain any references.*