# Description

Redis is an in-memory data structure project implementing a distributed, in-memory key-value database with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indexes.\nThis package allows you to interact with the [Redis](https://redis.io/) database API

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
|db|integer|0|True|DB to use usually (0-15)|None|10|None|None|
|host|string|None|True|Host, e.g. 10.4.4.4|None|10.4.4.4|None|None|
|port|integer|6379|True|Port|None|6379|None|None|

Example input:

```
{
  "db": 0,
  "host": "10.4.4.4",
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
|key|string|None|True|Key to delete|None|example:1234:session|None|None|
  
Example input:

```
{
  "key": "example:1234:session"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|False|Number of keys deleted|1|
  
Example output:

```
{
  "count": 1
}
```

#### Get
  
This action is used to get a key. Get will return a value at `key` if found, otherwise found will be false

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|key|string|None|True|Key to get|None|example:1234:active|None|None|
  
Example input:

```
{
  "key": "example:1234:active"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|True|
|value|string|False|Value|True|
  
Example output:

```
{
  "found": true,
  "value": true
}
```

#### Hash Get

This action is used to return all hash values at `key`. If no hash values are found `false` is returned.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|key|string|None|True|Key to get|None|user:profile|None|None|
  
Example input:

```
{
  "key": "user:profile"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|True|
|values|object|False|Values|{'name': 'Example Name', 'email': 'Example.email@example.com', 'age': '30'}|
  
Example output:

```
{
  "found": true,
  "values": {
    "age": "30",
    "email": "Example.email@example.com",
    "name": "Example Name"
  }
}
```

#### Hash Set

This action is used to set a given key to a key:value object. All values must be strings.
There is an optional expiration timeout which will auto remove the key when `expire` seconds have passed


##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expire|integer|None|False|Expiration in seconds|None|100|None|None|
|key|string|None|True|Key|None|user:1234|None|None|
|values|object|None|True|Object hash field:value to set|None|{'name': 'John Doe', 'email': 'johndoe@example.com', 'age': '30'}|None|None|
  
Example input:

```
{
  "expire": 100,
  "key": "user:1234",
  "values": {
    "age": "30",
    "email": "johndoe@example.com",
    "name": "John Doe"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|string|False|Reply (usually OK)|OK|
  
Example output:

```
{
  "reply": "OK"
}
```

#### Hash Increment By

This action is used to increments the number stored at field in the hash stored at key by increment.
If key does not exist, a new key holding a hash is created. If field does not exist the value is set to 0 before the operation is performed

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|field|string|None|True|Field to increment|None|login_count|None|None|
|key|string|None|True|Key to lookup|None|user:profile:123|None|None|
|value|integer|0|True|How much to increment by|None|1|None|None|
  
Example input:

```
{
  "field": "login_count",
  "key": "user:profile:123",
  "value": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|integer|False|Result returned after operation is ran|1|
  
Example output:

```
{
  "result": 1
}
```

#### Hash Multi Get

This action is used to returns the values associated with the specified fields in the hash stored at key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|[]string|None|False|Fields to retrieve values from|None|["name", "email"]|None|None|
|get_all|boolean|False|True|Get all values|None|False|None|None|
|key|string|None|True|Key to get|None|user:profile:123|None|None|
  
Example input:

```
{
  "fields": [
    "name",
    "email"
  ],
  "get_all": false,
  "key": "user:profile:123"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|values|object|False|Values returned from HMGET|{'name': 'Ryan Test', 'email': 'Ryan.test@example.com'}|
  
Example output:

```
{
  "values": {
    "email": "Ryan.test@example.com",
    "name": "Ryan Test"
  }
}
```

#### Hash Multi Set

This action is used to sets the specified fields to their respective values in the hash stored at key.
This command overwrites any specified fields already existing in the hash. If key does not exist, a new key holding a hash is created

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expire|integer|None|False|Expiration in seconds|None|100|None|None|
|key|string|None|True|Key|None|user:profile:123|None|None|
|values|object|None|True|Object hash field:value to set|None|{'name': 'Test Name', 'email': 'Test.Name@example.com', 'age': '30'}|None|None|
  
Example input:

```
{
  "expire": 100,
  "key": "user:profile:123",
  "values": {
    "age": "30",
    "email": "Test.Name@example.com",
    "name": "Test Name"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|boolean|False|Reply (usually OK)|True|
  
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
|pattern|string|None|True|Pattern, e.g. *o*|None|example:*:session|None|None|
  
Example input:

```
{
  "pattern": "example:*:session"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|False|Count of keys found|1|
|keys|[]string|False|Keys returned|["example:1234:session", "example:5678:session", "example:abcd:session"]|
  
Example output:

```
{
  "count": 1,
  "keys": [
    "example:1234:session",
    "example:5678:session",
    "example:abcd:session"
  ]
}
```

#### List Get

This action is used to get all elements in a list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|count|integer|1000|False|Max results to return|None|1000|None|None|
|key|string|None|True|Key to get|None|user:task_list:123|None|None|
  
Example input:

```
{
  "count": 1000,
  "key": "user:task_list:123"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|True|
|values|[]string|False|Values|["task1", "task2", "task3", "task4"]|
  
Example output:

```
{
  "found": true,
  "values": [
    "task1",
    "task2",
    "task3",
    "task4"
  ]
}
```

#### List Push

This action is used to list key's push

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expire|integer|None|False|Expiration in seconds|None|100|None|None|
|key|string|None|True|Key|None|user:task_list:123|None|None|
|value|string|None|True|Value to append|None|Complete monthly report|None|None|
  
Example input:

```
{
  "expire": 100,
  "key": "user:task_list:123",
  "value": "Complete monthly report"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|string|False|Reply (usually OK)|OK|
  
Example output:

```
{
  "reply": "OK"
}
```

#### Set
  
This action is used to set a key to a string value.
There is an optional expiration timeout which will auto remove the key when `expire` seconds have passed

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expire|integer|None|False|Expiration in seconds|None|100|None|None|
|key|string|None|True|Key to set|None|example:1234:session|None|None|
|value|string|None|True|Value to set|None|active|None|None|
  
Example input:

```
{
  "expire": 100,
  "key": "example:1234:session",
  "value": "active"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|string|False|Reply (usually OK)|OK|
  
Example output:

```
{
  "reply": "OK"
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