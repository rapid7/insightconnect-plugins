# Description

The [Tcpxtract](http://tcpxtract.sourceforge.net/) plugin is a tool for extracting files from network traffic.

It supports extracting the following file types:

* avi
* mpg
* fws
* art
* gif
* jpg
* png
* bmp
* tif
* doc
* pst
* ost
* dbx
* idx
* mbx
* html
* pdf
* mail
* ra
* zip
* java

# Key Features

* Extract a file from a PCAP file.

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Extract

This action is used to extract files from a given PCAP file.
A count of files extracted as well as a `bytes array` of the extracted files are returned.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|True|Base64 encoded pcap|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|[]bytes|False|Extracted files|
|file_count|integer|False|Number of files extracted|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode | Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Tcpxtract](http://tcpxtract.sourceforge.net/)

