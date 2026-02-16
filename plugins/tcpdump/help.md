# Description

The Tcpdump plugin is used to read contents of a PCAP

# Key Features

* Parse and return the contents of a PCAP file

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* Tcpdump 4.99.5

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Read PCAP

This action is used to read contents from a PCAP file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|Berkeley Packet Filter|None|TCP and port 22|None|None|
|options|string|None|False|Tcpdump Flags and Options (must be space-separated)|None|-n -r -c 10 -s 96|None|None|
|pcap|bytes|None|True|Base64 encoded PCAP file|None|UENBUCoAAE0AAAAABAAAAA==|None|None|
  
Example input:

```
{
  "filter": "TCP and port 22",
  "options": "-n -r -c 10 -s 96",
  "pcap": "UENBUCoAAE0AAAAABAAAAA=="
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|dump_contents|[]string|False|Traffic Dump as Array|["12:34:56.789012 IP 192.168.1.1.22 > 192.168.1.2.54321: S", "12:34:56.790123 IP 192.168.1.2.54321 > 192.168.1.1.22: S."]|
|dump_file|bytes|False|Traffic Dump as File|UENBUCoAAE0AAAAABAAAAA==|
|stderr|string|False|Tcpdump Standard Error|tcpdump: listening on eth0, link-type EN10MB (Ethernet), snapshot length 65535 bytes|
  
Example output:

```
{
  "dump_contents": [
    "12:34:56.789012 IP 192.168.1.1.22 > 192.168.1.2.54321: S",
    "12:34:56.790123 IP 192.168.1.2.54321 > 192.168.1.1.22: S."
  ],
  "dump_file": "UENBUCoAAE0AAAAABAAAAA==",
  "stderr": "tcpdump: listening on eth0, link-type EN10MB (Ethernet), snapshot length 65535 bytes"
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

* 2.0.0 - BREAKING CHANGE: Options must now be space-separated (e.g., use `-n -r -c 10` instead of `-nrc10`) | Security: Removed write/capture-related flags from whitelist (-w, -i, -C, -G, -W, -I, -D, -K, -p, -U, -Z) as plugin only supports reading PCAP files
* 1.1.1 - Refreshed the plugin | Updated SDK to the latest version (6.4.3)
* 1.1.0 - Updated spec and help.md format for the Extension Library, spec description changes
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Update to use the `komand/python-3-slim-plugin:2` Docker image to reduce plugin size
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Tcpdump](http://www.tcpdump.org)
* [Tcpdump manual](http://www.tcpdump.org/tcpdump_man.html)

## References

* [Tcpdump](http://www.tcpdump.org)
* [Tcpdump manual](http://www.tcpdump.org/tcpdump_man.html)