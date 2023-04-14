# Description

Armorblox secures enterprise communications over email and other cloud office applications with the power of Natural Language Understanding. The Armorblox platform connects over APIs and analyzes thousands of signals to understand the context of communications and protect people and data from compromise. Over 56,000 organizations use Armorblox to stop BEC and targeted phishing attacks, protect sensitive PII and PCI, and automate remediation of user-reported email threats. Armorblox was featured in the 2019 Forbes AI 50 list and was named a 2020 Gartner Cool Vendor in Cloud Office Security. Founded in 2017, Armorblox is headquartered in Sunnyvale, CA and backed by General Catalyst and Next47

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
  "tenant_name": "outbound-integrations"
}
```

## Technical Details

### Actions

#### Get Remediation Action

This action is used to get remediation action of a incident identified by Armorblox.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incident_id|string|None|True|An integer number representing the incident|None|3490|

Example input:

```
{
  "incident_id": 3490
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|remediation_details|string|True|Remediation Action of the requested incident identified by Armorblox|

Example output:

```
```

### Triggers

#### Get Incidents

This trigger is used to get a list of incidents identified by Armorblox, by default it starts polling all the incidents since last day.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|interval|integer|600|False|Polling inteval in seconds|None|600|

Example input:

```
{
  "interval": 600
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]incident|True|A list of incidents identified by Armorblox|

Example output:

```
```

### Custom Output Types

#### engagement

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Mail Count|string|False|Mail Count|
|Mail Count|string|False|Mail Count|

#### final_detection_tag

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Detection tag ID|string|False|Detection tag ID|
|Detection tag name|string|False|Detection tag name|

#### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|App Name|string|False|App Name|
|Occured Date|date|False|None|
|Engagements|engagement|False|Engagements|
|External senders|[]string|False|List of external senders|
|external users|[]user|False|List of external users|
|Detection tags|[]final_detection_tag|False|Detection Tags|
|Folder category|[]string|False|Folder category|
|Incident ID|string|False|Incident ID|
|Incident Type|string|False|Incident Type|
|Object Type|string|False|Object Type|
|policy_names|[]string|False|List of policies|
|Priority|string|False|Priority of the incident|
|Remediation Action|[]string|False|Remediation Action|
|Research Status|string|False|Research Status|
|resolution_state|string|False|Resolution State|
|SCL Score|integer|False|None|
|Is email tagged|boolean|False|Is email tagged|
|title|string|False|title|
|users|[]user|False|List of users|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user email|string|False|User email|
|Is User VIP|boolean|False|Is User VIP|
|user name|string|False|User name|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Armorblox](LINK TO PRODUCT/VENDOR WEBSITE)
