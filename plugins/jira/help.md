# Description

[Jira](https://www.atlassian.com/software/jira) is an issue tracking product developed by Atlassian that allows teams to plan, track, and release great software. This plugin uses the [Jira REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v2/) to programmatically manage and create issues and users. The Jira plugin supports cloud (only with InsightConnect cloud connections) and on-premise versions of Jira Software, Jira Server, and Jira ServiceDesk products from Atlassian.

# Key Features

* Create, find, edit, comment, and generally manage your Jira tickets through the Jira REST API to expedite operations
* (Re-)Assign issues to users to orchestrate operations
* Find and create new users in your Jira instance to automate account provisioning

# Requirements

* URL for Jira Software, Jira Server, or Jira ServiceDesk
* Jira user email address and API key when using Jira Cloud (Only JIRA cloud is supported with InsightConnect cloud connections.)
* Jira username and password credentials when using on-prem Jira server

# Supported Product Versions

* Jira Server 6.0
* Jira (Cloud)
* Jira ServiceDesk (Cloud)

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|False|Jira API key when connecting to Jira Cloud or Jira user password when connecting to on-prem Jira server|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|pat|credential_secret_key|None|False|Jira Personal Access Token, only works with the on-prem Jira Server|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|url|string|https://example.atlassian.net|False|Jira URL|None|https://example.atlassian.net|None|None|
|user|string|None|False|Jira user email when connecting to Jira Cloud or Jira username when connecting to on-prem Jira server|None|user@example.com|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "pat": "9de5069c5afe602b2ea0a04b66beb2c0",
  "url": "https://example.atlassian.net",
  "user": "user@example.com"
}
```

## Technical Details

### Actions


#### Assign Issue

This action is used to assign an issue to a user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assignee|string|None|True|Username of assignee|None|user1|None|None|
|id|string|None|True|Issue ID|None|10001|None|None|
  
Example input:

```
{
  "assignee": "user1",
  "id": 10001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|True if successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Add Attachment to Issue

This action is used to add an attachment to an issue in Jira

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachment_bytes|bytes|None|True|Attachment bytes|None|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|None|None|
|attachment_filename|string|None|True|Attachment filename. Must end with a filetype extension if possible|None|document.pdf|None|None|
|id|string|None|True|Issue ID|None|10001|None|None|
  
Example input:

```
{
  "attachment_bytes": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA...",
  "attachment_filename": "document.pdf",
  "id": 10001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|string|False|ID of attachment|1234-abcd|
  
Example output:

```
{
  "id": "1234-abcd"
}
```

#### Comment Issue

This action is used to comment on an issue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment to add|None|This comment was added by InsightConnect|None|None|
|id|string|None|True|Issue ID|None|10001|None|None|
  
Example input:

```
{
  "comment": "This comment was added by InsightConnect",
  "id": 10001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|comment_id|string|False|Comment ID|1234-abcd|
  
Example output:

```
{
  "comment_id": "1234-abcd"
}
```

#### Create Issue

This action is used to create an issue in Jira

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachment_bytes|bytes|None|False|Attachment bytes|None|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|None|None|
|attachment_filename|string|None|False|Attachment filename|None|document.pdf|None|None|
|description|string||False|Issue description|None|Successfully connect Jira to InsightConnect to automate ticket management|None|None|
|fields|object|None|False|Custom fields to assign. Fields used must be present on the same screen as the Create screen in Jira|None|{ "fields": { "project": { "key": "TEST" }, "summary": "Test Ticket", "description": "Test ticket created from InsightConnect", "issuetype": { "name": "Story" } } }|None|None|
|project|string|None|True|Project ID|None|TEST|None|None|
|summary|string|None|False|Issue summary|None|Connect Jira to InsightConnect|None|None|
|type|string|Task|False|Issue type. Typical issues type include Task, Story, Epic, Bug. You can also specify a custom issue type. This input is case-sensitive|None|Story|None|None|
  
Example input:

```
{
  "attachment_bytes": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA...",
  "attachment_filename": "document.pdf",
  "description": "",
  "fields": {
    "fields": {
      "description": "Test ticket created from InsightConnect",
      "issuetype": {
        "name": "Story"
      },
      "project": {
        "key": "TEST"
      },
      "summary": "Test Ticket"
    }
  },
  "project": "TEST",
  "summary": "Connect Jira to InsightConnect",
  "type": "Task"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issue|issue|False|Created issue|{"id": 3}|
  
Example output:

```
{
  "issue": {
    "id": 3
  }
}
```

#### Create User

This action is used to create a user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|True|Email|None|user@example.com|None|None|
|notify|boolean|False|True|Notify if true|[True, False]|True|None|None|
|password|string|None|False|Password|None|mypassword|None|None|
|products|array|None|False|Products the new user has access to|None|["jira-core", "jira-servicedesk", "jira-product-discovery", "jira-software"]|None|None|
|username|string|None|False|Username|None|user1|None|None|
  
Example input:

```
{
  "email": "user@example.com",
  "notify": false,
  "password": "mypassword",
  "products": [
    "jira-core",
    "jira-servicedesk",
    "jira-product-discovery",
    "jira-software"
  ],
  "username": "user1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|True if successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete User

This action is used to delete a user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_id|string|None|False|Unique identifier for an Atlassian account|None|5ec00968833be70b7e50df20|None|None|
|username|string|None|False|Username|None|user1|None|None|
  
Example input:

```
{
  "account_id": "5ec00968833be70b7e50df20",
  "username": "user1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|True if successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Edit Issue

This action is used to edit an issue within Jira

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Description field on the issue|None|Update ticket with additional Jira information for others teams wanting to leverage InsightConnect|None|None|
|fields|object|None|False|An object of fields and values to change|None|{ "fields": { "project": { "key": "TEST" }, "summary": "Test Ticket", "description": "Test ticket created from InsightConnect", "issuetype": { "name": "Story" } } }|None|None|
|id|string|None|True|Issue ID|None|TEST-1|None|None|
|notify|boolean|True|True|Will send a notification email about the issue updated. Admin and project admins credentials need to be used to disable the notification|None|True|None|None|
|summary|string|None|False|Summary field on the issue|None|Connect Jira to InsightConnect for Multiple Teams|None|None|
|update|object|None|False|An object that contains update operations to apply, see examples at https://developer.atlassian.com/server/jira/platform/updating-an-issue-via-the-jira-rest-apis-6848604/|None|{ "update": { "labels": [ {"add": "newlabel"} ] } }|None|None|
  
Example input:

```
{
  "description": "Update ticket with additional Jira information for others teams wanting to leverage InsightConnect",
  "fields": {
    "fields": {
      "description": "Test ticket created from InsightConnect",
      "issuetype": {
        "name": "Story"
      },
      "project": {
        "key": "TEST"
      },
      "summary": "Test Ticket"
    }
  },
  "id": "TEST-1",
  "notify": true,
  "summary": "Connect Jira to InsightConnect for Multiple Teams",
  "update": {
    "update": {
      "labels": [
        {
          "add": "newlabel"
        }
      ]
    }
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|If changes were successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Find Issues

This action is used to search for issues

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|get_attachments|boolean|False|False|Get attachments from issue|None|True|None|None|
|jql|string|None|True|JQL search string to use|None|project = "TEST"|None|None|
|max|integer|10|True|Max results to return|None|10|None|None|
  
Example input:

```
{
  "get_attachments": false,
  "jql": "project = \"TEST\"",
  "max": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issues|[]issue|False|The list of found issues|[{"id": 1}, {"id": 2}]|
  
Example output:

```
{
  "issues": [
    {
      "id": 1
    },
    {
      "id": 2
    }
  ]
}
```

#### Find Users

This action is used to search for a set of users

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|max|integer|10|True|Max results to return|None|10|None|None|
|query|string|None|True|Query String, e.g. Joe|None|Joe|None|None|
  
Example input:

```
{
  "max": 10,
  "query": "Joe"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|users|[]user|False|The list of found users|[{"id": 1}]|
  
Example output:

```
{
  "users": [
    {
      "id": 1
    }
  ]
}
```

#### Get Comments

This action is used to retrieve all comments on an issue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Issue ID|None|TEST-1|None|None|
  
Example input:

```
{
  "id": "TEST-1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|comments|[]comment|False|Comments list|[{"id": 1}, {"id": 2}]|
|count|integer|False|Count of comments found|3|
  
Example output:

```
{
  "comments": [
    {
      "id": 1
    },
    {
      "id": 2
    }
  ],
  "count": 3
}
```

#### Get Issue

This action is used to retrieve an issue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|get_attachments|boolean|False|False|Get attachments from issue|None|True|None|None|
|id|string|None|True|Issue ID|None|TEST-1|None|None|
  
Example input:

```
{
  "get_attachments": false,
  "id": "TEST-1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|True|
|issue|issue|False|Found issue|{"id": 2}|
  
Example output:

```
{
  "found": true,
  "issue": {
    "id": 2
  }
}
```

#### Label Issue

This action is used to label issue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Issue ID|None|10001|None|None|
|label|string|None|True|Label to add. To add multiple labels, separate by commas|None|documentation|None|None|
  
Example input:

```
{
  "id": 10001,
  "label": "documentation"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|True if successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Transition Issue

This action is used to transition an issue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|False|Comment to add|None|Transition executed by InsightConnect|None|None|
|fields|object|None|False|Custom fields to assign. Fields used must be present on the screen used for project, issue, and transition type e.g: { "field1": { "attribute1": "value1" }, "field2": { "attribute2": "value2" }}|None|{ "fields": { "project": { "key": "TEST" }, "summary": "Test Ticket", "description": "Test ticket created from InsightConnect", "issuetype": { "name": "Story" } } }|None|None|
|id|string|None|True|Issue ID|None|10001|None|None|
|transition|string|None|True|ID or name of transition to perform, e.g. In Progress|None|31|None|None|
  
Example input:

```
{
  "comment": "Transition executed by InsightConnect",
  "fields": {
    "fields": {
      "description": "Test ticket created from InsightConnect",
      "issuetype": {
        "name": "Story"
      },
      "project": {
        "key": "TEST"
      },
      "summary": "Test Ticket"
    }
  },
  "id": 10001,
  "transition": 31
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|True if successful|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers


#### Monitor Issues

This trigger is used to watches for newly-created or updated issues

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|get_attachments|boolean|False|False|Get attachments from issue|None|True|None|None|
|include_fields|boolean|False|False|Whether returned Issues should include fields|None|True|None|None|
|interval|integer|60|False|Interval between next poll in seconds, default is 60 seconds|None|60|None|None|
|jql|string|None|False|JQL search string to use|None|reporter='Example User'|None|None|
|projects|[]string|None|False|List of Project IDs or names|None|TEST|None|None|
  
Example input:

```
{
  "get_attachments": false,
  "include_fields": false,
  "interval": 60,
  "jql": "reporter='Example User'",
  "projects": "TEST"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issue|issue|False|New or updated issue|{"id": 5}|
  
Example output:

```
{
  "issue": {
    "id": 5
  }
}
```

#### New Issue

This trigger is used to trigger which indicates that a new issue has been created

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|get_attachments|boolean|False|False|Get attachments from issue|None|True|None|None|
|include_fields|boolean|False|False|Whether returned Issues should include fields|None|True|None|None|
|jql|string|None|False|JQL search string to use|None|project = 'TEST'|None|None|
|poll_timeout|integer|60|False|Timeout between next poll, default 60|None|60|None|None|
|project|string|None|False|Project ID or name|None|TEST|None|None|
  
Example input:

```
{
  "get_attachments": false,
  "include_fields": false,
  "jql": "project = 'TEST'",
  "poll_timeout": 60,
  "project": "TEST"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issue|issue|False|New issue|{"id": 4}|
  
Example output:

```
{
  "issue": {
    "id": 4
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account ID|string|None|False|User account ID|None|
|active|boolean|None|False|Whether the user is active|None|
|display_name|string|None|False|User's display name|None|
|email_address|string|None|False|User's email address|None|
|name|string|None|False|User name|None|
  
**comment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|author|user|None|False|Author|None|
|body|string|None|False|Body of comment|None|
|id|string|None|False|Comment ID|None|
  
**issue**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|assignee|string|None|False|Assigned User|None|
|attachments|[]file|None|False|Attachments|None|
|created_at|string|None|False|Created At|None|
|description|string|None|False|Description|None|
|fields|object|None|False|Full list of fields|None|
|id|string|None|False|Issue ID|None|
|key|string|None|False|Issue Key|None|
|labels|[]string|None|False|Labels|None|
|project|string|None|False|Project|None|
|reporter|string|None|False|Reporting User|None|
|resolution|string|None|False|Resolution|None|
|resolved_at|string|None|False|Resolved At|None|
|status|string|None|False|Status|None|
|summary|string|None|False|Summary|None|
|updated_at|string|None|False|Updated At|None|
|url|string|None|False|Issue URL|None|


## Troubleshooting

* Please note only Jira cloud is supported with InsightConnect cloud. For JIRA OnPrem, please use an orchestrator for connecting.

# Version History

* 6.5.1 - Updated normalizing user object | Updated SDK to the latest version
* 6.5.0 - Cloud enable the plugin | Bump SDK version to 6.1.0 | Added an error message if trying to connect to Jira on-prem for ICON cloud
* 6.4.0 - Fix Issue Where Create Issue failed when multiple versions of the input Issue Type exists in Jira | Fix failed connection test response for PAT based connection | Include Fields input added to New Issue and Monitor Issues triggers, to specify whether to return Issue fields in the output | Removed empty Fields output from returned Issues when not requested or available
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