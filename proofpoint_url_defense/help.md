# Description

[Proofpoint URL Defense](https://www.proofpoint.com/us) is a service designed to handle emails that contain malicious URLs.
This plugin decodes URLs that are encoded by Proofpoints URL Defense service using ppdecode.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### URL Decode

This action is used to take a proofpoint url and decodes to the original url.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|proofpoint_url|string|None|True|Proofpoint encoded URL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decoded_url|string|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Bug fix with decode parsing
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Proofpoint URL Defense](https://www.proofpoint.com/us/products/targeted-attack-protection)
* [ppdecode Library](https://github.com/warquel/ppdecode)

