# Description

[Proofpoint URL Defense](https://www.proofpoint.com/us) is a service designed to handle emails that contain malicious URLs.
This plugin decodes URLs that are encoded by Proofpoints URL Defense service using ppdecode.

# Key Features

* Decode a URL to its original form

# Requirements

_This plugin does not contain any requirements._

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

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Bug fix with decode parsing
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Proofpoint URL Defense](https://www.proofpoint.com/us/products/targeted-attack-protection)
* [ppdecode Library](https://github.com/warquel/ppdecode)

