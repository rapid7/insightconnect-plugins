# Description

GreyNoise helps analysts recognize events not worth their attention. Indicators in GreyNoise are likely associated with
opportunistic internet scanning or common business services, not targeted threats. This context helps analysts focus
on what matters most.  The GreyNoise Plugin provides users with context on an IP address around the activity
GreyNoise has observed.

More information can be found at [https://greynoise.io/why-greynoise](https://greynoise.io/why-greynoise)

# Key Features

* Perform a GreyNoise IP Context Lookup
* Perform a GreyNoise IP Quick Lookup
* Perform a GreyNoise IP RIOT (Rule it out) Lookup
* Query for additional Tag details
* Perform a GreyNoise Community IP Lookup

# Requirements

* Requires an API Key for the GreyNoise API [GreyNoise Account Details](https://viz.greynoise.io/account)
* A free trial can be created on the [GreyNoise Visualizer](https://viz.greynoise.io/signup)
* For Users with Community API Access only, a Community API key is required, and the only action supported is the Community IP Lookup.  Other actions will fail with a 401 for a Community API key.

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_secret_key|None|True|API key from GreyNoise Account|None|abcdefghijklmnopqrstuvwxyz0123456789|

Example input:

```
{
  "credentials": "abcdefghijklmnopqrstuvwxyz0123456789"
}
```

## Technical Details

### Actions

#### Context IP Lookup

This action is used to query a routable IPv4 address in the GreyNoise Context API endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|

Example input:

```
{
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|actor|string|False|GreyNoise Actor Associated with IP|
|bot|boolean|False|GreyNoise has identified this as a Bot|
|classification|string|False|GreyNoise Classification|
|cve|[]string|False|CVEs associated with GreyNoise Tags|
|first_seen|date|False|First Seen By GreyNoise|
|ip|string|False|Value that was Queried|
|last_seen|string|False|Last Seen By GreyNoise|
|metadata|metadata|False|GreyNoise IP Metadata|
|raw_data|raw_data|False|GreyNoise IP Raw Data|
|seen|boolean|False|Has this IP been Seen by GreyNoise|
|spoofable|boolean|False|IP address may be spoofed|
|tags|[]string|False|GreyNoise Tags Associated with IP|
|viz_url|string|False|Link to GreyNoise Visualizer for IP Details|
|vpn|boolean|False|GreyNoise has identified this as a VPN|
|vpn_service|string|False|Name of VPN Service|

Example output:

```
{
  "ip": "190.79.85.166",
  "first_seen": "2021-03-27T00:00:00+00:00",
  "last_seen": "2021-04-14T00:00:00+00:00",
  "seen": true,
  "tags": ["Eternalblue"],
  "actor": "unknown",
  "spoofable": false,
  "classification": "malicious",
  "cve": ["CVE-2017-0144"],
  "bot": false,
  "vpn": false,
  "vpn_service": "",
  "metadata": {
    "asn": "AS8048",
    "city": "Caracas",
    "country": "Venezuela",
    "country_code": "VE",
    "organization": "CANTV Servicios, Venezuela",
    "category": "isp",
    "tor": false,
    "rdns": "190-79-85-166.dyn.dsl.cantv.net",
    "os": "Windows 7/8",
    "region": "Distrito Federal"
    },
  "raw_data": {
    "scan": [{
      "port": 445,
      "protocol": "TCP"
      }],
    "web": {},
    "ja3": [],
    "hassh": []
  }
}
```

#### Quick IP Lookup

This action is used to query a routable IPv4 address in the GreyNoise Quick API endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|

Example input:

```
{
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|code|string|False|Response Code from Quick API endpoint|
|code_message|string|False|Response Code Message from Quick API endpoint|
|ip|string|False|Value that was Queried|
|noise|boolean|False|Defines if IP is Internet Noise|

Example output:

```
{
  "ip": "1.1.1.1",
  "noise": false,
  "code": "0x00",
  "code_message": "IP has never been observed scanning the Internet"
}
```

#### RIOT IP Lookup

This action is used to query a routable IPv4 address in the GreyNoise RIOT API endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|

Example input:

```
{
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|category|string|False|RIOT Category IP is part of|
|description|string|False|Description of the IP service|
|explanation|string|False|Explanation for why this is likely benign|
|ip|string|False|Value that was Queried|
|last_updated|date|False|Last time this IP was updated in RIOT dataset|
|name|string|False|Vendor Name IP belongs to|
|reference|string|False|Additional reference information|
|riot|boolean|False|Defines if IP is part of GreyNoise RIOT dataset|
|viz_url|string|False|Link to GreyNoise Visualizer for IP Details|

Example output:

```
{
  "ip": "8.8.8.8",
  "riot": true,
  "category": "public_dns",
  "name": "Google Public DNS",
  "description": "Google's global domain name system (DNS) resolution service.",
  "explanation": "Public DNS services are used as alternatives to ISP's name servers. You may see devices on your
    network communicating with Google Public DNS over port 53/TCP or 53/UDP to resolve DNS lookups.",
  "last_updated": "2021-04-20T13:55:41Z",
  "reference": "https://developers.google.com/speed/public-dns/docs/isp#alternative",
  "viz_url": "https://viz.greynoise.io/riot/8.8.8.8"}
}
```

#### Get Tag Details

This action is used to get Details of a GreyNoise Tag.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|tag_name|string|None|True|Tag Name to get additional Details From|None|BingBot|

Example input:

```
{
  "tag_name": "BingBot"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|category|string|False|Tag Category|
|cves|[]object|False|CVEs associate with Tag|
|description|string|False|Description of the Tag|
|intention|string|False|Tag Intention|
|name|string|False|Name of GreyNoise Tag|
|recommend_block|boolean|False|GreyNoise Recommends Blocking IPs associated with this Tag|
|references|[]object|False|References|

Example output:

```
{
  "name": "BingBot",
  "category": "search_engine",
  "intention": "benign",
  "description": "This IP address belongs to Bing, Microsoft's search engine. It is used to crawl web servers around
    the Internet and index content for search.",
  "references": [],
  "recommend_block": false,
  "cves": []
}
```

#### Community IP Lookup

This action is used to query a routable IPv4 address in the GreyNoise Community API.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|Routable IPv4 address to query|None|1.2.3.4|

Example input:

```
{
  "ip_address": "1.2.3.4"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|classification|string|False|GreyNoise Classification|
|ip|string|False|Value that was Queried|
|last_seen|string|False|Last Seen By GreyNoise|
|link|string|False|Link to GreyNoise Visualizer for IP Details|
|message|string|False|GreyNoise Community API Status Message|
|name|string|False|GreyNoise Actor or Service Name Associated with IP|
|noise|boolean|False|Defines if IP is Internet Noise|
|riot|boolean|False|Defines if IP is part of GreyNoise RIOT dataset|

Example output:

```
{
  "classification": "benign",
  "ip": "1.1.1.1",
  "last_seen": "2021-04-20T00:00:00+00:00",
  "link": "https://viz.greynoise.io/riot/1.1.1.1",
  "message": "Success",
  "name": "Cloudflare Public DNS",
  "noise": false,
  "riot": true
}
```

#### GreyNoise Query

This action is used to perform a GreyNoise GNQL Query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Query in GreyNoise Query Language (GNQL) Syntax|None|last_seen:1d|
|size|string|10|False|Max Number of IPs to Return Data For|None|10|

Example input:

```
{
  "query": "last_seen:1d",
  "size": "10"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|complete|boolean|False|GreyNoise Query Completed|
|count|integer|False|Count of IPs In Query|
|data|[]data|False|GreyNoise Query Data|
|message|string|False|GreyNoise Query Message|
|query|string|False|GreyNoise Query Sent to API|

Example output:

```
{
  "complete": false,
  "count": 318201,
  "data": [
    {
      "ip": "117.239.128.2",
      "metadata": {
        "asn": "AS9829",
        "city": "Hyderabad",
        "country": "India",
        "country_code": "IN",
        "organization": "National Internet Backbone",
        "category": "isp",
        "tor": false,
        "rdns": "",
        "os": "Windows 7/8",
        "region": "Telangana"
      },
      "bot": false,
      "vpn": false,
      "vpn_service": "",
      "spoofable": false,
      "raw_data": {
        "scan": [
          {
            "port": 445,
            "protocol": "TCP"
          }
        ],
        "web": {},
        "ja3": [],
        "hassh": []
      },
      "first_seen": "2021-04-07",
      "last_seen": "2021-04-20",
      "rdns": "",
      "seen": true,
      "tags": [
        "Eternalblue",
        "SMBv1 Crawler"
      ],
      "actor": "unknown",
      "classification": "malicious",
      "cve": [
        "CVE-2017-0144"
      ]
    }
  ],
  "message": "ok",
  "query": "last_seen:1d"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

### Response 401

If the actions are returning a 401, ensure that the API key provided is valid and has an appropriate subscription or
trial associated with it.

### Response 429

If the actions are returning a 429, check your daily rate-limit quota, as the API indicates the daily limit has been
reached or exceeded.

### Community API Keys

For users with Community API Keys or Enterprise Trial Keys that have expired, the Community IP Lookup is the only
action that will continue to function.  All other actions will return an 401.  This is expected behavior.

### Other Issues

For any other API or plugin related issues, feel free to reach out to [GreyNoise Support](mailto:support@greynoise.io)
or reference the [GreyNoise Developer Documentation](https://developer.greynoise.io)

# Version History

* 1.0.1 - Fix bug with connection parameters
* 1.0.0 - Initial plugin

# Links

## References

* [GreyNoise](https://greynoise.io)
* [GreyNoise Developer Docs](https://developer.greynoise.io)
* [GreyNoise Free Trial Signup](https://viz.greynoise.io/signup)
* [GreyNoise Account Info](https://viz.greynoise.io/account)
