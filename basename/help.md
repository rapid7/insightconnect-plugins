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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|path|string|None|True|URL or file path|None|https://example.com/text.txt|

Example input:

```
{
  "path": "https://example.com/text.txt"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|basename|string|False|Basename result|

Example output:

```
{
  "basename": "text.txt"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

If the input doesn't contain a slash `/` in the path the result will be the original string unmodified.

# Version History

* 1.1.0 - Add missing `title` in action Basename | Use input and output constants | Add example input and output | Changed `Exception` to `PluginException` | Added "f" strings
* 1.0.2 - Update to use the `insightconnect-python-3-38-slim-plugin:4` Docker image | Update plugin.spec.yaml to include `cloud_ready`
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode
* 0.1.1 - Update to v2 Python plugin architecture
* 0.1.0 - Initial plugin

# Links

## References

* [Python Basename](https://docs.python.org/2/library/os.path.html#os.path.basename)
