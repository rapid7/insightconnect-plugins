# Description

[Kintone](https://www.kintone.com/) allows for custom workflows and data management for businesses and non-profits in one place.

# Key Features

* Store and retrieve data

# Requirements

* API Key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api-key|credential_secret_key|None|True|API key|None|

## Technical Details

### Actions

#### Get Record by ID

This action is used to get a record by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|Application ID|None|
|record_id|string|None|True|Record ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|record|object|True|Record|

Example output:

```
{
  "record": {
    "Text_0": {
        "type": "SINGLE_LINE_TEXT",
        "value": "Some Test Data"
    },
    "Updated_datetime": {
        "type": "UPDATED_TIME",
        "value": "2019-07-18T19:21:00Z"
    },
    "Created_datetime": {
        "type": "CREATED_TIME",
        "value": "2019-07-18T19:21:00Z"
    },
    "Record_number": {
        "type": "RECORD_NUMBER",
        "value": "1"
    },
    "Text": {
        "type": "SINGLE_LINE_TEXT",
        "value": "A Test Title"
    },
    "Created_by": {
        "type": "CREATOR",
        "value": {
            "code": "jmcadams@example.com",
            "name": "Joseph McAdams"
        }
    },
    "$revision": {
        "type": "__REVISION__",
        "value": "1"
    },
    "Updated_by": {
        "type": "MODIFIER",
        "value": {
            "code": "jmcadams@example.com",
            "name": "Joseph McAdams"
        }
    },
    "$id": {
        "type": "__ID__",
        "value": "1"
    }
  }
}
```

#### Write Record

This action is used to write a record.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|Application ID|None|
|record_body|object|None|True|Record Body as JSON|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|add_record_response|object|True|Add Record Response|

Example output:

```
{
  "add_record_response": {
    "id": "6",
    "revision": "1"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - Fix issue where SSL Verify was set to false
* 1.0.0 - Initial plugin

# Links

## References

* [Kintone](https://www.kintone.com/)
* [Kintone Developer Portal](https://developer.kintone.io/hc/en-us)

