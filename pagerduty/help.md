# Description

[PagerDuty](https://www.pagerduty.com/) provides enterprise-grade incident management that helps you 
orchestrate the ideal response to create better customer, employee, and business value. Use this plugin to manage users
and incidents within workflows.
The PagerDuty plugin makes requests to the V2 API.

# Key Features

* Create and manage PagerDuty incidents
* Access PagerDuty user information

# Requirements

* PagerDuty API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API Key|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Get On-Call Users

This action is used to get a list of users on call.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]user|True|Users List|

Example output:

```
```

#### Send Acknowledge Event

This action is used to acknowledge an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|False|Text that will appear in the incident's log associated with this event|None|None|
|details|object|None|False|An arbitrary JSON object containing any data you'd like included in the incident log|None|None|
|incident_key|string|None|True|Incident Key|None|None|
|service_key|string|None|True|Service Key (aka Integration Key)|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident_key|string|False|Incident Key|
|message|string|False|Message|
|status|string|False|Status|

#### Create User

This action is used to create a user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email|None|None|
|from_email|string|None|True|Email of creating user|None|None|
|name|string|None|True|Name|None|None|
|role|string|None|False|Role|['admin', 'limited_user', 'owner', 'read_only_user', 'user']|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if created|
|user|user|False|User|

#### Get User by Email

This action is used to get information about a user by email address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|user|user|False|User|

#### Send Trigger Event

This action is used to trigger an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client|string|None|False|The name of the monitoring client that is triggering this event|None|None|
|client_url|string|None|False|The URL of the monitoring client that is triggering this event|None|None|
|contexts|[]object|None|False|Additional context objects|None|None|
|description|string|None|True|Text that will appear in the incident's log associated with this event|None|None|
|details|object|None|False|An arbitrary JSON object containing any data you'd like included in the incident log|None|None|
|service_key|string|None|True|Service Key (aka Integration Key)|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident_key|string|False|Incident Key|
|message|string|False|Message|
|status|string|False|Status|

#### Delete User by ID

This action is used to delete a user by id.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|User ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if deleted|
|user|user|False|User|

#### Send Resolve Event

This action is used to resolve an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|False|Text that will appear in the incident's log associated with this event|None|None|
|details|object|None|False|An arbitrary JSON object containing any data you'd like included in the incident log|None|None|
|incident_key|string|None|True|Incident Key|None|None|
|service_key|string|None|True|Service Key (aka Integration Key)|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident_key|string|False|Incident Key|
|message|string|False|Message|
|status|string|False|Status|

#### Get User by ID

This action is used to get information about a user by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|User ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|user|user|False|User|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.1.0 - New action Get On Call
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Fix issue to make 'service_key' required in Send Resolve Request action
* 1.0.1 - Update to [PagerDuty REST API v2](https://v2.developer.pagerduty.com/docs/migrating-to-api-v2)
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [PagerDuty API V2](https://v2.developer.pagerduty.com/v2/page/api-reference)
