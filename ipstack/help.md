# Description

[IPStack](https://ipstack.com) is a free service for Geo IP lookups (previously FreeGeoIP).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cred_token|credential_token|None|True|API Token|None|

## Technical Details

### Actions

#### GeoIP Lookup

This action is used to lookup IPStack information for a host.

##### Input

It accepts a user to query and host (IP or domain) to perform the query.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|False|Host to Lookup|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|city|string|False|None|
|region_code|string|False|None|
|region_name|string|False|None|
|time_zone|string|False|None|
|longitude|string|False|None|
|metro_code|integer|False|None|
|country_name|string|False|None|
|country_code|string|False|None|
|address|string|False|None|
|latitude|string|False|None|
|zip_code|string|False|None|

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

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

A valid domain or IP address must be provided.

# Version History

* 1.0.0 - Support web server mode
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [IPStack](https://ipstack.com)

