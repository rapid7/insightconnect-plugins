# Description

HappyFox is a practical help desk and customer support software solution. Using the HappyFox plugin for Rapid7 InsightConnect, users can create, delete and list tickets

# Key Features

* Create a ticket
* Create a ticket with attachments
* Delete a ticket
* List tickets
* Create inline attachment

# Requirements

* HappyFox API key and auth code

# Supported Product Versions

* HappyFox API v1.1 2022-12-22

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|apiKey|credential_secret_key|None|True|HappyFox API key|None|3395856ce81f2b7382dee72602f798b6|
|authCode|credential_secret_key|None|True|HappyFox auth code|None|44d88612fea8a8f36de82e1278abb02f|
|subdomain|string|None|True|Subdomain from your HappyFox URL, for example "example-company" from "https://example-company.happyfox.com"|None|example-company|

Example input:

```
{
  "apiKey": "3395856ce81f2b7382dee72602f798b6",
  "authCode": "44d88612fea8a8f36de82e1278abb02f",
  "subdomain": "example-company"
}
```

## Technical Details

### Actions

#### Create Inline Attachment

This action is used to generate a temporary URL that can be set as the value of the 'src' property of the 'img' tag in the ticket message (html) when creating the ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|file|None|True|The image file to be uploaded. Only one file can be uploaded at a time, and the size limit should not exceed 25 MB|None|{"filename": "image.png", "content": "iVBORw0KGgoAAAANSUhEUgAAAfQAAAH0CAYAAADL1t+KAAAAGXRFWHRTb2Z0"}|

Example input:

```
{
  "file": {
    "filename": "image.png",
    "content": "iVBORw0KGgoAAAANSUhEUgAAAfQAAAH0CAYAAADL1t+KAAAAGXRFWHRTb2Z0"
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|Temporary URL created for the provided file|

Example output:

```
{
  "url": "https://example.com"
}
```

#### Create Ticket

This action is used to create a new ticket in your helpdesk.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignee|integer|None|False|ID of the agent to assign the ticket to|None|10|
|bcc|string|None|False|List of email addresses, separated by commas|None|user@example.com, user2@example.com|
|category|integer|None|True|ID of the category in which the ticket should be created|None|1|
|cc|string|None|False|List of email addresses, separated by commas|None|user@example.com, user2@example.com|
|customFields|object|None|False|Key value pairs containing the names and values of Ticket and Contact custom fields|None|{"t-cf-1": "test value", "c-cf-1": "test value"}|
|dueDate|date|None|False|Due date of the ticket|None|2022-11-30T12:00:00Z|
|email|string|None|True|Email address of the contact|None|user@example.com|
|html|string|None|False|Ticket message in HTML. Text or HTML field is required|None|Example description|
|name|string|None|True|Name of the contact|None|Example Contact|
|phone|string|None|False|Phone number of the contact|None|111111111|
|priority|integer|None|False|ID of the priority of the ticket|None|4|
|subject|string|None|True|Subject of the ticket|None|Example Ticket|
|tags|string|None|False|List of tags separated by commas|None|tag1, tag2|
|text|string|None|False|Ticket message in plain text format. Text or HTML field is required|None|Example description|
|visibleOnlyStaff|boolean|False|True|Whether the ticket is private or not|None|False|

Example input:

```
{
  "assignee": 10,
  "bcc": "user@example.com, user2@example.com",
  "category": 1,
  "cc": "user@example.com, user2@example.com",
  "customFields": {
    "t-cf-1": "test value",
    "c-cf-1": "test value"
  },
  "dueDate": "2022-11-30T12:00:00Z",
  "email": "user@example.com",
  "html": "Example description",
  "name": "Example Contact",
  "phone": "111111111",
  "priority": 4,
  "subject": "Example Ticket",
  "tags": "tag1, tag2",
  "text": "Example description",
  "visibleOnlyStaff": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket|ticket|False|Information about created ticket|

Example output:

```
{
  "ticket": {
    "displayId": "#RS00000001",
    "firstMessage": "Example description\n\n",
    "lastUserReplyAt": "2022-11-20 07:37:24",
    "id": 1,
    "customFields": [
      {
        "compulsoryOnComplete": false,
        "name": "Test Field",
        "value": "test value",
        "type": "text",
        "id": 1,
        "visibleToStaffOnly": false
      }
    ],
    "subject": "Example Ticket",
    "category": {
      "prepopulateCc": "AR",
      "description": "Tickets will be created here by default.",
      "timeSpentMandatory": false,
      "public": true,
      "id": 1,
      "name": "example category"
    },
    "attachmentsCount": 0,
    "lastUpdatedAt": "2022-11-20 07:37:24",
    "priority": {
      "default": false,
      "id": 4,
      "name": "Low",
      "order": 1
    },
    "messagesCount": 1,
    "slaBreaches": 0,
    "mergedTickets": [],
    "status": {
      "name": "New",
      "color": "FF9900",
      "order": 1,
      "default": true,
      "behavior": "pending",
      "id": 1
    },
    "dueDate": "2022-11-30",
    "tags": "tag1,tag2",
    "user": {
      "name": "Example Contact",
      "primaryPhone": {
        "type": "m",
        "number": "111111111",
        "id": 3
      },
      "phones": [
        {
          "type": "o",
          "number": "111111111",
          "id": 4
        },
        {
          "type": "m",
          "number": "111111111",
          "id": 3
        }
      ],
      "createdAt": "2022-11-14 11:10:21",
      "updatedAt": "2022-11-14 11:10:21",
      "pendingTicketsCount": 25,
      "contactGroups": [],
      "ticketsCount": 25,
      "id": 7,
      "email": "user@example.com",
      "customFields": [
        {
          "name": "Test Field",
          "value": "test value",
          "type": "text",
          "id": 1,
          "visibleToStaffOnly": false
        }
      ]
    },
    "subscribers": [],
    "unresponded": true,
    "createdAt": "2022-11-30 07:37:24",
    "source": "TKT_CREATION_API",
    "assignedTo": {
      "name": "Example User",
      "isAccountAdmin": true,
      "email": "user@example.com",
      "role": {
        "name": "Administrator",
        "id": 1
      },
      "active": true,
      "id": 10,
      "categories": [
        1
      ],
      "permissions": []
    },
    "updates": [
      {
        "priorityChange": {
          "newName": "Low",
          "new": 4
        },
        "timestamp": "2022-11-30 07:37:24",
        "dueDateChange": {
          "new": "2022-11-30"
        },
        "by": {
          "email": "user@example.com",
          "type": "user",
          "id": 7,
          "name": "Example Contact"
        },
        "updateId": 60,
        "message": {
          "attachments": [],
          "bccList": "user@example.com,user2@example.com",
          "text": "Example description\n\n",
          "ccList": "user@example.com,user2@example.com",
          "customerUpdated": false,
          "html": "<html><head><meta charset=\"utf-8\"></head><body>Example description</body></html>"
        },
        "assigneeChange": {
          "newName": "Example User",
          "new": 1
        },
        "statusChange": {
          "newName": "New",
          "new": 1
        }
      }
    ]
  }
}
```

#### Create Ticket with Attachments

This action is used to create a new ticket with attachments in your helpdesk.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignee|integer|None|False|ID of the agent to assign the ticket to|None|10|
|attachments|[]file|None|False|List of files to be uploaded. The total size of all the files combined should not exceed 25 MB|None|[{"filename": "text.txt", "content": "dGVzdA=="}]|
|bcc|string|None|False|List of email addresses, separated by commas|None|user@example.com, user2@example.com|
|category|integer|None|True|ID of the category in which the ticket should be created|None|1|
|cc|string|None|False|List of email addresses, separated by commas|None|user@example.com, user2@example.com|
|customFields|object|None|False|Key value pairs containing the names and values of Ticket and Contact custom fields|None|{"t-cf-1": "test value", "c-cf-1": "test value"}|
|dueDate|date|None|False|Due date of the ticket|None|2022-11-30T12:00:00Z|
|email|string|None|True|Email address of the contact|None|user@example.com|
|html|string|None|False|Ticket message in HTML. Text or HTML field is required|None|Example description|
|name|string|None|True|Name of the contact|None|Example Contact|
|phone|string|None|False|Phone number of the contact|None|111111111|
|priority|integer|None|False|ID of the priority of the ticket|None|4|
|subject|string|None|True|Subject of the ticket|None|Example Ticket|
|tags|string|None|False|List of tags separated by commas|None|tag1, tag2|
|text|string|None|False|Ticket message in plain text format. Text or HTML field is required|None|Example description|
|visibleOnlyStaff|boolean|False|True|Whether the ticket is private or not|None|False|

Example input:

```
{
  "assignee": 10,
  "attachments": [
    {
      "filename": "text.txt",
      "content": "dGVzdA=="
    }
  ],
  "bcc": "user@example.com, user2@example.com",
  "category": 1,
  "cc": "user@example.com, user2@example.com",
  "customFields": {
    "t-cf-1": "test value",
    "c-cf-1": "test value"
  },
  "dueDate": "2022-11-30T12:00:00Z",
  "email": "user@example.com",
  "html": "Example description",
  "name": "Example Contact",
  "phone": "111111111",
  "priority": 4,
  "subject": "Example Ticket",
  "tags": "tag1, tag2",
  "text": "Example description",
  "visibleOnlyStaff": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket|ticket|False|Information about created ticket|

Example output:

```
{
  "ticket": {
    "displayId": "#RS00000001",
    "firstMessage": "Example description\n\n",
    "lastUserReplyAt": "2022-11-20 07:37:24",
    "id": 1,
    "customFields": [
      {
        "compulsoryOnComplete": false,
        "name": "Test Field",
        "value": "test value",
        "type": "text",
        "id": 1,
        "visibleToStaffOnly": false
      }
    ],
    "subject": "Example Ticket",
    "category": {
      "prepopulateCc": "AR",
      "description": "Tickets will be created here by default.",
      "timeSpentMandatory": false,
      "public": true,
      "id": 1,
      "name": "example category"
    },
    "attachmentsCount": 1,
    "lastUpdatedAt": "2022-11-20 07:37:24",
    "priority": {
      "default": false,
      "id": 4,
      "name": "Low",
      "order": 1
    },
    "messagesCount": 1,
    "slaBreaches": 0,
    "mergedTickets": [],
    "status": {
      "name": "New",
      "color": "FF9900",
      "order": 1,
      "default": true,
      "behavior": "pending",
      "id": 1
    },
    "dueDate": "2022-11-30",
    "tags": "tag1,tag2",
    "user": {
      "name": "Example Contact",
      "primaryPhone": {
        "type": "m",
        "number": "111111111",
        "id": 3
      },
      "phones": [
        {
          "type": "o",
          "number": "111111111",
          "id": 4
        },
        {
          "type": "m",
          "number": "111111111",
          "id": 3
        }
      ],
      "createdAt": "2022-11-14 11:10:21",
      "updatedAt": "2022-11-14 11:10:21",
      "pendingTicketsCount": 25,
      "contactGroups": [],
      "ticketsCount": 25,
      "id": 7,
      "email": "user@example.com",
      "customFields": [
        {
          "name": "Test Field",
          "value": "test value",
          "type": "text",
          "id": 1,
          "visibleToStaffOnly": false
        }
      ]
    },
    "subscribers": [],
    "unresponded": true,
    "createdAt": "2022-11-20 07:37:24",
    "source": "TKT_CREATION_API",
    "assignedTo": {
      "name": "Example User",
      "isAccountAdmin": true,
      "email": "user@example.com",
      "role": {
        "name": "Administrator",
        "id": 1
      },
      "active": true,
      "id": 10,
      "categories": [
        1
      ],
      "permissions": []
    },
    "updates": [
      {
        "priorityChange": {
          "newName": "Low",
          "new": 4
        },
        "timestamp": "2022-11-20 07:37:24",
        "dueDateChange": {
          "new": "2022-11-30"
        },
        "by": {
          "email": "user@example.com",
          "type": "user",
          "id": 7,
          "name": "Example Contact"
        },
        "updateId": 60,
        "message": {
          "attachments": [
            {
              "url": "https://example.com",
              "id": 1,
              "filename": "text.txt"
            }
          ],
          "bccList": "user@example.com,user2@example.com",
          "text": "Example description\n\n",
          "ccList": "user@example.com,user2@example.com",
          "customerUpdated": false,
          "html": "<html><head><meta charset=\"utf-8\"></head><body>Example description</body></html>"
        },
        "assigneeChange": {
          "newName": "Example User",
          "new": 1
        },
        "statusChange": {
          "newName": "New",
          "new": 1
        }
      }
    ]
  }
}
```

#### Delete Ticket

This action is used to delete a provided ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|staffId|integer|None|True|ID of the agent that is performing the category change|None|1|
|ticketId|integer|None|True|ID of the ticket which will be deleted|None|20|

Example input:

```
{
  "staffId": 1,
  "ticketId": 20
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the action was successful|

Example output:

```
{
  "success": true
}
```

#### List Tickets

This action is used to get a list of all tickets for the given filters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|category|integer|None|False|Filter tickets by category ID|None|1|
|minifyResponse|boolean|False|True|Show only list of ticket IDs in the response|None|False|
|page|integer|None|False|The number of the results page to be returned|None|1|
|query|string|None|False|Search tickets using advanced filters|None|tags:"tag1","tag2"|
|size|integer|20|False|The number of results per page|None|20|
|sort|string|last updated descending|False|Sort tickets using advanced filters|['assignee username ascending', 'assignee username descending', 'category ascending', 'category descending', 'contact ID ascending', 'contact ID descending', 'due date', 'last updated ascending', 'last updated descending', 'priority order ascending', 'priority order descending', 'status order ascending', 'status order descending', 'subject in alphabetical order ascending', 'subject in alphabetical order descending', 'ticket creation date ascending', 'ticket creation date descending', 'ticket ID ascending', 'ticket ID descending', 'ticket last modified date ascending', 'ticket last modified date descending', 'unresponded tickets first']|last updated descending|
|status|integer|None|False|Filter tickets by status ID|None|1|

Example input:

```
{
  "category": 1,
  "minifyResponse": false,
  "page": 1,
  "query": "tags:'tag1','tag2'",
  "size": 20,
  "sort": "last updated descending",
  "status": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticketIds|[]integer|False|List of ticket IDs obtained using the given filters. Returned if Minify Response is set to true|
|tickets|[]ticket|False|Information about all tickets obtained using the given filters. Returned if Minify Response is set to false|

Example output:

```
{
  "tickets": [
    {
      "status": {
        "name": "New",
        "color": "FF9900",
        "order": 1,
        "default": true,
        "behavior": "pending",
        "id": 1
      },
      "firstMessage": "Example description\n\n",
      "lastUserReplyAt": "2022-12-27 12:22:59",
      "id": 25,
      "messagesCount": 1,
      "subject": "New Ticket",
      "category": {
        "prepopulateCc": "AR",
        "description": "Tickets will be created here by default.",
        "timeSpentMandatory": false,
        "public": true,
        "id": 1,
        "name": "Test"
      },
      "attachmentsCount": 2,
      "lastUpdatedAt": "2022-12-27 12:22:59",
      "priority": {
        "default": false,
        "id": 4,
        "name": "Low",
        "order": 1
      },
      "customFields": [
        {
          "compulsoryOnComplete": false,
          "name": "Test Field",
          "value": "test value",
          "type": "text",
          "id": 1,
          "visibleToStaffOnly": false
        },
        {
          "compulsoryOnComplete": true,
          "name": "Test Field 2",
          "type": "text",
          "id": 4,
          "visibleToStaffOnly": false
        }
      ],
      "slaBreaches": 0,
      "mergedTickets": [],
      "visibleOnlyStaff": false,
      "displayId": "#RS00000025",
      "dueDate": "2023-01-01",
      "tags": "test tag,tag1",
      "lastModified": "2022-12-27 12:22:59",
      "user": {
        "name": "Test User",
        "primaryPhone": {
          "type": "m",
          "number": "111111111",
          "id": 3
        },
        "phones": [
          {
            "type": "m",
            "number": "111111111",
            "id": 3
          }
        ],
        "createdAt": "2022-12-14 11:10:21",
        "updatedAt": "2022-12-14 11:10:21",
        "pendingTicketsCount": 19,
        "contactGroups": [],
        "ticketsCount": 19,
        "id": 7,
        "email": "user@example.com",
        "customFields": []
      },
      "subscribers": [],
      "unresponded": true,
      "createdAt": "2022-12-27 12:22:59",
      "source": "TKT_CREATION_API",
      "updates": [
        {
          "priorityChange": {
            "newName": "Low",
            "new": 4
          },
          "timestamp": "2022-12-27 12:22:59",
          "dueDateChange": {
            "new": "2023-01-01"
          },
          "by": {
            "email": "user@example.com",
            "type": "user",
            "id": 7,
            "name": "Test User"
          },
          "updateId": 29,
          "message": {
            "attachments": [
              {
                "url": "https://example.com",
                "id": 9,
                "filename": "text.txt"
              },
              {
                "url": "https://example.com",
                "id": 10,
                "filename": "text2.txt"
              }
            ],
            "bccList": "user@example.com",
            "text": "Example description\n\n",
            "ccList": "user@example.com",
            "customerUpdated": false,
            "html": "<html><head><meta charset=\"utf-8\"></head><body>Example description</body></html>"
          },
          "statusChange": {
            "newName": "New",
            "new": 1
          }
        }
      ]
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### assignee

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Active|boolean|False|Active|
|Categories|[]integer|False|Categories|
|Email|string|False|Email|
|ID|integer|False|ID|
|Is Account Admin|boolean|False|Is account admin|
|Name|string|False|Name|
|Permissions|[]string|False|Permissions|
|Role|role|False|Role|

#### attachment

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Filename|string|False|Filename|
|ID|integer|False|ID|
|URL|string|False|URL|

#### by

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|Email|
|ID|integer|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### category

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|ID|integer|False|ID|
|Name|string|False|Name|
|Prepopulate CC|string|False|Prepopulate CC|
|Public|boolean|False|Public|
|Time Spent Mandatory|boolean|False|Whether adding time spent is mandatory|

#### change

|Name|Type|Required|Description|
|----|----|--------|-----------|
|New|integer|False|New|
|New Name|string|False|New name|
|Old|integer|False|Old|
|Old Name|string|False|Old name|

#### customField

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Compulsory On Complete|boolean|False|Whether this field is required on ticket completion|
|ID|integer|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|
|Value|string|False|Value|
|Visible To Staff Only|boolean|False|Visible to staff only|

#### dateChange

|Name|Type|Required|Description|
|----|----|--------|-----------|
|New|string|False|New|
|Old|string|False|Old|

#### message

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attachments|[]attachment|False|Attachments|
|BCC List|string|False|BCC list|
|CC List|string|False|CC list|
|Customer Updated|boolean|False|Customer updated|
|HTML|string|False|HTML|
|Subject|string|False|Subject|
|Text|string|False|Text|

#### phone

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|ID|
|Number|string|False|Number|
|Type|string|False|Type|

#### priority

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Default|boolean|False|Default|
|ID|integer|False|ID|
|Name|string|False|Name|
|Order|integer|False|Order|

#### role

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|ID|
|Name|string|False|Name|

#### status

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Behavior|integer|False|Behavior|
|Color|string|False|Color|
|Default|boolean|False|Default|
|ID|integer|False|ID|
|Name|string|False|Name|
|Order|integer|False|Order|

#### subscriber

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|Email|
|First Name|string|False|First name|
|ID|integer|False|ID|
|Last Name|string|False|Last name|

#### ticket

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assigned To|assignee|False|Assigned to|
|Attachments Count|integer|False|Attachments count|
|Category|category|False|Category|
|Created At|string|False|Created at|
|Custom Fields|[]customField|False|Custom fields|
|Display ID|string|False|Display ID|
|Due By|string|False|Due by|
|Due Date|string|False|Due date|
|First Message|string|False|First message|
|ID|integer|False|ID|
|Last Staff Reply At|string|False|Last staff replay at|
|Last Updated At|string|False|Last updated at|
|Last User Reply At|string|False|Last user reply at|
|Messages Count|integer|False|Messages count|
|Priority|priority|False|Priority|
|SLA Breaches|integer|False|SLA breaches|
|Source|string|False|Source|
|Status|status|False|Status|
|Subject|string|False|Subject|
|Subscribers|[]subscriber|False|Subscribers|
|Tags|string|False|Tags|
|Time Spent|string|False|Time spent|
|Unresponded|boolean|False|Unresponded|
|Updates|[]update|False|Updates|
|User|user|False|User|

#### update

|Name|Type|Required|Description|
|----|----|--------|-----------|
|By|by|False|By|
|Due Date Change|dateChange|False|Due date change|
|Message|message|False|Message|
|Priority Change|change|False|Priority change|
|Status Change|change|False|Status change|
|Time Spent|integer|False|Time spent|
|Timestamp|string|False|Timestamp|
|Update ID|integer|False|Update ID|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created At|string|False|Created at|
|Custom Fields|[]customField|False|Custom fields|
|Email|string|False|Email|
|ID|integer|False|ID|
|Name|string|False|Name|
|Pending Tickets Count|integer|False|Pending tickets count|
|Phones|[]phone|False|Phones|
|Primary Phone|phone|False|Primary phone|
|Tickets Count|integer|False|Tickets count|
|Updated At|string|False|Updated at|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin - Add Create Ticket, Delete Ticket, List Tickets, Create Ticket with Attachments and Create Inline Attachment actions

# Links

* [HappyFox](https://www.happyfox.com/)

## References

* [HappyFox](https://www.happyfox.com/)

