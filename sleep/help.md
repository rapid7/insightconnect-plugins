# Description

Sleep suspends execution for an interval of time expressed in seconds.
It's used to create artificial delays in a workflow when desirable.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Sleep

This action is used to suspend execution for an interval of time.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|None|False|Interval of time in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|slept|integer|False|Time spent asleep|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Python Time Sleep](https://docs.python.org/3/library/time.html#time.sleep)

