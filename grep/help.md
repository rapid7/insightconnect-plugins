# Description

The Grep InsightConnect plugin searches for a specified pattern in a string or a file by utilizing BusyBox grep. It calls `egrep` which supports extended regular expressions to improve pattern matching ability.

For example, here's a simple example of `egrep` from the command line:

```

$ printf "cat\ndog\nhorse\nbirds" | egrep 'dog|bird'
dog
bird

```

# Key Features

* Search pattern in a string
* Search pattern in a file

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Match Base64

This action is used to find patterns in a base64 encoded document.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pattern|string|None|True|Pattern to match|None|
|data|bytes|None|True|Base64 encoded text|None|
|behavior|string|Default|False|Return entire matched lines or only matched pattern|['Default', 'Only matching']|

##### Output

The plugin returns the the number of matches found, a string array of the matched lines, and whether any matches were found.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|matches|[]string|False|Matched lines|
|found|boolean|False|Found match boolean|
|hits|integer|False|Number of matches|

#### Match String

This action is used to find patterns in a string.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pattern|string|None|True|Pattern to match|None|
|behavior|string|Default|False|Return entire matched lines or only matched pattern|['Default', 'Only matching']|
|text|string|None|True|String to match|None|

##### Output

The plugin returns the the number of matches found, a string array of the matched lines, and whether any matches were found.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|matches|[]string|False|Matched lines|
|found|boolean|False|Found match boolean|
|hits|integer|False|Number of matches|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.4 - New spec and help.md format for the Hub
* 1.0.3 - New spec and help.md format for the Hub
* 1.0.2 - Update to use the `komand/python-3-slim-plugin:2` Docker image to reduce plugin size
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.0 - Support web server mode
* 0.1.2 - Bug fix to allow files over 1000 lines and not error when no matches are returned
* 0.1.1 - Port to Python 3 and update to v2 Python plugin architecture
* 0.1.0 - Initial plugin

# Links

## References

* [Grep](https://www.gnu.org/software/grep/manual/grep.html)

