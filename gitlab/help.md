# Description

[GitLab](https://www.gitlab.com) is a next generation developer collaboration software with version control capabilities.
GitLab InsightConnect plugin allows user and issue management.
This plugin utilizes the [GitLab API](https://docs.gitlab.com/ee/api/).

# Key Features

* Block and unblock users
* Delete SSH keys
* Retrieve users details
* Create issues

# Requirements

* GitLab host URL
* GitlLab account username and password (or token)

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|False|Host URL e.g. https://gitlab.example.com:8000/api/v4/|None|
|credentials|credential_username_password|None|True|Enter GitLab username and password (or token)|None|

## Technical Details

### Actions

#### Create Issue

This action is used to create an issue.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID to unblock|None|
|parameters|issue_input|None|False|Issue parameters|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assignee|user_output|False|Assignee|
|assignees|[]user_output|False|Assignees|
|author|user_output|False|Author|
|confidential|boolean|False|Confidential|
|created_at|date|False|Created at|
|description|string|False|Description|
|due_date|date|False|Due date|
|id|integer|False|ID|
|iid|integer|False|IID|
|labels|[]string|False|Labels|
|milestone|milestone_output|False|Milestone|
|project_id|integer|False|Project ID|
|state|string|False|State|
|subscribed|boolean|False|Subscribed|
|title|string|False|Title|
|updated_at|date|False|Updated at|
|user_notes_count|integer|False|User notes count|
|web_url|string|False|Web URL|

#### List User SSH Keys

This action is used to list user SSH keys.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ssh_keys|[]ssh_output|False|SSH keys|

#### Delete User

This action is used to delete a GitLab user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID to unblock|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Status|

#### Delete User SSH Key

This action is used to delete a user SSH key.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|key_id|integer|None|True|Key ID|None|
|id|integer|None|True|User ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Status|

#### Get User

This action is used to get GitLab user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|avatar_url|string|False|Avatar URL|
|bio|string|False|Bio|
|created_at|date|False|Create at|
|id|integer|False|ID|
|linkedin|string|False|LinkedIn|
|location|string|False|Location|
|name|string|False|Name|
|organization|string|False|Organization|
|skype|string|False|Skype|
|state|string|False|State|
|twitter|string|False|Twitter|
|username|string|False|Username|
|web_url|string|False|Web URL|
|website_url|string|False|Website URL|

#### Unblock User

This action is used to unlock GitLab user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID to unblock|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Status|

#### Block User

This action is used to block GitLab user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID to block|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|Status|

### Triggers

#### Issue

This trigger is used to monitor new issues.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|iids|integer|None|False|Return only the issues having the given iid|None|
|search|string|None|False|Search issues against their title and description|None|
|labels|string|None|True|Comma-separated list of label names, issues must have all labels to be returned|None|
|milestone|string|None|False|The milestone title|None|
|interval|integer|None|False|How often receive new issues|None|
|state|string|None|False|Return all issues or just those that are opened or closed|['Opened', 'Closed']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|object|False|Issue|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [GitLab](https://gitlab.com)
* [GitLab API](https://docs.gitlab.com/ce/api/README.html)

