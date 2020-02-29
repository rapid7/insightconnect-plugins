# Description

The `freegeoip` InsightConnect plugin lookup GeoIP information for specified host using [FreeGeoIP](https://freegeoip.net/) which is a free service for Geo IP lookups.

# Key Features

* Obtain GeoIP information for an IP address.

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_secret_key|None|True|Unique authentication key used to gain access to the ipstack API|None|

## Technical Details

### Actions

#### GeoIP Host Lookup

This action is used to get GeoIP Info for a Hosts.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hosts|[]string|None|True|Hosts to lookup|None|
|language|string|None|False|Response language, default EN|['en', 'de', 'es', 'fr', 'ja', 'pt-br', 'ru', 'zh']|
|should_return_hostname|boolean|None|False|Information about the hostname the given IP address resolves to|None|
|should_use_security|boolean|None|False|Should access the ipstack API's Security Module|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|information|information|True|Informations about requested IP|

Example output:

```
{
  'ip': '192.30.253.113',
  'type': 'ipv4',
  'continent_code': 'NA',
  'continent_name': 'North America',
  'country_code': 'US',
  'country_name': 'United States',
  'region_code': 'CA',
  'region_name': 'California',
  'city': 'San Francisco',
  'zip': '94107',
  'latitude': 37.76784896850586,
  'longitude': -122.39286041259766,
  'location': {
    'geoname_id': 5391959,
    'capital': 'Washington D.C.',
    'languages': [
      {
        'code': 'en',
        'name': 'English',
        'native': 'English'
      }
    ],
    'country_flag': 'http://assets.ipstack.com/flags/us.svg',
    'country_flag_emoji': '🇺🇸',
    'country_flag_emoji_unicode': 'U+1F1FA U+1F1F8',
    'calling_code': '1',
    'is_eu': False
  }
}
```

#### GeoIP Lookup

This action is used to get GeoIP info for a host.

##### Input

It accepts a user to query and host (IP or domain) to perform the query.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|language|string|None|False|Response language, default EN|['en', 'de', 'es', 'fr', 'ja', 'pt-br', 'ru', 'zh']|
|should_return_hostname|boolean|None|False|Information about the hostname the given IP address resolves to|None|
|should_use_security|boolean|None|False|Should access the ipstack API's Security Module|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|information|information|True|Informations about requested IP|

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

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

A valid domain or IP address must be provided.

# Version History

* 2.0.0 - `Freegeoip` is shutdown. Changed to `ipstack.com`
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [FreeGeoIP](https://freegeoip.net/)

