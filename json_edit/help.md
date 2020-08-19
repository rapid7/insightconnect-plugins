# Description

JSON Edit is a data utility that allows for the manipulation of [JSON](https://www.json.org/json-en.html) data. This plugin provides the ability to delete keys and update values in a JSON object.

# Key Features

* Edit JSON string

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Add Key

This action is used to add a JSON key.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|key|string|None|True|JSON key to add|None|E-mail|
|value|string|None|True|Value to add|None|user@example.com|

Example input:

```
{
  "key": "E-mail",
  "value": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|json|added_json|True|JSON object|

Example output:

```
{
  "json": {
    "key": "E-mail",
    "value": "user@example.com"
  }
}
```

#### Update

This action is used to update a value by key. It updates any values matching the key for an `object` or an `array` of `object`s.
A user must supply one of these data structure as input for the plugin to update.

It will iterate through each dictionary but is not recursive so nested dictionaries will not be operated on.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|array|[]object|None|False|Array of JSON objects|None|None|
|key|string|None|True|JSON key to update|None|None|
|object|object|None|False|JSON object|None|None|
|value|string|None|True|New value|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|json|[]object|True|Array of objects|

Example output:

```

{
  "json": [
    {
      "hostname": "BIGFIX-SRV",
      "ip": "Sanitized!",
      "os": "Win2012 6.2.9200"
    },
    {
      "hostname": "BIGFIX-DC",
      "ip": "Sanitized!",
      "os": "Win10"
    }
  ]
}

```

#### Delete

This action is used to delete a key by name. It deletes any matching keys for an `object` or an `array` of `object`s.
A user must supply one of these data structure as input for the plugin to update.

It will iterate through each dictionary but is not recursive so nested dictionaries will not be operated on.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|array|[]object|None|False|Array of JSON objects|None|None|
|key|string|None|True|Key to remove|None|None|
|object|object|None|False|JSON object|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|json|[]object|True|Array of objects|

Example output:

```

{
  "json": [
    {
      "hostname": "BIGFIX-SRV",
      "os": "Win2012 6.2.9200"
    },
    {
      "hostname": "BIGFIX-DC",
      "os": "Win10 6.2.9200"
    }
  ]
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### added_json

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Key|string|False|JSON key|
|Value|string|False|JSON value|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.1.0 - New action Add Key
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.0 - Initial plugin

# Links

## References

* [JSON](https://www.json.org/)
