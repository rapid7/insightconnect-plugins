# Description

The Pork Knocking plugin knocks the specified ports on a host and optionally supports a payload.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

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

This action does not contain any outputs.

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Port Knocking](https://en.wikipedia.org/wiki/Port_knocking)

