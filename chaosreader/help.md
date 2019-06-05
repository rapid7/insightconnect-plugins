
# Chaosreader

## About

[Chaosreader](http://chaosreader.sourceforge.net/) is a tool to trace sessions and fetch application data from snoop or tcpdump logs.
This plugin runs the Chaosreader tool directly.

## Actions

### Run

This action is used to run Chaosreader on a given capture (PCAP or Snoop) file.
Session details are provided in the output, as well as the extracted files in a `bytes array`.
Specific file traffic/file types can be excluded.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|exclude|string|None|False|Exclude traffic/files|['None', 'Info', 'Raw', 'TCP', 'UDP', 'ICMP']|
|dump|bytes|None|True|Base64 encoded PCAP or snoop file|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|[]bytes|False|Extracted files|
|tcp_count|[]count|False|List of TCP ports and their count|
|proto_count|[]count|False|List of IP protocols and their count|
|sessions|[]string|False|List of sessions found in traffic|
|ethernet_count|[]count|False|List of ethernet types and their count|
|udp_count|[]count|False|List of UDP ports and their count|
|ip_count|[]count|False|List of IPs and their count|
|file_count|integer|False|Number of files extracted|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Packet analysis
* File carving
* Forensics

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.1 - Fix issue where run action was excluded from plugin on build

## References

* [Chaosreader](http://chaosreader.sourceforge.net/)
