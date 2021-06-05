# Description

[Shodan](https://www.shodan.io/) is a search engine for internet-connected devices.
Using the Shodan plugin for Rapid7 InsightConnect, users can lookup hosts and run queries against their database in
real-time. Internal penetration tests and other security campaigns can be assisted and made more powerful with the
help of Shodan.

# Key Features

* Shodan database query
* Host lookup

# Requirements

* Shodan API token

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|token|credential_secret_key|None|True|API Token|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "token": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions

#### Shodan Query

This action is used to return information from a Shodan query (E.g. IPs, organizations, and total number of results).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Shodan Search Query|None|nginx country:"AU"|

Example input:

```
{
  "query": nginx country:"AU"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip_str|[]string|False|IP address as string|
|org|[]string|False|Array of organization names|
|total|integer|False|Number of results returned|

Example output:

```
{
  "ip_str": [
    "198.51.100.1",
    "198.51.100.2"
  ],
  "org": [
    "Example",
    "Example second"
  ],
  "total": 30
}
```

#### Host Information Lookup

This action is used to provide information on a given IP address, including banners for the discovered services.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip|string|None|True|Lookup Host IP for Discovered Services|None|198.51.100.1|

Example input:

```
{
  "ip": "198.51.100.1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asn|string|False|ASN|
|country_code|string|False|Code of host country|
|country_name|string|False|Name of host country|
|data|[]string|False|Banners for discovered services|
|hostnames|[]string|False|Array of hostnames|
|ip_str|string|False|IP address as string|
|org|string|False|Organization|
|os|string|False|Host OS|
|ports|[]integer|False|Ports discovered|

Example output:

```
{
  "org": "Fluency Communications Ltd",
  "ports": [
    443
  ],
  "asn": "AS5555",
  "country_code": "GB",
  "country_name": "United Kingdom",
  "data": [
    "HTTP/1.1 301 Moved Permanently\r\nContent-Type: text..."
  ],
  "hostnames": [],
  "ip_str": "198.51.100.1"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.0 - Add example inputs | Add example outputs | Update python version to `python-3-38-plugin:4` | Update Shodan version to `1.24.0` | Code refactor | Add connection test in connection.py
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Shodan](https://www.shodan.io/)

