# Description

GitLab is a next generation developer collaboration software with version control capabilities. The GitLab InsightConnect plugin enables user and issue management

# Key Features
  
* Block and unblock users  
* Delete SSH keys  
* Retrieve users details  
* Create issues

# Requirements
  
* GitLab host URL  
* GitLab account username and password (or token)

# Supported Product Versions

* GitLab API v4

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Enter GitLab username and password (or token)|None|{'username': 'user_name', 'password': 'personal_access_token'}|None|None|
|ssl_verify|boolean|None|True|Toggle SSL verify on or off for requests|None|True|None|None|
|url|string|None|True|Host URL|None|https://gitlab.example.com:8000/api/v4/|None|None|

Example input:

```
{
  "credentials": {
    "password": "personal_access_token",
    "username": "user_name"
  },
  "ssl_verify": true,
  "url": "https://gitlab.example.com:8000/api/v4/"
}
```

## Technical Details

### Actions


#### Block User

This action is used to block GitLab user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID to block|None|17|None|None|
  
Example input:

```
{
  "id": 17
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Indicate if action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Create Issue

This action is used to create issue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assignee_ids|[]integer|None|False|The ID of a user to assign issue|None|[1, 2, 3, 4]|None|None|
|confidential|boolean|None|False|Set an issue to be confidential|None|False|None|None|
|created_at|date|None|False|Date, ISO 8601 formatted (requires admin or project owner rights)|None|2016-01-07 12:44:33.959000+00:00|None|None|
|description|string|None|False|The description of an issue|None|Description of the issue|None|None|
|discussion_resolve|string|None|False|The ID of a discussion to resolve|None|TheDiscussion|None|None|
|due_date|date|None|False|Date time string in the format YEAR-MONTH-DAY|None|2016-01-07 12:44:33.959000+00:00|None|None|
|labels|string|None|False|Comma-separated label names for an issue|None|False,Alert,Seen,Unseen|None|None|
|merge_request|integer|None|False|The IID of a merge request in which to resolve all issues|None|13|None|None|
|milestone_id|integer|None|False|The ID of a milestone to assign issue|None|23|None|None|
|project_id|integer|None|True|ID of project|None|4|None|None|
|title|string|None|True|The title of an issue|None|Issues with auth|None|None|
  
Example input:

```
{
  "assignee_ids": [
    1,
    2,
    3,
    4
  ],
  "confidential": false,
  "created_at": "2016-01-07 12:44:33.959000+00:00",
  "description": "Description of the issue",
  "discussion_resolve": "TheDiscussion",
  "due_date": "2016-01-07 12:44:33.959000+00:00",
  "labels": "False,Alert,Seen,Unseen",
  "merge_request": 13,
  "milestone_id": 23,
  "project_id": 4,
  "title": "Issues with auth"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issue|create_issue_output|False|Newly created issue|{'assignees': [{'avatar_url': 'None', 'id': 18, 'name': 'Alexandra Bashirian', 'state': 'active', 'username': 'eileen.lowe', 'web_url': 'https://gitlab.example.com/eileen.lowe'}, {'avatar_url': None, 'id': 19, 'name': 'John Smith', 'state': 'active', 'username': 'john.smith', 'web_url': 'https://gitlab.example.com/john.smith'}], 'author': {'avatar_url': None, 'id': 18, 'name': 'Alexandra Bashirian', 'state': 'active', 'username': 'eileen.lowe', 'web_url': 'https://gitlab.example.com/eileen.lowe'}, 'confidential': True, 'created_at': '2016-01-07 12:44:33.959000+00:00', 'description': 'Short description about the issue', 'due_date': '2016-01-07 12:44:33.959000+00:00', 'id': 12, 'iid': 12, 'labels': ['label1', 'label2', 'label3'], 'milestone': {'created_at': '2016-01-07 12:44:33.959000+00:00', 'description': 'project description', 'due_date': '2016-01-07 12:44:33.959000+00:00', 'id': 3, 'iid': 34, 'project_id': 3, 'state': 'Opened', 'title': 'project title', 'updated_at': '2016-01-07 12:44:33.959000+00:00'}, 'project_id': 13, 'state': 'opened', 'subscribed': True, 'title': 'Issues with auth', 'updated_at': '2016-01-07 12:44:33.959000+00:00', 'user_notes_count': 20, 'web_url': 'https://gitlab.example.com/eileen.lowe'}|
  
Example output:

```
{
  "issue": {
    "assignees": [
      {
        "avatar_url": "None",
        "id": 18,
        "name": "Alexandra Bashirian",
        "state": "active",
        "username": "eileen.lowe",
        "web_url": "https://gitlab.example.com/eileen.lowe"
      },
      {
        "avatar_url": null,
        "id": 19,
        "name": "John Smith",
        "state": "active",
        "username": "john.smith",
        "web_url": "https://gitlab.example.com/john.smith"
      }
    ],
    "author": {
      "avatar_url": null,
      "id": 18,
      "name": "Alexandra Bashirian",
      "state": "active",
      "username": "eileen.lowe",
      "web_url": "https://gitlab.example.com/eileen.lowe"
    },
    "confidential": true,
    "created_at": "2016-01-07 12:44:33.959000+00:00",
    "description": "Short description about the issue",
    "due_date": "2016-01-07 12:44:33.959000+00:00",
    "id": 12,
    "iid": 12,
    "labels": [
      "label1",
      "label2",
      "label3"
    ],
    "milestone": {
      "created_at": "2016-01-07 12:44:33.959000+00:00",
      "description": "project description",
      "due_date": "2016-01-07 12:44:33.959000+00:00",
      "id": 3,
      "iid": 34,
      "project_id": 3,
      "state": "Opened",
      "title": "project title",
      "updated_at": "2016-01-07 12:44:33.959000+00:00"
    },
    "project_id": 13,
    "state": "opened",
    "subscribed": true,
    "title": "Issues with auth",
    "updated_at": "2016-01-07 12:44:33.959000+00:00",
    "user_notes_count": 20,
    "web_url": "https://gitlab.example.com/eileen.lowe"
  }
}
```

#### Delete User SSH Key

This action is used to delete user SSH key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID|None|18|None|None|
|key_id|integer|None|True|Key ID|None|17|None|None|
  
Example input:

```
{
  "id": 18,
  "key_id": 17
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Indicate if action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete User

This action is used to delete GitLab user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID to unblock|None|34|None|None|
  
Example input:

```
{
  "id": 34
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Indicate if action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get User

This action is used to get GitLab user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID|None|17|None|None|
  
Example input:

```
{
  "id": 17
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|get_user_output|False|User profile|{'avatar_url': 'http://localhost:3000/uploads/user/avatar/1/cd8.jpeg', 'bio': 'Software engineer from blahblah I love coding', 'created_at': '2012-05-23 08:00:58+00:00', 'id': 17, 'linkedin': 'user@linkedin.com', 'location': 'East Coast', 'name': 'John Smith', 'organization': 'Rapid7', 'skype': 'user@skype.com', 'state': 'active', 'twitter': 'user@twitter.com', 'username': 'john_smith', 'web_url': 'http://localhost:3000/john_smith', 'website_url': 'john_smith@john_smith.com'}|
  
Example output:

```
{
  "user": {
    "avatar_url": "http://localhost:3000/uploads/user/avatar/1/cd8.jpeg",
    "bio": "Software engineer from blahblah I love coding",
    "created_at": "2012-05-23 08:00:58+00:00",
    "id": 17,
    "linkedin": "user@linkedin.com",
    "location": "East Coast",
    "name": "John Smith",
    "organization": "Rapid7",
    "skype": "user@skype.com",
    "state": "active",
    "twitter": "user@twitter.com",
    "username": "john_smith",
    "web_url": "http://localhost:3000/john_smith",
    "website_url": "john_smith@john_smith.com"
  }
}
```

#### List User SSH Keys

This action is used to list user SSH keys

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|The ID of the user|None|17|None|None|
  
Example input:

```
{
  "id": 17
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ssh_keys|[]ssh_output|False|SSH keys|[{"created_at": "12.02.23", "id": 17, "key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9wa++Oi7Qkr8prgHc4soW6NUlfDzpvZK2H5E7eQaSeP3SAwGmQKUFHCddNaP0L+hM7zhFNzjFvpaMgJw0=", "title": "MyPubKey"}, {"created_at": "12.02.23", "id": 18, "key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9wa++Oi7Qkr8prgHc4soW6NUlfDzpvZK2H5E7eQaSeP3SAwGmQKUFHCddNaP0L+hM7zhFNzjFvpaMgJw0=", "title": "MyPubKey2"}]|
  
Example output:

```
{
  "ssh_keys": [
    {
      "created_at": "12.02.23",
      "id": 17,
      "key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9wa++Oi7Qkr8prgHc4soW6NUlfDzpvZK2H5E7eQaSeP3SAwGmQKUFHCddNaP0L+hM7zhFNzjFvpaMgJw0=",
      "title": "MyPubKey"
    },
    {
      "created_at": "12.02.23",
      "id": 18,
      "key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9wa++Oi7Qkr8prgHc4soW6NUlfDzpvZK2H5E7eQaSeP3SAwGmQKUFHCddNaP0L+hM7zhFNzjFvpaMgJw0=",
      "title": "MyPubKey2"
    }
  ]
}
```

#### Unblock User

This action is used to unlock GitLab user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User ID to unblock|None|17|None|None|
  
Example input:

```
{
  "id": 17
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Indicate if action was successful|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers


#### Get New Issues

This trigger is used to monitor new issues

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|iids|[]integer|None|False|Return only the issues having the given iid|None|[116, 115]|None|None|
|interval|integer|None|False|How often to check for new issues|None|10|None|None|
|labels|string|None|False|Comma-separated list of label names, issues must have all labels to be returned|None|label1,label2,label3|None|None|
|milestone|string|None|False|The milestone title|None|v4.0|None|None|
|search|string|None|False|Search issues against their title and description|None|Example issue|None|None|
|state|string|None|False|Return all issues or just those that are opened or closed|["Opened", "Closed"]|Opened|None|None|
  
Example input:

```
{
  "iids": [
    116,
    115
  ],
  "interval": 10,
  "labels": "label1,label2,label3",
  "milestone": "v4.0",
  "search": "Example issue",
  "state": "Opened"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issue|object|False|Issue|{'state': 'opened', 'description': 'Ratione dolores corrupti mollitia soluta quia.', 'author': {'state': 'active', 'id': 18, 'web_url': 'https://gitlab.example.com/eileen.lowe', 'name': 'Alexandra Bashirian', 'avatar_url': None, 'username': 'eileen.lowe'}, 'milestone': {'project_id': 1, 'description': 'Ducimus nam enim ex consequatur cumque ratione.', 'state': 'closed', 'due_date': None, 'iid': 2, 'created_at': '2016-01-04T15:31:39.996Z', 'title': 'v4.0', 'id': 17, 'updated_at': '2016-01-04T15:31:39.996Z'}, 'project_id': 1, 'assignees': [{'state': 'active', 'id': 1, 'name': 'Administrator', 'web_url': 'https://gitlab.example.com/root', 'avatar_url': None, 'username': 'root'}], 'assignee': {'state': 'active', 'id': 1, 'name': 'Administrator', 'web_url': 'https://gitlab.example.com/root', 'avatar_url': None, 'username': 'root'}, 'type': 'ISSUE', 'updated_at': '2016-01-04T15:31:51.081Z', 'closed_at': None, 'closed_by': None, 'id': 76, 'title': 'Consequatur vero maxime deserunt laboriosam est voluptas dolorem.', 'created_at': '2016-01-04T15:31:51.081Z', 'moved_to_id': None, 'iid': 6, 'labels': ['foo', 'bar'], 'upvotes': 4, 'downvotes': 0, 'merge_requests_count': 0, 'user_notes_count': 1, 'due_date': '2016-07-22', 'web_url': 'http://gitlab.example.com/my-group/my-project/issues/6', 'references': {'short': '#6', 'relative': 'my-group/my-project#6', 'full': 'my-group/my-project#6'}, 'time_stats': {'time_estimate': 0, 'total_time_spent': 0, 'human_time_estimate': None, 'human_total_time_spent': None}, 'has_tasks': True, 'task_status': '10 of 15 tasks completed', 'confidential': False, 'discussion_locked': False, 'issue_type': 'issue', 'severity': 'UNKNOWN', '_links': {'self': 'http://gitlab.example.com/api/v4/projects/1/issues/76', 'notes': 'http://gitlab.example.com/api/v4/projects/1/issues/76/notes', 'award_emoji': 'http://gitlab.example.com/api/v4/projects/1/issues/76/award_emoji', 'project': 'http://gitlab.example.com/api/v4/projects/1', 'closed_as_duplicate_of': 'http://gitlab.example.com/api/v4/projects/1/issues/75'}, 'task_completion_status': {'count': 0, 'completed_count': 0}}|
  
Example output:

```
{
  "issue": {
    "_links": {
      "award_emoji": "http://gitlab.example.com/api/v4/projects/1/issues/76/award_emoji",
      "closed_as_duplicate_of": "http://gitlab.example.com/api/v4/projects/1/issues/75",
      "notes": "http://gitlab.example.com/api/v4/projects/1/issues/76/notes",
      "project": "http://gitlab.example.com/api/v4/projects/1",
      "self": "http://gitlab.example.com/api/v4/projects/1/issues/76"
    },
    "assignee": {
      "avatar_url": null,
      "id": 1,
      "name": "Administrator",
      "state": "active",
      "username": "root",
      "web_url": "https://gitlab.example.com/root"
    },
    "assignees": [
      {
        "avatar_url": null,
        "id": 1,
        "name": "Administrator",
        "state": "active",
        "username": "root",
        "web_url": "https://gitlab.example.com/root"
      }
    ],
    "author": {
      "avatar_url": null,
      "id": 18,
      "name": "Alexandra Bashirian",
      "state": "active",
      "username": "eileen.lowe",
      "web_url": "https://gitlab.example.com/eileen.lowe"
    },
    "closed_at": null,
    "closed_by": null,
    "confidential": false,
    "created_at": "2016-01-04T15:31:51.081Z",
    "description": "Ratione dolores corrupti mollitia soluta quia.",
    "discussion_locked": false,
    "downvotes": 0,
    "due_date": "2016-07-22",
    "has_tasks": true,
    "id": 76,
    "iid": 6,
    "issue_type": "issue",
    "labels": [
      "foo",
      "bar"
    ],
    "merge_requests_count": 0,
    "milestone": {
      "created_at": "2016-01-04T15:31:39.996Z",
      "description": "Ducimus nam enim ex consequatur cumque ratione.",
      "due_date": null,
      "id": 17,
      "iid": 2,
      "project_id": 1,
      "state": "closed",
      "title": "v4.0",
      "updated_at": "2016-01-04T15:31:39.996Z"
    },
    "moved_to_id": null,
    "project_id": 1,
    "references": {
      "full": "my-group/my-project#6",
      "relative": "my-group/my-project#6",
      "short": "#6"
    },
    "severity": "UNKNOWN",
    "state": "opened",
    "task_completion_status": {
      "completed_count": 0,
      "count": 0
    },
    "task_status": "10 of 15 tasks completed",
    "time_stats": {
      "human_time_estimate": null,
      "human_total_time_spent": null,
      "time_estimate": 0,
      "total_time_spent": 0
    },
    "title": "Consequatur vero maxime deserunt laboriosam est voluptas dolorem.",
    "type": "ISSUE",
    "updated_at": "2016-01-04T15:31:51.081Z",
    "upvotes": 4,
    "user_notes_count": 1,
    "web_url": "http://gitlab.example.com/my-group/my-project/issues/6"
  }
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
|Created At|date|None|False|Date project was created|2016-01-07 12:44:33.959000+00:00|
|Description|string|None|False|Project description|Description about the project|
|Due Date|date|None|False|Date project is to be closed|2016-01-07 12:44:33.959000+00:00|
|ID|integer|None|False|Unique milestone ID|2|
|IID|integer|None|False|Unique ID only in scope of a single project|23|
|Project ID|integer|None|False|Project ID|3|
|State|string|None|False|Project state|Opened|
|Title|string|None|False|Project title|Project title|
|Updated At|date|None|False|Date project was updated|2016-01-07 12:44:33.959000+00:00|
  
**get_user_output**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Avatar URL|string|None|False|Avatar URL|http://localhost:3000/uploads/user/avatar/1/cd8.jpeg|
|Bio|string|None|False|Bio|Software engineer from blahblah I love coding|
|Created At|date|None|False|Create at|2012-05-23 08:00:58+00:00|
|ID|integer|None|False|ID|17|
|LinkedIn|string|None|False|LinkedIn|user@linkedin.com|
|Location|string|None|False|Location|East Coast|
|Name|string|None|False|Name|John Smith|
|Organization|string|None|False|Organization|Rapid7|
|Skype|string|None|False|Skype|user@skype.com|
|State|string|None|False|State|active|
|Twitter|string|None|False|Twitter|user@twitter.com|
|Username|string|None|False|Username|john_smith|
|Web URL|string|None|False|Web URL|http://localhost:3000/john_smith|
|Website URL|string|None|False|Website URL|john_smith@john_smith.com|
  
**create_issue_output**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assignees|[]user_output|None|False|Assignees|[{"name": "Alexandra Bashirian", "avatar_url": "None", "state": "active", "web_url": "https://gitlab.example.com/eileen.lowe", "id": 18, "username": "eileen.lowe"}, {"name": "John Smith", "avatar_url": null, "state": "active", "web_url": "https://gitlab.example.com/john.smith", "id": 19, "username": "john.smith"}]|
|Author|user_output|None|False|Author|{'name': 'Alexandra Bashirian', 'avatar_url': None, 'state': 'active', 'web_url': 'https://gitlab.example.com/eileen.lowe', 'id': 18, 'username': 'eileen.lowe'}|
|Confidential|boolean|None|False|Confidential|True|
|Created At|date|None|False|Created at|2016-01-07 12:44:33.959000+00:00|
|Description|string|None|False|Description|Short description about the issue|
|Due Date|date|None|False|Due date|2016-01-07 12:44:33.959000+00:00|
|ID|integer|None|False|ID|12|
|IID|integer|None|False|IID|12|
|Labels|[]string|None|False|Labels|["label1", "label2", "label3"]|
|Milestone|milestone_output|None|False|Milestone|{'id': 3, 'project_id': 3, 'iid': 34, 'title': 'project title', 'description': 'project description', 'state': 'Opened', 'created_at': datetime.datetime(2016, 1, 7, 12, 44, 33, 959000, tzinfo=datetime.timezone.utc), 'updated_at': datetime.datetime(2016, 1, 7, 12, 44, 33, 959000, tzinfo=datetime.timezone.utc), 'due_date': datetime.datetime(2016, 1, 7, 12, 44, 33, 959000, tzinfo=datetime.timezone.utc)}|
|Project ID|integer|None|False|Project ID|13|
|State|string|None|False|State|opened|
|Subscribed|boolean|None|False|Subscribed|True|
|Title|string|None|False|Title|Issues with auth|
|Updated At|date|None|False|Updated at|2016-01-07 12:44:33.959000+00:00|
|User Notes Count|integer|None|False|User notes count|20|
|Web URL|string|None|False|Web URL|https://gitlab.example.com/eileen.lowe|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.1 - Update requirements.txt to remove dependencies | SDK bump to 6.2.0
* 2.0.0 - Update SDK | Refactor Plugin | `Connection` - New input: `ssl_verify` | `Issues` - Renamed to `Get New Issues` | Added unit tests
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [GitLab](https://gitlab.com)

## References

* [GitLab API](https://docs.gitlab.com/ce/api/README.html)