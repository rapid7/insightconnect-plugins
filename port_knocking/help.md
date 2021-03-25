# Description

The Pork Knocking plugin knocks the specified ports on a host and optionally supports a payload.

Port knocking is a method of externally opening ports on a firewall by generating a connection attempt on a set of 
specified closed ports. Once a correct sequence of connection attempts is received, the firewall rules are 
dynamically modified to allow the host which sent the connection attempts to connect over specific port(s). 
A variant called single packet authorization exists, where only a single "knock" is needed, consisting of an 
encrypted packet.

# Key Features

* Port knock a sequence of ports

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Knock

This action is used to port knock a given host (IP address or domain).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|IP address or hostname to knock|None|
|ports|[]string|None|True|E.g. 7000/tcp, 8000/udp|None|

##### Output

_This action does not contain any outputs._

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Port Knocking](https://en.wikipedia.org/wiki/Port_knocking)

