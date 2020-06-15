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

* 1.0.0 - Initial plugin

# Links

## References

* [SonicWall Firewall](https://www.sonicwall.com/products/firewalls/)
* [SonicWall](https://www.sonicwall.com)
