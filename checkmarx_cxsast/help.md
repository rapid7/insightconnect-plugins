# Description

[Checkmarx CxSAST](https://www.checkmarx.com/products/static-application-security-testing/) Static analysis solution used to identify security vulnerabilities in custom code and open source components.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|CxSAST username and password|None|
|host|string|None|True|Host URL|None|

## Technical Details

### Actions

#### Create Branched Project

This action is used to create a branch of an existing project.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|ID of the project off which to create a branch|None|
|project|project|None|True|Details of the project|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the created project|
|link|link|True|Metadata about the project|

Example output:

```
{
  "id": 50,
  "link": {
    "rel": "self",
    "uri": "/projects/50"
  }
}
```

#### Create Project

This action is used to create a new project with default preset and configuration settings.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|isPublic|boolean|False|True|Whether the project is public or not|None|
|name|string|None|True|Name of the project|None|
|owningTeam|string|None|True|ID of the team that owns the project|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|ID of the created project|
|link|link|True|Metadata about the project|

Example output:

```
{
  "id": 50,
  "link": {
    "rel": "self",
    "uri": "/projects/50"
  }
}
```

#### Create Scan

This action creates a new Checkmarx Scan.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|Specifies the scan comment|None|
|forceScan|boolean|None|False|Specifies whether the code should be scanned or not, regardless of whether changes were made to the code since the last scan|None|
|isIncremental|boolean|None|False|Specifies whether the requested scan is incremental or full scan|None|
|isPublic|boolean|None|False|Specifies whether the requested scan is public or private|None|
|projectId|integer|None|False|Unique ID of the project to be scanned|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the created scan|
|link|link|True|Metadata about the scan|

Example output:

```
{
  "id": 1000000,
  "link": {
    "rel": "self",
    "uri": "/sast/scans/1000000"
  }
}
```

#### Define Scan Settings

This action is used to define the SAST scan settings according to a project (preset and engine configuration).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|emailNotifications|email_notifications|None|False|Email notification details|None|
|engineConfigurationId|integer|None|True|Unique ID of the engine configuration|None|
|presetId|integer|None|True|Unique ID of the preset|None|
|projectId|integer|None|True|Unique ID of the project|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the created scan settings|
|link|link|True|Metadata about the scan settings|

Example output:

```
{
  "id": 1,
  "link": {
    "rel": "self",
    "uri": "/sast/scanSettings/1"
  }
}
```

#### Get Scan Details

This action is used to get details of a specific SAST scan. Scan details can only be retrieved once a scan has been performed and the scan ID (id) is known.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Unique ID of the scan|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan|scan_details|False|Details of requested scan|

Example output:

```
{
  "scan": {
    "comment": "",
    "dateAndTime": {
        "engineFinishedOn": "2019-08-19T11:07:08.437",
        "engineStartedOn": "2019-08-19T10:58:37.38",
        "finishedOn": "2019-08-19T11:07:08.583",
        "startedOn": "2019-08-19T10:58:37.38"
    },
    "engineServer": {
        "id": 1,
        "link": {
        "rel": "engine-server",
        "uri": "/sast/engineServers/1"
        },
        "name": "Engine 1"
    },
    "finishedScanStatus": {
        "id": 1,
        "value": "Completed"
    },
    "id": 1000000,
    "initiatorName": "initiator",
    "isIncremental": false,
    "isLocked": false,
    "isPublic": true,
    "origin": "Web Portal",
    "owner": "owner",
    "owningTeamId": "e85cf506-f5a1-11e9-802a-5aa538984bd8",
    "partialScanReasons": [],
    "project": {
        "id": 16,
        "link": {
        "rel": "project",
        "uri": "/projects/25"
        },
        "name": "my-repo"
    },
    "resultsStatistics": {
        "link": {
        "rel": "results-statistics",
        "uri": "/sast/scans/1000000/resultsStatistics"
        }
    },
    "scanRisk": 10,
    "scanRiskSeverity": 10,
    "scanState": {
        "cxVersion": "9.0.0",
        "failedLinesOfCode": 100,
        "filesCount": 500,
        "languageStateCollection": [
        {
            "languageHash": "0000000000000000",
            "languageID": 1000000000,
            "languageName": "Common",
            "stateCreationDate": "2019-08-06T20:28:43.653"
        },
        {
            "languageHash": "0000000000000000",
            "languageID": 8,
            "languageName": "JavaScript",
            "stateCreationDate": "2019-08-06T20:28:43.653"
        },
        ],
        "linesOfCode": 75763,
        "path": " N/A (Zip File)",
        "sourceId": "0000000000_000000000000_00-000000000"
    },
    "scanType": {
        "id": 1,
        "value": "Regular"
    },
    "status": {
        "details": {
        "stage": "",
        "step": ""
        },
        "id": 7,
        "name": "Finished"
    }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### custom_field

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|Unique ID of the custom field|
|value|string|False|Custom field value|

#### link

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rel|string|False|Relation of the link|
|uri|string|False|Relative URL of the project|

#### source_settings_link

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rel|string|False|Relation of the link|
|type|string|False|Type of Source Control Repository|
|uri|string|False|Relative URL of the project|

#### project

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|ID of the project|
|is_public|boolean|False|Whether or not the project is public|
|link|link|False|Metadata about the project|
|name|string|False|Name of the project|
|sourceSettingsLink|source_settings_link|False|None|
|team_id|string|False|ID of the team to which this project belongs|

#### status_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stage|string|False|Status stage|
|step|string|False|Status step|

#### status

|Name|Type|Required|Description|
|----|----|--------|-----------|
|details|status_details|False|None|
|id|integer|False|ID of the status|
|name|string|False|Name of the status|

#### scan_type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|ID of the scan type|
|value|string|False|Value of the scan type|

#### date_and_time

|Name|Type|Required|Description|
|----|----|--------|-----------|
|engineFinishedOn|date|False|Date the engine finished scanning|
|engineStartedOn|date|False|Date the engine started scanning|
|finishedOn|date|False|Date the scan finished on|
|startedOn|date|False|Date the scan was fired|

#### language_state_collection

|Name|Type|Required|Description|
|----|----|--------|-----------|
|languageHash|string|False|Hash of the language|
|languageID|integer|False|ID of the programming language|
|languageName|string|False|Name of the programming language|
|stateCreationDate|date|False|State creation date of the language|

#### scan_state

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cxVersion|string|False|Version of CxSAST used to scan|
|failedLinesOfCode|integer|False|Number of lines of code failed to scan|
|filesCount|integer|False|Number of files scanned|
|languageStateCollection|language_state_collection|False|Language state collection|
|linesOfCode|integer|False|Number of lines of code scanned|
|path|string|False|Path of the scan state|
|sourceId|string|False|ID of the source|

#### engine_server

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|Unique ID of the engine|
|link|link|False|Link to the engine server|
|name|string|False|Name of the engine serer|

#### finished_scan_status

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|ID of the finished scan status|
|value|string|False|Value of the finished scan status|

#### scan_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comment|string|False|Comment on the scan|
|dateAndtime|date_and_time|False|Dates relevant to the scan|
|engineServer|engine_server|False|Engine server on which the scan was run|
|finishedScanStatus|finished_scan_status|False|Status of the scan once it is finished|
|id|integer|False|Unique ID of scan|
|initiatorName|string|False|User who initiated the scan|
|isIncremental|boolean|False|Whether or not the scan is incremental|
|isLocked|boolean|False|Whether or not the scan is locked|
|isPublic|boolean|False|Whether or not the scan is public|
|origin|string|False|Origin of the scan|
|owner|string|False|Owner of the scan|
|owningTeamId|string|False|ID of the team that owns the project of the scan|
|partialScanReasons|[]string|False|Reasons why the scan was not fully completed|
|project|project|False|Project of the scan|
|resultStatistics|link|False|Statistics of the scan results|
|scanRisk|integer|False|Score of risk of the scan|
|scanRiskSeverity|integer|False|Severity of the risk score of the scan|
|scanState|scan_state|False|State of the scan|
|scanType|scan_type|False|Type of the scan|
|status|status|False|Status of the scan|

#### email_notifications

|Name|Type|Required|Description|
|----|----|--------|-----------|
|afterScans|string|False|Specifies the email to send the post-scan message|
|beforeScan|string|False|Specifies the email to send the pre-scan message|
|failedScans|string|False|Specifies the email to send the scan failure message|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Checkmarx CxSAST](https://www.checkmarx.com/products/static-application-security-testing/)
* [CxSAST REST API](https://checkmarx.atlassian.net/wiki/spaces/KC/pages/131039271/CxSAST%2BREST%2BAPI)

