# Description

FreshDesk is an online cloud-based customer service software providing help desk support with all smart automations to get things done faster

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* FreshDesk API v2

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|apiKey|credential_secret_key|None|True|API key|None|eXaMpl3APIK3Y|None|None|
|domainName|string|None|True|Name of your FreshDesk domain|None|rapid7|None|None|

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

This action is used to create a FreshDesk ticket. At least one of those parameters must be provided - 'requesterId', 
'email', 'phone', 'twitterId', 'uniqueExternalId'

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachments|[]attachmentInput|None|False|Ticket attachments. The total size of these attachments cannot exceed 20MB|None|[{"name": "new_file.png", "content": "aGVsbG8gd29ybGQ="}]|None|None|
|ccEmails|[]string|None|False|Email address added in the 'CC' field of the incoming ticket email|None|["user@example.com"]|None|None|
|companyId|integer|None|False|Company ID of the requester. This attribute can only be set if the Multiple Companies feature is enabled (Estate plan and above)|None|103000179654|None|None|
|customFields|object|None|False|Key value pairs containing the names and values of custom fields. Read more at https://support.freshdesk.com/support/solutions/articles/216548|None|{"my_key": "my_value"}|None|None|
|description|string|None|True|HTML content of the ticket|None|My new ticket|None|None|
|dueBy|date|None|False|Timestamp that denotes when the ticket is due to be resolved|None|2023-12-24 12:56:15+05:00|None|None|
|email|string|None|False|Email address of the requester. If no contact exists with this email address in FreshDesk, it will be added as a new contact|None|user@example.com|None|None|
|emailConfigId|integer|None|False|ID of email config which is used for this ticket. If productId is given and emailConfigId is not given, product's primary emailConfigId will be set|None|103000032123|None|None|
|frDueBy|date|None|False|Timestamp that denotes when the first response is due|None|2023-12-21 12:56:15+05:00|None|None|
|groupId|integer|None|False|ID of the group to which the ticket has been assigned. The default value is the ID of the group that is associated with the given emailConfigId|None|103000085325|None|None|
|internalAgentId|integer|None|False|ID of the internal agent which the ticket should be assigned with. To use this parameter you have to enable `Shared ownership` in Admin > Advanced Ticketing menu|None|103018312012|None|None|
|internalGroupId|integer|None|False|ID of the internal group to which the ticket should be assigned with. To use this parameter you have to enable `Shared ownership` in Admin > Advanced Ticketing menu|None|103000096140|None|None|
|name|string|None|False|Name of the requester|None|Example Requester|None|None|
|parentId|integer|None|False|ID of the parent ticket under which the child ticket needs to be created. To use this parameter you have to enable `Parent-child ticketing` in Admin > Advanced Ticketing menu|None|11|None|None|
|phone|string|None|False|Phone number of the requester. If no contact exists with this phone number in FreshDesk, it will be added as a new contact. If the phone number is set and the email address is not, then the name attribute is mandatory|None|611800861902|None|None|
|priority|string|None|True|Priority of the ticket|None|High|None|None|
|productId|integer|None|False|ID of the product to which the ticket is associated. It will be ignored if the emailConfigId attribute is set in the request|None|103000000638|None|None|
|relatedTicketIds|[]integer|None|False|List of Ticket IDs which needs to be linked to the Tracker being created. To use this parameter you have to enable `Linked tickets` in Admin > Advanced Ticketing menu|None|[21, 43]|None|None|
|requesterId|integer|None|False|User ID of the requester. For existing contacts, the requesterId can be passed instead of the requester's email|None|103021764889|None|None|
|responderId|integer|None|False|User ID of the responder. For existing contacts, the requesterId can be passed instead of the requester's email|None|103021764889|None|None|
|source|string|None|False|The channel through which the ticket was created|None|Portal|None|None|
|status|string|None|True|Status of the ticket|None|Open|None|None|
|subject|string|None|True|Subject of the ticket|None|Example Subject|None|None|
|tags|[]string|None|False|Tags that have been associated with the ticket|None|["my_tag", "second_tag"]|None|None|
|twitterId|string|None|False|Twitter handle of the requester. If no contact exists with this handle in FreshDesk, it will be added as a new contact|None|123654789|None|None|
|type|string|None|False|Helps categorize the ticket according to the different kinds of issues your support team deals with|None|Incident|None|None|
|uniqueExternalId|string|None|False|External ID of the requester. If no contact exists with this external ID in FreshDesk, they will be added as a new contact|None|my_example_id|None|None|
  
Example input:

```
{
  "attachments": [
    {
      "content": "aGVsbG8gd29ybGQ=",
      "name": "new_file.png"
    }
  ],
  "ccEmails": [
    "user@example.com"
  ],
  "companyId": 103000179654,
  "customFields": {
    "my_key": "my_value"
  },
  "description": "My new ticket",
  "dueBy": "2023-12-24 12:56:15+05:00",
  "email": "user@example.com",
  "emailConfigId": 103000032123,
  "frDueBy": "2023-12-21 12:56:15+05:00",
  "groupId": 103000085325,
  "internalAgentId": 103018312012,
  "internalGroupId": 103000096140,
  "name": "Example Requester",
  "parentId": 11,
  "phone": 611800861902,
  "priority": "High",
  "productId": 103000000638,
  "relatedTicketIds": [
    21,
    43
  ],
  "requesterId": 103021764889,
  "responderId": 103021764889,
  "source": "Portal",
  "status": "Open",
  "subject": "Example Subject",
  "tags": [
    "my_tag",
    "second_tag"
  ],
  "twitterId": 123654789,
  "type": "Incident",
  "uniqueExternalId": "my_example_id"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|True|Ticket details|{}|
  
Example output:

```
{
  "ticket": {}
}
```

#### Filter Ticks

This action is used to use custom ticket fields that you have created in your account to filter through the tickets and
 get a list of tickets matching the specified ticket fields

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|integer|None|False|To scroll through the pages add page parameter to the url. The page number starts with 1 and should not exceed 10|None|2|None|None|
|query|string|None|False|Case sensitive query to filter against, supported fields are agent_id, group_id, priority, status, tag, type, due_by, fr_due_by, created_at, updated_at. Max 512 characters|None|(ticket_field:integer OR ticket_field:'string') AND ticket_field:boolean|None|None|
  
Example input:

```
{
  "page": 2,
  "query": "(ticket_field:integer OR ticket_field:'string') AND ticket_field:boolean"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]filteredTicket|False|Filtered tickets. The number of objects returned per page is 30|[{"cc_emails": ["clark.kent@kryptonspace.com"], "fwd_emails": ["clark.kent@kryptonspace.com"], "reply_cc_emails": ["clark.kent@kryptonspace.com"], "fr_escalated": false, "spam": false, "email_config_id": 17, "group_id": 156, "priority": 3, "requester_id": 6007738334, "responder_id": 6001263404, "source": 2, "company_id": 2, "status": 2, "subject": "Sample Title", "to_emails": ["clark.kent@kryptonspace.com"], "product_id": 1, "id": 47, "type": "Incident", "due_by": "2016-02-23T16:00:00Z", "fr_due_by": "2016-02-22T17:00:00Z", "is_escalated": true, "description": "<div>Sample description</div>", "description_text": "Sample description", "created_at": "2016-02-20T09:16:58Z", "updated_at": "2016-02-23T16:14:57Z", "custom_fields": {"my_key": "my_value"}}]|
|total|integer|False|Count of filtered tickets|10|
  
Example output:

```
{
  "results": [
    {
      "cc_emails": [
        "clark.kent@kryptonspace.com"
      ],
      "company_id": 2,
      "created_at": "2016-02-20T09:16:58Z",
      "custom_fields": {
        "my_key": "my_value"
      },
      "description": "<div>Sample description</div>",
      "description_text": "Sample description",
      "due_by": "2016-02-23T16:00:00Z",
      "email_config_id": 17,
      "fr_due_by": "2016-02-22T17:00:00Z",
      "fr_escalated": false,
      "fwd_emails": [
        "clark.kent@kryptonspace.com"
      ],
      "group_id": 156,
      "id": 47,
      "is_escalated": true,
      "priority": 3,
      "product_id": 1,
      "reply_cc_emails": [
        "clark.kent@kryptonspace.com"
      ],
      "requester_id": 6007738334,
      "responder_id": 6001263404,
      "source": 2,
      "spam": false,
      "status": 2,
      "subject": "Sample Title",
      "to_emails": [
        "clark.kent@kryptonspace.com"
      ],
      "type": "Incident",
      "updated_at": "2016-02-23T16:14:57Z"
    }
  ],
  "total": 10
}
```

#### Get Ticket by ID

This action is used to get ticket details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|include|string|None|False|Include additional ticket informations|["conversations", "requester", "company", "stats", "None"]|company|None|None|
|ticketId|integer|None|True|ID of the Ticket|None|178|None|None|
  
Example input:

```
{
  "include": "company",
  "ticketId": 178
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|True|Ticket details|{}|
  
Example output:

```
{
  "ticket": {}
}
```

#### Get Tickets List

This action is used to get tickets list. In `filterBy` input you can use only one of `requester` type inputs - 
`Requester ID`, `Requester Email` or `Requester Unique External ID`

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filterBy|ticketsFilter|None|False|Filter tickets by a specific fields|None|{"requesterId": 54332121123}|None|None|
|include|string|None|False|Include additional ticket informations|["requester", "company", "stats", "None"]|company|None|None|
|orderBy|string|None|False|Order tickets by specific field|["created_at", "due_by", "updated_at", "status"]|status|None|None|
|orderType|string|None|False|Type of the order|["asc", "desc"]|asc|None|None|
|page|integer|None|False|Page number|None|3|None|None|
|perPage|integer|None|False|Results per page. Less or equal to 100|None|12|None|None|
|predefinedFilter|string|None|False|The various filters available are new_and_my_open, watching, spam, deleted|None|new_and_my_open|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|tickets|[]ticket|True|List of tickets|[]|
  
Example output:

```
{
  "tickets": []
}
```

#### Update Ticket

This action is used to update a FreshDesk ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachments|[]attachmentInput|None|False|Ticket attachments. The total size of these attachments cannot exceed 20MB|None|[{"name": "new_file.png", "content": "aGVsbG8gd29ybGQ="}]|None|None|
|companyId|integer|None|False|Company ID of the requester. This attribute can only be set if the Multiple Companies feature is enabled (Estate plan and above)|None|103000179654|None|None|
|customFields|object|None|False|Key value pairs containing the names and values of custom fields. Read more at https://support.freshdesk.com/support/solutions/articles/216548|None|{"my_key": "my_value"}|None|None|
|description|string|None|False|HTML content of the ticket|None|My new ticket|None|None|
|dueBy|date|None|False|Timestamp that denotes when the ticket is due to be resolved|None|2023-12-24 12:56:15+05:00|None|None|
|email|string|None|False|Email address of the requester. If no contact exists with this email address in FreshDesk, it will be added as a new contact|None|user@example.com|None|None|
|emailConfigId|integer|None|False|ID of email config which is used for this ticket. If productId is given and emailConfigId is not given, product's primary emailConfigId will be set|None|103000032123|None|None|
|frDueBy|date|None|False|Timestamp that denotes when the first response is due|None|2023-12-21 12:56:15+05:00|None|None|
|groupId|integer|None|False|ID of the group to which the ticket has been assigned. The default value is the ID of the group that is associated with the given emailConfigId|None|103000085325|None|None|
|internalAgentId|integer|None|False|ID of the internal agent which the ticket should be assigned with. To use this parameter you have to enable `Shared ownership` in Admin > Advanced Ticketing menu|None|103018312012|None|None|
|internalGroupId|integer|None|False|ID of the internal group to which the ticket should be assigned with. To use this parameter you have to enable `Shared ownership` in Admin > Advanced Ticketing menu|None|103000096140|None|None|
|name|string|None|False|Name of the requester|None|Example Requester|None|None|
|phone|string|None|False|Phone number of the requester. If no contact exists with this phone number in FreshDesk, it will be added as a new contact. If the phone number is set and the email address is not, then the name attribute is mandatory|None|611800861902|None|None|
|priority|string|None|False|Priority of the ticket|None|High|None|None|
|productId|integer|None|False|ID of the product to which the ticket is associated. It will be ignored if the emailConfigId attribute is set in the request|None|103000000638|None|None|
|relatedTicketIds|[]integer|None|False|List of Ticket IDs which needs to be linked to the Tracker being created. To use this parameter you have to enable `Linked tickets` in Admin > Advanced Ticketing menu|None|[21, 43]|None|None|
|requesterId|integer|None|False|User ID of the requester. For existing contacts, the requesterId can be passed instead of the requester's email|None|103021764889|None|None|
|source|string|None|False|The channel through which the ticket was created|None|Portal|None|None|
|status|string|None|False|Status of the ticket|None|Open|None|None|
|subject|string|None|False|Subject of the ticket|None|Example Subject|None|None|
|tags|[]string|None|False|Tags that have been associated with the ticket|None|["my_tag", "second_tag"]|None|None|
|ticketId|integer|None|True|ID of the Ticket|None|178|None|None|
|twitterId|string|None|False|Twitter handle of the requester. If no contact exists with this handle in FreshDesk, it will be added as a new contact|None|123654789|None|None|
|type|string|None|False|Helps categorize the ticket according to the different kinds of issues your support team deals with|None|Incident|None|None|
|uniqueExternalId|string|None|False|External ID of the requester. If no contact exists with this external ID in FreshDesk, they will be added as a new contact|None|my_example_id|None|None|
  
Example input:

```
{
  "attachments": [
    {
      "content": "aGVsbG8gd29ybGQ=",
      "name": "new_file.png"
    }
  ],
  "companyId": 103000179654,
  "customFields": {
    "my_key": "my_value"
  },
  "description": "My new ticket",
  "dueBy": "2023-12-24 12:56:15+05:00",
  "email": "user@example.com",
  "emailConfigId": 103000032123,
  "frDueBy": "2023-12-21 12:56:15+05:00",
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
| :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|True|Ticket details|{}|
  
Example output:

```
{
  "ticket": {}
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**attachmentInput**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content|string|None|True|Base64 encoded content of the attachment|aGVsbG8gd29ybGQ=|
|Name|string|None|True|Attachment name|my_new_file.png|
  
**attachmentOutput**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attachment URL|string|None|False|URL of the attachment|https://example_storage/my_new23_file.txt|
|Content Type|string|None|False|Content type of the attachment|text/plain|
|Created At|string|None|False|Date of the attachment creation|2022-10-20T08:12:16Z|
|ID|integer|None|False|ID of the attachment|12365432314|
|Name|string|None|False|Attachment name|my_new_file.png|
|Size|integer|None|False|Size of the attachment|169199|
|Updated At|string|None|False|Date of the attachment update|2022-10-21T08:12:16Z|
  
**stats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Responded At|string|None|False|Agent responded at|2022-10-20 16:06:56+00:00|
|Closed At|string|None|False|Closed at|2022-10-20 16:06:56+00:00|
|First Responded At|string|None|False|First responded at|2022-10-20 16:06:56+00:00|
|Pending Since|string|None|False|Pending since|2022-10-20 16:06:56+00:00|
|Reopened At|string|None|False|Reopened at|2022-10-20 16:06:56+00:00|
|Requester Responded At|string|None|False|Requester responded at|2022-10-20 16:06:56+00:00|
|Resolved At|string|None|False|Resolved at|2022-10-20 16:06:56+00:00|
|Status Updated At|string|None|False|Status updated at|2022-10-20 16:06:56+00:00|
  
**company**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Company ID|123455641568|
|Name|string|None|False|Company name|my-comp-any|
  
**requester**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|False|Requester email|user@example.com|
|ID|integer|None|False|Requester ID|123455641568|
|Mobile|string|None|False|Requester mobile|611800338619023|
|Name|string|None|False|Requester name|my-comp-any|
|Phone|string|None|False|Requester phone|481129338619029|
  
**conversation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attachments|[]attachmentOutput|None|False|Conversation attachments|{}|
|Auto Response|boolean|None|False|Auto response|True|
|Automation ID|integer|None|False|Automation ID|2147834253|
|Automation Type ID|integer|None|False|Automation type ID|435434253|
|BCC Emails|[]string|None|False|BCC emails|["user@example.com"]|
|Body|string|None|False|Conversation body|<div style="font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif; font-size:14px"><div dir="ltr">Hello conversation</div></div>|
|Body Text|string|None|False|Conversation body text|Hello conversation|
|CC Emails|[]string|None|False|CC emails|["user@example.com"]|
|Created At|string|None|False|Date of the conversation creation|2022-10-20T08:12:16Z|
|Email Failure Count|integer|None|False|Email failure count|1|
|From Email|string|None|False|From email|user@example.com|
|ID|integer|None|False|Conversation ID|4156415341451|
|Incoming|boolean|None|False|Incoming conversation|True|
|Last Edited At|string|None|False|Date of the last conversation edit|2022-10-20T08:12:16Z|
|Last Edited User ID|integer|None|False|Last edited user ID|345435563465|
|Private|boolean|None|False|Private conversation|True|
|Support Email|string|None|False|Support email|user@example.com|
|Thread ID|integer|None|False|Thread ID|13435435435|
|Thread Message ID|integer|None|False|Thread message ID|1344235435435|
|Ticket ID|integer|None|False|Ticket ID|325|
|To Emails|[]string|None|False|To emails|["user@example.com"]|
|Updated At|string|None|False|Date of the conversation update|2022-10-21T08:12:16Z|
|User ID|integer|None|False|Conversation user ID|57564184515|
  
**ticket**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Associated Tickets List|[]integer|None|False|List of Ticket IDs which are linked to this ticket|[21, 43]|
|Association Type|integer|None|False|Association type, where 1 - Parent, 2 - Child, 3 - Tracker, 4 - Related|3|
|Attachments|[]attachmentOutput|None|False|Ticket attachments. The total size of these attachments cannot exceed 20MB|[]|
|CC Emails|[]string|None|False|Email address added in the 'CC' field of the incoming ticket email|["user@example.com"]|
|Company|company|None|False|Company details|{}|
|Company ID|integer|None|False|Company ID of the requester|103000179654|
|Conversations|[]conversation|None|False|Ticket conversations|[]|
|Created At|date|None|False|Ticket creation timestamp|2023-12-21 12:56:15+05:00|
|Custom Fields|object|None|False|Key value pairs containing the names and values of custom fields. Read more at https://support.freshdesk.com/support/solutions/articles/216548|{"my_key": "my_value"}|
|Deleted|boolean|None|False|Set to true if the ticket has been deleted/trashed. Deleted tickets will not be displayed in any views except the `deleted` filter|False|
|Description|string|None|False|HTML content of the ticket|<div>My new ticket</div>|
|Description Text|string|None|False|Content of the ticket in plain text|My new ticket|
|Due By|string|None|False|Timestamp that denotes when the ticket is due to be resolved|2023-12-24 12:56:15+05:00|
|Email|string|None|False|Email address of the requester|user@example.com|
|Email Config ID|integer|None|False|ID of email config which is used for this ticket|103000032123|
|First Response Due By|date|None|False|Timestamp that denotes when the first response is due|2023-12-21 12:56:15+05:00|
|First Response Escalated|boolean|None|False|Set to true if the ticket has been escalated as the result of first response time being breached|True|
|Forward Emails|[]string|None|False|Email address added while forwarding a ticket|["user@example.com"]|
|Group ID|integer|None|False|ID of the group to which the ticket has been assigned|103000085325|
|Internal Agent ID|integer|None|False|ID of the internal agent which the ticket should be assigned with|103018312012|
|Internal Group ID|integer|None|False|ID of the internal group to which the ticket should be assigned with|103000096140|
|Is Escalated|boolean|None|False|Set to true if the ticket has been escalated for any reason|False|
|Name|string|None|False|Name of the requester|Example Requester|
|Parent ID|integer|None|False|ID of the parent ticket under which the child ticket was created|12|
|Phone|string|None|False|Phone number of the requester|611800861902|
|Priority|string|None|False|Priority of the ticket|High|
|Product ID|integer|None|False|ID of the product to which the ticket is associated|103000000638|
|Reply CC Emails|[]string|None|False|Email address added while replying to a ticket|["user@example.com"]|
|Requester|requester|None|False|Requester details|{}|
|Requester ID|integer|None|False|User ID of the requester|103021764889|
|Responder ID|integer|None|False|ID of the agent to whom the ticket has been assigned|103021764889|
|Source|string|None|False|The channel through which the ticket was created|Portal|
|Spam|boolean|None|False|Set to true if the ticket has been marked as spam|False|
|Stats|stats|None|False|Ticket stats|{}|
|Status|string|None|False|Status of the ticket|Open|
|Subject|string|None|False|Subject of the ticket|Example Subject|
|Tags|[]string|None|False|Tags that have been associated with the ticket|["my_tag", "second_tag"]|
|To Emails|[]string|None|False|Email addresses to which the ticket was originally sent|["user@example.com"]|
|Twitter ID|string|None|False|Twitter handle of the requester|123654789|
|Type|string|None|False|Helps categorize the ticket according to the different kinds of issues your support team deals with|Incident|
|Unique External ID|string|None|False|External ID of the requester|my_example_id|
|Updated At|date|None|False|Ticket updated timestamp|2023-12-21 12:56:15+05:00|
  
**ticketsFilter**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Company ID|integer|None|False|Company ID of the requester|103000179654|
|Requester Email|string|None|False|Email of the requester|user@example.com|
|Requester ID|integer|None|False|ID of the requester|54332121123|
|Requester Unique External ID|string|None|False|External ID of the requester|my_example_id|
|Updated Since|date|None|False|Tickets updated since specified date|2023-12-24 12:56:15+05:00|
  
**filteredTicket**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CC Emails|[]string|None|False|CC Emails|["clark.kent@kryptonspace.com"]|
|Company ID|integer|None|False|Company ID|2|
|Created At|string|None|False|Created At|2016-02-20T09:16:58Z|
|Custom Fields|object|None|False|Custom Fields|{"my_key": "my_value"}|
|Description|string|None|False|Description|<div>Sample description</div>|
|Description Text|string|None|False|Description Text|Sample description|
|Due By|string|None|False|Due By|2016-02-23T16:00:00Z|
|Email Config ID|integer|None|False|Email Configuration ID|17|
|FR Due By|string|None|False|First Response Due By|2016-02-22T17:00:00Z|
|FR Escalated|boolean|None|False|First Response Escalated|False|
|FWD Emails|[]string|None|False|Forwarded Emails|["clark.kent@kryptonspace.com"]|
|Group ID|integer|None|False|Group ID|156|
|ID|integer|None|False|ID|47|
|Is Escalated|boolean|None|False|Is Escalated|True|
|Priority|integer|None|False|Priority|3|
|Product ID|integer|None|False|Product ID|1|
|Reply CC Emails|[]string|None|False|Reply CC Emails|["clark.kent@kryptonspace.com"]|
|Requester ID|integer|None|False|Requester ID|6007738334|
|Responder ID|integer|None|False|Responder ID|6001263404|
|Source|integer|None|False|Source|2|
|Spam|boolean|None|False|Spam|False|
|Status|integer|None|False|Status|2|
|Subject|string|None|False|Subject|Sample Title|
|To Emails|[]string|None|False|To Emails|["clark.kent@kryptonspace.com"]|
|Type|string|None|False|Type|Incident|
|Updated At|string|None|False|Updated At|2016-02-23T16:14:57Z|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History
  
*This plugin does not contain a version history.*

# Links
  
*This plugin does not contain any links.*

## References
  
*This plugin does not contain any references.*