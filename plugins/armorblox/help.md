# Description

Armorblox is an API-based platform that stops targeted email attacks, protects sensitive data, and automates incident response

# Key Features

* Fetches incidents detected by Armorblox for the given tenant.
* Retrieves the remediation action for a given incident.

# Requirements

* Requires an API key from the product.

# Supported Product Versions

* 1.0.0

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Armorblox API Key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|tenant_name|string|None|True|Armorblox Tenant Name|None|my-tenant-name|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "tenant_name": "my-tenant-name"
}
```
## Technical Details

### Actions

#### Get Remediation Action

This action is used to fetch remediation action of an incident identified by Armorblox.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incident_id|string|None|True|An integer number identifying the incident|None|3490|

Example input:

```
{
  "incident_id": 3490
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|remediation_details|string|True|Remediation action of the requested incident identified by Armorblox|ALERT|

Example output:
```
{
  "remediation_details": "ALERT"
}
```

### Triggers

#### Get Incidents

This trigger is used to get a list of incidents identified by Armorblox. By default, it starts querying for all the incidents since the previous day.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|interval|integer|600|False|Polling interval in seconds|None|600|

Example input:

```
{
  "interval": 600
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|incidents|[]incident|True|A list of incidents identified by Armorblox|{"incidents": "some incidents"}|

Example output:

```
{
  "incidents": "some incidents"
}
```

### Custom Output Types

#### engagement

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Forwarded Mail Count|string|False|Forwarded Mail Count|
|Reply Mail Count|string|False|Reply Mail Count|

#### final_detection_tag

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Detection tag ID|string|False|Detection tag ID|
|Detection tag name|string|False|Detection tag name|

#### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|App Name|string|False|App Name|
|Incident Date|date|False|None|
|Engagements|engagement|False|Engagements|
|External senders|[]string|False|List of external senders|
|External users|[]user|False|List of external users|
|Detection tags|[]final_detection_tag|False|Detection tags|
|Folder categories|[]string|False|Folder categories|
|Incident ID|string|False|Incident ID|
|Incident Type|string|False|Incident Type|
|Object Type|string|False|Object Type|
|policy_names|[]string|False|List of policies|
|Priority|string|False|Priority of the incident|
|Remediation Action|[]string|False|Remediation Action|
|resolution_state|string|False|Resolution State|
|SCL Score|integer|False|None|
|Is email tagged|boolean|False|Is email tagged|
|Subject|string|False|Subject|
|users|[]user|False|List of users|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|User email|string|False|User email|
|Is User VIP|boolean|False|Is User VIP|
|user name|string|False|User name|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

* [Armorblox](https://www.armorblox.com/)
## References
