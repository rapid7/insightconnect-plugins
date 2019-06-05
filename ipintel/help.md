
# IPIntel

## About

[IPIntel](https://ipintel.io/) is a free IP address lookup tool for the DFIR field.

## Actions

### Lookup Intelligence

This action is used to lookup intelligence information.
Stealth mode and GeoIP only are additional parameters that can be passed.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|geolookup|boolean|False|False|Enabling this will disable all threat intelligence lookups, and only return geolocation data for the IP addresses entered. This is much quicker, but provides no threat data.|None|
|stealth|boolean|False|False|When enabled, all external third-party API lookups are disabled. Threat lookups are local only, and geolocation data may be less accurate.|None|
|addresses|[]string|None|True|IP Addresses|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]intel|False|Intel object containing query results|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* IP enrichment

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode

## References

* [IPIntel](https://ipintel.io/)
