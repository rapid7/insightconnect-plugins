# Description

[Tcpdump](http://www.tcpdump.org) is a powerful command-line packet analyzer. This plugins run the Tcpdump packet tracer on a user supplied PCAP.

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

#### Read PCAP

This action is used to run Tcpdump on a user supplied PCAP file and return the output as `bytes` and a `string array` of packets.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|None|False|Berkely Packet Filter E.g. tcp and port 22|None|
|pcap|bytes|None|True|Base64 encoded PCAP file|None|
|options|string|None|False|Tcpdump Flags and Options E.g. -n -c 10 -s 96. -r is implied|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dump_contents|[]string|False|Traffic Dump as Array|
|dump_file|bytes|False|Traffic Dump as File|
|stderr|string|False|Tcpdump Standard Error|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - Update to use the `komand/python-3-slim-plugin:2` Docker image to reduce plugin size
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Tcpdump](http://www.tcpdump.org)
* [Tcpdump manual](http://www.tcpdump.org/tcpdump_man.html)

