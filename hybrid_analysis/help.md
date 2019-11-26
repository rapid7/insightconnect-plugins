# Description

[Hybrid Analysis](https://www.hybrid-analysis.com/) is a free malware analysis service powered by Payload Security that detects and analyzes unknown threats using a unique Hybrid Analysis technology. This plugin allows you to lookup file hashes to find out if they are malicious.

# Key Features

* Look up a file hash

# Requirements

* A HybridAnalysis API key and token

# Documentation

## Setup

An API key, API secret, and API URL is required.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|https://www.hybrid-analysis.com/api|False|URL|None|
|api_key|credential_secret_key|None|True|API Key|None|
|api_token|credential_secret_key|None|True|API token|None|

## Technical Details

### Actions

#### Lookup Hash

This action is used to look up a hash for malware information.

##### Input

The following hash types are supported:

* MD5
* SHA1
* SHA256

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|MD5/SHA1/SHA256 Hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|threatscore|integer|False|Threat Score (max found)|
|reports|[]report|False|Reports|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.1 - New spec and help.md format for the Hub
* 2.0.0 - Update to new secret key credential type
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Hybrid Analysis](https://www.hybrid-analysis.com/)

