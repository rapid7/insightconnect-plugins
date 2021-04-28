# Description

This plugin allows basic arithmetic functions to be performed.

# Key Features

* Math operations module and exponents
* Math Division and multiplication, addition and subtraction

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Max

This action is used to find the largest number from a list of numbers.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|numbers|[]number|None|True|Array of numbers to find the highest value from|None|[1, 5.5, 10, 100.5, 100]|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|max|number|True|Highest value number|

Example output:

```
{
  "max": 100.5
}
```

#### Calculate

This action is used to run a calculation.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|equation|string|None|True|Equation to calculate. Uses Python arithmetic operators (+, -, /, *, **, %)|None|((3**2) * 3) + 3 - 5|

Example input:

```
{
  "equation": "((3**2) * 3) + 3 - 5"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|number|True|Result of the arithmetic operation|

Example output:

```

{
  "result": 25.0
}

```

### Triggers

_This plugin does not contain any triggers._

### Tasks

_This plugin does not contain any tasks._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.1 - Update to v4 Python plugin runtime
* 1.2.0 - New action Max
* 1.1.3 - Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Changed `Exception` to `PluginException` | Use input and output constants | Remove not secure eval for simple_eval
* 1.1.2 - New spec and help.md format for the Extension Library
* 1.1.1 - Update plugin tag from `utility` to `utilities` for Marketplace searchability
* 1.1.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.0 - Update Calculate action: Allow freeform input
* 0.1.0 - Initial plugin

# Links

## References

* [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)

