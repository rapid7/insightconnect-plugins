# Description

The [Microsoft SQL](https://www.microsoft.com/en-us/sql-server/default.aspx) plugin allows user to run queries against Microsoft SQL databases.

# Key Features

* Run Microsoft SQL queries

# Requirements

* Database credentials
* Connection information to your database

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Database username and password|None|None|
|db|string|None|True|Database name|None|None|
|host|string|None|True|Database hostname|None|None|
|port|number|None|False|Database port. Port 1433 will be used if this is left blank|None|None|

Example input:

```
{
  "credentials": {
    "password": "password",
    "username": "username"
  },
  "db": "test",
  "host": "192.168.10.1",
  "port": 1433
}
```

## Technical Details

### Actions

#### Query

This action is used to run an SQL query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|parameters|[]object|None|False|Parameters for query. Parameters should be input as an ordered list of dictionaries e.g. [{"key1": "John Doe"},{"Key2": 23}] The values will be input into the query in order. Parameter values are represented by `?` in the query|None|None|
|query|string|None|True|Query to run|None|None|

Example input:

```
{
  "parameters": [{"key1":"Jane"}],
  "query": "select * from Person Where FirstName=?"
}
```

##### Output

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

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The `username` input in the plugin Connection must use `username@host` format,
e.g. user@example.database.windows.net.

This plugin uses ODBC driver version 17.
This plugin uses version-specific drivers for Debian 9.x.

# Version History

* 1.0.2 - Fix execute insert and update
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [pyodbc](https://github.com/mkleehammer/pyodbc/wiki)
* [Microsoft SQL](https://www.microsoft.com/en-us/sql-server/default.aspx)

