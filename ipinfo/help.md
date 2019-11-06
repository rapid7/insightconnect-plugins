# Description

[IPinfo](https://ipinfo.io/) returns IP information including: hostname, ASN, organization, and GeoIP data.
The IPinfo plugin queries the IPinfo webpage via its API and returns relevant information.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

Note that the API token is not required, but daily requests are limited under the free tier.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|token|string|None|False|API Token (Empty for unauthenticated access)|None|

## Technical Details

### Actions

#### Address Lookup

This action is used to retrieve information about an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip|string|None|True|IP Address to Query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|loc|string|False|None|
|city|string|False|None|
|country|string|False|None|
|region|string|False|None|
|hostname|string|False|None|
|ip|string|False|None|
|org|string|False|None|
|postal|string|False|None|

Example output:

```

{
  "loc": "37.3860,-122.0840",
  "city": "Mountain View",
  "country": "US",
  "region": "California",
  "hostname": "google-public-dns-a.google.com",
  "phone": "650",
  "ip": "8.8.8.8",
  "org": "AS15169 Google LLC",
  "postal": "94035"
}

```

If a lookup is unsuccessful, the following message is returned:

```

{
  "error": {
    "message": "Please provide a valid IP address",
    "title": "Wrong ip"
  }
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - Convert to Python 3
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types | Rename "IPInfo" plugin title to "IPinfo" | Rename "Lookup Address" action to "Address Lookup"
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [IPinfo](https://ipinfo.io/)

