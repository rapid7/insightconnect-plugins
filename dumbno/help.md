
# Dumbno

## About

[Dumbno](https://github.com/ncsa/dumbno) is free and open source flow shunting software for Arista switches using EOS API.
This plugin utilizes the Dumbno client library.

## Actions

### Add ACL

This action is used to add an ACL to an Arista switch.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|srcip|string|None|False|None|None|
|dport|string|None|False|None|None|
|dstip|string|None|False|None|None|
|sport|string|None|False|None|None|
|proto|string|None|False|None|None|

The following inputs are available:

* Source IP
* Destination IP
* Protocol
* Source Port
* Destination Port

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|None|

The action returns `boolean` on whether the add ACL request was successfully executed on the system.

```

{ 'success': false },

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin requires the Dumbno host address and the port it's running on.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|Dumbno Host|None|
|port|integer|9000|True|Dumbno Port|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* IP blocking

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode

## References

* [Dumbno](https://github.com/ncsa/dumbno)
