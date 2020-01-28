# Description

The [Tcpdump](http://www.tcpdump.org) plugin is used to parse the contents of a packet capture (PCAP) file.

# Key Features

* Parse and return the contents of a PCAP file.

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Read PCAP

This action is used to run Tcpdump on a user supplied PCAP file and return the output as `bytes` and a `string array` of packets.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|None|False|Berkeley Packet Filter E.g. TCP and port 22|None|
|options|string|None|False|Tcpdump Flags and Options E.g. -n -c 10 -s 96. -r is implied|None|
|pcap|bytes|None|True|Base64 encoded PCAP file|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dump_contents|[]string|False|Traffic Dump as Array|
|dump_file|bytes|False|Traffic Dump as File|
|stderr|string|False|Tcpdump Standard Error|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.0 - Updated spec and help.md format for the Hub, spec description changes
* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Update to use the `komand/python-3-slim-plugin:2` Docker image to reduce plugin size
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Tcpdump](http://www.tcpdump.org)
* [Tcpdump manual](http://www.tcpdump.org/tcpdump_man.html)

