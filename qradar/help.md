# Description

[QRadar](https://www-03.ibm.com/software/products/en/qradar) is an enterprise security information and event management solution from IBM. The QRadar plugin allows you to run Ariel queries and retrieve policy offense data.
This plugin utilizes the [QRadar API](https://www.ibm.com/support/knowledgecenter/SS42VS_7.3.0/com.ibm.qradar.doc/qradar_IC_welcome.html).

# Key Features

* Run Ariel queries and analyze the results
* Get offense data
* Add data to reference lists

# Requirements

* Administrative credentials to QRadar
* An API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|credential_secret_key|None|True|Host URL|None|
|credentials|credential_username_password|None|False|Basic auth username and password|None|
|api_key|credential_secret_key|None|False|An API key, an authorized service token is recommended|None|

## Technical Details

### Actions

#### Add Data to Reference Data Lists

This action is used to add data to reference_data lists.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|timeout_type|string|UNKNOWN|False|Indicates if the Time to Live interval is based on when the data was first seen or last seen|['FIRST_SEEN', 'LAST_SEEN', 'UNKNOWN']|
|time_to_live|string|None|False|Optional\: The time to live interval, for example\: '1 month' or '5 minutes'|None|
|element_type|string|None|True|The element type for the values allowed in the reference set. The allowed values are\: ALN (alphanumeric), ALNIC (alphanumeric ignore case), IP (IP address), NUM (numeric), PORT (port number) or DATE. Note that date values need to be represented in milliseconds since the Unix Epoch January 1st 1970.|['ALN', 'ALNIC', 'IP', 'NUM', 'PORT', 'DATE']|
|name|string|None|True|The name of the reference set being created|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|time_to_live|string|False|Time to live|
|element_type|string|False|Element type|
|name|string|False|Name|
|timeout_type|string|False|Timeout type|
|creation_time|number|False|Creation time|
|number_of_elements|number|False|Number of elements|

Example output:

```

{
  "creation_time": 42,
  "element_type": "String <one of: ALN, NUM, IP, PORT, ALNIC, DATE>",
  "name": "String",
  "number_of_elements": 42,
  "time_to_live": "String",
  "timeout_type": "String <one of: UNKNOWN, FIRST_SEEN, LAST_SEEN>"
}

```

#### Retrieve Offenses

This action is used to retrieve a list of offenses currently in the system.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|offenses|[]offense|True|None|

Example output:

```

[
  {
    "credibility": 42,
    "source_address_ids": [
      42
    ],
    "remote_destination_count": 42,
    "local_destination_address_ids": [
      42
    ],
    "assigned_to": "String",
    "local_destination_count": 42,
    "source_count": 42,
    "start_time": 42,
    "id": 42,
    "destination_networks": [
      "String"
    ],
    "inactive": true,
    "protected": true,
    "policy_category_count": 42,
    "description": "String",
    "category_count": 42,
    "domain_id": 42,
    "relevance": 42,
    "device_count": 42,
    "security_category_count": 42,
    "flow_count": 42,
    "event_count": 42,
    "offense_source": "String",
    "status": "String <one of: OPEN, HIDDEN, CLOSED>",
    "magnitude": 42,
    "severity": 42,
    "username_count": 42,
    "closing_user": "String",
    "follow_up": true,
    "closing_reason_id": 42,
    "close_time": 42,
    "source_network": "String",
    "last_updated_time": 42,
    "categories": [
      "String"
    ],
    "offense_type": 42
  }
]

```

#### Get Ariel Query Results

This action is used to gets the results of an ariel query by search ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|search_id|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status|
|record_count|integer|False|Record count|
|desired_retention_time_msec|integer|False|Desired retention time in ms|
|error_messages|[]error_messages|False|Error messages|
|data_total_size|integer|False|Data total size|
|index_file_count|integer|False|Index file count|
|data_file_count|integer|False|Data file count|
|compressed_data_total_size|integer|False|Compressed data total size|
|query_execution_time|integer|False|Query execution time|
|index_total_size|integer|False|Total size of index|
|save_results|boolean|False|Save results|
|processed_record_count|integer|False|Processed record count|
|compressed_data_file_count|integer|False|Compressed data file count|
|cursor_id|string|False|Cursor ID|
|progress|integer|False|Progress|
|search_id|string|False|ID of the search|

Example output:

```

{
  "compressed_data_file_count": 42,
  "compressed_data_total_size": 42,
  "cursor_id": "String",
  "data_file_count": 42,
  "data_total_size": 42,
  "desired_retention_time_msec": 42,
  "error_messages": [
    {
      "code": "String",
      "contexts": [
        "String"
      ],
      "message": "String",
      "severity": "String <one of: INFO, WARN, ERROR>"
    }
  ],
  "index_file_count": 42,
  "index_total_size": 42,
  "processed_record_count": 42,
  "progress": 42,
  "query_execution_time": 42,
  "record_count": 42,
  "save_results": true,
  "search_id": "73045ac5-b5ca-47af-a880-23db4f487fec",
  "status": "String <one of: WAIT, EXECUTE, SORTING, COMPLETED, CANCELED, ERROR>"
}

```

#### Query Data with Ariel

This action is used to asynchronously query data using the ariel query language.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_id|string|False|ID of the search|

Example output:

```

{
  "search_id": "73045ac5-b5ca-47af-a880-23db4f487fec"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.2 - New spec and help.md format for the Hub
* 2.0.1 - New spec and help.md format for the Hub
* 2.0.0 - Support web server mode | Update to new credential types | Rename "Add Data to Reference_Data Lists" action to "Add Data to Reference Data Lists"
* 1.0.0 - Finalize plugin
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [QRadar](https://www-03.ibm.com/software/products/en/qradar)
* [QRadar API](https://www.ibm.com/support/knowledgecenter/SS42VS_7.3.0)

