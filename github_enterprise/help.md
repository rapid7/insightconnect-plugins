# Description

[GitHub Enterprise](https://enterprise.github.com/) is the on-premises version of GitHub.
GitHub Enterprise InsightConnect plugin allows user management.

# Key Features

* Promote and demote users
* Suspend and unsuspend users
* Create an organization

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin requires a GitHub Enterprise host, username, and token or password.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|GitHub username|None|
|secret|string|None|True|GitHub password or token|None|
|host|string|None|True|Address of enterprise server|None|

## Technical Details

### Actions

#### Create Organization

This action is used to create organization in enterprise.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|admin|string|None|True|Username of who will manage this organization|None|
|profile_name|string|None|True|Organization display name|None|
|name|string|None|True|Organization name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

#### Demote User

This action is used to demote admin to ordinary user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|User to demote|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

#### Suspend User

This action is used to suspend user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|GitHub username|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

#### Unsuspend User

This action is used to unsuspend user from enterprise.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|GitHub username|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

#### Promote User

This action is used to promote an ordinary user to admin.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|User to promote|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

### Triggers

#### Issue

This trigger is used to monitor a repository for new issues and returns any new issues found.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization|string|None|False|Return issues of a specific organization|None|
|frequency|integer|300|False|Poll frequency in seconds|None|
|repository|string|None|True|Return issues of a specific repository|None|
|assignee|string|None|False|Username of assignee|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|object|False|None|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The GitHub Enterprise account must have sufficient privileges to perform the actions.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [GitHub Enterprise](https://enterprise.github.com/home)
* [GitHub Enterprise API](https://developer.github.com/v3/enterprise/)

