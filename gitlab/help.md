
# GitLab

## About

[GitLab](https://www.gitlab.com) is a next generation developer collaboration software with version control capabilities.
This plugin utilizes the [GitLab API](https://docs.gitlab.com/ee/api/).

## Actions

### Create Issue

This action is used to create an issue.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID to unblock|None|
|parameters|issue_input|None|False|Issue parameters|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|due_date|date|False|None|
|description|string|False|None|
|confidential|boolean|False|None|
|labels|[]string|False|None|
|updated_at|date|False|None|
|iid|integer|False|None|
|web_url|string|False|None|
|milestone|milestone_output|False|None|
|id|integer|False|None|
|subscribed|boolean|False|None|
|title|string|False|None|
|created_at|date|False|None|
|author|user_output|False|None|
|assignees|[]user_output|False|None|
|state|string|False|None|
|user_notes_count|integer|False|None|
|assignee|user_output|False|None|
|project_id|integer|False|None|

### List User SSH Keys

This action is used to list user SSH keys.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ssh_keys|[]ssh_output|False|None|

### Delete User

This action is used to delete a GitLab user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID to unblock|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

### Delete User SSH Key

This action is used to delete a user SSH key.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|key_id|integer|None|True|Key ID|None|
|id|integer|None|True|User ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

### Get User

This action is used to get GitLab user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|username|string|False|None|
|bio|string|False|None|
|name|string|False|None|
|avatar_url|string|False|None|
|twitter|string|False|None|
|linkedin|string|False|None|
|id|integer|False|None|
|state|string|False|None|
|web_url|string|False|None|
|location|string|False|None|
|skype|string|False|None|
|organization|string|False|None|
|created_at|date|False|None|
|website_url|string|False|None|

### Unblock User

This action is used to unlock GitLab user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID to unblock|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

### Block User

This action is used to block GitLab user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID to block|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

## Triggers

### Issue

This trigger is used to monitor new issues.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|iids|integer|None|False|Return only the issues having the given iid|None|
|search|string|None|False|Search issues against their title and description|None|
|labels|string|None|True|Comma-separated list of label names, issues must have all labels to be returned|None|
|milestone|string|None|False|The milestone title|None|
|interval|integer|None|False|How often recieve new issues|None|
|state|string|None|False|Return all issues or just those that are opened or closed|['Opened', 'Closed']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|object|False|None|

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|False|Host URL e.g. https\://gitlab.example.com\:8000/api/v4/|None|
|credentials|credential_username_password|None|True|Enter GitLab username and password (or token)|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Manage GitLab team
* Project version control
* Issue tracking

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types

## References

* [GitLab](https://gitlab.com)
* [GitLab API](https://docs.gitlab.com/ce/api/README.html)
