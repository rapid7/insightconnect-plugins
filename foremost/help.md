# Description

[Foremost](http://foremost.sourceforge.net/) is a data carving tool and is used to recover files from a disk image file.

It supports carving the following file types: jpg, gif, png, bmp, avi, exe, mpg, mp4, wav, riff, wmv, mov, pdf, ole, doc, zip, rar, htm, cpp, nts.

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

This action is used to extract files from a disk image.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|True|Base64 encoded disk image file|None|

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

Foremost only works on disk images such as those created by the `dd` tool.

# Version History

* 1.0.0 - Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Foremost](http://foremost.sourceforge.net/)

