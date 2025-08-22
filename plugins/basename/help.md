# Description

Basename is used to get the last item of a file path or URL using Python's basename utility

# Key Features

* Obtain Basename of a file path or URL.

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* Python 3.11

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Basename

This action is used to get the Basename of a path

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|path|string|None|True|URL or file path|None|https://example.com/text.txt|None|None|
  
Example input:

```
{
  "path": "https://example.com/text.txt"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|basename|string|False|Basename result|text.txt|
  
Example output:

```
{
  "basename": "text.txt"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* If the input doesn't contain a slash `/` in the path the result will be the original string unmodified.

# Version History

* 1.1.5 - Updated SDK to the latest version (6.3.9)
* 1.1.4 - Updated SDK to the latest version (6.2.5)
* 1.1.3 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 1.1.2 - Added `__init__.py` file to `unit_test` folder | Refreshed with new Tooling
* 1.1.1 - Update SDK to version 5
* 1.1.0 - Add missing `title` in action Basename | Use input and output constants | Add example input and output | Changed `Exception` to `PluginException` | Added "f" strings
* 1.0.2 - Update to use the `insightconnect-python-3-38-slim-plugin:4` Docker image | Update plugin.spec.yaml to include `cloud_ready`
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode
* 0.1.1 - Update to v2 Python plugin architecture
* 0.1.0 - Initial plugin 

# Links

* [Python Basename](https://docs.python.org/3/library/os.path.html)

## References

* [Python Basename](https://docs.python.org/3/library/os.path.html)