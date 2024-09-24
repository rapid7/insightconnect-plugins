# Description

IPStack (https://ipstack.com) offers one of the leading IP to geolocation APIs and global IP database services worldwide. This plugin uses the [ipstack API](https://ipstack.com/documentation) to get geolocation data for a provided IP address

# Key Features

* Lookup a host in IPStack's global database to geolocate an IP address or domain

# Requirements

* API Key from the product

# Supported Product Versions

* 2021-11-30T18:50:40Z

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cred_token|credential_secret_key|None|True|API Token|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|

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

This action is used to lookup IPStack Information for a Host

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|host|string|None|True|Host to Lookup|None|example.com|None|None|
  
Example input:

```
{
  "host": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address|string|False|IP address|8.8.8.8|
|city|string|False|City|Mountain View|
|country_code|string|False|Country code|US|
|country_name|string|False|Country name|United States|
|latitude|string|False|Latitude|37.386|
|longitude|string|False|Longitude|-122.0838|
|region_code|string|False|Region code|CA|
|region_name|string|False|Region name|California|
|time_zone|time_zone|False|Time zone information at IP location|America/Los_Angeles|
|zip_code|string|False|ZIP code for current IP lookup|94035|
  
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
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**time_zone**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|string|None|False|Universal code of the given time zone https://www.timeanddate.com/time/zones/|EDT|
|Current Time|string|None|False|Current time in this timezone at time of request|2018-03-30T07:54:25-04:00|
|GMT Offset|integer|None|False|Greenwich Mean Time offset in seconds|-14400|
|ID|string|None|False|Time zone identifier|America/New_York|
|Daylight Savings|boolean|None|False|Indicator for if this timezone is currently in daylight savings|True|


## Troubleshooting

A valid domain or IP address must be provided.

# Version History

* 3.0.2 - Connection Test Fixed | SDK and Plugin Refresh
* 3.0.1 - Cloud Enabled | Updated connection test
* 3.0.0 - Updated time_zone field type to match current API version
* 2.0.0 - Add example inputs | Updated Docker version | Connection input updated to secretKey
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode
* 0.1.0 - Initial plugin

# Links

* [IPStack](https://ipstack.com/)

## References

* [IPStack](https://ipstack.com)