# Description

Notify the right people, reduce response time, and avoid alert fatigue within a workflow

# Key Features

* Create new alert
* Close existing alert
* Get information about specific alerts
* Get current on-call participants

# Requirements

* Opsgenie API Key

# Supported Product Versions

* 2022-01-11

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Opsgenie authorization API key|None|1234567e-123c-123c-123c-1234567e9xAd|

Example input:

```
{
  "api_key": "1234567e-123c-123c-123c-1234567e9xAd"
}
```

## Technical Details

### Actions

#### Close Alert

This action is used to close an existing alert from Opsgenie.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|identifier|string|None|True|Identifier of the alert|None|8418d193-2dab-4490-b331-8c02cdd196b7|
|identifierType|string|ID|False|Type of the identifier that is provided as an in-line parameter. Possible values are ID, tiny ID and alias. Default value is ID|['', 'ID', 'tiny', 'alias']|ID|
|note|string|None|False|Additional alert note to add|None|Action executed via InsightConnect|
|source|string|None|False|Display name of the request source|None|AWS Lambda|
|user|string|None|False|Display name of the request owner|None|Monitoring Script|

Example input:

```
{
  "identifier": "8418d193-2dab-4490-b331-8c02cdd196b7",
  "identifierType": "ID",
  "note": "Action executed via InsightConnect",
  "source": "AWS Lambda",
  "user": "Monitoring Script"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|elapsed_time|float|True|Time taken to execute|
|requestId|string|True|ID of a executed API request|
|result|string|True|Result message from API|

Example output:

```
{
  "result": "Request will be processed",
  "took": 0.107,
  "requestId": "43a29c5c-3dbf-4fa4-9c26-f4f71023e120"
}
```

#### Create Alert

This action creates an alert for Opsgenie.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|actions|[]string|None|False|Custom actions that will be available for the alert|None|["Restart", "AnExampleAction"]|
|alias|string|None|False|Client-defined identifier of the alert, that is also the key element of Alert deduplication|None|An example alias|
|description|string|None|False|Alert description|None|An example description|
|details|object|None|False|JSON object of key-value pairs to use as custom properties of the alert|None|{"key1":"value1","key2":"value2"}|
|entity|string|None|False|Entity field of the alert that is generally used to specify which domain an alert is related to|None|An example entity|
|message|string|None|True|Message of the alert|None|An example alert message|
|note|string|None|False|Additional note that will be added when creating the alert|None|Example additional note|
|priority|string|P3|False|Priority level of the alert. Possible values are P1, P2, P3, P4 and P5. Default value is P3|['', 'P2', 'P1', 'P3', 'P4', 'P5']|P1|
|responders|[]object|None|False|Teams, users, escalations and schedules that the alert will be routed to send notifications. "id/name": Either id or name of each responder should be provided. "type": team, user, escalation, schedule. Format: [{"id/name":"value", "type":"team/user/escalation/schedule"}]|None|[{"id":"4513b7ea-3b91-438f-b7e4-e3e54af9147c", "type":"team"},{"name":"NOC","type":"team"}]|
|source|string|None|False|Source field of the alert. Default value is IP address of the incoming request|None|192.168.0.1|
|tags|[]string|None|False|Tags of the alert|None|["OverwriteQuietHours","Critical"]|
|user|string|None|False|Display name of the request owner|None|ExampleName|
|visibleTo|[]object|None|False|Teams and users that the alert will become visible to without sending any notification. Type field is mandatory for each item, where possible values are team and user. In addition to the type field, either ID or name should be given for teams and either ID or username should be given for users. Please note that alert will be visible to the teams that are specified within responders field by default, so there is no need to re-specify them within visibleTo field. "id/name": Either id or name of each responder should be provided. "type": team, user, escalation, schedule. Format: [{"id/name":"value", "type":"team/user/escalation/schedule"}]|None|[{"id":"4513b7ea-3b91-438f-b7e4-e3e54af9147c","type":"team"},{"name":"example_name","type":"team"}]|

Example input:

```
{
  "actions": [
    "Restart",
    "AnExampleAction"
  ],
  "alias": "An example alias",
  "description": "An example description",
  "entity": "An example entity",
  "message": "An example alert message",
  "note": "Example additional note",
  "priority": "P1",
  "source": "192.168.0.1",
  "tags": [
    "OverwriteQuietHours",
    "Critical"
  ],
  "user": "ExampleName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|elapsed_time|float|True|Time taken to execute|
|requestId|string|True|ID of a executed API request|
|result|string|True|Result message from API|

Example output:

```
{
  "result": "Request will be processed",
  "took": 0.302,
  "requestId": "43a29c5c-3dbf-4fa4-9c26-f4f71023e120"
}
```

#### Get Alert

This action is used to retrieve alert from Opsgenie.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|identifier|string|None|True|Identifier of the alert|None|8418d193-2dab-4490-b331-8c02cdd196b7|
|identifierType|string|ID|False|Type of the identifier that is provided as an in-line parameter. Possible values are ID, tiny ID and alias. Default value is ID|['', 'ID', 'tiny', 'alias']|ID|

Example input:

```
{
  "identifier": "8418d193-2dab-4490-b331-8c02cdd196b7",
  "identifierType": "ID"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|object|True|Data that contains JSON response|
|elapsed_time|float|True|Time taken to execute|
|requestId|string|True|ID of an request|

Example output:

```
{
  "data": {
      "id": "70413a06-38d6-4c85-92b8-5ebc900d42e2",
      "tinyId": "1791",
      "alias": "event_573",
      "message": "Our servers are in danger",
      "status": "closed",
      "acknowledged": false,
      "isSeen": true,
      "tags": [
          "OverwriteQuietHours",
          "Critical"
      ],
      "snoozed": true,
      "snoozedUntil": "2017-04-03T20:32:35.143Z",
      "count": 79,
      "lastOccurredAt": "2017-04-03T20:05:50.894Z",
      "createdAt": "2017-03-21T20:32:52.353Z",
      "updatedAt": "2017-04-03T20:32:57.301Z",
      "source": "Isengard",
      "owner": "user@example.com",
      "priority": "P5",
      "responders": [
        {
            "id": "4513b7ea-3b91-438f-b7e4-e3e54af9147c",
            "type": "team"
        },
        {
            "id": "bb4d9938-c3c2-455d-aaab-727aa701c0d8",
            "type": "user"
        },
        {
            "id": "aee8a0de-c80f-4515-a232-501c0bc9d715",
            "type": "escalation"
        },
        {
            "id": "80564037-1984-4f38-b98e-8a1f662df552",
            "type": "schedule"
        }
          ],
      "integration": {
          "id": "4513b7ea-3b91-438f-b7e4-e3e54af9147c",
          "name": "ExampleName",
          "type": "API"
      },
      "report": {
          "ackTime": 15702,
          "closeTime": 60503,
          "acknowledgedBy": "user@example.com",
          "closedBy": "user@example.com"
      },
      "actions": ["Restart", "Ping"],
      "entity": "EC2",
      "description": "Example description",
      "details": {
          "serverName": "ExampleName",
          "region": "ExampleRegion"
      }
  },
  "requestId": "9ae63dd7-ed00-4c81-86f0-c4ffd33142c9"
}
```

#### Get On-Calls

This action is used to get on-call request which is used to retrieve current on-call participants of a specific schedule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|date|date|None|False|Starting date of the timeline that will be provided in format as (yyyy-MM-dd'T'HH:mm:ssZ) (e.g. 2017-01-15T08:00:00+02:00). Default date is the moment of the time that request is received|None|2017-01-15T08:00:00+02:00|
|flat|boolean|None|False|When enabled, retrieves user names of all on-call participants. Default value is false|None|False|
|scheduleIdentifier|string|None|True|Identifier of the schedule|None|ScheduleName|
|scheduleIdentifierType|string|ID|False|Type of the schedule identifier. Possible values are ID and name. Default value is ID|['', 'ID', 'name']|name|

Example input:

```
{
  "date": "2017-01-15T08:00:00+02:00",
  "flat": false,
  "scheduleIdentifier": "ScheduleName",
  "scheduleIdentifierType": "name"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|object|True|Response data from Opsgenie|
|elapsed_time|float|True|Time taken to execute|
|requestId|string|True|ID of a executed API request|

Example output:

```
{
  "data": {
      "_parent": {
          "id": "d875alp4-9b4e-4219-alp3-0c26936d18de",
          "name": "ScheduleName",
          "enabled": true
      },
      "onCallParticipants": [
          {
              "id": "c569c016-alpc-4e20-8a28-bd5dc33b798e",
              "name": "TeamName",
              "type": "team"
          },
          {
              "id": "15445alp-e46c-446f-9236-7ad89ad1a4f7",
              "name": "TeamName_escalation",
              "type": "escalation",
              "onCallParticipants": [
                  {
                      "id": "e55700e1-ff76-4cd0-a6e8-e1a982423alp",
                      "name": "TeamName_schedule",
                      "type": "schedule",
                      "escalationTime": 0,
                      "notifyType": "default"
                  },
                  {
                      "id": "e55700e1-ff76-4cd0-a6e8-e1a982423alp",
                      "name": "TeamName_schedule",
                      "type": "schedule",
                      "escalationTime": 5,
                      "notifyType": "next"
                  },
                  {
                      "id": "c569c016-alpc-4e20-8a28-bd5dc33b798e",
                      "name": "TeamName",
                      "type": "team",
                      "onCallParticipants": [
                          {
                              "id": "balp7783-a9f1-40e3-940c-ffde45656054",

                              "name": "user@example.com",

                              "type": "user"
                          },
                          {
                              "id": "4falpb2e-348d-4b7c-b71b-149efb8361e4",

                              "name": "user@example.com",

                              "type": "user"
                          }
                      ],
                      "escalationTime": 10,
                      "notifyType": "all"
                  }
              ]
          }
      ]
  },
  "took": 0.305,
  "requestId": "e28ce37b-d81c-4b1d-abb8-0c371d8alp5f"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin (Actions: Create Alert, Close Alert, Get Alert, Get On-Calls)

# Links

## References

* [Opsgenie](https://docs.opsgenie.com/docs/api-overview)

