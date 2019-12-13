# Description

[Infoblox](https://www.infoblox.com) helps with managing and identifying devices connected to networks, specifically for the DNS, DHCP and IP address management (collectively, DDI).

This plugin utilizes the [Infoblox API](https://www.infoblox.com/wp-content/uploads/infoblox-deployment-infoblox-rest-api.pdf).

# Key Features

* Get information about devices on the network

# Requirements

* An account from the vendor to login to services

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Infoblox username and password|None|
|url|string|None|True|The URL of a running Infoblox instance (e.g. https://192.168.1.2 or https://example.infoblox.com)|None|
|api_version|string|2.7|True|Version of the API|['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '2.0', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7']|

## Technical Details

### Actions

#### Delete Host

This action is used to delete a host.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|_ref|string|None|True|Object Reference of the host to remove|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|_ref|string|True|Object Reference of the removed host|

Example output:

```
{
  "_ref": "record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLnRlc3QxMTE:test111.info.com/default"
}
```

#### Search by IP

This action is used to search for any object with an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip|string|None|True|IP address|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]string|True|Object References of all objects with given IP address|

Example output:

```
{
  "result": [
    "fixedaddress/ZG5zLmZpeGVkX2FkZHJlc3MkMTAuMTAuMTAuNS4wLi4:10.10.10.5/default"
  ]
}
```

#### Get Host

This action is used to obtain host details.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|_ref|string|None|True|Object Reference of the host|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|host|Host|True|Host details|

Example output:

```
{
  "host": {
    "_ref": "record:host/ZG5zLmhvc3QkLm5vbl9ETlNfaG9zdF9yb290LjAuMTUzMjY4OTgzMDkxMC5jb20uZXhhbXBsZS5hZG1pbg:admin.example.com/%20",
    "aliases": [
      "testing"
    ],
    "extattrs": {
      "Site": {
        "value": "East"
      }
    },
    "ipv4addrs": [
      {
        "_ref": "record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQubm9uX0ROU19ob3N0X3Jvb3QuMC4xNTMyNjg5ODMwOTEwLmNvbS5leGFtcGxlLmFkbWluLjEwLjEwLjEwLjc1Lg:10.10.10.75/admin.example.com/%20",
        "configure_for_dhcp": false,
        "host": "admin.example.com",
        "ipv4addr": "10.10.10.75"
      },
      {
        "_ref": "record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQubm9uX0ROU19ob3N0X3Jvb3QuMC4xNTMyNjg5ODMwOTEwLmNvbS5leGFtcGxlLmFkbWluLjEwLjEwLjEwLjc2Lg:10.10.10.76/admin.example.com/%20",
        "configure_for_dhcp": false,
        "host": "admin.example.com",
        "ipv4addr": "10.10.10.76"
      }
    ],
    "name": "admin.example.com",
    "view": " "
  }
}
```

#### Add Host

This action is used to add a new host (host has to match one of the existing authoritative networks, e.g. network fqdn = info.com, host name = example.info.com).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|HostCreate|None|True|New host data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|_ref|string|True|Object Reference of a newly added host|

Example output:

```
{
  "_ref": "record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLmFieA:abx.info.com/default"
}
```

#### Modify Host

This action is used to update host data.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|_ref|string|None|True|Object Reference of the host to update|None|
|updated_host|HostUpdate|None|False|Values of fields that should be changed|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|_ref|string|True|Object Reference of the modified host|

Example output:

```
{
  "_ref": "record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLnRlc3Q1:test5.info.com/default"
}
```

#### Search by MAC

This action is used to search fixed addresses by MAC address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|mac|string|None|True|MAC address|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]IPv4Addr|True|Matched fixed addresses|

Example output:

```
{
  "result": [
    {
      "_ref": "fixedaddress/ZG5zLmZpeGVkX2FkZHJlc3MkMTAuMTAuMTAuMi4wLi4:10.10.10.2/default",
      "ipv4addr": "10.10.10.2",
      "mac": "aa:bb:cc:11:22:33",
      "network_view": "default"
    }
  ]
}
```

#### Search by Name

This action is used to search hosts by name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name_pattern|string|None|True|Regular expression to match against host name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]Host|True|Matched hosts|

Example output:

```
{
  "result": [
    {
      "_ref": "record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLmFieA:abx.info.com/default",
      "ipv4addrs": [
        {
          "_ref": "record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQuX2RlZmF1bHQuY29tLmluZm8uYWJ4LjEwLjEwLjEwLjUyLg:10.10.10.52/abx.info.com/default",
          "configure_for_dhcp": false,
          "host": "abx.info.com",
          "ipv4addr": "10.10.10.52"
        }
      ],
      "name": "abx.info.com",
      "view": "default"
    },
    {
      "_ref": "record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLnRlc3Qz:test3.info.com/default",
      "ipv4addrs": [
        {
          "_ref": "record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQuX2RlZmF1bHQuY29tLmluZm8udGVzdDMuMTAuMTAuMTAuMjIu:10.10.10.22/test3.info.com/default",
          "configure_for_dhcp": true,
          "host": "test3.info.com",
          "ipv4addr": "10.10.10.22",
          "mac": "11:22:33:11:22:33"
        }
      ],
      "name": "test3.info.com",
      "view": "default"
    },
    {
      "_ref": "record:host/ZG5zLmhvc3QkLl9kZWZhdWx0LmNvbS5pbmZvLnRlc3Q1:test5.info.com/default",
      "ipv4addrs": [
        {
          "_ref": "record:host_ipv4addr/ZG5zLmhvc3RfYWRkcmVzcyQuX2RlZmF1bHQuY29tLmluZm8udGVzdDUuMTAuMTAuMTAuNzUu:10.10.10.75/test5.info.com/default",
          "configure_for_dhcp": false,
          "host": "test5.info.com",
          "ipv4addr": "10.10.10.75"
        }
      ],
      "name": "test5.info.com",
      "view": "default"
    }
  ]
}
```

#### Add Fixed Address

This action is used to add a fixed address (a specific IP address that a DHCP server always assigns when a lease request comes from a particular MAC address of the client).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|FixedAddressCreate|None|True|New fixed address data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|_ref|string|True|Object Reference of a newly added fixed address|

Example output:

```
{
  "_ref": "fixedaddress/ZG5zLmZpeGVkX2FkZHJlc3MkMTAuMTAuMTAuOC4wLi4:10.10.10.8/default"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Infoblox instance is required for this plugin. Infoblox does not provide a testing environment, but they do provide a properly configured VMWare virtual machine (the default credentials are `admin:infoblox`). Details can be found [here](https://www.infoblox.com/infoblox-download-center/).

When adding a new host make sure that a corresponding network is already created (otherwise you will get `The action is not allowed. A parent was not found.`). More details can be found in [this post](https://community.infoblox.com/t5/API-Integration/API-testing-environment-TestDrive-not-working/m-p/14047#M1765).

[Infoblox Community](https://community.infoblox.com/) provides a lot of answers on different topics, make sure to check it if you run into any problems.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [REST API examples](https://community.infoblox.com/t5/API-Integration/The-definitive-list-of-REST-examples/td-p/1214)

