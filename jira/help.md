# Description

[Jira](https://www.atlassian.com/software/jira) is an issue tracking product developed by Atlassian that allows teams to plan, track, and release great software. This plugin uses the [Jira REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v2/) to programmatically manage and create issues and users. The Jira REST API supports the Jira Software, Jira Server, and Jira Help Desk products from Atlassian.

# Key Features

* Create, find, edit, comment, and generally manage your Jira tickets through the Jira REST API to expedite operations
* (Re-)Assign issues to users to orchestrate operations
* Find and create new users in your Jira instance to automate account provisioning

# Requirements

* Jira URL
* Administrative credentials

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and API key|None|None|
|url|string|https://company.atlassian.net|False|Jira URL, e.g. https://company.atlassian.net|None|https://company.atlassian.net|

## Technical Details

### Actions

#### Find Issues

This action is used to search for issues.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|get_attachments|boolean|False|False|Get attachments from issue|None|True|
|jql|string|None|True|JQL search string to use|None|project = "TEST"|
|max|integer|10|True|Max results to return|None|10|

Example input:

```
{
  "jql": "asdf",
  "max": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|[]issue|False|The list of found issues|

Example output:

```
{
  "issues": [{
      "id": "10001",
      "key": "PT-2",
      "url": "https://komand-demo2.atlassian.net/browse/PT-2",
      "summary": "Test ticket for the plugin-test project",
      "description": "A test ticket",
      "status": "To Do",
      "reporter": "Mike Rinehart",
      "created_at": "2018-10-29T12:58:11.222-0500",
      "updated_at": "2018-10-29T13:06:31.250-0500",
      "labels": ["Needs_test"],
      "fields": {}
  }]
}
```

#### Add Attachment to Issue

This action is used to add an attachment to an issue in Jira.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachment_bytes|bytes|None|True|Attachment bytes|None|dGVzdA==|
|attachment_filename|string|None|True|Attachment filename. Must end with a filetype extension if possible|None|test|
|id|string|None|True|Issue ID|None|10001|

Example input:

```
{
  "attachment_bytes": "dGVzdA==",
  "attachment_filename": "test",
  "id": "10001"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|ID of attachment|

Example output:

```
{
  "id": "10001"
}
```

#### Transition Issue

This action is used to transition an issue.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Comment to add|None|test|
|fields|object|None|False|Custom fields to assign. Fields used must be present on the screen used for project, issue, and transition type e.g: { "field1": { "attribute1": "value1" }, "field2": { "attribute2": "value2" }}|None|{}|
|id|string|None|True|Issue ID|None|10001|
|transition|string|None|True|ID or name of transition to perform, e.g. In Progress|None|31|

Example input:

```
{
  "comment": "test",
  "id": "10001",
  "transition": "31"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

Example output:

```
{
  "success": true
}
```

#### Delete User

This action is used to delete a user account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|username|string|None|True|Username|None|username|

Example input:

```
{
  "username": "test1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

Example output:

```
{
  "success": true
}
```

#### Assign Issue

This action is used to assign an issue to a user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignee|string|None|True|Username of assignee|None|me|
|id|string|None|True|Issue ID|None|10001|

Example input:

```
{
  "assignee": "me",
  "id": "10001"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

Example output:

```
{
  "success": true
}
```

#### Create Issue

This action is used to create an issue in Jira.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachment_bytes|bytes|None|False|Attachment bytes|None|dGVzdA==|
|attachment_filename|string|None|False|Attachment filename|None|test|
|description|string||False|Issue description|None|description|
|fields|object|None|False|Custom fields to assign. Fields used must be present on the same screen as the Create screen in Jira|None|{}|
|project|string|None|True|Project ID|None|TEST|
|summary|string|None|False|Issue summary|None|summary|
|type|string|Task|False|Issue type. Typical issues type include Task, Story, Epic, Bug. You can also specify a custom issue type. This input is case-sensitive|None|Bug|

Example input:

```
{
  "attachment_bytes": "",
  "attachment_filename": "",
  "description": "Test test",
  "fields": {},
  "project": "TEST",
  "summary": "Test issue",
  "type": "Story"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|issue|False|Created issue|

Example output:

```
{
  "attachments": [],
  "id": "10001",
  "key": "TEST-2",
  "url": "https://morecode-test2.atlassian.net/browse/TEST-2",
  "summary": "Test issue",
  "description": "Test test",
  "status": "Backlog",
  "resolution": "",
  "reporter": "Mateusz Górny",
  "assignee": "",
  "created_at": "2020-04-09T23:08:00.782+0200",
  "updated_at": "2020-04-09T23:08:00.782+0200",
  "resolved_at": "",
  "labels": [],
  "fields": {}
}
```

#### Create User

This action is used to create a user account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email|None|user@example.com|
|notify|boolean|False|True|Notify if true|[True, False]|False|
|password|string|None|False|Password|None|password|
|username|string|None|True|Username|None|username|

Example input:

```
{
  "email": "user@example.com",
  "notify": false,
  "password": "test",
  "username": "test1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

Example output:

```
{
  "success": true
}
```

#### Label Issue

This action is used to label an issue.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Issue ID|None|10001|
|label|string|None|True|Label to add. To add multiple labels, separate by commas|None|label|

Example input:

```
{
  "id": "10001",
  "label": "test"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

Example output:

```
{
  "success": true
}
```

#### Find Users

This action is used to find users.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|max|integer|10|True|Max results to return|None|10|
|query|string|None|True|Query String, e.g. Joe|None|Joe|

Example input:

```
{
  "max": 10,
  "query": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]user|False|The list of found users|

Example output:

```
{
  "users": [{
      "name": "mrinehart",
      "email_address": "user@example.com",
      "display_name": "Mike Test",
      "active": true
  }]
}
```

#### Comment Issue

This action is used to comment on an issue.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Comment to add|None|comment|
|id|string|None|True|Issue ID|None|10001|

Example input:

```
{
  "comment": "new comment",
  "id": "10001"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comment_id|string|False|Comment ID|

Example output:

```
{
  "comment_id": "10001"
}
```

#### Get Issue

This action is used to retrieve an issue.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|get_attachments|boolean|False|False|Get attachments from issue|None|False|
|id|string|None|True|Issue ID|None|TEST-1|

Example input:

```
{
  "id": "PT-2"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|issue|issue|False|Found issue|

Example output:

```
{
  "found": true,
  "issue": {
      "id": "10001",
      "key": "PT-2",
      "url": "https://komand-demo2.atlassian.net/browse/PT-2",
      "summary": "Test ticket for the plugin-test project",
      "description": "A test ticket",
      "status": "To Do",
      "resolution": "",
      "reporter": "Mike Rinehart",
      "assignee": "",
      "created_at": "2018-10-29T12:58:11.222-0500",
      "updated_at": "2018-10-29T13:06:31.250-0500",
      "resolved_at": "",
      "labels": ["Needs_test"],
      "fields": {
          "issuetype": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/issuetype/10002",
              "id": "10002",
              "description": "A task that needs to be done.",
              "iconUrl": "https://komand-demo2.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10318&avatarType=issuetype",
              "name": "Task",
              "subtask": false,
              "avatarId": 10318
          },
          "timespent": null,
          "project": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/project/10000",
              "id": "10000",
              "key": "PT",
              "name": "plugin-test",
              "projectTypeKey": "software",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              }
          },
          "fixVersions": [],
          "aggregatetimespent": null,
          "resolution": null,
          "resolutiondate": null,
          "workratio": -1,
          "lastViewed": null,
          "watches": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/issue/PT-2/watchers",
              "watchCount": 1,
              "isWatching": true
          },
          "created": "2018-10-29T12:58:11.222-0500",
          "customfield_10020": [],
          "customfield_10021": "0|i00007:",
          "customfield_10022": [],
          "priority": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/priority/3",
              "iconUrl": "https://komand-demo2.atlassian.net/images/icons/priorities/medium.svg",
              "name": "Medium",
              "id": "3"
          },
          "labels": ["Needs_test"],
          "customfield_10016": null,
          "customfield_10017": {
              "hasEpicLinkFieldDependency": false,
              "showField": false,
              "nonEditableReason": {
                  "reason": "PLUGIN_LICENSE_ERROR",
                  "message": "Portfolio for Jira must be licensed for the Parent Link to be available."
              }
          },
          "customfield_10018": null,
          "customfield_10019": null,
          "aggregatetimeoriginalestimate": null,
          "timeestimate": null,
          "versions": [],
          "issuelinks": [],
          "assignee": null,
          "updated": "2018-10-29T13:06:31.250-0500",
          "status": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/status/10001",
              "description": "",
              "iconUrl": "https://komand-demo2.atlassian.net/",
              "name": "To Do",
              "id": "10001",
              "statusCategory": {
                  "self": "https://komand-demo2.atlassian.net/rest/api/2/statuscategory/2",
                  "id": 2,
                  "key": "new",
                  "colorName": "blue-gray",
                  "name": "To Do"
              }
          },
          "components": [],
          "timeoriginalestimate": null,
          "description": "A test ticket",
          "customfield_10010": null,
          "customfield_10014": null,
          "timetracking": {},
          "customfield_10015": null,
          "customfield_10005": null,
          "customfield_10006": null,
          "security": null,
          "customfield_10007": null,
          "customfield_10008": null,
          "customfield_10009": null,
          "attachment": [],
          "aggregatetimeestimate": null,
          "summary": "Test ticket for the plugin-test project",
          "creator": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/user?username=admin",
              "name": "admin",
              "key": "admin",
              "accountId": "5bd733f3f8460347a10cbdd9",
              "emailAddress": "user@example.com",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              },
              "displayName": "Mike Rinehart",
              "active": true,
              "timeZone": "America/Chicago"
          },
          "subtasks": [],
          "reporter": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/user?username=admin",
              "name": "admin",
              "key": "admin",
              "accountId": "5bd733f3f8460347a10cbdd9",
              "emailAddress": "user@example.com",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              },
              "displayName": "Mike Rinehart",
              "active": true,
              "timeZone": "America/Chicago"
          },
          "aggregateprogress": {
              "progress": 0,
              "total": 0
          },
          "customfield_10000": "{}",
          "environment": null,
          "duedate": null,
          "progress": {
              "progress": 0,
              "total": 0
          },
          "votes": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/issue/PT-2/votes",
              "votes": 0,
              "hasVoted": false
          },
          "comment": {
              "comments": [{
                  "self": "https://komand-demo2.atlassian.net/rest/api/2/issue/10001/comment/10000",
                  "id": "10000",
                  "author": {
                      "self": "https://komand-demo2.atlassian.net/rest/api/2/user?username=admin",
                      "name": "admin",
                      "key": "admin",
                      "accountId": "5bd733f3f8460347a10cbdd9",
                      "emailAddress": "user@example.com",
                      "avatarUrls": {
                          "48x48": "",
                          "24x24": "",
                          "16x16": "",
                          "32x32": ""
                      },
                      "displayName": "Mike Rinehart",
                      "active": true,
                      "timeZone": "America/Chicago"
                  },
                  "body": "Needs additional testing",
                  "updateAuthor": {
                      "self": "https://komand-demo2.atlassian.net/rest/api/2/user?username=admin",
                      "name": "admin",
                      "key": "admin",
                      "accountId": "5bd733f3f8460347a10cbdd9",
                      "emailAddress": "user@example.com",
                      "avatarUrls": {
                          "48x48": "",
                          "24x24": "",
                          "16x16": "",
                          "32x32": ""
                      },
                      "displayName": "Mike Rinehart",
                      "active": true,
                      "timeZone": "America/Chicago"
                  },
                  "created": "2018-10-29T13:06:31.250-0500",
                  "updated": "2018-10-29T13:06:31.250-0500",
                  "jsdPublic": true
              }],
              "maxResults": 1,
              "total": 1,
              "startAt": 0
          },
          "worklog": {
              "startAt": 0,
              "maxResults": 20,
              "total": 0,
              "worklogs": []
          }
      }
  }
}
```

#### Get Comments

This action is used to retrieve all comments on an issue.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Issue ID|None|TEST-1|

Example input:

```
{
  "id": "PT-2"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comments|[]comment|False|Comments list|
|count|integer|False|Count of comments found|

Example output:

```
{
  "count": 1,
  "comments": [{
      "self": "https://komand-demo2.atlassian.net/rest/api/2/issue/10001/comment/10000",
      "id": "10000",
      "author": {
          "name": "admin",
          "email_address": "user@example.com",
          "display_name": "Mike Rinehart",
          "active": true
      },
      "body": "Needs additional testing",
      "updateAuthor": {
          "self": "https://komand-demo2.atlassian.net/rest/api/2/user?username=admin",
          "name": "admin",
          "key": "admin",
          "accountId": "5bd733f3f8460347a10cbdd9",
          "emailAddress": "user@example.com",
          "avatarUrls": {
              "48x48": "",
              "24x24": "",
              "16x16": "",
              "32x32": ""
          },
          "displayName": "Mike Rinehart",
          "active": true,
          "timeZone": "America/Chicago"
      },
      "created": "2018-10-29T13:06:31.250-0500",
      "updated": "2018-10-29T13:06:31.250-0500",
      "jsdPublic": true
  }]
}
```

#### Edit Issue

This action is used to edit an issue within Jira.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|False|Description field on the issue|None|description|
|fields|object|None|False|An object of fields and values to change|None|{}|
|id|string|None|True|Issue ID|None|TEST-1|
|notify|boolean|True|True|Will send a notification email about the issue updated. Admin and project admins credentials need to be used to disable the notification|None|False|
|summary|string|None|False|Summary field on the issue|None|summary|
|update|object|None|False|An object that contains update operations to apply|None|{}|

Example input:

Making an update to custom fields in the `fields` parameter:

```
{
  "customfield_10200" : {"value" : "Test 1"},
  "customfield_10201" :{"value" : "Value 1"}
}
```

Update the assignee in the `field` parameter

```
{
   "assignee":{"name":"harry"}
}
```

Using the `update` parameter

```
{
  "components" : [{"add" : {"name" : "Engine"}}]
}
```

Updating multiple fields with the `update` parameter

```
{
  "components" : [{"remove" : {"name" : "Trans/A"}}, {"add" : {"name" : "Trans/M"}}],
  "assignee" : [{"set" : {"name" : "harry"}}],
  "summary" : [{"set" : "Big block Chevy"}]
}
```

Additional information can be found [here](https://developer.atlassian.com/server/jira/platform/jira-rest-api-example-edit-issues-6291632/)

Example input:

```
{
  "description": "Updated from Komand",
  "fields": {},
  "id": "TEST-1",
  "notify": true,
  "update": {}
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|If changes were successful|

Example output:

```
{
  "success": True
}
```

### Triggers

#### New Issue

This trigger is used to trigger which indicates that a new issue has been created.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|get_attachments|boolean|False|False|Get attachments from issue|None|False|
|jql|string|None|False|JQL search string to use|None|project = "TEST"|
|poll_timeout|integer|60|False|Timeout between next poll, default 60|None|60|
|project|string|None|True|Project ID or name|None|TEST|

Example input:

```
{
  "jql": 'project = "TEST"'
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|issue|False|New issue|

Example output:

```
{
  "found": true,
  "issue": {
      "id": "10001",
      "key": "PT-2",
      "url": "https://komand-demo2.atlassian.net/browse/PT-2",
      "summary": "Test ticket for the plugin-test project",
      "description": "A test ticket",
      "status": "To Do",
      "resolution": "",
      "reporter": "Mike Rinehart",
      "assignee": "",
      "created_at": "2018-10-29T12:58:11.222-0500",
      "updated_at": "2018-10-29T13:06:31.250-0500",
      "resolved_at": "",
      "labels": ["Needs_test"],
      "fields": {
          "issuetype": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/issuetype/10002",
              "id": "10002",
              "description": "A task that needs to be done.",
              "iconUrl": "https://komand-demo2.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10318&avatarType=issuetype",
              "name": "Task",
              "subtask": false,
              "avatarId": 10318
          },
          "timespent": null,
          "project": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/project/10000",
              "id": "10000",
              "key": "PT",
              "name": "plugin-test",
              "projectTypeKey": "software",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              }
          },
          "fixVersions": [],
          "aggregatetimespent": null,
          "resolution": null,
          "resolutiondate": null,
          "workratio": -1,
          "lastViewed": null,
          "watches": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/issue/PT-2/watchers",
              "watchCount": 1,
              "isWatching": true
          },
          "created": "2018-10-29T12:58:11.222-0500",
          "customfield_10020": [],
          "customfield_10021": "0|i00007:",
          "customfield_10022": [],
          "priority": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/priority/3",
              "iconUrl": "https://komand-demo2.atlassian.net/images/icons/priorities/medium.svg",
              "name": "Medium",
              "id": "3"
          },
          "labels": ["Needs_test"],
          "customfield_10016": null,
          "customfield_10017": {
              "hasEpicLinkFieldDependency": false,
              "showField": false,
              "nonEditableReason": {
                  "reason": "PLUGIN_LICENSE_ERROR",
                  "message": "Portfolio for Jira must be licensed for the Parent Link to be available."
              }
          },
          "customfield_10018": null,
          "customfield_10019": null,
          "aggregatetimeoriginalestimate": null,
          "timeestimate": null,
          "versions": [],
          "issuelinks": [],
          "assignee": null,
          "updated": "2018-10-29T13:06:31.250-0500",
          "status": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/status/10001",
              "description": "",
              "iconUrl": "https://komand-demo2.atlassian.net/",
              "name": "To Do",
              "id": "10001",
              "statusCategory": {
                  "self": "https://komand-demo2.atlassian.net/rest/api/2/statuscategory/2",
                  "id": 2,
                  "key": "new",
                  "colorName": "blue-gray",
                  "name": "To Do"
              }
          },
          "components": [],
          "timeoriginalestimate": null,
          "description": "A test ticket",
          "customfield_10010": null,
          "customfield_10014": null,
          "timetracking": {},
          "customfield_10015": null,
          "customfield_10005": null,
          "customfield_10006": null,
          "security": null,
          "customfield_10007": null,
          "customfield_10008": null,
          "customfield_10009": null,
          "attachment": [],
          "aggregatetimeestimate": null,
          "summary": "Test ticket for the plugin-test project",
          "creator": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/user?username=admin",
              "name": "admin",
              "key": "admin",
              "accountId": "5bd733f3f8460347a10cbdd9",
              "emailAddress": "user@example.com",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              },
              "displayName": "Mike Rinehart",
              "active": true,
              "timeZone": "America/Chicago"
          },
          "subtasks": [],
          "reporter": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/user?username=admin",
              "name": "admin",
              "key": "admin",
              "accountId": "5bd733f3f8460347a10cbdd9",
              "emailAddress": "user@example.com",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              },
              "displayName": "Mike Rinehart",
              "active": true,
              "timeZone": "America/Chicago"
          },
          "aggregateprogress": {
              "progress": 0,
              "total": 0
          },
          "customfield_10000": "{}",
          "environment": null,
          "duedate": null,
          "progress": {
              "progress": 0,
              "total": 0
          },
          "votes": {
              "self": "https://komand-demo2.atlassian.net/rest/api/2/issue/PT-2/votes",
              "votes": 0,
              "hasVoted": false
          },
          "comment": {
              "comments": [{
                  "self": "https://komand-demo2.atlassian.net/rest/api/2/issue/10001/comment/10000",
                  "id": "10000",
                  "author": {
                      "self": "https://komand-demo2.atlassian.net/rest/api/2/user?username=admin",
                      "name": "admin",
                      "key": "admin",
                      "accountId": "5bd733f3f8460347a10cbdd9",
                      "emailAddress": "user@example.com",
                      "avatarUrls": {
                          "48x48": "",
                          "24x24": "",
                          "16x16": "",
                          "32x32": ""
                      },
                      "displayName": "Mike Rinehart",
                      "active": true,
                      "timeZone": "America/Chicago"
                  },
                  "body": "Needs additional testing",
                  "updateAuthor": {
                      "self": "https://komand-demo2.atlassian.net/rest/api/2/user?username=admin",
                      "name": "admin",
                      "key": "admin",
                      "accountId": "5bd733f3f8460347a10cbdd9",
                      "emailAddress": "user@example.com",
                      "avatarUrls": {
                          "48x48": "",
                          "24x24": "",
                          "16x16": "",
                          "32x32": ""
                      },
                      "displayName": "Mike Rinehart",
                      "active": true,
                      "timeZone": "America/Chicago"
                  },
                  "created": "2018-10-29T13:06:31.250-0500",
                  "updated": "2018-10-29T13:06:31.250-0500",
                  "jsdPublic": true
              }],
              "maxResults": 1,
              "total": 1,
              "startAt": 0
          },
          "worklog": {
              "startAt": 0,
              "maxResults": 20,
              "total": 0,
              "worklogs": []
          }
      }
  }
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

#

# Version History

* 4.0.3 - Fix user enumeration  in `Find Users` | Add example input | Fix title names to upper case
* 4.0.2 - Moved `apk add` in Dockerfile to use cache | Changed bare strings in params.get and output to static fields from schema | Remove duplicated code in actions | Changed `Exception` to `PluginException`
* 3.2.1 - Update Get Issue, Find Issues and New Issue action to support a Get Attachments option
* 3.2.0 - Update Transition Issue action to allow for assignment of fields during issue transition
* 3.1.2 - Update Create Issue action to remove newlines from summaries
* 3.1.1 - Update connection input labels to reflect Jira API changes
* 3.1.0 - Added new Edit Issue action
* 3.0.5 - Fix issue where description in Get Issue action would return None if description was left empty
* 3.0.4 - Improve error handling by checking for known issue type before creating ticket in Create Issue action
* 3.0.3 - Implement new connection test messaging
* 3.0.2 - Update action and trigger descriptions
* 3.0.1 - Fix issue where the New Issue trigger and Create Issue action may not output properly
* 3.0.0 - Rename 'Attach Issue' action to 'Add Attachment to Issue' | Update 'Create Issue' action description to include note about case sensitivity | Update 'Create Issue' action and 'New Issue' trigger to use uniform 'Issue' output type | Fix issue where attachments were not being uploaded properly | Fix issue where trigger could fail with an empty ticket description
* 2.0.1 - Fix issue where test method is missing in Create Issue action
* 2.0.0 - Support web server mode
* 1.0.4 - Update to v2 Python plugin architecture
* 1.0.3 - Fix custom fields adding to Create Issue request
* 1.0.2 - Fix custom fields input in Create Issue
* 1.0.1 - SSL bug fix in SDK
* 1.0.0 - Fix action: Create Issue
* 0.2.2 - Fix action: Find Issue
* 0.1.0 - Initial plugin

# Links

## References

* [Jira](https://www.atlassian.com/software/jira)

