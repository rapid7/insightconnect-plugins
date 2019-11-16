# Description

[Tab Separated Value](https://en.wikipedia.org/wiki/Tab-separated_values) (TSV) is a common format to express data.
This plugin allows one to extract fields from TSV strings and files.

# Key Features

* Extract fields

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Filter Bytes

This action is used to extract fields from a user supplied TSV file expressed a base64 encoded data (bytes) and return a new TSV `bytes`
file with the extracted fields only. Field numbers (e.g. `f1`) and a range of fields (e.g. `f5-7`) are used to defined the extraction.
For example, to extract fields 1, 2, 4, 5, 6 the following fields value can be used: `f1, f2, f4-6`.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tsv|string|None|False|Base64 encoded TSV file|None|
|fields|bytes|None|False|Fields to filter E.g. f1, f2, f3-f6|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filtered|bytes|False|Filtered TSV file|

#### Filter String

This action is used to extract fields from a user supplied TSV string and return a new TSV string with the extracted fields only.
Field numbers (e.g. `f1`) and a range of fields (e.g. `f5-7`) are used to defined the extraction. For example, to extract fields
1, 2, 4, 5, 6 the following fields value can be used: `f1, f2, f4-6`.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tsv|string|None|False|TSV string|None|
|fields|string|None|False|Fields to filter E.g. f1, f2, f3-f6|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filtered|bytes|False|Filtered TSV string|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Ensure that the supplied file or string is valid TSV. Any TSV files containing double-quotes will need to have them triple escaped to work properly.
TSV files must not have non-TSV data such as comments.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [TSV](https://en.wikipedia.org/wiki/Tab-separated_values)

