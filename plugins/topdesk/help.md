# Description

TopDesk is a cloud/on-premise ticketing system that focuses on ease of use and extensibility

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|TopDesk username used for login and password generated in the 'Application passwords' section|None|{"username": "user", "password": "44d88612-fea8-a8f3-6de8-2e1278abb02f"}|
|domain|string|None|True|Domain|None|rapid7|

Example input:

```
{
  "credentials": {
    "username": "user",
    "password": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
  },
  "domain": "rapid7"
}
```

## Technical Details

### Actions

#### List Locations and Branches

This action is used to get a list of locations with branches.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|pageSize|integer|None|False|The maximum number of locations to be returned. Default is unlimited|None|100|
|query|string|None|False|A FIQL search expression to filter the result|None|branch.name=='Example Branch'|

Example input:

```
{
  "pageSize": 100,
  "query": "branch.name=='Example Branch'"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|locationsAndBranches|[]location|False|List of the locations with branches|[]|

Example output:

```
{
  "locationsAndBranches":[
    {
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb021",
      "name":"1st Floor",
      "branch":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb021",
        "name":"Example Branch"
      }
    }
  ]
}
```

#### Get Incident by Number

This action returns an incident by number.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incidentNumber|string|None|True|Number of the incident|None|I 2301 004|

Example input:

```
{
  "incidentNumber": "I 2301 004"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|incident|incident|False|Information about the given incident|{}|

Example output:

```
{
  "incident": {
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "status": "secondLine",
    "number": "I 2301 004",
    "request": "16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request",
    "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "caller": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "dynamicName": "Example User",
      "phoneNumber": "2222222",
      "mobileNumber": "1111111",
      "email": "user@example.com",
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Berlin"
      }
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
    "briefDescription": "Example description",
    "externalNumber": "test_123",
    "category": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Hardware"
    },
    "subcategory": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Monitor"
    },
    "callType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Failure"
    },
    "entryType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Chat"
    },
    "object": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "OBJ001"
    },
    "asset": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
    },
    "impact": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Person"
    },
    "urgency": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Normal"
    },
    "priority": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "P1"
    },
    "duration": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "1 week"
    },
    "targetDate": "2022-11-15T14:00:00.000+0200",
    "onHold": false,
    "operator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "status": "operator",
      "name": "Example Operator"
    },
    "operatorGroup": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Application management"
    },
    "supplier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "DELL",
      "forFirstLine": true,
      "forSecondLine": true
    },
    "processingStatus": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Registered"
    },
    "responded": false,
    "completed": false,
    "closed": false,
    "costs": 249.9900,
    "callDate": "2022-11-15T14:00:00.000+0200",
    "creator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "creationDate": "2022-11-15T14:00:00.000+0200",
    "modifier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "modificationDate": "2022-11-15T14:00:00.000+0200",
    "majorCall": true,
    "publishToSsd": false,
    "monitored": false,
    "expectedTimeSpent": 120,
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
    }
  }
}
```

#### Get Incident by ID

This action returns an incident by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The identifier of the incident to be returned|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|

Example input:

```
{
  "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|incident|incident|False|Information about the given incident|{}|

Example output:

```
{
  "incident": {
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "status": "secondLine",
    "number": "I 2301 004",
    "request": "16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request",
    "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "caller": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "dynamicName": "Example User",
      "phoneNumber": "2222222",
      "mobileNumber": "1111111",
      "email": "user@example.com",
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Berlin"
      }
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
    "briefDescription": "Example description",
    "externalNumber": "test_123",
    "category": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Hardware"
    },
    "subcategory": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Monitor"
    },
    "callType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Failure"
    },
    "entryType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Chat"
    },
    "object": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "OBJ001"
    },
    "asset": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
    },
    "impact": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Person"
    },
    "urgency": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Normal"
    },
    "priority": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "P1"
    },
    "duration": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "1 week"
    },
    "targetDate": "2022-11-15T14:00:00.000+0200",
    "onHold": false,
    "operator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "status": "operator",
      "name": "Example Operator"
    },
    "operatorGroup": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Application management"
    },
    "supplier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "DELL",
      "forFirstLine": true,
      "forSecondLine": true
    },
    "processingStatus": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Registered"
    },
    "responded": false,
    "completed": false,
    "closed": false,
    "costs": 249.9900,
    "callDate": "2022-11-15T14:00:00.000+0200",
    "creator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "creationDate": "2022-11-15T14:00:00.000+0200",
    "modifier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "modificationDate": "2022-11-15T14:00:00.000+0200",
    "majorCall": true,
    "publishToSsd": false,
    "monitored": false,
    "expectedTimeSpent": 120,
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
    }
  }
}
```

#### Update Incident by Number

This action updates an incident by number. It doesn't reset fields that are not included in input.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|False|Initial action|None|<b>example action</b>|
|actionInvisibleForCaller|boolean|None|False|Whether the initial action is invisible for callers|None|False|
|branch|string|None|False|Branch identifier for location. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|briefDescription|string|None|False|Brief description of the incident. For partials, if not provided, will be automatically copied from the main incident|None|Example description|
|callDate|date|None|False|The date when this call was registered|None|2022-11-15T14:00:00.000+0200|
|callType|string|None|False|The type of the call. Cannot be provided for partials as its automatically copied from the main incident|None|Failure|
|caller|callerInput|None|False|The caller contact details for this incident. Is filled in automatically for persons and when the callerLookup parameter is provided|None|{"branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "budgetHolder": "Management"," department": "Management", "dynamicName": "Example User", "email": "user@example.com", "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "mobileNumber": "1111111", "phoneNumber": "2222222"}|
|callerLookup|string|None|False|Caller email for filling in a registered caller's contact details|None|user@example.com|
|category|string|None|False|The name of the category. For partials, if not provided, will be automatically copied from the main incident|None|Hardware|
|closed|boolean|None|False|Whether the incident is closed|None|False|
|closedDate|date|None|False|Closed date|None|2022-11-15T14:00:00.000+0200|
|closureCode|string|None|False|Name of the closure code|None|Manual|
|completed|boolean|None|False|Whether the incident is completed|None|False|
|completedDate|date|None|False|Completed date|None|2022-11-15T14:00:00.000+0200|
|costs|float|None|False|Costs|None|12.5|
|duration|string|None|False|Duration name|None|1 week|
|entryType|string|None|False|The type of the entry|None|Chat|
|externalNumber|string|None|False|External number. For partials, if not provided, will be automatically copied from the main incident|None|test_123|
|feedbackMessage|string|None|False|Feedback message of the incident, only available for closed incidents|None|Great job!|
|feedbackRating|integer|None|False|Rate incident, only available for closed incidents|None|5|
|impact|string|None|False|Name of the impact. Cannot be provided for partials as its automatically copied from the main incident|None|Person|
|location|string|None|False|Location identifier. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|majorCall|boolean|None|False|Whether the incident is a major call|None|True|
|majorCallObject|string|None|False|Number of the major call incident to which you want to link the updated incident|None|I 2301 104|
|number|string|None|True|Number of the incident|None|I 2301 004|
|object|string|None|False|Name of the object. For partial incidents, this field is determined by the main incident and will give an error if provided. If both object and location are given, object is set and location is ignored|None|OBJ001|
|onHold|boolean|None|False|Whether incident is on hold|None|False|
|operator|string|None|False|Operator identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|operatorGroup|string|None|False|Operator group identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|optionalFields1|object|None|False|Optional Fields 1|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00.000+0200"}|
|optionalFields2|object|None|False|Optional Fields 2|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00.000+0200"}|
|priority|string|None|False|Name of the priority. Cannot be provided for partials as it is automatically copied from the main incident. Will be automatically filled in if you provide impact and/or urgency leading to a unique priority according to your priority matrix, and don't provide a priority. For incidents with a linked SLA, if the priority provided cannot be found in the Service Level Priority List, the duration field of the incident will be emptied|None|P1|
|processingStatus|string|None|False|Processing status name|None|Registered|
|publishToSsd|boolean|None|False|Whether the incident should be published in the Self Service Desk. Only major incidents can be published|None|False|
|request|string|None|False|Initial request that caused the incident|None|<b>example request</b>|
|responded|boolean|None|False|Whether the incident is responded|None|False|
|responseDate|date|None|False|Response date. Will automatically be set to current date if left out and 'responded' is set to 'true'|None|2022-11-15T14:00:00.000+0200|
|sla|string|None|False|SLA identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|subcategory|string|None|False|The name of the subcategory. For partials, if not provided, will be automatically copied from the main incident. If a subcategory is provided without a category, the corresponding category will be filled in automatically, unless there are multiple matching categories, in which case the action will fail|None|Laptop|
|supplier|string|None|False|Supplier identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|targetDate|date|None|False|Target date|None|2022-11-15T14:00:00.000+0200|
|urgency|string|None|False|Name of the urgency. Cannot be provided for partials as its automatically copied from the main incident|None|Normal|

Example input:

```
{
  "action": "<b>example action</b>",
  "actionInvisibleForCaller": false,
  "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "briefDescription": "Example description",
  "callDate": "2022-11-15T14:00:00.000+0200",
  "callType": "Failure",
  "caller": {
    "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "budgetHolder": "Management",
    "department": "Management",
    "email": "user@example.com",
    "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "mobileNumber": "1111111",
    "phoneNumber": "2222222"
  },
  "callerLookup": "user@example.com",
  "category": "Hardware",
  "closed": false,
  "closedDate": "2022-11-15T14:00:00.000+0200",
  "closureCode": "Manual",
  "completed": false,
  "completedDate": "2022-11-15T14:00:00.000+0200",
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
    "text1": "example value",
    "date1": "2022-11-15T14:00:00.000+0200"
  },
  "optionalFields2": {
    "boolean1": true,
    "text1": "example value",
    "date1": "2022-11-15T14:00:00.000+0200"
  },
  "priority": "P1",
  "processingStatus": "Registered",
  "publishToSsd": false,
  "request": "Example request",
  "responded": false,
  "responseDate": "2022-11-15T14:00:00.000+0200",
  "sla": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "subcategory": "Monitor",
  "supplier": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "targetDate": "2022-11-15T14:00:00.000+0200",
  "urgency": "Normal"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|incident|incident|False|Information about the updated incident|{}|

Example output:

```
{
  "incident": {
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "status": "secondLine",
    "number": "I 2301 004",
    "request": "16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request",
    "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "caller": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "dynamicName": "Example User",
      "phoneNumber": "2222222",
      "mobileNumber": "1111111",
      "email": "user@example.com",
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Berlin"
      }
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
    "briefDescription": "Example description",
    "externalNumber": "test_123",
    "category": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Hardware"
    },
    "subcategory": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Monitor"
    },
    "callType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Failure"
    },
    "entryType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Chat"
    },
    "object": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "OBJ001"
    },
    "asset": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
    },
    "impact": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Person"
    },
    "urgency": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Normal"
    },
    "priority": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "P1"
    },
    "duration": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "1 week"
    },
    "targetDate": "2022-11-15T14:00:00.000+0200",
    "onHold": false,
    "operator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "status": "operator",
      "name": "Example Operator"
    },
    "operatorGroup": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Application management"
    },
    "supplier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "DELL",
      "forFirstLine": true,
      "forSecondLine": true
    },
    "processingStatus": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Registered"
    },
    "responded": false,
    "completed": false,
    "closed": false,
    "costs": 249.9900,
    "callDate": "2022-11-15T14:00:00.000+0200",
    "creator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "creationDate": "2022-11-15T14:00:00.000+0200",
    "modifier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "modificationDate": "2022-11-15T14:00:00.000+0200",
    "majorCall": true,
    "publishToSsd": false,
    "monitored": false,
    "expectedTimeSpent": 120,
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
    }
  }
}
```

#### Update Incident by ID

This action updates an incident by identifier. It doesn't reset fields that are not included in input.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|False|Initial action|None|<b>example action</b>|
|actionInvisibleForCaller|boolean|None|False|Whether the initial action is invisible for callers|None|False|
|branch|string|None|False|Branch identifier for location. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|briefDescription|string|None|False|Brief description of the incident. For partials, if not provided, will be automatically copied from the main incident|None|Example description|
|callDate|date|None|False|The date when this call was registered|None|2022-11-15T14:00:00.000+0200|
|callType|string|None|False|The type of the call. Cannot be provided for partials as its automatically copied from the main incident|None|Failure|
|caller|callerInput|None|False|The caller contact details for this incident. Is filled in automatically for persons and when the callerLookup parameter is provided|None|{"branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "budgetHolder": "Management"," department": "Management", "dynamicName": "Example User", "email": "user@example.com", "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "mobileNumber": "1111111", "phoneNumber": "2222222"}|
|callerLookup|string|None|False|Caller email for filling in a registered caller's contact details|None|user@example.com|
|category|string|None|False|The name of the category. For partials, if not provided, will be automatically copied from the main incident|None|Hardware|
|closed|boolean|None|False|Whether the incident is closed|None|False|
|closedDate|date|None|False|Closed date|None|2022-11-15T14:00:00.000+0200|
|closureCode|string|None|False|Name of the closure code|None|Manual|
|completed|boolean|None|False|Whether the incident is completed|None|False|
|completedDate|date|None|False|Completed date|None|2022-11-15T14:00:00.000+0200|
|costs|float|None|False|Costs|None|12.5|
|duration|string|None|False|Duration name|None|1 week|
|entryType|string|None|False|The type of the entry|None|Chat|
|externalNumber|string|None|False|External number. For partials, if not provided, will be automatically copied from the main incident|None|test_123|
|feedbackMessage|string|None|False|Feedback message of the incident, only available for closed incidents|None|Great job!|
|feedbackRating|integer|None|False|Rate incident, only available for closed incidents|None|5|
|id|string|None|True|Identifier of the incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|impact|string|None|False|Name of the impact. Cannot be provided for partials as its automatically copied from the main incident|None|Person|
|location|string|None|False|Location identifier. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|majorCall|boolean|None|False|Whether the incident is a major call|None|True|
|majorCallObject|string|None|False|Number of the major call incident to which you want to link the updated incident|None|I 2301 104|
|object|string|None|False|Name of the object. For partial incidents, this field is determined by the main incident and will give an error if provided. If both object and location are given, object is set and location is ignored|None|OBJ001|
|onHold|boolean|None|False|Whether incident is on hold|None|False|
|operator|string|None|False|Operator identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|operatorGroup|string|None|False|Operator group identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|optionalFields1|object|None|False|Optional Fields 1|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00.000+0200"}|
|optionalFields2|object|None|False|Optional Fields 2|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00.000+0200"}|
|priority|string|None|False|Name of the priority. Cannot be provided for partials as it is automatically copied from the main incident. Will be automatically filled in if you provide impact and/or urgency leading to a unique priority according to your priority matrix, and don't provide a priority. For incidents with a linked SLA, if the priority provided cannot be found in the Service Level Priority List, the duration field of the incident will be emptied|None|P1|
|processingStatus|string|None|False|Processing status name|None|Registered|
|publishToSsd|boolean|None|False|Whether the incident should be published in the Self Service Desk. Only major incidents can be published|None|False|
|request|string|None|False|Initial request that caused the incident|None|<b>example request</b>|
|responded|boolean|None|False|Whether the incident is responded|None|False|
|responseDate|date|None|False|Response date. Will automatically be set to current date if left out and 'responded' is set to 'true'|None|2022-11-15T14:00:00.000+0200|
|sla|string|None|False|SLA identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|subcategory|string|None|False|The name of the subcategory. For partials, if not provided, will be automatically copied from the main incident. If a subcategory is provided without a category, the corresponding category will be filled in automatically, unless there are multiple matching categories, in which case the action will fail|None|Laptop|
|supplier|string|None|False|Supplier identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|targetDate|date|None|False|Target date|None|2022-11-15T14:00:00.000+0200|
|urgency|string|None|False|Name of the urgency. Cannot be provided for partials as its automatically copied from the main incident|None|Normal|

Example input:

```
{
  "action": "<b>example action</b>",
  "actionInvisibleForCaller": false,
  "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "briefDescription": "Example description",
  "callDate": "2022-11-15T14:00:00.000+0200",
  "callType": "Failure",
  "caller": {
    "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "budgetHolder": "Management",
    "department": "Management",
    "email": "user@example.com",
    "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "mobileNumber": "1111111",
    "phoneNumber": "2222222"
  },
  "callerLookup": "user@example.com",
  "category": "Hardware",
  "closed": false,
  "closedDate": "2022-11-15T14:00:00.000+0200",
  "closureCode": "Manual",
  "completed": false,
  "completedDate": "2022-11-15T14:00:00.000+0200",
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
    "text1": "example value",
    "date1": "2022-11-15T14:00:00.000+0200"
  },
  "optionalFields2": {
    "boolean1": true,
    "text1": "example value",
    "date1": "2022-11-15T14:00:00.000+0200"
  },
  "priority": "P1",
  "processingStatus": "Registered",
  "publishToSsd": false,
  "request": "Example request",
  "responded": false,
  "responseDate": "2022-11-15T14:00:00.000+0200",
  "sla": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "subcategory": "Monitor",
  "supplier": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "targetDate": "2022-11-15T14:00:00.000+0200",
  "urgency": "Normal"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|incident|incident|False|Information about the updated incident|{}|

Example output:

```
{
  "incident": {
    "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "status": "secondLine",
    "number": "I 2301 004",
    "request": "16-11-2022 18:10 [GMT +0:00] Example Operator: \nExample request\n\n16-11-2022 14:40 [GMT +0:00] Example Operator: \nTest request",
    "requests": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "action": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "attachments": "/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "caller": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "dynamicName": "Example User",
      "phoneNumber": "2222222",
      "mobileNumber": "1111111",
      "email": "user@example.com",
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Berlin"
      }
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
    "briefDescription": "Example description",
    "externalNumber": "test_123",
    "category": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Hardware"
    },
    "subcategory": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Monitor"
    },
    "callType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Failure"
    },
    "entryType": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Chat"
    },
    "object": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "OBJ001"
    },
    "asset": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
    },
    "impact": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Person"
    },
    "urgency": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Normal"
    },
    "priority": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "P1"
    },
    "duration": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "1 week"
    },
    "targetDate": "2022-11-15T14:00:00.000+0200",
    "onHold": false,
    "operator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "status": "operator",
      "name": "Example Operator"
    },
    "operatorGroup": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Application management"
    },
    "supplier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "DELL",
      "forFirstLine": true,
      "forSecondLine": true
    },
    "processingStatus": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Registered"
    },
    "responded": false,
    "completed": false,
    "closed": false,
    "costs": 249.9900,
    "callDate": "2022-11-15T14:00:00.000+0200",
    "creator": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "creationDate": "2022-11-15T14:00:00.000+0200",
    "modifier": {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name": "Example Operator"
    },
    "modificationDate": "2022-11-15T14:00:00.000+0200",
    "majorCall": true,
    "publishToSsd": false,
    "monitored": false,
    "expectedTimeSpent": 120,
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
    }
  }
}
```

#### List Operators

This action is used to get a list of operators.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Only include these specific fields in the response. The default is that all fields are included|None|id,dynamicName|
|pageSize|integer|None|False|The amount of operators to be returned per page. Must be between 1 and 100|None|100|
|query|string|None|False|A FIQL search expression to filter the result|None|dynamicName=='Test User'|
|start|integer|None|False|The offset at which to start listing the operators at. Must be greater or equal to 0|None|0|

Example input:

```
{
  "pageSize": 100,
  "query": "dynamicName=='Test User'",
  "start": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|operators|[]operatorOutput|False|List of the operators|[]|

Example output:

```
{
  "operators": [
    {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "principalId": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "status": "operator",
      "accountType": "regular",
      "surName": "User",
      "firstName": "Test",
      "dynamicName": "Test User",
      "initials": "T.",
      "title": "Mrs",
      "gender": "FEMALE",
      "language": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "English"
      },
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Dublin"
      },
      "location": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "branch": {
          "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
          "name": "Example branch",
          "timeZone": "Europe/Dublin"
        },
        "name": "Example location",
        "room": "Test room"
      },
      "telephone": "111111111",
      "email": "user@example.com",
      "exchangeAccount": "user@example.com",
      "loginName": "TEST",
      "loginPermission": true,
      "jobTitle": "Application Manager",
      "department": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "IT"
      },
      "hasAttention": false,
      "installer": true,
      "firstLineCallOperator": true,
      "secondLineCallOperator": true,
      "problemManager": true,
      "problemOperator": true,
      "changeCoordinator": true,
      "changeActivitiesOperator": true,
      "requestForChangeOperator": true,
      "extensiveChangeOperator": true,
      "simpleChangeOperator": true,
      "scenarioManager": true,
      "planningActivityManager": true,
      "projectCoordinator": true,
      "projectActiviesOperator": true,
      "stockManager": true,
      "reservationsOperator": true,
      "serviceOperator": true,
      "externalHelpDeskParty": true,
      "contractManager": true,
      "operationsOperator": true,
      "operationsManager": true,
      "knowledgeBaseManager": true,
      "accountManager": false,
      "creationDate": "2020-09-29T21:08:30.000+0000",
      "creator": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Admin"
      },
      "modificationDate": "2023-01-18T04:20:14.000+0000",
      "modifier": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "SUPPORT"
      },
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
      }
    }
  ]
}
```

#### List Operator Groups

This action is used to get a list of operator groups.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Only include these specific fields in the response. The default is that all fields are included|None|id,groupName|
|pageSize|integer|None|False|The amount of operator groups to be returned per page. Must be between 1 and 100|None|100|
|query|string|None|False|A FIQL search expression to filter the result|None|groupName=='Test Group'|
|start|integer|None|False|The offset at which to start listing the operator groups at. Must be greater or equal to 0|None|0|

Example input:

```
{
  "pageSize": 100,
  "query": "groupName=='Test Group'",
  "start": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|operatorGroups|[]operatorGroup|False|List of the operator groups|[]|

Example output:

```
{
  "operatorGroups": [
    {
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "status": "operatorGroup",
      "groupName": "Test Group",
      "branch": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Example branch",
        "timeZone": "Europe/Dublin"
      },
      "contact": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "dynamicName": "Test User",
        "telephone": "111111111",
        "email": "user@example.com",
        "department": {
          "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
          "name": "IT"
        },
        "hasAttention": false,
        "loginPermission": false,
        "installer": false,
        "firstLineCallOperator": false,
        "secondLineCallOperator": false,
        "problemManager": false,
        "problemOperator": false,
        "changeCoordinator": false,
        "changeActivitiesOperator": false,
        "requestForChangeOperator": false,
        "extensiveChangeOperator": false,
        "simpleChangeOperator": false,
        "scenarioManager": false,
        "planningActivityManager": false,
        "projectCoordinator": false,
        "projectActiviesOperator": false,
        "stockManager": false,
        "reservationsOperator": false,
        "serviceOperator": false,
        "externalHelpDeskParty": false,
        "contractManager": false,
        "operationsOperator": false,
        "operationsManager": false,
        "knowledgeBaseManager": false,
        "accountManager": false
      },
      "installer": false,
      "firstLineCallOperator": true,
      "secondLineCallOperator": true,
      "problemManager": false,
      "problemOperator": false,
      "changeCoordinator": true,
      "changeActivitiesOperator": true,
      "requestForChangeOperator": false,
      "extensiveChangeOperator": false,
      "simpleChangeOperator": false,
      "scenarioManager": false,
      "planningActivityManager": false,
      "projectCoordinator": false,
      "projectActiviesOperator": true,
      "stockManager": false,
      "reservationsOperator": false,
      "serviceOperator": false,
      "externalHelpDeskParty": false,
      "contractManager": false,
      "operationsOperator": false,
      "operationsManager": false,
      "knowledgeBaseManager": true,
      "accountManager": false,
      "creationDate": "2021-11-03T15:39:54.000+0000",
      "creator": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Test User"
      },
      "modificationDate": "2021-11-03T15:39:54.000+0000",
      "modifier": {
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name": "Test User"
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
      }
    }
  ]
}
```

#### List Suppliers

This action is used to get a list of suppliers.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|pageSize|integer|None|False|The amount of suppliers to be returned per request. Must be between 1 and 100|None|100|
|query|string|None|False|A FIQL search expression to filter the result|None|name=='Example Supplier'|
|start|integer|None|False|The offset at which to start listing the suppliers at. Must be greater or equal to 0|None|0|

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
|----|----|--------|-----------|------|
|suppliers|[]supplierOutput|False|List of the suppliers|[]|

Example output:

```
{
  "suppliers": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "Example Supplier",
      "forFirstLine": false,
      "forSecondLine": false,
      "forService": false,
      "forOperationalActivity": false,
      "forChangeManagement": false
    }
  ]
}
```

#### List Incidents

This action returns a list of incidents.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|all|boolean|None|False|Whether to return partial and archived incidents|None|True|
|fields|string|None|False|A comma-separated list of which fields should be returned. By default all fields will be returned|None|id,targetDate|
|pageSize|integer|None|False|How many incidents should be returned max. Default is 10. Should be between 1 and 1000|None|5|
|pageStart|integer|None|False|The offset to start at. Default is 0|None|2|
|query|string|None|False|A FIQL string to select which incidents should be returned|None|status==secondLine;priority.name==P1|
|sort|string|None|False|The sort order of the returned incidents|None|status:asc,creationDate:desc|

Example input:

```
{
  "all": true,
  "pageSize": 5,
  "pageStart": 2,
  "query": "status==secondLine;priority.name==P1",
  "sort": "status:asc,creationDate:desc"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|incidents|[]incident|False|List of the incidents|[]|

Example output:

```
{
  "incidents":[
    {
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "status":"secondLine",
      "number":"I 2301 103",
      "request":"25-01-2023 11:14 [GMT +0:00] User Example: \nexample request",
      "requests":"/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
      "action":"/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
      "attachments":"/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
      "caller":{
        "branch":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "budgetHolder":"Management",
        "department":"Management",
        "email":"user@example.com",
        "location":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "mobileNumber":"1111111",
        "phoneNumber":"2222222"
      },
      "callerBranch":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"TOPdesk",
        "timeZone":"Europe/Dublin"
      },
      "callerLocation":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"CEO's Office"
      },
      "briefDescription":"test description",
      "category":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Hardware"
      },
      "subcategory":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Laptop"
      },
      "callType":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Failure"
      },
      "entryType":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Telephone"
      },
      "impact":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Person"
      },
      "urgency":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Normal"
      },
      "priority":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"P1"
      },
      "duration":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"8 hours"
      },
      "targetDate":"2023-01-29T13:00:00.000+0000",
      "onHold":false,
      "feedbackMessage":"Great job!",
      "feedbackRating":2,
      "operator":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "status":"operator",
        "name":"Example User"
      },
      "processingStatus":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Registered"
      },
      "responded":true,
      "responseDate":"2023-01-25T11:14:25.000+0000",
      "completed":true,
      "completedDate":"2023-01-25T11:14:25.000+0000",
      "closed":true,
      "closedDate":"2023-01-25T11:14:25.000+0000",
      "closureCode":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Manual"
      },
      "costs":12.5,
      "callDate":"2023-01-25T11:14:25.000+0000",
      "creator":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Example User"
      },
      "creationDate":"2023-01-25T11:14:25.000+0000",
      "modifier":{
        "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "name":"Example User"
      },
      "modificationDate":"2023-01-25T11:14:25.000+0000",
      "majorCall":true,
      "publishToSsd":false,
      "monitored":false,
      "optionalFields1":{
        "boolean1":false,
        "boolean2":false,
        "boolean3":false,
        "boolean4":false,
        "boolean5":false
      },
      "optionalFields2":{
        "boolean1":false,
        "boolean2":false,
        "boolean3":false,
        "boolean4":false,
        "boolean5":false,
      }
    }
  ]
}
```

#### Create Incident

This action creates an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|False|Initial action|None|<b>example action</b>|
|actionInvisibleForCaller|boolean|None|False|Whether the initial action is invisible for callers|None|False|
|branch|string|None|False|Branch identifier for location. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|briefDescription|string|None|False|Brief description of the incident. For partials, if not provided, will be automatically copied from the main incident|None|Example description|
|callType|string|None|False|The type of the call. Cannot be provided for partials as its automatically copied from the main incident|None|Failure|
|caller|callerInput|None|False|The caller contact details for this incident. Is filled in automatically for persons and when the callerLookup parameter is provided|None|{"branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "budgetHolder": "Management"," department": "Management", "dynamicName": "Example User", "email": "user@example.com", "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f", "mobileNumber": "1111111", "phoneNumber": "2222222"}|
|callerLookup|string|None|False|Caller email for filling in a registered caller's contact details|None|user@example.com|
|category|string|None|False|The name of the category. For partials, if not provided, will be automatically copied from the main incident|None|Hardware|
|closed|boolean|None|False|Whether the incident is closed|None|False|
|closedDate|date|None|False|Closed date|None|2022-11-15T14:00:00.000+0200|
|closureCode|string|None|False|The name of the closure code|None|Manual|
|completed|boolean|None|False|Whether the incident is completed|None|False|
|completedDate|date|None|False|Completed date|None|2022-11-15T14:00:00.000+0200|
|costs|float|None|False|Costs|None|12.5|
|duration|string|None|False|Duration name|None|1 week|
|entryType|string|None|False|The type of the entry|None|Chat|
|externalNumber|string|None|False|External number. For partials, if not provided, will be automatically copied from the main incident|None|test_123|
|feedbackMessage|string|None|False|Feedback message of the incident, only available for closed incidents|None|Great job!|
|feedbackRating|integer|None|False|Rate incident, only available for closed incidents|None|5|
|impact|string|None|False|The name of the impact. Cannot be provided for partials as its automatically copied from the main incident|None|Person|
|location|string|None|False|Location identifier. For partial incidents, this field is determined by the main incident and will give an error if provided|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|mainIncident|string|None|False|Main incident number, required for creating a partial incident. This must be an open, unarchived second line incident and visible to the operator|None|I 1000 123|
|majorCall|boolean|None|False|Whether the incident is a major call|None|True|
|majorCallObject|string|None|False|Number of the major call incident to which you want to link the created incident|None|I 2301 104|
|object|string|None|False|The name of the object. For partial incidents, this field is determined by the main incident and will give an error if provided. If both object and location are given, object is set and location is ignored|None|OBJ001|
|onHold|boolean|None|False|Whether incident is on hold|None|False|
|operator|string|None|False|Operator identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|operatorGroup|string|None|False|Operator group identifier. For partials, if not provided, will be automatically copied from the main incident|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|optionalFields1|object|None|False|Optional Fields 1|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00.000+0200"}|
|optionalFields2|object|None|False|Optional Fields 2|None|{"boolean1": true, "text1": "example value", "date1": "2022-11-15T14:00:00.000+0200"}|
|priority|string|None|False|The name of the priority. Cannot be provided for partials as it is automatically copied from the main incident. Will be automatically filled in if you provide impact and/or urgency leading to a unique priority according to your priority matrix, and don't provide a priority. For incidents with a linked SLA, if the priority provided cannot be found in the Service Level Priority List, the duration field of the incident will be emptied|None|P1|
|processingStatus|string|None|False|Processing status name|None|Registered|
|publishToSsd|boolean|None|False|Whether the incident should be published in the Self Service Desk. Only major incidents can be published|None|False|
|request|string|None|False|Initial request that caused the incident|None|<b>example request</b>|
|responded|boolean|None|False|Whether the incident is responded|None|False|
|responseDate|date|None|False|Response date. Will automatically be set to current date if left out and 'responded' is set to 'true'|None|https://example.com|
|sla|string|None|False|SLA identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|status|string|None|True|Status of the incident|['First Line Incident', 'Second Line Incident', 'Partial Incident']|First Line Incident|
|subcategory|string|None|False|The name of the subcategory. For partials, if not provided, will be automatically copied from the main incident. If a subcategory is provided without a category, the corresponding category will be filled in automatically, unless there are multiple matching categories, in which case the action will fail|None|Laptop|
|supplier|string|None|False|Supplier identifier|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|targetDate|date|None|False|Target date|None|2022-11-15T14:00:00.000+0200|
|urgency|string|None|False|The name of the urgency. Cannot be provided for partials as its automatically copied from the main incident|None|Normal|

Example input:

```
{
  "action": "<b>example action</b>",
  "actionInvisibleForCaller": false,
  "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "briefDescription": "Example description",
  "callType": "Failure",
  "caller": {
    "branch": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "budgetHolder": "Management",
    "department": "Management",
    "email": "user@example.com",
    "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "mobileNumber": "1111111",
    "phoneNumber": "2222222"
  },
  "callerLookup": "user@example.com",
  "category": "Hardware",
  "closed": false,
  "completed": false,
  "costs": 12.5,
  "duration": "1 week",
  "entryType": "Chat",
  "externalNumber": "test_123",
  "impact": "Person",
  "location": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "mainIncident": "I 1000 123",
  "majorCall": false,
  "object": "OBJ001",
  "onHold": false,
  "operator": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "operatorGroup": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "optionalFields1": {
    "boolean1": true,
    "text1": "example value",
    "date1": "2022-11-15T14:00:00.000+0200"
  },
  "optionalFields2": {
    "boolean1": true,
    "text1": "example value",
    "date1": "2022-11-15T14:00:00.000+0200"
  },
  "priority": "P1",
  "processingStatus": "Registered",
  "publishToSsd": false,
  "request": "<b>example request</b>",
  "responded": false,
  "sla": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "status": "First Line Incident",
  "subcategory": "Laptop",
  "supplier": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "targetDate": "2022-11-15T14:00:00.000+0200",
  "urgency": "Normal"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|incident|incident|False|Information about the created incident|{}|

Example output:

```
{
  "incident":{
    "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "status":"firstLine",
    "number":"I 2301 103",
    "request":"25-01-2023 11:14 [GMT +0:00] User Example: \nexample request",
    "requests":"/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/requests",
    "action":"/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/actions",
    "attachments":"/tas/api/incidents/id/44d88612-fea8-a8f3-6de8-2e1278abb02f/attachments",
    "caller":{
      "branch":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "budgetHolder":"Management",
      "department":"Management",
      "email":"user@example.com",
      "location":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "mobileNumber":"1111111",
      "phoneNumber":"2222222"
    },
    "callerBranch":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"TOPdesk",
      "timeZone":"Europe/Dublin"
    },
    "callerLocation":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"CEO's Office"
    },
    "briefDescription":"test description",
    "category":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"Hardware"
    },
    "subcategory":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"Laptop"
    },
    "callType":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"Failure"
    },
    "entryType":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"Chat"
    },
    "impact":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"Person"
    },
    "urgency":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"Normal"
    },
    "priority":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"P1"
    },
    "duration":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"8 hours"
    },
    "targetDate":"2023-01-29T13:00:00.000+0000",
    "onHold":false,
    "operator":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "status":"operator",
      "name":"Example User"
    },
    "processingStatus":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"Registered"
    },
    "responded":false
    "completed":false
    "closed":false
    "costs":12.5,
    "callDate":"2023-01-25T11:14:25.000+0000",
    "creator":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"Example User"
    },
    "creationDate":"2023-01-25T11:14:25.000+0000",
    "modifier":{
      "id":"44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "name":"Example User"
    },
    "modificationDate":"2023-01-25T11:14:25.000+0000",
    "majorCall":true,
    "publishToSsd":false,
    "monitored":false,
    "optionalFields1":{
      "boolean1":false,
      "boolean2":false,
      "boolean3":false,
      "boolean4":false,
      "boolean5":false
    },
    "optionalFields2":{
      "boolean1":false,
      "boolean2":false,
      "boolean3":false,
      "boolean4":false,
      "boolean5":false,
    }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### accessRole

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HREF|string|False|HREF|
|Type|string|False|Type|

#### asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Asset identifier|

#### branch

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Client Reference Number|string|False|Client reference number|
|Extra Field A|fieldObject|False|Extra field A|
|Extra Field B|fieldObject|False|Extra field B|
|ID|string|False|Caller identifier|
|Name|string|False|Branch name|
|Time Zone|string|False|Time zone of the branch|

#### caller

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Branch|branch|False|Branch of the caller|
|Budget Holder|fieldObject|False|Budget holder of the caller|
|Department|fieldObject|False|Department of the caller|
|Dynamic Name|string|False|Caller dynamic name|
|Email|string|False|Email address of the caller|
|ID|string|False|Caller identifier|
|Mobile Number|string|False|Mobile number of the caller|
|Phone Number|string|False|Phone number of the caller|

#### callerInput

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Caller Branch|string|False|Branch identifier of the caller|
|Caller Budget Holder|string|False|Budget holder name of the caller|
|Caller Department|string|False|Department name of the caller|
|Caller Name|string|False|Name of the caller. Can only be changed for unregistered callers|
|Caller Email|string|False|Email address of the caller|
|Caller Location|string|False|Location identifier of the caller|
|Caller Phone Number|string|False|Mobile phone number of the caller|
|Caller Extra Field A|string|False|Caller extra field A of the caller by name|
|Caller Extra Field B|string|False|Caller extra field B of the caller by name|
|Caller Phone Number|string|False|Phone number of the caller|

#### externalLink

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Date|string|False|Date of the last synchronization|
|ID|string|False|The identifier of the field|
|Type|string|False|Number to identify the external system by|

#### fieldObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|The identifier of the field|
|Name|string|False|Name of the field|

#### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action|string|False|The list endpoint where the separate action entries can be retrieved with HTML formatting|
|Actual Duration|integer|False|Actual duration of the incident in minutes|
|Archiving Reason|fieldObject|False|Reason for archiving the incident|
|Asset|asset|False|Asset|
|Attachments|string|False|The list endpoint where the attachments can be retrieved|
|Branch|branch|False|Branch for location|
|Branch Extra Field A|fieldObject|False|The extraA field of the caller branch|
|Branch Extra Field B|fieldObject|False|The extraA field of the caller branch|
|Brief Description|string|False|Brief description|
|Call Date|string|False|Call date of the incident|
|Call Type|fieldObject|False|Call type|
|Caller|caller|False|Caller|
|Caller Branch|branch|False|The branch of the caller|
|Caller Location|fieldObject|False|The location of the caller|
|Category|fieldObject|False|Category|
|Closed|boolean|False|Whether the incident is closed|
|Closed Date|string|False|Date when incident was closed|
|Closure Code|fieldObject|False|Closure code of the incident|
|Completed|boolean|False|Whether the incident is completed|
|Completed Date|string|False|Date when incident was completed|
|Costs|float|False|Costs|
|Creation Date|string|False|Creation date|
|Creator|fieldObject|False|Incident creator|
|Duration|fieldObject|False|Duration identifier or name|
|Entry Type|fieldObject|False|Entry type|
|Escalation Operator|fieldObject|False|Escalation operator of the incident|
|Escalation Reason|fieldObject|False|Escalation reason of the incident|
|Escalation Status|string|False|Escalation status|
|Expected Time Spent|integer|False|Expected time spent on the incident|
|External Links|[]externalLink|False|Array of links to an external systems|
|External Number|string|False|External number|
|Feedback Message|string|False|Feedback message of the incident|
|Feedback Rating|integer|False|Rate incident|
|ID|string|False|The identifier of the incident|
|Impact|fieldObject|False|Impact identifier or name|
|Item Costs|float|False|Item costs|
|Location|location|False|Location of the incident|
|Main Incident|fieldObject|False|The identifier or name of the main incident|
|Major Call|boolean|False|Whether the incident is a major call|
|Major Call Object|majorCallObject|False|Major call object|
|Modification Date|string|False|Date of last modification|
|Modifier|fieldObject|False|Modifier|
|Monitored|boolean|False|Whether the incident is monitored|
|Number|string|False|Incident number|
|Object|incidentObject|False|Object name or identifier|
|Object Costs|float|False|Object costs|
|On Hold|boolean|False|Whether incident is on hold|
|On Hold Date|string|False|Date when incident was set as on hold|
|On Hold Duration|integer|False|Time registered on this incident since it was set to on hold|
|Operator|operator|False|Operator of the incident|
|Operator Group|fieldObject|False|Operator group of the object|
|Optional Fields 1|object|False|Optional fields 1|
|Optional Fields 2|object|False|Optional fields 2|
|Partial Incidents|[]link|False|Array of links to the partial incidents|
|Priority|fieldObject|False|Priority identifier or name|
|Processing Status|processingStatus|False|Processing status of the incident|
|Publish to Self Service Desk|boolean|False|Whether the incident should be published to the Self Service Desk|
|Request|string|False|The request text that caused the incident without any formatting|
|Requests|string|False|The list endpoint where the separate request entries can be retrieved with HTML formatting|
|Responded|boolean|False|Whether the incident is responded|
|Response Date|string|False|Response date|
|SLA|slaObject|False|SLA identifier|
|Status|string|False|Status of the incident|
|Subcategory|fieldObject|False|Subcategory name or identifier|
|Supplier|supplier|False|Supplier of the incident|
|Target Date|string|False|Target date|
|Time Spent|integer|False|The total time registered on this incident in minutes|
|Time Spent First Line|integer|False|Time registered on this incident while it was a 1st line incident in minutes|
|Time Spent Linked Partials|integer|False|Time registered on partials belonging to this incident in minutes|
|Time Spent Partial|integer|False|Time registered on this incident while it was a partial incident in minutes|
|Time Spent Second Line|integer|False|Time registered on this incident while it was a 2nd line incident in minutes|
|Urgency|fieldObject|False|Urgency identifier or name|

#### incidentObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Branch|fieldObject|False|Object branch|
|ID|string|False|Object identifier|
|Location|fieldObject|False|Object location|
|Make|fieldObject|False|Make|
|Model|fieldObject|False|Object model|
|Name|string|False|Object name|
|Serial Number|string|False|Object serial number|
|Specification|string|False|Object specification|
|Type|fieldObject|False|Object type|

#### link

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Link|string|False|Link|

#### location

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Branch|branch|False|Location branch|
|ID|string|False|Location identifier|
|Name|string|False|Location name|
|Room|string|False|Location room|

#### majorCallObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Major call ID|
|Major Incident|boolean|False|Whether the incident is major|
|Name|string|False|Major call name|
|Status|integer|False|Major call status|

#### operator

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Operator identifier|
|Name|string|False|Operator name|
|Status|string|False|Operator status|

#### operatorGroup

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access Roles|[]accessRole|False|Access roles|
|Account Manager|boolean|False|Account manager|
|Branch|branch|False|Branch|
|Budget Holder|fieldObject|False|Budget holder|
|Change Activities Operator|boolean|False|Change Activities operator|
|Change Coordinator|boolean|False|Change coordinator|
|Contact|operatorOutput|False|Contact|
|Contract Manager|boolean|False|Contract manager|
|Creation Date|string|False|Creation date|
|Creator|fieldObject|False|Creator|
|Extensive Change Operator|boolean|False|Extensive change operator|
|External HelpDesk party|boolean|False|External helpdesk party|
|First Lane Call Operator|boolean|False|First lane call operator|
|Group Name|string|False|Operator group name|
|Hourly Rate|integer|False|Hourly rate|
|ID|string|False|Operator group identifier|
|Installer|boolean|False|Installer|
|Knowledge Base Manager|boolean|False|Knowledge base manager|
|Location|location|False|Location|
|Modification Date|string|False|Modification date|
|Modifier|fieldObject|False|Modifier|
|Operations Manager|boolean|False|Operations manager|
|Operations Operator|boolean|False|Operations operator|
|Optional Field 1|optionalField|False|Optional field 1|
|Optional Field 2|optionalField|False|Optional field 2|
|Planning Activity Manager|boolean|False|Planning activity manager|
|Preset|string|False|Preset|
|Principal ID|string|False|Principal identifier|
|Problem Manager|boolean|False|Problem manager|
|Problem Operator|boolean|False|Problem operator|
|Project Activities Operator|boolean|False|Project activities operator|
|Project Coordinator|boolean|False|Project coordinator|
|Request for Change Operator|boolean|False|Request for change operator|
|Reservations Operator|boolean|False|Reservations operator|
|Scenario Manager|boolean|False|Scenario manager|
|Second Lane Call Operator|boolean|False|Second lane call operator|
|Service Operator|boolean|False|Service operator|
|Status|string|False|Operator group status|
|Stock Manager|boolean|False|Stock manager|

#### operatorOutput

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access Roles|[]accessRole|False|Access roles|
|Account Manager|boolean|False|Account manager|
|Account Type|string|False|Account type|
|Attention|fieldObject|False|Attention|
|Birth Name|string|False|Birth name|
|Branch|branch|False|Branch|
|Budget Holder|fieldObject|False|Budget holder|
|Change Activities Operator|boolean|False|Change Activities operator|
|Change Coordinator|boolean|False|Change coordinator|
|Comments|string|False|Comments|
|Contract Manager|boolean|False|Contract manager|
|Creation Date|string|False|Creation date|
|Creator|fieldObject|False|Creator|
|Department|fieldObject|False|Department|
|Dynamic Name|string|False|Dynamic name|
|Email|string|False|Email|
|Employee Number|string|False|Employee number|
|Exchange Account|string|False|Exchange account|
|Extensive Change Operator|boolean|False|Extensive change operator|
|External HelpDesk party|boolean|False|External helpdesk party|
|First Lane Call Operator|boolean|False|First lane call operator|
|Firstname|string|False|Firstname|
|Gender|string|False|Gender|
|Has Attention|boolean|False|Has attention|
|Hourly Rate|integer|False|Hourly rate|
|ID|string|False|Operator identifier|
|Initials|string|False|Initials|
|Installer|boolean|False|Installer|
|Job Title|string|False|Job title|
|Knowledge Base Manager|boolean|False|Knowledge base manager|
|Language|fieldObject|False|Language|
|Location|location|False|Location|
|Login Name|string|False|Login name|
|Login Permission|boolean|False|Login permission|
|Mainframe Login Name|string|False|Mainframe login name|
|Mobile Number|string|False|Mobile number|
|Modification Date|string|False|Modification date|
|Modifier|fieldObject|False|Modifier|
|Network Login Name|string|False|Network login name|
|Operations Manager|boolean|False|Operations manager|
|Operations Operator|boolean|False|Operations operator|
|Optional Field 1|optionalField|False|Optional field 1|
|Optional Field 2|optionalField|False|Optional field 2|
|Planning Activity Manager|boolean|False|Planning activity manager|
|Prefixes|string|False|Prefixes|
|Principal ID|string|False|Principal identifier|
|Problem Manager|boolean|False|Problem manager|
|Problem Operator|boolean|False|Problem operator|
|Project Activities Operator|boolean|False|Project activities operator|
|Project Coordinator|boolean|False|Project coordinator|
|Request for Change Operator|boolean|False|Request for change operator|
|Reservations Operator|boolean|False|Reservations operator|
|Scenario Manager|boolean|False|Scenario manager|
|Second Lane Call Operator|boolean|False|Second lane call operator|
|Service Operator|boolean|False|Service operator|
|Status|string|False|Status|
|Stock Manager|boolean|False|Stock manager|
|Surname|string|False|Surname|
|Telephone|string|False|Telephone|
|Title|string|False|Title|

#### optionalField

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Boolean 1|boolean|False|Optional boolean field|
|Boolean 2|boolean|False|Optional boolean field|
|Boolean 3|boolean|False|Optional boolean field|
|Boolean 4|boolean|False|Optional boolean field|
|Boolean 5|boolean|False|Optional boolean field|
|Date 1|string|False|Optional date field|
|Date 2|string|False|Optional date field|
|Date 3|string|False|Optional date field|
|Date 4|string|False|Optional date field|
|Date 5|string|False|Optional date field|
|Memo 1|string|False|Optional memo field|
|Memo 2|string|False|Optional memo field|
|Memo 3|string|False|Optional memo field|
|Memo 4|string|False|Optional memo field|
|Memo 5|string|False|Optional memo field|
|Number 1|integer|False|Optional number field|
|Number 2|integer|False|Optional number field|
|Number 3|integer|False|Optional number field|
|Number 4|integer|False|Optional number field|
|Number 5|integer|False|Optional number field|
|Search List 1|string|False|Optional search list field|
|Search List 2|string|False|Optional search list field|
|Search List 3|string|False|Optional search list field|
|Search List 4|string|False|Optional search list field|
|Search List 5|string|False|Optional search list field|
|Text 1|string|False|Optional text field|
|Text 2|string|False|Optional text field|
|Text 3|string|False|Optional text field|
|Text 4|string|False|Optional text field|
|Text 5|string|False|Optional text field|

#### processingStatus

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Processing status identifier|
|Name|string|False|Processing status name|

#### slaObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|SLA identifier|
|Response Target Date|string|False|Response target date|
|Target Date|string|False|Target date|

#### supplier

|Name|Type|Required|Description|
|----|----|--------|-----------|
|For First Line|boolean|False|Whether the supplier is for first line|
|For Second Line|boolean|False|Whether the supplier is for second line|
|ID|string|False|Supplier identifier|
|Name|string|False|Supplier name|

#### supplierOutput

|Name|Type|Required|Description|
|----|----|--------|-----------|
|For Change Management|boolean|False|Whether the supplier is for change management|
|For First Line|boolean|False|Whether the supplier is for first line|
|For Operational Activity|boolean|False|Whether the supplier is for operational activity|
|For Second Line|boolean|False|Whether the supplier is for second line|
|For Service|boolean|False|Whether the supplier is for service|
|ID|string|False|Supplier identifier|
|Name|string|False|Supplier name|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin | Add List Incidents, Create Incident, Get Incident by ID, Get Incident by Number, Update Incident by ID, Update Incident by Number, List Operators, List Operator Groups, List Suppliers, List Locations and Branches actions

# Links

* [TopDesk](https://www.topdesk.com/en/)

## References

* [TopDesk](https://www.topdesk.com/en/)
* [TopDesk Tutorial](https://developers.topdesk.com/tutorial.html)

