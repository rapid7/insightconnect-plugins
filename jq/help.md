# Description

[jq](https://stedolan.github.io/jq/) is a command-line tool used for slicing, filtering, mapping, and transforming structured JSON data. The jq plugin passes the given list of flags to the jq command, which then runs the given filter expression on the given JSON input. For flexibility, the output is returned as a string.

# Key Features

* JSON File processing

# Requirements

_This plugin does not contain any requirements_

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Run

This action is used to pass the given JSON object to the jq command, using the given flags and filter.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|None|True|Filter expression to be used by the jq command not in surrounding quotes|None|
|json_in|object|None|True|Data in JSON format to be passed to jq|None|
|flags|[]string|None|False|Flags with which to invoke the jq command (e.g. -c)|None|
|timeout|integer|15|False|Timeout in seconds during which the jq command runs|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|json_out|string|True|The output JSON|

Example output:

```
{
  "json_out": "[\"How's it going?\",\"What's up?\"]"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Note that the filter expression should not be surrounded by quotes.
This differs from use of jq on the command line, where the jq filter
needs to be quoted to avoid collision with special shell characters.

Likewise, individual command flags should not be surrounded by
quotes.

If the flags or filter given to jq are not well formed, this plugin
returns a string beginning with "ill-formed jq command".  One
possible problem might be a mismatch between the expected jq version
and the version actually contained in the plugin.

If jq fails to produce output within the given timeout (or 10
seconds if not supplied) this plugin returns the special string
"TIMEOUT".

Note that the jq command itself can return the string "null".  This
may be expected, or it may indicate a problem in the given filter
string.

The `--seq` and `--stream` flags are not supported in version 0.1.0 of this plugin.

# Version History

* 2.0.5 - New spec and help.md format for the Hub | Changed docker image from `komand/python-3-slim-plugin:2` to `komand/python-3-37-slim-plugin` | Change mutable function parameter to immutable | Removed comments | Changed concatenation to format in loggers
* 2.0.4 - Fix issue where jq was not available in the docker image | Update to python | Update to use the `komand/python-3-slim-plugin:2` Docker image to reduce plugin size | Set a default `timeout` of 15 seconds in the Run action
* 2.0.3 - Add `utilities` plugin tag for Marketplace searchability
* 2.0.2 - Regenerate with latest Go SDK to solve bug with triggers
* 2.0.1 - Updating to Go SDK 2.6.4
* 2.0.0 - Rename "JQ" plugin title to "jq" | Rename "Run JQ" action to "Run"
* 1.1.0 - Support web server mode
* 1.0.0 - Update to v2 Go plugin architecture
* 0.1.3 - Strip trailing newline on output
* 0.1.2 - Larger inputs were blocking
* 0.1.1 - Allow arrays to be passed into jq
* 0.1.0 - Initial plugin

# Links

## References

* [jq](https://stedolan.github.io/jq/)

