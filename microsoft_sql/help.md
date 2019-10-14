# Microsoft SQL

## About

[Microsoft SQL](https://www.microsoft.com/en-us/sql-server/default.aspx) database module.

## Actions

### Query

This action is used to run an SQL query.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|parameters|object|None|False|Parameters for query|None|
|query|string|None|True|Query to run|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|header|[]string|False|Array of header fields for the columns|
|results|[]object|False|Result rows, each as an object with header keys|

Example output:

```
{
  "header": [
    "PersonId",
    "FirstName",
    "MiddelInitial",
    "LastName",
    "DateOfBirth"
  ],
  "results": [
    {
      "PersonId": 1,
      "FirstName": "John",
      "MiddelInitial": "J",
      "LastName": "Smith",
      "DateOfBirth": "2019-08-19"
    },
    {
      "PersonId": 2,
      "FirstName": "Jane",
      "MiddelInitial": "J",
      "LastName": "Doe",
      "DateOfBirth": "2019-08-12"
    }
  ]
}
```

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Database username and password|None|
|db|string|None|True|Database name|None|
|host|string|None|True|Database hostname|None|
|port|string|None|False|Database port. If blank port 1433 will be used|None|

## Troubleshooting

The `username` input in the plugin Connection must use `username@host` format,
e.g. jdoe@example.database.windows.net.

This plugin uses ODBC driver version 17.
This plugin uses version-specific drivers for Debian 9.x.

## Workflows

Examples:

* Query a Microsoft SQL Server database

## Versions

* 1.0.0 - Initial plugin

## References

* [pyodbc](https://github.com/mkleehammer/pyodbc/wiki)
* [Microsoft SQL](https://www.microsoft.com/en-us/sql-server/default.aspx)

## Custom Output Types

_This plugin does not contain any custom output types._
