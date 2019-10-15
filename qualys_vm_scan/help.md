
# Qualys Vulnerability Management Scans

## About

Quals VM Scan allows managing vulnerability scans via the Qualys V2 API.

## Actions

### List

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Reference|string|None|false|Filter scans by reference|None|
|State|string|None|false|Filter scans by state|None|
|Processed|integer|None|false|Filter whether scans have been processed or not|None|
|Type|string|None|false|Filter scans by type|None|
|Target|string|None|false|Filter scans by target|None|
|User Login|string|None|false|Filter scans by user login|None|
|Launched After|date|None|false|Filter scans by launched after a date and time|None|
|Launched Before|date|None|false|Filter scans by launched before a date and timee|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Scans|[]scan|True|List of scans|

### Launch

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Title|string|None|True|Title of scan to be launched|None|
|Option Title|string|None|True|Title of option profile to use in scan|None|
|Priority|string|None|True|Priority of the scan to be launched|None|
|IP|string|None|True|IP(s) to launch scan on (single, comma-separated, or range)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|True|ID of launched scan|
|Reference|string|True|Reference of launched scan|

### Cancel

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Reference|string|True|Reference of scan to cancel|

#### Output

There is no output associated with this action.

### Pause

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Reference|string|True|Reference of scan to pause|

#### Output

There is no output associated with this action.

### Resume

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Reference|string|True|Reference of scan to resume|

#### Output

There is no output associated with this action.

### Delete

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Reference|string|True|Reference of scan to delete|

#### Output

There is no output associated with this action.

## Triggers

There are no triggers associated with this plugin.

## Connection

|Name|Type|Default|Required|Description|
|----|----|-------|--------|-----------|
|Hostname|string|https://qualysapi.qualys.com/|True|Base URL of Qualys API Server for your region|
|credentials|credential_username_password|None|True|Qualys username and password|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Run a scan

## Versions

* 0.0.1 - Initial plugin
* 1.0.0 - Support web server mode | Update credentials | Semver compliance
* 1.0.1 - Updating to Go SDK 2.6.4
* 1.0.2 - Regenerate with latest Go SDK to solve bug with triggers

## References

* [Qualys API V2 User Guide](https://www.qualys.com/docs/qualys-api-v2-user-guide.pdf)
