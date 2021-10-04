# Description

The Subnet plugin takes input as a network in CIDR notation and returns useful information, such as the number of hosts, the ID, host address range, and broadcast address.

# Key Features

* Returns network information about CIDR

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Check Address in Subnet

This action is used to determine if the provided IP address is in the subnet.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|The IP address|None|198.51.100.100|
|subnet|string|None|True|The subnet in CIDR notation or Netmask|None|198.51.100.0/24|

Example input:

```
{
  "ip_address": "198.51.100.100",
  "subnet": "198.51.100.0/24"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|Whether the IP address was found|

Example output:

```
{
  "found": true
}
```

#### Calculate

This action is used to return network information for IP and Netmask.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cidr|string|None|True|Network in CIDR notation, E.g. 198.51.100.0/24|None|198.51.100.0/24|

Example input:

```
{
  "cidr": "198.51.100.0/24"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|binary_netmask|string|False|Binary netmask|
|broadcast|string|False|Broadcast address|
|cidr|string|False|CIDR notation|
|host_range|string|False|Host address range|
|hosts|integer|False|Number of hosts|
|ip|string|False|IP address|
|ip_class|string|False|IP class|
|netmask|string|False|Subnet mask|
|subnet_id|string|False|Subnet ID|
|subnets|integer|False|Number of subnetworks|
|wildcard|string|False|Wildcard mask|

Example output:

```
{
  "wildcard": "0.0.0.255",
  "binary_netmask": "11111111111111111111111100000000",
  "host_range": "192.168.1.1 - 192.168.1.254",
  "ip": "192.168.1.1",
  "subnet_id": "192.168.1.0",
  "subnets": 1,
  "broadcast": "192.168.1.255",
  "cidr": "/24",
  "hosts": 254,
  "ip_class": "C",
  "netmask": "255.255.255.0"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The number of hosts per network does not include the ID and broadcast address.
However, the number of network does include the all-ones and all-zeros network.

# Version History

* 2.0.0 - Add new action Check Address in Subnet | Code refactor
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Subnetwork](https://en.wikipedia.org/wiki/Subnetwork)
* [Python IPCalc](https://github.com/tehmaze/ipcalc)

