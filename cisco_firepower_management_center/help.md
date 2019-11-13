# Description

[Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html) is your administrative nerve center for managing critical Cisco network security solutions.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

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

* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html)

