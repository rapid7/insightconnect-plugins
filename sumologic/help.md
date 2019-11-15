# Description

[Sumo Logic](https://www.sumologic.com/) is a cloud log management and metrics monitoring solution used by IT, Security and Development teams across all customer sizes.
The Sumo Logic plugin allows you to run a Sumo Logic query and view the results.

# Key Features

* Run a Sumo Logic search query and return the results

# Requirements

* Sumo Logic access key
* Sumo Logic access id

# Documentation

## Setup

This plugin requires a Sumo Logic access ID and access key.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|access_key|credential_secret_key|None|True|Access key|None|
|access_id|credential_secret_key|None|True|Access ID|None|

## Technical Details

### Actions

#### Search

This action is used to run a Sumo Logic search query and return the results.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|timeone|string|UTC|False|Timezone (Default is UTC)|None|
|to_time|string|None|False|To time. Must be either ISO 8601 datetimes, or epoch milliseconds. If not provided, default is now.|None|
|query|string|None|True|Query|None|
|page_offset|integer|0|False|Page offset for search|None|
|timeout|integer|60|False|Timeout in seconds|None|
|from_time|string|None|False|From time. Must be either ISO 8601 datetimes, or epoch milliseconds. If not\: searches 24 hours back by default.|None|
|page_limit|integer|100|False|Number of messages to return per page|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|fields|[]field|False|Fields returned|
|page_count|integer|False|Number of pages|
|messages|[]object|False|Messages returned|
|total_count|integer|False|Total count of messages matched|

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

## References

* [Sumo Logic](https://www.sumologic.com/)

