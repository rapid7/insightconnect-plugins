# Description

[Grafana](https://grafana.org) is an open platform for analytics and monitoring.
This plugin utilizes the [Grafana HTTP API](http://docs.grafana.org/http_api/) to manage organizations and users.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup



## Technical Details

### Actions

#### Update Organization

This action is used to update the name of the organization.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|integer|-1|False|Unique ID of the organization eg. 123 (-1 implies current)|None|
|name|string|None|True|New name for organization|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|Grafana API response, if any|
|success|boolean|False|True, if organization name was updated|

```

{
  "message": "Organization updated",
  "success": true
}

```

#### Delete Organization User

This action is used to a delete user in actual organization.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|integer|-1|False|Unique ID of the organization eg. 123 (-1 implies current)|None|
|user_id|integer|None|True|Unique ID of the user eg. 123|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|Grafana API response, if any|
|success|boolean|False|True, if the user was deleted|

```

{
  "success": true,
  "message": "User removed from organization"
}

```

#### Search Users

This action is used to search users.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]search_user|False|List of all users|

```

{
  "users": [
    {
      "id": 1,
      "isAdmin": true,
      "login": "admin",
      "name": "admin2",
      "email": "admin@localhost"
    }
  ]
}

```

#### Get Organization Users

This action is used to get all users within the organization.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|integer|-1|False|Unique ID of the organization eg. 123 (-1 implies current)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]organization_user|False|List of all organization users|

```

{
  "users": [
    {
      "role": "Admin",
      "orgId": 1,
      "login": "admin",
      "email": "admin@localhost",
      "userId": 1
    }
  ]
}

```

#### Delete Global User

This action is used to delete a global user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|integer|None|True|Unique ID of the user eg. 123|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|Grafana API response, if any|
|success|boolean|False|True, if the user was deleted|

```

{
  "message": "User deleted",
  "success": true
}

```

#### Proxy Call to Data Source

This action is used to proxy all calls to the actual datasource.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|path|string|None|False|Path to be called at datasource eg. `/logstash/_search`|None|
|datasource_id|integer|None|True|Unique ID of the Datasource eg. 123|None|
|parameters|object|None|False|Query Parameters, if any, to be used for the request|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|object|False|Data returned from the datasource|

This sample is from a call made to the `/query` endpoint of an elasticsearch datasource.

```

{
  "response": {
    "results": [
      {
        "series": [
          {
            "values": [
              [
                "_internal"
              ],
              [
                "komand"
              ]
            ],
            "name": "databases",
            "columns": [
              "name"
            ]
          }
        ],
        "statement_id": 0
      }
    ]
  }
}

```

#### Update Organization User

This action is used to update the role of the user in actual organization.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|integer|-1|False|Unique ID of the organization eg. 123 (-1 implies current)|None|
|role|string|None|True|New role for the user|['Admin', 'Editor', 'Viewer']|
|user_id|integer|None|True|Unique ID of the user eg. 123|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|Grafana API response, if any|
|success|boolean|False|True, if the user was updated|

```

{
  "success": true,
  "message": "Organization user updated"
}

```

#### Get User

This action is used to get a single user by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|integer|None|True|Unique ID of the user eg. 123|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|single_user|False|Details of the requested user|

```

{
  "user": {
    "name": "admin2",
    "email": "admin@localhost",
    "login": "admin",
    "orgId": 1,
    "isGrafanaAdmin": true,
    "theme": ""
  }
}

```

#### Add Organization User

This action is used to add a global user to the organization.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|integer|-1|False|Unique ID of the organization eg. 123 (-1 implies current)|None|
|login_or_email|string|None|True|Username or Email ID of the global user|None|
|role|string|None|True|Role for the global user in the organization|['Admin', 'Editor', 'Viewer']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|Grafana API response, if any|
|success|boolean|False|True, if the user was added|

```

{
  "message": "User added to organization",
  "success": true
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Grafana](https://grafana.org)
* [Grafana HTTP API](http://docs.grafana.org/http_api/)

