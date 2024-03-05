# Description

[SonicWall](https://www.sonicwall.com/products/firewalls/) next-generation firewalls (NGFW) provide the security, control and visibility you need to maintain an effective cybersecurity posture.
Manage your firewalls and block malicious hosts through this plugin.

# Key Features
  
* Block and unblock hosts by managing address groups

# Requirements
  
* Username and password  
* Base URL of firewall

# Supported Product Versions
  
* SonicWall 04-03-2024

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|
|port|integer|443|False|The port number for provided host|None|443|
|url|string|None|True|Base URL for the SonicWall endpoint|None|https://www.example.com|
|verify_ssl|boolean|True|False|Check the server's SSL certificate|None|True|
  
Example input:

```
{
  "credentials": {
    "password": "mypassword",
    "username": "user1"
  },
  "port": 443,
  "url": "https://www.example.com",
  "verify_ssl": true
}
```

## Technical Details

### Actions


#### Add Address Object to Group
  
This action is used to add address object (FQDN, MAC, IPv4 or IPv6) to group (IPv4, IPv6 or Mixed)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|string|None|True|Name of the address object|None|MaliciousHost|
|group|string|None|True|Name of the address group to add the address object to|None|BlockList|
  
Example input:

```
{
  "address_object": "MaliciousHost",
  "group": "BlockList"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|object_action|object_action|False|Return information about add address object to group|{"status":{"status":{"success":true,"cli":{"mode":"config_mode","depth":1,"configuring":true,"pending_config":false,"restart_required":"FALSE"},"info":[{"level":"info","code":"E_OK","message":"Changes made."}]}}}|
  
Example output:

```
{
  "object_action": {
    "status": {
      "status": {
        "cli": {
          "configuring": true,
          "depth": 1,
          "mode": "config_mode",
          "pending_config": false,
          "restart_required": "FALSE"
        },
        "info": [
          {
            "code": "E_OK",
            "level": "info",
            "message": "Changes made."
          }
        ],
        "success": true
      }
    }
  }
}
```

#### Check if Address in Group
  
This action is used to check that a host or address object is in an address group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|Address Object name, or IP, CIDR, or domain name when Enable Search is set to true|None|MaliciousHost|
|enable_search|boolean|False|False|When enabled, search for contents of Address Objects for an IP, CIDR or domain. This is useful when you don't know the Address Object by its name|None|True|
|group|string|None|True|Name of address group to check|None|InsightConnect Block List|
  
Example input:

```
{
  "address": "MaliciousHost",
  "enable_search": false,
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address_objects|[]object|False|The names and details of the address objects that match or contain the address|[{"dns_ttl":0,"domain":"example.com","name":"InsightConnect Block List","uuid":"00000000-0000-0001-0100-00401034ea00","zone":"DMZ"}]|
|found|boolean|True|Return true if address was found in group, return false if not found|True|
  
Example output:

```
{
  "address_objects": [
    {
      "dns_ttl": 0,
      "domain": "example.com",
      "name": "InsightConnect Block List",
      "uuid": "00000000-0000-0001-0100-00401034ea00",
      "zone": "DMZ"
    }
  ],
  "found": true
}
```

#### Create Address Object
  
This action is used to creates a new address object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IP, CIDR, or domain name to assign to the Address Object|None|example.com|
|address_object|string|None|False|Name of the address object, defaults to value address if no name is given|None|MaliciousHost|
|skip_private_address|boolean|None|True|If set to true, any addresses that are defined in the RFC1918 space will not be blocked. e.g. 10/8, 172.16/12, 192.168/16|None|True|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be blocked. This can include IPs, CIDRs, and domains|None|["198.51.100.100", "192.0.2.0/24", "example.com"]|
|zone|string|WAN|True|Name of the zone where the new object will be placed|None|WAN|
  
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
  ],
  "zone": "WAN"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|host_status|string|False|Returns information about the host status|created|
|status|status|False|Returns information about creating new address object|{"success":true,"cli":{"mode":"config_mode","depth":1,"configuring":true,"pending_config":true,"restart_required":"FALSE"},"info":[{"level":"info","code":"E_OK","message":"Success."}]}|
  
Example output:

```
{
  "host_status": "created",
  "status": {
    "cli": {
      "configuring": true,
      "depth": 1,
      "mode": "config_mode",
      "pending_config": true,
      "restart_required": "FALSE"
    },
    "info": [
      {
        "code": "E_OK",
        "level": "info",
        "message": "Success."
      }
    ],
    "success": true
  }
}
```

#### Delete Address Object
  
This action is used to deletes an address object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|string|None|True|Name of the address object to delete|None|MaliciousHost|
  
Example input:

```
{
  "address_object": "MaliciousHost"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|status|False|Returns information about creating new address object|{"cli":{"configuring":true,"depth":1,"mode":"config_mode","pending_config":true,"restart_required":"FALSE"},"info":[{"code":"E_OK","level":"info","message":"Success."}],"success": true}|
  
Example output:

```
{
  "status": {
    "cli": {
      "configuring": true,
      "depth": 1,
      "mode": "config_mode",
      "pending_config": true,
      "restart_required": "FALSE"
    },
    "info": [
      {
        "code": "E_OK",
        "level": "info",
        "message": "Success."
      }
    ],
    "success": true
  }
}
```

#### Remove Address Object from Group
  
This action is used to deletes an address object from an address group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|string|None|True|Name of the address object|None|MaliciousHost|
|group|string|None|True|Name of the address group|None|InsightConnect Block List|
  
Example input:

```
{
  "address_object": "MaliciousHost",
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|status|False|Returns information about removing the address object from the address group|{"cli":{"configuring":true,"depth":1,"mode":"config_mode","pending_config":true,"restart_required":"FALSE"},"info":[{"code":"E_OK","level":"info","message":"Success."}],"success":true}|
  
Example output:

```
{
  "status": {
    "cli": {
      "configuring": true,
      "depth": 1,
      "mode": "config_mode",
      "pending_config": true,
      "restart_required": "FALSE"
    },
    "info": [
      {
        "code": "E_OK",
        "level": "info",
        "message": "Success."
      }
    ],
    "success": true
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**cli**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Configuring|boolean|None|False|Configuring|None|
|Depth|integer|None|False|Depth|None|
|Mode|string|None|False|Mode|None|
|Pending Config|boolean|None|False|Pending config|None|
|Restart Required|string|None|False|Restart required|None|
  
**info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|string|None|False|Code|None|
|Level|string|None|False|Level|None|
|Message|string|None|False|Message|None|
  
**status**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CLI|cli|None|False|CLI|None|
|Info|[]info|None|False|Info|None|
|Success|boolean|None|False|Success|None|
  
**object_action**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Status|status|None|False|Status|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 1.3.2 - Updated SDK to the latest version to address memory usage issue | Fixed connection test  
* 1.3.1 - Replace the PluginException with a logger in Create Address Object action | Add `host_status` output parameter in Create Address Object action  
* 1.3.0 - New action Remove Address from Group  
* 1.2.0 - New action Check If Address In Address Group  
* 1.1.0 - New actions Create Address Object and Delete Address Object  
* 1.0.0 - Initial plugin

# Links

* [SonicWall](https://www.sonicwall.com)

## References

* [SonicWall Firewall](https://www.sonicwall.com/products/firewalls/)
* [SonicWall](https://www.sonicwall.com)
