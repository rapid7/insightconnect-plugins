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

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin requires an network accessible syslog server (IP address or domain) from Komand host, the syslog server's port, and its transport protocol.

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

This action does not contain any outputs.

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to Python v2 architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Syslog](https://en.wikipedia.org/wiki/Syslog)

