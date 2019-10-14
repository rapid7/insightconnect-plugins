
# Syslog Listener

## About

This plugin allows for triggering events via [Syslog](https://en.wikipedia.org/wiki/Syslog) by starting a listener on a port.

## Actions

This plugin does not contain any actions.

## Triggers

### Listen for Syslog Messages

This trigger is used to listen for syslog messages.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|endpoint|string|0.0.0.0|True|IP address of the Komand host to listen on. 0.0.0.0 to listen on the all address|None|
|filter|string|None|False|Regex Message filter, e.g. '.*hello.*'|None|
|facility|string|None|False|Syslog Facility Filter|['None', 'KERN', 'USER', 'MAIL', 'DAEMON', 'AUTH', 'SYSLOG', 'LPR', 'NEWS', 'UUCP', 'CRON', 'AUTHPRIV', 'FTP', 'LOCAL0', 'LOCAL1', 'LOCAL2', 'LOCAL3', 'LOCAL4', 'LOCAL5', 'LOCAL6', 'LOCAL7']|
|port|integer|5114|True|Syslog Port. Only one trigger can listen per port. Should be > 1024|None|
|transport|string|None|True|Protocol Transport|['TCP', 'UDP']|
|level|string|None|False|Syslog Level Filter|['None', 'EMERG', 'ALERT', 'CRIT', 'ERR', 'WARNING', 'NOTICE', 'INFO', 'DEBUG']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|host|string|False|Name or address where message originated from|
|level|string|False|Syslog Level|
|msg|string|False|Syslog message|
|msgid|string|False|Message ID|
|facility|string|False|Syslog Facility|
|proc|string|False|Process name|

## Connection

This plugin does not contain a connection.

## Troubleshooting

Test the service by sending a syslog message to the Komand host.

```

logger -p auth.notice "Test Komand Syslog Trigger" -P 5114 -d -n <Komand Host>

```

## Workflows

Examples:

* Logging

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 0.1.2 - Endpoint addition to trigger
* 1.2.0 - Support web server mode | Major version bump for validation
* 1.2.1 - Updating to Go SDK 2.6.4
* 1.2.2 - Regenerate with latest Go SDK to solve bug with triggers

## References

* [Syslog](https://en.wikipedia.org/wiki/Syslog)
