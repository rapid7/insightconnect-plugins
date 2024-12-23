# Description

[Cisco Adaptive Security Appliances](https://www.cisco.com/c/en/us/products/security/adaptive-security-appliance-asa-software/index.html) deliver enterprise-class firewall capabilities and the Cisco ASA plugin allows you to automate the management of network objects for ASA appliances

# Key Features

* Determine if a host is blocked by checking if it's found in an address group applied to a firewall rule
* Block and unblock hosts from the firewall through object management
* Block and unblock hosts with the shun command
* Check which hosts are blocked with the shun command

# Requirements

* Username and Password for an ASA account with the appropriate privilege level for the action
* Cisco ASA server with the [REST API server enabled](https://www.cisco.com/c/en/us/td/docs/security/asa/api/qsg-asa-api.html)

# Supported Product Versions

* 9.13(1)

# Documentation

## Setup

The REST API server must be installed and enabled on the Cisco ASA device this plugin connects to. Cisco provides online
documentation for this available [here](https://www.cisco.com/c/en/us/td/docs/security/asa/api/qsg-asa-api.html). In
addition, the user account must have the necessary permissions for the intended actions:

* Actions that retrieve or check data require Cisco privilege level 5 or greater
* Actions that change or modify data require Cisco privilege level 15

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username and password|None|{"username": "admin", "password": "mypassword"}|None|None|
|port|integer|443|False|The port number for provided host|None|443|None|None|
|ssl_verify|boolean|True|False|Validate TLS / SSL certificate|None|True|None|None|
|url|string|None|True|API Access URL|None|https://example.com|None|None|
|user_agent|string|REST API Agent|False|User agent for provided host|None|REST API Agent|None|None|

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

This action is used to add an IP address associated with an existing Object to a Network Group.
It works by checking the user-supplied IPv4 or IPv6 addresses across all Objects in Cisco ASA. If a match is found, it adds the object associated with the provided IP address to the group. This is useful when you don't know the Object by its name.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|Name of the address, which can be an IPv4 or IPv6 address|None|198.51.100.100|None|None|
|group|string|None|True|Name of the group to add the address to|None|InsightConnect Block List|None|None|
  
Example input:

```
{
  "address": "198.51.100.100",
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Success if address add to group|True|
  
Example output:

```
{
  "success": true
}
```

#### Block Host

This action is used to block hosts by IP address(IPv4) using the shun command

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|destination_ip|string|None|False|Destination IP address|None|198.51.100.100|None|None|
|destination_port|integer|None|False|Destination port|None|443|None|None|
|protocol|string|None|False|IP protocol, for example TCP or UDP|None|TCP|None|None|
|shun|boolean|True|True|True to block a host or false to unblock a host using the shun command|None|True|None|None|
|source_ip|string|None|True|Source IP address you want to block or unblock|None|198.51.100.100|None|None|
|source_port|integer|None|False|Source port|None|443|None|None|
  
Example input:

```
{
  "destination_ip": "198.51.100.100",
  "destination_port": 443,
  "protocol": "TCP",
  "shun": true,
  "source_ip": "198.51.100.100",
  "source_port": 443
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the block or unblock action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Check If Address in Group

This action checks to see if an IP address, CIDR IP address, or domain is in an Address Group. Supports IPv6

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IP, CIDR, or domain name when Enable Search is off or Address Object name, object ID, IP, CIDR, or domain name if Enable Search is on|None|198.51.100.100|None|None|
|enable_search|boolean|False|True|Set to true to search contents of object by its name, ID, IP, CIDR, or domain name|None|False|None|None|
|group|string|None|True|Name of address group to check|None|InsightConnect Block List|None|None|
  
Example input:

```
{
  "address": "198.51.100.100",
  "enable_search": false,
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address_objects|[]address_objects|False|List of found address objects|None|
|found|boolean|True|Was address found in group|True|
  
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

#### Create Address Object

This action is used to create address object by the object IPv4 address, IPv6 address, CIDR, range, or domain name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IPv4 address, IPv6 address, CIDR, range, or domain name to assign to the address object|None|198.51.100.100|None|None|
|address_object|string|None|False|Name of the address object, defaults to the value in the address field if no name is given|None|MaliciousHost|None|None|
|skip_private_addresses|boolean|None|False|If set to true, any addresses that are defined in the RFC1918 space will not be blocked. e.g. 10/8, 172.16/12, 192.168/16|None|False|None|None|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be blocked. This can include IPs, CIDRs, and domains|None|["198.51.100.100"]|None|None|
  
Example input:

```
{
  "address": "198.51.100.100",
  "address_object": "MaliciousHost",
  "skip_private_addresses": false,
  "whitelist": [
    "198.51.100.100"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Returns true if object was created|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Address Object

This action is used to delete an Address Object by its object name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|string|None|True|Name of the address object to delete|None|MaliciousDomain|None|None|
  
Example input:

```
{
  "address_object": "MaliciousDomain"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Success if address object deleted|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Blocked Hosts

This action is used to get blocked hosts

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|hosts|[]hosts|True|List of hosts blocked with shun command|None|
  
Example output:

```
{
  "hosts": [
    {
      "source_ip": "10.1.1.27",
      "dest_ip": "10.2.2.89",
      "source_port": "444",
      "dest_port": "555",
      "protocol": "6"
    }
  ]
}
```

#### Remove Address from Group

This action is used to remove an address from a group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|The IP address or FQDN to remove from group|None|198.51.100.100|None|None|
|group|string|None|True|Name of the group to remove the address from|None|InsightConnect Block List|None|None|
  
Example input:

```
{
  "address": "198.51.100.100",
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Success if address removed from group|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**host**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Kind|string|None|False|Kind is the type of object e.g. IPv4Address, IPv4FQDN, etc.|None|
|Value|string|None|False|The value of the object. This will be the actual IPv4, IPv6, FQDN, etc. address the object refers to.|None|
  
**address_objects**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Host|host|None|False|Host|None|
|Kind|string|None|False|Kind|None|
|Object Name|string|None|False|The name of the object|None|
|Object ID|string|None|False|Object ID|None|
|Self Link|string|None|False|Self link|None|
  
**hosts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Destination IP|string|None|False|Destination IP address|None|
|Destination Port|string|None|False|Destination port|None|
|Protocol|string|None|False|Protocol|None|
|Source IP|string|None|False|Source IP address|None|
|Source Port|string|None|False|Source port|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.5.1 - Bumping requirements.txt | SDK bump to 6.2.0
* 1.5.0 - Add new actions Get Blocked Hosts and Block Host
* 1.4.2 - Add `docs_url` in plugin spec | Update `source_url` in plugin spec
* 1.4.1 - Fix None check in actions Add Address to Group and Create Address Object
* 1.4.0 - Add new action Create Address Object
* 1.3.0 - Add new action Add Address to Group
* 1.2.0 - Add new action Delete Address Object
* 1.1.0 - Add new action Remove Address from Group
* 1.0.0 - Initial plugin

# Links

* [Cisco Adaptive Security Appliance](https://www.cisco.com/c/en/us/products/security/adaptive-security-appliance-asa-software/index.html)

## References

* [Cisco Adaptive Security Appliance API Docs](https://www.cisco.com/c/en/us/td/docs/security/asa/api/quick-start/qsg-asa-api.html)