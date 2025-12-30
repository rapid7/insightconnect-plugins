# Description

The [Zendesk](https://www.zendesk.com) plugin helps manage communication with customers. This plugin allows you to manage tickets and users in Zendesk. Customer Resource Management tool to manage tickets of user complaints and support issues. This plugin utilizes the [Zendesk Python SDK](https://github.com/facetoe/zenpy)

# Key Features

* Create, manage, and delete issues and epics
* Retrieve data about events, issues, epics, and boards

# Requirements

* A Zendesk API key
* Information about your Zendesk instance

# Supported Product Versions

* 2024-07-11

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_token|string|None|True|Zendesk API Token|None|A6yLhgioJiF2wOP1omP9sTa5yWSTvucx2U7yg67u|None|None|
|email|string|None|True|Email|None|user@example.com|None|None|
|subdomain|string|None|True|Zendesk subdomain|None|example-subdomain|None|None|

Example input:

```
{
  "api_token": "A6yLhgioJiF2wOP1omP9sTa5yWSTvucx2U7yg67u",
  "email": "user@example.com",
  "subdomain": "example-subdomain"
}
```

## Technical Details

### Actions


#### Create Ticket

This action is used to create ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assignee_id|integer|None|False|Assignee ID|None|361738647591|None|None|
|attachment|file|None|False|Optional file attachment|None|{"content": "Sample Content", "filename": "sample_file.txt"}|None|None|
|collaborator_ids|[]integer|None|False|List of collaborator IDs|None|[361738647591, 361738647672]|None|None|
|description|string|None|True|Ticket description|None|Example description|None|None|
|due_at|date|None|False|Time ticket is due|None|2021-04-10 12:00:00|None|None|
|external_id|string|None|False|Support ticket ID|None|10|None|None|
|group_id|integer|None|False|Group ID|None|1400012453812|None|None|
|priority|string|None|False|Ticket priority|["", "Urgent", "High", "Normal", "Low"]|High|None|None|
|problem_id|integer|None|False|For tickets of type 'incident', the numeric ID of the problem the incident is linked to|None|25|None|None|
|recipient|string|None|False|The original recipient e-mail address of the ticket|None|352083642834|None|None|
|requester_id|integer|None|False|ID of user requesting support|None|361738647672|None|None|
|status|string|None|False|Ticket status|["", "New", "Open", "Pending", "Hold", "Solved", "Closed"]|Open|None|None|
|subject|string|None|True|Subject of ticket|None|New Subject|None|None|
|tags|[]string|None|False|Tags describing ticket|None|["tag", "example", "ticket"]|None|None|
|type|string|None|False|Ticket type|["", "Problem", "Incident", "Task", "Question"]|Problem|None|None|
  
Example input:

```
{
  "assignee_id": 361738647591,
  "attachment": {
    "content": "Sample Content",
    "filename": "sample_file.txt"
  },
  "collaborator_ids": [
    361738647591,
    361738647672
  ],
  "description": "Example description",
  "due_at": "2021-04-10 12:00:00",
  "external_id": 10,
  "group_id": 1400012453812,
  "priority": "High",
  "problem_id": 25,
  "recipient": 352083642834,
  "requester_id": 361738647672,
  "status": "Open",
  "subject": "New Subject",
  "tags": [
    "tag",
    "example",
    "ticket"
  ],
  "type": "Problem"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|False|Ticket meta data|{"assignee_id":361738647591,"brand_id":1500182396435,"collaborator_ids":[361738647591,361738647672],"created_at":"2021-03-28T20:05:16Z","description":"Example description","due_at":"2021-04-10T12:00:00Z","external_id":"10","forum_topic_id":null,"group_id":1400012453812,"has_incidents":false,"id":15,"organization_id":1500075172832,"priority":"high","problem_id":25,"raw_subject":"New Subject","recipient":352083642834,"requester_id":361738647672,"sharing_agreement_ids":[],"status":"open","subject":"New Subject","submitter_id":1503798876742,"tags":["example","tag","ticket"],"type":"problem","updated_at":"2021-03-28T20:05:16Z","url":"https:/zendesk.com/api/v2/tickets/15.json"}|
  
Example output:

```
{
  "ticket": {
    "assignee_id": 361738647591,
    "brand_id": 1500182396435,
    "collaborator_ids": [
      361738647591,
      361738647672
    ],
    "created_at": "2021-03-28T20:05:16Z",
    "description": "Example description",
    "due_at": "2021-04-10T12:00:00Z",
    "external_id": "10",
    "forum_topic_id": null,
    "group_id": 1400012453812,
    "has_incidents": false,
    "id": 15,
    "organization_id": 1500075172832,
    "priority": "high",
    "problem_id": 25,
    "raw_subject": "New Subject",
    "recipient": 352083642834,
    "requester_id": 361738647672,
    "sharing_agreement_ids": [],
    "status": "open",
    "subject": "New Subject",
    "submitter_id": 1503798876742,
    "tags": [
      "example",
      "tag",
      "ticket"
    ],
    "type": "problem",
    "updated_at": "2021-03-28T20:05:16Z",
    "url": "https:/zendesk.com/api/v2/tickets/15.json"
  }
}
```

#### Delete Membership

This action is used to delete organization membership

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|membership_id|integer|None|True|ID of membership to delete E.g. 1401295821555|None|1401295821555|None|None|
  
Example input:

```
{
  "membership_id": 1401295821555
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|True|Success or failure|True|
  
Example output:

```
{
  "status": true
}
```

#### Delete Ticket

This action is used to delete ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ticket_id|integer|None|True|Delete ticket|None|10|None|None|
  
Example input:

```
{
  "ticket_id": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|True|Success or failure|True|
  
Example output:

```
{
  "status": true
}
```

#### Delete User

This action is used to delete user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|integer|None|True|ID of user to delete E.g. 361738647591|None|361738647591|None|None|
  
Example input:

```
{
  "user_id": 361738647591
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|True|Success or failure|True|
  
Example output:

```
{
  "status": true
}
```

#### Search

This action is used to search Zendesk

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|item|string|None|True|Search item E.g. password reset|None|Example User|None|None|
|type|string|None|True|Search type|["User", "Organization", "Ticket"]|User|None|None|
  
Example input:

```
{
  "item": "Example User",
  "type": "User"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|organizations|[]organization|False|Get Zendesk query results for organizations|None|
|tickets|[]ticket|False|Get Zendesk query results for tickets|None|
|users|[]user|False|Get Zendesk query results for users|[{"active":true,"alias":null,"chat_only":false,"created_at":"2018-01-26T14:24:58Z","custom_role_id":null,"details":null,"email":"user@example.com","external_id":null,"id":360385011372,"last_login_at":"2018-05-25T12:27:14Z","locale":"en-US","locale_id":1,"moderator":true,"name":"Example User","notes":null,"only_private_comments":false,"organization_id":360002530352,"phone":null,"photo":{"url":"https://organization.zendesk.com/api/v2/attachments/360004125291.json","id":360004125291,"file_name":"profile_image_360385011372_2206139.png","content_url":"https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139.png","mapped_content_url":"https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139.png","content_type":"image/png","size":1141,"width":80,"height":80,"inline":false,"thumbnails":[{"url":"https://organization.zendesk.com/api/v2/attachments/360004125311.json","id":360004125311,"file_name":"profile_image_360385011372_2206139_thumb.png","content_url":"https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139_thumb.png","mapped_content_url":"https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139_thumb.png","content_type":"image/png","size":601,"width":32,"height":32,"inline":false}]},"restricted_agent":false,"role":"admin","shared":false,"shared_agent":false,"signature":null,"suspended":false,"tags":[],"ticket_restriction":null,"time_zone":"Bogota","two_factor_auth_enabled":null,"updated_at":"2018-05-25T12:27:20Z","url":"https://organization.zendesk.com/api/v2/users/360385011372.json","verified":true}]|
  
Example output:

```
{
  "users": [
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
      "name": "Example User",
      "notes": null,
      "only_private_comments": false,
      "organization_id": 360002530352,
      "phone": null,
      "photo": {
        "content_type": "image/png",
        "content_url": "https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139.png",
        "file_name": "profile_image_360385011372_2206139.png",
        "height": 80,
        "id": 360004125291,
        "inline": false,
        "mapped_content_url": "https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139.png",
        "size": 1141,
        "thumbnails": [
          {
            "content_type": "image/png",
            "content_url": "https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139_thumb.png",
            "file_name": "profile_image_360385011372_2206139_thumb.png",
            "height": 32,
            "id": 360004125311,
            "inline": false,
            "mapped_content_url": "https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139_thumb.png",
            "size": 601,
            "url": "https://organization.zendesk.com/api/v2/attachments/360004125311.json",
            "width": 32
          }
        ],
        "url": "https://organization.zendesk.com/api/v2/attachments/360004125291.json",
        "width": 80
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
      "url": "https://organization.zendesk.com/api/v2/users/360385011372.json",
      "verified": true
    }
  ]
}
```

#### Show Organization Memberships

This action is used to show all organization memberships

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|integer|None|True|ID of user to show E.g. 361738647591|None|361738647591|None|None|
  
Example input:

```
{
  "user_id": 361738647591
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|memberships|[]organization_memberships|True|Members data|[{"created_at":"2021-03-16T19:29:22Z","default":true,"id":1401295821555,"organization_id":1500183722875,"updated_at":"2021-03-16T19:29:22Z","user_id":1504758840389}]|
  
Example output:

```
{
  "memberships": [
    {
      "created_at": "2021-03-16T19:29:22Z",
      "default": true,
      "id": 1401295821555,
      "organization_id": 1500183722875,
      "updated_at": "2021-03-16T19:29:22Z",
      "user_id": 1504758840389
    }
  ]
}
```

#### Show User

This action is used to retrieve user information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|integer|None|True|ID of user to show E.g. 361738647591|None|361738647591|None|None|
  
Example input:

```
{
  "user_id": 361738647591
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|object|True|User meta data|{"active":true,"alias":null,"chat_only":false,"created_at":"2021-03-16T19:29:15Z","custom_role_id":null,"details":null,"email":"user@example.com","external_id":null,"id":361738647591,"last_login_at":"2021-03-28T20:59:47Z","locale":"en-US","locale_id":1,"moderator":true,"name":"Example User","notes":null,"only_private_comments":false,"organization_id":1500182396435,"phone":null,"photo":null,"restricted_agent":false,"role":"admin","shared":false,"shared_agent":false,"signature":null,"suspended":false,"tags":[],"ticket_restriction":null,"time_zone":"America/Chicago","two_factor_auth_enabled":null,"updated_at":"2021-03-28T20:59:47Z","url":"https://zendesk.com/api/v2/users/361738647591.json","verified":true}|
  
Example output:

```
{
  "user": {
    "active": true,
    "alias": null,
    "chat_only": false,
    "created_at": "2021-03-16T19:29:15Z",
    "custom_role_id": null,
    "details": null,
    "email": "user@example.com",
    "external_id": null,
    "id": 361738647591,
    "last_login_at": "2021-03-28T20:59:47Z",
    "locale": "en-US",
    "locale_id": 1,
    "moderator": true,
    "name": "Example User",
    "notes": null,
    "only_private_comments": false,
    "organization_id": 1500182396435,
    "phone": null,
    "photo": null,
    "restricted_agent": false,
    "role": "admin",
    "shared": false,
    "shared_agent": false,
    "signature": null,
    "suspended": false,
    "tags": [],
    "ticket_restriction": null,
    "time_zone": "America/Chicago",
    "two_factor_auth_enabled": null,
    "updated_at": "2021-03-28T20:59:47Z",
    "url": "https://zendesk.com/api/v2/users/361738647591.json",
    "verified": true
  }
}
```

#### Suspend User

This action is used to suspend user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|integer|None|True|ID of user to delete E.g. 361738647591|None|361738647591|None|None|
  
Example input:

```
{
  "user_id": 361738647591
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|True|Success or failure|True|
  
Example output:

```
{
  "status": true
}
```

#### Update Ticket

This action is used to update ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assignee_id|integer|None|False|Assignee ID|None|361738647591|None|None|
|collaborator_ids|[]integer|None|False|List of collaborator IDs|None|[361738647591, 361738647672]|None|None|
|comment|comment|None|False|Comment|None|{"author_id": 361738647591,"body": "Test comment","html_body": "<u>Test Underlined comment</u>","public": true}|None|None|
|due_at|date|None|False|Time ticket is due|None|2021-04-10 12:00:00|None|None|
|external_id|string|None|False|Support ticket ID|None|10|None|None|
|group_id|integer|None|False|Group ID|None|1400012453812|None|None|
|priority|string|None|False|Ticket priority|["", "Urgent", "High", "Normal", "Low"]|High|None|None|
|problem_id|integer|None|False|For tickets of type 'incident', the numeric ID of the problem the incident is linked to|None|25|None|None|
|recipient|string|None|False|ID of user recipient|None|352083642834|None|None|
|requester_id|integer|None|False|ID of user requesting support|None|361738647672|None|None|
|status|string|None|False|Ticket status|["", "New", "Open", "Pending", "Hold", "Solved", "Closed"]|Open|None|None|
|subject|string|None|False|Subject of ticket|None|New Subject|None|None|
|tags|[]string|None|False|Tags describing ticket|None|["tag", "example", "ticket"]|None|None|
|ticket_id|integer|None|True|Ticket ID|None|30|None|None|
|type|string|None|False|Ticket type|["", "Problem", "Incident", "Task", "Question"]|Problem|None|None|
  
Example input:

```
{
  "assignee_id": 361738647591,
  "collaborator_ids": [
    361738647591,
    361738647672
  ],
  "comment": {
    "author_id": 361738647591,
    "body": "Test comment",
    "html_body": "<u>Test Underlined comment</u>",
    "public": true
  },
  "due_at": "2021-04-10 12:00:00",
  "external_id": 10,
  "group_id": 1400012453812,
  "priority": "High",
  "problem_id": 25,
  "recipient": 352083642834,
  "requester_id": 361738647672,
  "status": "Open",
  "subject": "New Subject",
  "tags": [
    "tag",
    "example",
    "ticket"
  ],
  "ticket_id": 30,
  "type": "Problem"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|True|Ticket meta data|{"assignee_id":"361738647591","brand_id":1500182396435,"collaborator_ids":["361738647591","361738647672"],"created_at":"2021-03-28T18:51:48Z","due_at":"2021-04-10T12:00:00Z","external_id":"10","group_id":"1400012453812","has_incidents":false,"id":12,"organization_id":1500075172832,"priority":"High","problem_id":"25","raw_subject":"Example Ticket","recipient":"1503798876742","requester_id":"1503798876742","sharing_agreement_ids":[],"status":"Open","subject":"New Subject","submitter_id":361738647591,"tags":["tag","example","ticket"],"type":"Problem","updated_at":"2021-03-28T20:46:09Z","url":"https://zendesk.com/api/v2/tickets/12.json","comment":{"author_id":"361738647591","body":"Test comment","html_body":"<u>Test Underlined comment</u>","public":true}}|
  
Example output:

```
{
  "ticket": {
    "assignee_id": "361738647591",
    "brand_id": 1500182396435,
    "collaborator_ids": [
      "361738647591",
      "361738647672"
    ],
    "comment": {
      "author_id": "361738647591",
      "body": "Test comment",
      "html_body": "<u>Test Underlined comment</u>",
      "public": true
    },
    "created_at": "2021-03-28T18:51:48Z",
    "due_at": "2021-04-10T12:00:00Z",
    "external_id": "10",
    "group_id": "1400012453812",
    "has_incidents": false,
    "id": 12,
    "organization_id": 1500075172832,
    "priority": "High",
    "problem_id": "25",
    "raw_subject": "Example Ticket",
    "recipient": "1503798876742",
    "requester_id": "1503798876742",
    "sharing_agreement_ids": [],
    "status": "Open",
    "subject": "New Subject",
    "submitter_id": 361738647591,
    "tags": [
      "tag",
      "example",
      "ticket"
    ],
    "type": "Problem",
    "updated_at": "2021-03-28T20:46:09Z",
    "url": "https://zendesk.com/api/v2/tickets/12.json"
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**comment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Author ID|string|None|None|Author ID|None|
|Body|string|None|None|Comment body|None|
|HTML Body|string|None|None|The comment formatted as HTML. This will be preferred over body|None|
|Public|boolean|None|None|Public (true if public comment, false if an internal note)|None|
  
**organization**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|date|None|False|Created at|None|
|Details|string|None|False|Details|None|
|External ID|string|None|False|External ID|None|
|Group ID|integer|None|False|Group ID|None|
|ID|integer|None|False|ID|None|
|Name|string|None|False|Name|None|
|Notes|string|None|False|Notes|None|
|Shared Comments|boolean|None|False|Shared comments|None|
|Shared Tickets|boolean|None|False|Shared tickets|None|
|Tags|[]string|None|False|Tags|None|
|Updated At|string|None|False|Updated at|None|
|URL|string|None|False|URL|None|
  
**ticket**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assignee ID|integer|None|False|Assignee ID|None|
|Attachment|file|None|False|Attachment|None|
|Collaborator IDs|[]integer|None|False|Collaborator IDs|None|
|Comment|comment|None|False|Comment|None|
|Description|string|None|False|Description|None|
|Due At|date|None|False|Due at|None|
|External ID|string|None|False|External ID|None|
|Group ID|integer|None|False|Group ID|None|
|ID|integer|None|False|ID|None|
|Priority|string|None|False|Priority|None|
|Problem ID|integer|None|False|Problem ID|None|
|Recipient ID|string|None|False|Recipient ID|None|
|Requester ID|integer|None|False|Requester ID|None|
|Status|string|None|False|Status|None|
|Subject|string|None|False|Subject|None|
|Tags|[]string|None|False|Tags|None|
|Type|string|None|False|Type|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active|boolean|None|False|Active|None|
|Alias|string|None|False|Alias|None|
|Chat Only|boolean|None|False|Chat only|None|
|Created At|date|None|False|Created at|None|
|Custom Role ID|integer|None|False|Custom role ID|None|
|Details|string|None|False|Details|None|
|Email|string|None|False|Email|None|
|External ID|string|None|False|External ID|None|
|ID|integer|None|False|ID|None|
|Last Login At|date|None|False|Last login at|None|
|Locale|string|None|False|Locale|None|
|Locale ID|integer|None|False|Locale ID|None|
|Moderator|boolean|None|False|Moderator|None|
|Name|string|None|False|Name|None|
|Notes|string|None|False|Notes|None|
|Only Private Comments|boolean|None|False|Only private comments|None|
|Organization ID|integer|None|False|Organization ID|None|
|Phone|string|None|False|Phone|None|
|Photo|object|None|False|Photo|None|
|Restricted Agent|boolean|None|False|Restricted agent|None|
|Role|string|None|False|Role|None|
|Shared|boolean|None|False|Shared|None|
|Shared Agent|boolean|None|False|Shared agent|None|
|Signature|string|None|False|Signature|None|
|Suspended|boolean|None|False|Suspended|None|
|Tags|[]string|None|False|Tags|None|
|Ticket Restriction|string|None|False|Ticket restriction|None|
|Time Zone|string|None|False|Time Zone|None|
|Two Factor Auth Enabled|boolean|None|False|Two factor auth enabled|None|
|Updated At|string|None|False|Updated at|None|
|URL|string|None|False|URL|None|
|Verified|boolean|None|False|Verified|None|
  
**organization_memberships**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|date|None|False|Created at|None|
|Default|boolean|None|False|Indicates weather it's default organization membership or not for a user|None|
|ID|integer|None|False|ID|None|
|Organization ID|integer|None|False|Organization ID|None|
|Updated At|date|None|False|Updated at|None|
|User ID|integer|None|False|ID of user|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 5.0.0 - Adjusted authentication methods | Updated SDK to the latest version (6.4.1)
* 4.0.3 - Update dependency version | Updated SDK to the latest version
* 4.0.2 - Updated SDK to the latest version | `Search`: Fixed issue where only one search result was returned
* 4.0.1 - Updated the exceptions for all the actions | Show Organization Memberships: Added types to the actions output
* 4.0.0 - Change ID parameter types into integer | Update dependency version
* 3.0.0 - Add custom output types in Search action | Add conversion of IDs to string in Search action to allow reuse search data in other actions | Add action input and output examples to the documentation
* 2.0.1 - Change custom output type `group_id` from integer to string | Change `group_id` input type from integer to string in Create Ticket action
* 2.0.0 - Remove unwanted input fields, add comment field in action Update Ticket | Fix enum fields issue with Create Ticket action
* 1.1.1 - New spec and help.md format for the Extension Library
* 1.1.0 - Updated Search action to return multiple results
* 1.0.1 - Updated to use PyPy3 SDK
* 1.0.0 - Add Update Ticket action and fix for documentation | Support web server mode
* 0.2.0 - Update connection to allow API key usage
* 0.1.2 - Update to v2 Python plugin architecture. Filename bug fix in Create Ticket action.
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Zendesk](https://www.zendesk.com)

## References

* [Zendesk](https://www.zendesk.com)
* [Zendesk Python SDK](https://github.com/facetoe/zenpy)
* [Zendesk Developer Portal](https://developer.zendesk.com)