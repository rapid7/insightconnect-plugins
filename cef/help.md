
# CEF

## About

Common Event Format (CEF) is an extensible, text-based format that defines a syntax for log records comprised of a
standard header and a variable extension, formatted as key-value pairs. It is used to promote
interoperability among various devices and apps.

## Types

### CEF

|Name|Type|Required|Description|
|----|----|--------|-----------|
|version|string|False|Version of CEF Format|
|device_vendor|string|False|With product and version, uniquely identifies the type of sending device|
|device_product|string|False|With vendor and version, uniquely identifies the type of sending device|
|device_version|string|False|With vendor and product, uniquely identifies the type of sending device|
|signature_id|string|False|Unique identifier per event-type|
|name|string|False|Represents a human-readable and understandable description of the event|
|severity|string|False|Reflects the importance of the event|
|extension|string|False|JSON object of key value pairs with keys and values as defined by the ArcSight Extension Dictionary|

## Actions

### Create String

This action is used to create a CEF string from an object.

#### Input

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef|cef|True|CEF Object|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef_string|string|True|CEF Formatted String|

### Parse String

This action is used to parse a CEF formatted string.

#### Input

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef_string|string|True|CEF Formatted String|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cef|cef|True|CEF Object|

### Parse File

This action is used to parse a multiple CEF formatted strings from a base64 encoded file.

#### Input

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|A base64 encoded file containing CEF formatted strings separated by '\n'|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cefs|[]cef|True|A list of CEF Objects|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not require a connection.

## Troubleshooting

Ensure your CEF strings are properly formatted.

## Workflows

Examples:

* Data transformation

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode

## References

* [ArcSight Common Event Format (CEF) Guide](https://www.protect724.hpe.com/docs/DOC-1072)
