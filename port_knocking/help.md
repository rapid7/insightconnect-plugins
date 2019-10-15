
# Port Knocking

## About

The Pork Knocking plugin knocks the specified ports on a host and optionally supports a payload.

## Actions

### Knock

This action is used to port knock a given host (IP address or domain).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|IP address or hostname to knock|None|
|ports|[]string|None|True|E.g. 7000/tcp, 8000/udp|None|

#### Output

This action does not contain any outputs.

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Authentication
* Port checking

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode

## References

* [Port Knocking](https://en.wikipedia.org/wiki/Port_knocking)
