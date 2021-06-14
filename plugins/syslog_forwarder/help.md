# Description

This plugin allows forwarding of messages to a remote [syslog server](https://en.wikipedia.org/wiki/Syslog).

It supports:

* TCP and UDP protocols
* Facility
* Level
* Optional Hostname
* Optional Message ID
* Optional Process Name

# Key Features

* Forward a custom syslog message

# Requirements

* A remote syslog server

# Documentation

## Setup

This plugin requires the IP address or hostname, port number, and transport protocol for a syslog server that is accessible from the Orchestrator.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|Syslog Host|None|
|port|integer|514|True|Syslog Port|None|
|transport|string|None|True|Protocol Transport|['TCP', 'UDP']|

## Technical Details

### Actions

#### Forward Message

This action is used to forward a custom syslog message.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|False|Name or address where message originated from|None|
|level|string|None|True|Syslog Level|['EMERG', 'ALERT', 'CRIT', 'ERR', 'WARNING', 'NOTICE', 'INFO', 'DEBUG']|
|msg|string|None|True|Syslog message|None|
|msgid|string|None|False|Message ID|None|
|facility|string|None|True|Syslog Facility|['KERN', 'USER', 'MAIL', 'DAEMON', 'AUTH', 'SYSLOG', 'LPR', 'NEWS', 'UUCP', 'CRON', 'AUTHPRIV', 'FTP', 'LOCAL0', 'LOCAL1', 'LOCAL2', 'LOCAL3', 'LOCAL4', 'LOCAL5', 'LOCAL6', 'LOCAL7']|
|proc|string|None|False|Process name|None|

##### Output

_This action does not contain any outputs._

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to Python v2 architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Syslog](https://en.wikipedia.org/wiki/Syslog)

