# Description

The [Komand](komand.com) plugin provides backwards compatibility to run workflows in Komand, Rapid7's legacy on-premise SOAR solution.

# Key Features

* Automate manual tasks to save time and improve efficiency
* Orchestrate incident response using data and actions from a wide variety of solutions

# Requirements

* Username and Password
* Komand Server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to Komand server, e.g. https://komand.company.com|None|
|credentials|credential_username_password|None|True|Username and password for user|None|

## Technical Details

### Actions

#### Run Asynchronously

This action is used to run a workflow without waiting for results.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|workflow_uid|string|None|False|Workflow UID to run. Either this or name should be provided.|None|
|input|object|None|False|Input object to supply to the workflow job|None|
|workflow_name|string|None|False|Workflow name to run. Either this or UID should be provided.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|Job URL|
|job_id|string|False|Job ID|

#### Run Synchronously

This action is used to run a workflow and wait for results.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|workflow_uid|string|None|False|Workflow UID to run. Either this or name should be provided|None|
|input|object|None|False|Input object to supply to the workflow job|None|
|workflow_name|string|None|False|Workflow name to run. Either this or UID should be provided|None|
|timeout|number|150|True|Timeout for executed workflow to finish, in seconds. Use 0 for no timeout|None|
|completion_checks|number|10|False|How many times the executed workflow should be checked for completion during the timeout period. Higher numbers should result in quicker job turnover. Leave blank if timeout is set to 0|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Job Status|
|ended_at|string|False|None|
|job_id|string|False|Job ID|
|workflow_uid|string|False|Workflow UID|
|created_at|string|False|None|
|updated_at|string|False|None|
|url|string|False|Job URL|
|steps|[]object|False|Step outputs|
|group_id|string|False|Job Group ID|
|name|string|False|None|

### Triggers

#### Job

This trigger is used to monitor for new jobs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|True|Status to trigger on|['failed', 'queued', 'succeeded', 'retried']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Job Status|
|ended_at|string|False|None|
|job_id|string|False|Job ID|
|workflow_uid|string|False|Workflow UID|
|created_at|string|False|None|
|updated_at|string|False|None|
|url|string|False|Job URL|
|group_id|string|False|Job Group ID|
|name|string|False|None|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.3 - New spec and help.md format for the Hub
* 1.0.2 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.1 - Fix issue where Lookup Workflow Name can crash due to excessive data
* 1.0.0 - Support web server mode | Update to new credential types | Plugin spec revision
* 0.3.0 - Bugfix: Run Synchronously not waiting for executed workflow to finish, customizable timeout period
* 0.2.1 - Update help
* 0.2.0 - Update connection to match new Komand API
* 0.1.2 - Port plugin to new architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Komand](https://www.komand.com/)

