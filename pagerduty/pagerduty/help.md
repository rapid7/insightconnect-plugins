# Description

Leverage PagerDuty for incident management and response

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

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

#### Create User

This action is used to create a User.

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

Example output:

```
```

#### Delete User by ID

This action is used to delete a User by ID.

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

Example output:

```
```

#### Get List of Users on Call

This action is used to get List of Users on Call.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]user|True|Users List|

Example output:

```
```

#### Get User by Email

This action is used to get a User by Email.

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

Example output:

```
```

#### Get User by ID

This action is used to get a User by ID.

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

Example output:

```
```

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

Example output:

```
```

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

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Avatar Url|string|False|Avatar URL|
|Color|string|False|Color|
|Description|string|False|Description|
|Email|string|True|Email|
|Id|string|False|ID|
|Job Title|string|False|Job Title|
|Name|string|True|Name|
|Role|string|False|Role|
|Self|string|False|URL to view object|
|Summary|string|False|Summary|
|Time Zone|string|False|Time Zone, e.g. America/Lima|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [PagerDuty](LINK TO PRODUCT/VENDOR WEBSITE)
