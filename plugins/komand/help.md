# Description

The [Komand](komand.com) plugin provides backwards compatibility to run workflows in Komand, Rapid7's legacy on-premise SOAR solution.

# Key Features

* Automate manual tasks to save time and improve efficiency
* Orchestrate incident response using data and actions from a wide variety of solutions

# Requirements

* Username and Password
* Komand Server

# Supported Product Versions

* 2023-05-15

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|URL to Komand server|None|https://komand.company.com|
|credentials|credential_username_password|None|True|Username and password for user|None|{ 'username': 'user1', 'password': 'mypassword' }|

Example input:

```
{
  "credentials": {
    "username": "user1",
    "password": "mypassword"
  },
  "url": "https://komand.company.com"
}
```

## Technical Details

### Actions

#### Run Asynchronously

This action is used to run a workflow without waiting for results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|object|None|False|Input object to supply to the workflow job|None|{}|
|workflow_name|string|None|False|Workflow name to run. Either this or UID should be provided|None|example-name|
|workflow_uid|string|None|False|Workflow UID to run. Either this or name should be provided|None|b595ccea-f324-11ed-a05b-0242ac120003|

Example input:

```
{
  "input": "{}",
  "workflow_name": "example-name",
  "workflow_uid": "b595ccea-f324-11ed-a05b-0242ac120003"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|url|string|False|Job URL|www.example.com|
|job_id|string|False|Job ID|b595ccea-f324-11ed-a05b-0242ac120003|

Example output:

```
{
  "url": "www.example.com",
  "job_id": "b595ccea-f324-11ed-a05b-0242ac120003"
}
```

#### Run Synchronously

This action is used to run a workflow and wait for results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|completion_checks|number|10|False|How many times the executed workflow should be checked for completion during the timeout period. Higher numbers should result in quicker job turnover. Leave blank if timeout is set to 0|None|10|
|input|object|None|False|Input object to supply to the workflow job|None|{}|
|timeout|number|150|True|Timeout for executed workflow to finish, in seconds. Use 0 for no timeout|None|150|
|workflow_name|string|None|False|Workflow name to run. Either this or UID should be provided|None|example-name|
|workflow_uid|string|None|False|Workflow UID to run. Either this or name should be provided|None|b595ccea-f324-11ed-a05b-0242ac120003|

Example input:

```
{
  "completion_checks": 10,
  "input": "{}",
  "timeout": 150,
  "workflow_name": "example-name",
  "workflow_uid": "b595ccea-f324-11ed-a05b-0242ac120003"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|status|string|False|Job Status|failed|
|ended_at|string|False|None|Jan 01, 2000 0:00 AM|
|job_id|string|False|Job ID|b595ccea-f324-11ed-a05b-0242ac120003|
|workflow_uid|string|False|Workflow UID|b595ccea-f324-11ed-a05b-0242ac120003|
|created_at|string|False|Created at|Jan 01, 2000 0:00 AM|
|updated_at|string|False|Updated at|Jan 01, 2000 0:00 AM|', '|ended_at|string|False|Ended at|Jan 01, 2000 0:00 AM|
|url|string|False|Job URL|www.example.com|
|steps|[]object|False|Step outputs|[{}]|
|group_id|string|False|Job Group ID|b595ccea-f324-11ed-a05b-0242ac120003|
|name|string|False|Name|example-name|

Example output:

```
{
  "status": "failed",
  "ended_at": "Jan 01, 2000 0:00 AM",
  "job_id": "b595ccea-f324-11ed-a05b-0242ac120003",
  "workflow_uid": "b595ccea-f324-11ed-a05b-0242ac120003",
  "created_at": "Jan 01, 2000 0:00 AM",
  "updated_at": "Jan 01, 2000 0:00 AM",
  "url": "www.example.com",
  "steps": [{}],
  "group_id": "b595ccea-f324-11ed-a05b-0242ac120003",
  "name": "example-name"
}
```

### Triggers

#### Job

This trigger is used to monitor for new jobs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|status|string|None|True|Status to trigger on|['failed', 'queued', 'succeeded', 'retried']|failed|

Example input:

```
{
  "status": "failed"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|status|string|False|Job status|succeeded|
|ended_at|string|False|Ended at|Jan 01, 2000 0:00 AM|
|job_id|string|False|Job ID|b595ccea-f324-11ed-a05b-0242ac120003|
|workflow_uid|string|False|Workflow UID|b595ccea-f324-11ed-a05b-0242ac120003|
|created_at|string|False|Created at|Jan 01, 2000 0:00 AM|
|updated_at|string|False|Updated at|Jan 01, 2000 0:00 AM|
|url|string|False|Job URL|www.example.com|
|group_id|string|False|Job group ID|b595ccea-f324-11ed-a05b-0242ac120003|
|name|string|False|Name|example-name|

Example output:

```
{
  "status": "failed",
  "ended_at": "Jan 01, 2000 0:00 AM",
  "job_id": "b595ccea-f324-11ed-a05b-0242ac120003",
  "workflow_uid": "b595ccea-f324-11ed-a05b-0242ac120003",
  "created_at": "Jan 01, 2000 0:00 AM",
  "updated_at": "Jan 01, 2000 0:00 AM",
  "url": "www.example.com",
  "group_id": "b595ccea-f324-11ed-a05b-0242ac120003",
  "name": "example-name"
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.4 - Deprecate plugin
* 1.0.3 - New spec and help.md format for the Extension Library
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

* [Komand](https://www.komand.com/)

## References
