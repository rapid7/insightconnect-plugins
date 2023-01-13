# Description

[Jira](https://www.atlassian.com/software/jira) is an issue tracking product developed by Atlassian that allows teams to plan, track, and release great software. This plugin uses the [Jira REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v2/) to programmatically manage and create issues and users. The Jira plugin supports cloud and on-premise versions of Jira Software, Jira Server, and Jira ServiceDesk products from Atlassian. 

# Key Features

* Create, find, edit, comment, and generally manage your Jira tickets through the Jira REST API to expedite operations
* (Re-)Assign issues to users to orchestrate operations 
* Find and create new users in your Jira instance to automate account provisioning

# Requirements

* URL for Jira Software, Jira Server, or Jira ServiceDesk
* Jira user email address and API key when using Jira Cloud
* Jira username and password credentials when using on-prem Jira server

# Supported Product Versions

* Jira Server 6.0
* Jira (Cloud)
* Jira ServiceDesk (Cloud)

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|False|Jira API key when connecting to Jira Cloud or Jira user password when connecting to on-prem Jira server|None|9de5069c5afe602b2ea0a04b66beb2c0|
|pat|credential_secret_key|None|False|Jira Personal Access Token, only works with the on-prem Jira Server|None|9de5069c5afe602b2ea0a04b66beb2c0|
|url|string|https://example.com|False|Jira URL|None|https://example.com|
|user|string|None|False|Jira user email when connecting to Jira Cloud or Jira username when connecting to on-prem Jira server|None|https://example.com|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "url": "https://example.atlassian.net",
  "user": "user@example.com"
}
```

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
  "get_attachments": true,
  "jql": "project = \"TEST\"",
  "max": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|issues|[]issue|False|The list of found issues|[{"id": 1}, {"id": 2}]|

Example output:

```
{
  "issues": [{
      "id": "10001",
      "key": "PT-2",
      "url": "https://example.atlassian.net/browse/PT-2",
      "summary": "Test ticket for the plugin-test project",
      "description": "A test ticket",
      "status": "To Do",
      "reporter": "User1",
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
|attachment_bytes|bytes|None|True|Attachment bytes|None|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|
|attachment_filename|string|None|True|Attachment filename. Must end with a filetype extension if possible|None|document.pdf|
|id|string|None|True|Issue ID|None|10001|

Example input:

```
{
  "attachment_bytes": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA...",
  "attachment_filename": "document.pdf",
  "id": 10001
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|ID of attachment|1234-abcd|

Example output:

```
{
  "id": "10001"
}
```

#### Transition Issue

This action is used to transition an issue.  For `fields` examples, see https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Comment to add|None|Transition executed by InsightConnect|
|fields|object|None|False|Custom fields to assign. Fields used must be present on the screen used for project, issue, and transition type e.g: { "field1": { "attribute1": "value1" }, "field2": { "attribute2": "value2" }}|None|{ "fields": { "project": { "key": "TEST" }, "summary": "Test Ticket", "description": "Test ticket created from InsightConnect", "issuetype": { "name": "Story" } } }|
|id|string|None|True|Issue ID|None|10001|
|transition|string|None|True|ID or name of transition to perform, e.g. In Progress|None|31|

Example input:

```
{
  "comment": "transition executed by insightconnect",
  "id": 10001,
  "transition": 31
}
```


##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|True if successful|True|

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
|account_id|string|None|False|Unique identifier for an Atlassian account|None|5ec00968833be70b7e50df20|
|username|string|None|False|Username|None|user1|

Example input:

```
{
  "account_id": "5ec00968833be70b7e50df20",
  "username": "user1"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|True if successful|True|

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
|assignee|string|None|True|Username of assignee|None|user1|
|id|string|None|True|Issue ID|None|10001|

Example input:

```
{
  "assignee": "user1",
  "id": 10001
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|True if successful|True|

Example output:

```
{
  "success": true
}
```

#### Create Issue

This action is used to create an issue in Jira.  For `fields` examples, see https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachment_bytes|bytes|None|False|Attachment bytes|None|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|
|attachment_filename|string|None|False|Attachment filename|None|document.pdf|
|description|string||False|Issue description|None|Successfully connect Jira to InsightConnect to automate ticket management|
|fields|object|None|False|Custom fields to assign. Fields used must be present on the same screen as the Create screen in Jira|None|{ "fields": { "project": { "key": "TEST" }, "summary": "Test Ticket", "description": "Test ticket created from InsightConnect", "issuetype": { "name": "Story" } } }|
|project|string|None|True|Project ID|None|TEST|
|summary|string|None|False|Issue summary|None|Connect Jira to InsightConnect|
|type|string|Task|False|Issue type. Typical issues type include Task, Story, Epic, Bug. You can also specify a custom issue type. This input is case-sensitive|None|Story|

Example input:

```
{
  "attachment_bytes": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA...",
  "attachment_filename": "document.pdf",
  "description": "Successfully connect Jira to InsightConnect to automate ticket management"
}
```


##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|issue|False|Created issue|{"id": 3}|

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
  "reporter": "User2",
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
|notify|boolean|False|True|Notify if true|[True, False]|True|
|password|string|None|False|Password|None|mypassword|
|username|string|None|False|Username|None|user1|

Example input:

```
{
  "email": "user@example.com",
  "notify": true,
  "password": "mypassword",
  "username": "user1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|True|

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
|label|string|None|True|Label to add. To add multiple labels, separate by commas|None|documentation|

Example input:

```
{
  "id": 10001,
  "label": "documentation"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|True if successful|True|

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
  "query": "Joe"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|users|[]user|False|The list of found users|[{"id": 1}]|


Example output:

```
{
  "users": [
    {
      "account_id": "5ebaff48acdf9c0b917dac88",
      "active": true,
      "display_name": "user1",
      "email_address": "user@example.com"
    }
  ]
}
```

#### Comment Issue

This action is used to comment on an issue.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Comment to add|None|This comment was added by InsightConnect|
|id|string|None|True|Issue ID|None|10001|

Example input:

```
{
  "comment": "This comment was added by InsightConnect",
  "id": 10001
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comment_id|string|False|Comment ID|1234-abcd|

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
|get_attachments|boolean|False|False|Get attachments from issue|None|True|
|id|string|None|True|Issue ID|None|TEST-1|

Example input:

```
{
  "get_attachments": true,
  "id": "TEST-1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|True|
|issue|issue|False|Found issue|{"id": 2}|

Example output:

```
{
  "found": true,
  "issue": {
      "id": "10001",
      "key": "PT-2",
      "url": "https://example.atlassian.net/browse/PT-2",
      "summary": "Test ticket for the plugin-test project",
      "description": "A test ticket",
      "status": "To Do",
      "resolution": "",
      "reporter": "User1",
      "assignee": "",
      "created_at": "2018-10-29T12:58:11.222-0500",
      "updated_at": "2018-10-29T13:06:31.250-0500",
      "resolved_at": "",
      "labels": ["Needs_test"],
      "fields": {
          "issuetype": {
              "self": "https://example.atlassian.net/rest/api/2/issuetype/10002",
              "id": "10002",
              "description": "A task that needs to be done.",
              "iconUrl": "https://example.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10318&avatarType=issuetype",
              "name": "Task",
              "subtask": false,
              "avatarId": 10318
          },
          "timespent": null,
          "project": {
              "self": "https://example.atlassian.net/rest/api/2/project/10000",
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
              "self": "https://example.atlassian.net/rest/api/2/issue/PT-2/watchers",
              "watchCount": 1,
              "isWatching": true
          },
          "created": "2018-10-29T12:58:11.222-0500",
          "customfield_10020": [],
          "customfield_10021": "0|i00007:",
          "customfield_10022": [],
          "priority": {
              "self": "https://example.atlassian.net/rest/api/2/priority/3",
              "iconUrl": "https://example.atlassian.net/images/icons/priorities/medium.svg",
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
              "self": "https://example.atlassian.net/rest/api/2/status/10001",
              "description": "",
              "iconUrl": "https://example.atlassian.net/",
              "name": "To Do",
              "id": "10001",
              "statusCategory": {
                  "self": "https://example.atlassian.net/rest/api/2/statuscategory/2",
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
              "self": "https://example.atlassian.net/rest/api/2/user?username=admin",
              "name": "admin",
              "key": "admin",
              "accountId": "4ac123f3f8412345a10cbaa0",
              "emailAddress": "user@example.com",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              },
              "displayName": "User1",
              "active": true,
              "timeZone": "America/Chicago"
          },
          "subtasks": [],
          "reporter": {
              "self": "https://example.atlassian.net/rest/api/2/user?username=admin",
              "name": "admin",
              "key": "admin",
              "accountId": "4ac123f3f8412345a10cbaa0",
              "emailAddress": "user@example.com",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              },
              "displayName": "User1",
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
              "self": "https://example.atlassian.net/rest/api/2/issue/PT-2/votes",
              "votes": 0,
              "hasVoted": false
          },
          "comment": {
              "comments": [{
                  "self": "https://example.atlassian.net/rest/api/2/issue/10001/comment/10000",
                  "id": "10000",
                  "author": {
                      "self": "https://example.atlassian.net/rest/api/2/user?username=admin",
                      "name": "admin",
                      "key": "admin",
                      "accountId": "4ac123f3f8412345a10cbaa0",
                      "emailAddress": "user@example.com",
                      "avatarUrls": {
                          "48x48": "",
                          "24x24": "",
                          "16x16": "",
                          "32x32": ""
                      },
                      "displayName": "User1",
                      "active": true,
                      "timeZone": "America/Chicago"
                  },
                  "body": "Needs additional testing",
                  "updateAuthor": {
                      "self": "https://example.atlassian.net/rest/api/2/user?username=admin",
                      "name": "admin",
                      "key": "admin",
                      "accountId": "4ac123f3f8412345a10cbaa0",
                      "emailAddress": "user@example.com",
                      "avatarUrls": {
                          "48x48": "",
                          "24x24": "",
                          "16x16": "",
                          "32x32": ""
                      },
                      "displayName": "User1",
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
  "id": "TEST-1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comments|[]comment|False|Comments list|[{"id": 1}, {"id": 2}]|
|count|integer|False|Count of comments found|3|

Example output:

```
{
  "count":1,
  "comments":[
    {
      "self":"https://example.atlassian.net/rest/api/2/issue/10001/comment/10000",
      "id":"10000",
      "author":{
        "name":"admin",
        "email_address":"user@example.com",
        "display_name":"User1",
        "active":true
      },
      "body":"Needs additional testing",
      "updateAuthor":{
        "self":"https://example.atlassian.net/rest/api/2/user?username=admin",
        "name":"admin",
        "key":"admin",
        "accountId":"4ac123f3f8412345a10cbaa0",
        "emailAddress":"user@example.com",
        "avatarUrls":{
          "48x48":"",
          "24x24":"",
          "16x16":"",
          "32x32":""
        },
        "displayName":"User1",
        "active":true,
        "timeZone":"America/Chicago"
      },
      "created":"2018-10-29T13:06:31.250-0500",
      "updated":"2018-10-29T13:06:31.250-0500",
      "jsdPublic":true
    }
  ]
}
```

#### Edit Issue

This action is used to edit an issue within Jira. See https://developer.atlassian.com/server/jira/platform/updating-an-issue-via-the-jira-rest-apis-6848604/ for `update` examples.
For `fields` examples, see https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|False|Description field on the issue|None|Update ticket with additional Jira information for others teams wanting to leverage InsightConnect|
|fields|object|None|False|An object of fields and values to change|None|{ "fields": { "project": { "key": "TEST" }, "summary": "Test Ticket", "description": "Test ticket created from InsightConnect", "issuetype": { "name": "Story" } } }|
|id|string|None|True|Issue ID|None|TEST-1|
|notify|boolean|True|True|Will send a notification email about the issue updated. Admin and project admins credentials need to be used to disable the notification|None|True|
|summary|string|None|False|Summary field on the issue|None|Connect Jira to InsightConnect for Multiple Teams|
|update|object|None|False|An object that contains update operations to apply, see examples at https://developer.atlassian.com/server/jira/platform/updating-an-issue-via-the-jira-rest-apis-6848604/|None|{ "update": { "labels": [ {"add": "newlabel"} ] } }|


Example input:

```
{
  "description": "Update ticket with additional Jira information for others teams wanting to leverage InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|If changes were successful|True|

Example output:

```
{
  "success": True
}
```

### Triggers

#### Monitor Issues

This trigger watches for newly-created or updated issues.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|get_attachments|boolean|False|False|Get attachments from issue|None|True|
|interval|integer|60|False|Interval between next poll in seconds, default is 60 seconds|None|60|
|jql|string|None|False|JQL search string to use|None|reporter='Example User'|
|projects|[]string|None|False|List of Project IDs or names|None|TEST|

Example input:

```
{
  "get_attachments": true,
  "interval": 60,
  "jql": "reporter='Example User'",
  "projects": "TEST"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|issue|False|New or updated issue|{"id": 5}|

Example output:

```
{
  'attachments': [
    {
      'filename': 'test',
      'content': 'VGVzdA=='
    }
  ],
  'id': '15466',
  'key': 'TEST-1',
  'url': 'https://example.atlassian.net/browse/TEST-1',
  'summary': 'Test',
  'description': 'Test',
  'status': 'To Do',
  'resolution': '',
  'reporter': 'Example User',
  'assignee': '',
  'created_at': '2021-07-06T12:37:54.250-0400',
  'updated_at': '2021-07-23T04:38:23.281-0400',
  'resolved_at': '',
  'labels': ["example_label"],
  'fields': {}
}
```

#### New Issue

This trigger is used to trigger which indicates that a new issue has been created.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|get_attachments|boolean|False|False|Get attachments from issue|None|True|
|jql|string|None|False|JQL search string to use|None|project = 'TEST'|
|poll_timeout|integer|60|False|Timeout between next poll, default 60|None|60|
|project|string|None|False|Project ID or name|None|TEST|

Example input:

```
{
  "get_attachments": true,
  "jql": "project = 'TEST'",
  "poll_timeout": 60,
  "project": "TEST"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issue|issue|False|New issue|{"id": 4}|

Example output:

```
{
  "found": true,
  "issue": {
      "id": "10001",
      "key": "PT-2",
      "url": "https://example.atlassian.net/browse/PT-2",
      "summary": "Test ticket for the plugin-test project",
      "description": "A test ticket",
      "status": "To Do",
      "resolution": "",
      "reporter": "User1",
      "assignee": "",
      "created_at": "2018-10-29T12:58:11.222-0500",
      "updated_at": "2018-10-29T13:06:31.250-0500",
      "resolved_at": "",
      "labels": ["Needs_test"],
      "fields": {
          "issuetype": {
              "self": "https://example.atlassian.net/rest/api/2/issuetype/10002",
              "id": "10002",
              "description": "A task that needs to be done.",
              "iconUrl": "https://example.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10318&avatarType=issuetype",
              "name": "Task",
              "subtask": false,
              "avatarId": 10318
          },
          "timespent": null,
          "project": {
              "self": "https://example.atlassian.net/rest/api/2/project/10000",
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
              "self": "https://example.atlassian.net/rest/api/2/issue/PT-2/watchers",
              "watchCount": 1,
              "isWatching": true
          },
          "created": "2018-10-29T12:58:11.222-0500",
          "customfield_10020": [],
          "customfield_10021": "0|i00007:",
          "customfield_10022": [],
          "priority": {
              "self": "https://example.atlassian.net/rest/api/2/priority/3",
              "iconUrl": "https://example.atlassian.net/images/icons/priorities/medium.svg",
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
              "self": "https://example.atlassian.net/rest/api/2/status/10001",
              "description": "",
              "iconUrl": "https://example.atlassian.net/",
              "name": "To Do",
              "id": "10001",
              "statusCategory": {
                  "self": "https://example.atlassian.net/rest/api/2/statuscategory/2",
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
              "self": "https://example.atlassian.net/rest/api/2/user?username=admin",
              "name": "admin",
              "key": "admin",
              "accountId": "4ac123f3f8412345a10cbaa0",
              "emailAddress": "userexample.com",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              },
              "displayName": "User1",
              "active": true,
              "timeZone": "America/Chicago"
          },
          "subtasks": [],
          "reporter": {
              "self": "https://example.atlassian.net/rest/api/2/user?username=admin",
              "name": "admin",
              "key": "admin",
              "accountId": "4ac123f3f8412345a10cbaa0",
              "emailAddress": "user@example.com",
              "avatarUrls": {
                  "48x48": "",
                  "24x24": "",
                  "16x16": "",
                  "32x32": ""
              },
              "displayName": "User1",
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
              "self": "https://example.atlassian.net/rest/api/2/issue/PT-2/votes",
              "votes": 0,
              "hasVoted": false
          },
          "comment": {
              "comments": [{
                  "self": "https://example.atlassian.net/rest/api/2/issue/10001/comment/10000",
                  "id": "10000",
                  "author": {
                      "self": "https://example.atlassian.net/rest/api/2/user?username=admin",
                      "name": "admin",
                      "key": "admin",
                      "accountId": "4ac123f3f8412345a10cbaa0",
                      "emailAddress": "user@example.com",
                      "avatarUrls": {
                          "48x48": "",
                          "24x24": "",
                          "16x16": "",
                          "32x32": ""
                      },
                      "displayName": "User1",
                      "active": true,
                      "timeZone": "America/Chicago"
                  },
                  "body": "Needs additional testing",
                  "updateAuthor": {
                      "self": "https://example.atlassian.net/rest/api/2/user?username=admin",
                      "name": "admin",
                      "key": "admin",
                      "accountId": "4ac123f3f8412345a10cbaa0",
                      "emailAddress": "user@example.com",
                      "avatarUrls": {
                          "48x48": "",
                          "24x24": "",
                          "16x16": "",
                          "32x32": ""
                      },
                      "displayName": "User1",
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

_This plugin does not contain any troubleshooting information._

# Version History

* 6.3.1 - Fix Issue Where Create Issue failed when multiple versions of the input Issue Type exists in Jira | Fix failed connection test response for PAT based connection | Fix Issue where Fields output was no returned in New Issue Trigger and Monitor Issues Trigger
* 6.3.0 - Add PAT authentication scheme for Jira on-prem
* 6.2.1 - Fix issue in Find Issues action where normalize_user has an attribute error for labels | Changed Dockerfile to don't use slim version
* 6.2.0 - Fix issue in Get Comments actions where normalize_user is missing the is_cloud argument from client connection
* 6.1.1 - Fix issue where attachments added in tickets were empty
* 6.1.0 - Add Monitor Issues trigger | Update New Issue trigger to only trigger in case of recently created tickets | Change `required` property to false for `project` input in New Issue trigger | Fix issue in New Issue trigger to include all results that match JQL | Fix issue in New Issue trigger with retrieving attachments
* 6.0.8 - Fix issue where exception type was wrong in Create Issue
* 6.0.7 - Fix issue in Create Issue and Attach Issue actions where adding attachments failed
* 6.0.6 - Fix build issue
* 6.0.5 - Add more documentation on authentication
* 6.0.4 - Update to v4 Python plugin runtime
* 6.0.3 - Add `docs_url` to plugin spec with link to [plugin setup guide](https://docs.rapid7.com/insightconnect/jira)
* 6.0.2 - Fix in Comment Issue action where the Python module attributes were logged | Remove duplicate ConnectionTestException call from Connection Test
* 6.0.1 - Update documentation to include supported Jira products
* 6.0.0 - Update Create User, Delete User and Find Users to reflect [Jira Cloud API privacy changes](https://developer.atlassian.com/cloud/jira/platform/api-changes-for-user-privacy-announcement/) to support `accountId` | Fix issue in connection test where the error was logged but did not fail for users | Update connection schema to match the API key and username inputs
* 5.0.0 - Fix user enumeration  in `Find Users` | Add example input | Update titles of Attachment Filename input in Attach Issue action and Poll Timeout input in New Issue trigger to match style
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

* [Jira](https://www.atlassian.com/software/jira)

## References

* [Jira](https://www.atlassian.com/software/jira)
