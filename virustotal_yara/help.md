# Description

Identity and classify malware based on textual or binary patterns.  Provide simple rules when scanning files based on those patterns.  [VirusTotal Yara](http://virustotal.github.io/yara/) is a pattern matching swiss knife for malware researchers. This plugin utilizes [yara-python](https://pypi.python.org/pypi/yara-python), a Python library for Yara.

# Key Features

* Binary scans on a file
* Text scans

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Scan File

This action scans a file using Yara.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|True|File to be scanned|None|aGVsbG8gd29ybGQK=|
|rules|bytes|None|True|File containing Yara rules|None|cnVsZSBoZWxsbwp7CglzdHJpbmdzOgoJCSRzaGVsbG8gPSAiSGVsbG8sIFdvcmxkIgoJY29uZGl0aW9uOgoJCSRzaGVsbG8KfQo=|

Example input:

```
{
  "file": "aGVsbG8gd29ybGQK=",
  "rules": "cnVsZSBoZWxsbwp7CglzdHJpbmdzOgoJCSRzaGVsbG8gPSAiSGVsbG8sIFdvcmxkIgoJY29uZGl0aW9uOgoJCSRzaGVsbG8KfQo="
}
```

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

_This plugin does not contain any triggers._

### Custom Output Types

#### results

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Meta|object|False|Metadata|
|Namespace|string|False|Namespace|
|Rule|string|False|Rule that was used|
|String|[]string|False|String that the rule triggered on|
|Tags|[]string|False|A collection of tags|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.2 - Add example inputs
* 1.1.1 - New spec and help.md format for the Hub
* 1.1.0 - Support web server mode
* 1.0.0 - Undocumented update
* 0.1.0 - Initial plugin

# Links

## References

* [VirusTotal Yara](http://virustotal.github.io/yara/)
* [yara-python](https://pypi.python.org/pypi/yara-python)

