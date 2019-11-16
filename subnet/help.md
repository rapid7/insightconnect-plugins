# Description

The Subnet plugin takes input as a network in CIDR notation and returns useful information, such as the number of hosts, the ID, host address range, and broadcast address.

# Key Features

* Returns network information about CIDR

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Calculate

This action is used to returns network information information for IP and Netmask.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cidr|string|None|True|Network in CIDR Notation, E.g. 192.168.1.1/24|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|subnets|integer|False|None|
|ip_class|string|False|None|
|subnet_id|string|False|None|
|ip|string|False|None|
|host_range|string|False|None|
|broadcast|string|False|None|
|binary_netmask|string|False|None|
|netmask|string|False|None|
|hosts|integer|False|None|
|wildcard|string|False|None|
|cidr|string|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The number of hosts per network does not include the ID and broadcast address.
However, the number of network does include the all-ones and all-zeros network.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Subnetwork](https://en.wikipedia.org/wiki/Subnetwork)
* [Python IPCalc](https://github.com/tehmaze/ipcalc)

