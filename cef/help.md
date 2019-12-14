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

_This plugin does not require a connection._

## Technical Details

### Actions

#### Create String

This action is used to create a CEF string from an object.

##### Input

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef|cef|True|CEF Object|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef_string|string|True|CEF Formatted String|

#### Parse String

This action is used to parse a CEF formatted string.

##### Input

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef_string|string|True|CEF Formatted String|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef|cef|True|CEF Object|

#### Parse File

This action is used to parse a multiple CEF formatted strings from a base64 encoded file.

##### Input

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|A base64 encoded file containing CEF formatted strings separated by '\n'|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cefs|[]cef|True|A list of CEF Objects|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Ensure your CEF strings are properly formatted.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [ArcSight Common Event Format (CEF) Guide](https://www.protect724.hpe.com/docs/DOC-1072)

