# Description

Bitbucket is the Git solution for professional teams. This plugin allows management of your Bitbucket account using its API.

# Key Features

* Repository administration
* User administration

# Requirements

* Requires Bitbucket account
* Requires username and API Key from the product
* API Token must be generated in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Bitbucket username and password|None|

## Technical Details

### Actions

#### Create Issue

This action is used to create a Bitbucket issue.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|assignee|string|None|False|Assignee username|None|
|component|string|None|False|Component name|None|
|content|string|None|False|Issue description|None|
|kind|string|None|False|Kind e.g. bug, proposal, etc|['None', 'Bug', 'Enhancement', 'Proposal', 'Task']|
|milestone|string|None|False|Milestone name|None|
|priority|string|None|False|Priority e.g. major, critical, etc|['None', 'Trivial', 'Minor', 'Major', 'Critical', 'Blocker']|
|repository|string|None|True|Repository name|None|
|state|string|None|False|State e.g. open, resolved, etc|['None', 'New', 'Open', 'Resolved', 'On hold', 'Invalid', 'Duplicate', 'Wontfix', 'Closed']|
|title|string|None|True|Issue title|None|
|version|string|None|False|Version name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|object|False|Issue|

#### Create Repository

This action is used to create a repository.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|description|string|None|False|Description of repository|None|
|has_issues|boolean|True|False|Add issue tracker|None|
|has_wiki|boolean|False|False|Has wiki|None|
|is_private|boolean|False|False|Repository is private|None|
|title|string|None|True|Title of repository|None|
|type|string|Git|False|Repo type e.g. Git, Mercurial, etc|['Hg', 'Git']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|repository|object|False|Repository|

#### Delete Repository

This action is used to delete a repository.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|title|string|None|True|Title of repository|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status|

#### User

This action is used to retrieve information about a given Bitbucket account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Bitbucket username|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|object|False|User|

### Triggers

#### Issue

This trigger allows monitoring a repository for newly created issues. It checks for new issues at every poll interval and returns any issues found.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|assignee|string|None|False|Assignee username|None|
|component|string|None|False|Component name|None|
|kind|string|None|False|Kind e.g. bug, proposal, etc|['None', 'Bug', 'Enhancement', 'Proposal', 'Task']|
|milestone|string|None|False|Milestone name|None|
|poll|integer|None|False|Poll interval in seconds|None|
|priority|string|None|False|Priority e.g. major, critical, etc|['None', 'Trivial', 'Minor', 'Major', 'Critical', 'Blocker']|
|repository|string|None|True|Return issues of a specific repository|None|
|state|string|None|False|State e.g. open, resolved, etc|['None', 'New', 'Open', 'Resolved', 'On hold', 'Invalid', 'Duplicate', 'Wontfix', 'Closed']|
|version|string|None|False|Version name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|[]object|False|Issues|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Be sure the provided Bitbucket account used has permissions to perform the actions.

# Version History

* 1.0.2 - Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-slim-plugin:3` | Use input and output constants | Changed `Exception` to `PluginException` | Added "f" strings | Removed duplicated code
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [BitBucket](https://bitbucket.org/)

