# Description

[Base64](https://en.wikipedia.org/wiki/Base64) is a common binary-to-text encoding scheme used in various protocols and software such as MIME.
This plugin utilizes allows data to be encoded or decoded using the standard Base64 alphabet.

# Key Features

* Encode text
* Decode text

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Encoder

This action is used to Base64 encode a `string` using the standard Base64 alphabet.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|content|string|None|True|String to Encode|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|bytes|False|None|

#### Decoder

This action is used to decode a Base64 `string` or file of type `bytes` using the standard Base64 alphabet.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|base64|bytes|None|True|Data to decode|None|
|errors|string|None|False|How errors should be handled when decoding Base64 e.g replace or ignore|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|string|False|None|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For the Base64 decode action, be sure that the input contains valid Base64 data.

If the Base64 you're decoding contains any non UTF-8 characters the plugin will fail. To remedy this issue, there's a
option to set how errors are to be handled. These options are "replace" and "ignore". Replace will change all non UTF-8
characters to `\uffd` or `?`. While ignore will drop the character from the output.

# Version History

* 1.1.2 - New spec and help.md format for the Hub
* 1.1.1 - Fixed issue where action Decode required error parameter
* 1.1.0 - Bug fix in decode action, added an option for error handling
* 1.0.0 - Support web server mode
* 0.2.2 - Generate plugin with new schema
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Plugin variable naming and description improvements, add required outputs
* 0.1.1 - Bug fix in output variables
* 0.1.0 - Initial plugin

# Links

## References

* [Base64](https://en.wikipedia.org/wiki/Base64)
* [Python Base64 Encode](https://docs.python.org/2/library/base64.html#base64.standard_b64encode)
* [Python Base64 Decode](https://docs.python.org/2/library/base64.html#base64.standard_b64decode)

