# Description

[McAfee ePO](https://www.mcafee.com/us/products/epolicy-orchestrator.aspx) is a McAfee ePolicy Orchestrator provides a web API for McAfee endpoint protection management activities
This plugin utilizes libraries available through McAfee's ePolicy Orchestrator Management interface.

# Key Features

* Policy enforcement

# Requirements

* Username and Password
* McAfee ePO server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password to access McAfee ePO|None|{"username":"user1", "password":"mypassword"}|
|port|number|None|True|McAfee ePO port|None|8443|
|url|string|None|True|McAfee ePO address|None|https://www.example.com|

Example input:

```
{
  "credentials": {
    "username":"user1",
    "password":"mypassword"
  },
  "port": 8443,
  "url": "https://www.example.com"
}
```

## Technical Details

### Actions

#### Get Policies

This action is used to get policies assigned to a user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|search_text|string|None|True|Finds all policies that the user is permitted to see that match the given search text|None|Search text|

Example input:

```
{
  "search_text": "Search text"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|policies_returned|[]policies_returned|True|All policies that match to the given search text|

Example output:

```
```

#### System Information

This action is used to list information about system(s).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|integer|None|False|System search query e.g Device-1|None|Device-1|

Example input:

```
{
  "query": "Device-1"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|devices|[]string|None|True|Array of all devices to tag|None|["Device-1", "Device-2"]|
|tag|string|None|True|The tag to apply|None|Tag1|

Example input:

```
{
  "devices": [
    "Device-1",
    "Device-2"
  ],
  "tag": "Tag1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Response message|

Example output:

```
```

#### Add Permission Set to User

This action is used to add permission set(s) to a specified user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|permission_set|string|None|False|String name of the permission set to apply|None|Group admin|
|user|string|None|False|Username of the target user|None|user1|

Example input:

```
{
  "permission_set": "Group admin",
  "user": "user1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|boolean|True|Response message|

Example output:

```
```

#### Clear Tags

This action is used to clear the given tag to a supplied list of systems.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|devices|[]string|None|True|Array of all devices to clear tag|None|["Device-1", "Device-2"]|
|tag|string|None|True|The tag to clear|None|Tag1|

Example input:

```
{
  "devices": [
    "Device-1",
    "Device-2"
  ],
  "tag": "Tag1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Response message|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.1.0 - New action Get Policies 
* 2.0.0 - Update to use the `insightconnect-python-3-38-plugin:4` Docker image
* 1.0.2 - Fix issue with wrong type in action System Information
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Updates
* 0.1.0 - Initial plugin

# Links

## References

* [McAfee ePO](https://www.mcafee.com/us/products/epolicy-orchestrator.aspx)
* [McAfee ePO 5.1.0 Web API Documentation](https://kc.mcafee.com/corporate/index?page=content&id=PD24810)

