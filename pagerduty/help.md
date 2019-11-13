# Description

[PagerDuty](https://www.pagerduty.com/) provides enterprise-grade incident management that helps you orchestrate the ideal response to create better customer, employee, and business value.
The PagerDuty plugin makes requests to the V2 API.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API Key|None|

This plugin requires an API key or user token to authenticate to PagerDuty.

There are 2 way to create API keys:

#

## Technical Details

### Actions

#### Send Acknowledge Event

This action is used to acknowledge an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|incident_key|string|None|True|Incident Key|None|
|service_key|string|None|False|Service Key|None|
|details|object|None|False|An arbitrary JSON object containing any data you'd like included in the incident log.|None|
|description|string|None|False|Text that will appear in the incident's log associated with this event|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status|
|message|string|False|Message|
|incident_key|string|False|Incident Key|

#### Create User

This action is used to create a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|Email|None|
|role|string|None|False|Role|['admin', 'limited_user', 'owner', 'read_only_user', 'user']|
|name|string|None|True|Name|None|
|from_email|string|None|True|Email of creating user|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|user|False|User|
|success|boolean|False|True if created|

#### Get User by Email

This action is used to get information about a user by email address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|Email|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|user|user|False|User|

#### Send Trigger Event

This action is used to trigger an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|client_url|string|None|False|The URL of the monitoring client that is triggering this event|None|
|client|string|None|False|The name of the monitoring client that is triggering this event|None|
|description|string|None|True|Text that will appear in the incident's log associated with this event|None|
|contexts|[]object|None|False|Additional context objects|None|
|service_key|string|None|False|Service Key|None|
|details|object|None|False|An arbitrary JSON object containing any data you'd like included in the incident log.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status|
|message|string|False|Message|
|incident_key|string|False|Incident Key|

#### Delete User by ID

This action is used to delete a user by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|User ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|user|False|User|
|success|boolean|False|True if deleted|

#### Send Resolve Event

This action is used to resolve an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|incident_key|string|None|True|Incident Key|None|
|service_key|string|None|False|Service Key|None|
|details|object|None|False|An arbitrary JSON object containing any data you'd like included in the incident log.|None|
|description|string|None|False|Text that will appear in the incident's log associated with this event|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status|
|message|string|False|Message|
|incident_key|string|False|Incident Key|

#### Get User by ID

This action is used to get information about a user by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|User ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|user|user|False|User|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Fix issue to make 'service_key' required in Send Resolve Request action
* 1.0.1 - Update to [PagerDuty REST API v2](https://v2.developer.pagerduty.com/docs/migrating-to-api-v2)
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Connecting PagerDuty To Komand](https://komand.zendesk.com/hc/en-us/articles/115003012007)
* [PagerDuty API V2](https://v2.developer.pagerduty.com/v2/page/api-reference)

