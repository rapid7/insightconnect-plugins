# Description

The [Zendesk](https://www.zendesk.com) plugin helps manage communication with customers. This plugin allows you to manage tickets and users in Zendesk. Customer Resource Management tool to manage tickets of user complaints and support issues.

This plugin utilizes the [Zendesk Python SDK](https://github.com/facetoe/zenpy).

# Key Features

* Create, manage, and delete issues and epics
* Retrieve data about events, issues, epics, and boards

# Requirements

* A Zendesk API key
* Information about your Zendesk instance

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|False|Zendesk API key|None|
|credentials|credential_username_password|None|True|Email and password|None|
|subdomain|string|None|True|Zendesk subdomain|None|

## Technical Details

### Actions

#### Search

This action is used to search Zendesk.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|item|string|None|True|Search item E.g. password reset|None|
|type|string|None|True|Search type|['User', 'Organization', 'Ticket']|

Example input:

```
{
  "item": "Alex",
  "type": "User"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]object|False|Get Zendesk query results|

Example output:

```

{
  "results": [
    {
      "active": true,
      "alias": null,
      "chat_only": false,
      "created_at": "2018-01-26T14:24:58Z",
      "custom_role_id": null,
      "details": null,
      "email": "user@example.com",
      "external_id": null,
      "id": 360385011372,
      "last_login_at": "2018-05-25T12:27:14Z",
      "locale": "en-US",
      "locale_id": 1,
      "moderator": true,
      "name": "Jen Andre",
      "notes": null,
      "only_private_comments": false,
      "organization_id": 360002530352,
      "phone": null,
      "photo": {
        "url": "https://komand.zendesk.com/api/v2/attachments/360004125291.json",
        "id": 360004125291,
        "file_name": "profile_image_360385011372_2206139.png",
        "content_url": "https://komand.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139.png",
        "mapped_content_url": "https://komand.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139.png",
        "content_type": "image/png",
        "size": 1141,
        "width": 80,
        "height": 80,
        "inline": false,
        "thumbnails": [
          {
            "url": "https://komand.zendesk.com/api/v2/attachments/360004125311.json",
            "id": 360004125311,
            "file_name": "profile_image_360385011372_2206139_thumb.png",
            "content_url": "https://komand.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139_thumb.png",
            "mapped_content_url": "https://komand.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139_thumb.png",
            "content_type": "image/png",
            "size": 601,
            "width": 32,
            "height": 32,
            "inline": false
          }
        ]
      },
      "restricted_agent": false,
      "role": "admin",
      "shared": false,
      "shared_agent": false,
      "signature": null,
      "suspended": false,
      "tags": [],
      "ticket_restriction": null,
      "time_zone": "Bogota",
      "two_factor_auth_enabled": null,
      "updated_at": "2018-05-25T12:27:20Z",
      "url": "https://komand.zendesk.com/api/v2/users/360385011372.json",
      "verified": true
    }
  ]
}

```

#### Delete Ticket

This action is used to delete a ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ticket_id|string|None|True|Delete ticket|None|

Example input:

```
{
  "ticket_id": "20181554587"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Success or failure|

#### Delete Membership

This action is used to delete an organization membership.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|membership_id|string|None|True|ID of membership to delete E.g. 1657574807|None|

Example input:

```
{
  "membership_id": "1657574807"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Success or failure|

#### Show User

This action is used to retrieve user information.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|ID of user to show E.g. 20444826487|None|

Example input:

```
{
  "user_id": "361738647591"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|object|True|User meta data|

#### Suspend User

This action is used to suspend a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|ID of user to delete E.g. 20444826487|None|

Example input:

```
{
  "user_id": "361738647591"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Success or failure|

#### Delete User

This action is used to delete a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|ID of user to delete E.g. 20444826487|None|

Example input:

```
{
  "user_id": "361738647591"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Success or failure|

#### Create Ticket

This action is used to create a ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|assignee_id|string|None|False|Assignee ID|None|
|attachment|file|None|False|Optional file attachment|None|
|collaborator_ids|[]string|None|False|List of collaborator IDs|None|
|description|string|None|True|Ticket description|None|
|due_at|date|None|False|Time ticket is due|None|
|external_id|string|None|False|Support ticket ID|None|
|group_id|integer|None|False|Group ID|None|
|priority|string|None|False|Ticket priority|['Urgent', 'High', 'Normal', 'Low', '']|
|problem_id|string|None|False|For tickets of type 'incident', the numeric ID of the problem the incident is linked to|None|
|recipient|string|None|False|ID of user recipient|None|
|requester_id|string|None|False|ID of user requesting support|None|
|status|string|None|False|Ticket status|['New', 'Open', 'Pending', 'Hold', 'Solved', 'Closed', '']|
|subject|string|None|True|Subject of ticket|None|
|tags|[]string|None|False|Tags describing ticket|None|
|type|string|None|False|Ticket type|['Problem', 'Incident', 'Task', 'Question', '']|

Example input:

```
{
  "assignee_id":"20241548208",
  "attachment":{
    "content":"heyMAX",
    "filename":"hello.txt"
  },
  "collaborator_ids":[
    "20241548208",
    "20180428207"
  ],
  "description":"Hello description",
  "due_at":"2017-03-20T23:03:32.114196",
  "external_id":"22",
  "priority":"High",
  "problem_id":"14",
  "recipient":"20243926068",
  "requester_id":"20243926068",
  "status":"Pending",
  "subject":"hello Subject",
  "tags":[
    "Peace",
    "Love",
    "Happiness"
  ],
  "type":"Incident"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket|object|False|Ticket meta data|

#### Update Ticket

This action is used to update ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|assignee_id|string|None|False|Assignee ID|None|
|collaborator_ids|[]string|None|False|List of collaborator IDs|None|
|comment|comment|None|False|Comment|None|
|due_at|date|None|False|Time ticket is due|None|
|external_id|string|None|False|Support ticket ID|None|
|group_id|string|None|False|Group ID|None|
|priority|string|None|False|Ticket priority|['Urgent', 'High', 'Normal', 'Low', '']|
|problem_id|string|None|False|For tickets of type 'incident', the numeric ID of the problem the incident is linked to|None|
|recipient|string|None|False|ID of user recipient|None|
|requester_id|string|None|True|ID of user requesting support|None|
|status|string|None|False|Ticket status|['New', 'Open', 'Pending', 'Hold', 'Solved', 'Closed', '']|
|subject|string|None|False|Subject of ticket|None|
|tags|[]string|None|False|Tags describing ticket|None|
|ticket_id|string|None|True|Ticket ID|None|
|type|string|None|False|Ticket type|['Problem', 'Incident', 'Task', 'Question', '']|

Example input:

```
{
  "assignee_id":"",
  "comment":{
    "author_id":"435353535",
    "body":"Test comment",
    "html_body":"<u>Test Underlined comment</u>",
    "public":true
  },
  "collaborator_ids":[
    "20241548208",
    "20180428207"
  ],
  "due_at":"2017-03-20T23:03:32.114196",
  "external_id":"57",
  "group_id":"22",
  "description":"New description",
  "priority":"Urgent",
  "problem_id":"14",
  "recipient":"20243926068",
  "requester_id":"406059378433",
  "status":"Open",
  "subject":"New Subject",
  "tags":[
    "tag1",
    "tag2"
  ],
  "ticket_id":"53",
  "type":"Problem"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket|ticket|True|Ticket meta data|

Example output:

```

{
  "assignee_id":"",
  "brand_id":360000066092,
  "comment":{
    "author_id":"435353535",
    "body":"Test comment",
    "html_body":"<u>Test Underlined comment</u>",
    "public":true
  },
  "collaborator_ids":[

  ],
  "created_at":"2018-05-01T15:36:04Z",
  "description":"",
  "due_at":"0001-01-01T00:00:00Z",
  "external_id":"",
  "forum_topic_id":null,
  "group_id":"",
  "has_incidents":false,
  "id":399,
  "organization_id":null,
  "priority":null,
  "problem_id":"",
  "raw_subject":"some ticket",
  "recipient":"",
  "requester_id":"360386052052",
  "sharing_agreement_ids":[

  ],
  "status":"new",
  "subject":"I want to change things",
  "submitter_id":363945031071,
  "tags":[

  ],
  "type":null,
  "updated_at":"2018-05-16T15:22:00Z",
  "url":"https://zendesk.com/api/v2/tickets/399.json"
}

```

#### Show Organization Memberships

This action is used to show all organization memberships.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|ID of user to show E.g. 20444826487|None|

Example input:

```
{
  "user_id": "361738647591"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|memberships|[]object|True|Members data|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### comment

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Author ID|string|False|Author ID|
|Body|string|False|Comment body|
|HTML Body|string|False|The comment formatted as HTML. This will be preferred over body|
|Public|boolean|False|Public (true if public comment, false if an internal note)|

#### ticket

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assignee ID|string|False|None|
|Attachment|file|False|None|
|Collaborator IDs|[]string|False|None|
|Comment|comment|False|None|
|Description|string|False|None|
|Due At|date|False|None|
|External ID|string|False|None|
|Group ID|integer|False|None|
|Priority|string|False|None|
|Problem ID|string|False|None|
|Recipient ID|string|False|None|
|Requester ID|string|False|None|
|Status|string|False|None|
|Subject|string|False|None|
|Tags|[]string|False|None|
|Type|string|False|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Remove unwanted input fields, add comment field in action Update Ticket | Fix enum fields issue with Create Ticket action
* 1.1.1 - New spec and help.md format for the Hub
* 1.1.0 - Updated Search action to return multiple results
* 1.0.1 - Updated to use PyPy3 SDK
* 1.0.0 - Add Update Ticket action and fix for documentation | Support web server mode
* 0.2.0 - Update connection to allow API key usage
* 0.1.2 - Update to v2 Python plugin architecture. Filename bug fix in Create Ticket action.
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Zendesk](https://www.zendesk.com)
* [Zendesk Python SDK](https://github.com/facetoe/zenpy)
* [Zendesk Developer Portal](https://developer.zendesk.com)

