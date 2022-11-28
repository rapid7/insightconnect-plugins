# Description

Freshservice is a cloud-based IT Service Management solution that was designed using ITIL best practices. Freshservice helps IT organizations streamline their service delivery processes with a strong focus on user experience and employee happiness

# Key Features

* List groups
* List agents
* Create, update, delete and list tickets
* Create, update and delete ticket tasks

# Requirements

* FreshService API key

# Supported Product Versions

* FreshService API v2 2022-11-14

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|apiKey|credential_secret_key|None|True|FreshService API key|None|44d88612fea8a8f36de82e1278abb02f|
|subdomain|string|None|True|Subdomain from your FreshService URL, for example "example-company" from "https://example-company.freshservice.com"|None|example-company|

Example input:

```
{
  "apiKey": "44d88612fea8a8f36de82e1278abb02f",
  "subdomain": "example-company"
}
```

## Technical Details

### Actions

#### Update Ticket

This action is used to update an existing ticket in your service desk.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assets|[]assetInput|None|False|Assets that have to be associated with the ticket|None|{"displayId": 2}|
|attachments|[]attachmentInput|None|False|Ticket attachments. The total size of these attachments cannot exceed 15MB|None|[{"name": "test.txt", "content": "dGVzdA=="}]|
|category|string|None|False|Ticket category|None|Hardware|
|customFields|object|None|False|Key value pairs containing the names and values of custom fields|None|{"key": "value"}|
|departmentId|integer|None|False|Department ID of the requester|None|123456789|
|description|string|None|False|HTML content of the ticket|None|Example description|
|dueBy|date|None|False|Timestamp that denotes when the ticket is due to be resolved|None|2022-11-30T12:00:00Z|
|email|string|None|False|Email address of the requester. If no contact exists with this email address in FreshService, it will be added as a new contact|None|user@example.com|
|frDueBy|date|None|False|Timestamp that denotes when the first response is due|None|2022-11-30T12:00:00Z|
|groupId|integer|None|False|ID of the group to which the ticket has been assigned|None|123456789|
|impact|integer|1|False|Impact of the ticket|None|1|
|itemCategory|string|None|False|Ticket item category|None|PC|
|name|string|None|False|Name of the requester|None|Example Requester|
|phone|string|None|False|Phone number of the requester. If no contact exists with this phone number in FreshService, it will be added as a new contact. If the phone number is set and the email address is not, then the name attribute is mandatory|None|11111111|
|priority|integer|1|False|Priority of the ticket|None|1|
|requesterId|integer|None|False|ID of the requester|None|123456789|
|responderId|integer|None|False|ID of the agent to whom the ticket has been assigned|None|987654321|
|source|integer|None|False|The channel through which the ticket was created|None|2|
|status|integer|None|False|Status|None|2|
|subCategory|string|None|False|Ticket sub category|None|Computer|
|subject|string|None|False|Subject of the ticket|None|Example Subject|
|tags|[]string|None|False|Tags that have been associated with the ticket|None|["tag1", "tag2"]|
|ticketId|integer|None|True|ID of the ticket which will be updated|None|10|
|type|string|None|False|Type of the ticket|None|Incident|
|urgency|integer|1|False|Urgency|None|2|

Example input:

```
{
  "assets": {
    "displayId": 2
  },
  "attachments": [
    {
      "name": "test.txt",
      "content": "dGVzdA=="
    }
  ],
  "category": "Hardware",
  "customFields": {
    "key": "value"
  },
  "departmentId": 123456789,
  "description": "Example description",
  "dueBy": "2022-11-30T12:00:00Z",
  "email": "user@example.com",
  "frDueBy": "2022-11-30T12:00:00Z",
  "groupId": 123456789,
  "impact": 1,
  "itemCategory": "PC",
  "name": "Example Requester",
  "phone": 11111111,
  "priority": 1,
  "requesterId": 123456789,
  "responderId": 987654321,
  "source": 2,
  "status": 2,
  "subCategory": "Computer",
  "subject": "Example Subject",
  "tags": [
    "tag1",
    "tag2"
  ],
  "ticketId": 10,
  "type": "Incident",
  "urgency": 2
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket|ticket|False|Information about updated ticket|

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
    "frEscalated": false,
    "spam": false,
    "groupId": 123456789,
    "priority": 2,
    "requesterId": 123456789,
    "requestedForId": 123456789,
    "responderId": 987654321,
    "source": 2,
    "status": 2,
    "subject": "Example Subject",
    "departmentId": 123456789,
    "id": 10,
    "type": "Incident",
    "dueBy": "2022-12-20T12:00:00Z",
    "frDueBy": "2022-12-10T12:00:00Z",
    "isEscalated": false,
    "description": "<div>Example description</div>",
    "descriptionText": "Example description",
    "category": "Hardware",
    "subCategory": "Computer",
    "itemCategory": "PC",
    "customFields": {
      "key": "value"
    },
    "createdAt": "2022-11-24T17:31:33Z",
    "updatedAt": "2022-11-24T17:31:33Z",
    "tags": [
      "tag1",
      "tag2"
    ],
    "attachments": [
      {
        "id": 123,
        "contentType": "text/plain",
        "size": 4,
        "name": "test.txt",
        "attachmentUrl": "https://example.com",
        "createdAt": "2022-11-24T17:37:50Z",
        "updatedAt": "2022-11-24T17:37:50Z"
      }
    ],
    "assets": [
      {
        "name": "Dell Monitor",
        "ciTypeId": 1122334455,
        "impact": 1,
        "created": "2022-11-17T16:14:17Z",
        "updated": "2022-11-17T16:14:17Z",
        "authorId": 6677889900,
        "authorType": "User",
        "deleted": false,
        "displayId": 2
      }
    ]
  }
}
```

#### Create Ticket

This action is used to create a new ticket in your service desk.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assets|[]assetInput|None|False|Assets that have to be associated with the ticket|None|{"displayId": 2}|
|attachments|[]attachmentInput|None|False|Ticket attachments. The total size of these attachments cannot exceed 15MB|None|[{"name": "test.txt", "content": "dGVzdA=="}]|
|category|string|None|False|Ticket category|None|Hardware|
|ccEmails|[]string|None|False|Email addresses added in the 'cc' field of the incoming ticket email|None|["user@example.com"]|
|customFields|object|None|False|Key value pairs containing the names and values of custom fields|None|{"key": "value"}|
|departmentId|integer|None|False|Department ID of the requester|None|123456789|
|description|string|None|True|HTML content of the ticket|None|Example description|
|dueBy|date|None|False|Timestamp that denotes when the ticket is due to be resolved|None|2022-11-30T12:00:00Z|
|email|string|None|False|Email address of the requester. If no contact exists with this email address in FreshService, it will be added as a new contact|None|user@example.com|
|frDueBy|date|None|False|Timestamp that denotes when the first response is due|None|2022-11-30T12:00:00Z|
|groupId|integer|None|False|ID of the group to which the ticket has been assigned|None|123456789|
|impact|integer|1|False|Impact of the ticket|None|1|
|itemCategory|string|None|False|Ticket item category|None|PC|
|name|string|None|False|Name of the requester|None|Example Requester|
|phone|string|None|False|Phone number of the requester. If no contact exists with this phone number in FreshService, it will be added as a new contact. If the phone number is set and the email address is not, then the name attribute is mandatory|None|11111111|
|priority|integer|1|True|Priority of the ticket|None|1|
|requesterId|integer|None|False|ID of the requester|None|123456789|
|responderId|integer|None|False|ID of the agent to whom the ticket has been assigned|None|987654321|
|source|integer|None|False|The channel through which the ticket was created|None|2|
|status|integer|None|True|Status|None|2|
|subCategory|string|None|False|Ticket sub category|None|Computer|
|subject|string|None|True|Subject of the ticket|None|Example Subject|
|tags|[]string|None|False|Tags that have been associated with the ticket|None|["tag1", "tag2"]|
|type|string|None|False|Type of the ticket|None|Incident|
|urgency|integer|1|False|Urgency|None|2|

Example input:

```
{
  "assets": {
    "displayId": 2
  },
  "attachments": [
    {
      "name": "test.txt",
      "content": "dGVzdA=="
    }
  ],
  "category": "Hardware",
  "ccEmails": [
    "user@example.com"
  ],
  "customFields": {
    "key": "value"
  },
  "departmentId": 123456789,
  "description": "Example description",
  "dueBy": "2022-11-30T12:00:00Z",
  "email": "user@example.com",
  "frDueBy": "2022-11-30T12:00:00Z",
  "groupId": 123456789,
  "impact": 1,
  "itemCategory": "PC",
  "name": "Example Requester",
  "phone": 11111111,
  "priority": 1,
  "requesterId": 123456789,
  "responderId": 987654321,
  "source": 2,
  "status": 2,
  "subCategory": "Computer",
  "subject": "Example Subject",
  "tags": [
    "tag1",
    "tag2"
  ],
  "type": "Incident",
  "urgency": 2
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
    "ccEmails": [
      "user@example.com"
    ],
    "fwdEmails": [],
    "replyCcEmails": [
      "user@example.com"
    ],
    "frEscalated": false,
    "spam": false,
    "groupId": 123456789,
    "priority": 2,
    "requesterId": 123456789,
    "requestedForId": 123456789,
    "responderId": 987654321,
    "source": 2,
    "status": 2,
    "subject": "Example Subject",
    "departmentId": 123456789,
    "id": 10,
    "type": "Incident",
    "dueBy": "2022-12-20T12:00:00Z",
    "frDueBy": "2022-12-10T12:00:00Z",
    "isEscalated": false,
    "description": "<div>Example description</div>",
    "descriptionText": "Example description",
    "category": "Hardware",
    "subCategory": "Computer",
    "itemCategory": "PC",
    "customFields": {
      "key": "value"
    },
    "createdAt": "2022-11-24T17:31:33Z",
    "updatedAt": "2022-11-24T17:31:33Z",
    "tags": [
      "tag1",
      "tag2"
    ],
    "attachments": [
      {
        "id": 123,
        "contentType": "text/plain",
        "size": 4,
        "name": "test.txt",
        "attachmentUrl": "https://example.com",
        "createdAt": "2022-11-24T17:37:50Z",
        "updatedAt": "2022-11-24T17:37:50Z"
      }
    ],
    "assets": [
      {
        "name": "Dell Monitor",
        "ciTypeId": 1122334455,
        "impact": 1,
        "created": "2022-11-17T16:14:17Z",
        "updated": "2022-11-17T16:14:17Z",
        "authorId": 6677889900,
        "authorType": "User",
        "deleted": false,
        "displayId": 2
      }
    ]
  }
}
```

#### Delete Ticket

This action is used to delete the given ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ticketId|integer|None|True|ID of the ticket which will be deleted|None|20|

Example input:

```
{
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
  "success": True
}
```

#### Delete Ticket Task

This action is used to delete a task on a ticket request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|taskId|integer|None|True|ID of the task which will be deleted|None|10|
|ticketId|integer|None|True|ID of the ticket for which the task will be deleted|None|20|

Example input:

```
{
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
  "success": True
}
```

#### Update Ticket Task

This action is used to update an existing task on a ticket request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|False|Description of the task|None|Example description|
|dueDate|date|None|False|Due date of the task|None|2022-11-14T00:00:00Z|
|groupId|integer|None|False|Unique ID of the group to which the task will be  assigned|None|123456789|
|notifyBefore|integer|None|False|Time in seconds before which notification is sent prior to due date|None|3600|
|status|string|Open|False|Status of the task|['Open', 'In Progress', 'Completed']|Open|
|taskId|integer|None|True|ID of the task which will be updated|None|10|
|ticketId|integer|None|True|ID of the ticket for which the task will be updated|None|20|
|title|string|None|False|Title of the task|None|Task|

Example input:

```
{
  "description": "Example description",
  "dueDate": "2022-11-14T00:00:00Z",
  "groupId": 123456789,
  "notifyBefore": 3600,
  "status": "Open",
  "taskId": 10
  "ticketId": 20,
  "title": "Task"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|task|task|False|Information about the created task for the provided ticket|

Example output:

```
{
  "task": {
    "id": 10,
    "status": 1,
    "dueDate": "2022-12-14T00:00:00Z",
    "notifyBefore": 3600,
    "title": "Task",
    "description": "Example description",
    "createdAt": "2022-11-24T09:55:44Z",
    "updatedAt": "2022-11-24T09:55:44Z",
    "groupId": 123456789,
    "deleted": false
  }
}
```

#### Create Ticket Task

This action is used to create a new task on a ticket request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|False|Description of the task|None|Example description|
|dueDate|date|None|False|Due date of the task|None|2022-11-14T00:00:00Z|
|groupId|integer|None|False|Unique ID of the group to which the task will be  assigned|None|123456789|
|notifyBefore|integer|None|False|Time in seconds before which notification is sent prior to due date|None|3600|
|status|string|Open|False|Status of the task|['Open', 'In Progress', 'Completed']|Open|
|ticketId|integer|None|True|ID of the ticket for which the task will be created|None|20|
|title|string|None|True|Title of the task|None|Task|

Example input:

```
{
  "description": "Example description",
  "dueDate": "2022-11-14T00:00:00Z",
  "groupId": 123456789,
  "notifyBefore": 3600,
  "status": "Open",
  "taskId": 10
  "ticketId": 20,
  "title": "Task"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|task|task|False|Information about the created task for the provided ticket|

Example output:

```
{
  "task": {
    "id": 10,
    "status": 1,
    "dueDate": "2022-12-14T00:00:00Z",
    "notifyBefore": 3600,
    "title": "Task",
    "description": "Example description",
    "createdAt": "2022-11-24T09:55:44Z",
    "updatedAt": "2022-11-24T09:55:44Z",
    "groupId": 123456789,
    "deleted": false
  }
}
```

#### List Tickets

This action is used to list all tickets for the given filters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|False|Filter tickets by requester email|None|user@example.com|
|filter|string|None|False|Filter tickets using predefined filters. The filters available are new_and_my_open, watching, spam, deleted|None|watching|
|orderType|string|desc|False|Type of the order|['asc', 'desc']|desc|
|page|integer|None|False|The number of the results page to be returned|None|1|
|perPage|integer|20|False|The number of results per page|None|20|
|requesterId|integer|None|False|Filter tickets by requester ID|None|123456789|
|type|string|All|False|Filter tickets by type|['Incident', 'Service Request', 'All']|All|
|updatedSince|date|None|False|Filter tickets by update date|None|2022-11-14T00:00:00Z|

Example input:

```
{
  "email": "user@example.com",
  "filter": "watching",
  "orderType": "desc",
  "page": 1,
  "perPage": 20,
  "requesterId": 123456789,
  "type": "All",
  "updatedSince": "2022-11-14T00:00:00Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tickets|[]ticket|False|Information about all tickets obtained using the given filters|

Example output:

```
{
  "tickets": [
    {
      "subject": "Example Ticket",
      "groupId": 123456789,
      "departmentId": 987654321,
      "category": "Hardware",
      "subCategory": "Computer",
      "itemCategory": "PC",
      "requesterId": 123456789,
      "responderId": 987654321,
      "dueBy": "2022-12-20T12:00:00Z",
      "frEscalated": false,
      "deleted": false,
      "spam": false,
      "fwdEmails": [],
      "replyCcEmails": [],
      "ccEmails": [],
      "isEscalated": false,
      "frDueBy": "2022-12-15T12:00:00Z",
      "id": 16,
      "priority": 2,
      "status": 2,
      "source": 4,
      "createdAt": "2022-11-10T00:00:00Z",
      "updatedAt": "2022-11-16T00:00:00Z",
      "requestedForId": 123456789,
      "type": "Incident",
      "description": "Example description",
      "descriptionText": "Example description",
      "customFields": {
        "key": "value"
      }
    }
  ]
}
```

#### List All Agents

This action is used to view information about all agents in the account. Use filters to view only specific agents (those who match the criteria that you choose).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|active|string|all|False|Return active, deactivated or all agents|['true', 'false', 'all']|all|
|email|string|None|False|Email address of the agent based on which the results will be filtered|None|user@example.com|
|mobilePhoneNumber|string|None|False|Mobile phone number of the agent based on which the results will be filtered|None|664345|
|state|string|all|False|Return fulltime, occasional or all agents|['fulltime', 'occasional', 'all']|all|
|workPhoneNumber|string|None|False|Work phone number of the agent based on which the results will be filtered|None|5564435|

Example input:

```
{
  "active": "all",
  "email": "user@example.com",
  "mobilePhoneNumber": "664345",
  "state": "all",
  "workPhoneNumber": "5564435"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents|[]agent|False|Information about agents in the account|

Example output:

```
{
  "agents": [
    {
      "active": true,
      "autoAssignTickets": true,
      "canSeeAllTicketsFromAssociatedDepartments": false,
      "createdAt": "2022-11-17T16:13:30Z",
      "customFields": {},
      "departmentIds": [],
      "email": "user@example.com",
      "firstName": "User",
      "hasLoggedIn": false,
      "id": 1234567890,
      "language": "en",
      "mobilePhoneNumber": 664345,
      "occasional": false,
      "roleIds": [
        987654321
      ],
      "roles": [
        {
          "roleId": 987654321,
          "assignmentScope": "entire_helpdesk",
          "groups": []
        }
      ],
      "scopes": {},
      "timeFormat": "12h",
      "timeZone": "Eastern Time (US & Canada)",
      "updatedAt": "2022-11-17T16:13:30Z",
      "vipUser": false,
      "workPhoneNumber": "5564435",
      "groupIds": [],
      "memberOf": [],
      "observerOf": [],
      "memberOfPendingApproval": [],
      "observerOfPendingApproval": []
    }
  ]
}
```

#### List All Groups

This action is used to view information about all groups in the account.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|groups|[]group|False|Information about all groups in the account|

Example output:

```
{
  "groups": [
    {
      "id": 1234567890,
      "name": "Incident Team",
      "description": "Incident Management Team",
      "createdAt": "2022-11-17T16:13:29Z",
      "updatedAt": "2022-11-17T16:13:29Z",
      "autoTicketAssign": false,
      "restricted": false,
      "approvalRequired": false,
      "agentIds": [],
      "members": [],
      "observers": [],
      "leaders": [],
      "membersPendingApproval": [],
      "leadersPendingApproval": [],
      "observersPendingApproval": []
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### agent

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Active|boolean|False|True if the agent is active, false if the agent has been deactivated|
|Address|string|False|Address of the agent|
|Background Information|string|False|Background information of the agent|
|Can See All Tickets from Associated Departments|boolean|False|Set to true if the agent must be allowed to view tickets filed by other members of the department, and false otherwise|
|Created At|string|False|Date and time when the agent was created|
|Custom Fields|object|False|Key-value pair containing the names and values of the (custom) agent fields|
|Department IDs|[]string|False|Unique IDs of the departments associated with the agent|
|Email|string|False|Email address of the agent|
|First Name|string|False|First name of the agent|
|Has Logged In|boolean|False|Set to true if the user has logged in to FreshService at least once, and false otherwise|
|ID|integer|False|User ID of the agent|
|Job Title|string|False|Job title of the agent|
|Language|string|False|Language used by the agent|
|Last Active At|string|False|Timestamp of the agent's recent activity|
|Last Login At|string|False|Timestamp of the agent's last successful login|
|Last Name|string|False|Last name of the agent|
|Location ID|integer|False|Unique ID of the location associated with the agent|
|Member Of|[]integer|False|Unique IDs of the groups that the agent is a member of|
|Member Of Pending Approval|[]integer|False|Unique IDs of the restricted groups to which the agent's addition as a member is pending approval|
|Mobile Phone Number|string|False|Mobile phone number of the agent|
|Observer Of|[]integer|False|Unique IDs of the groups that the agent is an observer of|
|Observer Of Pending Approval|[]integer|False|Unique IDs of the restricted groups to which the agent's addition as an observer is pending approval|
|Occasional|boolean|False|True if the agent is an occasional agent, and false if full-time agent|
|Reporting Manager ID|integer|False|User ID of the agent's reporting manager|
|Roles|[]role|False|Roles that are granted to the agent|
|Scopes|scope|False|Scopes of the agent|
|Scoreboard Level ID|integer|False|Unique ID of the level of the agent in the Arcade|
|Ticket Scope|string|False|Ticket scope of the agent|
|Time Format|string|False|Time format for the agent|
|Time Zone|string|False|Time zone of the agent|
|Updated At|string|False|Date and time when the agent was last updated|
|Work Phone Number|string|False|Work phone number of the agent|

#### asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent ID|integer|False|ID of the agent|
|Assigned On|string|False|Assigned on|
|Author ID|integer|False|ID of the author|
|Author Type|string|False|Type of the author|
|CI Type ID|integer|False|ID of the configuration item type|
|Created|string|False|Date and time when the asset was created|
|Deleted|boolean|False|Whether the asset has been deleted|
|Department ID|integer|False|ID of the department|
|Description|string|False|Description of the asset|
|Display ID|integer|False|Display ID of the asset|
|Impact|integer|False|Impact|
|Name|string|False|Name of the asset|
|Updated|string|False|Date and time when the asset was updated|
|User ID|integer|False|ID of the user|

#### assetInput

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Display ID|integer|False|Display ID of the asset|

#### attachment

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attachment URL|string|False|Attachment URL|
|Content Type|string|False|Content type of the attachment|
|Created At|string|False|Date and time when the attachment was created|
|ID|integer|False|ID of the attachment|
|Name|string|False|Size of the attachment|
|Size|integer|False|Size of the attachment|

#### attachmentInput

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Content|bytes|False|Base64 encoded content of the attachment|
|Name|string|False|Name of the attachment|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent IDs|[]integer|False|List of agent user IDs separated by commas|
|Approval Required|boolean|False|Whether the restricted group requires approvals for membership changes|
|Auto Ticket Assign|boolean|False|Describes the automatic ticket assignment type|
|Business Hours ID|integer|False|Unique ID of the business hours configuration associated with the group|
|Created At|string|False|Date and time when the agent group was created|
|Description|string|False|Description of the group|
|Escalate To|integer|False|The Unique ID of the user to whom an escalation email is sent if a ticket in this group is unassigned|
|ID|integer|False|ID of the group|
|Leaders|[]integer|False|A comma separated list of user IDs of agents who are leaders of this group|
|Leaders Pending Approval|[]integer|False|A comma-separated list of user IDs of agents whose leader access to the group is pending approval by an existing group leader|
|Members|[]integer|False|A comma separated list of user IDs of agents who are members of this group|
|Members Pending Approval|[]integer|False|A comma-separated list of user IDs of agents whose member access to the group is pending approval by a group leader|
|Name|string|False|Name of the group|
|Observers|[]integer|False|A comma separated list of user IDs of agents who are observers of this group|
|Observers Pending Approval|[]integer|False|A comma-separated list of user IDs of agents whose observer access to the group is pending approval by a group leader|
|Restricted|boolean|False|Whether a group is marked as restricted|
|Unassigned For|string|False|The time after which an escalation email is sent if a ticket in the group remains unassigned|
|Updated At|string|False|Date and time when the agent group was last updated|

#### role

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assignment Scope|string|False|The scope in which the agent can use the permissions granted by this role|
|Groups|[]integer|False|Unique IDs of Groups in which the permissions granted by the role applies|
|Role ID|integer|False|Unique ID of the role assigned|

#### scope

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Asset|string|False|Asset scope of the agent|
|Change|string|False|Change scope of the agent|
|Contract|string|False|Contract scope of the agent|
|Problem|string|False|Problem scope of the agent|
|Release|string|False|Release scope of the agent|
|Solution|string|False|Solution scope of the agent|
|Ticket|string|False|Ticket scope of the agent|

#### task

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent ID|integer|False|ID of the agent to whom the task is assigned|
|Closed AT|string|False|Timestamp at which the task was closed|
|Created At|string|False|Timestamp at which the task was created|
|Description|string|False|Description of the task|
|Due Date|string|False|Due date of the task|
|Group ID|integer|False|Unique ID of the group to which the task is assigned|
|ID|integer|False|Unique ID of the task|
|Notify Before|integer|False|Time in seconds before which notification is sent prior to due date|
|Status|integer|False|Status of the task|
|Title|string|False|Title of the task|
|Updated At|string|False|Timestamp at which the task was updated|

#### ticket

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assets|[]asset|False|Assets associated with the ticket|
|Attachments|[]attachment|False|Ticket attachments|
|Category|string|False|Ticket category|
|CC Emails|[]string|False|Email addresses added in the 'cc' field of the incoming ticket email|
|Created At|string|False|Ticket creation timestamp|
|Custom Fields|object|False|Key value pairs containing the names and values of custom fields|
|Deleted|boolean|False|Whether the ticket has been deleted|
|Department ID|integer|False|ID of the department to which this ticket belongs|
|Description|string|False|HTML content of the ticket|
|Description Text|string|False|Content of the ticket in plain text|
|Due By|string|False|Timestamp that denotes when the ticket is due to be resolved|
|Email|string|False|Email address of the requester|
|Email Config ID|integer|False|ID of email config which is used for this ticket|
|First Response Due By|string|False|Timestamp that denotes when the first response is due|
|First Response Escalated|boolean|False|Set to true if the ticket has been escalated as a result of the first response time being breached|
|Fwd Emails|[]string|False|Email addresses added while forwarding a ticket|
|Group ID|integer|False|ID of the group to which the ticket has been assigned|
|ID|integer|False|Unique ID of the ticket|
|Impact|integer|False|Impact|
|Is Escalated|boolean|False|Set to true if the ticket has been escalated for any reason|
|Item Category|string|False|Ticket item category|
|Name|string|False|Name of the requester|
|Phone|string|False|Phone number of the requester|
|Priority|integer|False|Priority of the ticket|
|Reply CC Emails|[]string|False|Email addresses added while replying to a ticket|
|Requester ID|integer|False|User ID of the requester|
|Responder ID|integer|False|ID of the agent to whom the ticket has been assigned|
|Source|integer|False|The channel through which the ticket was created|
|Spam|boolean|False|Set to true if the ticket has been marked as spam|
|Status|integer|False|Status of the ticket|
|Sub Category|string|False|Ticket sub category|
|Subject|string|False|Subject of the ticket|
|Tags|[]string|False|Tags that have been associated with the ticket|
|To Emails|[]string|False|Email addresses to which the ticket was originally sent|
|Type|string|False|Type of the ticket|
|Updated At|string|False|Ticket updated timestamp|
|Urgency|integer|False|Ticket urgency|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin | Add Create Ticket, Update Ticket, Delete Ticket, List Tickets, Create Ticket Task, Update Ticket Task, Delete Ticket Task, List Groups and List Agents actions

# Links

## References

* [FreshService](https://freshservice.com)

