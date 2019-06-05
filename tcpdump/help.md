
# Tcpdump

## About

[Tcpdump](http://www.tcpdump.org) is a powerful command-line packet analyzer. This plugins run the Tcpdump packet tracer on a user supplied PCAP.

## Actions

### Read PCAP

This action is used to run Tcpdump on a user supplied PCAP file and return the output as `bytes` and a `string array` of packets.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|None|False|Berkely Packet Filter E.g. tcp and port 22|None|
|pcap|bytes|None|True|Base64 encoded PCAP file|None|
|options|string|None|False|Tcpdump Flags and Options E.g. -n -c 10 -s 96. -r is implied|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dump_contents|[]string|False|Traffic Dump as Array|
|dump_file|bytes|False|Traffic Dump as File|
|stderr|string|False|Tcpdump Standard Error|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Packet analysis

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.1 - Update to use the `komand/python-3-slim-plugin:2` Docker image to reduce plugin size

## References

* [Tcpdump](http://www.tcpdump.org)
* [Tcpdump manual](http://www.tcpdump.org/tcpdump_man.html)
