# Description

The Redis plugin allows you to add, update, and manage data in a Redis database

# Key Features

* Set and retrieve data from Redis

# Requirements

* Connection information for your Redis database

# Supported Product Versions

* 2024-11-8

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|db|integer|0|True|DB to use usually (0-15)|None|None|None|None|
|host|string|None|True|Host, e.g. 10.4.4.4|None|None|None|None|
|port|integer|6379|True|Port|None|None|None|None|

Example input:

```
{
  "db": 0,
  "host": "",
  "port": 6379
}
```

## Technical Details

### Actions


#### Delete

This action is used to delete a key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|key|string|None|True|Key to delete|None|None|None|None|
  
Example input:

```
{
  "key": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|False|Number of keys deleted|None|
  
Example output:

```
{
  "count": 0
}
```

#### Get

This action is used to get a key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|key|string|None|True|Key to get|None|None|None|None|
  
Example input:

```
{
  "key": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|None|
|value|string|False|Value|None|
  
Example output:

```
{
  "found": true,
  "value": ""
}
```

#### Hash Get

This action is used to get key's hash

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|key|string|None|True|Key to get|None|None|None|None|
  
Example input:

```
{
  "key": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|None|
|values|object|False|Values|None|
  
Example output:

```
{
  "found": true,
  "values": {}
}
```

#### Hash Set

This action is used to set key's hash

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expire|integer|None|False|Expiration in seconds|None|None|None|None|
|key|string|None|True|Key|None|None|None|None|
|values|object|None|True|Object hash field:value to set|None|None|None|None|
  
Example input:

```
{
  "expire": 0,
  "key": "",
  "values": {}
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|string|False|Reply (usually OK)|None|
  
Example output:

```
{
  "reply": ""
}
```

#### Hash Increment By

This action is used to increments the number stored at field in the hash stored at key by increment

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|field|string|None|True|Field to increment|None|None|None|None|
|key|string|None|True|Key to lookup|None|None|None|None|
|value|integer|0|True|How much to increment by|None|None|None|None|
  
Example input:

```
{
  "field": "",
  "key": "",
  "value": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|integer|False|Result returned after operation is ran|None|
  
Example output:

```
{
  "result": 0
}
```

#### Hash Multi Get

This action is used to returns the values associated with the specified fields in the hash stored at key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|[]string|None|False|Fields to retrieve values from|None|None|None|None|
|get_all|boolean|False|True|Get all values|None|None|None|None|
|key|string|None|True|Key to get|None|None|None|None|
  
Example input:

```
{
  "fields": [
    ""
  ],
  "get_all": false,
  "key": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|values|object|False|Values returned from HMGET|None|
  
Example output:

```
{
  "values": {}
}
```

#### Hash Multi Set

This action is used to sets the specified fields to their respective values in the hash stored at key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expire|integer|None|False|Expiration in seconds|None|None|None|None|
|key|string|None|True|Key|None|None|None|None|
|values|object|None|True|Object hash field:value to set|None|None|None|None|
  
Example input:

```
{
  "expire": 0,
  "key": "",
  "values": {}
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|boolean|False|Reply (usually OK)|None|
  
Example output:

```
{
  "reply": true
}
```

#### Keys

This action is used to return keys matching pattern

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|pattern|string|None|True|Pattern, e.g. *o*|None|None|None|None|
  
Example input:

```
{
  "pattern": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|False|Count of keys found|None|
|keys|[]string|False|Keys returned|None|
  
Example output:

```
{
  "count": 0,
  "keys": [
    ""
  ]
}
```

#### List Get

This action is used to get all elements in a list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|count|integer|1000|False|Max results to return|None|None|None|None|
|key|string|None|True|Key to get|None|None|None|None|
  
Example input:

```
{
  "count": 1000,
  "key": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|None|
|values|[]string|False|Values|None|
  
Example output:

```
{
  "found": true,
  "values": [
    ""
  ]
}
```

#### List Push

This action is used to list key's push

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expire|integer|None|False|Expiration in seconds|None|None|None|None|
|key|string|None|True|Key|None|None|None|None|
|value|string|None|True|Value to append|None|None|None|None|
  
Example input:

```
{
  "expire": 0,
  "key": "",
  "value": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|string|False|Reply (usually OK)|None|
  
Example output:

```
{
  "reply": ""
}
```

#### Set

This action is used to set a key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expire|integer|None|False|Expiration in seconds|None|None|None|None|
|key|string|None|True|Key to set|None|None|None|None|
|value|string|None|True|Value to set|None|None|None|None|
  
Example input:

```
{
  "expire": 0,
  "key": "",
  "value": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|string|False|Reply (usually OK)|None|
  
Example output:

```
{
  "reply": ""
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

* 1.0.2 - Bumping requirements.txt | SDK bump to 6.2.0
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode | Add actions HMSET, HMGET and HINCRBY
* 0.1.2 - Update to new plugin architecture, fix action 'keys'
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [REDIS](https://redis.io/)

## References

* [REDIS API Docs](https://redis.io/docs/latest/apis/)