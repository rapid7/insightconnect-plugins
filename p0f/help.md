
# p0f

## About

[P0f](http://lcamtuf.coredump.cx/p0f3/) is a Free and Open Source passive OS fingerprinting tool.
The p0f plugin runs the tool directly.

## Actions

### Run

This action is used to run p0f on a PCAP.
It returns the traffic details including p0f's detection of the operating systems used for each host in a communication.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|True|Base64 encoded PCAP|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|traffic|[]string|False|Traffic details|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Host fingerprinting
* OS detection

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.1 - Fix issue where run action was excluded from plugin on build

## References

* [p0f](http://lcamtuf.coredump.cx/p0f3/)
