# Description

[SonicWall](https://www.sonicwall.com/products/firewalls/) next-generation firewalls (NGFW) provide the security, control and visibility you need to maintain an effective cybersecurity posture.
Manage your firewalls and block malicious hosts through this plugin.

# Key Features

* Block and unblock hosts by managing address groups

# Requirements

* Username and password
* Base URL of firewall

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|
|port|integer|443|False|The port number for provided host|None|443|
|url|string|None|True|Base URL for the SonicWall endpoint|None|https://www.example.com|
|verify_ssl|boolean|True|False|Check the server's SSL certificate|None|True|

Example input:

```
{
  "credentials": {
    "username":"user1",
    "password":"mypassword"
    },
  "port": 443,
  "url": "https://www.example.com",
  "verify_ssl": true
}
```

## Technical Details

### Actions

#### Delete Address Object

This action deletes an address object that has an exact match for the name.

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
|status|status|False|Returns information about creating new address object|

Example output:

```
{
    "status": {
        "success": true,
        "cli": {
            "mode": "config_mode",
            "depth": 1,
            "configuring": true,
            "pending_config": true,
            "restart_required": "FALSE"
        },
        "info": [
            {
                "level": "info",
                "code": "E_OK",
                "message": "Success."
            }
        ]
    }
}
```

#### Create Address Object

This action creates a new IPv4 Address Object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|status|False|Returns information about creating new address object|

Example output:

```
{
    "status": {
        "success": true,
        "cli": {
            "mode": "config_mode",
            "depth": 1,
            "configuring": true,
            "pending_config": true,
            "restart_required": "FALSE"
        },
        "info": [
            {
                "level": "info",
                "code": "E_OK",
                "message": "Success."
            }
        ]
    }
}
```

#### Add Address Object to Group

This action is used to add address object (FQDN, MAC, IPv4 or IPv6) to group (IPv4, IPv6 or Mixed).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|object_action|object_action|False|Return information about add address object to group|

Example output:

```
{
  "object_action": {
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
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### CLI

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Configuring|boolean|False|Configuring|
|Depth|integer|False|Depth|
|Mode|string|False|Mode|
|Pending Config|boolean|False|Pending config|
|Restart Required|string|False|Restart required|

#### info

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Code|string|False|Code|
|Level|string|False|Level|
|Message|string|False|Message|

#### object_action

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status|status|False|Status|

#### status

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CLI|cli|False|CLI|
|Info|[]info|False|Info|
|Success|boolean|False|Success|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.0 - New actions Create Address Object and Delete Address Object
* 1.0.0 - Initial plugin

# Links

## References

* [SonicWall Firewall](https://www.sonicwall.com/products/firewalls/)
* [SonicWall](https://www.sonicwall.com)
