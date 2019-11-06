# Description

[P0f](http://lcamtuf.coredump.cx/p0f3/) is a Free and Open Source passive OS fingerprinting tool.
The p0f plugin runs the tool directly.

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

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - Fix issue where run action was excluded from plugin on build
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [p0f](http://lcamtuf.coredump.cx/p0f3/)

