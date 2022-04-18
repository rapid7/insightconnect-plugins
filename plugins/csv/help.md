# Description

[Comma Separated Value](https://en.wikipedia.org/wiki/Comma-separated_values) (CSV) is a common format to express data.
This plugin allows one to extract fields from CSV strings and files.

Using the CSV plugin, users can automate conversions between JSON and CSV to help enable service interoperability
as well as filter data within a CSV file.

# Key Features

* Convert between JSON and CSV
* Filter strings

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### JSON to CSV String

This action is used to convert a JSON array to CSV string.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|json|[]object|None|True|JSON array to convert to CSV string|None|[{"column1": "value1","column2": "value2","column3": "value3"},{"column1": "value4","column2": "value5","column3": "value6"}]|

Example input:

```
{
  "json": [
    {
      "column1": "value1",
      "column2": "value2",
      "column3": "value3"
    },
    {
      "column1": "value4",
      "column2": "value5",
      "column3": "value6"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|csv_string|string|True|Resulting CSV string from the conversion|

Example output:

```
{
  "csv": "column1,column2,column3\r\nvalue1,value2,value3\r\nvalue4,value5,value6\r\n"
}
```

#### JSON to CSV Bytes

This action is used to convert a JSON array to CSV bytes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|json|[]object|None|True|JSON array to convert to CSV bytes|None|[{"column1": "value1","column2": "value2","column3": "value3"},{"column1": "value4","column2": "value5","column3": "value6"}]|

Example input:

```
{
  "json": [
    {
      "column1": "value1",
      "column2": "value2",
      "column3": "value3"
    },
    {
      "column1": "value4",
      "column2": "value5",
      "column3": "value6"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|csv_bytes|bytes|True|Resulting CSV file from the conversion|

Example output:

```
{
  "csv": "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFs\ndWU1LHZhbHVlNg0K\n"
}
```

#### Filter Bytes

This action is used to extract fields from a user supplied CSV file expressed a base64 encoded data (bytes) and return a new CSV file
with the extracted fields only.

##### Input

Field numbers (e.g. `f1`) and a range of fields (e.g. `f5-7`) are used to defined the extraction.
For example, to extract fields 1, 2, 4, 5, 6 the following fields value can be used: `f1, f2, f4-6`.

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|csv|bytes|None|True|Base64 encoded CSV file|None|ZmllbGQxLCBmaWVsZDIKdmFsdWUxLCB2YWx1ZTIK|
|fields|string|None|True|Fields to filter|None|f1, f2, f3-f6|

Example input:

```
{
  "csv": "ZmllbGQxLCBmaWVsZDIKdmFsdWUxLCB2YWx1ZTIK",
  "fields": "f1, f2, f3-f6"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filtered|bytes|True|Filtered CSV file|

Example output:

```
{
  "filtered": "ZmllbGQxLCBmaWVsZDIKdmFsdWUxLCB2YWx1ZTI="
}
```

#### Filter String

This action is used to extract fields from a user supplied CSV string and return a new CSV string with the extracted fields only.

##### Input

Field numbers (e.g. `f1`) and a range of fields (e.g. `f5-7`) are used to defined the extraction. For example, to extract fields
1, 2, 4, 5, 6 the following fields value can be used: `f1, f2, f4-6`.

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|csv|string|None|True|CSV string|None|column1, column2\nvalue1, value2|
|fields|string|None|True|Fields to filter|None|f1, f2, f3-f6|

Example input:

```
{
  "csv": "column1, column2\\nvalue1, value2",
  "fields": "f1, f2, f3-f6"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|string|string|True|Filtered CSV string|

Example output:

```
{
  "string": "field1\nvalue1\nvalue1-1"
}
```

#### To JSON

This action is used to convert CSV to JSON.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|csv|bytes|None|True|Base64 encoded CSV file|None|ZmllbGQxLCBmaWVsZDIKdmFsdWUxLCB2YWx1ZTIK|
|validation|boolean|False|True|Validate CSV data, error if not valid|None|True|

Example input:

```
{
  "csv": "ZmllbGQxLCBmaWVsZDIKdmFsdWUxLCB2YWx1ZTIK",
  "validation": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|json|[]object|True|List of objects|

Example output:

```

{
  "json": [
    {
      "Asset OS Family": "Microsoft Windows",
      "Asset OS Name": "Microsoft Windows 7 Enterprise Edition",
      "Asset OS Version": "SP1",
      "Asset IP Address": "192.168.1.2"
    },
    {
      "Asset OS Family": "Microsoft Windows",
      "Asset OS Name": "Microsoft Windows Server 2012",
      "Asset OS Version": "SP2",
      "Asset IP Address": "192.168.1.3"
    }
  ]
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Ensure that the supplied file or string is valid CSV. Any CSV files containing double-quotes will need to have them triple escaped to work properly.
CSV files must not have non-CSV data such as comments.

# Version History

* 2.0.1 - Fix bug with extra space character in JSON keys in `To JSON` action | Fix bugs with parsing cells with quotes and comma in `To JSON`, `Filter Bytes` and `Filter String` actions | Add unit tests for `To JSON`, `Filter Bytes` and `Filter String` actions
* 2.0.0 - Add JSON to CSV String action | Rename JSON to CSV action to JSON to CSV Bytes
* 1.1.6 - Update to v4 Python plugin runtime
* 1.1.5 - Use input and output constants | Change docker image from `komand/python-2-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Changed `Exception` to `PluginException`
* 1.1.4 - New spec and help.md format for the Extension Library | Add missing title values for actions in plugin.spec.yaml
* 1.1.3 - Fix issue where connection tests were failing, output did not match spec
* 1.1.2 - Support webserver mode
* 1.1.1 - Fix JSON to CSV action to account for correct input type
* 1.1.0 - Add JSON to CSV action
* 1.0.0 - Add CSV to JSON action | Support web server mode
* 0.1.2 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)

