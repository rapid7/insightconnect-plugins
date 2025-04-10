# Description

The Subnet plugin takes input as a network in CIDR notation and returns useful information, such as the number of hosts, the ID, host address range, and broadcast address

# Key Features

* Returns network information about CIDR

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-10-09

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Calculate

This action is used to return Subnet information for IP and Netmask

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cidr|string|None|True|Network in CIDR notation, E.g. 198.51.100.0/24|None|198.51.100.0/24|None|None|
  
Example input:

```
{
  "cidr": "198.51.100.0/24"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|binary_netmask|string|False|Binary netmask|11111111111111111111111100000000|
|broadcast|string|False|Broadcast address|192.168.1.255|
|cidr|string|False|CIDR notation|/24|
|host_range|string|False|Host address range|192.168.1.1 - 192.168.1.254|
|hosts|integer|False|Number of hosts|254|
|ip|string|False|IP address|192.168.1.1|
|ip_class|string|False|IP class|C|
|netmask|string|False|Subnet mask|255.255.255.0|
|subnet_id|string|False|Subnet ID|192.168.1.0|
|subnets|integer|False|Number of subnetworks|1|
|wildcard|string|False|Wildcard mask|0.0.0.255|
  
Example output:

```
{
  "binary_netmask": 11111111111111111111111100000000,
  "broadcast": "192.168.1.255",
  "cidr": "/24",
  "host_range": "192.168.1.1 - 192.168.1.254",
  "hosts": 254,
  "ip": "192.168.1.1",
  "ip_class": "C",
  "netmask": "255.255.255.0",
  "subnet_id": "192.168.1.0",
  "subnets": 1,
  "wildcard": "0.0.0.255"
}
```

#### Check Address in Subnet

This action is used to determine if the provided IP address is in the Subnet

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|The IP address|None|198.51.100.100|None|None|
|subnet|string|None|True|The Subnet in CIDR notation or Netmask|None|198.51.100.0/24|None|None|
  
Example input:

```
{
  "ip_address": "198.51.100.100",
  "subnet": "198.51.100.0/24"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|True|Whether the IP address was found|True|
  
Example output:

```
{
  "found": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* The number of hosts per network does not include the ID and broadcast address. However, the number of network does include the all-ones and all-zeros network.

# Version History

* 2.0.3 - Updated SDK to the latest version (6.3.3)
* 2.0.2 - Updated SDK to the latest version (6.2.5)
* 2.0.1 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 2.0.0 - Add new action Check Address in Subnet | Code refactor
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Subnetwork](https://en.wikipedia.org/wiki/Subnetwork)
* [Python IPCalc](https://github.com/tehmaze/ipcalc)

## References

* [Subnetwork](https://en.wikipedia.org/wiki/Subnetwork)
* [Python IPCalc](https://github.com/tehmaze/ipcalc)