# Description

[Foremost](http://foremost.sourceforge.net/) is a data carving tool and is used to recover files from a disk image file. The Foremost plugin will take a disk image and attempt to recover files from it.

It supports carving the following file types: jpg, gif, png, bmp, avi, exe, mpg, mp4, wav, riff, wmv, mov, pdf, ole, doc, zip, rar, htm, cpp, nts.

# Key Features

* Extract files from a disk image

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Extract

This action is used to extract files from a disk image.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|True|Base64 encoded disk image file|None|

Example input:

```
{
    "file": "UEsDBBQAAAAIAAFziEk97XjbGgAAABwAAAAIABwAdGVzdC50eHRVVAkAAwFtSVhabUlYdXgLAAEE6AMAAAToAwAAK8nILFYAokSFktTiEoW0/CIQTs3NLy7hAgBQSwECHgMUAAAACAABc4hJPe142xoAAAAcAAAACAAYAAAAAAABAAAAtIEAAAAAdGVzdC50eHRVVAUAAwFtSVh1eAsAAQToAwAABOgDAABQSwUGAAAAAAEAAQBOAAAAXAAAAAAA"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_count|integer|False|Number of files extracted|
|files|[]bytes|False|Extracted files|

Example output:

```
{
  "file_count": 1,
  "files": [
    "UEsDBBQAAAAIAAFziEk97XjbGgAAABwAAAAIABwAdGVzdC50eHRVVAkAAwFtSVhabUlYdXgLAAEE6AMAAAToAwAAK8nILFYAokSFktTiEoW0/CIQTs3NLy7hAgBQSwECHgMUAAAACAABc4hJPe142xoAAAAcAAAACAAYAAAAAAABAAAAtIEAAAAAdGVzdC50eHRVVAUAAwFtSVh1eAsAAQToAwAABOgDAABQSwUGAAAAAAEAAQBOAAAAXAAAAAAAAA=="
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Foremost only works on disk images such as those created by the `dd` tool.

# Version History

* 1.0.2 - Use input and output constants | Change docker image from `komand/python-3-plugin:2` to `komand/python-3-37-plugin:3` to reduce plugin image size | Use input and output constants | Added "f" strings | Changed `Exception` to `PluginException` | Change "/tmp" to tempfile.gettempdir()
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Foremost](http://foremost.sourceforge.net/)

