# Description

Surface Command gives you full visibility over your assets and identities across multiple technology platforms

# Key Features

* Query Surface Command Data

# Requirements

* User or Organization Key from the Insight Platform. To create one follow [Generate User API Key guide](https://docs.rapid7.com/insight/managing-platform-api-keys/#generating-a-user-key)
* The Region where your Rapid7 Surface Command instance is hosted. To identify your region, see [Identify Data Region](https://docs.rapid7.com/insight/navigate-the-insight-platform/#check-your-data-region)
* A valid Query ID (UUID) from Rapid7 Surface Command. To obtain a Query ID, edit a Saved Query in the Surface Command UI and retrieve its ID from the URL

# Supported Product Versions

* v1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|User or Organization Key from the Insight Platform|None|a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99|None|None|
|region|string|us|True|Region|["us", "us2", "us3", "eu", "ca", "au", "ap"]|us|None|None|

Example input:

```
{
  "api_key": "a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99",
  "region": "us"
}
```

## Technical Details

### Actions


#### Run an Adhoc Query

This action is used to run and execute an adhoc query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cypher|string|None|True|Cypher query to execute|None|MATCH (m:Machine) RETURN m|None|None|
  
Example input:

```
{
  "cypher": "MATCH (m:Machine) RETURN m"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]object|False|Array of Items|[]|
  
Example output:

```
{
  "items": []
}
```

#### Run a Saved Query

This action is used to run and execute a saved query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query_id|string|None|True|Query ID (UUID) to Run from Surface Command|None|12345678-1234-1234-1234-123456789012|None|None|
  
Example input:

```
{
  "query_id": "12345678-1234-1234-1234-123456789012"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]object|False|Array of Items|[]|
  
Example output:

```
{
  "items": []
}
```

#### Tag Assets in Bulk

This action is used to add, set, or remove tags on multiple assets in bulk

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|object_ids|[]string|None|True|List of asset object IDs (UUIDs) to tag|None|["11111111-1111-1111-1111-111111111111", "22222222-2222-2222-2222-222222222222"]|None|None|
|operation|string|None|True|Tag operation to perform: add (append tags), set (replace all tags), or remove (delete tags)|["add", "set", "remove"]|add|None|None|
|tags|[]string|None|True|List of tag values to apply|None|["env:prod", "team:security"]|None|None|
  
Example input:

```
{
  "object_ids": [
    "11111111-1111-1111-1111-111111111111",
    "22222222-2222-2222-2222-222222222222"
  ],
  "operation": "add",
  "tags": [
    "env:prod",
    "team:security"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|failure_count|integer|True|Number of assets that could not be tagged|0|
|failures|[]object|False|Details of any tagging failures, including the object ID and error message|[]|
|success_count|integer|True|Number of assets successfully tagged|2|
  
Example output:

```
{
  "failure_count": 0,
  "failures": [],
  "success_count": 2
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

* 1.2.0 - Add new action | Tag Assets in Bulk
* 1.1.0 - Update action title | Add new action | Run Adhoc Query
* 1.0.0 - Initial plugin

# Links

* [Rapid7 Surface Command](https://www.rapid7.com/products/command/attack-surface-management-asm/)

## References

* [Identify Data Region](https://docs.rapid7.com/insight/navigate-the-insight-platform/#check-your-data-region)
* [Generate User API Key](https://docs.rapid7.com/insight/managing-platform-api-keys/#generating-a-user-key)