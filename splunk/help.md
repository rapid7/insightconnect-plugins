# Description

[Splunk](https://www.splunk.com/) captures, indexes, and correlates real-time data in a searchable repository from which it can generate graphs, reports, alerts, dashboards, and visualizations. This plugin allows you to interact with Splunk by hooking alerts to trigger InsightConnect workflows, run (saved) searches, retrieve search results, and even insert data back into Splunk from a workflow.

To get Splunk alerts or send saved searches to InsightConnect, please use the [InsightConnect Splunk App](https://splunkbase.splunk.com/app/4673/).

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

# Documentation

## Setup

To connect to Splunk, you must have valid credentials and network access to the Splunk API port (Splunk's default is TCP/8089). This plugin supports both the Free and Enterprise Splunk licenses.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|False|Username and password|None|None|
|host|string|None|True|Hostname or IP address of Splunk server to connect to e.g. splunk.example.com|None|None|
|license|string|None|True|License type for Splunk host|['Enterprise', 'Free']|None|
|port|integer|8089|True|Port the Splunk API is listening on. Default is 8089|None|None|
|ssl_verify|boolean|None|True|Verify server's SSL/TLS certificate|None|None|
|use_ssl|boolean|None|True|Whether or not to use SSL|None|None|

To configure your Splunk instance to allow remote login add the following line to the general stanza in `$SPLUNK_HOME/etc/system/local/server.conf`:

```

[general]
allowRemoteLogin = always

```

There's no authentication in the free license, so set `license` to `Free` and omit input to the username and password fields.

Example input:

```
```

## Technical Details

### Actions

#### List Saved Searches

This action lists all saved searches.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|saved_searches|[]object|False|Array of saved search objects|

#### Insert

This action is used to insert events into an index.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event|string|None|True|The event to submit|None|None|
|host|string|None|False|The source host, e.g. localhost or 192.168.2.2|None|None|
|index|string|None|True|Name of index|None|None|
|source|string|None|False|Source of the event (e.g., /var/log/syslog)|None|None|
|sourcetype|string|None|False|The optional source type value of the event (e.g. access_combined, syslog)|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Search

This action allows you run a search command in Splunk.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|count|integer|100|True|The maximum number of results to return. Set to 0 for unlimited results|None|None|
|query|string|None|True|Run a search query (e.g. search *)|None|None|
|search_timeframe|string|None|False|The specified timeframe for the search. Default searches over all time. Separated with dash, in the form of Unix epoch timestamps, e.g. 1498824598-1598824598. If end time is left blank, it defaults to the current time|None|1598984278-1598984478|

Example input:

```
{
  "count": 10,
  "query": "| from datamodel:\"internal_audit_logs.searches\"",
  "search_timeframe": "1598984278-1598984478"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Count of results returned|
|result|object|False|Raw search results|

Example output:

```
{
  "count": 1,
  "result": {
    "fields": [
      {
        "name": "_time"
      },
      {
        "name": "host"
      },
      {
        "name": "source"
      },
      {
        "name": "sourcetype"
      },
      {
        "name": "info"
      },
      {
        "name": "user"
      },
      {
        "name": "exec_time"
      },
      {
        "name": "result_count"
      },
      {
        "name": "savedsearch_name"
      },
      {
        "name": "scan_count"
      },
      {
        "name": "total_run_time"
      },
      {
        "name": "is_realtime",
        "type": "str"
      },
      {
        "name": "search_id",
        "type": "str"
      },
      {
        "name": "search",
        "type": "str"
      },
      {
        "name": "search_type",
        "type": "str"
      },
      {
        "name": "_bkt"
      },
      {
        "name": "_cd"
      },
      {
        "name": "_indextime"
      },
      {
        "name": "_kv"
      },
      {
        "name": "_raw"
      },
      {
        "name": "_serial"
      },
      {
        "name": "_si"
      },
      {
        "name": "_sourcetype"
      },
      {
        "name": "_subsecond"
      }
    ],
    "highlighted": {},
    "init_offset": 0,
    "messages": [],
    "preview": false,
    "results": [
      {
        "_bkt": "_audit~0~0B6E6961-7112-4FAF-9BDD-C477139D9519",
        "_cd": "0:32607",
        "_indextime": "1598984305",
        "_kv": "1",
        "_raw": "Audit:[timestamp=09-01-2020 18:18:25.732, user=splunk-system-user, action=search, info=canceled, search_id='1598984220.14', total_run_time=0.40, event_count=0, result_count=0, available_count=0, scan_count=0, drop_count=0, exec_time=1598984220, api_et=N/A, api_lt=N/A, search_et=N/A, search_lt=N/A, is_realtime=0, savedsearch_name=\"\", search_startup_time=\"129\", has_error_msg=false, fully_completed_search=true, searched_buckets=0, eliminated_buckets=0, considered_events=0, total_slices=0, decompressed_slices=0, duration.command.search.index=0, invocations.command.search.index.bucketcache.hit=0, duration.command.search.index.bucketcache.hit=0, invocations.command.search.index.bucketcache.miss=0, duration.command.search.index.bucketcache.miss=0, invocations.command.search.index.bucketcache.error=0, duration.command.search.rawdata=0, invocations.command.search.rawdata.bucketcache.hit=0, duration.command.search.rawdata.bucketcache.hit=0, invocations.command.search.rawdata.bucketcache.miss=0, duration.command.search.rawdata.bucketcache.miss=0, invocations.command.search.rawdata.bucketcache.error=0, roles='admin+power+splunk-system-role+user', search='| copybuckets json=\"{\\\"vixes\\\": {}, \\\"providers\\\": {}}\"'][n/a]",
        "_serial": "0",
        "_si": [
          "97dd3284e275",
          "_audit"
        ],
        "_sourcetype": "audittrail",
        "_subsecond": ".732782",
        "_time": "2020-09-01T18:18:25.732+00:00",
        "exec_time": "1598984220",
        "host": "97dd3284e275",
        "info": "canceled",
        "is_realtime": "false",
        "result_count": "0",
        "savedsearch_name": "",
        "scan_count": "0",
        "search": "| copybuckets json=\"{\\\"vixes\\\": {}, \\\"providers\\\": {}}\"",
        "search_id": "1598984220.14",
        "search_type": "adhoc",
        "source": "audittrail",
        "sourcetype": "audittrail",
        "total_run_time": "0.40",
        "user": "splunk-system-user"
      }
    ]
  }
}
```

#### Modify Saved Search Properties

This action is used to modify the properties of a saved search.
A full list of saved search properties can be found [here](http://dev.splunk.com/view/python-sdk/SP-CAAAEK2#savedsearchparams).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|properties|object|None|True|JSON object of properties and values to modify|None|None|
|saved_search_name|string|None|True|Name of saved search to display properties for|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the update was successful|

#### Run Saved Search

This action is used to run a saved search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|saved_search_name|string|None|True|Name of saved search to run|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job_id|string|False|Job ID for the search job created|

#### View Saved Search Properties

This action is used to return the properties for a saved search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|saved_search_name|string|None|True|Name of saved search to display properties for|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|properties|object|False|JSON object containing saved search properties|

#### Delete Saved Search

This action is used to delete a saved search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|saved_search_name|string|None|True|Name of the saved search to delete|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the deletion was successful|

#### Display Search Results

This action is used to display the search results from a job.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|job_id|string|None|True|Job ID to look up results for|None|None|
|timeout|number|None|True|Duration of time, in seconds, to wait for retrieving results|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_results|[]object|False|Search results from a job|

#### Create Saved Search

This action is used to create a saved search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|properties|object|None|False|JSON object containing additional properties to save with the saved search|None|None|
|query|string|None|True|Search query|None|None|
|saved_search_name|string|None|True|Name to give to the saved search|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|saved_search|object|False|Newly created saved search object|

#### Get Saved Search Job History

This action is used to return the job history of a specified saved search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|saved_search_name|string|None|True|Name of a saved search|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job_history|[]object|False|Job history belonging to a saved search|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

* If issues are encountered when using the `Search` action, try prefixing your query with `search`, example: `search index="*" | head 5`.

# Version History

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

## References

* [Splunk](https://www.splunk.com/)
* [InsightConnect Splunk App](https://splunkbase.splunk.com/app/4673/)
