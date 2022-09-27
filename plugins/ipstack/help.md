# Description

[IPStack](https://ipstack.com) offers one of the leading IP to geolocation APIs and global IP database services worldwide. This plugin uses the [ipstack API](https://ipstack.com/documentation) to get geolocation data for a provided IP address.


# Key Features

* Lookup a host in IPStack's global database to geolocate an IP address or domain

# Requirements

* API Key from the product

# Supported Product Versions

* 2021-11-30T18:50:40Z

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cred_token|credential_secret_key|None|True|API Token|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "cred_token": {
    "secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"
  }
}

```

## Technical Details

### Actions

#### GeoIP Lookup

This action is used to lookup IPStack information for a host.

##### Input

It accepts a user to query and host (IP or domain) to perform the query.

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|host|string|None|True|Host to Lookup|None|example.com|

Example input:

```
{
  "host": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address|string|False|IP address|
|city|string|False|City|
|country_code|string|False|Country code|
|country_name|string|False|Country name|
|latitude|string|False|Latitude|
|longitude|string|False|Longitude|
|region_code|string|False|Region code|
|region_name|string|False|Region name|
|time_zone|time_zone|False|Time zone information at IP location|
|zip_code|string|False|ZIP code for current IP lookup|

Example output:

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

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

A valid domain or IP address must be provided.

# Version History

* 3.0.1 - Cloud Enabled | Updated connection test
* 3.0.0 - Updated time_zone field type to match current API version
* 2.0.0 - Add example inputs | Updated Docker version | Connection input updated to secretKey
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode
* 0.1.0 - Initial plugin

# Links

## References

* [IPStack](https://ipstack.com)
