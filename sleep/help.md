
# Sleep

## About

Sleep suspends execution for an interval of time expressed in seconds.
It's used to create artificial delays in a workflow when desirable.

## Actions

### Sleep

This action is used to suspend execution for an interval of time.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|None|False|Interval of time in seconds|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|slept|integer|False|Time spent asleep|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Flow control

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode

## References

* [Python Time Sleep](https://docs.python.org/3/library/time.html#time.sleep)
