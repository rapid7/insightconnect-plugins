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
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2025-02-25

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Hash Bytes

This action is used to generate hashes from file bytes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|bytes|bytes|None|True|Base64 encoded file bytes to hash|None|aGVsbG8gd29ybGQ=|None|None|
  
Example input:

```
{
  "bytes": "aGVsbG8gd29ybGQ="
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|md5|string|False|MD5 hash|098f6bcd4621d373cade4e832627b4f6|
|sha1|string|False|SHA1 hash|a94a8fe5ccb19ba61c4c0873d391e987982fbbd3|
|sha256|string|False|SHA256 hash|9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08|
|sha512|string|False|SHA512 hash|ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff|
  
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

This action is used to generate hashes from text

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|string|string|None|True|String of text to hash|None|hello world|None|None|
  
Example input:

```
{
  "string": "hello world"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|md5|string|False|MD5 hash|098f6bcd4621d373cade4e832627b4f6|
|sha1|string|False|SHA1 hash|a94a8fe5ccb19ba61c4c0873d391e987982fbbd3|
|sha256|string|False|SHA256 hash|9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08|
|sha512|string|False|SHA512 hash|ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff|
  
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
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.6 - Updated SDK to the latest version (6.2.5)
* 2.0.5 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 2.0.4 - Update to v4 Python plugin runtime
* 2.0.3 - Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Use input and output constants | Remove test from actions
* 2.0.2 - New spec and help.md format for the Extension Library
* 2.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 2.0.0 - Rename "Hash a String" action to "Hash String"
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Fix failing test in string action and remove unused foo input
* 0.1.0 - Initial plugin

# Links

* [Hashlib](https://docs.python.org/3.4/library/hashlib.html)

## References

* [Hashlib](https://docs.python.org/3.4/library/hashlib.html)