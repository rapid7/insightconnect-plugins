# Description

[InfluxDB](https://docs.influxdata.com/influxdb) is a scalable data store for metrics, events, and real-time analytics.
This plugin utilizes the [InfluxDB API](https://docs.influxdata.com/influxdb/v1.2/tools/api/).

# Key Features

* Post metrics
* Retrieve metrics

# Requirements

* An InfluxDB server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|server|string|http://localhost:8086|True|InfluxDB API Server|None|

## Technical Details

### Actions

#### Write to Database

This action is used to write data to a pre-existing database.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|False|Sets the username for authentication|None|
|retention_policy|string|None|False|Sets the target retention policy for the write|None|
|consistency|string|None|False|Sets the write consistency for the point. One of [any,one,quorum,all]|['any', 'one', 'quorum', 'all']|
|database_name|string|None|True|Database name|None|
|password|password|None|False|Set the password for authentication|None|
|data|string|None|False|Data to be written into the database. Must be in Line Protocol format. See https://docs.influxdata.com/influxdb/v1.2/write_protocols/line_protocol_tutorial/|None|
|precision|string|None|False|Sets the precision for the supplied Unix time values|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|Status code|
|message|string|False|Message|

#### Query Database

This action is used to query data and manage databases, retention policies, and users.

An example query would be `select * from mytable`

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|False|Sets the username for authentication|None|
|epoch|string|None|False|Returns epoch timestamps with the specified precision. Default is nanoseconds|None|
|password|password|None|False|Sets the password for authentication|None|
|query|string|None|False|Database query. Must follow InfluxQL syntax. See https://docs.influxdata.com/influxdb/v1.2/query_language/|None|
|database_name|string|None|True|Database name|None|
|chunked|string|None|False|If set to true, InfluxDB chunks responses by series or by every 10,000 points, whichever occurs first. If set to a specific value, InfluxDB chunks responses by series or by that number of points|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results|

#### Ping Database

This action is used to check the status of your InfluxDB instance and your version of InfluxDB.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status|
|version|string|False|Version|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### point

|Name|Type|Required|Description|
|----|----|--------|-----------|
|columns|[]string|False|None|
|name|string|False|None|
|values|[][]string|False|None|

#### result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|error|string|False|None|
|series|[]point|False|None|
|statement_id|integer|False|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [InfluxDB](https://docs.influxdata.com/influxdb)
* [InfluxDB API](https://docs.influxdata.com/influxdb/v1.2/tools/api/)
