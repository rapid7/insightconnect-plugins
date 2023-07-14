# Description
  
Freshservice is a cloud-based IT Service Management solution that was designed using ITIL best practices. Freshservice 
helps IT organizations streamline their service delivery processes with a strong focus on user experience and employee 
happiness
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
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

#### Create Ticket
Create a new ticket in your service desk
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assets|[]assetInput|None|False|Assets that have to be associated with the ticket|None|{"displayId": 2}|
|attachments|[]attachmentInput|None|False|Ticket attachments. The total size of these attachments cannot exceed 15MB|None|[{"name": "test.txt", "content": "dGVzdA=="}]|
|category|string|None|False|Ticket category|None|Hardware|
|ccEmails|[]string|None|False|Email addresses added in the 'cc' field of the incoming ticket email|None|["user@example.com"]|
|customFields|object|None|False|Key value pairs containing the names and values of custom fields|None|{"key": "value"}|
|departmentId|integer|None|False|Department ID of the requester|None|123456789|
|description|string|None|True|HTML content of the ticket|None|Example description|
|dueBy|date|None|False|Timestamp that denotes when the ticket is due to be resolved|None|2022-11-30 12:00:00+00:00|
|email|string|None|False|Email address of the requester. If no contact exists with this email address in FreshService, it will be added as a new contact|None|user@example.com|
|frDueBy|date|None|False|Timestamp that denotes when the first response is due|None|2022-11-30 12:00:00+00:00|
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
      "content": "dGVzdA==",
      "name": "test.txt"
    }
  ],
  "category": "Hardware",
  "ccEmails": "user@example.com",
  "customFields": {
    "key": "value"
  },
  "departmentId": 123456789,
  "description": "Example description",
  "dueBy": "2022-11-30 12:00:00+00:00",
  "email": "user@example.com",
  "frDueBy": "2022-11-30 12:00:00+00:00",
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
  "tags": "tag1",
  "type": "Incident",
  "urgency": 1
}
```
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|None|False|Information about created ticket|None|None|
  
Example output:

```
{
  "ticket": {
    "Assets": [
      {
        "Agent ID": {},
        "Assigned On": {},
        "Author ID": {},
        "Author Type": {},
        "CI Type ID": 0,
        "Created": {},
        "Deleted": "true",
        "Department ID": {},
        "Description": {},
        "Display ID": {},
        "Impact": {},
        "Name": "",
        "Updated": {},
        "User ID": {}
      }
    ],
    "Attachments": [
      {
        "Attachment URL": {},
        "Content Type": {},
        "Created At": {},
        "ID": {},
        "Name": {},
        "Size": {}
      }
    ],
    "CC Emails": [
      {}
    ],
    "Category": {},
    "Created At": {},
    "Custom Fields": {},
    "Deleted": {},
    "Department ID": {},
    "Description": {},
    "Description Text": {},
    "Due By": {},
    "Email": {},
    "Email Config ID": {},
    "First Response Due By": {},
    "First Response Escalated": {},
    "Fwd Emails": {},
    "Group ID": {},
    "ID": {},
    "Impact": {},
    "Is Escalated": {},
    "Item Category": {},
    "Name": {},
    "Phone": {},
    "Priority": {},
    "Reply CC Emails": {},
    "Requester ID": {},
    "Responder ID": {},
    "Source": {},
    "Spam": {},
    "Status": {},
    "Sub Category": {},
    "Subject": {},
    "Tags": {},
    "To Emails": {},
    "Type": {},
    "Updated At": {},
    "Urgency": {}
  }
}
```
#### Create Ticket Task
Create a new task on a ticket request
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Description of the task|None|Example description|
|dueDate|date|None|False|Due date of the task|None|2022-11-14 00:00:00+00:00|
|groupId|integer|None|False|Unique ID of the group to which the task will be  assigned|None|123456789|
|notifyBefore|integer|None|False|Time in seconds before which notification is sent prior to due date|None|3600|
|status|string|Open|False|Status of the task|['Open', 'In Progress', 'Completed']|Open|
|ticketId|integer|None|True|ID of the ticket for which the task will be created|None|20|
|title|string|None|True|Title of the task|None|Task|
  
Example input:

```
{
  "description": "Example description",
  "dueDate": "2022-11-14 00:00:00+00:00",
  "groupId": 123456789,
  "notifyBefore": 3600,
  "status": "Open",
  "ticketId": 20,
  "title": "Task"
}
```
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task|task|None|False|Information about the created task for the provided ticket|None|None|
  
Example output:

```
{
  "task": {
    "Agent ID": {},
    "Closed AT": {},
    "Created At": {},
    "Description": {},
    "Due Date": "",
    "Group ID": {},
    "ID": 0,
    "Notify Before": {},
    "Status": {},
    "Title": {},
    "Updated At": {}
  }
}
```
#### Delete Ticket
Delete the given ticket
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ticketId|integer|None|True|ID of the ticket which will be deleted|None|20|
  
Example input:

```
{
  "ticketId": 20
}
```
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|success|boolean|None|True|Whether the action was successful|None|None|
  
Example output:

```
{
  "success": true
}
```
#### Delete Ticket Task
Delete a task on a ticket request
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|taskId|integer|None|True|ID of the task which will be deleted|None|10|
|ticketId|integer|None|True|ID of the ticket for which the task will be deleted|None|20|
  
Example input:

```
{
  "taskId": 10,
  "ticketId": 20
}
```
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|success|boolean|None|True|Whether the action was successful|None|None|
  
Example output:

```
{
  "success": true
}
```
#### List All Agents
View information about all agents in the account. Use filters to view only specific agents (those who match the criteria
 that you choose)
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
  "mobilePhoneNumber": 664345,
  "state": "all",
  "workPhoneNumber": 5564435
}
```
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agents|[]agent|None|False|Information about agents in the account|None|None|
  
Example output:

```
{
  "agents": [
    {
      "Active": {},
      "Address": {},
      "Background Information": {},
      "Can See All Tickets from Associated Departments": {},
      "Created At": {},
      "Custom Fields": {},
      "Department IDs": [
        {}
      ],
      "Email": {},
      "First Name": "",
      "Has Logged In": {},
      "ID": 0,
      "Job Title": {},
      "Language": {},
      "Last Active At": {},
      "Last Login At": {},
      "Last Name": {},
      "Location ID": {},
      "Member Of": [
        {}
      ],
      "Member Of Pending Approval": {},
      "Mobile Phone Number": {},
      "Observer Of": {},
      "Observer Of Pending Approval": {},
      "Occasional": "true",
      "Reporting Manager ID": {},
      "Roles": [
        {
          "Assignment Scope": {},
          "Groups": {},
          "Role ID": {}
        }
      ],
      "Scopes": {
        "Asset": {},
        "Change": {},
        "Contract": {},
        "Problem": {},
        "Release": {},
        "Solution": {},
        "Ticket": {}
      },
      "Scoreboard Level ID": {},
      "Ticket Scope": {},
      "Time Format": {},
      "Time Zone": {},
      "Updated At": {},
      "Work Phone Number": {}
    }
  ]
}
```
#### List All Groups
View information about all groups in the account
##### Input
  
*This action does not contain any inputs.*
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|groups|[]group|None|False|Information about all groups in the account|None|None|
  
Example output:

```
{
  "groups": [
    {
      "Agent IDs": [
        {}
      ],
      "Approval Required": {},
      "Auto Ticket Assign": {},
      "Business Hours ID": {},
      "Created At": {},
      "Description": {},
      "Escalate To": {},
      "ID": 0,
      "Leaders": {},
      "Leaders Pending Approval": {},
      "Members": {},
      "Members Pending Approval": {},
      "Name": "",
      "Observers": {},
      "Observers Pending Approval": {},
      "Restricted": "true",
      "Unassigned For": {},
      "Updated At": {}
    }
  ]
}
```
#### List Tickets
List all tickets for the given filters
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|False|Filter tickets by requester email|None|user@example.com|
|filter|string|None|False|Filter tickets using predefined filters. The filters available are new_and_my_open, watching, spam, deleted|None|watching|
|orderType|string|desc|False|Type of the order|['asc', 'desc']|desc|
|page|integer|None|False|The number of the results page to be returned|None|1|
|perPage|integer|20|False|The number of results per page|None|20|
|requesterId|integer|None|False|Filter tickets by requester ID|None|123456789|
|type|string|All|False|Filter tickets by type|['Incident', 'Service Request', 'All']|All|
|updatedSince|date|None|False|Filter tickets by update date|None|2022-11-14 00:00:00+00:00|
  
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
  "updatedSince": "2022-11-14 00:00:00+00:00"
}
```
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|tickets|[]ticket|None|False|Information about all tickets obtained using the given filters|None|None|
  
Example output:

```
{
  "tickets": [
    {
      "Assets": [
        {
          "Agent ID": {},
          "Assigned On": {},
          "Author ID": {},
          "Author Type": {},
          "CI Type ID": 0,
          "Created": {},
          "Deleted": "true",
          "Department ID": {},
          "Description": {},
          "Display ID": {},
          "Impact": {},
          "Name": "",
          "Updated": {},
          "User ID": {}
        }
      ],
      "Attachments": [
        {
          "Attachment URL": {},
          "Content Type": {},
          "Created At": {},
          "ID": {},
          "Name": {},
          "Size": {}
        }
      ],
      "CC Emails": [
        {}
      ],
      "Category": {},
      "Created At": {},
      "Custom Fields": {},
      "Deleted": {},
      "Department ID": {},
      "Description": {},
      "Description Text": {},
      "Due By": {},
      "Email": {},
      "Email Config ID": {},
      "First Response Due By": {},
      "First Response Escalated": {},
      "Fwd Emails": {},
      "Group ID": {},
      "ID": {},
      "Impact": {},
      "Is Escalated": {},
      "Item Category": {},
      "Name": {},
      "Phone": {},
      "Priority": {},
      "Reply CC Emails": {},
      "Requester ID": {},
      "Responder ID": {},
      "Source": {},
      "Spam": {},
      "Status": {},
      "Sub Category": {},
      "Subject": {},
      "Tags": {},
      "To Emails": {},
      "Type": {},
      "Updated At": {},
      "Urgency": {}
    }
  ]
}
```
#### Update Ticket
Update an existing ticket in your service desk
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assets|[]assetInput|None|False|Assets that have to be associated with the ticket|None|{"displayId": 2}|
|attachments|[]attachmentInput|None|False|Ticket attachments. The total size of these attachments cannot exceed 15MB|None|[{"name": "test.txt", "content": "dGVzdA=="}]|
|category|string|None|False|Ticket category|None|Hardware|
|customFields|object|None|False|Key value pairs containing the names and values of custom fields|None|{"key": "value"}|
|departmentId|integer|None|False|Department ID of the requester|None|123456789|
|description|string|None|False|HTML content of the ticket|None|Example description|
|dueBy|date|None|False|Timestamp that denotes when the ticket is due to be resolved|None|2022-11-30 12:00:00+00:00|
|email|string|None|False|Email address of the requester. If no contact exists with this email address in FreshService, it will be added as a new contact|None|user@example.com|
|frDueBy|date|None|False|Timestamp that denotes when the first response is due|None|2022-11-30 12:00:00+00:00|
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
|tags|[]string|None|False|Tags that have been associated with the ticket|None|['tag1', 'tag2']|
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
      "content": "dGVzdA==",
      "name": "test.txt"
    }
  ],
  "category": "Hardware",
  "customFields": {
    "key": "value"
  },
  "departmentId": 123456789,
  "description": "Example description",
  "dueBy": "2022-11-30 12:00:00+00:00",
  "email": "user@example.com",
  "frDueBy": "2022-11-30 12:00:00+00:00",
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
  "tags": "tag1",
  "ticketId": 10,
  "type": "Incident",
  "urgency": 1
}
```
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ticket|ticket|None|False|Information about updated ticket|None|None|
  
Example output:

```
{
  "ticket": {
    "Assets": [
      {
        "Agent ID": {},
        "Assigned On": {},
        "Author ID": {},
        "Author Type": {},
        "CI Type ID": 0,
        "Created": {},
        "Deleted": "true",
        "Department ID": {},
        "Description": {},
        "Display ID": {},
        "Impact": {},
        "Name": "",
        "Updated": {},
        "User ID": {}
      }
    ],
    "Attachments": [
      {
        "Attachment URL": {},
        "Content Type": {},
        "Created At": {},
        "ID": {},
        "Name": {},
        "Size": {}
      }
    ],
    "CC Emails": [
      {}
    ],
    "Category": {},
    "Created At": {},
    "Custom Fields": {},
    "Deleted": {},
    "Department ID": {},
    "Description": {},
    "Description Text": {},
    "Due By": {},
    "Email": {},
    "Email Config ID": {},
    "First Response Due By": {},
    "First Response Escalated": {},
    "Fwd Emails": {},
    "Group ID": {},
    "ID": {},
    "Impact": {},
    "Is Escalated": {},
    "Item Category": {},
    "Name": {},
    "Phone": {},
    "Priority": {},
    "Reply CC Emails": {},
    "Requester ID": {},
    "Responder ID": {},
    "Source": {},
    "Spam": {},
    "Status": {},
    "Sub Category": {},
    "Subject": {},
    "Tags": {},
    "To Emails": {},
    "Type": {},
    "Updated At": {},
    "Urgency": {}
  }
}
```
#### Update Ticket Task
Update an existing task on a ticket request
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Description of the task|None|Example description|
|dueDate|date|None|False|Due date of the task|None|2022-11-14 00:00:00+00:00|
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
  "dueDate": "2022-11-14 00:00:00+00:00",
  "groupId": 123456789,
  "notifyBefore": 3600,
  "status": "Open",
  "taskId": 10,
  "ticketId": 20,
  "title": "Task"
}
```
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task|task|None|False|Information about the created task for the provided ticket|None|None|
  
Example output:

```
{
  "task": {
    "Agent ID": {},
    "Closed AT": {},
    "Created At": {},
    "Description": {},
    "Due Date": "",
    "Group ID": {},
    "ID": 0,
    "Notify Before": {},
    "Status": {},
    "Title": {},
    "Updated At": {}
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*
### Custom Types
  
**role**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assignment Scope|string|None|False|The scope in which the agent can use the permissions granted by this role|None|
|Groups|[]integer|None|False|Unique IDs of Groups in which the permissions granted by the role applies|None|
|Role ID|integer|None|False|Unique ID of the role assigned|None|
  
**scope**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Asset|string|None|False|Asset scope of the agent|None|
|Change|string|None|False|Change scope of the agent|None|
|Contract|string|None|False|Contract scope of the agent|None|
|Problem|string|None|False|Problem scope of the agent|None|
|Release|string|None|False|Release scope of the agent|None|
|Solution|string|None|False|Solution scope of the agent|None|
|Ticket|string|None|False|Ticket scope of the agent|None|
  
**agent**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active|boolean|None|False|True if the agent is active, false if the agent has been deactivated|None|
|Address|string|None|False|Address of the agent|None|
|Background Information|string|None|False|Background information of the agent|None|
|Can See All Tickets from Associated Departments|boolean|None|False|Set to true if the agent must be allowed to view tickets filed by other members of the department, and false otherwise|None|
|Created At|string|None|False|Date and time when the agent was created|None|
|Custom Fields|object|None|False|Key-value pair containing the names and values of the (custom) agent fields|None|
|Department IDs|[]string|None|False|Unique IDs of the departments associated with the agent|None|
|Email|string|None|False|Email address of the agent|None|
|First Name|string|None|False|First name of the agent|None|
|Has Logged In|boolean|None|False|Set to true if the user has logged in to FreshService at least once, and false otherwise|None|
|ID|integer|None|False|User ID of the agent|None|
|Job Title|string|None|False|Job title of the agent|None|
|Language|string|None|False|Language used by the agent|None|
|Last Active At|string|None|False|Timestamp of the agent's recent activity|None|
|Last Login At|string|None|False|Timestamp of the agent's last successful login|None|
|Last Name|string|None|False|Last name of the agent|None|
|Location ID|integer|None|False|Unique ID of the location associated with the agent|None|
|Member Of|[]integer|None|False|Unique IDs of the groups that the agent is a member of|None|
|Member Of Pending Approval|[]integer|None|False|Unique IDs of the restricted groups to which the agent's addition as a member is pending approval|None|
|Mobile Phone Number|string|None|False|Mobile phone number of the agent|None|
|Observer Of|[]integer|None|False|Unique IDs of the groups that the agent is an observer of|None|
|Observer Of Pending Approval|[]integer|None|False|Unique IDs of the restricted groups to which the agent's addition as an observer is pending approval|None|
|Occasional|boolean|None|False|True if the agent is an occasional agent, and false if full-time agent|None|
|Reporting Manager ID|integer|None|False|User ID of the agent's reporting manager|None|
|Roles|[]role|None|False|Roles that are granted to the agent|None|
|Scopes|scope|None|False|Scopes of the agent|None|
|Scoreboard Level ID|integer|None|False|Unique ID of the level of the agent in the Arcade|None|
|Ticket Scope|string|None|False|Ticket scope of the agent|None|
|Time Format|string|None|False|Time format for the agent|None|
|Time Zone|string|None|False|Time zone of the agent|None|
|Updated At|string|None|False|Date and time when the agent was last updated|None|
|Work Phone Number|string|None|False|Work phone number of the agent|None|
  
**asset**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent ID|integer|None|False|ID of the agent|None|
|Assigned On|string|None|False|Assigned on|None|
|Author ID|integer|None|False|ID of the author|None|
|Author Type|string|None|False|Type of the author|None|
|CI Type ID|integer|None|False|ID of the configuration item type|None|
|Created|string|None|False|Date and time when the asset was created|None|
|Deleted|boolean|None|False|Whether the asset has been deleted|None|
|Department ID|integer|None|False|ID of the department|None|
|Description|string|None|False|Description of the asset|None|
|Display ID|integer|None|False|Display ID of the asset|None|
|Impact|integer|None|False|Impact|None|
|Name|string|None|False|Name of the asset|None|
|Updated|string|None|False|Date and time when the asset was updated|None|
|User ID|integer|None|False|ID of the user|None|
  
**assetInput**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Display ID|integer|None|False|Display ID of the asset|None|
  
**attachment**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attachment URL|string|None|False|Attachment URL|None|
|Content Type|string|None|False|Content type of the attachment|None|
|Created At|string|None|False|Date and time when the attachment was created|None|
|ID|integer|None|False|ID of the attachment|None|
|Name|string|None|False|Size of the attachment|None|
|Size|integer|None|False|Size of the attachment|None|
  
**attachmentInput**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content|bytes|None|False|Base64 encoded content of the attachment|None|
|Name|string|None|False|Name of the attachment|None|
  
**group**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent IDs|[]integer|None|False|List of agent user IDs separated by commas|None|
|Approval Required|boolean|None|False|Whether the restricted group requires approvals for membership changes|None|
|Auto Ticket Assign|boolean|None|False|Describes the automatic ticket assignment type|None|
|Business Hours ID|integer|None|False|Unique ID of the business hours configuration associated with the group|None|
|Created At|string|None|False|Date and time when the agent group was created|None|
|Description|string|None|False|Description of the group|None|
|Escalate To|integer|None|False|The Unique ID of the user to whom an escalation email is sent if a ticket in this group is unassigned|None|
|ID|integer|None|False|ID of the group|None|
|Leaders|[]integer|None|False|A comma separated list of user IDs of agents who are leaders of this group|None|
|Leaders Pending Approval|[]integer|None|False|A comma-separated list of user IDs of agents whose leader access to the group is pending approval by an existing group leader|None|
|Members|[]integer|None|False|A comma separated list of user IDs of agents who are members of this group|None|
|Members Pending Approval|[]integer|None|False|A comma-separated list of user IDs of agents whose member access to the group is pending approval by a group leader|None|
|Name|string|None|False|Name of the group|None|
|Observers|[]integer|None|False|A comma separated list of user IDs of agents who are observers of this group|None|
|Observers Pending Approval|[]integer|None|False|A comma-separated list of user IDs of agents whose observer access to the group is pending approval by a group leader|None|
|Restricted|boolean|None|False|Whether a group is marked as restricted|None|
|Unassigned For|string|None|False|The time after which an escalation email is sent if a ticket in the group remains unassigned|None|
|Updated At|string|None|False|Date and time when the agent group was last updated|None|
  
**task**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent ID|integer|None|False|ID of the agent to whom the task is assigned|None|
|Closed AT|string|None|False|Timestamp at which the task was closed|None|
|Created At|string|None|False|Timestamp at which the task was created|None|
|Description|string|None|False|Description of the task|None|
|Due Date|string|None|False|Due date of the task|None|
|Group ID|integer|None|False|Unique ID of the group to which the task is assigned|None|
|ID|integer|None|False|Unique ID of the task|None|
|Notify Before|integer|None|False|Time in seconds before which notification is sent prior to due date|None|
|Status|integer|None|False|Status of the task|None|
|Title|string|None|False|Title of the task|None|
|Updated At|string|None|False|Timestamp at which the task was updated|None|
  
**ticket**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assets|[]asset|None|False|Assets associated with the ticket|None|
|Attachments|[]attachment|None|False|Ticket attachments|None|
|Category|string|None|False|Ticket category|None|
|CC Emails|[]string|None|False|Email addresses added in the 'cc' field of the incoming ticket email|None|
|Created At|string|None|False|Ticket creation timestamp|None|
|Custom Fields|object|None|False|Key value pairs containing the names and values of custom fields|None|
|Deleted|boolean|None|False|Whether the ticket has been deleted|None|
|Department ID|integer|None|False|ID of the department to which this ticket belongs|None|
|Description|string|None|False|HTML content of the ticket|None|
|Description Text|string|None|False|Content of the ticket in plain text|None|
|Due By|string|None|False|Timestamp that denotes when the ticket is due to be resolved|None|
|Email|string|None|False|Email address of the requester|None|
|Email Config ID|integer|None|False|ID of email config which is used for this ticket|None|
|First Response Due By|string|None|False|Timestamp that denotes when the first response is due|None|
|First Response Escalated|boolean|None|False|Set to true if the ticket has been escalated as a result of the first response time being breached|None|
|Fwd Emails|[]string|None|False|Email addresses added while forwarding a ticket|None|
|Group ID|integer|None|False|ID of the group to which the ticket has been assigned|None|
|ID|integer|None|False|Unique ID of the ticket|None|
|Impact|integer|None|False|Impact|None|
|Is Escalated|boolean|None|False|Set to true if the ticket has been escalated for any reason|None|
|Item Category|string|None|False|Ticket item category|None|
|Name|string|None|False|Name of the requester|None|
|Phone|string|None|False|Phone number of the requester|None|
|Priority|integer|None|False|Priority of the ticket|None|
|Reply CC Emails|[]string|None|False|Email addresses added while replying to a ticket|None|
|Requester ID|integer|None|False|User ID of the requester|None|
|Responder ID|integer|None|False|ID of the agent to whom the ticket has been assigned|None|
|Source|integer|None|False|The channel through which the ticket was created|None|
|Spam|boolean|None|False|Set to true if the ticket has been marked as spam|None|
|Status|integer|None|False|Status of the ticket|None|
|Sub Category|string|None|False|Ticket sub category|None|
|Subject|string|None|False|Subject of the ticket|None|
|Tags|[]string|None|False|Tags that have been associated with the ticket|None|
|To Emails|[]string|None|False|Email addresses to which the ticket was originally sent|None|
|Type|string|None|False|Type of the ticket|None|
|Updated At|string|None|False|Ticket updated timestamp|None|
|Urgency|integer|None|False|Ticket urgency|None|

## Troubleshooting
  
*There is no troubleshooting for this plugin.*  

# Version History
  
* 1.0.1 - Update Connection Test to account for Agents with least privileges 
* 1.0.0 - Initial plugin | Add Create Ticket, Update Ticket, Delete Ticket, List Tickets, Create Ticket Task, Update Ticket Task, Delete Ticket Task, List Groups and List Agents actions

# Links

## References
  
* [FreshService](https://freshservice.com)