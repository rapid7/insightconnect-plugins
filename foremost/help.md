
# Foremost

## About

[Foremost](http://foremost.sourceforge.net/) is a data carving tool and is used to recover files from a disk image file.

It supports carving the following file types: jpg, gif, png, bmp, avi, exe, mpg, mp4, wav, riff, wmv, mov, pdf, ole, doc, zip, rar, htm, cpp, nts.

## Actions

### Extract

This action is used to extract files from a disk image.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|True|Base64 encoded disk image file|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|[]bytes|False|Extracted files|
|file_count|integer|False|Number of files extracted|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

Foremost only works on disk images such as those created by the `dd` tool.

## Workflows

Examples:

* File carving, data recovery
* Forensics

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Support web server mode

## References

* [Foremost](http://foremost.sourceforge.net/)
