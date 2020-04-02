# Description

The Diff InsightConnect plugin allows you to find the difference between strings using Python's [difflib](https://docs.python.org/3/library/difflib.html) library.
Results persist across runs of workflows (using the unique label).

# Key Features

* Get changes between strings.

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Diff

This action is used to `diff` strings.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|compare|string|None|True|New data, for comparison against the old data|None|
|label|string|None|True|Unique label to store the old data|None|

Example input:

```
{
  "compare": "hello 1234",
  "label": "helloer"
}

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|diff|string|False|Diff string|
|different|boolean|False|True if different|

Example output:

```
{
  "diff": "",
  "different": false
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.3 - Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Add user nobody in Dockerfile | Use input and output constants | Added "f" strings | Add example inputs
* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Update plugin tag `utility` to `utilities` for Marketplace searchability
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* None

