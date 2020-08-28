# Description

[Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html) is your administrative nerve center for managing critical Cisco network security solutions.
The Cisco Firepower Management Center InsightConnect plugin allows you to create a new block URL policy.

# Key Features

* Create block URL policy

# Requirements

* Cisco Firepower Management Center server name
* Cisco Firepower Management Center username and password

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|server|string|None|False|Enter the address for the server|None|https://www.example.com|
|username_and_password|credential_username_password|None|True|Cisco username and password|None|{"username":"user1", "password":"mypassword"}|
|verify_ssl|boolean|True|False|Check the server's SSL certificate|None|True|

Example input:

```
{
  "server": "https://www.example.com",
  "username_and_password": {
    "username": "user1",
    "password": "mypassword"
  },
  "verify_ssl": true
}
```

## Technical Details

### Actions

#### Create Address Object

This action creates a new address object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|IP address, CIDR IP address, or domain name to assign to the Address Object|None|example.com|
|address_object|string|None|False|Name of the Address Object, defaults to the value address in the address field if no name is given|None|MaliciousHost|
|skip_private_address|boolean|None|True|If set to true, any addresses that are defined in the RFC1918 space will not be blocked. e.g. 10/8, 172.16/12, 192.168/16|None|True|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be blocked. This can include IP addresses, CIDR IP addresses, and domains|None|["198.51.100.100", "192.0.2.0/24", "example.com"]|

Example input:

```
{
  "address": "example.com",
  "address_object": "MaliciousHost",
  "skip_private_address": true,
  "whitelist": [
    "198.51.100.100",
    "192.0.2.0/24",
    "example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_object|address_object|False|Returns information about the newly created address object|

Example output:

```
```

#### Block URL Policy

This action is used to create a new block URL policy.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access_policy|string|None|True|Access Policy name|None|None|
|rule_name|string|None|True|Name for the Access Rule to be created|None|None|
|url_objects|[]url_object|None|True|URL objects to block|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
{
    "success": True
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html)

