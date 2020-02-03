# Description

[IPIntel](https://ipintel.io/) is a free IP address lookup tool for the DFIR field.

# Key Features

* Detect Users locations

# Requirements

* Requires an API Key from the product

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Lookup Intelligence

This action is used to lookup intelligence information.
Stealth mode and GeoIP only are additional parameters that can be passed.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|addresses|[]string|None|True|IP Addresses|None|
|geolookup|boolean|False|False|Enabling this will disable all threat intelligence lookups, and only return geolocation data for the IP addresses entered. This is much quicker, but provides no threat data|None|
|stealth|boolean|False|False|When enabled, all external third-party API lookups are disabled. Threat lookups are local only, and geolocation data may be less accurate|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]intel|False|Intel object containing query results|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [IPIntel](https://ipintel.io/)

