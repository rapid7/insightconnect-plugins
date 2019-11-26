# Description

The Compression plugin for Rapid7 InsightConnect allows users to compress/decompress files using different
compression algorithms. Use this plugin to help enable interoperability between different services, compress data
for faster file transmission, and more.

# Key Features

* File Compression
* File decompression

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Compress Bytes

This action is used to compress a file. It supports a choice of one of the following Compression algorithms:

* gzip
* bzip
* lz
* xz
* zip

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|bytes|bytes|None|False|Base64-encoded file|None|
|algorithm|string|None|False|Compression algorithm|['gzip', 'bzip', 'lz', 'xz', 'zip']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|compressed|bytes|False|None|

#### Decompress Bytes

This action is used to decompress a file. It automatically determines the Compression algorithm used, decompresses it,
and returns the decompressed file.

The following algorithms are supported:

* gzip
* bzip
* lz
* xz
* zip

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|bytes|bytes|None|False|Base64-encoded file|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decompressed|bytes|False|None|

#### Create Archive

This action is used to compress a files into archive.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|files|[]file|None|True|Files to be compressed|None|
|algorithm|string|None|True|Compression algorithm|['tarball', 'zip']|
|filename|string|None|True|Name of file archive|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|archive|file|False|Archive|

Example output:

```
```

#### Extract Archive

This action is used to exctract file archive.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|archive|file|None|True|Base64-encoded archive file|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|[]file|False|Files|

Example output:

```
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

On decompression, be sure that the inputted file has been compressed using one of the supported algorithms.

# Version History

* 2.0.2 - New spec and help.md format for the Hub
* 2.0.1 - New spec and help.md format for the Hub
* 2.0.0 - Rename "Create archive" action to "Create Archive" | Rename "Decompress bytes" action to "Decompress Bytes" | Rename "Compress bytes" action to "Compress Bytes" | Rename "Extract Archive" to "Exctract archive"
* 1.1.0 - Port to Python v2 architecture | Support web server mode
* 1.0.3 - Extract archive single file bug fix
* 1.0.2 - Decompress gz files within zip file
* 1.0.1 - New structure and compress multi file support
* 1.0.0 - Multiple files support for ZIP files | Update to v2 Python plugin architecture
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Add ZIP file support
* 0.1.0 - Initial plugin

# Links

## References

* [bz2 python library](https://docs.python.org/3/library/bz2.html)
* [gzip python library](https://docs.python.org/3/library/gzip.html)
* [lz python library](https://docs.python.org/3/library/lzma.html)
* [xz python library](https://docs.python.org/3/library/lzma.html)
* [zipfile python library](https://docs.python.org/3/library/zipfile.html)

