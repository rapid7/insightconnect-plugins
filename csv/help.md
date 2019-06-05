
# CSV

## About

[Comma Separated Value](https://en.wikipedia.org/wiki/Comma-separated_values) (CSV) is a common format to express data.
This plugin allows one to extract fields from CSV strings and files.

## Actions

### Filter Bytes

This action is used to extract fields from a user supplied CSV file expressed a base64 encoded data (bytes) and return a new CSV file
with the extracted fields only.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|fields|string|None|False|Fields to filter E.g. f1, f2, f3-f6|None|
|csv|bytes|None|False|Base64 encoded CSV file|None|

Field numbers (e.g. `f1`) and a range of fields (e.g. `f5-7`) are used to defined the extraction.
For example, to extract fields 1, 2, 4, 5, 6 the following fields value can be used: `f1, f2, f4-6`.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filtered|bytes|False|Filtered CSV file|

### Filter String

This action is used to extract fields from a user supplied CSV string and return a new CSV string with the extracted fields only.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|fields|string|None|False|Fields to filter E.g. f1, f2, f3-f6|None|
|csv|string|None|False|CSV string|None|

Field numbers (e.g. `f1`) and a range of fields (e.g. `f5-7`) are used to defined the extraction. For example, to extract fields
1, 2, 4, 5, 6 the following fields value can be used: `f1, f2, f4-6`.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|string|string|False|Filtered CSV string|

### To JSON

This action is used to convert CSV to JSON.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|csv|bytes|None|True|Base64 encoded CSV file|None|

#### Output

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

### JSON to CSV

This action is used to convert a JSON array to CSV.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|json|[]object|None|True|JSON array to convert to CSV|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|csv|bytes|True|Resulting CSV file from the conversion|

Example output:

```

{
  "csv": "QXNzZXQgT1MgRmFtaWx5LEFzc2V0IE9TIE5hbWUsQXNzZXQgSVAgQWRkcmVzcyxBc3NldCBOYW1lcyxBc3NldCBPUyBWZXJzaW9uDQpNaWNyb3NvZnQgV2luZG93cyxNaWNyb3NvZnQgV2luZG93cyBTZXJ2ZXIgMjAxMiBTdGFuZGFyZCBFZGl0aW9uLDEwLjQuMjMuNDYsIkJJR0ZJWC1DTFQtVzEyLGJpZ2ZpeC1jbHQtdzEyLnZ1bG4ubGF4LnJhcGlkNy5jb20iLA0KTWljcm9zb2Z0IFdpbmRvd3MsTWljcm9zb2Z0IFdpbmRvd3MgU2VydmVyIDIwMTIgU3RhbmRhcmQgRWRpdGlvbiwxMC40LjIzLjY5LCJCSUdGSVgtU1JWLGJpZ2ZpeC1zcnYudnVsbi5sYXgucmFwaWQ3LmNvbSIsDQpNaWNyb3NvZnQgV2luZG93cyxNaWNyb3NvZnQgV2luZG93cyBTZXJ2ZXIgMjAxMiBTdGFuZGFyZCBFZGl0aW9uLDEwLjQuMjMuNjksIkJJR0ZJWC1TUlYsYmlnZml4LXNydi52dWxuLmxheC5yYXBpZDcuY29tIiwNCk1pY3Jvc29mdCBXaW5kb3dzLE1pY3Jvc29mdCBXaW5kb3dzIDcgRW50ZXJwcmlzZSBFZGl0aW9uLDEwLjQuMjMuNTUsIkJJR0ZJWC1DTFQtVzcsYmlnZml4LWNsdC13Ny52dWxuLmxheC5yYXBpZDcuY29tIixTUDENCg == "
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

Ensure that the supplied file or string is valid CSV. Any CSV files containing double-quotes will need to have them triple escaped to work properly.
CSV files must not have non-CSV data such as comments.

## Workflows

Examples:

* Data format

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 0.1.2 - Update to v2 Python plugin architecture
* 1.0.0 - Add CSV to JSON action | Support web server mode
* 1.1.0 - Add JSON to CSV action
* 1.1.1 - Fix JSON to CSV action to account for correct input type
* 1.1.2 - Support webserver mode
* 1.1.3 - Fix issue where connection tests were failing, output did not match spec

## References

* [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)
