# Description

This plugin allows basic arithmetic functions to be performed

# Key Features

* Math operations module and exponents
* Math Division and multiplication, addition and subtraction

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-10-09

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Calculate

This action is used to run a calculation

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|equation|string|None|True|Equation to calculate. Uses Python arithmetic operators (+, -, /, *, **, %)|None|((3**2) * 3) + 3 - 5|None|None|
  
Example input:

```
{
  "equation": "((3**2) * 3) + 3 - 5"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|number|True|Result of the arithmetic operation|25|
  
Example output:

```
{
  "result": 25
}
```

#### Max

This action is used to find the largest number from a list of numbers

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|numbers|[]number|None|True|Array of numbers to find the highest value from|None|[1, 5.5, 10, 100.5, 100]|None|None|
  
Example input:

```
{
  "numbers": [
    1,
    5.5,
    10,
    100.5,
    100
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|max|number|True|Highest value number|100.5|
  
Example output:

```
{
  "max": 100.5
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.2.4 - Updated SDK to the latest version (6.2.5)
* 1.2.3 - Updated SDK to the latest version (v6.2.2) | Address vulnerabilities
* 1.2.2 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 1.2.1 - Update to v4 Python plugin runtime
* 1.2.0 - New action Max
* 1.1.3 - Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Changed `Exception` to `PluginException` | Use input and output constants | Remove not secure eval for simple_eval
* 1.1.2 - New spec and help.md format for the Extension Library
* 1.1.1 - Update plugin tag from `utility` to `utilities` for Marketplace searchability
* 1.1.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.0 - Update Calculate action: Allow freeform input
* 0.1.0 - Initial plugin

# Links

* [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)

## References

* [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)