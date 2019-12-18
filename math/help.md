# Description

This plugin allows basic arithmetic functions to be performed.

# Key Features

* Math operations module and exponents
* Math Division and multiplication, addition and subtraction

# Requirements

_This plugin does not contain any requirements_

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Calculate

This action is used to run a calculation.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|equation|string|None|True|Equation to calculate. Uses Python arithmetic operators (+, -, /, *, **, %)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|number|False|Result of the arithmetic operation|

Example output:

```

{
  "result": 25.0
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.2 - New spec and help.md format for the Hub
* 1.1.1 - Update plugin tag from `utility` to `utilities` for Marketplace searchability
* 1.1.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.0 - Update Calculate action: Allow freeform input
* 0.1.0 - Initial plugin

# Links

## References

* [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)

