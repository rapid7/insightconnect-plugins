# Description

[Dumbno](https://github.com/ncsa/dumbno) is a free and open source flow shunting software for Arista switches using the EOS API. Using this plugin will allow users to add ACLs to switches

# Key Features

* Add ACL switch

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|Dumbno Host|None|
|port|integer|9000|True|Dumbno Port|None|

## Technical Details

### Actions

#### Add ACL

This action is used to add an ACL to an Arista switch.

##### Input

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

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|None|

The action returns `boolean` on whether the add ACL request was successfully executed on the system.

```

{ 'success': false },

```

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

* [Dumbno](https://github.com/ncsa/dumbno)

