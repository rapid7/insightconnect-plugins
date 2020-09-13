# Description

[Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html) is your administrative nerve center for managing critical Cisco network security solutions.
The Cisco Firepower Management Center InsightConnect plugin allows you to create a new block URL policy.

# Key Features

* Create block URL policy
* Create address object
* Delete address object

# Requirements

* Cisco Firepower Management Center server name
* Cisco Firepower Management Center username and password

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|Global|False|Cisco FirePower Management Centre Domain|None|Global|
|port|integer|443|False|The port number for provided host|None|443|
|server|string|None|False|Enter the address for the server|None|www.example.com|
|ssl_verify|boolean|True|False|Validate TLS / SSL certificate|None|True|
|username_and_password|credential_username_password|None|True|Cisco username and password|None|{"username":"user1", "password":"mypassword"}|

Example input:

```
{
  "domain": "Global",
  "port": 443,
  "server": "www.example.com",
  "ssl_verify": true,
  "username_and_password": {
    "username": "user1",
    "password": "mypassword"
  }
}
```

## Technical Details

### Actions

#### Check If Address in Group

This action checks if provided Address Object name or host exists in the Address Group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|Address Object name, or IP, CIDR, or domain name when Enable Search is on|None|MaliciousHost|
|enable_search|boolean|False|False|Boolean to search for contents of Address Objects for IP, CIDR, domain|None|False|
|group|string|None|True|Name of address group to check|None|MaliciousAddressGroup|

Example input:

```
{
  "address": "MaliciousHost",
  "enable_search": false,
  "group": "MaliciousAddressGroup"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_objects|[]address_object|False|List of found address objects|
|found|boolean|True|Was address found in group|

Example output:

```
```

#### Delete Address Object

This action deletes the address object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address_object|string|None|True|Name of the address object to delete|None|MaliciousHost|

Example input:

```
{
  "address_object": "MaliciousHost"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_object|address_object|False|Returns information about the deleted address object|

Example output:

```
{
  "address_object": {
    "dnsResolution": "IPV4_AND_IPV6",
    "id": "00000000-0000-0ed3-0000-012884905524",
    "links": {
      "parent": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkaddresses",
      "self": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/fqdns/00000000-0000-0ed3-0000-012884905524"
    },
    "metadata": {
      "domain": {
        "id": "e276abec-e0f2-11e3-8169-6d9ed49b625f",
        "name": "Global",
        "type": "Domain"
      },
      "lastUser": {
        "name": "admin"
      },
      "parentType": "NetworkAddress",
      "timestamp": 0
    },
    "name": "Example Object Created from InsightConnect",
    "overridable": false,
    "type": "FQDN",
    "value": "example.com"
  }
}
```

#### Create Address Object

This action creates a new address object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|IP address, CIDR IP address, or domain name to assign to the Address Object|None|example.com|
|address_object|string|None|False|Name of the address object, defaults to the value address in the address field if no name is given|None|MaliciousHost|
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
{
  "address_object": {
    "dnsResolution": "IPV4_AND_IPV6",
    "id": "00000000-0000-0ed3-0000-012884905524",
    "links": {
      "parent": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkaddresses",
      "self": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/fqdns/00000000-0000-0ed3-0000-012884905524"
    },
    "metadata": {
      "domain": {
        "id": "e276abec-e0f2-11e3-8169-6d9ed49b625f",
        "name": "Global",
        "type": "Domain"
      },
      "lastUser": {
        "name": "admin"
      },
      "parentType": "NetworkAddress",
      "timestamp": 0
    },
    "name": "Example Object Created from InsightConnect",
    "overridable": false,
    "type": "FQDN",
    "value": "example.com"
  }
}
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

* 1.1.0 - New actions - Create Address Object, Delete Address Object
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html)
