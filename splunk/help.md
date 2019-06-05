
# Splunk

## About

The [Splunk](https://www.splunk.com/) plugin allows you to interact with Splunk by hooking alerts to trigger Komand workflows,
running additional searches, and even inserting data back into Splunk from a Komand workflow.

## Actions

### Insert

This action allows you to index (insert) an event in Splunk.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|False|Source of the event (e.g., /var/log/syslog)|None|
|index|string|None|True|Name of index|None|
|host|string|None|False|The source host, e.g. localhost or 192.168.2.2|None|
|sourcetype|string|None|False|The optional source type value of the event (e.g. access_combined, syslog)|None|
|event|string|None|True|The event to submit|None|

#### Output

This action does not contain any outputs.

### Search

This action allows you run a search command in Splunk.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Run a search query (e.g. search *)|None|
|count|integer|100|True|The maximum number of results to return. Set to 0 for unlimited results|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Count of results returned|
|result|object|False|Raw search results|

### Modify Saved Search Properties

This action is used to modifies the properties of a saved search.
A full list of saved search properties can be found [here](http://dev.splunk.com/view/python-sdk/SP-CAAAEK2#savedsearchparams).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|saved_search_name|string|None|True|Name of saved search to display properties for|None|
|properties|object|None|True|JSON object of properties and values to modify|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the update was successful|

### Run Saved Search

This action is used to runs a saved search.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|saved_search_name|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job_id|string|False|Job ID for the search job created|

### View Saved Search Properties

This action is used to returns the properties for a saved search.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|saved_search_name|string|None|True|Name of saved search to display properties for|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|properties|object|False|JSON object containing saved search properties|

### Delete Saved Search

This action is used to deletes a saved search.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|saved_search_name|string|None|True|Name of the saved search to delete|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the deletion was successful|

### Display Search Results

This action is used to displays the search results from a job.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|job_id|string|None|True|Job ID to look up results for|None|
|timeout|number|None|True|Duration of time to wait for retrieving results|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_results|[]object|False|Search results from a job|

### List Saved Searches

This action is used to lists all saved searches. Note that the Splunk API returns credential information in clear-text for this action's output.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|saved_searches|[]object|False|Array of saved search objects|

### Create Saved Search

This action is used to creates a saved search.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Search query|None|
|saved_search_name|string|None|True|Name to give to the saved search|None|
|properties|object|None|False|JSON object containing additional properties to save with the saved search|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|saved_search|object|False|Newly created saved search object|

### Get Saved Search Job History

This action is used to returns the job history of a specified saved search.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|saved_search_name|string|None|True|Name of a saved search|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job_history|[]object|False|Job history belonging to a saved search|

## Triggers

### Alert

This trigger allows you to configure a Splunk Alert to send data to Komand. It will add a webhook action to the Splunk actions to send the data to Komand.
Any other webhook will be overwritten. You must have the name of the alert to hook.

By default, this trigger makes a request every 15 seconds to establish the webhook.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|15|False|Poll interval in seconds|None|
|names|[]string|None|True|Names of the alerts to hook|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results_link|string|False|None|
|result|object|False|None|
|search_name|string|False|None|

## Connection

To connect to Splunk, you must have valid credentials and network access to the Splunk API port (Splunk's default is TCP/8089). This plugin supports both the Free and Enterprise Splunk licenses.

If use the Splunk free license, configure your Splunk instance to allow remote login by adding the following line to the general stanza in `$SPLUNK_HOME/etc/system/local/server.conf`:

```

[general]
allowRemoteLogin = always

```

There's no authentication in the free license, so set `license` to `Free` and omit input to the username and password fields.

To configure an alert trigger, the Splunk server must be able to connect back to the Komand server via http(s) ports to send webhook events.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|False|Host of Splunk server to connect to|None|
|credentials|credential_username_password|None|False|Username and password|None|
|port|integer|8089|False|None|None|
|license|string|None|True|License type for Splunk host|['Enterprise', 'Free']|
|use_ssl|boolean|None|False|Use HTTPs|None|
|ssl_verify|boolean|None|True|Verify server's SSL/TLS certificate|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Search
* Log investigation
* Alerts

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - Added poll interval input to Alert trigger
* 0.1.2 - Remove logging of username and password
* 0.2.0 - Add 8 saved search and related actions
* 0.2.1 - Bugfix in connection attempts
* 0.2.2 - Fix bug when using multiple alert names
* 0.2.3 - UTF-8 encode events in the insert action
* 0.2.4 - SSL bug fix in SDK
* 0.2.4 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Support free Splunk license
* 1.0.1 - Fix issue where json module was not imported in Search action
* 1.1.0 - Add support for user specified number of results in the Search action
* 2.0.0 - Support SSL Verify option in the Connection | Improve error handling in Connection | Update documentation

## References

* [Tutorial: Connecting Splunk Alerts To Komand](https://komand.zendesk.com/hc/en-us/articles/115001374187)
* [Splunk](https://www.splunk.com/)
