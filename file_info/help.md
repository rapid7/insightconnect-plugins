# Description

Return basic information about a file including its size and file type.

# Key Features

* Information about file type
* Information about file size

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Get File Info

This action is used to get information about a file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|True|The file to analyze, represented in base64 (bytes type)|None|cmFwaWQ3IGluc2lnaHQ=|

Example input:

```
{
  "file": "cmFwaWQ3IGluc2lnaHQ="
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_size|integer|True|Return information about file size|
|file_type|string|True|Return information about file type|

Example output:

```
{
  "file_size": 288,
  "file_type": "pdf"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [File type](https://pypi.org/project/filetype/)
