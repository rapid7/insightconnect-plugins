# Description

[Kolide](https://www.kolide.co/) is a state of the art host monitoring platform tailored to security experts.
Leveraging Facebook's battle-tested osquery project, Kolide delivers fast answers to big questions.

This plugin utilizes the [Kolide API](https://github.com/kolide/fleet/tree/master/docs/api).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|https\://localhost\:8080|True|URL to connect to|None|
|api_token|credential_secret_key|None|True|API token for Kolide|None|
|ssl_verify|boolean|False|True|Verify SSL certificate|None|

## Technical Details

### Actions

#### Create Query

This action is used to create a new query in Kolide

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Name of query|None|
|description|string|None|True|Description of query|None|
|query|string|None|True|Query to run on fleet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|False|Results from creating a new query|

Example output:

```
{
  "query":{
    "created_at":"0001-01-01T00:00:00Z",
    "updated_at":"0001-01-01T00:00:00Z",
    "deleted_at":null,
    "deleted":false,
    "id":13,
    "name":"Komand Test Query",
    "description":"Create Test Query",
    "query":"Select * from users",
    "saved":true,
    "author_id":1,
    "author_name":"",
    "packs":[

    ]
  }
}
```

#### Run Query

This action is used to run selected query on fleet.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Query to run|None|
|hosts|[]integer|None|False|A list of host IDs the query will be ran on|None|
|labels|[]integer|None|False|A list of label IDs the query will be ran on|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|False|Results from the query|

Example output:

```
{
  "campaign":{
    "created_at":"0001-01-01T00:00:00Z",
    "updated_at":"0001-01-01T00:00:00Z",
    "deleted_at":null,
    "deleted":false,
    "id":11,
    "query_id":14,
    "status":0,
    "user_id":1
  }
}
```

#### Get Query

This action is used to get query details on past queries by specified query ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|queryid|string|None|True|Query ID from a query already ran|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|False|Results from the query|

Example output:

```
{
  "query":{
    "created_at":"2019-02-06T19:42:33Z",
    "updated_at":"2019-02-06T19:42:33Z",
    "deleted_at":null,
    "deleted":false,
    "id":12,
    "name":"distributed_komand_1549482153",
    "description":"",
    "query":"SELECT * FROM users",
    "saved":false,
    "author_id":1,
    "author_name":"komand",
    "packs":[

    ]
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

* 2.0.0 - New actions Create Query, Run Query and Get Query | Removed action Query Node
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Use new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Kolide](https://www.kolide.co/)

