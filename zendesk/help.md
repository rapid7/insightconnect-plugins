# Description

[Zendesk](https://www.zendesk.com) helps improve communication and make sense of massive amounts of data.
This plugin utilizes the [Zendesk Python SDK](https://github.com/facetoe/zenpy).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|password|password|None|False|Zendesk password|None|
|api_key|credential_secret_key|None|False|Zendesk API key|None|
|subdomain|string|None|True|Zendesk subdomain E.g. mycompany|None|
|email|string|None|True|Email address|None|

## Technical Details

### Actions

#### Search

This action is used to search Zendesk.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|item|string|None|True|Search item E.g. password reset|None|
|type|string|None|True|Search type|['User', 'Organization', 'Ticket']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]object|False|None|

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
      "email": "jen@komand.com",
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

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Delete Membership

This action is used to delete an organization membership.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|membership_id|string|None|True|ID of membership to delete E.g. 1657574807|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Show User

This action is used to retrieve user information.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|ID of user to show E.g. 20444826487|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|object|False|None|

#### Suspend User

This action is used to suspend a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|ID of user to delete E.g. 20444826487|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Delete User

This action is used to delete a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|ID of user to delete E.g. 20444826487|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Create Ticket

This action is used to create a ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|False|Ticket status|['New', 'Open', 'Pending', 'Hold', 'Solved', 'Closed']|
|assignee_id|string|None|False|Assignee ID|None|
|description|string|None|True|Ticket description|None|
|tags|[]string|None|False|Tags describing ticket|None|
|due_at|date|None|False|Time ticket is due|None|
|type|string|None|False|Ticket type|['Problem', 'Incident', 'Task', 'Question']|
|subject|string|None|True|Subject of ticket|None|
|collaborator_ids|[]string|None|False|List of collaborator IDs|None|
|priority|string|None|False|Ticket priority|['Urgent', 'High', 'Normal', 'Low']|
|attachment|file|None|False|Optional file attachment|None|
|requester_id|string|None|False|ID of user requesting support|None|
|group_id|string|None|False|Group ID|None|
|recipient|string|None|False|ID of user recipient|None|
|problem_id|string|None|False|For tickets of type 'incident', the numeric ID of the problem the incident is linked to|None|
|external_id|string|None|False|Support ticket ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket|object|False|None|

#### Update Ticket

This action is used to update ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|False|Ticket status|['New', 'Open', 'Pending', 'Hold', 'Solved', 'Closed', '']|
|description|string|None|False|Ticket description|None|
|tags|[]string|None|False|Tags describing ticket|None|
|assignee_id|string|None|False|Assignee ID|None|
|requester_id|string|None|True|ID of user requesting support|None|
|recipient|string|None|False|ID of user recipient|None|
|problem_id|string|None|False|For tickets of type 'incident', the numeric ID of the problem the incident is linked to|None|
|subject|string|None|False|Subject of ticket|None|
|due_at|date|None|False|Time ticket is due|None|
|external_id|string|None|False|Support ticket ID|None|
|collaborator_ids|[]string|None|False|List of collaborator IDs|None|
|priority|string|None|False|Ticket priority|['Urgent', 'High', 'Normal', 'Low', '']|
|ticket_id|string|None|True|Ticket ID|None|
|group_id|string|None|False|Group ID|None|
|type|string|None|False|Ticket type|['Problem', 'Incident', 'Task', 'Question', '']|
|attachment|file|None|False|Optional file attachment|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket|object|True|Ticket meta data|

Example output:

```

{
  "assignee_id":"",
  "brand_id":360000066092,
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

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|memberships|[]object|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Use new credential types
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

