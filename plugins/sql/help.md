# Description

[SQLAlchemy](http://docs.sqlalchemy.org/en/latest/) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
This plugin allows users to run and execute queries against a SQL database

# Key Features

* Run SQL queries

# Requirements

* Type of SQL database (MSSQL, MySQL, PostgreSQL)
* The host and port of your SQL database
* Name of your SQL database
* Credentials (username and password) for your SQL database

# Supported Product Versions

* MySQL 8.0.21
* MSSQL 2019 15.0.4223.1
* PostgresSQL 13.0

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Database username and password|None|{ "username": "user@example.com", "password": "mypassword"}|None|None|
|db|string|None|True|Database name|None|database_name|None|None|
|host|string|None|True|Database hostname|None|198.51.100.1|None|None|
|port|string|None|False|Database port|None|1433|None|None|
|type|string|None|True|Database type (MSSQL, MySQL, PostgreSQL)|["MSSQL", "MySQL", "PostgreSQL"]|MySQL|None|None|

Example input:

```
{
  "credentials": {
    "password": "mypassword",
    "username": "user@example.com"
  },
  "db": "database_name",
  "host": "198.51.100.1",
  "port": 1433,
  "type": "MySQL"
}
```

## Technical Details

### Actions


#### Query

This action is used to run an arbitrary SQL query against the connected database

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|parameters|object|None|False|Parameters for query|None|{ "name": "user" }|None|None|
|query|string|None|True|Query to run|None|SELECT * FROM example WHERE name=:name|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|header|[]string|False|Array of header fields for the columns|["name", "surname", "index", "alias"]|
|results|[]object|False|Result rows, each as an object with header keys|[{"name": "User", "index": "1", "Surname": "Example", "alias": "Test"}]|
|status|string|True|Status message|operation success|
  
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
      "Surname": "Example",
      "alias": "Test",
      "index": "1",
      "name": "User"
    }
  ],
  "status": "operation success"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 3.0.8 - Bumped `SQLAlchemy` and `psycopg2` and removed 'SQLAlchemy-Utils' | SDK Bump to 6.3.3 | Updated query handling
* 3.0.7 - Bumped version of SQLAlchemy used to version 1.2.18 | bump version of SDK used to version 5
* 3.0.6 - Update plugin runtime to InsightConnect
* 3.0.5 - Update pymssql version library to support latest MSSQL update 2019 15.0.4223.1
* 3.0.4 - Fix issue with get method's keyword argument in Query action
* 3.0.3 - Change example input Port in Connection | Update file util.py to Python3
* 3.0.2 - Add default PORT for MSSQL and MySQL connection
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

* [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/)

## References

* [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/)