# Description

cortex xdr

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
|api_key|credential_secret_key|None|True|XDR auth key|None|rapid7.fqdn.paloaltonetworks.com|
|api_key_id|credential_secret_key|None|True|XDR auth ID|None|1|
|fqdn|string|None|True|Fully qualified domain name|None|www.fqdn.com|

Example input:

```
{
  "api_key": "rapid7.fqdn.paloaltonetworks.com",
  "api_key_id": "1",
  "fqdn": "www.fqdn.com"
}
```

## Technical Details

### Actions

_This plugin does not contain any actions._

### Triggers

#### Get Incidents

This trigger is used to get Incidents.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|start_time|integer|None|False|Earliest incident time in epoch ms|None|None|
|time_field|string|None|True|Which time field to filter and sort on|['modification_time', 'creation_time']|creation_time|

Example input:

```
{
  "time_field": "creation_time"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|False|Incident|

Example output:

```
```

### Custom Output Types

#### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert Count|integer|False|Alert Count|
|Assigned User Mail|string|False|Assigned User Mail|
|Assigned User Pretty Name|string|False|Assigned User Pretty Name|
|Creation Time|integer|False|Creation Time|
|Description|string|False|Description|
|Detection Time|integer|False|Detection Time|
|High Severity Alert Count|integer|False|High Severity Alert Count|
|Host Count|integer|False|Host Count|
|Hosts|[]string|False|Hosts|
|Incident ID|string|False|Incident ID|
|Incident Name|string|False|Incident Name|
|Incident Sources|[]string|False|Incident Sources|
|Low Severity Alert Count|integer|False|Low Severity Alert Count|
|Manual Description|string|False|Manual Description|
|Manual Score|integer|False|Manual Score|
|Manual Severity|string|False|Manual Severity|
|Med Severity Alert Count|integer|False|Med Severity Alert Count|
|Modification Time|integer|False|Modification Time|
|Notes|string|False|Notes|
|Resolve Comment|string|False|Resolve Comment|
|Rule Based Score|integer|False|Rule Based Score|
|Severity|string|False|Severity|
|Starred|boolean|False|Starred|
|Status|string|False|Status|
|User Count|integer|False|User Count|
|Users|[]string|False|Users|
|XDR URL|string|False|XDR URL|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Cortex XDR](LINK TO PRODUCT/VENDOR WEBSITE)
