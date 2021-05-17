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
|api_key|credential_secret_key|None|True|The API Key that is generated when creating a new key|None|1234123412341234asdfasdfasdfasdfasdf1234123412341234123412341234asdfasdfasdfasdfasdf123412341234123412341234asdfasdfasdfasdfasdf|
|api_key_id|int|None|True|The API Key ID shown in the API Keys table in settings. e.g. 1, 2, 3|None|1|
|fqdn|string|None|True|Fully qualified domain name|None|https://api-example.xdr.us.paloaltonetworks.com/|
|security_level|string|Standard|True|The Security Level of the key provided. This can be found in the API Key settings table in the Cortex XDR settings|['Advanced', 'Standard']|Standard|

Example input:

```
{
  "api_key": "1234123412341234asdfasdfasdfasdfasdf1234123412341234123412341234asdfasdfasdfasdfasdf123412341234123412341234asdfasdfasdfasdfasdf",
  "api_key_id": 1,
  "fqdn": "https://api-example.xdr.us.paloaltonetworks.com/",
  "security_level": "Standard"
}
```

## Technical Details

### Actions

#### Get Endpoint Details

This action is used to get information about an endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|True|The hostname to get information about|None|example-host|

Example input:

```
{
  "hostname": "example-host"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|endpoints|[]endpoint|True|Any endpoints that match the given hostname|

Example output:

```
```

### Triggers

#### Get Incidents

This trigger is used to get Incidents.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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
|incident|object|False|Incident|

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
