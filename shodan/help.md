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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|token|credential_secret_key|None|True|API Token|None|

## Technical Details

### Actions

#### Shodan Query

This action is used to return information from a Shodan query (E.g. IPs, organizations, and total number of results).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Shodan Search Query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip_str|[]string|False|None|
|total|integer|False|None|
|org|[]string|False|None|

#### Host Information Lookup

This action is used to provide information on a given IP address, including banners for the discovered services.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip|string|None|True|Lookup Host IP for Discovered Services|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|os|string|False|None|
|asn|string|False|None|
|hostnames|[]string|False|None|
|country_code|string|False|None|
|ip_str|string|False|None|
|country_name|string|False|None|
|org|string|False|None|
|data|[]string|False|None|
|ports|[]integer|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Shodan](https://www.shodan.io/)

