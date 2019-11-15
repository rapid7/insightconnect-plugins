# Description

The Checkmarx CxSAST plugin access CxSAST service to manage projects and scans.

# Key Features

* Manage CxSAST projects
* Manage CxSAST scans

# Requirements

* Requires username and password for the CxSAST service.

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

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Checkmarx CxSAST](https://www.checkmarx.com/products/static-application-security-testing/)
* [CxSAST REST API](https://checkmarx.atlassian.net/wiki/spaces/KC/pages/131039271/CxSAST%2BREST%2BAPI)

