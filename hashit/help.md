# Description

The HashIt plugin will generate common hashes from a file or string. Supported hashes are:

* MD5
* SHA1
* SHA256
* SHA512

# Key Features

* Generate a hash from a provided Base64 encoded file input
* Generate a hash from a provided text string input

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Hash Bytes

This action is used to return the supported hashes for a file type.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|bytes|bytes|None|True|Base64 encoded file bytes to hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha256|string|False|SHA256 hash|
|sha512|string|False|SHA512 hash|
|md5|string|False|MD5 hash|
|sha1|string|False|SHA1 hash|

Example output:

```

{
  "md5": "098f6bcd4621d373cade4e832627b4f6",
  "sha1": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",
  "sha256": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "sha512": "ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff"
}

```

#### Hash String

This action is used to return the supported hashes for a string.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|foo|string|None|False|None|None|
|string|string|None|True|String of text to hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha256|string|False|SHA256 hash|
|sha512|string|False|SHA512 hash|
|md5|string|False|MD5 hash|
|sha1|string|False|SHA1 hash|

Example output:

```

{
  "md5": "098f6bcd4621d373cade4e832627b4f6",
  "sha1": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",
  "sha256": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "sha512": "ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.2 - New spec and help.md format for the Hub
* 2.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 2.0.0 - Rename "Hash a String" action to "Hash String"
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Fix failing test in string action and remove unused foo input
* 0.1.0 - Initial plugin

# Links

## References

* [Hashlib](https://docs.python.org/3.4/library/hashlib.html)

