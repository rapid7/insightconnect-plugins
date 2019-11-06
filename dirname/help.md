# Description

The `dirname` utility deletes any suffix beginning with the slash `/` character
This plugin is used to get the directory name of a file path or protocol and domain of a URL. Examples, using Python

```

>>> os.path.dirname('/usr/bin/ssh')
'/usr/bin'
>>> os.path.dirname('https://www.google.com/robots.txt')
'https://www.google.com'

```

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin does not contain a connection.

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
|dirname|string|False|None|

Example output

```

{
    "dirname": "/usr/local/bin"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

If the input doesn't contain a slash `/` in the path, the result will be an empty string.

# Version History

* 1.0.1 - Update to use the `komand/python-3-slim-plugin:2` Docker image to reduce plugin size
* 1.0.0 - Support web server mode
* 0.1.1 - Update to v2 Python plugin architecture
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Python Dirname](https://docs.python.org/2/library/os.path.html#os.path.dirname)

