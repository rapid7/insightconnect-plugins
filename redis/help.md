# Description

Redis is an in-memory data structure project implementing a distributed, in-memory key-value database with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indexes.

This package allows you to interact with the [Redis](https://redis.io/) database API.

# Key Features

* Set and retrieve data from Redis.

# Requirements

* Connection information for your Redis database

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|Host, e.g. 10.4.4.4|None|
|db|integer|0|True|Db to use usually (0-15)|None|
|port|integer|6379|True|Port|None|

## Technical Details

### Actions

#### Set

This action is used to set a key to a string value.
There is an optional expiration timeout which will auto remove the key when `expire` seconds have passed.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|expire|integer|None|False|Expiration in seconds|None|
|key|string|None|True|Key to set|None|
|value|string|None|True|Value to set|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reply|string|False|Reply (usually OK)|

Example output:

```

{
  "reply": "OK"
}

```

#### List Get

This action is used to get all elements in a list.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|count|integer|1000|False|Max results to return|None|
|key|string|None|True|Key to get|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|values|[]string|False|Values|

Example output:

```

{
  "found": false,
  "values": []
}

```

#### Get

This action is used to get a key. Get will return a value at `key` if found, otherwise found will be false

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|key|string|None|True|Key to get|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|value|string|False|Value|

Example output:

```

{
  "value": "",
  "found": false
}

```

#### Keys

This action is used to return all keys matching a pattern.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pattern|string|None|True|Pattern, e.g. *o*|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Count of keys found|
|keys|[]string|False|Keys returned|

Example output:

```

{
  "count": 27,
  "keys": [
    "hashfoo",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:207f28a4-8787-445b-af29-5e467f77c503",
    "LogonToAssetFilter:821dfdb4-22c2-46fe-b693-752d00802f9d:e9a804f6-1b84-44e9-8e56-e81d06082c57",
    "LogonToAssetFilter:821dfdb4-22c2-46fe-b693-752d00802f9d:316ea7f6-2d1b-44d8-97f9-290460f5b18b",
    "LogonToAssetFilter:821dfdb4-22c2-46fe-b693-752d00802f9d:5c74f7fe-9dfd-440a-8b50-ba0acc49b264",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:3e49f67a-1fbf-4207-84d8-2a88f1032239",
    "CollectorHeartbeat:821dfdb4-22c2-46fe-b693-752d00802f9d:4fa0c9df-c61a-4d99-935e-633ff7c65112",
    "CollectorHeartbeat:a4cabb19-cac1-4e1d-975a-e012d3b68bc8:aa485f7e-854e-4c43-b41c-035baf16b0a7",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:98705784-1c5e-4dc5-af96-838f59ee369b",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:46273cef-0300-4ac6-b9f7-0ccc21d220d4",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:b22dd672-e901-4738-a1dd-7428fbe06749",
    "spring:session:index:org.springframework.session.FindByIndexNameSessionRepository.PRINCIPAL_NAME_INDEX_NAME:dev",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:538151a3-5588-49e3-9199-0e06f410dac1",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:d0d31086-4891-4da8-a649-900c672a2c07",
    "LogonToAssetFilter:821dfdb4-22c2-46fe-b693-752d00802f9d:1d7677e6-f4a7-48d6-bb31-7cfc0fcc6089",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:9002df97-dabe-4024-9017-2452f3cc56f1",
    "CollectorHeartbeat:821dfdb4-22c2-46fe-b693-752d00802f9d:a652b834-fa52-438a-885a-609d84bc44cd",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:c4be1a2a-b5e2-4f52-9b82-815fd26ca32d",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:54eb9391-9524-487b-8352-94e8627bf5a3",
    "CollectorHeartbeat:1f78ace5-bdef-4512-abed-4c96548dc043:c8198ec1-5afb-4561-bb0f-d1a308d94471",
    "keylist",
    "LogonToAssetFilter:821dfdb4-22c2-46fe-b693-752d00802f9d:3e8c29da-fa56-4643-9b1e-5c74f90c1ae6",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:4cafcba4-0614-48b5-9ba9-418c5a3bb95e",
    "LogonToAssetFilter:1f78ace5-bdef-4512-abed-4c96548dc043:14038b45-f012-41fc-9c22-ee824e9700c4",
    "CollectorHeartbeat:1f78ace5-bdef-4512-abed-4c96548dc043:52253bef-7a4c-4f09-9d3b-f188f1477f41",
    "LogonToAssetFilter:821dfdb4-22c2-46fe-b693-752d00802f9d:77efac95-c6ff-437d-b1c4-e5d021ad2bd7",
    "LogonToAssetFilter:821dfdb4-22c2-46fe-b693-752d00802f9d:acc4c70f-9440-4ba5-8610-4602935752af"
  ]
}

```

#### Hash Set

This action is used to set a given key to a key:value object. All values must be strings.
There is an optional expiration timeout which will auto remove the key when `expire` seconds have passed.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|expire|integer|None|False|Expiration in seconds|None|
|values|object|None|True|Object hash field:value to set|None|
|key|string|None|True|Key|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reply|string|False|Reply (usually OK)|

Example output:

```

{
  "reply": "OK"
}

```

#### List Push

This action is used to list key's push.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|expire|integer|None|False|Expiration in seconds|None|
|key|string|None|True|Key|None|
|value|string|None|True|Value to append|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reply|string|False|Reply (usually OK)|

Example output:

```

{
  "reply": "OK"
}

```

#### Hash Get

This action is used to return all hash values at `key`. If no hash values are found `false` is returned.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|key|string|None|True|Key to get|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|values|object|False|Values|

Example output:

```

{
  "values": {},
  "found": false
}

```

#### Delete

This action is used to delete a key.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|key|string|None|True|Key to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Number of keys deleted|

Example output:

```

{
  "count": 1
}

```

#### Hash Increment By

This action is used to increments the number stored at field in the hash stored at key by increment.
If key does not exist, a new key holding a hash is created. If field does not exist the value is set to 0 before the operation is performed

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|key|string|None|True|Key to lookup|None|
|field|string|None|True|Field to increment|None|
|value|integer|0|True|How much to increment by|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|integer|False|Result returned after operation is ran|

Example output:

```

{
  "result": 18
}

```

#### Hash Multi Get

This action is used to returns the values associated with the specified fields in the hash stored at key.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|key|string|None|True|Key to get|None|
|fields|[]string|None|False|Fields to retrieve values from|None|
|get_all|boolean|False|True|Get all values|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|values|object|False|Values returned from HMGET|

Example output:

```

{
  "values": {
    "address": "192.168.0.1",
    "type": "ipv4",
    "subnet": "255.255.255.0"
  }
}

```

#### Hash Multi Set

This action is used to sets the specified fields to their respective values in the hash stored at key.
This command overwrites any specified fields already existing in the hash. If key does not exist, a new key holding a hash is created

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|key|string|None|True|Key|None|
|values|object|None|True|Object hash field:value to set|None|
|expire|integer|None|False|Expiration in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reply|boolean|False|Reply (usually OK)|

Example output:

```

{
  "reply": true
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Support web server mode | Add actions HMSET, HMGET and HINCRBY
* 0.1.2 - Update to new plugin architecture, fix action "keys"
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [REDIS](https://redis.io/)

