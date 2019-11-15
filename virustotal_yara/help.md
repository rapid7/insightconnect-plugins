# Description

The VirusTotal Yara plugin allows the user to analyze files with the Yara Python libarary.

[VirusTotal Yara](http://virustotal.github.io/yara/) is a pattern matching swiss knife for malware researchers.
This plugin utilizes [yara-python](https://pypi.python.org/pypi/yara-python), a Python library for Yara.

# Key Features

* Scan a file

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Scan File

This action is used to scan a file using Yara.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|rules|file|None|True|File containing Yara rules|None|
|file|file|None|True|File to be scanned|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]object|True|Results returned form Yara's analysis. Note: byte information has been encoded to UTF-8|

Example output:

```

{
  "meta": {},
  "namespace": "default",
  "rule": "hello_world",
  "string": [
    "3994",
    "$example_output",
    "Hello, World"
  ],
  "tags": []
  }

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.1.0 - Support web server mode
* 1.0.0 - Undocumented update
* 0.1.0 - Initial plugin

# Links

## References

* [VirusTotal Yara](http://virustotal.github.io/yara/)
* [yara-python](https://pypi.python.org/pypi/yara-python)

