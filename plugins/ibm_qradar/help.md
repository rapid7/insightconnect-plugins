# Description

Orchestrate and automate ariel search and automate the offence management using the IBM Qradar

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|True|Hostname for the Qradar application|None|None|
|password|password|None|True|Qradar Password|None|None|
|username|string|None|True|Qradar Username|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Get Ariel Search By Id

This action is used to get Ariel Search By Id.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|poll_interval|number|None|False|Poll interval is the number of seconds to recheck until the search gets COMPLETED.|None|None|
|search_id|string|None|True|Specific Search Id|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search|False|Json Data of the Search|

Example output:

```
{
  "completed": true,
  "data_file_count": 20,
  "index_total_size": 0,
  "cursor_id": "a75310e4-01ed-423c-89e9-3a72f62b6eed",
  "data_total_size": 2254061,
  "desired_retention_time_msec": 86400000,
  "status": "COMPLETED",
  "subsearch_ids": [],
  "compressed_data_file_count": 0,
  "processed_record_count": 73122,
  "progress_details": [],
  "query_execution_time": 138,
  "search_id": "a75310e4-01ed-423c-89e9-3a72f62b6eed",
  "size_on_disk": 49160480,
  "compressed_data_total_size": 0,
  "index_file_count": 0,
  "progress": 100,
  "query_string": "SELECT * FROM events LAST 10 MINUTES",
  "record_count": 73122,
  "save_results": false,
  "snapshot": null
}
```

#### Start Ariel Search

This action is used to start Ariel Search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|AQL|string|None|False|Aql query to perform the search.|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search|False|Json Data of the Search|

Example output:

```

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### SearchDto

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Completed|boolean|False|None|
|Compressed Data File Count|number|False|None|
|Compressed Data Total Size|number|False|None|
|Cursor Id|string|False|None|
|Data File Count|number|False|None|
|Data Total Size|number|False|None|
|Desired Retention Time Msec|number|False|None|
|Index File Count|number|False|None|
|Index Total Size|number|False|None|
|Processed Record Count|number|False|None|
|Progress|number|False|None|
|Progress Details|[]object|False|None|
|Query Execution Time|number|False|None|
|Query String|string|False|None|
|Record Count|number|False|None|
|Save Results|boolean|False|None|
|Search Id|string|False|None|
|Size On Disk|number|False|None|
|Snapshot|object|False|None|
|Status|string|False|None|
|Subsearch Ids|[]string|False|None|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [IBM Qradar](LINK TO PRODUCT/VENDOR WEBSITE)

