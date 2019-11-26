# Description

[New Relic](https://www.newrelic.com) monitors the performance of applications and infrastructure.
This plugin utilizes the [newrelic-api](https://pypi.python.org/pypi/newrelic-api/1.0.4) python library.

# Key Features

* Monitor system integrity

# Requirements

* Requires an API Key from the New Relic service

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key|None|

## Technical Details

### Actions

#### List Users

This action is used to show a paginated list of all users. Users can be filtered by their IDs or email.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|False|Filter by user email|None|
|ids|string|None|False|Filter by user IDs. IDs should be a comma separated list eg 123,345,678|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user_list|[]user|False|List of users that meet the filter criteria|

Example output:

```

{
  "user_list": [
    {
      "id": 2162712,
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "jane_doe@example.com",
      "role": "owner"
    }
  ]
}

```

#### Show User

This action is used to return a single user, identified by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user_found|boolean|False|Returns true if user with specified ID found|
|user_information|user|False|Information on the user|

Example output:

```

{
  "user_found": true,
  "user_information": {
    "user": {
      "id": 2162712,
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "jane_doe@company.com",
      "role": "owner"
    }
  }
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.2 - New spec and help.md format for the Hub
* 2.0.1 - New spec and help.md format for the Hub
* 2.0.0 - Support web server mode and update to new credential types
* 1.0.0 - Initial plugin

# Links

## References

* [New Relic API Docs](http://new-relic-api.readthedocs.io/en/develop/examples.html)
* [newrelic-api](https://pypi.python.org/pypi/newrelic-api/1.0.4)

