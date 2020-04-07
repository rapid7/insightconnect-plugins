# Description

The Basename InsightConnect plugin is used to get the last item of a file path or URL using Python's `basename` utility.
The `basename` utility deletes any prefix ending with the last slash `/` character.

For example:

```

>>> os.path.basename('/usr/bin/ssh')
'ssh'
>>> os.path.basename('https://www.google.com/robots.txt')
'robots.txt'

```

# Key Features

* Obtain Basename of a file path or URL.

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Basename

This action is used to get the `basename` of a path.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|path|string|None|True|URL or file path|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|basename|string|False|Basename result|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

If the input doesn't contain a slash `/` in the path the result will be the original string unmodified.

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode
* 0.1.1 - Update to v2 Python plugin architecture
* 0.1.0 - Initial plugin

# Links

## References

* [Python Basename](https://docs.python.org/2/library/os.path.html#os.path.basename)

