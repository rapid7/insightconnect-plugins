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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|server|string|None|False|Enter the address for the server|None|
|username_and_password|credential_username_password|None|True|Cisco username and password|None|

## Technical Details

### Actions

#### Block URL Policy

This action is used to create a new block URL policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|access_policy|string|None|True|Access Policy name|None|
|rule_name|string|None|True|Name for Access Rule to be created|None|
|url_objects|[]url_object|None|True|URL Objects to block|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|string|True|Success|

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

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html)

