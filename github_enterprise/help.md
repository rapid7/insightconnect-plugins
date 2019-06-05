
# GitHub Enterprise

## About

[GitHub Enterprise](https://enterprise.github.com/) is the on-premises version of GitHub.

## Actions

### Create Organization

This action is used to create organization in enterprise.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|admin|string|None|True|Username of who will manage this organization|None|
|profile_name|string|None|True|Organization display name|None|
|name|string|None|True|Organization name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

### Demote User

This action is used to demote admin to ordinary user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|User to demote|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

### Suspend User

This action is used to suspend user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|GitHub username|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

### Unsuspend User

This action is used to unsuspend user from enterprise.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|GitHub username|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

### Promote User

This action is used to promote an ordinary user to admin.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|User to promote|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

## Triggers

### Issue

This trigger is used to monitor a repository for new issues and returns any new issues found.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization|string|None|False|Return issues of a specific organization|None|
|frequency|integer|300|False|Poll frequency in seconds|None|
|repository|string|None|True|Return issues of a specific repository|None|
|assignee|string|None|False|Username of assignee|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|object|False|None|

## Connection

This plugin requires a GitHub Enterprise host, username, and token or password.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|GitHub username|None|
|secret|string|None|True|GitHub password or token|None|
|host|string|None|True|Address of enterprise server|None|

## Troubleshooting

The GitHub Enterprise account must have sufficient privileges to perform the actions.

## Workflows

Examples:

* Ticket monitoring
* User provisioning and deprovisioning

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types

## References

* [GitHub Enterprise](https://enterprise.github.com/home)
* [GitHub Enterprise API](https://developer.github.com/v3/enterprise/)
