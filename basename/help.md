
# Basename

## About

The `basename` utility deletes any prefix ending with the last slash `/` character
This plugin is used to get the last item of a file path or URL. Examples, using Python

```

>>> os.path.basename('/usr/bin/ssh')
'ssh'
>>> os.path.basename('https://www.google.com/robots.txt')
'robots.txt'

```

## Actions

### Basename

This action is used to get the `basename` of a path.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|path|string|None|True|URL or file path|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|basename|string|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

If the input doesn't contain a slash `/` in the path the result will be the original string unmodified.

## Workflows

Examples:

* Data formatting for any workflow

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - Update to v2 Python plugin architecture
* 1.0.0 - Support web server mode

## References

* [Python Basename](https://docs.python.org/2/library/os.path.html#os.path.basename)
