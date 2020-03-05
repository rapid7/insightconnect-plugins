# Description

The `dirname` InsightConnect plugin is used to get the directory name of a file path or protocol and domain of a URL. This deletes any suffix beginning with the slash `/` character.

Examples, using Python:

```

>>> os.path.dirname('/usr/bin/ssh')
'/usr/bin'
>>> os.path.dirname('https://www.google.com/robots.txt')
'https://www.google.com'

```

# Key Features

* Retrieve directory name of a file path or protocol and domain of a URL.

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Dirname

This action is used to get the directory name of a path.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|path|string|None|True|URL or file path|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dirname|string|False|Directory name of a path|

Example output

```

{
    "dirname": "/usr/local/bin"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

If the input doesn't contain a slash `/` in the path, the result will be an empty string.

# Version History

* 1.0.3 - Update to use the `komand/python-3-37-slim-plugin:3` Docker image | Changed description in action output | Changed `Exception` to `PluginException` | Use output constants
* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Update to use the `komand/python-3-slim-plugin:2` Docker image to reduce plugin size
* 1.0.0 - Support web server mode
* 0.1.1 - Update to v2 Python plugin architecture
* 0.1.0 - Initial plugin

# Links

## References

* [Python Dirname](https://docs.python.org/2/library/os.path.html#os.path.dirname)

