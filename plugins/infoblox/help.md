# Description

[Infoblox](https://www.infoblox.com) helps with managing and identifying devices connected to networks, specifically for the DNS, DHCP and IP address management (collectively, DDI)

# Key Features

* Get information about devices on the network

# Requirements

* An account from the vendor to login to services

# Supported Product Versions

* 2024-05-03

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_version|string|2.7|True|Version of the API|["1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9", "2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"]|2.7|None|None|
|credentials|credential_username_password|None|True|Infoblox username and password|None|{'username': 'user', 'password': 'pass'}|None|None|
|url|string|None|True|The URL of a running Infoblox instance (e.g. https://192.168.1.2 or https://example.infoblox.com)|None|https://192.168.1.2|None|None|

Example input:

```
{
  "api_version": 2.7,
  "credentials": {
    "password": "pass",
    "username": "user"
  },
  "url": "https://192.168.1.2"
}
```

## Technical Details

### Actions


#### Add Fixed Address

This action is used to add fixed address (a specific IP address that a DHCP server always assigns when a lease request 
comes from a particular MAC address of the client)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|FixedAddressCreate|None|True|New fixed address data|None|{'ipv4addr': '192.168.0.1', 'mac': '2c549188c9e3'}|None|None|
  
Example input:

```
{
  "address": {
    "ipv4addr": "192.168.0.1",
    "mac": "2c549188c9e3"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ref|string|True|Object Reference of a newly added fixed address|ObjectRef|
  
Example output:

```
{
  "ref": "ObjectRef"
}
```

#### Add Host

This action is used to add a new host (host has to match one of the existing authoritative networks, e.g. network FQDN 
= info.com, host name = example.info.com)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|host|HostCreate|None|True|New host data|None|{'Name': 'name', 'View': 'network_view', 'ipv4addrs': ['192.168.0.1', '192.168.0.2', '192.168.0.3']}|None|None|
  
Example input:

```
{
  "host": {
    "Name": "name",
    "View": "network_view",
    "ipv4addrs": [
      "192.168.0.1",
      "192.168.0.2",
      "192.168.0.3"
    ]
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ref|string|True|Object Reference of a newly added host|ExampleObjectRef|
  
Example output:

```
{
  "ref": "ExampleObjectRef"
}
```

#### Delete Host

This action is used to delete a host

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ref|string|None|True|Object Reference of the host to remove|None|ObjectRef|None|None|
  
Example input:

```
{
  "ref": "ObjectRef"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ref|string|True|Object Reference of the removed host|ObjectRef|
  
Example output:

```
{
  "ref": "ObjectRef"
}
```

#### Get Host

This action is used to obtain host details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ref|string|None|True|Object Reference of the host|None|ExampleObjectRef|None|None|
  
Example input:

```
{
  "ref": "ExampleObjectRef"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|host|Host|True|Host details|{'ref': 'ExampleObjectRef', 'name': 'HostName', 'ipv4addrs': ['192.168.0.1', '192.168.0.2', '192.168.0.3'], 'view': 'FQDN', 'extattrs': {'idk': 'idk'}, 'aliases': ['alias1', 'alias2']}|
  
Example output:

```
{
  "host": {
    "aliases": [
      "alias1",
      "alias2"
    ],
    "extattrs": {
      "idk": "idk"
    },
    "ipv4addrs": [
      "192.168.0.1",
      "192.168.0.2",
      "192.168.0.3"
    ],
    "name": "HostName",
    "ref": "ExampleObjectRef",
    "view": "FQDN"
  }
}
```

#### Modify Host

This action is used to update host data

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ref|string|None|True|Object Reference of the host to update|None|HostRef|None|None|
|updated_host|HostUpdate|None|False|Values of fields that should be changed|None|{'aliases': ['alias1', 'alias2'], 'extattrs': {'idk': 'idk'}, 'ipv4addrs': {'ipv4addr': '192.168.0.1', 'mac': '2c549188c9e3'}, 'ipv4addrs+': {'ipv4addr': '192.168.0.1', 'mac': '2c549188c9e3'}, 'ipv4addrs-': {'ipv4addr': '192.168.0.1', 'mac': '2c549188c9e3'}}|None|None|
  
Example input:

```
{
  "ref": "HostRef",
  "updated_host": {
    "aliases": [
      "alias1",
      "alias2"
    ],
    "extattrs": {
      "idk": "idk"
    },
    "ipv4addrs": {
      "ipv4addr": "192.168.0.1",
      "mac": "2c549188c9e3"
    },
    "ipv4addrs+": {
      "ipv4addr": "192.168.0.1",
      "mac": "2c549188c9e3"
    },
    "ipv4addrs-": {
      "ipv4addr": "192.168.0.1",
      "mac": "2c549188c9e3"
    }
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ref|string|True|Object Reference of the modified host|ObjectRef|
  
Example output:

```
{
  "ref": "ObjectRef"
}
```

#### Search by IP

This action is used to search for any object with an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip|string|None|True|IP address|None|192.168.0.1|None|None|
  
Example input:

```
{
  "ip": "192.168.0.1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|[]string|True|Object References of all objects with given IP address|["Object1", "Object2"]|
  
Example output:

```
{
  "result": [
    "Object1",
    "Object2"
  ]
}
```

#### Search by MAC

This action is used to search fixed addresses by MAC address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|mac|string|None|True|MAC address|None|2c549188c9e3|None|None|
  
Example input:

```
{
  "mac": "2c549188c9e3"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|[]IPv4Addr|True|Matched fixed addresses|[{"ipv4addr": "192.168.0.1", "mac": "2c549188c9e3"}, {"ipv4addr": "192.168.0.2", "mac": "2c549188c9e3"}]|
  
Example output:

```
{
  "result": [
    {
      "ipv4addr": "192.168.0.1",
      "mac": "2c549188c9e3"
    },
    {
      "ipv4addr": "192.168.0.2",
      "mac": "2c549188c9e3"
    }
  ]
}
```

#### Search by Name

This action is used to search hosts by name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name_pattern|string|None|True|Regular expression to match against host name|None|/^[a-z ,.'-]+$/i|None|None|
  
Example input:

```
{
  "name_pattern": "/^[a-z ,.'-]+$/i"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|[]Host|True|Matched hosts|["Host1", "Host2"]|
  
Example output:

```
{
  "result": [
    "Host1",
    "Host2"
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*

### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**FixedAddressCreate**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IPv4 Address|string|None|True|Either an IP address or a function (e.g. func:nextavailableip:10.1.1.0/24)|None|
|MAC|string|None|True|MAC address|None|
  
**IPv4AddrCreate**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IPv4 Address|string|None|True|Either an IP address or a function (e.g. func:nextavailableip:10.1.1.0/24)|None|
|MAC|string|None|False|MAC address|None|
  
**IPv4Addr**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Configure for DHCP|boolean|None|False|Configure for DHCP flag|None|
|Host|string|None|False|The name of the host|None|
|IPv4 Address|string|None|True|Either an IP address or a function (e.g. func:nextavailableip:10.1.1.0/24)|None|
|MAC|string|None|False|MAC address|None|
|Ref|string|None|True|Object Reference of the IP address|None|
  
**Host**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Aliases|[]string|None|False|Aliases associated with the host|None|
|Extattrs|object|None|False|Extensible attributes|None|
|IPv4 Addresses|[]IPv4Addr|None|True|IP addresses associated with the new host|None|
|Name|string|None|True|Name of the new host|None|
|Ref|string|None|True|Object Reference of the host|None|
|View|string|None|False|The network view this host is associated with|None|
  
**HostCreate**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IPv4 Addresses|[]IPv4AddrCreate|None|True|List of IP addresses associated with the new host|None|
|Name|string|None|True|Name of new new host|None|
|View|string|None|False|The network view this host is associated with|None|
  
**HostUpdate**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Aliases|[]string|None|False|Aliases associated with the host|None|
|Extattrs|object|None|False|Extensible attributes|None|
|IPv4 Addresses|[]IPv4AddrCreate|None|False|New list of IP addresses associated with the new host (overrides the original list)|None|
|Added IPv4 Addresses|[]IPv4AddrCreate|None|False|IP addresses added to the list associated with the new host|None|
|Removed IPv4 Addresses|[]IPv4AddrCreate|None|False|IP addresses removed from the list associated with the new host|None|


## Troubleshooting

Infoblox instance is required for this plugin. Infoblox does not provide a testing environment, but they do provide a properly configured VMWare virtual machine (the default credentials are `admin:infoblox`). Details can be found [here](https://www.infoblox.com/infoblox-download-center/).

When adding a new host make sure that a corresponding network is already created (otherwise you will get `The action is not allowed. A parent was not found.`). More details can be found in [this post](https://community.infoblox.com/t5/API-Integration/API-testing-environment-TestDrive-not-working/m-p/14047#M1765).

[Infoblox Community](https://community.infoblox.com/) provides a lot of answers on different topics, make sure to check it if you run into any problems.

# Version History

* 1.1.0 - `Connection` - Add SSL verify input | Update SDK from `komand` to `insightconnect_plugin_runtime`
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [Infoblox API](https://www.infoblox.com/wp-content/uploads/infoblox-deployment-infoblox-rest-api.pdf)

## References

* [REST API examples](https://community.infoblox.com/t5/API-Integration/The-definitive-list-of-REST-examples/td-p/1214)