# Description

GitLab plugin allows user management and issue management in Gitlab

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
*This plugin does not contain any supported product versions.*

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Enter GitLab username and password (or token)|None|None|
|url|string|None|True|Host URL e.g. https://gitlab.example.com:8000/api/v4/|None|None|
  
Example input:

```
{
  "credentials": {
    "password": "",
    "username": ""
  },
  "url": ""
}
```

## Technical Details

### Actions


#### Block User
  
This action is used to block GitLab user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID to block|None|None|
  
Example input:

```
{
  "id": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|Status|None|
  
Example output:

```
{
  "status": true
}
```

#### Create Issue
  
This action is used to create issue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID to unblock|None|None|
|parameters|issue_input|None|False|Issue parameters|None|None|
  
Example input:

```
{
  "id": 0,
  "parameters": {
    "Assignees": [
      {}
    ],
    "Confidential": "true",
    "Created At": "",
    "Description title": {},
    "Discussion To Resolve": {},
    "Due Date": {},
    "Issue title": "",
    "Labels": {},
    "Merge Request To Resolve Discussions Of": {},
    "Milestone": {},
    "Project ID": 0
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assignee|user_output|False|Assignee|None|
|assignees|[]user_output|False|Assignees|None|
|author|user_output|False|Author|None|
|confidential|boolean|False|Confidential|None|
|created_at|date|False|Created at|None|
|description|string|False|Description|None|
|due_date|date|False|Due date|None|
|id|integer|False|ID|None|
|iid|integer|False|IID|None|
|labels|[]string|False|Labels|None|
|milestone|milestone_output|False|Milestone|None|
|project_id|integer|False|Project ID|None|
|state|string|False|State|None|
|subscribed|boolean|False|Subscribed|None|
|title|string|False|Title|None|
|updated_at|date|False|Updated at|None|
|user_notes_count|integer|False|User notes count|None|
|web_url|string|False|Web URL|None|
  
Example output:

```
{
  "assignee": {
    "Avatar URL": {},
    "ID": 0,
    "Name": "",
    "State": {},
    "Username": {},
    "Web URL": {}
  },
  "assignees": [
    {
      "Avatar URL": {},
      "ID": 0,
      "Name": "",
      "State": {},
      "Username": {},
      "Web URL": {}
    }
  ],
  "author": {
    "Avatar URL": {},
    "ID": 0,
    "Name": "",
    "State": {},
    "Username": {},
    "Web URL": {}
  },
  "confidential": true,
  "created_at": "",
  "description": "",
  "due_date": "",
  "id": 0,
  "iid": 0,
  "labels": [
    ""
  ],
  "milestone": {
    "Created At": "",
    "Description": {},
    "Due Date": {},
    "ID": 0,
    "IID": {},
    "Project ID": {},
    "State": {},
    "Title": "",
    "Updated At": {}
  },
  "project_id": 0,
  "state": "",
  "subscribed": true,
  "title": "",
  "updated_at": "",
  "user_notes_count": 0,
  "web_url": ""
}
```

#### Delete User SSH Key
  
This action is used to delete user SSH key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID|None|None|
|key_id|integer|None|True|Key ID|None|None|
  
Example input:

```
{
  "id": 0,
  "key_id": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|Status|None|
  
Example output:

```
{
  "status": true
}
```

#### Delete User
  
This action is used to delete GitLab user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID to unblock|None|None|
  
Example input:

```
{
  "id": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|Status|None|
  
Example output:

```
{
  "status": true
}
```

#### Get User
  
This action is used to get GitLab user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID|None|None|
  
Example input:

```
{
  "id": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|avatar_url|string|False|Avatar URL|None|
|bio|string|False|Bio|None|
|created_at|date|False|Create at|None|
|id|integer|False|ID|None|
|linkedin|string|False|LinkedIn|None|
|location|string|False|Location|None|
|name|string|False|Name|None|
|organization|string|False|Organization|None|
|skype|string|False|Skype|None|
|state|string|False|State|None|
|twitter|string|False|Twitter|None|
|username|string|False|Username|None|
|web_url|string|False|Web URL|None|
|website_url|string|False|Website URL|None|
  
Example output:

```
{
  "avatar_url": "",
  "bio": "",
  "created_at": "",
  "id": 0,
  "linkedin": "",
  "location": "",
  "name": "",
  "organization": "",
  "skype": "",
  "state": "",
  "twitter": "",
  "username": "",
  "web_url": "",
  "website_url": ""
}
```

#### List User SSH Keys
  
This action is used to list user SSH keys

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID|None|None|
  
Example input:

```
{
  "id": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ssh_keys|[]ssh_output|False|SSH keys|None|
  
Example output:

```
{
  "ssh_keys": [
    {
      "Created At": "",
      "ID": 0,
      "SSH Key": {},
      "Title": ""
    }
  ]
}
```

#### Unblock User
  
This action is used to unlock GitLab user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID to unblock|None|None|
  
Example input:

```
{
  "id": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|False|Status|None|
  
Example output:

```
{
  "status": true
}
```
### Triggers


#### Issue
  
This trigger is used to monitor new issues

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|iids|integer|None|False|Return only the issues having the given iid|None|None|
|interval|integer|None|False|How often receive new issues|None|None|
|labels|string|None|True|Comma-separated list of label names, issues must have all labels to be returned|None|None|
|milestone|string|None|False|The milestone title|None|None|
|search|string|None|False|Search issues against their title and description|None|None|
|state|string|None|False|Return all issues or just those that are opened or closed|["Opened", "Closed"]|None|
  
Example input:

```
{
  "iids": 0,
  "interval": 0,
  "labels": "",
  "milestone": "",
  "search": "",
  "state": [
    "Opened",
    "Closed"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issue|object|False|Issue|None|
  
Example output:

```
{
  "issue": {}
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**ssh_output**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|date|None|False|Date SSH was created|None|
|ID|integer|None|False|SSH enumerated ID|None|
|SSH Key|string|None|False|RSA SSH key|None|
|Title|string|None|False|SSH Key title|None|
  
**user_output**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Avatar URL|string|None|False|User avatar URL|None|
|ID|integer|None|False|Unique user ID|None|
|Name|string|None|False|User full name|None|
|State|string|None|False|User state 'Active' or 'Inactive' |None|
|Username|string|None|False|User's username|None|
|Web URL|string|None|False|User profile URL|None|
  
**milestone_output**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|date|None|False|Date project was created|None|
|Description|string|None|False|Project Description|None|
|Due Date|date|None|False|Date project is to be closed|None|
|ID|integer|None|False|Unique milestone ID|None|
|IID|integer|None|False|Unique ID only in scope of a single project|None|
|Project ID|integer|None|False|Project ID|None|
|State|string|None|False|Project State e.g. 'Opened', 'Closed'|None|
|Title|string|None|False|Project title|None|
|Updated At|date|None|False|Date project was updated|None|
  
**issue_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assignees|[]integer|None|False|The ID of a user to assign issue|None|
|Confidential|boolean|None|False|Set an issue to be confidential|None|
|Created At|date|None|False|Date, ISO 8601 formatted (requires admin or project owner rights)|None|
|Description title|string|None|False|The description of an issue|None|
|Discussion To Resolve|string|None|False|The ID of a discussion to resolve|None|
|Due Date|date|None|False|Date time string in the format YEAR-MONTH-DAY|None|
|Labels|string|None|False|Comma-separated label names for an issue|None|
|Merge Request To Resolve Discussions Of|integer|None|False|The IID of a merge request in which to resolve all issues|None|
|Milestone|integer|None|False|The ID of a milestone to assign issue|None|
|Project ID|integer|None|True|ID of project|None|
|Issue title|string|None|True|The title of an issue|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History
  
*This plugin does not contain a version history.*

# Links


## References
  
*This plugin does not contain any references.*