# Description

IntSights is disrupting external threat intelligence with a combination of human and automated collection, intelligent analysis, and strategic threat hunting that turns the clear, deep, and dark webs into an intelligence resource that any company can deploy

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
|account_id|credential_secret_key|None|True|Account id|None|{"secret_key": "account_id"}|
|api_key|credential_secret_key|None|True|API key|None|{"secret_key": "api_key"}|

Example input:

```
{
  "account_id": "{\"secret_key\": \"account_id\"}",
  "api_key": "{\"secret_key\": \"api_key\"}"
}
```

## Technical Details

### Actions

#### Get Indicator by Value

This action this action will search indicators in Intsights TIP.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator_value|string|None|True|Indicator Value|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|first_seen|string|True|First Seen|
|geo_location|string|True|GEO Location|
|last_seen|string|True|Last Seen|
|last_update|string|True|Last Update|
|related_campaigns|[]string|True|Related Campaigns|
|related_malware|[]string|True|Related Malware|
|related_threat_actors|[]string|True|Related Threat Actors|
|score|integer|True|Score|
|severity|string|True|Severity|
|sources|[]source|True|Sources|
|system_tags|[]string|True|System Tags|
|tags|[]string|True|Tags|
|type|string|True|Type|
|value|string|True|Value|
|whitelist|string|True|Whitelist|

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

* [IntSights](LINK TO PRODUCT/VENDOR WEBSITE)

