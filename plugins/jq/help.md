# Description

[jq](https://stedolan.github.io/jq/) is a command-line tool used for slicing, filtering, mapping, and transforming structured JSON data. The jq plugin passes the given list of flags to the jq command, which then runs the given filter expression on the given JSON input. For flexibility, the output is returned as a string

# Key Features

* JSON File processing

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2025-04-17

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Run

This action is used to pass the given JSON to the jq command, using the given flags and filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|Filter expression to be used by the jq command not in surrounding quotes|None|.user.name|None|None|
|flags|[]string|None|False|Flags with which to invoke the jq command (e.g. ["-c"]). Multiple flags are supported in one action: ["-c", "-r", "--tab"] and the following are all possible flags: ["-c", "-r", "-R", "-j", "-S", "-n", "--tab"]|None|[]|None|None|
|json_in|object|None|True|Data in JSON format to be passed to jq|None|{'user': {'name': 'Alice', 'age': 30}}|None|None|
|timeout|integer|15|False|Timeout in seconds during which the jq command runs|None|15|None|None|
  
Example input:

```
{
  "filter": ".user.name",
  "flags": [],
  "json_in": {
    "user": {
      "age": 30,
      "name": "Alice"
    }
  },
  "timeout": 15
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|json_out|string|True|The output JSON|"Alice"|
  
Example output:

```
{
  "json_out": "Alice"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* Note that the filter expression should not be surrounded by quotes. This differs from use of jq on the command line, where the jq filter needs to be quoted to avoid collision with special shell characters.
* Likewise, individual command flags should not be surrounded by quotes.
* If the flags or filter given to jq are not well formed, this plugin returns a string beginning with "ill-formed jq command". One possible problem might be a mismatch between the expected jq version and the version actually contained in the plugin.
* If jq fails to produce output within the given timeout (or 10 seconds if not supplied) this plugin returns the special string `"TIMEOUT"`.
* Note that the jq command itself can return the string `"null"`. This may be expected, or it may indicate a problem in the given filter string.
* The `--seq` and `--stream` flags are not supported in version 0.1.0 of this plugin.

# Version History

* 3.0.0 - Enabled plugin as `cloud_ready` | Updated `run` action to limit `flag` inputs | 'filter` input no longer required for action to run | Updated SDK to the latest version (6.3.3) | Unit Tests added
* 2.0.5 - New spec and help.md format for the Extension Library | Changed docker image from `komand/python-3-slim-plugin:2` to `komand/python-3-37-slim-plugin` | Change mutable function parameter to immutable | Removed comments | Changed concatenation to format in loggers
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

* https://jqlang.org/

## References

* [jq](https://stedolan.github.io/jq/)