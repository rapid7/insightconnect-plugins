# Description

FreshDesk is an online cloud-based customer service software providing help desk support with all smart automations to get things done faster

# Key Features

* Create and update FreshDesk ticket
* Get list of FreshDesk tickets
* Get ticket by ID

# Requirements

* [FreshDesk API Key](https://support.freshdesk.com/en/support/solutions/articles/215517-how-to-find-your-api-key)
* FreshDesk domain name


# Supported Product Versions

* FreshDesk API v2

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|apiKey|credential_secret_key|None|True|API key|None|eXaMpl3APIK3Y|
|domainName|string|None|True|Name of your FreshDesk domain|None|rapid7|

Example input:

```
{
  "apiKey": "eXaMpl3APIK3Y",
  "domainName": "rapid7"
}
```

## Technical Details

### Actions

#### Create Ticket

This action is used to create a FreshDesk ticket. At least one of those parameters must be provided - 'requesterId', 'email', 'phone', 'twitterId', 'uniqueExternalId'.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachments|[]attachmentInput|None|False|Ticket attachments. The total size of these attachments cannot exceed 20MB|None|[{"name": "new_file.png", "content": "aGVsbG8gd29ybGQ="}]|
|ccEmails|[]string|None|False|Email address added in the 'CC' field of the incoming ticket email|None|["user@example.com"]|
|companyId|integer|None|False|Company ID of the requester. This attribute can only be set if the Multiple Companies feature is enabled (Estate plan and above)|None|103000179654|
|customFields|object|None|False|Key value pairs containing the names and values of custom fields. Read more at https://support.freshdesk.com/support/solutions/articles/216548|None|{"my_key": "my_value"}|
|description|string|None|True|HTML content of the ticket|None|My new ticket|
|dueBy|date|None|False|Timestamp that denotes when the ticket is due to be resolved|None|2023-12-24 12:56:15+05:00|
|emailConfigId|integer|None|False|ID of email config which is used for this ticket. If productId is given and emailConfigId is not given, product's primary emailConfigId will be set|None|103000032123|
|frDueBy|date|None|False|Timestamp that denotes when the first response is due|None|2023-12-21 12:56:15+05:00|
|groupId|integer|None|False|ID of the group to which the ticket has been assigned. The default value is the ID of the group that is associated with the given emailConfigId|None|103000085325|
|internalAgentId|integer|None|False|ID of the internal agent which the ticket should be assigned with. To use this parameter you have to enable `Shared ownership` in Admin > Advanced Ticketing menu|None|103018312012|
|internalGroupId|integer|None|False|ID of the internal group to which the ticket should be assigned with. To use this parameter you have to enable `Shared ownership` in Admin > Advanced Ticketing menu|None|103000096140|
|name|string|None|False|Name of the requester|None|Example Requester|
|parentId|integer|None|False|ID of the parent ticket under which the child ticket needs to be created. To use this parameter you have to enable `Parent-child ticketing` in Admin > Advanced Ticketing menu|None|11|
|phone|string|None|False|Phone number of the requester. If no contact exists with this phone number in FreshDesk, it will be added as a new contact. If the phone number is set and the email address is not, then the name attribute is mandatory|None|611800861902|
|email|string|None|False|Email address of the requester. If no contact exists with this email address in FreshDesk, it will be added as a new contact|None|user@example.com|
|priority|string|None|True|Priority of the ticket|None|High|
|productId|integer|None|False|ID of the product to which the ticket is associated. It will be ignored if the emailConfigId attribute is set in the request|None|103000000638|
|relatedTicketIds|[]integer|None|False|List of Ticket IDs which needs to be linked to the Tracker being created. To use this parameter you have to enable `Linked tickets` in Admin > Advanced Ticketing menu|None|[21, 43]|
|requesterId|integer|None|False|User ID of the requester. For existing contacts, the requesterId can be passed instead of the requester's email|None|103021764889|
|source|string|None|False|The channel through which the ticket was created|None|Portal|
|status|string|None|True|Status of the ticket|None|Open|
|subject|string|None|True|Subject of the ticket|None|Example Subject|
|tags|[]string|None|False|Tags that have been associated with the ticket|None|["my_tag", "second_tag"]|
|twitterId|string|None|False|Twitter handle of the requester. If no contact exists with this handle in FreshDesk, it will be added as a new contact|None|123654789|
|type|string|None|False|Helps categorize the ticket according to the different kinds of issues your support team deals with|None|Incident|
|uniqueExternalId|string|None|False|External ID of the requester. If no contact exists with this external ID in FreshDesk, they will be added as a new contact|None|my_example_id|

Example input:

```
{
  "attachments": [
    {
      "name": "new_file.png",
      "content": "aGVsbG8gd29ybGQ="
    }
  ],
  "ccEmails": [
    "user@example.com"
  ],
  "customFields": {
    "my_key": "my_value"
  },
  "description": "My new ticket",
  "dueBy": "2023-12-24T12:56:15+05:00",
  "email": "user@example.com",
  "emailConfigId": 103000032123,
  "frDueBy": "2023-12-21T12:56:15+05:00",
  "groupId": 103000085325,
  "name": "Example Requester",
  "phone": "611800861902",
  "priority": "High",
  "productId": 103000000638,
  "relatedTicketIds": [
    21,
    43
  ],
  "requesterId": 103021764889,
  "source": "Portal",
  "status": "Open",
  "subject": "Example Subject",
  "tags": [
    "my_tag",
    "second_tag"
  ],
  "twitterId": "123654789",
  "type": "Incident",
  "uniqueExternalId": "my_example_id"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|------|
|ticket|ticket|True|Ticket details|{}|

Example output:

```
{
  "ticket": {
    "ccEmails": [
      "user@example.com"
    ],
    "fwdEmails": [],
    "replyCcEmails": [
      "user@example.com"
    ],
    "ticketCcEmails": [
      "user@example.com"
    ],
    "spam": false,
    "emailConfigId": 103000032123,
    "frEscalated": false,
    "groupId": 103000085325,
    "priority": "High",
    "requesterId": 103021871212,
    "source": "Portal",
    "status": "Open",
    "subject": "Example Subject",
    "customFields": {
      "cf_my_key": "my_value"
    },
    "description": "<div>My new ticket</div>",
    "descriptionText": "My new ticket",
    "id": 127,
    "type": "Incident",
    "productId": 103000000638,
    "associationType": 3,
    "associatedTicketsList": [
      43
    ],
    "attachments": [
      {
        "id": 103002339218,
        "contentType": "application/octet-stream",
        "size": 11,
        "name": "new_file.png",
        "attachmentUrl": "https://example.com/storage/euc-cdn.freshdesk.com/data/helpdesk/attachments/production/103002339218/original/new_file.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAS6FNSMY2XLZULJPI%2F20221025%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20221025T105751Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=65c7aa2f82ead5cbe8cb675cb10c9d02b00c63d654cfc94f95e3a03e2d1da380",
        "createdAt": "2022-10-25T10:57:51Z",
        "updatedAt": "2022-10-25T10:57:51Z"
      }
    ],
    "isEscalated": false,
    "tags": [
      "my_tag",
      "second_tag"
    ],
    "nrEscalated": false,
    "createdAt": "2022-10-25T10:57:50Z",
    "updatedAt": "2022-10-25T10:57:50Z",
    "dueBy": "2023-12-24T07:56:15Z",
    "frDueBy": "2023-12-21T07:56:15Z",
    "formId": 103000025687
  }
}
```

#### Get Ticket by ID

This action is used to get ticket details.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|include|string|None|False|Include additional ticket informations|['conversations', 'requester', 'company', 'stats', 'None']|company|
|ticketId|integer|None|True|ID of the Ticket|None|178|

Example input:

```
{
  "include": "company",
  "ticketId": 178
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|------|
|ticket|ticket|True|Ticket details|{}|

Example output:

```
{
  "ticket": {
    "ccEmails": [
      "user@example.com"
    ],
    "fwdEmails": [],
    "replyCcEmails": [
      "user@example.com"
    ],
    "ticketCcEmails": [
      "user@example.com"
    ],
    "frEscalated": false,
    "spam": false,
    "emailConfigId": 103000032123,
    "groupId": 103000085325,
    "priority": "Low",
    "requesterId": 103021764887,
    "source": "Phone",
    "status": "xyz test status",
    "subject": "API Ticket",
    "associationType": 3,
    "productId": 103000000638,
    "id": 178,
    "type": "Incident",
    "dueBy": "2023-12-24T07:26:15Z",
    "frDueBy": "2023-12-21T07:26:15Z",
    "isEscalated": false,
    "description": "<div>Ticket detail</div>",
    "descriptionText": "Ticket detail",
    "customFields": {
      "cf_test_key": 4444748,
      "cf_new_field": "124.0"
    },
    "createdAt": "2022-10-25T07:57:19Z",
    "updatedAt": "2022-10-25T07:57:19Z",
    "tags": [
      "mc_tag",
      "tag2"
    ],
    "attachments": [
      {
        "id": 103002319445,
        "contentType": "image/png",
        "size": 169199,
        "name": "first_plugin_attachment.png",
        "attachmentUrl": "https://example.storage.com/euc-cdn.freshdesk.com/data/helpdesk/attachments/production/103002319445/original/first_plugin_attachment.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAS6FNSMY2XLZULJPI%2F20221025%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20221025T110745Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=c0a49c14e403a20ec617b450ed582f0ba5ff3147100a274db2bec2a766222374",
        "createdAt": "2022-10-25T08:05:25Z",
        "updatedAt": "2022-10-25T08:05:25Z"
      }
    ],
    "associatedTicketsList": [
      1
    ],
    "conversations": [],
    "nrEscalated": false
  }
}
```

#### Get Tickets List

This action is used to get tickets list. In `filterBy` input you can use only one of `requester` type inputs - `Requester ID`, `Requester Email` or `Requester Unique External ID`

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filterBy|ticketsFilter|None|False|Filter tickets by a specific fields|None|{"requesterId": 54332121123}|
|include|string|None|False|Include additional ticket informations|['requester', 'company', 'stats', 'None']|company|
|orderBy|string|None|False|Order tickets by specific field|['created_at', 'due_by', 'updated_at', 'status']|status|
|orderType|string|None|False|Type of the order|['asc', 'desc']|asc|
|page|integer|None|False|Page number|None|3|
|perPage|integer|None|False|Results per page. Less or equal to 100|None|12|
|predefinedFilter|string|None|False|The various filters available are new_and_my_open, watching, spam, deleted|None|new_and_my_open|

Example input:

```
{
  "filterBy": {
    "requesterId": 54332121123
  },
  "include": "company",
  "orderBy": "status",
  "orderType": "asc",
  "page": 3,
  "perPage": 12,
  "predefinedFilter": "new_and_my_open"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|------|
|tickets|[]ticket|True|List of tickets|[]|

Example output:

```
{
  "tickets": [
    {
      "ccEmails": [],
      "fwdEmails": [],
      "replyCcEmails": [],
      "ticketCcEmails": [],
      "frEscalated": false,
      "spam": false,
      "groupId": 103000085326,
      "priority": "Medium",
      "requesterId": 103018312028,
      "source": "Phone",
      "status": "Open",
      "subject": "Email address change",
      "associationType": 4,
      "id": 1,
      "type": "Question",
      "dueBy": "2022-10-04T07:00:00Z",
      "frDueBy": "2022-10-03T15:00:00Z",
      "isEscalated": true,
      "customFields": {},
      "createdAt": "2022-10-01T09:28:39Z",
      "updatedAt": "2022-10-25T07:57:19Z",
      "tags": [],
      "company": {},
      "nrEscalated": false
    },
    {
      "frEscalated": true,
      "spam": false,
      "groupId": 103000085326,
      "priority": "Medium",
      "requesterId": 103018312078,
      "source": "Email",
      "companyId": 103000150466,
      "status": "Open",
      "subject": "Payment failed",
      "associationType": 4,
      "id": 2,
      "type": "Question",
      "dueBy": "2022-10-04T07:00:00Z",
      "frDueBy": "2022-10-03T15:00:00Z",
      "isEscalated": true,
      "customFields": {},
      "createdAt": "2022-10-01T09:28:39Z",
      "updatedAt": "2022-10-12T10:29:55Z",
      "tags": [],
      "company": {
        "id": 103000150466,
        "name": "Acme Inc."
      },
      "nrEscalated": false
    },
    {
      "frEscalated": true,
      "spam": false,
      "groupId": 103000085326,
      "priority": "Low",
      "requesterId": 103018312171,
      "source": "Email",
      "status": "Open",
      "subject": "Received a broken TV",
      "id": 3,
      "type": "Question",
      "dueBy": "2022-10-06T12:00:51Z",
      "frDueBy": "2022-10-03T21:00:00Z",
      "isEscalated": true,
      "customFields": {},
      "createdAt": "2022-10-01T09:28:39Z",
      "updatedAt": "2022-10-06T12:14:45Z",
      "tags": [],
      "company": {},
      "nrEscalated": false
    }
  ]
}
```

#### Update Ticket

This action is used to update a FreshDesk ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachments|[]attachmentInput|None|False|Ticket attachments. The total size of these attachments cannot exceed 20MB|None|[{"name": "new_file.png", "content": "aGVsbG8gd29ybGQ="}]|
|companyId|integer|None|False|Company ID of the requester. This attribute can only be set if the Multiple Companies feature is enabled (Estate plan and above)|None|103000179654|
|customFields|object|None|False|Key value pairs containing the names and values of custom fields. Read more at https://support.freshdesk.com/support/solutions/articles/216548|None|{"my_key": "my_value"}|
|description|string|None|False|HTML content of the ticket|None|My new ticket|
|email|string|None|False|Email address of the requester. If no contact exists with this email address in FreshDesk, it will be added as a new contact|None|user@example.com|
|dueBy|date|None|False|Timestamp that denotes when the ticket is due to be resolved|None|2023-12-24 12:56:15+05:00|
|emailConfigId|integer|None|False|ID of email config which is used for this ticket. If productId is given and emailConfigId is not given, product's primary emailConfigId will be set|None|103000032123|
|frDueBy|date|None|False|Timestamp that denotes when the first response is due|None|2023-12-21 12:56:15+05:00|
|groupId|integer|None|False|ID of the group to which the ticket has been assigned. The default value is the ID of the group that is associated with the given emailConfigId|None|103000085325|
|internalAgentId|integer|None|False|ID of the internal agent which the ticket should be assigned with. To use this parameter you have to enable `Shared ownership` in Admin > Advanced Ticketing menu|None|103018312012|
|internalGroupId|integer|None|False|ID of the internal group to which the ticket should be assigned with. To use this parameter you have to enable `Shared ownership` in Admin > Advanced Ticketing menu|None|103000096140|
|name|string|None|False|Name of the requester|None|Example Requester|
|phone|string|None|False|Phone number of the requester. If no contact exists with this phone number in FreshDesk, it will be added as a new contact. If the phone number is set and the email address is not, then the name attribute is mandatory|None|611800861902|
|priority|string|None|False|Priority of the ticket|None|High|
|productId|integer|None|False|ID of the product to which the ticket is associated. It will be ignored if the emailConfigId attribute is set in the request|None|103000000638|
|relatedTicketIds|[]integer|None|False|List of Ticket IDs which needs to be linked to the Tracker being created. To use this parameter you have to enable `Linked tickets` in Admin > Advanced Ticketing menu|None|[21, 43]|
|requesterId|integer|None|False|User ID of the requester. For existing contacts, the requesterId can be passed instead of the requester's email|None|103021764889|
|source|string|None|False|The channel through which the ticket was created|None|Portal|
|status|string|None|False|Status of the ticket|None|Open|
|subject|string|None|False|Subject of the ticket|None|Example Subject|
|tags|[]string|None|False|Tags that have been associated with the ticket|None|["my_tag", "second_tag"]|
|ticketId|integer|None|True|ID of the Ticket|None|178|
|twitterId|string|None|False|Twitter handle of the requester. If no contact exists with this handle in FreshDesk, it will be added as a new contact|None|123654789|
|type|string|None|False|Helps categorize the ticket according to the different kinds of issues your support team deals with|None|Incident|
|uniqueExternalId|string|None|False|External ID of the requester. If no contact exists with this external ID in FreshDesk, they will be added as a new contact|None|my_example_id|

Example input:

```
{
  "attachments": [
    {
      "name": "new_file.png",
      "content": "aGVsbG8gd29ybGQ="
    }
  ],
  "companyId": 103000179654,
  "customFields": {
    "my_key": "my_value"
  },
  "description": "My new ticket",
  "dueBy": "2023-12-24T12:56:15+05:00",
  "email": "user@example.com",
  "emailConfigId": 103000032123,
  "frDueBy": "2023-12-21T12:56:15+05:00",
  "groupId": 103000085325,
  "internalAgentId": 103018312012,
  "internalGroupId": 103000096140,
  "name": "Example Requester",
  "phone": 611800861902,
  "priority": "High",
  "productId": 103000000638,
  "relatedTicketIds": [
    21,
    43
  ],
  "requesterId": 103021764889,
  "source": "Portal",
  "status": "Open",
  "subject": "Example Subject",
  "tags": [
    "my_tag",
    "second_tag"
  ],
  "ticketId": 178,
  "twitterId": 123654789,
  "type": "Incident",
  "uniqueExternalId": "my_example_id"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|------|
|ticket|ticket|True|Ticket details|{}|

Example output:

```
{
  "ticket": {
    "ccEmails": [
      "user@example.com"
    ],
    "fwdEmails": [],
    "replyCcEmails": [
      "user@example.com"
    ],
    "ticketCcEmails": [
      "user@example.com"
    ],
    "spam": false,
    "emailConfigId": 103000032123,
    "frEscalated": false,
    "groupId": 103000085325,
    "priority": "High",
    "requesterId": 103021871212,
    "source": "Portal",
    "status": "Open",
    "subject": "Example Subject",
    "customFields": {
      "cf_my_key": "my_value"
    },
    "description": "<div>My new ticket</div>",
    "descriptionText": "My new ticket",
    "id": 178,
    "type": "Incident",
    "productId": 103000000638,
    "associationType": 3,
    "associatedTicketsList": [
      43
    ],
    "attachments": [
      {
        "id": 103002339218,
        "contentType": "application/octet-stream",
        "size": 11,
        "name": "new_file.png",
        "attachmentUrl": "https://example.com/storage/euc-cdn.freshdesk.com/data/helpdesk/attachments/production/103002339218/original/new_file.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAS6FNSMY2XLZULJPI%2F20221025%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20221025T105751Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=65c7aa2f82ead5cbe8cb675cb10c9d02b00c63d654cfc94f95e3a03e2d1da380",
        "createdAt": "2022-10-25T10:57:51Z",
        "updatedAt": "2022-10-25T10:57:51Z"
      }
    ],
    "isEscalated": false,
    "tags": [
      "my_tag",
      "second_tag"
    ],
    "nrEscalated": false,
    "createdAt": "2022-10-25T10:57:50Z",
    "updatedAt": "2022-10-25T10:57:50Z",
    "dueBy": "2023-12-24T07:56:15Z",
    "frDueBy": "2023-12-21T07:56:15Z",
    "formId": 103000025687
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### attachmentInput

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Content|string|True|Base64 encoded content of the attachment|
|Name|string|True|Attachment name|

#### attachmentOutput

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attachment URL|string|False|URL of the attachment|
|Content Type|string|False|Content type of the attachment|
|Created At|string|False|Date of the attachment creation|
|ID|integer|False|ID of the attachment|
|Name|string|False|Attachment name|
|Size|integer|False|Size of the attachment|
|Updated At|string|False|Date of the attachment update|

#### company

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|Company ID|
|Name|string|False|Company name|

#### conversation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attachments|[]attachmentOutput|False|Conversation attachments|
|Auto Response|boolean|False|Auto response|
|Automation ID|integer|False|Automation ID|
|Automation Type ID|integer|False|Automation type ID|
|Bcc Emails|[]string|False|BCC emails|
|Body|string|False|Conversation body|
|Body Text|string|False|Conversation body text|
|Cc Emails|[]string|False|CC emails|
|Created At|string|False|Date of the conversation creation|
|Email Failure Count|integer|False|Email failure count|
|From Email|string|False|From email|
|ID|integer|False|Conversation ID|
|Incoming|boolean|False|Incoming conversation|
|Last Edited At|string|False|Date of the last conversation edit|
|Last Edited User ID|integer|False|Last edited user ID|
|Private|boolean|False|Private conversation|
|Support Email|string|False|Support email|
|Thread ID|integer|False|Thread ID|
|Thread Message ID|integer|False|Thread message ID|
|Ticket ID|integer|False|Ticket ID|
|To Emails|[]string|False|To emails|
|Updated At|string|False|Date of the conversation update|
|User ID|integer|False|Conversation user ID|

#### requester

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|Requester email|
|ID|integer|False|Requester ID|
|Mobile|string|False|Requester mobile|
|Name|string|False|Requester name|
|Phone|string|False|Requester phone|

#### stats

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent Responded At|string|False|Agent responded at|
|Closed At|string|False|Closed at|
|First Responded At|string|False|First responded at|
|Pending Since|string|False|Pending since|
|Reopened At|string|False|Reopened at|
|Requester Responded At|string|False|Requester responded at|
|Resolved At|string|False|Resolved at|
|Status Updated At|string|False|Status updated at|

#### ticket

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Associated Tickets List|[]integer|False|List of Ticket IDs which are linked to this ticket|
|Association Type|integer|False|Association type, where 1 - Parent, 2 - Child, 3 - Tracker, 4 - Related|
|Attachments|[]attachmentOutput|False|Ticket attachments. The total size of these attachments cannot exceed 20MB|
|CC Emails|[]string|False|Email address added in the 'CC' field of the incoming ticket email|
|Company|company|False|Company details|
|Company ID|integer|False|Company ID of the requester|
|Conversations|[]conversation|False|Ticket conversations|
|Created At|date|False|Ticket creation timestamp|
|Custom Fields|object|False|Key value pairs containing the names and values of custom fields. Read more at https://support.freshdesk.com/support/solutions/articles/216548|
|Deleted|boolean|False|Set to true if the ticket has been deleted/trashed. Deleted tickets will not be displayed in any views except the "deleted" filter|
|Description|string|False|HTML content of the ticket|
|Description Text|string|False|Content of the ticket in plain text|
|Due By|string|False|Timestamp that denotes when the ticket is due to be resolved|
|Email|string|False|Email address of the requester|
|Email Config ID|integer|False|ID of email config which is used for this ticket|
|First Response Due By|date|False|Timestamp that denotes when the first response is due|
|First Response Escalated|boolean|False|Set to true if the ticket has been escalated as the result of first response time being breached|
|Forward Emails|[]string|False|Email address added while forwarding a ticket|
|Group ID|integer|False|ID of the group to which the ticket has been assigned|
|Internal Agent ID|integer|False|ID of the internal agent which the ticket should be assigned with|
|Internal Group ID|integer|False|ID of the internal group to which the ticket should be assigned with|
|Is Escalated|boolean|False|Set to true if the ticket has been escalated for any reason|
|Name|string|False|Name of the requester|
|Parent ID|integer|False|ID of the parent ticket under which the child ticket was created|
|Phone|string|False|Phone number of the requester|
|Priority|string|False|Priority of the ticket|
|Product ID|integer|False|ID of the product to which the ticket is associated|
|Reply CC Emails|[]string|False|Email address added while replying to a ticket|
|Requester|requester|False|Requester details|
|Requester ID|integer|False|User ID of the requester|
|Responder ID|integer|False|ID of the agent to whom the ticket has been assigned|
|Source|string|False|The channel through which the ticket was created|
|Spam|boolean|False|Set to true if the ticket has been marked as spam|
|Stats|stats|False|Ticket stats|
|Status|string|False|Status of the ticket|
|Subject|string|False|Subject of the ticket|
|Tags|[]string|False|Tags that have been associated with the ticket|
|To Emails|[]string|False|Email addresses to which the ticket was originally sent|
|Twitter ID|string|False|Twitter handle of the requester|
|Type|string|False|Helps categorize the ticket according to the different kinds of issues your support team deals with|
|Unique External ID|string|False|External ID of the requester|
|Updated At|date|False|Ticket updated timestamp|

#### ticketsFilter

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Company ID|integer|False|Company ID of the requester|
|Requester Email|string|False|Email of the requester|
|Requester ID|integer|False|ID of the requester|
|Requester Unique External ID|string|False|External ID of the requester|
|Updated Since|string|False|Tickets updated since specified date|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin - Actions: `Create Ticket`, `Update Ticket`, `Get Tickets`, `Get Ticket by ID`

# Links

* [FreshDesk](https://freshdesk.com/)

## References

* [FreshDesk](https://freshdesk.com/)

