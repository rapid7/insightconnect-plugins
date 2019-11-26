# Description

Sleep allows Rapid7 InsightConnect users to suspend workflow execution for a specified period of time.
Popular uses are to avoid rate limiting by a service or to wait for processing by a service to complete.

# Key Features

* Suspend workflow execution

# Requirements

_This plugin does not contain any requirements._

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

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Python Time Sleep](https://docs.python.org/3/library/time.html#time.sleep)

