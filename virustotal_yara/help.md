# Description

Identity and classify malware based on textual or binary patterns.  Provide simple rules when scanning files based on those patterns.  [VirusTotal Yara](http://virustotal.github.io/yara/) is a pattern matching swiss knife for malware researchers. This plugin utilizes [yara-python](https://pypi.python.org/pypi/yara-python), a Python library for Yara.

# Key Features

* Binary scans on a file
* Text scans

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
|file|bytes|None|True|File to be scanned|None|
|rules|bytes|None|True|File containing Yara rules|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]results|True|Results returned from the Yara analysis. It is byte information, encoded to UTF-8|

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

* 1.1.1 - New spec and help.md format for the Hub
* 1.1.0 - Support web server mode
* 1.0.0 - Undocumented update
* 0.1.0 - Initial plugin

# Links

## References

* [VirusTotal Yara](http://virustotal.github.io/yara/)
* [yara-python](https://pypi.python.org/pypi/yara-python)

