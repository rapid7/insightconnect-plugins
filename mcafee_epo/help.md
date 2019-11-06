# Description

[McAfee ePO](https://www.mcafee.com/us/products/epolicy-orchestrator.aspx) is a McAfee ePolicy Orchestrator provides a web API for McAfee endpoint protection management activities
This plugin utilizes libraries available through McAfee's ePolicy Orchestrator Management interface.

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
|url|string|None|True|McAfee ePO address e.g. epo.company.com|None|
|credentials|credential_username_password|None|True|Username and password to access McAfee ePO e.g. admin|None|
|port|number|None|True|McAfee ePO Port e.g. 8443|None|

## Technical Details

### Actions

#### System Information

This action is used to list information about system(s).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|False|System search query e.g Device-1|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|properties|[]computer_properties|True|Computer Properties|

Example output:

```
```

#### Add Tags

This action is used to assign the given tag to a supplied list of systems.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tag|string|None|True|The tag to apply|None|
|devices|[]string|None|True|Array of all devices to tag e.g. ["Device-1","Device-2"]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Response message|

#### Add Permission Set to User

This action is used to add permission set(s) to a specified user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|False|Username of the target user|None|
|permission_set|string|None|False|String name of the permission set to apply e.g. Group Admin|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|boolean|True|Response message|

#### Clear Tags

This action is used to clear the given tag to a supplied list of systems.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tag|string|None|True|The tag to clear|None|
|devices|[]string|None|True|Array of all devices to clear tag e.g. ["Device-1","Device-2"]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Response message|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Updates
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [McAfee ePO](https://www.mcafee.com/us/products/epolicy-orchestrator.aspx)
* [McAfee ePO 5.1.0 Web API Documentation](https://kc.mcafee.com/corporate/index?page=content&id=PD24810)

