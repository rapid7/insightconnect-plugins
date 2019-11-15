# Description
Streamline your data for analysis and action with the Rapid7 [InsightOps](https://insightops.help.rapid7.com/docs) plugin using InsightConnect. With the ability to submit new log data as well as query existing log data, you can drive a lot more efficiency in getting your data out of InsightOps and into the hands of your security and IT teams!

This plugin utilizes [Rapid7 InsightOps API](https://insightops.help.rapid7.com/docs).

# Key Features

* Submit Log Data
* Query logs

# Requirements

* Requires an API Key from Insight platform

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|region|string|us|True|Region of InsightOps service to access e.g. eu|['eu', 'us']|
|api_key|string|None|True|API Key to access InsightOps service e.g. 39dd20eb-1337-45a0-a4044-133f237b50fa|None|

## Technical Details

### Actions

#### Query Logs

This action is used to retrieve logs from InsightOps service.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|logs|logs|True|None|

#### Submit Log Data

This action is used to submit JSON to a specified log within an InsightOps logset.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|data|object|None|False|JSON that will be passed to InsightOps logset|None|
|logset_container_id|string|None|False|An UUID that specifics a container within an InsightOps logset|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Reports if data was submitted successfully|

#### Create Logset Container

This action is used to create a container within the specified logset for the InsightOps service.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|le_agent_filename|string|None|False|Log entry agent filename|None|
|source_type|string|token|False|A unique identifier for the log|None|
|name|string|None|False|Name of the container|None|
|token_seed|string|None|False|Token Seed is used to generate a token that can be shared. If a random uuid needs to be created leave this blank|None|
|structures|[]string|None|False|The structure of the log. e.g. Syslog, JSON, Apache and Nginx|None|
|id|string|None|False|ID points to the [logset](https://insightops.help.rapid7.com/docs/using-log-search) ID to which the container will be created e.g. c17cef2e-01c1-404e-b42b-ea5088c2f713|None|
|le_agent_follow|string|None|False|Log entry agent follow|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|log|logset_container|False|Returned data from created container|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|log|post_log|False|Data returned from the posted log|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - Support web server mode | Use new credential types
* 1.0.0 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [InsightOps](https://www.rapid7.com/products/insightops/)
* [InsightOps API](https://insightops.help.rapid7.com/docs)
* [Logsets](https://insightops.help.rapid7.com/docs/using-log-search)

