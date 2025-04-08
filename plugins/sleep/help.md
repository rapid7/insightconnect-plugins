# Description

Sleep allows Rapid7 InsightConnect users to suspend workflow execution for a specified period of time. Popular uses are to avoid rate limiting by a service or to wait for processing by a service to complete

# Key Features

* Suspend workflow execution for a given number of seconds

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-10-09

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Sleep

This action is used to suspend execution for an interval of time

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|None|False|Interval of time in seconds|None|10|None|None|
  
Example input:

```
{
  "interval": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|slept|integer|False|Time spent asleep|10|
  
Example output:

```
{
  "slept": 10
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

* 1.0.5 - Updated SDK to the latest version (6.3.2)
* 1.0.4 - Updated SDK to the latest version (6.2.5)
* 1.0.3 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 1.0.2 - Use input and output constants | Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Add interval input validation
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Python Time Sleep](https://docs.python.org/3/library/time.html#time.sleep)

## References

* [Python Time Sleep](https://docs.python.org/3/library/time.html#time.sleep)