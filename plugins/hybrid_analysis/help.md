# Description

[Hybrid Analysis](https://www.hybrid-analysis.com/) is a free malware analysis service powered by Payload Security that detects and analyzes unknown threats using a unique Hybrid Analysis technology. This plugin provides the ability to lookup file hashes to determine whether or not they are malicious.

# Key Features

* Lookup a file hash to identify known and unknown threats using Hybrid Analysis technology

# Requirements

* A HybridAnalysis API key and token

# Supported Product Versions

* Hybrid Analysis API v1

# Documentation

## Setup

An API key, API secret, and API URL is required.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API Key|None|30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050|
|api_token|credential_secret_key|None|True|API token|None|02699626f388ed830012e5b787640e71c56d42d8abababab|
|url|string|https://www.hybrid-analysis.com/api|True|URL|None|https://www.hybrid-analysis.com/api|

Example input:

```
{
  "api_key": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "api_token": "3395856ce81f2b7382dee72602f798b642f14140abababab",
  "url": "https://www.hybrid-analysis.com/api"
}
```

## Technical Details

### Actions

#### Lookup Hash

This action is used to look up a hash for malware information.

##### Input

The following hash types are supported:

* MD5
* SHA1
* SHA256

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|MD5/SHA1/SHA256 Hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|

Example input:

```
{
  "hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|reports|[]report|False|Reports|
|threatscore|integer|False|Threat Score (max found)|

Example output:

```
{
  "found": false,
  "reports": [],
  "threatscore": 0
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.2 - Fix threatscore KeyError
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Update to new secret key credential type
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Hybrid Analysis](https://www.hybrid-analysis.com/)

