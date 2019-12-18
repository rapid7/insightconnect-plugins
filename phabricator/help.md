# Description

[Phabricator](https://secure.phabricator.com/) is a suite of open source tools for peer code review, 
task management, and project communication. The Phabricator plugin allows you to setup and manage code reviews.

This plugin utilizes the [Python Phabricator](https://github.com/disqus/python-phabricator) library.

# Key Features

* Create and edit tasks
* Create projects

# Requirements

* Phabricator API token

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|token|string|None|False|API Token|None|
|url|string|None|False|API URL e.g. https://test-v2lvaidr55f4.phacility.com/api/|None|

## Technical Details

### Actions

#### Change Status

This action is used to change the status of a task.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|True|Status name [Open\|Resolved\|Wontfix\|Invalid\|Spite]|None|
|id|string|None|True|Task ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|

#### Create Task

This action is used to create a new task on your Phabricator account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|description|string|None|False|Description of new created task|None|
|title|string|None|True|Name of task|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|True|None|

#### Claim

This action is used to claim a task.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Task ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|

#### Priority

This action is used to change the priority of a task.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|priority|string|None|True|Task priority from [unbreak, triage, high, normal, low, wish]|None|
|id|string|None|True|Task ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|

#### Add Subscriber

This action is used to add users or projects as subscribers.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|subscribes|[]string|None|True|Subscribe users or projects [PHID-USER-xxx, PHID-PROJ-xxx]|None|
|id|string|None|True|Task ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|

#### Remove Subscriber

This action is used to remove yourself as a subscriber.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Task ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|

#### Close

This action is used to close a task.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Task ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|

#### Assign

This action is used to assign a specific user to task.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Task ID|None|
|user|string|None|True|Specific user assign to task|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|

#### Projects

This action is used to add related projects.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ID|string|None|True|Task ID|None|
|projects|[]string|None|True|Related projects names|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to the new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Phabricator](https://secure.phabricator.com/)
* [Python Phabricator](https://github.com/disqus/python-phabricator)

