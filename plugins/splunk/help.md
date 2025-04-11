# Description

[Splunk](https://www.splunk.com/) captures, indexes, and correlates real-time data in a searchable repository from which it can generate graphs, reports, alerts, dashboards, and visualizations. This plugin allows you to interact with Splunk by hooking alerts to trigger InsightConnect workflows, run (saved) searches, retrieve search results, and even insert data back into Splunk from a workflow

# Key Features

* Run a search query to get the results from your Splunk instance
* Display search results from a specified job
* Run, create, delete, and list saved searches to store and rerun queries over time
* List and modify saved search properties to view and update your reusable queries
* Get saved search job history to retrieve the history of a specified saved search
* Insert events into an index to update your Splunk instance

# Requirements

* Administrative credentials
* Splunk host IP address or hostname
* Splunk API port

# Supported Product Versions

* Splunk SDK 1.7.4

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|False|Username and password|None|{"username":"ExampleUser","password":"ExamplePassword"}|None|None|
|host|string|None|True|Hostname or IP address of Splunk server to connect to|None|splunk.example.com|None|None|
|license|string|None|True|License type for Splunk host|["Enterprise", "Free"]|Free|None|None|
|port|integer|8089|True|Port the Splunk API is listening on. Default is 8089|None|8089|None|None|
|ssl_verify|boolean|None|True|Verify server's SSL/TLS certificate|None|True|None|None|
|use_ssl|boolean|None|True|Whether or not to use SSL|None|True|None|None|

Example input:

```
{
  "credentials": {
    "password": "ExamplePassword",
    "username": "ExampleUser"
  },
  "host": "splunk.example.com",
  "license": "Free",
  "port": 8089,
  "ssl_verify": true,
  "use_ssl": true
}
```

## Technical Details

### Actions


#### Create Saved Search

This action is used to creates a saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|properties|object|None|False|JSON object containing additional properties to save with the saved search|None|{"description":"ExampleDescription","is_scheduled":true}|None|None|
|query|string|None|True|Search query|None|search *|None|None|
|saved_search_name|string|None|True|Name to give to the saved search|None|ExampleSavedSearchName|None|None|
  
Example input:

```
{
  "properties": {
    "description": "ExampleDescription",
    "is_scheduled": true
  },
  "query": "search *",
  "saved_search_name": "ExampleSavedSearchName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|saved_search|object|False|Newly created saved search object|{"name":"ExampleSavedSearchName","search":"index=main sourcetype=access_combined status=200","dispatch.earliest_time":"-1d","dispatch.latest_time":"now"}|
  
Example output:

```
{
  "saved_search": {
    "dispatch.earliest_time": "-1d",
    "dispatch.latest_time": "now",
    "name": "ExampleSavedSearchName",
    "search": "index=main sourcetype=access_combined status=200"
  }
}
```

#### Delete Saved Search

This action is used to deletes a saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|saved_search_name|string|None|True|Name of the saved search to delete|None|ExampleSavedSearchName|None|None|
  
Example input:

```
{
  "saved_search_name": "ExampleSavedSearchName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the deletion was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Display Search Results

This action is used to displays the search results from a job

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|job_id|string|None|True|The Job ID to look up results for|None|12345|None|None|
|timeout|number|None|True|Duration of time, in seconds, to wait for retrieving results|None|5|None|None|
  
Example input:

```
{
  "job_id": 12345,
  "timeout": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|search_results|[]object|False|Search results from a job|[{"_raw":"2023-10-15 12:00:00, INFO - Application started","host":"server-1","source":"/var/log/application.log","sourcetype":"test","index":"main","_time":"2023-10-15T12:00:00","event":{"level":"INFO","message":"Application started"}}]|
  
Example output:

```
{
  "search_results": [
    {
      "_raw": "2023-10-15 12:00:00, INFO - Application started",
      "_time": "2023-10-15T12:00:00",
      "event": {
        "level": "INFO",
        "message": "Application started"
      },
      "host": "server-1",
      "index": "main",
      "source": "/var/log/application.log",
      "sourcetype": "test"
    }
  ]
}
```

#### Get Saved Search Job History

This action is used to returns the job history of a specified saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|saved_search_name|string|None|True|Name of a saved search|None|ExampleSavedSearchName|None|None|
  
Example input:

```
{
  "saved_search_name": "ExampleSavedSearchName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|job_history|[]object|False|Job history belonging to a saved search|[{"name":"ExampleSavedSearchName","app":"search","search":"index=_internal","dispatchState":"DONE","resultCount":100,"runDuration":15000,"cursorTime":"2024-01-29T12:00:00.000-07:00","earliestTime":"2024-01-29T11:00:00.000-07:00","latestTime":"2024-01-29T11:30:00.000-07:00","statusBuckets":300,"ttl":600,"autoSummarize":true}]|
  
Example output:

```
{
  "job_history": [
    {
      "app": "search",
      "autoSummarize": true,
      "cursorTime": "2024-01-29T12:00:00.000-07:00",
      "dispatchState": "DONE",
      "earliestTime": "2024-01-29T11:00:00.000-07:00",
      "latestTime": "2024-01-29T11:30:00.000-07:00",
      "name": "ExampleSavedSearchName",
      "resultCount": 100,
      "runDuration": 15000,
      "search": "index=_internal",
      "statusBuckets": 300,
      "ttl": 600
    }
  ]
}
```

#### Insert

This action is used to insert events into an index

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event|string|None|True|The event to submit|None|User logged in|None|None|
|host|string|None|False|The source host|None|example_host|None|None|
|index|string|None|True|Name of index|None|ExampleIndexName|None|None|
|source|string|None|False|Source of the event|None|ExampleEventSource|None|None|
|source_type|string|None|False|The optional source type value of the event|None|ExampleEventSourceType|None|None|
  
Example input:

```
{
  "event": "User logged in",
  "host": "example_host",
  "index": "ExampleIndexName",
  "source": "ExampleEventSource",
  "source_type": "ExampleEventSourceType"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Boolean value that indicates whether event got inserted or not|True|
  
Example output:

```
{
  "success": true
}
```

#### List Saved Searches

This action is used to lists all saved searches

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|saved_searches|[]object|False|Array of saved search objects|[{"name":"example_saved_search_1","acl":{"app":"search","can_write":"1","modifiable":"1","owner":"admin","sharing":"app"},"content":{"alert.expires":"24h","alert.severity":"2","alert.suppress":"0","alert.track":"1","dispatch.earliest_time":"-1d@d","dispatch.latest_time":"now","displayview":"flashtimeline","enableSched":"1","is_scheduled":"1","search":"index=_internal | stats count by sourcetype","alert.digest_mode":"1","cron_schedule":"0 0 * * *"},"links":{"alternate":"/example_saved_search_1","edit":"/example_saved_search_1","list":"/example_saved_search_1","remove":"/example_saved_search_1","disable":"/example_saved_search_1/disable","dispatch":"/example_saved_search_1/dispatch","alert":"/example_saved_search_1/alert","scheduled_view":"/example_saved_search_1/scheduled_view"}}]|
  
Example output:

```
{
  "saved_searches": [
    {
      "acl": {
        "app": "search",
        "can_write": "1",
        "modifiable": "1",
        "owner": "admin",
        "sharing": "app"
      },
      "content": {
        "alert.digest_mode": "1",
        "alert.expires": "24h",
        "alert.severity": "2",
        "alert.suppress": "0",
        "alert.track": "1",
        "cron_schedule": "0 0 * * *",
        "dispatch.earliest_time": "-1d@d",
        "dispatch.latest_time": "now",
        "displayview": "flashtimeline",
        "enableSched": "1",
        "is_scheduled": "1",
        "search": "index=_internal | stats count by sourcetype"
      },
      "links": {
        "alert": "/example_saved_search_1/alert",
        "alternate": "/example_saved_search_1",
        "disable": "/example_saved_search_1/disable",
        "dispatch": "/example_saved_search_1/dispatch",
        "edit": "/example_saved_search_1",
        "list": "/example_saved_search_1",
        "remove": "/example_saved_search_1",
        "scheduled_view": "/example_saved_search_1/scheduled_view"
      },
      "name": "example_saved_search_1"
    }
  ]
}
```

#### Modify Saved Search Properties

This action is used to modifies the properties of a saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|properties|object|None|True|JSON object of properties and values to modify|None|{"description":"ExampleDescription","is_scheduled":true}|None|None|
|saved_search_name|string|None|True|Name of saved search to display properties for|None|ExampleSavedSearchName|None|None|
  
Example input:

```
{
  "properties": {
    "description": "ExampleDescription",
    "is_scheduled": true
  },
  "saved_search_name": "ExampleSavedSearchName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the update was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Run Saved Search

This action is used to runs a saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|saved_search_name|string|None|True|Name of saved search to run|None|ExampleSavedSearchName|None|None|
  
Example input:

```
{
  "saved_search_name": "ExampleSavedSearchName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|job_id|string|False|The Job ID for the search job created|12345|
  
Example output:

```
{
  "job_id": 12345
}
```

#### Search

This action is used to run a query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|count|integer|100|True|The maximum number of results to return. Set to 0 for unlimited results|None|100|None|None|
|query|string|None|True|Run a search query|None|search *|None|None|
|search_timeframe|string|None|False|The specified timeframe for the search. Default searches over all time. Separated with dash, in the form of Unix epoch timestamps, e.g. 1498824598-1598824598. If end time is left blank, it defaults to the current time|None|1598984278-1598984478|None|None|
  
Example input:

```
{
  "count": 100,
  "query": "search *",
  "search_timeframe": "1598984278-1598984478"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|False|Count of results returned|1|
|result|object|False|Raw search results|[{"_time":"2024-01-30T12:46:00","event":"ExampleEvent1"}]|
  
Example output:

```
{
  "count": 1,
  "result": [
    {
      "_time": "2024-01-30T12:46:00",
      "event": "ExampleEvent1"
    }
  ]
}
```

#### View Saved Search Properties

This action is used to returns the properties for a saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|saved_search_name|string|None|True|Name of saved search to display properties for|None|ExampleSavedSearchName|None|None|
  
Example input:

```
{
  "saved_search_name": "ExampleSavedSearchName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|properties|object|False|JSON object containing saved search properties|{"description":"ExampleDescription","is_scheduled":true}|
  
Example output:

```
{
  "properties": {
    "description": "ExampleDescription",
    "is_scheduled": true
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* If issues are encountered when using the `Search` action, try prefixing your query with `search`, example: `search index="*" | head 5`.

# Version History

* 3.0.5 - Updated SDK to latest version (6.2.5)
* 3.0.4 - Updated SDK to latest version | Refreshed the plugin | Added unittests | Updated packages
* 3.0.3 - Add `search_timeframe` input to Search action
* 3.0.2 - Fix issue with typos in help.md and plugin description
* 3.0.1 - New spec and help.md format for the Extension Library
* 3.0.0 - Remove Komand-specific Alert trigger | Fix invalid output properties | Numerous typographical fixes | Improve error handling | Smaller plugin size due to slim SDK migration | New connection test code
* 2.0.0 - Support SSL Verify option in the Connection | Improve error handling in Connection | Update documentation
* 1.1.0 - Add support for user specified number of results in the Search action
* 1.0.1 - Fix issue where JSON module was not imported in Search action
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Support free Splunk license
* 0.2.4 - SSL bug fix in SDK
* 0.2.3 - UTF-8 encode events in the insert action
* 0.2.2 - Fix bug when using multiple alert names
* 0.2.1 - Bugfix in connection attempts
* 0.2.0 - Add 8 saved search and related actions
* 0.1.2 - Remove logging of username and password
* 0.1.1 - Added poll interval input to Alert trigger
* 0.1.0 - Initial plugin

# Links

* [Splunk](https://www.splunk.com/)

## References

* [Splunk](https://www.splunk.com/)