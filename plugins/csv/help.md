# Description

[Comma Separated Value](https://en.wikipedia.org/wiki/Comma-separated_values) (CSV) is a common format to express data.
This plugin allows one to extract fields from CSV strings and files.

Using the CSV plugin, users can automate conversions between JSON and CSV to help enable service interoperability
as well as filter data within a CSV file

# Key Features

* Convert between JSON and CSV
* Filter strings

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2025-02-25

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Filter Bytes

This action is used to keep fields from base64 CSV file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|csv|bytes|None|True|Base64 encoded CSV file|None|ZmllbGQxLCBmaWVsZDIKdmFsdWUxLCB2YWx1ZTIK|None|None|
|fields|string|None|True|Fields to filter|None|f1, f2|None|None|
  
Example input:

```
{
  "csv": "ZmllbGQxLCBmaWVsZDIKdmFsdWUxLCB2YWx1ZTIK",
  "fields": "f1, f2"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|filtered|bytes|True|Filtered CSV file|ZmllbGQxLGZpZWxkMgp2YWx1ZTEsdmFsdWUy|
  
Example output:

```
{
  "filtered": "ZmllbGQxLGZpZWxkMgp2YWx1ZTEsdmFsdWUy"
}
```

#### Filter String

This action is used to keep fields from CSV string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|csv|string|None|True|CSV string|None|column1, column2, column3\nvalue1, value2, value3|None|None|
|fields|string|None|True|Fields to filter|None|f1, f2-f3|None|None|
  
Example input:

```
{
  "csv": "column1, column2, column3\\nvalue1, value2, value3",
  "fields": "f1, f2-f3"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|string|string|True|Filtered CSV string|column1,column2,column3\nvalue1|
  
Example output:

```
{
  "string": "column1,column2,column3\\nvalue1"
}
```

#### JSON to CSV Bytes

This action is used to convert a JSON array to CSV bytes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|json|[]object|None|True|JSON array to convert to CSV bytes|None|[{"column1": "value1","column2": "value2","column3": "value3"},{"column1": "value4","column2": "value5","column3": "value6"}]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|csv_bytes|bytes|True|Resulting CSV file from the conversion|Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFs\ndWU1LHZhbHVlNg0K\n|
  
Example output:

```
{
  "csv_bytes": "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFs\\ndWU1LHZhbHVlNg0K\\n"
}
```

#### JSON to CSV String

This action is used to convert a JSON array to CSV string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|json|[]object|None|True|JSON array to convert to CSV string|None|[{"column1": "value1","column2": "value2","column3": "value3"},{"column1": "value4","column2": "value5","column3": "value6"}]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|csv_string|string|True|Resulting CSV string from the conversion|Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFs|
  
Example output:

```
{
  "csv_string": "Y29sdW1uMSxjb2x1bW4yLGNvbHVtbjMNCnZhbHVlMSx2YWx1ZTIsdmFsdWUzDQp2YWx1ZTQsdmFs"
}
```

#### To JSON

This action is used to convert CSV to JSON

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|csv|bytes|None|True|Base64 encoded CSV file|None|ZmllbGQxLCBmaWVsZDIKdmFsdWUxLCB2YWx1ZTIK|None|None|
|validation|boolean|False|True|Validate CSV data, error if not valid|None|True|None|None|
  
Example input:

```
{
  "csv": "ZmllbGQxLCBmaWVsZDIKdmFsdWUxLCB2YWx1ZTIK",
  "validation": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|json|[]object|True|List of objects|[{"field1":"value1","field2":"value2"}]|
  
Example output:

```
{
  "json": [
    {
      "field1": "value1",
      "field2": "value2"
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* Ensure that the supplied file or string is valid CSV. Any CSV files containing double-quotes will need to have them triple escaped to work properly.
* CSV files must not have non-CSV data such as comments.

# Version History

* 2.0.4 - Updated SDK to the latest version (6.3.3)
* 2.0.3 - Updated SDK to the latest version (6.2.5)
* 2.0.2 - Initial updates for fedramp compliance | Updated SDK to the latest version
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

* [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)

## References

* [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)