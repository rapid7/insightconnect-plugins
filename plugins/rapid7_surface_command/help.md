# Description

Surface Command gives you full visibility over your assets and identities across multiple technology platforms

# Key Features

* Query Surface Command Data
* Run long queries asynchronously with Start a Query and Get Query Result

# Requirements

* User or Organization Key from the Insight Platform. To create one follow [Generate User API Key guide](https://docs.rapid7.com/insight/managing-platform-api-keys/#generating-a-user-key)
* The Region where your Rapid7 Surface Command instance is hosted. To identify your region, see [Identify Data Region](https://docs.rapid7.com/insight/navigate-the-insight-platform/#check-your-data-region)
* A valid Query ID (UUID) from Rapid7 Surface Command. To obtain a Query ID, edit a Saved Query in the Surface Command UI and retrieve its ID from the URL

# Supported Product Versions

* v1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|User or Organization Key from the Insight Platform|None|a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99|None|None|
|region|string|us|True|Region|["us", "us2", "us3", "eu", "ca", "au", "ap"]|us|None|None|
|timeout|integer|170|False|Number of seconds to wait for a response from Surface Command before the request times out. Actions running in the cloud are stopped after 180 seconds, so higher values only take effect on an orchestrator|None|170|None|None|

Example input:

```
{
  "api_key": "a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99",
  "region": "us",
  "timeout": 170
}
```

## Technical Details

### Actions


#### Get Query Result

This action is used to get the rows of a query started with Start a Query, waiting up to Max Wait seconds for the job 
to finish

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|job_id|string|None|True|ID of the query job returned by Start a Query|None|0b1c2d3e-4f50-6172-8394-a5b6c7d8e9f0|None|None|
|max_wait|integer|180|False|Seconds to wait for the job to finish before returning with status running (at most 200). Actions running in the cloud are stopped after 240 seconds|None|180|None|None|
  
Example input:

```
{
  "job_id": "0b1c2d3e-4f50-6172-8394-a5b6c7d8e9f0",
  "max_wait": 180
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]object|False|Rows returned by the query when the status is complete|[]|
|job_id|string|False|ID of the query job|0b1c2d3e-4f50-6172-8394-a5b6c7d8e9f0|
|status|string|True|Status of the query job, either running or complete. Items is empty while the status is running, so check the status before using Items|complete|
  
Example output:

```
{
  "items": [],
  "job_id": "0b1c2d3e-4f50-6172-8394-a5b6c7d8e9f0",
  "status": "complete"
}
```

#### Run an Adhoc Query

This action is used to run and execute an adhoc query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cypher|string|None|True|Cypher query to execute|None|MATCH (m:Machine) RETURN m|None|None|
  
Example input:

```
{
  "cypher": "MATCH (m:Machine) RETURN m"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]object|False|Array of Items|[]|
  
Example output:

```
{
  "items": []
}
```

#### Run a Saved Query

This action is used to run and execute a saved query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query_id|string|None|True|Query ID (UUID) to Run from Surface Command|None|12345678-1234-1234-1234-123456789012|None|None|
  
Example input:

```
{
  "query_id": "12345678-1234-1234-1234-123456789012"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]object|False|Array of Items|[]|
  
Example output:

```
{
  "items": []
}
```

#### Start a Query

This action is used to start a saved or adhoc query as an asynchronous job and return without waiting for it to finish.
 Use Get Query Result to collect the rows

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cypher|string|None|False|Cypher query to run. Provide either Query ID or Cypher Query, not both|None|MATCH (m:Machine) RETURN m|None|None|
|query_id|string|None|False|ID (UUID) of a saved query to run. Provide either Query ID or Cypher Query, not both|None|12345678-1234-1234-1234-123456789012|None|None|
  
Example input:

```
{
  "cypher": "MATCH (m:Machine) RETURN m",
  "query_id": "12345678-1234-1234-1234-123456789012"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]object|False|Rows returned by the query when the status is complete|[]|
|job_id|string|False|ID of the query job to pass to Get Query Result. Empty when the rows were returned immediately|0b1c2d3e-4f50-6172-8394-a5b6c7d8e9f0|
|status|string|True|Status of the query job, either running or complete. When complete, the rows are already in Items; when running, Items is empty and the rows must be collected with Get Query Result|running|
  
Example output:

```
{
  "items": [],
  "job_id": "0b1c2d3e-4f50-6172-8394-a5b6c7d8e9f0",
  "status": "running"
}
```

#### Tag Assets in Bulk

This action is used to add, set, or remove tags on multiple assets in bulk

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|object_ids|[]string|None|True|List of asset object IDs (UUIDs) to tag|None|["11111111-1111-1111-1111-111111111111", "22222222-2222-2222-2222-222222222222"]|None|None|
|operation|string|None|True|Tag operation to perform: add (append tags), set (replace all tags), or remove (delete tags)|["add", "set", "remove"]|add|None|None|
|tags|[]string|None|True|List of tag values to apply|None|["env:prod", "team:security"]|None|None|
  
Example input:

```
{
  "object_ids": [
    "11111111-1111-1111-1111-111111111111",
    "22222222-2222-2222-2222-222222222222"
  ],
  "operation": "add",
  "tags": [
    "env:prod",
    "team:security"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|failure_count|integer|True|Number of assets that could not be tagged|0|
|failures|[]object|False|Details of any tagging failures, including the object ID and error message|[]|
|success_count|integer|True|Number of assets successfully tagged|2|
  
Example output:

```
{
  "failure_count": 0,
  "failures": [],
  "success_count": 2
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* Actions running in the cloud are stopped after 240 seconds. For queries that take longer, use Start a Query, then call Get Query Result in a loop while its Status is `running`, for example: Start a Query, then a Loop with the condition Status equals `running` (maximum 6 iterations) containing Get Query Result with Max Wait 180, then use Items
* Start a Query needs async table queries to be enabled for the organization in Surface Command. If it fails with `Surface Command did not return a query job before the request timed out`, contact support to enable them, or use Run a Saved Query or Run an Adhoc Query
* Query results are kept for 1 hour after the query starts. If Get Query Result reports that the job was not found or has expired, start the query again
* Large results (over about 8 MB) can only be collected once: after Get Query Result has returned them, run Start a Query again to fetch them again

# Version History

* 1.4.0 - Add new actions | Start a Query | Get Query Result
* 1.3.0 - Add optional connection input | Timeout | Increase default request timeout from 90 to 170 seconds | Updated SDK to the latest version (6.6.1)
* 1.2.0 - Add new action | Tag Assets in Bulk
* 1.1.0 - Update action title | Add new action | Run Adhoc Query
* 1.0.0 - Initial plugin

# Links

* [Rapid7 Surface Command](https://www.rapid7.com/products/command/attack-surface-management-asm/)

## References

* [Identify Data Region](https://docs.rapid7.com/insight/navigate-the-insight-platform/#check-your-data-region)
* [Generate User API Key](https://docs.rapid7.com/insight/managing-platform-api-keys/#generating-a-user-key)