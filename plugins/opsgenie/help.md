# Description

Notify the right people, reduce response time, and avoid alert fatigue within a workflow.

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|OpsGenie authorization API key|None|1234567e-123c-123c-123c-1234567e9xAd|

Example input:

```
```

## Technical Details

### Actions

#### Close Alert

This action is used to close existing alert from OpsGenie.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|identifier|string|None|True|Identifier of the alert|None|8418d193-2dab-4490-b331-8c02cdd196b7|
|identifierType|string|id|False|Type of the identifier that is provided as an in-line parameter. Possible values are id, tiny and alias. Default value is id|['', 'id', 'tiny', 'alias']|id|
|note|string|None|False|Additional alert note to add|None|Action executed via Alert API|
|source|string|None|False|Display name of the request source|None|AWS Lambda|
|user|string|None|False|Display name of the request owner|None|Monitoring Script|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|requestId|string|True|ID of a executed API request|
|result|string|True|Result message from API|
|took|float|True|Time took to execute API|

Example output:

```
```

#### Create Alert

This action creates an alert for OpsGenie.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|actions|[]string|None|False|Custom actions that will be available for the alert|None|["Restart", "AnExampleAction"]|
|alias|string|None|False|Client-defined identifier of the alert, that is also the key element of Alert De-Duplication|None|An example Alias|
|description|string|None|False|Description field of the alert that is generally used to provide a detailed information about the alert|None|An example description|
|details|object|None|False|Map of key-value pairs to use as custom properties of the alert|None|{"key1":"value1","key2":"value2"}|
|entity|string|None|False|Entity field of the alert that is generally used to specify which domain alert is related to|None|An example entity|
|message|string|None|True|Message of the alert|None|An example alert message|
|note|string|None|False|Additional note that will be added while creating the alert|None|Example additional note|
|priority|string|P3|False|Priority level of the alert. Possible values are P1, P2, P3, P4 and P5. Default value is P3|['', 'P1', 'P2', 'P3', 'P4', 'P5']|P1|
|responders|[]object|None|False|Teams, users, escalations and schedules that the alert will be routed to send notifications. type field is mandatory for each item, where possible values are team, user, escalation and schedule. If the API Key belongs to a team integration, this field will be overwritten with the owner team. Either id or name of each responder should be provided.You can refer below for example values|None|[{"id":"4513b7ea-3b91-438f-b7e4-e3e54af9147c", "type":"team"},{"name":"NOC","type":"team"}]|
|source|string|None|False|Source field of the alert. Default value is IP address of the incoming request|None|192.168.0.1|
|tags|[]string|None|False|Tags of the alert|None|["OverwriteQuietHours","Critical"]|
|user|string|None|False|Display name of the request owner|None|ExampleName|
|visibleTo|[]object|None|False|Teams and users that the alert will become visible to without sending any notification.type field is mandatory for each item, where possible values are team and user. In addition to the type field, either id or name should be given for teams and either id or username should be given for users. Please note that alert will be visible to the teams that are specified withinresponders field by default, so there is no need to re-specify them within visibleTo field. You can refer below for example values|None|[{"id":"4513b7ea-3b91-438f-b7e4-e3e54af9147c","type":"team"},{"name":"example_name","type":"team"}]|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|requestId|string|True|ID of a executed API request|
|result|string|True|Result message from API|
|took|float|True|Time took to execute API|

Example output:

```
```

#### Get Alert

This action is used to retrieve alert from OpsGenie.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|identifier|string|None|True|Identifier of the alert|None|8418d193-2dab-4490-b331-8c02cdd196b7|
|identifierType|string|id|False|Type of the identifier that is provided as an in-line parameter. Possible values are id, tiny and alias. Default value is id|['', 'id', 'tiny', 'alias']|id|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|object|True|Data that contains JSON response|
|requestId|string|True|ID of an request|

Example output:

```
```

#### Get On Calls

This action is used to get on-call request is used to retrieve current on-call participants of a specific schedule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|date|date|None|False|Starting date of the timeline that will be provided in format as (yyyy-MM-dd'T'HH:mm:ssZ) (e.g. 2017-01-15T08:00:00+02:00). Default date is the moment of the time that request is received.|None|2017-01-15T08:00:00+02:00|
|flat|boolean|None|False|When enabled, retrieves user names of all on call participants. Default value is false|None|false|
|scheduleIdentifier|string|None|True|Identifier of the schedule|None|ScheduleName|
|scheduleIdentifierType|string|id|False|Type of the schedule identifier that is provided as an in-line parameter. Possible values are id and name. Default value is id|['', 'id', 'name']|name|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|object|True|Response DATA from OpsGenie API|
|requestId|string|True|ID of a executed API request|
|took|float|True|Time took to execute API|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [OpsGenie](LINK TO PRODUCT/VENDOR WEBSITE)

