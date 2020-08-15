# Description

[Cisco Adaptive Security Appliances](https://www.cisco.com/c/en/us/products/security/adaptive-security-appliance-asa-software/index.html) deliver enterprise-class firewall capabilities and the Cisco ASA plugin allows you to automate the management of network objects for ASA appliances.

# Key Features

* Check if address is in address group
* Remove address from group
* Delete Address Object
* Add Address to Group

# Requirements

* Username and Password for an ASA account with the appropriate privilege level for the action
* Cisco ASA server with the [REST API server enabled](https://www.cisco.com/c/en/us/td/docs/security/asa/api/qsg-asa-api.html)

# Documentation

## Setup

The REST API server must be installed and enabled on the Cisco ASA device this plugin connects to. Cisco provides online
documentation for this available [here](https://www.cisco.com/c/en/us/td/docs/security/asa/api/qsg-asa-api.html). In
addition, the user account must have the necessary permissions for the intended actions:

* Actions that retrieve or check data require Cisco privilege level 5 or greater
* Actions that change or modify data require Cisco privilege level 15

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username": "admin", "password": "mypassword"}|
|port|integer|443|False|The port number for provided host|None|443|
|ssl_verify|boolean|True|False|Validate TLS / SSL certificate|None|True|
|url|string|None|True|API Access URL|None|https://example.com|
|user_agent|string|REST API Agent|False|User agent for provided host|None|REST API Agent|

Example input:

```
{
  "credentials": {
    "username": "admin",
    "password": "mypassword"
  },
  "port": 443,
  "ssl_verify": true,
  "url": "https://example.com",
  "user_agent": "REST API Agent"
}
```

## Technical Details

### Actions

#### Add Address to Group

This action is used to add a preexisting Addresses to a Network Object Group from to allow them to block the host.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|Name of the address, which can be an IPv4 or IPv6 address|None|198.51.100.100|
|group|string|None|True|Name of the group to add the address to|None|InsightConnect Block List|

Example input:

```
{
  "address": "198.51.100.100",
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success if address add to group|

Example output:

```
{
  "success": true
}
```

#### Delete Address Object

This action is used to delete an Address Object by its object name.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address_object|string|None|True|Name of the address object to delete|None|MaliciousDomain|

Example input:

```
{
  "address_object": "MaliciousDomain"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success if address object deleted|

Example output:

```
{
  "success": true
}
```

#### Remove Address from Group

This action is used to remove an address from a group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|The IP address or FQDN to remove from group|None|198.51.100.100|
|group|string|None|True|Name of the group to remove the address from|None|InsightConnect Block List|

Example input:

```
{
  "address": "198.51.100.100",
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success if address removed from group|

Example output:

```
{
  "success": true
}
```

#### Check If Address in Group

This action checks to see if an IP address, CIDR IP address, or domain is in an Address Group. Supports IPv6.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|IP, CIDR, or domain name when Enable Search is off or Address Object name, object ID, IP, CIDR, or domain name if Enable Search is on|None|198.51.100.100|
|enable_search|boolean|False|True|Set to true to search contents of object by its name, ID, IP, CIDR, or domain name|None|False|
|group|string|None|True|Name of address group to check|None|InsightConnect Block List|

Example input:

```
{
  "address": "198.51.100.100",
  "enable_search": false,
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_objects|[]address_objects|False|List of found address objects|
|found|boolean|True|Was address found in group|

Example output:

```
{
  "address_objects": [
    {
      "host": {
        "kind": "IPv4Address",
        "value": "198.51.100.100"
      },
      "kind": "object#NetworkObj",
      "name": "ASA_Demo_NObj_00",
      "objectId": "ASA_Demo_NObj_00",
      "selfLink": "https://example.com:443/api/objects/networkobjects/ASA_Demo_NObj_00"
    }
  ],
  "found": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### address_objects

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Host|host|False|Host|
|Kind|string|False|Kind|
|Name|string|False|Name|
|Object ID|string|False|Object ID|
|Self Link|string|False|Self link|

#### host

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Kind|string|False|Kind|
|Value|string|False|Value|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.3.0 - Add new action Add Address to Group
* 1.2.0 - Add new action Delete Address Object
* 1.1.0 - Add new action Remove Address from Group
* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Adaptive Security Appliance](https://www.cisco.com/c/en/us/products/security/adaptive-security-appliance-asa-software/index.html)
