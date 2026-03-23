# Description

The Compression plugin for Rapid7 InsightConnect allows users to compress/decompress files using different compression algorithms

# Key Features

* File compression using gzip, bzip, lz, xz, and ZIP algorithms
* File decompression with automatic algorithm detection

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2026-03-16

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Compress Bytes

This action is used to compress a file using a choice of one of the following compression algorithms gzip, bzip, lz, 
xz, or ZIP

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|algorithm|string|None|True|Compression algorithm|["gzip", "bzip", "lz", "xz", "zip"]|gzip|None|None|
|bytes|bytes|None|True|Base64-encoded file/bytes|None|SGVsbG8gV29ybGQ=|None|None|
  
Example input:

```
{
  "algorithm": "gzip",
  "bytes": "SGVsbG8gV29ybGQ="
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|compressed|bytes|False|Compressed file as Base64-encoded bytes|H4sIAAAAAAAAA0tMTAYAVMUbFQQAAAA=|
  
Example output:

```
{
  "compressed": "H4sIAAAAAAAAA0tMTAYAVMUbFQQAAAA="
}
```

#### Create Archive

This action is used to compress files into an archive

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|algorithm|string|None|True|Compression algorithm|["tarball", "zip"]|zip|None|None|
|filename|string|None|True|Name of file archive|None|archive.zip|None|None|
|files|[]file|None|True|Files to be compressed|None|[{"filename": "test.txt", "content": "sample content"}]|None|None|
  
Example input:

```
{
  "algorithm": "zip",
  "filename": "archive.zip",
  "files": [
    {
      "content": "sample content",
      "filename": "test.txt"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|archive|file|False|Compressed archive file|{"filename": "archive.zip", "content": "UEsDBBQAAAAIAA=="}|
  
Example output:

```
{
  "archive": {
    "content": "UEsDBBQAAAAIAA==",
    "filename": "archive.zip"
  }
}
```

#### Decompress Bytes

This action is used to decompress a file by automatically determining the compression algorithm used and returning the 
decompressed file. Supported algorithms are gzip, bzip, lz, xz, and ZIP

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|bytes|bytes|None|True|Compressed Base64-encoded bytes|None|H4sIAAAAAAAAA0tMTAYAVMUbFQQAAAA=|None|None|
  
Example input:

```
{
  "bytes": "H4sIAAAAAAAAA0tMTAYAVMUbFQQAAAA="
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|decompressed|bytes|False|Decompressed file as Base64-encoded bytes|SGVsbG8gV29ybGQ=|
  
Example output:

```
{
  "decompressed": "SGVsbG8gV29ybGQ="
}
```

#### Extract Archive

This action is used to extract file archive

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|archive|file|None|True|Base64-encoded archive file|None|{"filename": "archive.zip", "content": "UEsDBBQAAAAIAA=="}|None|None|
  
Example input:

```
{
  "archive": {
    "content": "UEsDBBQAAAAIAA==",
    "filename": "archive.zip"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|files|[]file|False|Extracted files from the archive|[{"filename": "test.txt", "content": "c2FtcGxlIGNvbnRlbnQ="}]|
  
Example output:

```
{
  "files": [
    {
      "content": "c2FtcGxlIGNvbnRlbnQ=",
      "filename": "test.txt"
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

* On decompression, be sure that the inputted file has been compressed using one of the supported algorithms.

# Version History

* 2.0.3 - Updated dependency | Updated SDK to the latest version (6.4.3)
* 2.0.2 - Correct spelling in help.md
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Rename "Create archive" action to "Create Archive" | Rename "Decompress bytes" action to "Decompress Bytes" | Rename "Compress bytes" action to "Compress Bytes" | Rename "Extract Archive" to "Exctract archive"
* 1.1.0 - Port to Python v2 architecture | Support web server mode
* 1.0.3 - Extract archive single file bug fix
* 1.0.2 - Decompress gz files within ZIP file
* 1.0.1 - New structure and compress multi file support
* 1.0.0 - Multiple files support for ZIP files | Update to v2 Python plugin architecture
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Add ZIP file support
* 0.1.0 - Initial plugin

# Links

* [bz2 python library](https://docs.python.org/3/library/bz2.html)
* [gzip python library](https://docs.python.org/3/library/gzip.html)
* [lz python library](https://docs.python.org/3/library/lzma.html)
* [xz python library](https://docs.python.org/3/library/lzma.html)
* [zipfile python library](https://docs.python.org/3/library/zipfile.html)

## References

* [bz2 python library](https://docs.python.org/3/library/bz2.html)
* [gzip python library](https://docs.python.org/3/library/gzip.html)
* [lz python library](https://docs.python.org/3/library/lzma.html)
* [xz python library](https://docs.python.org/3/library/lzma.html)
* [zipfile python library](https://docs.python.org/3/library/zipfile.html)