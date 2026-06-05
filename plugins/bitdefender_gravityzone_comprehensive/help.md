# Description

Exposes documented Bitdefender GravityZone API methods

# Key Features

* Execute dynamic Bitdefender API methods.

# Requirements



# Supported Product Versions

* GravityZone Cloud

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_token|None|True|The API token|None|12345abcde67890fghij|None|None|
|url|string|None|True|The base URL|None|https://cloud.gravityzone.bitdefender.com|None|None|

Example input:

```
{
  "api_key": "12345abcde67890fghij",
  "url": "https://cloud.gravityzone.bitdefender.com"
}
```

## Technical Details

### Actions


#### Execute API Method

This action is used to executes a dynamic method call

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_version|string|None|True|The version string|None|v1.0|None|None|
|method_name|string|None|True|The literal method string|None|getEndpointsList|None|None|
|parameters|object|None|False|The data object|None|None|None|None|
|service_group|string|None|True|The endpoint route|None|network|None|None|
  
Example input:

```
{
  "api_version": "v1.0",
  "method_name": "getEndpointsList",
  "parameters": {},
  "service_group": "network"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|object|False|Output response data|None|
  
Example output:

```
{
  "result": {}
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting


# Version History

* 2.0.0 - Initial release

# Links



## References

