
# Math

## About

This plugin allows basic arithmetic functions to be performed.

## Actions

### Calculate

This action is used to run a calculation.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|equation|string|None|True|Equation to calculate. Uses Python arithmetic operators (+, -, /, *, **, %)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|number|False|Result of the arithmetic operation|

Example output:

```

{
  "result": 25.0
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Calculating differences in timestamps
* General utility

## Versions

* 0.1.0 - Initial plugin
* 1.0.0 - Update Calculate action: Allow freeform input
* 1.1.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.1.1 - Update plugin tag from `utility` to `utilities` for Marketplace searchability

## References

* [Arithmetic](https://en.wikipedia.org/wiki/Arithmetic)
