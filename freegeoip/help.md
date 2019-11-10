
# FreeGeoIP

## About

[FreeGeoIP](https://freegeoip.net/) is a free service for Geo IP lookups.

## Actions

### GeoIP Lookup

This action is used to get GeoIP info for a host.

#### Input

It accepts a user to query and host (IP or domain) to perform the query.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|Host to Lookup|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|city|string|False|City|
|region_code|string|False|Region code|
|region_name|string|False|Region name|
|time_zone|string|False|Time zone|
|longitude|string|False|Longitude|
|metro_code|integer|False|Metro code|
|country_name|string|False|Country name|
|country_code|string|False|Country code|
|address|string|False|IP address|
|latitude|string|False|Latitude|
|zip_code|string|False|Zip code|

On success, the raw output will look like the following:

```

{
  "city": "Mountain View",
  "region_code": "CA",
  "region_name": "California",
  "time_zone": "America/Los_Angeles",
  "longitude": "-122.0838",
  "metro_code": 807,
  "country_name": "United States",
  "country_code": "US",
  "address": "8.8.8.8",
  "latitude": "37.386",
  "zip_code": "94035"
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

A valid domain or IP address must be provided.

## Workflows

Examples:

* IP enrichment

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode

## References

* [FreeGeoIP](https://freegeoip.net/)
