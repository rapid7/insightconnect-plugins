# Description

[SQLAlchemy](http://docs.sqlalchemy.org/en/latest/) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
This plugin allows users to run and execute queries against a SQL database.

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
  |type|string|None|True|Database type (i.e. mysql, postgres... etc.)|None|
  |host|string|None|True|Database hostname|None|
  |port|string|None|False|Database port|None|
  |db|string|None|True|Database name|None|
  |credentials|credential_username_password|None|True|Database username and password|None|

## Technical Details

### Actions

#### Query

This action is used to run an arbitrary SQL query against the connected database.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|query to run|None|
|parameters|object|None|True|parameter for parameterized query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Status message|
|header|[]string|False|Array of header fields for the columns|
|results|[]object|False|Result rows, each as an object with header keys|

Example output:

```
"output": {
  "status": "operation success",
  "header": [
    "PluginName"
  ],
  "results": [
    {
      "PluginName": "Test Plugin Name"
    }
  ]
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For the SQL query action, be sure that your query is valid SQL.

# Version History

* 2.0.4 - Add support for Microsoft SQL server
* 2.0.3 - Fix issue where credentials used incorrect username | Update help
* 2.0.2 - Fix issue where credentials was spelled wrong in connection
* 2.0.1 - Add MSSQL support
* 2.0.0 - Update to new credential types | Rename "query" action to "Query"
* 1.0.0 - Add port to connection, make results array of objects | Support web server mode
* 0.1.0 - Initial plugin

# Links

## References

* [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/)

