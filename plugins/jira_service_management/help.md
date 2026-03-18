# Description

Notify the right people, reduce response time, and avoid alert fatigue with Jira Service Management

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2026-02-25

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_token|credential_secret_key|None|True|Jira Service Management API Token generated here https://id.atlassian.com/manage-profile/security/api-tokens|None|ABCD1234efgh5678IJKLmnopqrstUVWXyz9876543210|None|None|
|cloud_id|string|None|True|Cloud ID of the Jira Service Management instance. It can be found in the https://yoursite.atlassian.net/_edge/tenant_info API response or by contacting Atlassian support|None|example@yoursite.com|None|None|
|email|string|None|True|Email address of the user that is used to create API token. It should be the email address of an active user in the Jira Service Management instance|None|user@example.com|None|None|

Example input:

```
{
  "api_token": "ABCD1234efgh5678IJKLmnopqrstUVWXyz9876543210",
  "cloud_id": "example@yoursite.com",
  "email": "user@example.com"
}
```

## Technical Details

### Actions


#### Close Alert

This action is used to close an existing alert from Jira Service Management

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|identifier|string|None|True|Identifier of the alert|None|8418d193-2dab-4490-b331-8c02cdd196b7|None|None|
  
Example input:

```
{
  "identifier": "8418d193-2dab-4490-b331-8c02cdd196b7"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|elapsed_time|float|True|Time taken to execute|0.195|
|requestId|string|True|ID of a executed API request|d383c6e9-b1e7-4b59-9c35-72f1a2187777|
|result|string|True|Result message from API|Request will be processed|
  
Example output:

```
{
  "elapsed_time": 0.195,
  "requestId": "d383c6e9-b1e7-4b59-9c35-72f1a2187777",
  "result": "Request will be processed"
}
```

#### Create Alert

This action is used to creates an alert for Jira Service Management

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|actions|[]string|None|False|Custom actions that will be available for the alert|None|["Restart", "AnExampleAction"]|None|None|
|alias|string|None|False|Client-defined identifier of the alert, that is also the key element of Alert deduplication|None|An example alias|None|None|
|description|string|None|False|Alert description|None|An example description|None|None|
|details|object|None|False|JSON object of key-value pairs to use as custom properties of the alert|None|{"key1":"value1","key2":"value2"}|None|None|
|entity|string|None|False|Entity field of the alert that is generally used to specify which domain an alert is related to|None|An example entity|None|None|
|message|string|None|True|Message of the alert|None|An example alert message|None|None|
|note|string|None|False|Additional note that will be added when creating the alert|None|Example additional note|None|None|
|priority|string|P3|False|Priority level of the alert. Possible values are P1, P2, P3, P4 and P5. Default value is P3|["", "P2", "P1", "P3", "P4", "P5"]|P1|None|None|
|responders|[]object|None|False|Teams, users, escalations and schedules that the alert will be routed to send notifications. "id/name": Either id or name of each responder should be provided. "type": team, user, escalation, schedule. Format: [{"id/name":"value", "type":"team/user/escalation/schedule"}]|None|[{"id":"4513b7ea-3b91-438f-b7e4-e3e54af9147c", "type":"team"},{"name":"NOC","type":"team"}]|None|None|
|source|string|Rapid7 Automation|False|Source field of the alert. Default value is Rapid7 Automation|None|Rapid7 Automation|None|None|
|tags|[]string|None|False|Tags of the alert|None|["OverwriteQuietHours","Critical"]|None|None|
|user|string|None|False|Display name of the request owner|None|ExampleName|None|None|
|visibleTo|[]object|None|False|Teams and users that the alert will become visible to without sending any notification. Type field is mandatory for each item, where possible values are team and user. In addition to the type field, either ID or name should be given for teams and either ID or username should be given for users. Please note that alert will be visible to the teams that are specified within responders field by default, so there is no need to re-specify them within visibleTo field. "id/name": Either id or name of each responder should be provided. "type": team, user, escalation, schedule. Format: [{"id/name":"value", "type":"team/user/escalation/schedule"}]|None|[{"id":"4513b7ea-3b91-438f-b7e4-e3e54af9147c","type":"team"},{"name":"example_name","type":"team"}]|None|None|
  
Example input:

```
{
  "actions": [
    "Restart",
    "AnExampleAction"
  ],
  "alias": "An example alias",
  "description": "An example description",
  "details": {
    "key1": "value1",
    "key2": "value2"
  },
  "entity": "An example entity",
  "message": "An example alert message",
  "note": "Example additional note",
  "priority": "P3",
  "responders": [
    {
      "id": "4513b7ea-3b91-438f-b7e4-e3e54af9147c",
      "type": "team"
    },
    {
      "name": "NOC",
      "type": "team"
    }
  ],
  "source": "Rapid7 Automation",
  "tags": [
    "OverwriteQuietHours",
    "Critical"
  ],
  "user": "ExampleName",
  "visibleTo": [
    {
      "id": "4513b7ea-3b91-438f-b7e4-e3e54af9147c",
      "type": "team"
    },
    {
      "name": "example_name",
      "type": "team"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alertId|string|True|ID of an created alert|8418d193-2dab-4490-b331-8c02cdd196b7|
|elapsed_time|float|True|Time taken to execute|0.195|
|requestId|string|True|ID of a executed API request|d383c6e9-b1e7-4b59-9c35-72f1a2187777|
|result|string|True|Result message from API|Request will be processed|
  
Example output:

```
{
  "alertId": "8418d193-2dab-4490-b331-8c02cdd196b7",
  "elapsed_time": 0.195,
  "requestId": "d383c6e9-b1e7-4b59-9c35-72f1a2187777",
  "result": "Request will be processed"
}
```

#### Get Alert

This action is used to retrieve alert from Jira Service Management

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|identifier|string|None|True|Identifier of the alert|None|8418d193-2dab-4490-b331-8c02cdd196b7|None|None|
  
Example input:

```
{
  "identifier": "8418d193-2dab-4490-b331-8c02cdd196b7"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|object|True|Data that contains JSON response|{'acknowledged': False, 'actions': [], 'alias': 'alert-123e4567-e89b-12d3-a456-426614174000', 'count': 2, 'createdAt': '2026-01-10T08:15:30.000Z', 'description': 'Example alert', 'entity': 'example-service', 'extraProperties': {'environment': 'staging', 'region': 'eu-central-1'}, 'id': 'alert-123e4567-e89b-12d3-a456-426614174000', 'integrationName': 'example-monitoring', 'integrationType': 'webhook', 'lastOccuredAt': '2026-01-10T08:20:00.000Z', 'message': 'High CPU usage detected on instance i-abc123example', 'owner': 'on-call-team', 'priority': 'P2', 'responders': [{'name': 'example-user', 'type': 'team'}], 'seen': True, 'services': [{'name': 'example-api', 'status': 'degraded'}], 'snoozed': False, 'source': 'example-monitoring-system', 'status': 'open', 'tags': ['cpu', 'performance', 'demo'], 'tinyId': '42', 'updatedAt': '2026-01-10T08:21:10.000Z'}|
  
Example output:

```
{
  "data": {
    "acknowledged": false,
    "actions": [],
    "alias": "alert-123e4567-e89b-12d3-a456-426614174000",
    "count": 2,
    "createdAt": "2026-01-10T08:15:30.000Z",
    "description": "Example alert",
    "entity": "example-service",
    "extraProperties": {
      "environment": "staging",
      "region": "eu-central-1"
    },
    "id": "alert-123e4567-e89b-12d3-a456-426614174000",
    "integrationName": "example-monitoring",
    "integrationType": "webhook",
    "lastOccuredAt": "2026-01-10T08:20:00.000Z",
    "message": "High CPU usage detected on instance i-abc123example",
    "owner": "on-call-team",
    "priority": "P2",
    "responders": [
      {
        "name": "example-user",
        "type": "team"
      }
    ],
    "seen": true,
    "services": [
      {
        "name": "example-api",
        "status": "degraded"
      }
    ],
    "snoozed": false,
    "source": "example-monitoring-system",
    "status": "open",
    "tags": [
      "cpu",
      "performance",
      "demo"
    ],
    "tinyId": "42",
    "updatedAt": "2026-01-10T08:21:10.000Z"
  }
}
```

#### Get On-Calls

This action is used to get current on-call participants

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|date|date|None|False|Starting date of the timeline that will be provided in format as (yyyy-MM-dd'T'HH:mm:ssZ) (e.g. 2017-01-15T08:00:00+02:00). Default date is the moment of the time that request is received|None|2017-01-15T08:00:00+02:00|None|None|
|flat|boolean|None|False|When enabled, retrieves user names of all on-call participants. Default value is false|None|False|None|None|
|scheduleIdentifier|string|None|True|Identifier of the schedule|None|ScheduleName|None|None|
  
Example input:

```
{
  "date": "2017-01-15T08:00:00+02:00",
  "flat": false,
  "scheduleIdentifier": "ScheduleName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|object|True|Response data from Jira Service Management|{"onCallParticipants":[{"id":"bc667897-cb21-496f-a46e-7c05ff0419dd","type":"team"},{"id":"5b2b0e011b3a756623f4e25e","type":"user"},{"id":"7a24e9d7-7a4f-4f86-a1df-21ca9c3112ac","type":"escalation","onCallParticipants":[{"id":"5b2b0e011b3a756623f4e25e","type":"user","forwardedFrom":{"id":"c5646941-3f05-404d-8594-825fa73af99f","type":"user"}}]}]}|
  
Example output:

```
{
  "data": {
    "onCallParticipants": [
      {
        "id": "bc667897-cb21-496f-a46e-7c05ff0419dd",
        "type": "team"
      },
      {
        "id": "5b2b0e011b3a756623f4e25e",
        "type": "user"
      },
      {
        "id": "7a24e9d7-7a4f-4f86-a1df-21ca9c3112ac",
        "onCallParticipants": [
          {
            "forwardedFrom": {
              "id": "c5646941-3f05-404d-8594-825fa73af99f",
              "type": "user"
            },
            "id": "5b2b0e011b3a756623f4e25e",
            "type": "user"
          }
        ],
        "type": "escalation"
      }
    ]
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.0 - Initial plugin

# Links

* [Jira Service Management](https://www.atlassian.com/software/jira/service-management)

## References
  
*This plugin does not contain any references.*