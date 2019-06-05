
# Syslog Forwarder

## About

This plugin allows forwarding of messages to a remote [syslog server](https://en.wikipedia.org/wiki/Syslog).

It supports:

* TCP and UDP protocols
* Facility
* Level
* Optional Hostname
* Optional Message ID
* Optional Process Name

## Actions

### Forward Message

This action is used to forward a custom syslog message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|False|Name or address where message originated from|None|
|level|string|None|True|Syslog Level|['EMERG', 'ALERT', 'CRIT', 'ERR', 'WARNING', 'NOTICE', 'INFO', 'DEBUG']|
|msg|string|None|True|Syslog message|None|
|msgid|string|None|False|Message ID|None|
|facility|string|None|True|Syslog Facility|['KERN', 'USER', 'MAIL', 'DAEMON', 'AUTH', 'SYSLOG', 'LPR', 'NEWS', 'UUCP', 'CRON', 'AUTHPRIV', 'FTP', 'LOCAL0', 'LOCAL1', 'LOCAL2', 'LOCAL3', 'LOCAL4', 'LOCAL5', 'LOCAL6', 'LOCAL7']|
|proc|string|None|False|Process name|None|

#### Output

This action does not contain any outputs.

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin requires an network accessible syslog server (IP address or domain) from Komand host, the syslog server's port, and its transport protocol.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|Syslog Host|None|
|port|integer|514|True|Syslog Port|None|
|transport|string|None|True|Protocol Transport|['TCP', 'UDP']|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Logging

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to Python v2 architecture | Support web server mode

## References

* [Syslog](https://en.wikipedia.org/wiki/Syslog)
