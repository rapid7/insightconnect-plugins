# Description

[SQLAlchemy](http://docs.sqlalchemy.org/en/latest/) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
This plugin allows users to run and execute queries against a SQL database.

# Key Features

* Run SQL queries

# Requirements

* Type of SQL database (MSSQL, MySQL, PostgreSQL)
* The host and port of your SQL database
* Name of your SQL database
* Credentials (username and password) for your SQL database

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Database username and password|None|{ "username": "user@example.com", "password": "mypassword"}|
|db|string|None|True|Database name|None|database_name|
|host|string|None|True|Database hostname|None|198.51.100.1|
|port|string|None|False|Database port|None|443|
|type|string|None|True|Database type (MSSQL, MySQL, PostgreSQL)|['MSSQL', 'MySQL', 'PostgreSQL']|MySQL|

Example input:

```
{
  "credentials": {
    "username": "user@example.com",
    "password": "mypassword"
  },
  "db": "database_name",
  "host": "198.51.100.1",
  "port": 443,
  "type": "MySQL"
}
```

## Technical Details

### Actions

#### Query

This action is used to run an arbitrary SQL query against the connected database.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|parameters|object|None|False|Parameters for query|None|{ "name": "user" }|
|query|string|None|True|Query to run|None|SELECT * FROM example WHERE name=:name|

Example input:

```
{
  "parameters": {
    "name": "user" 
  },
  "query": "SELECT * FROM example WHERE name=:name"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|header|[]string|False|Array of header fields for the columns|
|results|[]object|False|Result rows, each as an object with header keys|
|status|string|True|Status message|

Example output:

```
{
  "header": [
    "name",
    "surname",
    "index",
    "alias"
  ],
  "results": [
    {
      "name": "User",
      "index": "1",
      "Surname": "Example",
      "alias": "Test"
    }
  ],
  "status": "operation success"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For the SQL query action, be sure that your query is valid SQL.

# Version History

* 3.0.1 - Close database connection after use
* 3.0.0 - Add example input and title in connection and Query action | Update python version to `python-3-37-plugin:3` | Add `USER` in Dockerfile | Update `psycopg2` and `mysqlclient` version | Code refactor in connection.py, util.py and Query action.py
* 2.0.7 - Add supported databases as a drop-down list | Add example inputs
* 2.0.6 - Fix issue where connection test always success
* 2.0.5 - New spec and help.md format for the Extension Library
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
