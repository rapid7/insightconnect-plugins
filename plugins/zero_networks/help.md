# Description

Search for and quarantine assets managed by the Zero Networks Segment platform

# Key Features

* Look up a Zero Networks asset ID from a fully qualified domain name
* Quarantine or release an asset to contain a compromised host

# Requirements

* A Zero Networks API key
* The URL of your Zero Networks API instance

# Supported Product Versions

* Zero Networks API v1 (1.26.8)

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|The Zero Networks API key, created from the API section of the Zero Networks portal settings|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|url|string|https://portal.zeronetworks.com/api/v1|True|The URL of the Zero Networks API instance, including the API version path|None|https://portal.zeronetworks.com/api/v1|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "url": "https://portal.zeronetworks.com/api/v1"
}
```

## Technical Details

### Actions


#### Quarantine Asset

This action is used to quarantine an asset to block its network traffic, or release an asset from quarantine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_id|string|None|True|The ID of the asset to quarantine or release, as returned by the Search Asset action|None|a:a:JF2xro6g|None|None|
|quarantine|boolean|True|True|Whether to quarantine the asset, set to false to release the asset from quarantine|None|True|None|None|
  
Example input:

```
{
  "asset_id": "a:a:JF2xro6g",
  "quarantine": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the quarantine state was applied successfully|True|
  
Example output:

```
{
  "success": true
}
```

#### Search Asset

This action is used to search for an asset by its fully qualified domain name and return its asset ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fqdn|string|None|True|The fully qualified domain name of the asset to search for|None|server.domain.local|None|None|
  
Example input:

```
{
  "fqdn": "server.domain.local"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset_id|string|False|The ID of the matching asset, empty when no asset was found|a:a:JF2xro6g|
|found|boolean|True|Whether an asset matching the given fully qualified domain name was found|True|
  
Example output:

```
{
  "asset_id": "a:a:JF2xro6g",
  "found": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* `Search Asset` returns `Found: false` rather than failing when no asset matches. Zero Networks matches the fully qualified domain name exactly, so supply the full name (for example `server.domain.local`) rather than the short hostname.
* `Quarantine Asset` needs an asset ID in the `a:<type>:<id>` format returned by `Search Asset`, not a hostname or an IP address. A not found error means the asset ID does not exist in this Zero Networks environment.
* The URL in the connection must include the API version path, for example `https://portal.zeronetworks.com/api/v1`. A connection test that fails with an authentication error means the API key is invalid or has been revoked; generate a new key from the API section of the Zero Networks portal settings.

# Version History

* 1.0.0 - Initial plugin

# Links

* [Zero Networks](https://zeronetworks.com)

## References

* This plugin was developed against version 1.26.8 of the Zero Networks API v1.
* API keys are created from Settings > Integrations > API in the [Zero Networks portal](https://portal.zeronetworks.com). The key must have permission to read assets and to perform asset actions.