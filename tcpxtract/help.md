# Description

[Tcpxtract](http://tcpxtract.sourceforge.net/) is a tool for extracting files from network traffic.

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

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin does not contain a connection.

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

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Support web server mode | Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Tcpxtract](http://tcpxtract.sourceforge.net/)

