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

# Supported Product Versions
  
*This plugin does not contain any supported product versions.*

# Documentation

## Setup

To connect to Splunk, you must have valid credentials and network access to the Splunk API port (Splunk's default is TCP/8089). This plugin supports both the Free and Enterprise Splunk licenses.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|False|Username and password|None|{'username': 'user', 'password': 'pass'}|
|host|string|None|True|Hostname or IP address of Splunk server to connect to|None|splunk.example.com|
|license|string|None|True|License type for Splunk host|['Enterprise', 'Free']|Free|
|port|integer|8089|True|Port the Splunk API is listening on|None|8089|
|ssl_verify|boolean|None|True|Verify server's SSL/TLS certificate|None|True|
|use_ssl|boolean|None|True|Whether or not to use SSL|None|True|
  
Example input:

```
{
  "credentials": {
    "password": "pass",
    "username": "user"
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|properties|object|None|False|JSON object containing additional properties to save with the saved search|None|{}|
|query|string|None|True|Search query|None|search-query|
|saved_search_name|string|None|True|Name to give to the saved search|None|Example Name|
  
Example input:

```
{
  "properties": {},
  "query": "search-query",
  "saved_search_name": "Example Name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|saved_search|object|False|Newly created saved search object|{}|
  
Example output:

```
{
  "saved_search": {}
}
```

#### Delete Saved Search
  
This action is used to deletes a saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|saved_search_name|string|None|True|Name of the saved search to delete|None|Example Name|
  
Example input:

```
{
  "saved_search_name": "Example Name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the deletion was successful|None|
  
Example output:

```
{
  "success": true
}
```

#### Display Search Results
  
This action is used to displays the search results from a job

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|job_id|string|None|True|Job ID to look up results for|None|job-id-identifier|
|timeout|number|None|True|Duration of time, in seconds, to wait for retrieving results|None|50|
  
Example input:

```
{
  "job_id": "job-id-identifier",
  "timeout": 50
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|search_results|[]object|False|Search results from a job|[{}, {}]|
  
Example output:

```
{
  "search_results": {}
}
```

#### Get Saved Search Job History
  
This action is used to returns the job history of a specified saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|saved_search_name|string|None|True|Name of a saved search|None|Example Name|
  
Example input:

```
{
  "saved_search_name": "Example Name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|job_history|[]object|False|Job history belonging to a saved search|[{}, {}]|
  
Example output:

```
{
  "job_history": {}
}
```

#### Insert
  
This action is used to insert events into an index

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|event|string|None|True|The event to submit|None|Event|
|host|string|None|False|The source host|None|localhost or 192.168.2.2|
|index|string|None|True|Name of index|None|Index|
|source|string|None|False|Source of the event|None|/var/log/syslog|
|sourcetype|string|None|False|The optional source type value of the event|None|access_combined, syslog|
  
Example input:

```
{
  "event": "Event",
  "host": "localhost or 192.168.2.2",
  "index": "Index",
  "source": "/var/log/syslog",
  "sourcetype": "access_combined, syslog"
}
```

##### Output
  
*This action does not contain any outputs.*

#### List Saved Searches
  
This action is used to lists all saved searches

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|saved_searches|[]object|False|Array of saved search objects|[{}, {}]|
  
Example output:

```
{
  "saved_searches": {}
}
```

#### Modify Saved Search Properties
  
This action is used to modifies the properties of a saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|properties|object|None|True|JSON object of properties and values to modify|None|{}|
|saved_search_name|string|None|True|Name of saved search to display properties for|None|Example name|
  
Example input:

```
{
  "properties": {},
  "saved_search_name": "Example name"
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

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|saved_search_name|string|None|True|Name of saved search to run|None|Example Name|
  
Example input:

```
{
  "saved_search_name": "Example Name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|job_id|string|False|Job ID for the search job created|job-id-identifier|
  
Example output:

```
{
  "job_id": "job-id-identifier"
}
```

#### Search
  
This action is used to run a query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|count|integer|100|True|The maximum number of results to return. Set to 0 for unlimited results|None|100|
|query|string|None|True|Run a search query|None|search *|
|search_timeframe|string|None|False|The specified timeframe for the search. Default searches over all time. Separated with dash, in the form of Unix epoch timestamps. If end time is left blank, it defaults to the current time|None|1598984278-1598984478|
  
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
|count|integer|False|Count of results returned|2|
|result|object|False|Raw search results|{}|
  
Example output:

```
{
  "count": 2,
  "result": {}
}
```

#### View Saved Search Properties
  
This action is used to returns the properties for a saved search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|saved_search_name|string|None|True|Name of saved search to display properties for|None|Example Name|
  
Example input:

```
{
  "saved_search_name": "Example Name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|properties|object|False|JSON object containing saved search properties|{}|
  
Example output:

```
{
  "properties": {}
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

* 4.0.0 - Update splunk-sdk dependency | Refresh with new tooling | Update SDK
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

* [InsightConnect Splunk App](https://splunkbase.splunk.com/app/4673/)
