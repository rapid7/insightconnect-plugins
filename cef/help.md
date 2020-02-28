# Description

Common Event Format (CEF) is an extensible, text-based format that defines a syntax for log records comprised of a standard header and a variable extension, formatted as key-value pairs. It is used to promote
interoperability among various devices and apps. This plugin is used for generating and manipulating event in a Common Event Format (CEF).

# Key Features

* Generate events in CEF
* Manipulate events in CEF

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Create String

This action is used to create a CEF string from an object.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cef|cef|None|True|CEF Data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef_string|string|False|CEF formatted string|

#### Parse String

This action is used to parse a CEF formatted string.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cef_string|string|None|True|CEF formatted string|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef|cef|False|CEF object|

#### Parse File

This action is used to parse a multiple CEF formatted strings from a base64 encoded file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|True|Parse multiple CEF formatted strings from a file|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cefs|[]cef|False|A list of CEF objects parsed from the file|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Ensure your CEF strings are properly formatted.

# Version History

* 2.0.0 - Changed `ValueError` to `PluginException` | Use input and output constants | Added "f" strings | Move test from action to connection | Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-slim-plugin:3`
* 1.0.1 - New spec and help.md format for the Hub | Add missing title values for actions in plugin.spec.yaml
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [ArcSight Common Event Format (CEF) Whitepaper](https://kc.mcafee.com/resources/sites/MCAFEE/content/live/CORP_KNOWLEDGEBASE/78000/KB78712/en_US/CEF_White_Paper_20100722.pdf)
