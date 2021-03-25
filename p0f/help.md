# Description

[p0f](http://lcamtuf.coredump.cx/p0f3/) is a free and open source passive OS fingerprinting tool for analyzing PCAP
files.
The p0f plugin runs the tool directly.

# Key Features

* Detection of operating systems from PCAP

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Run

This action is used to run p0f on a PCAP.
It returns the traffic details including p0f's detection of the operating systems used for each host in a communication.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|True|Base64 encoded PCAP|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|traffic|[]string|False|Traffic details|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Fix issue where run action was excluded from plugin on build
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [p0f](http://lcamtuf.coredump.cx/p0f3/)
