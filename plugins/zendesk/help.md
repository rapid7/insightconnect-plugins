# Description

The [Zendesk](https://www.zendesk.com) plugin helps manage communication with customers. This plugin allows you to manage tickets and users in Zendesk. Customer Resource Management tool to manage tickets of user complaints and support issues.

This plugin utilizes the [Zendesk Python SDK](https://github.com/facetoe/zenpy).

# Key Features

* Create, manage, and delete issues and epics
* Retrieve data about events, issues, epics, and boards

# Requirements

* A Zendesk API key
* Information about your Zendesk instance

# Supported Product Versions

* 2022-01-28

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|False|Zendesk API key|None|A6yLhgioJiF2wOP1omP9sTa5yWSTvucx2U7yg67u|
|credentials|credential_username_password|None|True|Email and password|None|{"username": "user@example.com", "password": "password"}|
|subdomain|string|None|True|Zendesk subdomain|None|example-subdomain|

Example input:

```
{
  "api_key": "A6yLhgioJiF2wOP1omP9sTa5yWSTvucx2U7yg67u",
  "credentials": {
    "username": "user@example.com",
    "password": "password"
  },
  "subdomain": "example-subdomain"
}
```

## Technical Details

### Actions

#### Search

This action is used to search Zendesk.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|item|string|None|True|Search item E.g. password reset|None|Example User|
|type|string|None|True|Search type|['User', 'Organization', 'Ticket']|User|

Example input:

```
{
  "item": "Example User",
  "type": "User"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|organizations|[]organization|False|Get Zendesk query results for organizations|
|tickets|[]ticket|False|Get Zendesk query results for tickets|
|users|[]user|False|Get Zendesk query results for users|

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
        "url": "https://organization.zendesk.com/api/v2/attachments/360004125291.json",
        "id": 360004125291,
        "file_name": "profile_image_360385011372_2206139.png",
        "content_url": "https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139.png",
        "mapped_content_url": "https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139.png",
        "content_type": "image/png",
        "size": 1141,
        "width": 80,
        "height": 80,
        "inline": false,
        "thumbnails": [
          {
            "url": "https://organization.zendesk.com/api/v2/attachments/360004125311.json",
            "id": 360004125311,
            "file_name": "profile_image_360385011372_2206139_thumb.png",
            "content_url": "https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139_thumb.png",
            "mapped_content_url": "https://organization.zendesk.com/system/photos/3600/0412/5291/profile_image_360385011372_2206139_thumb.png",
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
      "url": "https://organization.zendesk.com/api/v2/users/360385011372.json",
      "verified": true
    }
  ]
}
```

#### Delete Ticket

This action is used to delete a ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ticket_id|integer|None|True|Delete ticket|None|10|

Example input:

```
{
  "ticket_id": 10
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Success or failure|

Example output:

```
{
  "status": true
}
```

#### Delete Membership

This action is used to delete an organization membership.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|membership_id|integer|None|True|ID of membership to delete E.g. 1401295821555|None|1401295821555|

Example input:

```
{
  "membership_id": 1401295821555
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Success or failure|

Example output:

```
{
  "status": true
}
```

#### Show User

This action is used to retrieve user information.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|integer|None|True|ID of user to show E.g. 361738647591|None|361738647591|

Example input:

```
{
  "user_id": 361738647591
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|object|True|User meta data|

Example output:

```
{
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
```

#### Suspend User

This action is used to suspend a user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|integer|None|True|ID of user to delete E.g. 361738647591|None|361738647591|

Example input:

```
{
  "user_id": 361738647591
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Success or failure|

Example output:

```
{
  "status": true
}
```

#### Delete User

This action is used to delete a user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|integer|None|True|ID of user to delete E.g. 361738647591|None|361738647591|

Example input:

```
{
  "user_id": 361738647591
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Success or failure|

Example output:

```
{
  "status": true
}
```

#### Create Ticket

This action is used to create a ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignee_id|integer|None|False|Assignee ID|None|361738647591|
|attachment|file|None|False|Optional file attachment|None|{"content": "Sample Content", "filename": "sample_file.txt"}|
|collaborator_ids|[]integer|None|False|List of collaborator IDs|None|[361738647591, 361738647672]|
|description|string|None|True|Ticket description|None|Example description|
|due_at|date|None|False|Time ticket is due|None|2021-04-10 12:00:00|
|external_id|string|None|False|Support ticket ID|None|10|
|group_id|integer|None|False|Group ID|None|1400012453812|
|priority|string|None|False|Ticket priority|['Urgent', 'High', 'Normal', 'Low', '']|High|
|problem_id|integer|None|False|For tickets of type 'incident', the numeric ID of the problem the incident is linked to|None|25|
|recipient|string|None|False|The original recipient e-mail address of the ticket|None|352083642834|
|requester_id|integer|None|False|ID of user requesting support|None|361738647672|
|status|string|None|False|Ticket status|['New', 'Open', 'Pending', 'Hold', 'Solved', 'Closed', '']|Open|
|subject|string|None|True|Subject of ticket|None|New Subject|
|tags|[]string|None|False|Tags describing ticket|None|["tag", "example", "ticket"]|
|type|string|None|False|Ticket type|['Problem', 'Incident', 'Task', 'Question', '']|Problem|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket|ticket|False|Ticket meta data|

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

#### Update Ticket

This action is used to update ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignee_id|integer|None|False|Assignee ID|None|361738647591|
|collaborator_ids|[]integer|None|False|List of collaborator IDs|None|[361738647591, 361738647672]|
|comment|comment|None|False|Comment|None|{"author_id": 361738647591,"body": "Test comment","html_body": "<u>Test Underlined comment</u>","public": true}|
|due_at|date|None|False|Time ticket is due|None|2021-04-10 12:00:00|
|external_id|string|None|False|Support ticket ID|None|10|
|group_id|integer|None|False|Group ID|None|1400012453812|
|priority|string|None|False|Ticket priority|['Urgent', 'High', 'Normal', 'Low', '']|High|
|problem_id|integer|None|False|For tickets of type 'incident', the numeric ID of the problem the incident is linked to|None|25|
|recipient|string|None|False|ID of user recipient|None|352083642834|
|requester_id|integer|None|False|ID of user requesting support|None|361738647672|
|status|string|None|False|Ticket status|['New', 'Open', 'Pending', 'Hold', 'Solved', 'Closed', '']|Open|
|subject|string|None|False|Subject of ticket|None|New Subject|
|tags|[]string|None|False|Tags describing ticket|None|["tag", "example", "ticket"]|
|ticket_id|integer|None|True|Ticket ID|None|30|
|type|string|None|False|Ticket type|['Problem', 'Incident', 'Task', 'Question', '']|Problem|

Example input:

```
{
  "assignee_id": 361738647591,
  "collaborator_ids": [
    361738647591,
    361738647672
  ],
  "comment": {
    "author_id": "361738647591",
    "body": "Test comment",
    "html_body": "<u>Test Underlined comment</u>",
    "public": true
  },
  "due_at": "2021-04-10T12:00:00Z",
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket|ticket|True|Ticket meta data|

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
    "url": "https://zendesk.com/api/v2/tickets/12.json",
    "comment": {
      "author_id": "361738647591",
      "body": "Test comment",
      "html_body": "<u>Test Underlined comment</u>",
      "public": true
    }
  }
}
```

#### Show Organization Memberships

This action is used to show all organization memberships.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|integer|None|True|ID of user to show E.g. 361738647591|None|361738647591|

Example input:

```
{
  "user_id": 361738647591
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|memberships|[]organization_memberships|True|Members data|

Example input:

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

#### organization

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created At|date|False|Created at|
|Details|string|False|Details|
|External ID|string|False|External ID|
|Group ID|integer|False|Group ID|
|ID|integer|False|ID|
|Name|string|False|Name|
|Notes|string|False|Notes|
|Shared Comments|boolean|False|Shared comments|
|Shared Tickets|boolean|False|Shared tickets|
|Tags|[]string|False|Tags|
|Updated At|string|False|Updated at|
|URL|string|False|URL|

#### organization_memberships

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created At|date|False|Created at|
|Default|boolean|False|Indicates weather it's default organization membership or not for a user|
|ID|integer|False|ID|
|Organization ID|integer|False|Organization ID|
|Updated At|date|False|Updated at|
|User ID|integer|False|ID of user|

#### ticket

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assignee ID|integer|False|Assignee ID|
|Attachment|file|False|Attachment|
|Collaborator IDs|[]integer|False|Collaborator IDs|
|Comment|comment|False|Comment|
|Description|string|False|Description|
|Due At|date|False|Due at|
|External ID|string|False|External ID|
|Group ID|integer|False|Group ID|
|ID|integer|False|ID|
|Priority|string|False|Priority|
|Problem ID|integer|False|Problem ID|
|Recipient ID|string|False|Recipient ID|
|Requester ID|integer|False|Requester ID|
|Status|string|False|Status|
|Subject|string|False|Subject|
|Tags|[]string|False|Tags|
|Type|string|False|Type|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Active|boolean|False|Active|
|Alias|string|False|Alias|
|Chat Only|boolean|False|Chat only|
|Created At|date|False|Created at|
|Custom Role ID|integer|False|Custom role ID|
|Details|string|False|Details|
|Email|string|False|Email|
|External ID|string|False|External ID|
|ID|integer|False|ID|
|Last Login At|date|False|Last login at|
|Locale|string|False|Locale|
|Locale ID|integer|False|Locale ID|
|Moderator|boolean|False|Moderator|
|Name|string|False|Name|
|Notes|string|False|Notes|
|Only Private Comments|boolean|False|Only private comments|
|Organization ID|integer|False|Organization ID|
|Phone|string|False|Phone|
|Photo|object|False|Photo|
|Restricted Agent|boolean|False|Restricted agent|
|Role|string|False|Role|
|Shared|boolean|False|Shared|
|Shared Agent|boolean|False|Shared agent|
|Signature|string|False|Signature|
|Suspended|boolean|False|Suspended|
|Tags|[]string|False|Tags|
|Ticket Restriction|string|False|Ticket restriction|
|Time Zone|string|False|Time Zone|
|Two Factor Auth Enabled|boolean|False|Two factor auth enabled|
|Updated At|string|False|Updated at|
|URL|string|False|URL|
|Verified|boolean|False|Verified|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

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

## References

* [Zendesk](https://www.zendesk.com)
* [Zendesk Python SDK](https://github.com/facetoe/zenpy)
* [Zendesk Developer Portal](https://developer.zendesk.com)

