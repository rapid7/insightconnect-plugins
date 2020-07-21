# Description

Take actions on an Insight Agent

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
|api_key|credential_secret_key|None|False|X API Key from the Insight Platform|None|a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99|
|org_id|credential_secret_key|None|False|Organization ID|None|2cg99z6y-795n-7bzf-hj67-12355h554974|
|region|string|United States|False|Region|['United States', 'Europe', 'Canada', 'Australia', 'Japan']|United States|

Example input:

```
{
  "api_key": "a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99",
  "org_id": "2cg99z6y-795n-7bzf-hj67-12355h554974",
  "region": "United States"
}
```
## Technical Details

### Actions

#### Get Agent Details

This action this action is used to find and display detailed information about a device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|IP address, MAC address, or host name of the device to get information from|None|MaliciousHost|

Example input:

```
{
  "agent": "MaliciousHost"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|object|True|Agent information|

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

* [Rapid7 Insight Agent](LINK TO PRODUCT/VENDOR WEBSITE)
