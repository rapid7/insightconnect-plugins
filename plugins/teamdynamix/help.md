# Description

TeamDynamix is an IT Service Management (ITSM) and Project Portfolio Management  platform. This plugin allows users to create, read, update, and search tickets  within a TeamDynamix instance, enabling automated ticketing workflows.


# Key Features

* Create TeamDynamix tickets to initiate remediation workflows
* Get ticket details to monitor ticket status
* Update existing tickets with new information or status
* Search tickets by various criteria

# Requirements

* TeamDynamix instance base URL (e.g., https://yourorg.teamdynamix.com)
* For Admin authentication - BEID and Web Services Key, found in TDAdmin under the organization detail page (requires the Add BE Administrators permission)
* For User authentication - Username and password for a TeamDynamix service account with a security role that has ticket create/edit permissions and access to the target ticketing application
* Application ID for the target TeamDynamix ticketing application, found in TDAdmin under Applications

# Supported Product Versions

* TeamDynamix Web API

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|app_id|integer|None|True|Numeric Application ID for the target ticketing application, found in TDAdmin under Applications|None|42|None|None|
|auth_type|string|Admin|True|Admin uses BEID and Web Services Key (broad access), User uses username and password for a service account (scoped permissions)|["Admin", "User"]|Admin|None|None|
|base_url|string|None|True|The base URL of your TeamDynamix instance (e.g., https://yourorg.teamdynamix.com)|None|https://yourorg.teamdynamix.com|None|None|
|beid|string|None|False|Back End Identifier found in TDAdmin on the organization detail page, required for Admin authentication|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|None|None|
|credentials|credential_username_password|None|False|Username and password for a TeamDynamix service account created in TDAdmin under Users and Roles, required for User authentication|None|{"username": "svc_insightconnect", "password": "password"}|None|None|
|web_services_key|credential_secret_key|None|False|Web Services Key found in TDAdmin on the organization detail page, required for Admin authentication|None|xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx|None|None|

Example input:

```
{
  "app_id": 42,
  "auth_type": "Admin",
  "base_url": "https://yourorg.teamdynamix.com",
  "beid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "credentials": {
    "password": "password",
    "username": "svc_insightconnect"
  },
  "web_services_key": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

## Technical Details

### Actions


#### Create Ticket

This action is used to create a new ticket in TeamDynamix, use this action to open remediation tickets

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_id|integer|None|True|Numeric ID of the account or department|None|789|None|None|
|additional_fields|object|None|False|JSON object of additional fields to include in the ticket payload (e.g., custom attributes)|None|{"StatusID": 602}|None|None|
|description|string|None|False|Full description of the ticket|None|Critical vulnerability found on host 192.168.1.10|None|None|
|form_id|integer|None|False|Numeric ID of the ticket form in TeamDynamix|None|456|None|None|
|priority_id|integer|None|True|Numeric ID of the priority level in TeamDynamix|None|20|None|None|
|requestor_email|string|None|True|Email address of the ticket requestor|None|user@example.com|None|None|
|responsible_group_id|integer|None|False|Numeric ID of the group responsible for the ticket|None|100|None|None|
|status_id|integer|None|True|Numeric ID of the initial ticket status in TeamDynamix|None|602|None|None|
|title|string|None|True|Short title/subject of the ticket|None|Remediate Critical Vulnerability CVE-2024-1234|None|None|
|type_id|integer|None|True|Numeric ID of the ticket type in TeamDynamix|None|123|None|None|
  
Example input:

```
{
  "account_id": 789,
  "additional_fields": {
    "StatusID": 602
  },
  "description": "Critical vulnerability found on host 192.168.1.10",
  "form_id": 456,
  "priority_id": 20,
  "requestor_email": "user@example.com",
  "responsible_group_id": 100,
  "status_id": 602,
  "title": "Remediate Critical Vulnerability CVE-2024-1234",
  "type_id": 123
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the ticket was created successfully|True|
|ticket_id|integer|True|Numeric ID of the newly created ticket|12345|
|ticket_url|string|True|Direct URL to the created ticket in TeamDynamix|https://yourorg.teamdynamix.com/TDClient/42/Requests/TicketDet?TicketID=12345|
  
Example output:

```
{
  "success": true,
  "ticket_id": 12345,
  "ticket_url": "https://yourorg.teamdynamix.com/TDClient/42/Requests/TicketDet?TicketID=12345"
}
```

#### Get Ticket

This action is used to retrieve a TeamDynamix ticket by its ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ticket_id|integer|None|True|The numeric ID of the ticket to retrieve|None|12345|None|None|
  
Example input:

```
{
  "ticket_id": 12345
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|string|False|Current status of the ticket|New|
|ticket|object|True|The full ticket object returned by TeamDynamix|{"ID": 12345, "Title": "Test Ticket", "StatusName": "New"}|
|ticket_id|integer|False|Numeric ID of the ticket|12345|
|title|string|False|Title of the ticket|Test Ticket|
  
Example output:

```
{
  "status": "New",
  "ticket": {
    "ID": 12345,
    "StatusName": "New",
    "Title": "Test Ticket"
  },
  "ticket_id": 12345,
  "title": "Test Ticket"
}
```

#### Search Tickets

This action is used to search for tickets in TeamDynamix

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|max_results|integer|25|False|Maximum number of tickets to return (default 25)|None|25|None|None|
|search_text|string|None|False|Text to search in ticket titles and descriptions|None|CVE-2024|None|None|
|status_id|integer|None|False|Filter by status ID|None|602|None|None|
  
Example input:

```
{
  "max_results": 25,
  "search_text": "CVE-2024",
  "status_id": 602
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of tickets returned|1|
|tickets|[]object|True|List of matching ticket objects|[{"ID": 12345, "Title": "Test Ticket"}]|
  
Example output:

```
{
  "count": 1,
  "tickets": [
    {
      "ID": 12345,
      "Title": "Test Ticket"
    }
  ]
}
```

#### Update Ticket

This action is used to update an existing TeamDynamix ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_fields|object|None|False|JSON object of additional fields to update|None|{"AssignedAppID": 42}|None|None|
|description|string|None|False|New description for the ticket|None|Updated description|None|None|
|priority_id|integer|None|False|New priority ID for the ticket|None|20|None|None|
|status_id|integer|None|False|New status ID for the ticket|None|602|None|None|
|ticket_id|integer|None|True|The numeric ID of the ticket to update|None|12345|None|None|
|title|string|None|False|New title for the ticket|None|Updated title|None|None|
  
Example input:

```
{
  "additional_fields": {
    "AssignedAppID": 42
  },
  "description": "Updated description",
  "priority_id": 20,
  "status_id": 602,
  "ticket_id": 12345,
  "title": "Updated title"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the ticket was updated successfully|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* Admin authentication: The BEID and Web Services Key are found in TDAdmin on the organization detail page. An administrator with the Add BE Administrators permission can view these. The admin service account must be set to Active.
* User authentication: Create a service account in TDAdmin under Users & Roles > Users > Create > Create Service Account. Assign a security role with the following minimum permissions - All: View All Accts/Depts, Tickets: Create/Edit Tickets. Then grant the service account access to the target ticketing application under Applications > [App] > Users & Roles.
* Application ID: Found in TDAdmin under Applications. Select the ticketing application and note the numeric ID in the URL or application details.
* The base URL should not include a trailing slash
* Verify the Application ID matches the target TeamDynamix ticketing application

# Version History

* 1.0.0 - Initial plugin release with Create, Get, Update, and Search Ticket actions

# Links

* [TeamDynamix](https://www.teamdynamix.com/)
* [TeamDynamix Web API](https://solutions.teamdynamix.com/TDWebApi/)
* [TeamDynamix Web API Authentication](https://solutions.teamdynamix.com/TDWebApi/Home/section/Auth)

## References

* [TeamDynamix Web API Documentation](https://solutions.teamdynamix.com/TDWebApi/)
* [TeamDynamix Web API Authentication](https://solutions.teamdynamix.com/TDWebApi/Home/section/Auth)