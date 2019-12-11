# Description

[Presto](https://prestodb.io/) is an open source distributed SQL query engine for running interactive analytic 
queries against data sources of all sizes ranging from gigabytes to petabytes. The Presto plugin will allow you to 
run database operations with Presto.

This plugin utilizes the [PyHive](https://github.com/dropbox/PyHive) library.

# Key Features

* Run a PrestoDB database operation

# Requirements

* PrestoDB credentials
* PrestoDB connection information

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|False|Username|None|
|poll_interval|integer|1|False|How often to ask the Presto REST interface for a progress update, defaults to a second|None|
|host|string|None|True|Hostname to connect to|None|
|source|string|pyhive|False|Arbitrary identifier (shows up in the Presto monitoring page)|None|
|catalog|string|hive|False|Catalog name|None|
|port|integer|8080|False|Port|None|
|schema|string|default|False|Database name|None|

## Technical Details

### Actions

#### Execute

This action is used to prepare and execute a database operation (query or command).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|operation|string|None|True|Query or command to execute|None|
|parameters|string|None|False|Reserved for future use. Parameters which safely will be passed to operation string|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rows|[]row|True|Rows as sequence of sequences|

Example Output:

```

{
  "rows":
    [
      {
        "row": ["com.facebook.presto.execution:name=queryexecution"]
      },
      {
        "row": ["com.facebook.presto.execution:name=querymanager"]
      },
      {
        "row": ["com.facebook.presto.execution:name=remotetaskfactory"]
      },
      {
        "row": ["com.facebook.presto.execution:name=taskexecutor"]
      }
    ]
}

```

#### Execute One

This action is used to prepare and execute a database operation (query or command) and return only first row.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|operation|string|None|True|Query or command to execute|None|
|parameters|string|None|False|Reserved for future use. Parameters which safely will be passed to operation string|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|row|row|True|Row as sequence|

Example Output:

```

{
  "row": ["com.facebook.presto.execution.scheduler:name=nodescheduler"]
}

```

### Triggers

This plugin does not contain any triggers.

### Troubleshooting

This plugin does not contain any troubleshooting information.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [PyHive](https://github.com/dropbox/PyHive)
* [Presto](https://github.com/prestodb/presto/wiki/HTTP-Protocol)

