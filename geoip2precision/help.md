
# GeoIP2 Precision

## About

[MaxMind GeoIP2 Precision](https://www.maxmind.com/en/geoip2-precision-services) provides IP intelligence data.

The GeoIP2 Precision plugin queries the MaxMind Insights service via its API and returns relevant data on the provided IP.

## Actions

### Lookup

This action is used to lookup IP address information.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IP address to query|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|city|string|False|City associated with IP|
|domain|string|False|Domain associated with IP|
|country|string|False|Country of location|
|time_zone|string|False|Time zone for location|
|longitude|string|False|Longitude for location|
|registered_country|string|False|Country of IP registration|
|state|string|False|State associated with IP|
|address|string|False|IP address queried|
|latitude|string|False|Latitude for location|
|org|string|False|Organization associated with ASN|
|postal|integer|False|Postal Code for location|
|asn|integer|False|Autonomous system number|

## Triggers

This plugin does not contain any triggers.

## Connection

A MaxMind Precision user ID and license key is needed.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|integer|None|True|User ID number|None|
|license_key|credential_secret_key|None|True|License key|None|

## Troubleshooting

A valid IP address must be provided.

## Workflows

Examples:

* IP enrichment
* Location services

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types

## References

* [GeoIP Precision](https://www.maxmind.com/en/geoip2-precision-services)
