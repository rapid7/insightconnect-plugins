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
|username|string|None|True|Bitbucket username|None|
|secret|credential_token|None|True|Bitbucket password or token|None|

## Technical Details

### Actions

#### Create Issue

This action is used to create a Bitbucket issue.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|priority|string|None|False|Priority e.g. major, critical, etc.|['None', 'Trivial', 'Minor', 'Major', 'Critical', 'Blocker']|
|kind|string|None|False|Kind e.g. bug, proposal, etc.|['None', 'Bug', 'Enhancement', 'Proposal', 'Task']|
|repository|string|None|True|Repository name|None|
|title|string|None|True|Issue title|None|
|component|string|None|False|Component name|None|
|content|string|None|False|Issue description|None|
|assignee|string|None|False|Assignee username|None|
|state|string|None|False|State e.g. open, resolved, etc.|['None', 'New', 'Open', 'Resolved', 'On hold', 'Invalid', 'Duplicate', 'Wontfix', 'Closed']|
|version|string|None|False|Version name|None|
|milestone|string|None|False|Milestone name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|object|False|None|

#### Create Repository

This action is used to create a repository.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|has_wiki|boolean|False|False|Has wiki|None|
|description|string|None|False|Description of repository|None|
|title|string|None|True|Title of repository|None|
|has_issues|boolean|True|False|Add issue tracker|None|
|type|string|Git|False|Repo type e.g. Git, Mercurial, etc.|['Hg', 'Git']|
|is_private|boolean|False|False|Repository is private|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|repository|object|False|None|

#### Delete Repository

This action is used to delete a repository.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|title|string|None|True|Title of repository|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|

#### User

This action is used to retrieve information about a given Bitbucket account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Bitbucket username|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|object|False|None|

### Triggers

#### Issue

This trigger allows monitoring a repository for newly created issues. It checks for new issues at every poll interval and returns any issues found.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|kind|string|None|False|Kind e.g. bug, proposal, etc.|['None', 'Bug', 'Enhancement', 'Proposal', 'Task']|
|repository|string|None|True|Return issues of a specific repository|None|
|component|string|None|False|Component name|None|
|priority|string|None|False|Priority e.g. major, critical, etc.|['None', 'Trivial', 'Minor', 'Major', 'Critical', 'Blocker']|
|assignee|string|None|False|Assignee username|None|
|state|string|None|False|State e.g. open, resolved, etc.|['None', 'New', 'Open', 'Resolved', 'On hold', 'Invalid', 'Duplicate', 'Wontfix', 'Closed']|
|version|string|None|False|Version name|None|
|milestone|string|None|False|Milestone name|None|
|poll|integer|None|False|Poll interval in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|[]object|False|None|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Be sure the provided Bitbucket account used has permissions to perform the actions.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [BitBucket](https://bitbucket.org/)

