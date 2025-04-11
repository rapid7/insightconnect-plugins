# Description

Surface Command gives you full visibilty over your assets and identies across multiple technology platforms.

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* v1.0.790

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|User or Organization Key from the Insight Platform|None|a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99|None|None|
|region|string|United States|True|Region|["United States", "United States 2", "United States 3", "Europe", "Canada", "Australia", "Japan"]|United States|None|None|

Example input:

```
{
  "api_key": "a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99",
  "region": "United States"
}
```

## Technical Details

### Actions


#### Run Surface Command Query

This action is used to run and execute Surface Command Query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query_id|string|None|True|Query ID (UUID) to run from Surface Command|None|12345678-1234-1234-1234-123456789012|None|None|
  
Example input:

```
{
  "query_id": "12345678-1234-1234-1234-123456789012"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|items|False|Array of Items|[]|
  
Example output:

```
{
  "items": []
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History
  
*This plugin does not contain a version history.*

# Links
  
*This plugin does not contain any links.*

## References

* [Identify Data Region](https://docs.rapid7.com/insight/navigate-the-insight-platform/#check-your-data-region)
* [Generate User API Key](https://docs.rapid7.com/insight/managing-platform-api-keys/#generating-a-user-key)