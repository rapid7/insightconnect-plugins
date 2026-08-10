# Description

Enrich and assess IPv4/IPv6 addresses and domains using the IPGeolocation.io v3 APIs: geolocation, country metadata, currency, network, company, time zone, user-agent parsing, security risk signals (VPN/proxy/Tor/threat score), ASN routing intelligence, and network abuse contacts

# Key Features

* Enrich an IP or domain with location, country metadata, currency, network, company, ASN, and time zone data
* Add optional modules to an enrichment: security, abuse, hostname, geo accuracy, DMA code, and parsed user-agent
* Score an IP for risk with VPN, proxy, residential-proxy, Tor, relay, bot, spam, and known-attacker signals
* Resolve ASN routing intelligence (peers, upstreams, downstreams, routes, WHOIS) for network investigations
* Look up the responsible abuse contact for an IP to report confirmed malicious activity
* Process large IP sets efficiently with bulk geolocation and bulk security lookups (up to 50,000 entries)
* Trim responses with the Fields and Excludes parameters to reduce payload size and processing time

# Requirements

* An IPGeolocation.io API key (free or paid). Security, abuse, domain, bulk, user-agent, hostname, geo accuracy, DMA code, and non-English lookups require a paid subscription

# Supported Product Versions

* IPGeolocation.io v3 API 2026-08-10

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|IPGeolocation.io API key used to authenticate every request|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions


#### Abuse Contact

This action is used to look up the network abuse contact for a single IPv4/IPv6 address via /v3/abuse. Paid plans only.
 1 credit

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|excludes|[]string|None|False|Remove these fields from the abuse object, in abuse.field_key form (e.g. abuse.address). The IP cannot be excluded|None|["abuse.emails"]|None|None|
|fields|[]string|None|False|Return only these fields from the abuse object, in abuse.field_key form (e.g. abuse.emails). The IP is always returned|None|["abuse.emails"]|None|None|
|ip|string|None|True|IPv4 or IPv6 address to find the responsible abuse contact for|None|91.128.103.196|None|None|
  
Example input:

```
{
  "excludes": [
    "abuse.emails"
  ],
  "fields": [
    "abuse.emails"
  ],
  "ip": "91.128.103.196"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|abuse|abuse|True|Abuse contact details for the network that owns the IP|None|
|ip|string|True|The IP address that was queried|91.128.103.196|
  
Example output:

```
{
  "abuse": {
    "Address": {},
    "Country": {},
    "Emails": [
      {}
    ],
    "Kind": {},
    "Name": {},
    "Organization": {},
    "Phone Numbers": {},
    "Route": ""
  },
  "ip": "91.128.103.196"
}
```

#### ASN Lookup

This action is used to resolve ASN routing intelligence by AS number or IP via /v3/asn (1 credit). Provide either an 
ASN or an IP

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asn|string|None|False|Autonomous System Number to look up, with or without the AS prefix (e.g. 24940 or AS24940). Ignored if an IP is provided|None|24940|None|None|
|excludes|[]string|None|False|Remove these fields from the ASN object, in asn.field_key form (e.g. asn.date_allocated). The IP cannot be excluded|None|["asn.date_allocated", "asn.allocation_status"]|None|None|
|fields|[]string|None|False|Return only these fields from the ASN object, in asn.field_key form (e.g. asn.organization). Heavier objects such as asn.peers must also be listed in Include|None|["asn.organization", "asn.country", "asn.downstreams"]|None|None|
|include|[]string|None|False|Optional heavier ASN objects to add to the response. Allowed values: peers, upstreams, downstreams, routes, whois_response. If both Include and Fields are used, only Include is applied|None|["peers", "routes"]|None|None|
|ip|string|None|False|IPv4 or IPv6 address whose ASN should be resolved. Leave both ASN and IP blank to use the orchestrator's public IP|None|49.12.0.0|None|None|
  
Example input:

```
{
  "asn": 24940,
  "excludes": [
    "asn.date_allocated",
    "asn.allocation_status"
  ],
  "fields": [
    "asn.organization",
    "asn.country",
    "asn.downstreams"
  ],
  "include": [
    "peers",
    "routes"
  ],
  "ip": "49.12.0.0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asn|asn_detail|True|ASN details and routing intelligence|None|
|ip|string|False|The queried IP. Returned only when the lookup was performed by IP|49.12.0.0|
  
Example output:

```
{
  "asn": {
    "AS Number": "",
    "ASN Name": {},
    "Allocation Status": {},
    "Country": {},
    "Date Allocated": {},
    "Domain": {},
    "Downstreams": {},
    "Number of IPv4 Routes": {},
    "Number of IPv6 Routes": {},
    "Organization": {},
    "Peers": [
      {
        "AS Number": {},
        "Country": {},
        "Description": {}
      }
    ],
    "RIR": {},
    "Routes": [
      {}
    ],
    "Type": {},
    "Upstreams": {},
    "WHOIS Response": {}
  },
  "ip": "49.12.0.0"
}
```

#### IP Geolocation

This action is used to enrich a single IPv4/IPv6 address or domain with location, country metadata, currency, network, 
company, ASN, and time zone data via /v3/ipgeo (1 credit; +2 if security is included, +1 if abuse is included)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|excludes|[]string|None|False|Remove these objects or fields from the response. Use object_key.field_key for nested fields (e.g. location.continent_code) or the object key alone for a whole object. The IP cannot be excluded, and Include takes priority over Excludes|None|["currency", "location.continent_code"]|None|None|
|fields|[]string|None|False|Return only these objects or fields. Use object_key.field_key for nested fields (e.g. location.city, security.threat_score) or the object key alone for a whole object. The IP is always returned. Fields from non-default objects must also be listed in Include|None|["location.city", "security.threat_score"]|None|None|
|include|[]string|None|False|Optional paid modules to add to the response. Allowed values: security, abuse, hostname, liveHostname, hostnameFallbackLive, geo_accuracy, dma_code, user_agent, or * for every module. When more than one hostname option is given the API applies liveHostname first, then hostname, then hostnameFallbackLive|None|["security", "abuse"]|None|None|
|ip|string|None|False|IPv4 address, IPv6 address, or domain name to enrich. Leave blank to enrich the orchestrator's public IP. Domain lookups require a paid plan|None|8.8.8.8|None|None|
|lang|string|en|False|Language for the geolocation response. Any value other than English requires a paid plan|["en", "de", "ru", "ja", "fr", "cn", "es", "cs", "it", "ko", "fa", "pt", "ar"]|en|None|None|
|user_agent|string|None|False|User-Agent string to parse and return in the user_agent object. Sent as the User-Agent request header and only used when user_agent is listed in Include. Leave blank to parse the orchestrator's own user agent|None|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36|None|None|
  
Example input:

```
{
  "excludes": [
    "currency",
    "location.continent_code"
  ],
  "fields": [
    "location.city",
    "security.threat_score"
  ],
  "include": [
    "security",
    "abuse"
  ],
  "ip": "8.8.8.8",
  "lang": "en",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|geolocation_result|True|Enrichment data for the IP or domain|None|
  
Example output:

```
{
  "result": {
    "ASN": {
      "AS Number": {},
      "Country": {},
      "Date Allocated": {},
      "Domain": {},
      "Organization": {},
      "RIR": {},
      "Type": {}
    },
    "Abuse Contact": {
      "Address": {},
      "Country": {},
      "Emails": {},
      "Kind": {},
      "Name": {},
      "Organization": {},
      "Phone Numbers": {},
      "Route": {}
    },
    "Company": {
      "Domain": {},
      "Name": {},
      "Type": {}
    },
    "Country Metadata": {
      "Calling Code": {},
      "Languages": [
        {}
      ],
      "TLD": {}
    },
    "Currency": {
      "Code": {},
      "Name": {},
      "Symbol": {}
    },
    "Domain": {},
    "Hostname": {},
    "IP": "",
    "Location": {
      "Accuracy Radius": {},
      "City": {},
      "Confidence": {},
      "Continent Code": {},
      "Continent Name": {},
      "Country Capital": {},
      "Country Code 2": {},
      "Country Code 3": {},
      "Country Emoji": {},
      "Country Flag": {},
      "Country Name": {},
      "DMA Code": {},
      "District": {},
      "GeoName ID": {},
      "Is EU": "true",
      "Latitude": {},
      "Locality": {},
      "Longitude": {},
      "Official Country Name": {},
      "State / Province": {},
      "State Code": {},
      "ZIP Code": {}
    },
    "Message": {},
    "Network": {
      "Connection Type": {},
      "Is Anycast": {},
      "Route": {}
    },
    "Security": {
      "Cloud Provider Name": {},
      "Is Anonymous": {},
      "Is Bot": {},
      "Is Cloud Provider": {},
      "Is Known Attacker": {},
      "Is Proxy": {},
      "Is Relay": {},
      "Is Residential Proxy": {},
      "Is Spam": {},
      "Is Tor": {},
      "Is VPN": {},
      "Proxy Confidence Score": {},
      "Proxy Last Seen": {},
      "Proxy Provider Names": {},
      "Relay Provider Name": {},
      "Threat Score": {},
      "VPN Confidence Score": {},
      "VPN Last Seen": {},
      "VPN Provider Names": {}
    },
    "Time Zone": {
      "Current Time": {},
      "Current Time Unix": {},
      "Current Time Zone Abbreviation": {},
      "Current Time Zone Full Name": {},
      "DST End": {},
      "DST Exists": {},
      "DST Savings": {},
      "DST Start": {
        "Date Time After": {},
        "Date Time Before": {},
        "Duration": {},
        "Gap": {},
        "Overlap": {},
        "UTC Time": {}
      },
      "DST Time Zone Abbreviation": {},
      "DST Time Zone Full Name": {},
      "Is DST": {},
      "Name": {},
      "Offset": 0,
      "Offset With DST": {},
      "Standard Time Zone Abbreviation": {},
      "Standard Time Zone Full Name": {}
    },
    "User Agent": {
      "Device": {
        "Brand": {},
        "CPU": {},
        "Name": {},
        "Type": {}
      },
      "Engine": {
        "Major Version": {},
        "Name": {},
        "Type": {},
        "Version": {}
      },
      "Major Version": {},
      "Name": {},
      "Operating System": {
        "Build": {},
        "Major Version": {},
        "Name": {},
        "Type": {},
        "Version": {}
      },
      "Type": {},
      "User Agent String": {},
      "Version": {}
    }
  }
}
```

#### IP Geolocation Bulk

This action is used to enrich up to 50,000 IPv4/IPv6 addresses or domains in one request via /v3/ipgeo-bulk. Paid plans
 only. Billed per valid entry using the same credit rules as a single lookup

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|excludes|[]string|None|False|Remove these objects or fields from each result. Use object_key.field_key for nested fields (e.g. security.threat_score). The IP cannot be excluded, and Include takes priority over Excludes|None|["security.threat_score"]|None|None|
|fields|[]string|None|False|Return only these objects or fields in each result. Use object_key.field_key for nested fields (e.g. location.city). The IP is always returned. Fields from non-default objects must also be listed in Include|None|["location.city", "currency", "security"]|None|None|
|include|[]string|None|False|Optional paid modules to add to each result. Allowed values: security, abuse, hostname, liveHostname, hostnameFallbackLive, geo_accuracy, dma_code, user_agent, or * for every module. When more than one hostname option is given the API applies liveHostname first, then hostname, then hostnameFallbackLive|None|["security"]|None|None|
|ips|[]string|None|True|IPv4 addresses, IPv6 addresses, or domain names to enrich (max 50,000)|None|["8.8.8.8", "1.1.1.1"]|None|None|
|lang|string|en|False|Language for the geolocation response|["en", "de", "ru", "ja", "fr", "cn", "es", "cs", "it", "ko", "fa", "pt", "ar"]|en|None|None|
  
Example input:

```
{
  "excludes": [
    "security.threat_score"
  ],
  "fields": [
    "location.city",
    "currency",
    "security"
  ],
  "include": [
    "security"
  ],
  "ips": [
    "8.8.8.8",
    "1.1.1.1"
  ],
  "lang": "en"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]geolocation_result|True|One result per submitted entry, in the order sent. Invalid or bogon entries contain only a message field|None|
  
Example output:

```
{
  "results": [
    {
      "ASN": {
        "AS Number": {},
        "Country": {},
        "Date Allocated": {},
        "Domain": {},
        "Organization": {},
        "RIR": {},
        "Type": {}
      },
      "Abuse Contact": {
        "Address": {},
        "Country": {},
        "Emails": {},
        "Kind": {},
        "Name": {},
        "Organization": {},
        "Phone Numbers": {},
        "Route": {}
      },
      "Company": {
        "Domain": {},
        "Name": {},
        "Type": {}
      },
      "Country Metadata": {
        "Calling Code": {},
        "Languages": [
          {}
        ],
        "TLD": {}
      },
      "Currency": {
        "Code": {},
        "Name": {},
        "Symbol": {}
      },
      "Domain": {},
      "Hostname": {},
      "IP": "",
      "Location": {
        "Accuracy Radius": {},
        "City": {},
        "Confidence": {},
        "Continent Code": {},
        "Continent Name": {},
        "Country Capital": {},
        "Country Code 2": {},
        "Country Code 3": {},
        "Country Emoji": {},
        "Country Flag": {},
        "Country Name": {},
        "DMA Code": {},
        "District": {},
        "GeoName ID": {},
        "Is EU": "true",
        "Latitude": {},
        "Locality": {},
        "Longitude": {},
        "Official Country Name": {},
        "State / Province": {},
        "State Code": {},
        "ZIP Code": {}
      },
      "Message": {},
      "Network": {
        "Connection Type": {},
        "Is Anycast": {},
        "Route": {}
      },
      "Security": {
        "Cloud Provider Name": {},
        "Is Anonymous": {},
        "Is Bot": {},
        "Is Cloud Provider": {},
        "Is Known Attacker": {},
        "Is Proxy": {},
        "Is Relay": {},
        "Is Residential Proxy": {},
        "Is Spam": {},
        "Is Tor": {},
        "Is VPN": {},
        "Proxy Confidence Score": {},
        "Proxy Last Seen": {},
        "Proxy Provider Names": {},
        "Relay Provider Name": {},
        "Threat Score": {},
        "VPN Confidence Score": {},
        "VPN Last Seen": {},
        "VPN Provider Names": {}
      },
      "Time Zone": {
        "Current Time": {},
        "Current Time Unix": {},
        "Current Time Zone Abbreviation": {},
        "Current Time Zone Full Name": {},
        "DST End": {},
        "DST Exists": {},
        "DST Savings": {},
        "DST Start": {
          "Date Time After": {},
          "Date Time Before": {},
          "Duration": {},
          "Gap": {},
          "Overlap": {},
          "UTC Time": {}
        },
        "DST Time Zone Abbreviation": {},
        "DST Time Zone Full Name": {},
        "Is DST": {},
        "Name": {},
        "Offset": 0,
        "Offset With DST": {},
        "Standard Time Zone Abbreviation": {},
        "Standard Time Zone Full Name": {}
      },
      "User Agent": {
        "Device": {
          "Brand": {},
          "CPU": {},
          "Name": {},
          "Type": {}
        },
        "Engine": {
          "Major Version": {},
          "Name": {},
          "Type": {},
          "Version": {}
        },
        "Major Version": {},
        "Name": {},
        "Operating System": {
          "Build": {},
          "Major Version": {},
          "Name": {},
          "Type": {},
          "Version": {}
        },
        "Type": {},
        "User Agent String": {},
        "Version": {}
      }
    }
  ]
}
```

#### IP Security

This action is used to assess a single IPv4/IPv6 address for risk (threat score, VPN, proxy, Tor, relay, bot, spam, 
attacker) via /v3/security. Paid plans only. 2 credits. Domains are not supported

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|excludes|[]string|None|False|Remove these fields from the security object, in security.field_key form (e.g. security.is_tor). The IP cannot be excluded|None|["security.is_tor", "security.is_cloud_provider"]|None|None|
|fields|[]string|None|False|Return only these fields from the security object, in security.field_key form (e.g. security.threat_score). The IP is always returned|None|["security.threat_score", "security.is_vpn"]|None|None|
|ip|string|None|False|IPv4 or IPv6 address to assess. Leave blank to assess the orchestrator's public IP|None|2.56.188.34|None|None|
  
Example input:

```
{
  "excludes": [
    "security.is_tor",
    "security.is_cloud_provider"
  ],
  "fields": [
    "security.threat_score",
    "security.is_vpn"
  ],
  "ip": "2.56.188.34"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ip|string|True|The IP address that was assessed|2.56.188.34|
|security|security|True|Risk and anonymization signals for the IP|None|
  
Example output:

```
{
  "ip": "2.56.188.34",
  "security": {
    "Cloud Provider Name": {},
    "Is Anonymous": {},
    "Is Bot": {},
    "Is Cloud Provider": {},
    "Is Known Attacker": {},
    "Is Proxy": {},
    "Is Relay": {},
    "Is Residential Proxy": {},
    "Is Spam": {},
    "Is Tor": "true",
    "Is VPN": {},
    "Proxy Confidence Score": {},
    "Proxy Last Seen": {},
    "Proxy Provider Names": [
      ""
    ],
    "Relay Provider Name": {},
    "Threat Score": 0,
    "VPN Confidence Score": {},
    "VPN Last Seen": {},
    "VPN Provider Names": {}
  }
}
```

#### IP Security Bulk

This action is used to assess up to 50,000 IPv4/IPv6 addresses for risk in one request via /v3/security-bulk. Paid 
plans only. Billed 2 credits per valid IP

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|excludes|[]string|None|False|Remove these fields from each security object, in security.field_key form (e.g. security.vpn_last_seen). The IP cannot be excluded|None|["security.threat_score", "security.proxy_last_seen", "security.vpn_last_seen"]|None|None|
|fields|[]string|None|False|Return only these fields from each security object, in security.field_key form (e.g. security.is_vpn). The IP is always returned|None|["security.is_vpn", "security.vpn_confidence_score", "security.is_proxy"]|None|None|
|ips|[]string|None|True|IPv4 or IPv6 addresses to assess (max 50,000). Domains are not supported|None|["2.56.188.34", "8.8.8.8"]|None|None|
  
Example input:

```
{
  "excludes": [
    "security.threat_score",
    "security.proxy_last_seen",
    "security.vpn_last_seen"
  ],
  "fields": [
    "security.is_vpn",
    "security.vpn_confidence_score",
    "security.is_proxy"
  ],
  "ips": [
    "2.56.188.34",
    "8.8.8.8"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]security_result|True|One result per submitted IP, in the order sent. Invalid or bogon entries contain only a message field|None|
  
Example output:

```
{
  "results": [
    {
      "IP": "",
      "Message": {},
      "Security": {
        "Cloud Provider Name": {},
        "Is Anonymous": {},
        "Is Bot": {},
        "Is Cloud Provider": {},
        "Is Known Attacker": {},
        "Is Proxy": {},
        "Is Relay": {},
        "Is Residential Proxy": {},
        "Is Spam": {},
        "Is Tor": "true",
        "Is VPN": {},
        "Proxy Confidence Score": {},
        "Proxy Last Seen": {},
        "Proxy Provider Names": [
          {}
        ],
        "Relay Provider Name": {},
        "Threat Score": 0,
        "VPN Confidence Score": {},
        "VPN Last Seen": {},
        "VPN Provider Names": {}
      }
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**geolocation_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Abuse Contact|abuse|None|False|Network abuse contact (returned only when abuse is included)|None|
|ASN|asn|None|False|ASN that owns the IP's network|None|
|Company|company|None|False|Company or ISP mapped to the IP|None|
|Country Metadata|country_metadata|None|False|Calling code, top-level domain, and languages for the country|None|
|Currency|currency|None|False|Currency used in the country of the IP location|None|
|Domain|string|None|False|The domain submitted, exactly as sent (returned only for domain lookups)|None|
|Hostname|string|None|False|Reverse DNS (PTR) hostname. Returned only when a hostname module is included, and falls back to the queried IP when no hostname resolves|None|
|IP|string|None|False|The IP looked up, or for a domain lookup the resolved A or AAAA record|None|
|Location|location|None|False|Geographic location of the IP|None|
|Message|string|None|False|Error message for this entry in a bulk response (e.g. bogon or invalid IP)|None|
|Network|network|None|False|Network and connection details|None|
|Security|security|None|False|Risk and anonymization signals (returned only when security is included)|None|
|Time Zone|time_zone|None|False|Time zone and daylight saving details for the IP location|None|
|User Agent|user_agent|None|False|Parsed user-agent details (returned only when user_agent is included)|None|
  
**security_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP|string|None|False|The IP address that was assessed|None|
|Message|string|None|False|Error message for this entry (e.g. bogon or invalid IP)|None|
|Security|security|None|False|Risk and anonymization signals for the IP|None|
  
**location**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Accuracy Radius|string|None|False|Estimated accuracy radius in km around the latitude and longitude (returned only when geo_accuracy is included)|None|
|City|string|None|False|City name|None|
|Confidence|string|None|False|Confidence level for the accuracy radius: low, medium, or high (returned only when geo_accuracy is included)|None|
|Continent Code|string|None|False|Two-letter continent code: AF, AN, AS, EU, NA, OC, or SA|None|
|Continent Name|string|None|False|Continent name|None|
|Country Capital|string|None|False|Capital city of the country|None|
|Country Code 2|string|None|False|ISO 3166-1 alpha-2 country code|None|
|Country Code 3|string|None|False|ISO 3166-1 alpha-3 country code|None|
|Country Emoji|string|None|False|Unicode flag emoji for the country|None|
|Country Flag|string|None|False|URL of the country flag image|None|
|Country Name|string|None|False|Common country name|None|
|Official Country Name|string|None|False|Official ISO-style country name, when it differs from the common name|None|
|District|string|None|False|District or county name, when available|None|
|DMA Code|string|None|False|US Designated Market Area code, non-empty only for US IPs (returned only when dma_code is included)|None|
|GeoName ID|string|None|False|GeoNames place identifier, when available|None|
|Is EU|boolean|None|False|Whether the country is in the European Union|None|
|Latitude|string|None|False|Latitude in decimal degrees, from -90 to 90|None|
|Locality|string|None|False|Neighborhood or suburb within the city, which may match the city (returned only when geo_accuracy is included)|None|
|Longitude|string|None|False|Longitude in decimal degrees, from -180 to 180|None|
|State Code|string|None|False|State, province, or region code, usually ISO 3166-2 or a local short code|None|
|State / Province|string|None|False|State, province, or region name|None|
|ZIP Code|string|None|False|Postal or ZIP code|None|
  
**country_metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Calling Code|string|None|False|International dialing prefix for the country|None|
|Languages|[]string|None|False|ISO 639-1 language codes commonly spoken in the country|None|
|TLD|string|None|False|Country-code top-level domain|None|
  
**currency**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|string|None|False|ISO 4217 currency code|None|
|Name|string|None|False|Currency name|None|
|Symbol|string|None|False|Currency symbol|None|
  
**network**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Connection Type|string|None|False|Connection type (e.g. DSL, Cable, Mobile, Wireless, 5G) when available|None|
|Is Anycast|boolean|None|False|Whether the IP is announced as anycast from multiple locations|None|
|Route|string|None|False|CIDR network prefix that contains the IP|None|
  
**asn**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AS Number|string|None|False|ASN identifier in AS<number> format|None|
|Country|string|None|False|ISO 3166-1 alpha-2 country of ASN registration|None|
|Date Allocated|string|None|False|Date the ASN was allocated in YYYY-MM-DD format (paid plans only)|None|
|Domain|string|None|False|Domain associated with the ASN operator (paid plans only)|None|
|Organization|string|None|False|Organization that operates the ASN|None|
|RIR|string|None|False|Regional Internet Registry: RIPE, ARIN, APNIC, LACNIC, or AFRINIC (paid plans only)|None|
|Type|string|None|False|ASN category: ISP, HOSTING, BUSINESS, EDUCATION, or GOVERNMENT (paid plans only)|None|
  
**company**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Domain|string|None|False|Company domain|None|
|Name|string|None|False|Company or ISP name|None|
|Type|string|None|False|Company category: ISP, HOSTING, BUSINESS, EDUCATION, or GOVERNMENT|None|
  
**dst_transition**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Date Time After|string|None|False|Local date and time immediately after the transition|None|
|Date Time Before|string|None|False|Local date and time immediately before the transition|None|
|Duration|string|None|False|Clock change at the transition, positive when clocks move forward (e.g. +1.00H)|None|
|Gap|boolean|None|False|Whether local time jumps forward so that some local times do not exist|None|
|Overlap|boolean|None|False|Whether local times repeat so that the same local time occurs twice|None|
|UTC Time|string|None|False|Moment of the transition in UTC|None|
  
**time_zone**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Current Time|string|None|False|Current local date and time at the IP location|None|
|Current Time Unix|number|None|False|Current local time as Unix epoch seconds|None|
|Current Time Zone Abbreviation|string|None|False|Abbreviation currently in effect (e.g. CET)|None|
|Current Time Zone Full Name|string|None|False|Full name of the time zone currently in effect|None|
|DST End|dst_transition|None|False|Details of the transition out of daylight saving time|None|
|DST Exists|boolean|None|False|Whether the time zone observes DST at any point in the year|None|
|DST Savings|number|None|False|Daylight saving shift in hours, or 0 when DST is not active|None|
|DST Start|dst_transition|None|False|Details of the transition into daylight saving time|None|
|DST Time Zone Abbreviation|string|None|False|Abbreviation used while DST is active (e.g. CEST)|None|
|DST Time Zone Full Name|string|None|False|Full time zone name used while DST is active|None|
|Is DST|boolean|None|False|Whether daylight saving time is active at the returned local time|None|
|Name|string|None|False|IANA time zone name (e.g. Europe/Stockholm)|None|
|Offset|number|None|False|Standard UTC offset in hours|None|
|Offset With DST|number|None|False|Current effective UTC offset in hours, including DST when active|None|
|Standard Time Zone Abbreviation|string|None|False|Non-DST abbreviation for the time zone|None|
|Standard Time Zone Full Name|string|None|False|Non-DST full name of the time zone|None|
  
**user_agent_device**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Brand|string|None|False|Device vendor or brand, when identified|None|
|CPU|string|None|False|CPU or architecture string, when detected|None|
|Name|string|None|False|Detected device label (e.g. Linux Desktop)|None|
|Type|string|None|False|Device category, such as Desktop, Mobile, Tablet, or Bot|None|
  
**user_agent_engine**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Rendering engine name (e.g. Blink, WebKit, Gecko)|None|
|Type|string|None|False|Engine category, typically Browser|None|
|Version|string|None|False|Full engine version string|None|
|Major Version|string|None|False|Major engine version|None|
  
**user_agent_operating_system**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Build|string|None|False|Operating system build identifier, when available|None|
|Name|string|None|False|Operating system name (e.g. Linux, Windows, Android)|None|
|Type|string|None|False|OS category, such as Desktop, Mobile, or Server|None|
|Version|string|None|False|Operating system version string|None|
|Major Version|string|None|False|Major operating system version|None|
  
**user_agent**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Device|user_agent_device|None|False|Device details parsed from the user agent|None|
|Engine|user_agent_engine|None|False|Rendering engine details parsed from the user agent|None|
|Name|string|None|False|Detected user agent product name (e.g. Chrome)|None|
|Operating System|user_agent_operating_system|None|False|Operating system details parsed from the user agent|None|
|Type|string|None|False|User agent category, such as Browser, Mobile App, Robot, or Bot|None|
|User Agent String|string|None|False|Raw User-Agent string that was parsed|None|
|Version|string|None|False|Full product version string|None|
|Major Version|string|None|False|Major product version|None|
  
**security**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Cloud Provider Name|string|None|False|Cloud or hosting provider name, when identified|None|
|Is Anonymous|boolean|None|False|Whether any anonymization signal is present (VPN, proxy, Tor, or relay)|None|
|Is Bot|boolean|None|False|Whether the IP is associated with suspicious or abusive automation. Well-known search engine crawlers are not flagged|None|
|Is Cloud Provider|boolean|None|False|Whether the IP belongs to a cloud or hosting provider|None|
|Is Known Attacker|boolean|None|False|Whether the IP is flagged in known attacker or threat feeds|None|
|Is Proxy|boolean|None|False|Whether the IP belongs to a known proxy service|None|
|Is Relay|boolean|None|False|Whether the IP is part of a relay network (e.g. iCloud Private Relay)|None|
|Is Residential Proxy|boolean|None|False|Whether the IP is a known residential proxy|None|
|Is Spam|boolean|None|False|Whether the IP is listed in spam databases|None|
|Is Tor|boolean|None|False|Whether the IP is a known Tor exit node|None|
|Is VPN|boolean|None|False|Whether the IP belongs to a known VPN provider|None|
|Proxy Confidence Score|number|None|False|Confidence from 0 to 100 that the IP is a proxy, defaulting to 0 when not detected|None|
|Proxy Last Seen|string|None|False|Date the IP was last observed as a proxy (YYYY-MM-DD)|None|
|Proxy Provider Names|[]string|None|False|Names of proxy providers associated with the IP|None|
|Relay Provider Name|string|None|False|Relay provider name, when identified|None|
|Threat Score|number|None|False|Aggregate risk score from 0 (clean) to 100 (high risk)|None|
|VPN Confidence Score|number|None|False|Confidence from 0 to 100 that the IP is a VPN endpoint, defaulting to 0 when not detected|None|
|VPN Last Seen|string|None|False|Date the IP was last observed as a VPN endpoint (YYYY-MM-DD)|None|
|VPN Provider Names|[]string|None|False|Names of VPN providers associated with the IP|None|
  
**abuse**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Address|string|None|False|Registered postal address of the network owner|None|
|Country|string|None|False|ISO 3166-1 alpha-2 country where the abuse contact is registered|None|
|Emails|[]string|None|False|Abuse contact email addresses|None|
|Kind|string|None|False|Contact type: group or individual|None|
|Name|string|None|False|Display name of the abuse contact role, team, or person|None|
|Organization|string|None|False|Organization responsible for the network|None|
|Phone Numbers|[]string|None|False|Abuse contact phone numbers|None|
|Route|string|None|False|CIDR network the abuse contact is responsible for|None|
  
**asn_relation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AS Number|string|None|False|ASN of the related autonomous system|None|
|Country|string|None|False|ISO 3166-1 alpha-2 country of the related autonomous system|None|
|Description|string|None|False|Name or description of the related autonomous system|None|
  
**asn_detail**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Allocation Status|string|None|False|Current allocation status of the ASN (e.g. ASSIGNED, ALLOCATED)|None|
|AS Number|string|None|False|ASN identifier in AS<number> format|None|
|ASN Name|string|None|False|Official ASN handle|None|
|Country|string|None|False|ISO 3166-1 alpha-2 country of ASN registration|None|
|Date Allocated|string|None|False|Date the ASN was allocated (YYYY-MM-DD)|None|
|Domain|string|None|False|Domain associated with the ASN operator|None|
|Downstreams|[]asn_relation|None|False|Downstream (customer) autonomous systems|None|
|Number of IPv4 Routes|string|None|False|Count of distinct IPv4 prefixes announced by the ASN|None|
|Number of IPv6 Routes|string|None|False|Count of distinct IPv6 prefixes announced by the ASN|None|
|Organization|string|None|False|Organization the ASN is assigned to|None|
|Peers|[]asn_relation|None|False|Directly connected peer autonomous systems|None|
|RIR|string|None|False|Regional Internet Registry: RIPE, ARIN, APNIC, LACNIC, or AFRINIC|None|
|Routes|[]string|None|False|IPv4 and IPv6 prefixes announced by the ASN|None|
|Type|string|None|False|ASN category: ISP, HOSTING, BUSINESS, EDUCATION, or GOVERNMENT|None|
|Upstreams|[]asn_relation|None|False|Upstream (provider) autonomous systems|None|
|WHOIS Response|string|None|False|Raw ASN WHOIS record text|None|


## Troubleshooting

* A 401 error usually means the requested data (security, abuse, hostname, geo_accuracy, dma_code, user_agent, bulk, domain lookup, or a non-English language) is not available on a free plan, or the API key is invalid
* A 423 (Locked) error means the IP is a private or bogon address and cannot be looked up
* A 400 error on a bulk action usually means the IP list is empty or contains more than 50,000 entries
* If a field you requested is missing, confirm it was added with the Include input first. Fields such as security, abuse, hostname, geo accuracy, DMA code, and user agent are not returned by default
* When a field appears in both Include and Excludes, Include takes priority and the field is still returned

# Version History

* 1.0.0 - Initial plugin

# Links

* [IPGeolocation.io](https://ipgeolocation.io)

## References

* [IP Location API](https://ipgeolocation.io/documentation/ip-location-api.html)
* [IP Security API](https://ipgeolocation.io/documentation/ip-security-api.html)
* [ASN API](https://ipgeolocation.io/documentation/asn-api.html)
* [IP Abuse Contact API](https://ipgeolocation.io/documentation/ip-abuse-contact-api.html)
* [Credits Usage](https://ipgeolocation.io/documentation/credits-usage.html)