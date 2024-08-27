# Description

TopDesk is a cloud ticketing system that focuses on ease of use and extensibility

# Key Features

* List Incidents
* Create Incident
* Get Incident by ID
* Get Incident by Number
* Update Incident by ID
* Update Incident by Number
* List Suppliers
* List Operators
* List Operator Groups
* List Locations and Branches

# Requirements

* TopDesk username
* [Application password](https://developers.topdesk.com/tutorial.html) needed to communicate with the API
* TopDesk domain

# Supported Product Versions

* TopDesk API v3.8.5

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|TopDesk username used for login and password generated in the 'Application passwords' section|None|{"username": "user", "password": "44d88612-fea8-a8f3-6de8-2e1278abb02f"}|None|None|
|domain|string|None|True|Domain|None|rapid7|None|None|

Example input:

```
{
  "credentials": {
    "password": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "username": "user"
  },
  "domain": "rapid7"
}
```

## Technical Details

### Actions


#### Create Incident

This action is used to creates an incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|False|Initial action|None|<b>example action</b>|None|None|
|actionInvisibleForCaller|boolean|None|False|Whether the initial action is invisible for callers|None|False|None|None|
|branch|string|None|False|Branch identifier for location. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|briefDescription|string|None|False|Brief description of the incident. For partials, if not provided, will be automatically copied from the main incident|None|Example description|None|None|
|callType|string|None|False|The type of the call. Cannot be provided for partials as its automatically copied from the main incident|None|Failure|None|None|
|caller|callerInput|None|False|The caller contact details for this incident. Is filled in automatically for persons and when the callerLookup parameter is provided|None|{"branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "budgetHolder": "Management"," department": "Management", "dynamicName": "Example User", "email": "user@example.com", "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "mobileNumber": "1111111", "phoneNumber": "2222222"}|None|None|
|callerLookup|string|None|False|Caller email for filling in a registered caller's contact details|None|user@example.com|None|None|
|category|string|None|False|The name of the category. For partials, if not provided, will be automatically copied from the main incident|None|Hardware|None|None|
|closed|boolean|None|False|Whether the incident is closed|None|False|None|None|
|closedDate|date|None|False|Closed date|None|2022-11-15T14:00:00+0200|None|None|
|closureCode|string|None|False|The name of the closure code|None|Manual|None|None|
|completed|boolean|None|False|Whether the incident is completed|None|False|None|None|
|completedDate|date|None|False|Completed date|None|2022-11-15T14:00:00+0200|None|None|
|costs|float|None|False|Costs|None|12.5|None|None|
|duration|string|None|False|Duration name|None|1 week|None|None|
|entryType|string|None|False|The type of the entry|None|Chat|None|None|
|externalNumber|string|None|False|External number. For partials, if not provided, will be automatically copied from the main incident|None|test_123|None|None|
|feedbackMessage|string|None|False|Feedback message of the incident, only available for closed incidents|None|Great job!|None|None|
|feedbackRating|integer|None|False|Rate incident, only available for closed incidents|None|5|None|None|
|impact|string|None|False|The name of the impact. Cannot be provided for partials as its automatically copied from the main incident|None|Person|None|None|
|location|string|None|False|Location identifier. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|mainIncident|string|None|False|Main incident number, required for creating a partial incident. This must be an open, unarchived second line incident and visible to the operator|None|I 1000 123|None|None|
|majorCall|boolean|None|False|Whether the incident is a major call|None|True|None|None|
|majorCallObject|string|None|False|Number of the major call incident to which you want to link the created incident|None|I 2301 104|None|None|
|object|string|None|False|The name of the object. For partial incidents, this field is determined by the main incident and will give an error if provided. If both object and location are given, object is set and location is ignored|None|OBJ001|None|None|
|onHold|boolean|None|False|Whether incident is on hold|None|False|None|None|
|operator|string|None|False|Operator identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|operatorGroup|string|None|False|Operator group identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|optionalFields1|object|None|False|Optional Fields 1|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00+0200"}|None|None|
|optionalFields2|object|None|False|Optional Fields 2|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00+0200"}|None|None|
|priority|string|None|False|The name of the priority. Cannot be provided for partials as it is automatically copied from the main incident. Will be automatically filled in if you provide impact and/or urgency leading to a unique priority according to your priority matrix, and don't provide a priority. For incidents with a linked SLA, if the priority provided cannot be found in the Service Level Priority List, the duration field of the incident will be emptied|None|P1|None|None|
|processingStatus|string|None|False|Processing status name|None|Registered|None|None|
|publishToSsd|boolean|None|False|Whether the incident should be published in the Self Service Desk. Only major incidents can be published|None|False|None|None|
|request|string|None|False|Initial request that caused the incident|None|<b>example request</b>|None|None|
|responded|boolean|None|False|Whether the incident is responded|None|False|None|None|
|responseDate|date|None|False|Response date. Will automatically be set to current date if left out and 'responded' is set to 'true'|None|2022-11-15T14:00:00+0200|None|None|
|sla|string|None|False|SLA identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|status|string|None|False|Status of the incident|["", "First Line Incident", "Second Line Incident", "Partial Incident"]|First Line Incident|None|None|
|subcategory|string|None|False|The name of the subcategory. For partials, if not provided, will be automatically copied from the main incident. If a subcategory is provided without a category, the corresponding category will be filled in automatically, unless there are multiple matching categories, in which case the action will fail|None|Laptop|None|None|
|supplier|string|None|False|Supplier identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|targetDate|date|None|False|Target date|None|2022-11-15T14:00:00+0200|None|None|
|urgency|string|None|False|The name of the urgency. Cannot be provided for partials as its automatically copied from the main incident|None|Normal|None|None|
  
Example input:

```
{
  "action": "<b>example action</b>",
  "actionInvisibleForCaller": false,
  "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "briefDescription": "Example description",
  "callType": "Failure",
  "caller": {
    " department": "Management",
    "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "budgetHolder": "Management",
    "dynamicName": "Example User",
    "email": "user@example.com",
    "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "mobileNumber": "1111111",
    "phoneNumber": "2222222"
  },
  "callerLookup": "user@example.com",
  "category": "Hardware",
  "closed": false,
  "closedDate": "2022-11-15T14:00:00+0200",
  "closureCode": "Manual",
  "completed": false,
  "completedDate": "2022-11-15T14:00:00+0200",
  "costs": 12.5,
  "duration": "1 week",
  "entryType": "Chat",
  "externalNumber": "test_123",
  "feedbackMessage": "Great job!",
  "feedbackRating": 5,
  "impact": "Person",
  "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "mainIncident": "I 1000 123",
  "majorCall": true,
  "majorCallObject": "I 2301 104",
  "object": "OBJ001",
  "onHold": false,
  "operator": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "operatorGroup": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "optionalFields1": {
    "boolean1": true,
    "date1": "2022-11-15T14:00:00+0200",
    "text1": "example value"
  },
  "optionalFields2": {
    "boolean1": true,
    "date1": "2022-11-15T14:00:00+0200",
    "text1": "example value"
  },
  "priority": "P1",
  "processingStatus": "Registered",
  "publishToSsd": false,
  "request": "<b>example request</b>",
  "responded": false,
  "responseDate": "2022-11-15T14:00:00+0200",
  "sla": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "status": "First Line Incident",
  "subcategory": "Laptop",
  "supplier": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "targetDate": "2022-11-15T14:00:00+0200",
  "urgency": "Normal"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|False|Information about the created incident|{'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'firstLine', 'number': 'I 2301 103', 'request': '25-01-2023 11:14 [GMT +0:00] User Example: \nexample request', 'requests': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests', 'action': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions', 'attachments': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments', 'caller': {'branch': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'budgetHolder': 'Management', 'department': 'Management', 'email': 'user@example.com', 'location': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'mobileNumber': '1111111', 'phoneNumber': '2222222'}, 'callerBranch': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'TOPdesk', 'timeZone': 'Europe/Dublin'}, 'callerLocation': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': "CEO's Office"}, 'briefDescription': 'test description', 'category': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Hardware'}, 'subcategory': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Laptop'}, 'callType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Failure'}, 'entryType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Chat'}, 'impact': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Person'}, 'urgency': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Normal'}, 'priority': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'P1'}, 'duration': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': '8 hours'}, 'targetDate': '2023-01-29T13:00:00.000+0000', 'onHold': False, 'operator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'operator', 'name': 'Example User'}, 'processingStatus': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Registered'}, 'responded': 'false "completed":false "closed":false "costs":12.5', 'callDate': '2023-01-25T11:14:25.000+0000', 'creator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example User'}, 'creationDate': '2023-01-25T11:14:25.000+0000', 'modifier': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example User'}, 'modificationDate': '2023-01-25T11:14:25.000+0000', 'majorCall': True, 'publishToSsd': False, 'monitored': False, 'optionalFields1': {'boolean1': False, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False}, 'optionalFields2': {'boolean1': False, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False}}|
  
Example output:

```
{
  "incident": {
    "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "briefDescription": "test description",
    "callDate": "2023-01-25T11:14:25.000+0000",
    "callType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Failure"
    },
    "caller": {
      "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "budgetHolder": "Management",
      "department": "Management",
      "email": "user@example.com",
      "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "mobileNumber": "1111111",
      "phoneNumber": "2222222"
    },
    "callerBranch": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "TOPdesk",
      "timeZone": "Europe/Dublin"
    },
    "callerLocation": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "CEO's Office"
    },
    "category": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Hardware"
    },
    "creationDate": "2023-01-25T11:14:25.000+0000",
    "creator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example User"
    },
    "duration": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "8 hours"
    },
    "entryType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Chat"
    },
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "impact": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Person"
    },
    "majorCall": true,
    "modificationDate": "2023-01-25T11:14:25.000+0000",
    "modifier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example User"
    },
    "monitored": false,
    "number": "I 2301 103",
    "onHold": false,
    "operator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example User",
      "status": "operator"
    },
    "optionalFields1": {
      "boolean1": false,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false
    },
    "optionalFields2": {
      "boolean1": false,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false
    },
    "priority": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "P1"
    },
    "processingStatus": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Registered"
    },
    "publishToSsd": false,
    "request": "25-01-2023 11:14 [GMT +0:00] User Example: \nexample request",
    "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "responded": "false \"completed\":false \"closed\":false \"costs\":12.5",
    "status": "firstLine",
    "subcategory": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Laptop"
    },
    "targetDate": "2023-01-29T13:00:00.000+0000",
    "urgency": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Normal"
    }
  }
}
```

#### Get Incident by ID

This action is used to returns an incident by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The identifier of the incident to be returned|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
  
Example input:

```
{
  "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|False|Information about the given incident|{'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'secondLine', 'number': 'I 2301 004', 'request': '16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request', 'requests': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests', 'action': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions', 'attachments': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments', 'caller': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'dynamicName': 'Example User', 'phoneNumber': '2222222', 'mobileNumber': '1111111', 'email': 'user@example.com', 'branch': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example branch', 'timeZone': 'Europe/Berlin'}}, 'callerBranch': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example branch', 'timeZone': 'Europe/Berlin'}, 'callerLocation': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example location'}, 'briefDescription': 'Example description', 'externalNumber': 'test_123', 'category': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Hardware'}, 'subcategory': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Monitor'}, 'callType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Failure'}, 'entryType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Chat'}, 'object': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'OBJ001'}, 'asset': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f'}, 'impact': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Person'}, 'urgency': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Normal'}, 'priority': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'P1'}, 'duration': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': '1 week'}, 'targetDate': '2022-11-15T14:00:00.000+0200', 'onHold': False, 'operator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'operator', 'name': 'Example Operator'}, 'operatorGroup': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Application management'}, 'supplier': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'DELL', 'forFirstLine': True, 'forSecondLine': True}, 'processingStatus': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Registered'}, 'responded': False, 'completed': False, 'closed': False, 'costs': 249.99, 'callDate': '2022-11-15T14:00:00.000+0200', 'creator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example Operator'}, 'creationDate': '2022-11-15T14:00:00.000+0200', 'modifier': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example Operator'}, 'modificationDate': '2022-11-15T14:00:00.000+0200', 'majorCall': True, 'publishToSsd': False, 'monitored': False, 'expectedTimeSpent': 120, 'optionalFields1': {'boolean1': False, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False}, 'optionalFields2': {'boolean1': False, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False}}|
  
Example output:

```
{
  "incident": {
    "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "asset": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
    },
    "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "briefDescription": "Example description",
    "callDate": "2022-11-15T14:00:00.000+0200",
    "callType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Failure"
    },
    "caller": {
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Berlin"
      },
      "dynamicName": "Example User",
      "email": "user@example.com",
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "mobileNumber": "1111111",
      "phoneNumber": "2222222"
    },
    "callerBranch": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example branch",
      "timeZone": "Europe/Berlin"
    },
    "callerLocation": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example location"
    },
    "category": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Hardware"
    },
    "closed": false,
    "completed": false,
    "costs": 249.99,
    "creationDate": "2022-11-15T14:00:00.000+0200",
    "creator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "duration": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "1 week"
    },
    "entryType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Chat"
    },
    "expectedTimeSpent": 120,
    "externalNumber": "test_123",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "impact": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Person"
    },
    "majorCall": true,
    "modificationDate": "2022-11-15T14:00:00.000+0200",
    "modifier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "monitored": false,
    "number": "I 2301 004",
    "object": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "OBJ001"
    },
    "onHold": false,
    "operator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator",
      "status": "operator"
    },
    "operatorGroup": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Application management"
    },
    "optionalFields1": {
      "boolean1": false,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false
    },
    "optionalFields2": {
      "boolean1": false,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false
    },
    "priority": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "P1"
    },
    "processingStatus": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Registered"
    },
    "publishToSsd": false,
    "request": "16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request",
    "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "responded": false,
    "status": "secondLine",
    "subcategory": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Monitor"
    },
    "supplier": {
      "forFirstLine": true,
      "forSecondLine": true,
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "DELL"
    },
    "targetDate": "2022-11-15T14:00:00.000+0200",
    "urgency": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Normal"
    }
  }
}
```

#### Get Incident by Number

This action is used to returns an incident by number

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentNumber|string|None|True|Number of the incident|None|I 2301 004|None|None|
  
Example input:

```
{
  "incidentNumber": "I 2301 004"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|False|Information about the given incident|{'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'secondLine', 'number': 'I 2301 004', 'request': '16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request', 'requests': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests', 'action': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions', 'attachments': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments', 'caller': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'dynamicName': 'Example User', 'phoneNumber': '2222222', 'mobileNumber': '1111111', 'email': 'user@example.com', 'branch': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example branch', 'timeZone': 'Europe/Berlin'}}, 'callerBranch': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example branch', 'timeZone': 'Europe/Berlin'}, 'callerLocation': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example location'}, 'briefDescription': 'Example description', 'externalNumber': 'test_123', 'category': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Hardware'}, 'subcategory': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Monitor'}, 'callType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Failure'}, 'entryType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Chat'}, 'object': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'OBJ001'}, 'asset': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f'}, 'impact': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Person'}, 'urgency': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Normal'}, 'priority': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'P1'}, 'duration': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': '1 week'}, 'targetDate': '2022-11-15T14:00:00.000+0200', 'onHold': False, 'operator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'operator', 'name': 'Example Operator'}, 'operatorGroup': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Application management'}, 'supplier': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'DELL', 'forFirstLine': True, 'forSecondLine': True}, 'processingStatus': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Registered'}, 'responded': False, 'completed': False, 'closed': False, 'costs': 249.99, 'callDate': '2022-11-15T14:00:00.000+0200', 'creator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example Operator'}, 'creationDate': '2022-11-15T14:00:00.000+0200', 'modifier': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example Operator'}, 'modificationDate': '2022-11-15T14:00:00.000+0200', 'majorCall': True, 'publishToSsd': False, 'monitored': False, 'expectedTimeSpent': 120, 'optionalFields1': {'boolean1': False, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False}, 'optionalFields2': {'boolean1': False, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False}}|
  
Example output:

```
{
  "incident": {
    "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "asset": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
    },
    "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "briefDescription": "Example description",
    "callDate": "2022-11-15T14:00:00.000+0200",
    "callType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Failure"
    },
    "caller": {
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Berlin"
      },
      "dynamicName": "Example User",
      "email": "user@example.com",
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "mobileNumber": "1111111",
      "phoneNumber": "2222222"
    },
    "callerBranch": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example branch",
      "timeZone": "Europe/Berlin"
    },
    "callerLocation": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example location"
    },
    "category": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Hardware"
    },
    "closed": false,
    "completed": false,
    "costs": 249.99,
    "creationDate": "2022-11-15T14:00:00.000+0200",
    "creator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "duration": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "1 week"
    },
    "entryType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Chat"
    },
    "expectedTimeSpent": 120,
    "externalNumber": "test_123",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "impact": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Person"
    },
    "majorCall": true,
    "modificationDate": "2022-11-15T14:00:00.000+0200",
    "modifier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "monitored": false,
    "number": "I 2301 004",
    "object": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "OBJ001"
    },
    "onHold": false,
    "operator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator",
      "status": "operator"
    },
    "operatorGroup": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Application management"
    },
    "optionalFields1": {
      "boolean1": false,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false
    },
    "optionalFields2": {
      "boolean1": false,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false
    },
    "priority": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "P1"
    },
    "processingStatus": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Registered"
    },
    "publishToSsd": false,
    "request": "16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request",
    "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "responded": false,
    "status": "secondLine",
    "subcategory": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Monitor"
    },
    "supplier": {
      "forFirstLine": true,
      "forSecondLine": true,
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "DELL"
    },
    "targetDate": "2022-11-15T14:00:00.000+0200",
    "urgency": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Normal"
    }
  }
}
```

#### List Incidents

This action is used to returns a list of incidents

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|all|boolean|None|False|Whether to return partial and archived incidents|None|True|None|None|
|fields|string|None|False|A comma-separated list of which fields should be returned. By default all fields will be returned|None|id,targetDate|None|None|
|pageSize|integer|None|False|How many incidents should be returned max. Default is 10. Should be between 1 and 1000|None|5|None|None|
|pageStart|integer|None|False|The offset to start at. Default is 0|None|2|None|None|
|query|string|None|False|A FIQL string to select which incidents should be returned|None|status==secondLine;priority.name==P1|None|None|
|sort|string|None|False|The sort order of the returned incidents|None|status:asc,creationDate:desc|None|None|
  
Example input:

```
{
  "all": true,
  "fields": "id,targetDate",
  "pageSize": 5,
  "pageStart": 2,
  "query": "status==secondLine;priority.name==P1",
  "sort": "status:asc,creationDate:desc"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incidents|[]incident|False|List of the incidents|[{"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "status": "secondLine", "number": "I 2301 103", "request": "25-01-2023 11:14 [GMT +0:00] User Example: \nexample request", "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests", "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions", "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments", "caller": {"branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "budgetHolder": "Management", "department": "Management", "email": "user@example.com", "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "mobileNumber": "1111111", "phoneNumber": "2222222"}, "callerBranch": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "TOPdesk", "timeZone": "Europe/Dublin"}, "callerLocation": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "CEO's Office"}, "briefDescription": "test description", "category": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Hardware"}, "subcategory": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Laptop"}, "callType": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Failure"}, "entryType": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Telephone"}, "impact": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Person"}, "urgency": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Normal"}, "priority": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "P1"}, "duration": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "8 hours"}, "targetDate": "2023-01-29T13:00:00.000+0000", "onHold": false, "feedbackMessage": "Great job!", "feedbackRating": 2, "operator": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "status": "operator", "name": "Example User"}, "processingStatus": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Registered"}, "responded": true, "responseDate": "2023-01-25T11:14:25.000+0000", "completed": true, "completedDate": "2023-01-25T11:14:25.000+0000", "closed": true, "closedDate": "2023-01-25T11:14:25.000+0000", "closureCode": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Manual"}, "costs": 12.5, "callDate": "2023-01-25T11:14:25.000+0000", "creator": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Example User"}, "creationDate": "2023-01-25T11:14:25.000+0000", "modifier": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Example User"}, "modificationDate": "2023-01-25T11:14:25.000+0000", "majorCall": true, "publishToSsd": false, "monitored": false, "optionalFields1": {"boolean1": false, "boolean2": false, "boolean3": false, "boolean4": false, "boolean5": false}, "optionalFields2": {"boolean1": false, "boolean2": false, "boolean3": false, "boolean4": false, "boolean5": false}}]|
  
Example output:

```
{
  "incidents": [
    {
      "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
      "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
      "briefDescription": "test description",
      "callDate": "2023-01-25T11:14:25.000+0000",
      "callType": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Failure"
      },
      "caller": {
        "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "budgetHolder": "Management",
        "department": "Management",
        "email": "user@example.com",
        "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "mobileNumber": "1111111",
        "phoneNumber": "2222222"
      },
      "callerBranch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "TOPdesk",
        "timeZone": "Europe/Dublin"
      },
      "callerLocation": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "CEO's Office"
      },
      "category": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Hardware"
      },
      "closed": true,
      "closedDate": "2023-01-25T11:14:25.000+0000",
      "closureCode": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Manual"
      },
      "completed": true,
      "completedDate": "2023-01-25T11:14:25.000+0000",
      "costs": 12.5,
      "creationDate": "2023-01-25T11:14:25.000+0000",
      "creator": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example User"
      },
      "duration": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "8 hours"
      },
      "entryType": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Telephone"
      },
      "feedbackMessage": "Great job!",
      "feedbackRating": 2,
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "impact": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Person"
      },
      "majorCall": true,
      "modificationDate": "2023-01-25T11:14:25.000+0000",
      "modifier": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example User"
      },
      "monitored": false,
      "number": "I 2301 103",
      "onHold": false,
      "operator": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example User",
        "status": "operator"
      },
      "optionalFields1": {
        "boolean1": false,
        "boolean2": false,
        "boolean3": false,
        "boolean4": false,
        "boolean5": false
      },
      "optionalFields2": {
        "boolean1": false,
        "boolean2": false,
        "boolean3": false,
        "boolean4": false,
        "boolean5": false
      },
      "priority": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "P1"
      },
      "processingStatus": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Registered"
      },
      "publishToSsd": false,
      "request": "25-01-2023 11:14 [GMT +0:00] User Example: \nexample request",
      "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
      "responded": true,
      "responseDate": "2023-01-25T11:14:25.000+0000",
      "status": "secondLine",
      "subcategory": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Laptop"
      },
      "targetDate": "2023-01-29T13:00:00.000+0000",
      "urgency": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Normal"
      }
    }
  ]
}
```

#### List Locations and Branches

This action is used to get a list of locations with branches

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|pageSize|integer|None|False|The maximum number of locations to be returned. Default is unlimited|None|100|None|None|
|query|string|None|False|A FIQL search expression to filter the result|None|branch.name=='Example Branch'|None|None|
  
Example input:

```
{
  "pageSize": 100,
  "query": "branch.name=='Example Branch'"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|locationsAndBranches|[]location|False|List of the locations with branches|[{"id": "44d88612-fea8-a8f3-6de8-2e1278abb021", "name": "1st Floor", "branch": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb021", "name": "Example Branch"}}]|
  
Example output:

```
{
  "locationsAndBranches": [
    {
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb021",
        "name": "Example Branch"
      },
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb021",
      "name": "1st Floor"
    }
  ]
}
```

#### List Operator Groups

This action is used to get a list of operator groups

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|Only include these specific fields in the response. The default is that all fields are included|None|id,groupName|None|None|
|pageSize|integer|None|False|The amount of operator groups to be returned per page. Must be between 1 and 100|None|100|None|None|
|query|string|None|False|A FIQL search expression to filter the result|None|groupName=='Test Group'|None|None|
|start|integer|None|False|The offset at which to start listing the operator groups at. Must be greater or equal to 0|None|0|None|None|
  
Example input:

```
{
  "fields": "id,groupName",
  "pageSize": 100,
  "query": "groupName=='Test Group'",
  "start": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|operatorGroups|[]operatorGroup|False|List of the operator groups|[{"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "status": "operatorGroup", "groupName": "Test Group", "branch": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Example branch", "timeZone": "Europe/Dublin"}, "contact": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "dynamicName": "Test User", "telephone": "111111111", "email": "user@example.com", "department": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "IT"}, "hasAttention": false, "loginPermission": false, "installer": false, "firstLineCallOperator": false, "secondLineCallOperator": false, "problemManager": false, "problemOperator": false, "changeCoordinator": false, "changeActivitiesOperator": false, "requestForChangeOperator": false, "extensiveChangeOperator": false, "simpleChangeOperator": false, "scenarioManager": false, "planningActivityManager": false, "projectCoordinator": false, "projectActiviesOperator": false, "stockManager": false, "reservationsOperator": false, "serviceOperator": false, "externalHelpDeskParty": false, "contractManager": false, "operationsOperator": false, "operationsManager": false, "knowledgeBaseManager": false, "accountManager": false}, "installer": false, "firstLineCallOperator": true, "secondLineCallOperator": true, "problemManager": false, "problemOperator": false, "changeCoordinator": true, "changeActivitiesOperator": true, "requestForChangeOperator": false, "extensiveChangeOperator": false, "simpleChangeOperator": false, "scenarioManager": false, "planningActivityManager": false, "projectCoordinator": false, "projectActiviesOperator": true, "stockManager": false, "reservationsOperator": false, "serviceOperator": false, "externalHelpDeskParty": false, "contractManager": false, "operationsOperator": false, "operationsManager": false, "knowledgeBaseManager": true, "accountManager": false, "creationDate": "2021-11-03T15:39:54.000+0000", "creator": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Test User"}, "modificationDate": "2021-11-03T15:39:54.000+0000", "modifier": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Test User"}, "optionalFields1": {"boolean1": false, "boolean2": false, "boolean3": false, "boolean4": false, "boolean5": false}, "optionalFields2": {"boolean1": false, "boolean2": false, "boolean3": false, "boolean4": false, "boolean5": false}}]|
  
Example output:

```
{
  "operatorGroups": [
    {
      "accountManager": false,
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Dublin"
      },
      "changeActivitiesOperator": true,
      "changeCoordinator": true,
      "contact": {
        "accountManager": false,
        "changeActivitiesOperator": false,
        "changeCoordinator": false,
        "contractManager": false,
        "department": {
          "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
          "name": "IT"
        },
        "dynamicName": "Test User",
        "email": "user@example.com",
        "extensiveChangeOperator": false,
        "externalHelpDeskParty": false,
        "firstLineCallOperator": false,
        "hasAttention": false,
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "installer": false,
        "knowledgeBaseManager": false,
        "loginPermission": false,
        "operationsManager": false,
        "operationsOperator": false,
        "planningActivityManager": false,
        "problemManager": false,
        "problemOperator": false,
        "projectActiviesOperator": false,
        "projectCoordinator": false,
        "requestForChangeOperator": false,
        "reservationsOperator": false,
        "scenarioManager": false,
        "secondLineCallOperator": false,
        "serviceOperator": false,
        "simpleChangeOperator": false,
        "stockManager": false,
        "telephone": "111111111"
      },
      "contractManager": false,
      "creationDate": "2021-11-03T15:39:54.000+0000",
      "creator": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Test User"
      },
      "extensiveChangeOperator": false,
      "externalHelpDeskParty": false,
      "firstLineCallOperator": true,
      "groupName": "Test Group",
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "installer": false,
      "knowledgeBaseManager": true,
      "modificationDate": "2021-11-03T15:39:54.000+0000",
      "modifier": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Test User"
      },
      "operationsManager": false,
      "operationsOperator": false,
      "optionalFields1": {
        "boolean1": false,
        "boolean2": false,
        "boolean3": false,
        "boolean4": false,
        "boolean5": false
      },
      "optionalFields2": {
        "boolean1": false,
        "boolean2": false,
        "boolean3": false,
        "boolean4": false,
        "boolean5": false
      },
      "planningActivityManager": false,
      "problemManager": false,
      "problemOperator": false,
      "projectActiviesOperator": true,
      "projectCoordinator": false,
      "requestForChangeOperator": false,
      "reservationsOperator": false,
      "scenarioManager": false,
      "secondLineCallOperator": true,
      "serviceOperator": false,
      "simpleChangeOperator": false,
      "status": "operatorGroup",
      "stockManager": false
    }
  ]
}
```

#### List Operators

This action is used to get a list of operators

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|Only include these specific fields in the response. The default is that all fields are included|None|id,dynamicName|None|None|
|pageSize|integer|None|False|The amount of operators to be returned per page. Must be between 1 and 100|None|100|None|None|
|query|string|None|False|A FIQL search expression to filter the result|None|dynamicName=='Test User'|None|None|
|start|integer|None|False|The offset at which to start listing the operators at. Must be greater or equal to 0|None|0|None|None|
  
Example input:

```
{
  "fields": "id,dynamicName",
  "pageSize": 100,
  "query": "dynamicName=='Test User'",
  "start": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|operators|[]operatorOutput|False|List of the operators|[{"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "principalId": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "status": "operator", "accountType": "regular", "surName": "User", "firstName": "Test", "dynamicName": "Test User", "initials": "T.", "title": "Mrs", "gender": "FEMALE", "language": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "English"}, "branch": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Example branch", "timeZone": "Europe/Dublin"}, "location": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "branch": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Example branch", "timeZone": "Europe/Dublin"}, "name": "Example location", "room": "Test room"}, "telephone": "111111111", "email": "user@example.com", "exchangeAccount": "user@example.com", "loginName": "TEST", "loginPermission": true, "jobTitle": "Application Manager", "department": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "IT"}, "hasAttention": false, "installer": true, "firstLineCallOperator": true, "secondLineCallOperator": true, "problemManager": true, "problemOperator": true, "changeCoordinator": true, "changeActivitiesOperator": true, "requestForChangeOperator": true, "extensiveChangeOperator": true, "simpleChangeOperator": true, "scenarioManager": true, "planningActivityManager": true, "projectCoordinator": true, "projectActiviesOperator": true, "stockManager": true, "reservationsOperator": true, "serviceOperator": true, "externalHelpDeskParty": true, "contractManager": true, "operationsOperator": true, "operationsManager": true, "knowledgeBaseManager": true, "accountManager": false, "creationDate": "2020-09-29T21:08:30.000+0000", "creator": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "Admin"}, "modificationDate": "2023-01-18T04:20:14.000+0000", "modifier": {"id": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "name": "SUPPORT"}, "accessRoles": [{"href": "https://example.com", "type": "application/json"}, {"href": "https://example.com", "type": "application/json"}], "optionalFields1": {"boolean1": false, "boolean2": false, "boolean3": false, "boolean4": false, "boolean5": false}, "optionalFields2": {"boolean1": false, "boolean2": false, "boolean3": false, "boolean4": false, "boolean5": false}}]|
  
Example output:

```
{
  "operators": [
    {
      "accessRoles": [
        {
          "href": "https://example.com",
          "type": "application/json"
        },
        {
          "href": "https://example.com",
          "type": "application/json"
        }
      ],
      "accountManager": false,
      "accountType": "regular",
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Dublin"
      },
      "changeActivitiesOperator": true,
      "changeCoordinator": true,
      "contractManager": true,
      "creationDate": "2020-09-29T21:08:30.000+0000",
      "creator": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Admin"
      },
      "department": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "IT"
      },
      "dynamicName": "Test User",
      "email": "user@example.com",
      "exchangeAccount": "user@example.com",
      "extensiveChangeOperator": true,
      "externalHelpDeskParty": true,
      "firstLineCallOperator": true,
      "firstName": "Test",
      "gender": "FEMALE",
      "hasAttention": false,
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "initials": "T.",
      "installer": true,
      "jobTitle": "Application Manager",
      "knowledgeBaseManager": true,
      "language": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "English"
      },
      "location": {
        "branch": {
          "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
          "name": "Example branch",
          "timeZone": "Europe/Dublin"
        },
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example location",
        "room": "Test room"
      },
      "loginName": "TEST",
      "loginPermission": true,
      "modificationDate": "2023-01-18T04:20:14.000+0000",
      "modifier": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "SUPPORT"
      },
      "operationsManager": true,
      "operationsOperator": true,
      "optionalFields1": {
        "boolean1": false,
        "boolean2": false,
        "boolean3": false,
        "boolean4": false,
        "boolean5": false
      },
      "optionalFields2": {
        "boolean1": false,
        "boolean2": false,
        "boolean3": false,
        "boolean4": false,
        "boolean5": false
      },
      "planningActivityManager": true,
      "principalId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "problemManager": true,
      "problemOperator": true,
      "projectActiviesOperator": true,
      "projectCoordinator": true,
      "requestForChangeOperator": true,
      "reservationsOperator": true,
      "scenarioManager": true,
      "secondLineCallOperator": true,
      "serviceOperator": true,
      "simpleChangeOperator": true,
      "status": "operator",
      "stockManager": true,
      "surName": "User",
      "telephone": "111111111",
      "title": "Mrs"
    }
  ]
}
```

#### List Suppliers

This action is used to get a list of suppliers

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|pageSize|integer|None|False|The amount of suppliers to be returned per request. Must be between 1 and 100|None|100|None|None|
|query|string|None|False|A FIQL search expression to filter the result|None|name=='Example Supplier'|None|None|
|start|integer|None|False|The offset at which to start listing the suppliers at. Must be greater or equal to 0|None|0|None|None|
  
Example input:

```
{
  "pageSize": 100,
  "query": "name=='Example Supplier'",
  "start": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|suppliers|[]supplierOutput|False|List of the suppliers|[{"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "name": "Example Supplier", "forFirstLine": false, "forSecondLine": false, "forService": false, "forOperationalActivity": false, "forChangeManagement": false}]|
  
Example output:

```
{
  "suppliers": [
    {
      "forChangeManagement": false,
      "forFirstLine": false,
      "forOperationalActivity": false,
      "forSecondLine": false,
      "forService": false,
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "Example Supplier"
    }
  ]
}
```

#### Update Incident by ID

This action is used to updates an incident by identifier. It doesn't reset fields that are not included in input

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|False|Initial action|None|<b>example action</b>|None|None|
|actionInvisibleForCaller|boolean|None|False|Whether the initial action is invisible for callers|None|False|None|None|
|branch|string|None|False|Branch identifier for location. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|briefDescription|string|None|False|Brief description of the incident. For partials, if not provided, will be automatically copied from the main incident|None|Example description|None|None|
|callDate|date|None|False|The date when this call was registered|None|2022-11-15T14:00:00+0200|None|None|
|callType|string|None|False|The type of the call. Cannot be provided for partials as its automatically copied from the main incident|None|Failure|None|None|
|caller|callerInput|None|False|The caller contact details for this incident. Is filled in automatically for persons and when the callerLookup parameter is provided|None|{"branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "budgetHolder": "Management"," department": "Management", "dynamicName": "Example User", "email": "user@example.com", "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "mobileNumber": "1111111", "phoneNumber": "2222222"}|None|None|
|callerLookup|string|None|False|Caller email for filling in a registered caller's contact details|None|user@example.com|None|None|
|category|string|None|False|The name of the category. For partials, if not provided, will be automatically copied from the main incident|None|Hardware|None|None|
|closed|boolean|None|False|Whether the incident is closed|None|False|None|None|
|closedDate|date|None|False|Closed date|None|2022-11-15T14:00:00+0200|None|None|
|closureCode|string|None|False|Name of the closure code|None|Manual|None|None|
|completed|boolean|None|False|Whether the incident is completed|None|False|None|None|
|completedDate|date|None|False|Completed date|None|2022-11-15T14:00:00+0200|None|None|
|costs|float|None|False|Costs|None|12.5|None|None|
|duration|string|None|False|Duration name|None|1 week|None|None|
|entryType|string|None|False|The type of the entry|None|Chat|None|None|
|externalNumber|string|None|False|External number. For partials, if not provided, will be automatically copied from the main incident|None|test_123|None|None|
|feedbackMessage|string|None|False|Feedback message of the incident, only available for closed incidents|None|Great job!|None|None|
|feedbackRating|integer|None|False|Rate incident, only available for closed incidents|None|5|None|None|
|id|string|None|True|Identifier of the incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|impact|string|None|False|Name of the impact. Cannot be provided for partials as its automatically copied from the main incident|None|Person|None|None|
|location|string|None|False|Location identifier. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|majorCall|boolean|None|False|Whether the incident is a major call|None|True|None|None|
|majorCallObject|string|None|False|Number of the major call incident to which you want to link the updated incident|None|I 2301 104|None|None|
|object|string|None|False|Name of the object. For partial incidents, this field is determined by the main incident and will give an error if provided. If both object and location are given, object is set and location is ignored|None|OBJ001|None|None|
|onHold|boolean|None|False|Whether incident is on hold|None|False|None|None|
|operator|string|None|False|Operator identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|operatorGroup|string|None|False|Operator group identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|optionalFields1|object|None|False|Optional Fields 1|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00+0200"}|None|None|
|optionalFields2|object|None|False|Optional Fields 2|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00+0200"}|None|None|
|priority|string|None|False|Name of the priority. Cannot be provided for partials as it is automatically copied from the main incident. Will be automatically filled in if you provide impact and/or urgency leading to a unique priority according to your priority matrix, and don't provide a priority. For incidents with a linked SLA, if the priority provided cannot be found in the Service Level Priority List, the duration field of the incident will be emptied|None|P1|None|None|
|processingStatus|string|None|False|Processing status name|None|Registered|None|None|
|publishToSsd|boolean|None|False|Whether the incident should be published in the Self Service Desk. Only major incidents can be published|None|False|None|None|
|request|string|None|False|Initial request that caused the incident|None|<b>example request</b>|None|None|
|responded|boolean|None|False|Whether the incident is responded|None|False|None|None|
|responseDate|date|None|False|Response date. Will automatically be set to current date if left out and 'responded' is set to 'true'|None|2022-11-15T14:00:00+0200|None|None|
|sla|string|None|False|SLA identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|subcategory|string|None|False|The name of the subcategory. For partials, if not provided, will be automatically copied from the main incident. If a subcategory is provided without a category, the corresponding category will be filled in automatically, unless there are multiple matching categories, in which case the action will fail|None|Laptop|None|None|
|supplier|string|None|False|Supplier identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|targetDate|date|None|False|Target date|None|2022-11-15T14:00:00+0200|None|None|
|urgency|string|None|False|Name of the urgency. Cannot be provided for partials as its automatically copied from the main incident|None|Normal|None|None|
  
Example input:

```
{
  "action": "<b>example action</b>",
  "actionInvisibleForCaller": false,
  "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "briefDescription": "Example description",
  "callDate": "2022-11-15T14:00:00+0200",
  "callType": "Failure",
  "caller": {
    " department": "Management",
    "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "budgetHolder": "Management",
    "dynamicName": "Example User",
    "email": "user@example.com",
    "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "mobileNumber": "1111111",
    "phoneNumber": "2222222"
  },
  "callerLookup": "user@example.com",
  "category": "Hardware",
  "closed": false,
  "closedDate": "2022-11-15T14:00:00+0200",
  "closureCode": "Manual",
  "completed": false,
  "completedDate": "2022-11-15T14:00:00+0200",
  "costs": 12.5,
  "duration": "1 week",
  "entryType": "Chat",
  "externalNumber": "test_123",
  "feedbackMessage": "Great job!",
  "feedbackRating": 5,
  "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "impact": "Person",
  "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "majorCall": true,
  "majorCallObject": "I 2301 104",
  "object": "OBJ001",
  "onHold": false,
  "operator": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "operatorGroup": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "optionalFields1": {
    "boolean1": true,
    "date1": "2022-11-15T14:00:00+0200",
    "text1": "example value"
  },
  "optionalFields2": {
    "boolean1": true,
    "date1": "2022-11-15T14:00:00+0200",
    "text1": "example value"
  },
  "priority": "P1",
  "processingStatus": "Registered",
  "publishToSsd": false,
  "request": "<b>example request</b>",
  "responded": false,
  "responseDate": "2022-11-15T14:00:00+0200",
  "sla": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "subcategory": "Laptop",
  "supplier": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "targetDate": "2022-11-15T14:00:00+0200",
  "urgency": "Normal"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|False|Information about the updated incident|{'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'secondLine', 'number': 'I 2301 004', 'request': '16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request', 'requests': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests', 'action': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions', 'attachments': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments', 'caller': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'dynamicName': 'Example User', 'phoneNumber': '2222222', 'mobileNumber': '1111111', 'email': 'user@example.com', 'branch': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example branch', 'timeZone': 'Europe/Berlin'}}, 'callerBranch': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example branch', 'timeZone': 'Europe/Berlin'}, 'callerLocation': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example location'}, 'briefDescription': 'Example description', 'externalNumber': 'test_123', 'category': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Hardware'}, 'subcategory': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Monitor'}, 'callType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Failure'}, 'entryType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Chat'}, 'object': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'OBJ001'}, 'asset': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f'}, 'impact': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Person'}, 'urgency': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Normal'}, 'priority': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'P1'}, 'duration': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': '1 week'}, 'targetDate': '2022-11-15T14:00:00.000+0200', 'onHold': False, 'operator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'operator', 'name': 'Example Operator'}, 'operatorGroup': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Application management'}, 'supplier': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'DELL', 'forFirstLine': True, 'forSecondLine': True}, 'processingStatus': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Registered'}, 'responded': False, 'completed': False, 'closed': False, 'costs': 249.99, 'callDate': '2022-11-15T14:00:00.000+0200', 'creator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example Operator'}, 'creationDate': '2022-11-15T14:00:00.000+0200', 'modifier': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example Operator'}, 'modificationDate': '2022-11-15T14:00:00.000+0200', 'majorCall': True, 'publishToSsd': False, 'monitored': False, 'expectedTimeSpent': 120, 'optionalFields1': {'boolean1': True, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False, 'date1': '2022-11-15T14:00:00.000+0200', 'text1': 'example value'}, 'optionalFields2': {'boolean1': True, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False, 'date1': '2022-11-15T14:00:00.000+0200', 'text1': 'example value'}}|
  
Example output:

```
{
  "incident": {
    "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "asset": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
    },
    "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "briefDescription": "Example description",
    "callDate": "2022-11-15T14:00:00.000+0200",
    "callType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Failure"
    },
    "caller": {
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Berlin"
      },
      "dynamicName": "Example User",
      "email": "user@example.com",
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "mobileNumber": "1111111",
      "phoneNumber": "2222222"
    },
    "callerBranch": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example branch",
      "timeZone": "Europe/Berlin"
    },
    "callerLocation": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example location"
    },
    "category": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Hardware"
    },
    "closed": false,
    "completed": false,
    "costs": 249.99,
    "creationDate": "2022-11-15T14:00:00.000+0200",
    "creator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "duration": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "1 week"
    },
    "entryType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Chat"
    },
    "expectedTimeSpent": 120,
    "externalNumber": "test_123",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "impact": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Person"
    },
    "majorCall": true,
    "modificationDate": "2022-11-15T14:00:00.000+0200",
    "modifier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "monitored": false,
    "number": "I 2301 004",
    "object": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "OBJ001"
    },
    "onHold": false,
    "operator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator",
      "status": "operator"
    },
    "operatorGroup": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Application management"
    },
    "optionalFields1": {
      "boolean1": true,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false,
      "date1": "2022-11-15T14:00:00.000+0200",
      "text1": "example value"
    },
    "optionalFields2": {
      "boolean1": true,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false,
      "date1": "2022-11-15T14:00:00.000+0200",
      "text1": "example value"
    },
    "priority": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "P1"
    },
    "processingStatus": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Registered"
    },
    "publishToSsd": false,
    "request": "16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request",
    "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "responded": false,
    "status": "secondLine",
    "subcategory": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Monitor"
    },
    "supplier": {
      "forFirstLine": true,
      "forSecondLine": true,
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "DELL"
    },
    "targetDate": "2022-11-15T14:00:00.000+0200",
    "urgency": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Normal"
    }
  }
}
```

#### Update Incident by Number

This action is used to updates an incident by number. It doesn't reset fields that are not included in input

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|False|Initial action|None|<b>example action</b>|None|None|
|actionInvisibleForCaller|boolean|None|False|Whether the initial action is invisible for callers|None|False|None|None|
|branch|string|None|False|Branch identifier for location. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|briefDescription|string|None|False|Brief description of the incident. For partials, if not provided, will be automatically copied from the main incident|None|Example description|None|None|
|callDate|date|None|False|The date when this call was registered|None|2022-11-15T14:00:00+0200|None|None|
|callType|string|None|False|The type of the call. Cannot be provided for partials as its automatically copied from the main incident|None|Failure|None|None|
|caller|callerInput|None|False|The caller contact details for this incident. Is filled in automatically for persons and when the callerLookup parameter is provided|None|{"branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "budgetHolder": "Management"," department": "Management", "dynamicName": "Example User", "email": "user@example.com", "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "mobileNumber": "1111111", "phoneNumber": "2222222"}|None|None|
|callerLookup|string|None|False|Caller email for filling in a registered caller's contact details|None|user@example.com|None|None|
|category|string|None|False|The name of the category. For partials, if not provided, will be automatically copied from the main incident|None|Hardware|None|None|
|closed|boolean|None|False|Whether the incident is closed|None|False|None|None|
|closedDate|date|None|False|Closed date|None|2022-11-15T14:00:00+0200|None|None|
|closureCode|string|None|False|Name of the closure code|None|Manual|None|None|
|completed|boolean|None|False|Whether the incident is completed|None|False|None|None|
|completedDate|date|None|False|Completed date|None|2022-11-15T14:00:00+0200|None|None|
|costs|float|None|False|Costs|None|12.5|None|None|
|duration|string|None|False|Duration name|None|1 week|None|None|
|entryType|string|None|False|The type of the entry|None|Chat|None|None|
|externalNumber|string|None|False|External number. For partials, if not provided, will be automatically copied from the main incident|None|test_123|None|None|
|feedbackMessage|string|None|False|Feedback message of the incident, only available for closed incidents|None|Great job!|None|None|
|feedbackRating|integer|None|False|Rate incident, only available for closed incidents|None|5|None|None|
|impact|string|None|False|Name of the impact. Cannot be provided for partials as its automatically copied from the main incident|None|Person|None|None|
|location|string|None|False|Location identifier. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|majorCall|boolean|None|False|Whether the incident is a major call|None|True|None|None|
|majorCallObject|string|None|False|Number of the major call incident to which you want to link the updated incident|None|I 2301 104|None|None|
|number|string|None|True|Number of the incident|None|I 2301 004|None|None|
|object|string|None|False|Name of the object. For partial incidents, this field is determined by the main incident and will give an error if provided. If both object and location are given, object is set and location is ignored|None|OBJ001|None|None|
|onHold|boolean|None|False|Whether incident is on hold|None|False|None|None|
|operator|string|None|False|Operator identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|operatorGroup|string|None|False|Operator group identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|optionalFields1|object|None|False|Optional Fields 1|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00+0200"}|None|None|
|optionalFields2|object|None|False|Optional Fields 2|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00+0200"}|None|None|
|priority|string|None|False|Name of the priority. Cannot be provided for partials as it is automatically copied from the main incident. Will be automatically filled in if you provide impact and/or urgency leading to a unique priority according to your priority matrix, and don't provide a priority. For incidents with a linked SLA, if the priority provided cannot be found in the Service Level Priority List, the duration field of the incident will be emptied|None|P1|None|None|
|processingStatus|string|None|False|Processing status name|None|Registered|None|None|
|publishToSsd|boolean|None|False|Whether the incident should be published in the Self Service Desk. Only major incidents can be published|None|False|None|None|
|request|string|None|False|Initial request that caused the incident|None|<b>example request</b>|None|None|
|responded|boolean|None|False|Whether the incident is responded|None|False|None|None|
|responseDate|date|None|False|Response date. Will automatically be set to current date if left out and 'responded' is set to 'true'|None|2022-11-15T14:00:00+0200|None|None|
|sla|string|None|False|SLA identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|subcategory|string|None|False|The name of the subcategory. For partials, if not provided, will be automatically copied from the main incident. If a subcategory is provided without a category, the corresponding category will be filled in automatically, unless there are multiple matching categories, in which case the action will fail|None|Laptop|None|None|
|supplier|string|None|False|Supplier identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|targetDate|date|None|False|Target date|None|2022-11-15T14:00:00+0200|None|None|
|urgency|string|None|False|Name of the urgency. Cannot be provided for partials as its automatically copied from the main incident|None|Normal|None|None|
  
Example input:

```
{
  "action": "<b>example action</b>",
  "actionInvisibleForCaller": false,
  "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "briefDescription": "Example description",
  "callDate": "2022-11-15T14:00:00+0200",
  "callType": "Failure",
  "caller": {
    " department": "Management",
    "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "budgetHolder": "Management",
    "dynamicName": "Example User",
    "email": "user@example.com",
    "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "mobileNumber": "1111111",
    "phoneNumber": "2222222"
  },
  "callerLookup": "user@example.com",
  "category": "Hardware",
  "closed": false,
  "closedDate": "2022-11-15T14:00:00+0200",
  "closureCode": "Manual",
  "completed": false,
  "completedDate": "2022-11-15T14:00:00+0200",
  "costs": 12.5,
  "duration": "1 week",
  "entryType": "Chat",
  "externalNumber": "test_123",
  "feedbackMessage": "Great job!",
  "feedbackRating": 5,
  "impact": "Person",
  "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "majorCall": true,
  "majorCallObject": "I 2301 104",
  "number": "I 2301 004",
  "object": "OBJ001",
  "onHold": false,
  "operator": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "operatorGroup": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "optionalFields1": {
    "boolean1": true,
    "date1": "2022-11-15T14:00:00+0200",
    "text1": "example value"
  },
  "optionalFields2": {
    "boolean1": true,
    "date1": "2022-11-15T14:00:00+0200",
    "text1": "example value"
  },
  "priority": "P1",
  "processingStatus": "Registered",
  "publishToSsd": false,
  "request": "<b>example request</b>",
  "responded": false,
  "responseDate": "2022-11-15T14:00:00+0200",
  "sla": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "subcategory": "Laptop",
  "supplier": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "targetDate": "2022-11-15T14:00:00+0200",
  "urgency": "Normal"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|False|Information about the updated incident|{'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'secondLine', 'number': 'I 2301 004', 'request': '16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request', 'requests': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests', 'action': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions', 'attachments': '/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments', 'caller': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'dynamicName': 'Example User', 'phoneNumber': '2222222', 'mobileNumber': '1111111', 'email': 'user@example.com', 'branch': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example branch', 'timeZone': 'Europe/Berlin'}}, 'callerBranch': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example branch', 'timeZone': 'Europe/Berlin'}, 'callerLocation': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example location'}, 'briefDescription': 'Example description', 'externalNumber': 'test_123', 'category': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Hardware'}, 'subcategory': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Monitor'}, 'callType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Failure'}, 'entryType': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Chat'}, 'object': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'OBJ001'}, 'asset': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f'}, 'impact': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Person'}, 'urgency': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Normal'}, 'priority': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'P1'}, 'duration': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': '1 week'}, 'targetDate': '2022-11-15T14:00:00.000+0200', 'onHold': False, 'operator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'status': 'operator', 'name': 'Example Operator'}, 'operatorGroup': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Application management'}, 'supplier': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'DELL', 'forFirstLine': True, 'forSecondLine': True}, 'processingStatus': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Registered'}, 'responded': False, 'completed': False, 'closed': False, 'costs': 249.99, 'callDate': '2022-11-15T14:00:00.000+0200', 'creator': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example Operator'}, 'creationDate': '2022-11-15T14:00:00.000+0200', 'modifier': {'id': '44d88612-fea8-a8f3-6de8-2e1278abb02f', 'name': 'Example Operator'}, 'modificationDate': '2022-11-15T14:00:00.000+0200', 'majorCall': True, 'publishToSsd': False, 'monitored': False, 'expectedTimeSpent': 120, 'optionalFields1': {'boolean1': True, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False, 'date1': '2022-11-15T14:00:00.000+0200', 'text1': 'example value'}, 'optionalFields2': {'boolean1': True, 'boolean2': False, 'boolean3': False, 'boolean4': False, 'boolean5': False, 'date1': '2022-11-15T14:00:00.000+0200', 'text1': 'example value'}}|
  
Example output:

```
{
  "incident": {
    "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "asset": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
    },
    "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "briefDescription": "Example description",
    "callDate": "2022-11-15T14:00:00.000+0200",
    "callType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Failure"
    },
    "caller": {
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Berlin"
      },
      "dynamicName": "Example User",
      "email": "user@example.com",
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "mobileNumber": "1111111",
      "phoneNumber": "2222222"
    },
    "callerBranch": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example branch",
      "timeZone": "Europe/Berlin"
    },
    "callerLocation": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example location"
    },
    "category": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Hardware"
    },
    "closed": false,
    "completed": false,
    "costs": 249.99,
    "creationDate": "2022-11-15T14:00:00.000+0200",
    "creator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "duration": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "1 week"
    },
    "entryType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Chat"
    },
    "expectedTimeSpent": 120,
    "externalNumber": "test_123",
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "impact": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Person"
    },
    "majorCall": true,
    "modificationDate": "2022-11-15T14:00:00.000+0200",
    "modifier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "monitored": false,
    "number": "I 2301 004",
    "object": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "OBJ001"
    },
    "onHold": false,
    "operator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator",
      "status": "operator"
    },
    "operatorGroup": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Application management"
    },
    "optionalFields1": {
      "boolean1": true,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false,
      "date1": "2022-11-15T14:00:00.000+0200",
      "text1": "example value"
    },
    "optionalFields2": {
      "boolean1": true,
      "boolean2": false,
      "boolean3": false,
      "boolean4": false,
      "boolean5": false,
      "date1": "2022-11-15T14:00:00.000+0200",
      "text1": "example value"
    },
    "priority": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "P1"
    },
    "processingStatus": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Registered"
    },
    "publishToSsd": false,
    "request": "16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request",
    "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "responded": false,
    "status": "secondLine",
    "subcategory": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Monitor"
    },
    "supplier": {
      "forFirstLine": true,
      "forSecondLine": true,
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "DELL"
    },
    "targetDate": "2022-11-15T14:00:00.000+0200",
    "urgency": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Normal"
    }
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**fieldObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|The identifier of the field|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Name|string|None|False|Name of the field|Example name|
  
**branch**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Client Reference Number|string|None|False|Client reference number|example|
|Extra Field A|fieldObject|None|False|Extra field A|{}|
|Extra Field B|fieldObject|None|False|Extra field B|{}|
|ID|string|None|False|Caller identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Name|string|None|False|Branch name|Example branch name|
|Time Zone|string|None|False|Time zone of the branch|example|
  
**caller**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Branch|branch|None|False|Branch of the caller|{}|
|Budget Holder|fieldObject|None|False|Budget holder of the caller|{}|
|Department|fieldObject|None|False|Department of the caller|{}|
|Dynamic Name|string|None|False|Caller dynamic name|Example User|
|Email|string|None|False|Email address of the caller|user@example.com|
|ID|string|None|False|Caller identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Mobile Number|string|None|False|Mobile number of the caller|123123123|
|Phone Number|string|None|False|Phone number of the caller|123123123|
  
**incidentObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Branch|fieldObject|None|False|Object branch|{}|
|ID|string|None|False|Object identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Location|fieldObject|None|False|Object location|{}|
|Make|fieldObject|None|False|Make|{}|
|Model|fieldObject|None|False|Object model|{}|
|Name|string|None|False|Object name|Example Object Name|
|Serial Number|string|None|False|Object serial number|OBJ123456|
|Specification|string|None|False|Object specification|Example specification|
|Type|fieldObject|None|False|Object type|{}|
  
**asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Asset identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
  
**location**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Branch|branch|None|False|Location branch|{}|
|ID|string|None|False|Location identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Name|string|None|False|Location name|Example Location|
|Room|string|None|False|Location room|Room 01|
  
**slaObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|SLA identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Response Target Date|string|None|False|Response target date|2022-11-15T14:00:00.000+0200|
|Target Date|string|None|False|Target date|2022-11-15T14:00:00.000+0200|
  
**operator**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Operator identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Name|string|None|False|Operator name|Example Operator|
|Status|string|None|False|Operator status|operator|
  
**supplier**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|For First Line|boolean|None|False|Whether the supplier is for first line|False|
|For Second Line|boolean|None|False|Whether the supplier is for second line|False|
|ID|string|None|False|Supplier identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Name|string|None|False|Supplier name|Example Supplier|
  
**processingStatus**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Processing status identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Name|string|None|False|Processing status name|Registered|
  
**majorCallObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Major call ID|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Major Incident|boolean|None|False|Whether the incident is major|False|
|Name|string|None|False|Major call name|example|
|Status|integer|None|False|Major call status|2|
  
**externalLink**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Date|string|None|False|Date of the last synchronization|2022-11-15T14:00:00.000+0200|
|ID|string|None|False|The identifier of the field|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Type|string|None|False|Number to identify the external system by|11|
  
**link**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Link|string|None|False|Link|/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f|
  
**incident**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|The list endpoint where the separate action entries can be retrieved with HTML formatting|<b>example action</b>|
|Actual Duration|integer|None|False|Actual duration of the incident in minutes|2|
|Archiving Reason|fieldObject|None|False|Reason for archiving the incident|{}|
|Asset|asset|None|False|Asset|{}|
|Attachments|string|None|False|The list endpoint where the attachments can be retrieved|/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments|
|Branch|branch|None|False|Branch for location|{}|
|Branch Extra Field A|fieldObject|None|False|The extraA field of the caller branch|{}|
|Branch Extra Field B|fieldObject|None|False|The extraA field of the caller branch|{}|
|Brief Description|string|None|False|Brief description|Example description|
|Call Date|string|None|False|Call date of the incident|2022-11-15T14:00:00.000+0200|
|Call Type|fieldObject|None|False|Call type|{}|
|Caller|caller|None|False|Caller|{}|
|Caller Branch|branch|None|False|The branch of the caller|{}|
|Caller Location|fieldObject|None|False|The location of the caller|{}|
|Category|fieldObject|None|False|Category|{}|
|Closed|boolean|None|False|Whether the incident is closed|False|
|Closed Date|string|None|False|Date when incident was closed|2022-11-15T14:00:00.000+0200|
|Closure Code|fieldObject|None|False|Closure code of the incident|{}|
|Completed|boolean|None|False|Whether the incident is completed|False|
|Completed Date|string|None|False|Date when incident was completed|2022-11-15T14:00:00.000+0200|
|Costs|float|None|False|Costs|12.5|
|Creation Date|string|None|False|Creation date|2022-11-15T14:00:00.000+0200|
|Creator|fieldObject|None|False|Incident creator|{}|
|Duration|fieldObject|None|False|Duration identifier or name|{}|
|Entry Type|fieldObject|None|False|Entry type|{}|
|Escalation Operator|fieldObject|None|False|Escalation operator of the incident|{}|
|Escalation Reason|fieldObject|None|False|Escalation reason of the incident|{}|
|Escalation Status|string|None|False|Escalation status|Escalated|
|Expected Time Spent|integer|None|False|Expected time spent on the incident|2|
|External Links|[]externalLink|None|False|Array of links to an external systems|[]|
|External Number|string|None|False|External number|test_123|
|Feedback Message|string|None|False|Feedback message of the incident|Great job!|
|Feedback Rating|integer|None|False|Rate incident|5|
|ID|string|None|False|The identifier of the incident|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Impact|fieldObject|None|False|Impact identifier or name|{}|
|Item Costs|float|None|False|Item costs|12.5|
|Location|location|None|False|Location of the incident|{}|
|Main Incident|fieldObject|None|False|The identifier or name of the main incident|{}|
|Major Call|boolean|None|False|Whether the incident is a major call|True|
|Major Call Object|majorCallObject|None|False|Major call object|{}|
|Modification Date|string|None|False|Date of last modification|2022-11-15T14:00:00.000+0200|
|Modifier|fieldObject|None|False|Modifier|{}|
|Monitored|boolean|None|False|Whether the incident is monitored|False|
|Number|string|None|False|Incident number|I 2301 004|
|Object|incidentObject|None|False|Object name or identifier|{}|
|Object Costs|float|None|False|Object costs|12.5|
|On Hold|boolean|None|False|Whether incident is on hold|False|
|On Hold Date|string|None|False|Date when incident was set as on hold|2022-11-15T14:00:00.000+0200|
|On Hold Duration|integer|None|False|Time registered on this incident since it was set to on hold|1|
|Operator|operator|None|False|Operator of the incident|{}|
|Operator Group|fieldObject|None|False|Operator group of the object|{}|
|Optional Fields 1|object|None|False|Optional fields 1|{}|
|Optional Fields 2|object|None|False|Optional fields 2|{}|
|Partial Incidents|[]link|None|False|Array of links to the partial incidents|[]|
|Priority|fieldObject|None|False|Priority identifier or name|{}|
|Processing Status|processingStatus|None|False|Processing status of the incident|{}|
|Publish to Self Service Desk|boolean|None|False|Whether the incident should be published to the Self Service Desk|False|
|Request|string|None|False|The request text that caused the incident without any formatting|<b>example request</b>|
|Requests|string|None|False|The list endpoint where the separate request entries can be retrieved with HTML formatting|/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests|
|Responded|boolean|None|False|Whether the incident is responded|False|
|Response Date|string|None|False|Response date|2022-11-15T14:00:00.000+0200|
|SLA|slaObject|None|False|SLA identifier|{}|
|Status|string|None|False|Status of the incident|firstLine|
|Subcategory|fieldObject|None|False|Subcategory name or identifier|{}|
|Supplier|supplier|None|False|Supplier of the incident|{}|
|Target Date|string|None|False|Target date|2022-11-15T14:00:00.000+0200|
|Time Spent|integer|None|False|The total time registered on this incident in minutes|2|
|Time Spent First Line|integer|None|False|Time registered on this incident while it was a 1st line incident in minutes|2|
|Time Spent Linked Partials|integer|None|False|Time registered on partials belonging to this incident in minutes|2|
|Time Spent Partial|integer|None|False|Time registered on this incident while it was a partial incident in minutes|2|
|Time Spent Second Line|integer|None|False|Time registered on this incident while it was a 2nd line incident in minutes|2|
|Urgency|fieldObject|None|False|Urgency identifier or name|{}|
  
**supplierOutput**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|For Change Management|boolean|None|False|Whether the supplier is for change management|False|
|For First Line|boolean|None|False|Whether the supplier is for first line|False|
|For Operational Activity|boolean|None|False|Whether the supplier is for operational activity|False|
|For Second Line|boolean|None|False|Whether the supplier is for second line|False|
|For Service|boolean|None|False|Whether the supplier is for service|False|
|ID|string|None|False|Supplier identifier|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Name|string|None|False|Supplier name|Example Supplier|
  
**callerInput**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Caller Branch|string|None|False|Branch identifier of the caller|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Caller Budget Holder|string|None|False|Budget holder name of the caller|IT|
|Caller Department|string|None|False|Department name of the caller|Management|
|Caller Name|string|None|False|Name of the caller. Can only be changed for unregistered callers|Maxine Rogers|
|Caller Email|string|None|False|Email address of the caller|user@example.com|
|Caller Location|string|None|False|Location identifier of the caller|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|Caller Phone Number|string|None|False|Mobile phone number of the caller|123123123|
|Caller Extra Field A|string|None|False|Caller extra field A of the caller by name|Internal application|
|Caller Extra Field B|string|None|False|Caller extra field B of the caller by name|Hired|
|Caller Phone Number|string|None|False|Phone number of the caller|123123123|
  
**accessRole**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|False|HREF|None|
|Type|string|None|False|Type|None|
  
**optionalField**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Boolean 1|boolean|None|False|Optional boolean field|None|
|Boolean 2|boolean|None|False|Optional boolean field|None|
|Boolean 3|boolean|None|False|Optional boolean field|None|
|Boolean 4|boolean|None|False|Optional boolean field|None|
|Boolean 5|boolean|None|False|Optional boolean field|None|
|Date 1|string|None|False|Optional date field|None|
|Date 2|string|None|False|Optional date field|None|
|Date 3|string|None|False|Optional date field|None|
|Date 4|string|None|False|Optional date field|None|
|Date 5|string|None|False|Optional date field|None|
|Memo 1|string|None|False|Optional memo field|None|
|Memo 2|string|None|False|Optional memo field|None|
|Memo 3|string|None|False|Optional memo field|None|
|Memo 4|string|None|False|Optional memo field|None|
|Memo 5|string|None|False|Optional memo field|None|
|Number 1|integer|None|False|Optional number field|None|
|Number 2|integer|None|False|Optional number field|None|
|Number 3|integer|None|False|Optional number field|None|
|Number 4|integer|None|False|Optional number field|None|
|Number 5|integer|None|False|Optional number field|None|
|Search List 1|string|None|False|Optional search list field|None|
|Search List 2|string|None|False|Optional search list field|None|
|Search List 3|string|None|False|Optional search list field|None|
|Search List 4|string|None|False|Optional search list field|None|
|Search List 5|string|None|False|Optional search list field|None|
|Text 1|string|None|False|Optional text field|None|
|Text 2|string|None|False|Optional text field|None|
|Text 3|string|None|False|Optional text field|None|
|Text 4|string|None|False|Optional text field|None|
|Text 5|string|None|False|Optional text field|None|
  
**operatorOutput**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access Roles|[]accessRole|None|False|Access roles|None|
|Account Manager|boolean|None|False|Account manager|None|
|Account Type|string|None|False|Account type|None|
|Attention|fieldObject|None|False|Attention|None|
|Birth Name|string|None|False|Birth name|None|
|Branch|branch|None|False|Branch|None|
|Budget Holder|fieldObject|None|False|Budget holder|None|
|Change Activities Operator|boolean|None|False|Change Activities operator|None|
|Change Coordinator|boolean|None|False|Change coordinator|None|
|Comments|string|None|False|Comments|None|
|Contract Manager|boolean|None|False|Contract manager|None|
|Creation Date|string|None|False|Creation date|None|
|Creator|fieldObject|None|False|Creator|None|
|Department|fieldObject|None|False|Department|None|
|Dynamic Name|string|None|False|Dynamic name|None|
|Email|string|None|False|Email|None|
|Employee Number|string|None|False|Employee number|None|
|Exchange Account|string|None|False|Exchange account|None|
|Extensive Change Operator|boolean|None|False|Extensive change operator|None|
|External HelpDesk party|boolean|None|False|External helpdesk party|None|
|First Lane Call Operator|boolean|None|False|First lane call operator|None|
|Firstname|string|None|False|Firstname|None|
|Gender|string|None|False|Gender|None|
|Has Attention|boolean|None|False|Has attention|None|
|Hourly Rate|integer|None|False|Hourly rate|None|
|ID|string|None|False|Operator identifier|None|
|Initials|string|None|False|Initials|None|
|Installer|boolean|None|False|Installer|None|
|Job Title|string|None|False|Job title|None|
|Knowledge Base Manager|boolean|None|False|Knowledge base manager|None|
|Language|fieldObject|None|False|Language|None|
|Location|location|None|False|Location|None|
|Login Name|string|None|False|Login name|None|
|Login Permission|boolean|None|False|Login permission|None|
|Mainframe Login Name|string|None|False|Mainframe login name|None|
|Mobile Number|string|None|False|Mobile number|None|
|Modification Date|string|None|False|Modification date|None|
|Modifier|fieldObject|None|False|Modifier|None|
|Network Login Name|string|None|False|Network login name|None|
|Operations Manager|boolean|None|False|Operations manager|None|
|Operations Operator|boolean|None|False|Operations operator|None|
|Optional Field 1|optionalField|None|False|Optional field 1|None|
|Optional Field 2|optionalField|None|False|Optional field 2|None|
|Planning Activity Manager|boolean|None|False|Planning activity manager|None|
|Prefixes|string|None|False|Prefixes|None|
|Principal ID|string|None|False|Principal identifier|None|
|Problem Manager|boolean|None|False|Problem manager|None|
|Problem Operator|boolean|None|False|Problem operator|None|
|Project Activities Operator|boolean|None|False|Project activities operator|None|
|Project Coordinator|boolean|None|False|Project coordinator|None|
|Request for Change Operator|boolean|None|False|Request for change operator|None|
|Reservations Operator|boolean|None|False|Reservations operator|None|
|Scenario Manager|boolean|None|False|Scenario manager|None|
|Second Lane Call Operator|boolean|None|False|Second lane call operator|None|
|Service Operator|boolean|None|False|Service operator|None|
|Status|string|None|False|Status|None|
|Stock Manager|boolean|None|False|Stock manager|None|
|Surname|string|None|False|Surname|None|
|Telephone|string|None|False|Telephone|None|
|title|string|None|False|Title|None|
  
**operatorGroup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access Roles|[]accessRole|None|False|Access roles|None|
|Account Manager|boolean|None|False|Account manager|None|
|Branch|branch|None|False|Branch|None|
|Budget Holder|fieldObject|None|False|Budget holder|None|
|Change Activities Operator|boolean|None|False|Change Activities operator|None|
|Change Coordinator|boolean|None|False|Change coordinator|None|
|Contact|operatorOutput|None|False|Contact|None|
|Contract Manager|boolean|None|False|Contract manager|None|
|Creation Date|string|None|False|Creation date|None|
|Creator|fieldObject|None|False|Creator|None|
|Extensive Change Operator|boolean|None|False|Extensive change operator|None|
|External HelpDesk party|boolean|None|False|External helpdesk party|None|
|First Lane Call Operator|boolean|None|False|First lane call operator|None|
|Group Name|string|None|False|Operator group name|None|
|Hourly Rate|integer|None|False|Hourly rate|None|
|ID|string|None|False|Operator group identifier|None|
|Installer|boolean|None|False|Installer|None|
|Knowledge Base Manager|boolean|None|False|Knowledge base manager|None|
|Location|location|None|False|Location|None|
|Modification Date|string|None|False|Modification date|None|
|Modifier|fieldObject|None|False|Modifier|None|
|Operations Manager|boolean|None|False|Operations manager|None|
|Operations Operator|boolean|None|False|Operations operator|None|
|Optional Field 1|optionalField|None|False|Optional field 1|None|
|Optional Field 2|optionalField|None|False|Optional field 2|None|
|Planning Activity Manager|boolean|None|False|Planning activity manager|None|
|Preset|string|None|False|Preset|None|
|Principal ID|string|None|False|Principal identifier|None|
|Problem Manager|boolean|None|False|Problem manager|None|
|Problem Operator|boolean|None|False|Problem operator|None|
|Project Activities Operator|boolean|None|False|Project activities operator|None|
|Project Coordinator|boolean|None|False|Project coordinator|None|
|Request for Change Operator|boolean|None|False|Request for change operator|None|
|Reservations Operator|boolean|None|False|Reservations operator|None|
|Scenario Manager|boolean|None|False|Scenario manager|None|
|Second Lane Call Operator|boolean|None|False|Second lane call operator|None|
|Service Operator|boolean|None|False|Service operator|None|
|Status|string|None|False|Operator group status|None|
|Stock Manager|boolean|None|False|Stock manager|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.1.0 - `Create Incident`: Changed required for `status` to False. Updated action to remove `responded` when `status` is set.
* 1.0.0 - Initial plugin | Add List Incidents, Create Incident, Get Incident by ID, Get Incident by Number, Update Incident by ID, Update Incident by Number, List Operators, List Operator Groups, List Suppliers, List Locations and Branches actions

# Links

* [TopDesk](https://www.topdesk.com/en/)

## References

* [TopDesk Tutorial](https://developers.topdesk.com/tutorial.html)