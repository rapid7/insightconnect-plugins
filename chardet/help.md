# Description

This plugin is a Python compatible character encoding detector.

# Key Features

* Detect character encoding

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Detect Encoding

This action is used to detect encoding.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|bytes_to_analyze|bytes|None|True|Bytes to analyze|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|recommendation|recommendation|False|Recommendation|

Example output:

```
{
  "recommendation": {
    "encoding": "Windows-1254",
    "confidence": 0.2105891645091143,
    "language": "Turkish"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [Chardet](https://chardet.readthedocs.io/en/latest/index.html)
* [How it Works](https://chardet.readthedocs.io/en/latest/how-it-works.html)

