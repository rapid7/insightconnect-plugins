# Description

[Base64](https://en.wikipedia.org/wiki/Base64) is a common binary-to-text encoding scheme used in various protocols and software such as MIME to carry data stored in binary formats across channels that only reliably support text content. This plugin allows data to be Base64-encoded or decoded using the standard Base64 alphabet

# Key Features

* Encode data in Base64 to transfer binary data, image files, etc. in a text format
* Decode Base64 encoded text to reveal the plaintext

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-08-05

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Decoder

This action is used to decode a Base64 `string` or file of type `bytes` using the standard Base64 alphabet

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|base64|bytes|None|True|Data to decode|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0IQ==|None|None|
|errors|string|nothing|False|How errors should be handled when decoding Base64|["replace", "ignore", "nothing"]|ignore|None|None|
  
Example input:

```
{
  "base64": "UmFwaWQ3IEluc2lnaHRDb25uZWN0IQ==",
  "errors": "nothing"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|string|True|Decoded data result|Rapid7 InsightConnect!|
  
Example output:

```
{
  "data": "Rapid7 InsightConnect!"
}
```

#### Encoder

This action is used to encode a `string` using the standard Base64 alphabet

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|content|string|None|True|Data to encode|None|Rapid7 InsightConnect|None|None|
  
Example input:

```
{
  "content": "Rapid7 InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|bytes|True|Encoded data result|UmFwaWQ3IEluc2lnaHRDb25uZWN0|
  
Example output:

```
{
  "data": "UmFwaWQ3IEluc2lnaHRDb25uZWN0"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* For the Base64 decode action, be sure that the input contains valid Base64 data.
* If the Base64 you're decoding contains any non UTF-8 characters the plugin will fail. To remedy this issue, there's a option to set how errors are to be handled. These options are "replace" and "ignore". Replace will change all non UTF-8 characters to `\uffd` or `?`. While ignore will drop the character from the output.

# Version History

* 1.1.10 - Updated SDK to the latest version (6.3.3)
* 1.1.9 - Updated SDK to the latest version (6.2.5)
* 1.1.8 - Updated SDK to the latest version (v6.2.2) | Address vulnerabilities
* 1.1.7 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 1.1.6 - Update to v4 Python plugin runtime
* 1.1.5 - Improve PluginException message in Decode action
* 1.1.4 - Add example inputs
* 1.1.3 - Use input and output constants | Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Change `Exception` to `PluginException` | Change descriptions in help.md | Add user nobody in Dockerfile
* 1.1.2 - New spec and help.md format for the Extension Library
* 1.1.1 - Fixed issue where action Decode required error parameter
* 1.1.0 - Bug fix in decode action, added an option for error handling
* 1.0.0 - Support web server mode
* 0.2.2 - Generate plugin with new schema
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Plugin variable naming and description improvements, add required outputs
* 0.1.1 - Bug fix in output variables
* 0.1.0 - Initial plugin

# Links

* [Base64$](https://en.wikipedia.org/wiki/Base64)

## References

* [Base64](https://en.wikipedia.org/wiki/Base64)
* [Python Base64 Encode](https://docs.python.org/2/library/base64.html#base64.standard_b64encode)
* [Python Base64 Decode](https://docs.python.org/2/library/base64.html#base64.standard_b64decode)