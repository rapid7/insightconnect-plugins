
# Hybrid Analysis

## About

[Hybrid Analysis](https://www.hybrid-analysis.com/) is a free malware analysis service powered by Payload Security that detects and analyzes unknown threats using a unique Hybrid Analysis technology.

## Actions

### Lookup Hash

This action is used to look up a hash for malware information.

#### Input

The following hash types are supported:

* MD5
* SHA1
* SHA256

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|MD5/SHA1/SHA256 Hash|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|threatscore|integer|False|Threat Score (max found)|
|reports|[]report|False|Reports|

## Triggers

This plugin does not contain any triggers.

## Connection

An API key, API secret, and API URL is required.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|https://www.hybrid-analysis.com/api|False|URL|None|
|api_key|credential_secret_key|None|True|API Key|None|
|api_token|credential_secret_key|None|True|API token|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Malware analysis

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 2.0.0 - Update to new secret key credential type

## References

* [Hybrid Analysis](https://www.hybrid-analysis.com/)
