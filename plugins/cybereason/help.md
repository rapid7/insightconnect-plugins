# Description

The Cybereason platform provides military-grade cyber security with real-time awareness and detection. Respond to threats and remediate in seconds using the Cybereason plugin.

# Key Features

* Quickly respond to threats by quarantining (isolating) a machine associated with a Malop
* Search files on machines

# Requirements

* Requires a Cybereason username and password
* Cybereason account configured as shown [here](https://nest.cybereason.com/user/login?destination=/documentation/product-documentation/191/search-and-browse-files-machines-0#pre-requisites) for File Search capabilities

# Supported Product Versions

* All

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|False|Username and password|None|{"username": "user@example.com", "password": "mypassword"}|
|hostname|string|None|True|Enter the hostname|None|example.com|
|port|integer|8443|True|Enter the port|None|8443|

Example input:

```
{
  "credentials": {
    "username": "user@example.com",
    "password": "mypassword"
  },
  "hostname": "example.com",
  "port": 8443
}
```

## Technical Details

### Actions

#### Archive Sensor

This action is used to archive sensor.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|argument|string|None|True|The reason for archiving the sensor or sensors|None|Sensors are no longer in use|
|sensor_ids|[]string|None|True|The unique identifier of the machine(s) you wish to perform the operation on|None|["58ae74fae4b06dca39c1d4bc:PYLUMCLIENT_ORG1-PROD_WINTEST-PC_005056A104F9"]|

Example input:

```
{
  "argument": "Sensors are no longer in use",
  "sensor_ids": [
    "58ae74fae4b06dca39c1d4bc:PYLUMCLIENT_ORG1-PROD_WINTEST-PC_005056A104F9"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|archive_sensor_response|archiveSensorResponse|True|Archive sensor response|

Example output:

```
{
    "batchId": 605064018,
    "actionType": "Archive",
    "actionArguments": null,
    "globalStats": {
        "stats": {
            "FailedSending": 0,
            "InvalidState": 0,
            "ProbeRemoved": 0,
            "TimeoutSending": 0,
            "Pending": 0,
            "ChunksRequired": 0,
            "MsiFileCorrupted": 0,
            "SendingMsi": 0,
            "NewerInstalled": 0,
            "MsiSendFail": 0,
            "partialResponse": 0,
            "EndedWithSensorTimeout": 0,
            "FailedSendingToServer": 0,
            "GettingChunks": 0,
            "Aborted": 0,
            "Started": 0,
            "InProgress": 0,
            "Disconnected": 0,
            "Failed": 0,
            "Timeout": 0,
            "EndedWithTooManyResults": 0,
            "AlreadyUpdated": 0,
            "EndedWithTooManySearches": 0,
            "Succeeded": 0,
            "NotSupported": 0,
            "EndedWithUnknownError": 0,
            "None": 1,
            "Primed": 0,
            "EndedWithInvalidParam": 0,
            "UnknownProbe": 0,
            "AbortTimeout": 0,
            "UnauthorizedUser": 0
        }
    },
    "finalState": false,
    "totalNumberOfProbes": 1,
    "initiatorUser": "admin@myserver.com",
    "startTime": 1523875125179,
    "aborterUser": null,
    "abortTime": 0,
    "abortTimeout": false,
    "abortHttpStatusCode": null
}

```

#### Get Sensor

This action is used to get sensor.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|limit|integer|None|True|The number of sensors to which to send the request|None|1|
|offset|integer|None|True|Set to 0 to receive the first limit set of sensors|None|0|
|indicator|string|None|True|The unique identifier of the machine you wish to perform the operation on, this can be an internal IPv4 address, hostname or sensor GUID|None|104.31.2.164|

Example input:

```
{
  "limit": 1,
  "offset": 0,
  "indicator": "104.31.2.164"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sensor|sensors|True|Sensor|

Example output:

```
{
    "sensorId": "5e57b2dde4b06a3a515cc0eb:PYLUMCLIENT_SES_WIN10-EDLAB-AIQ_000C29B6AB6D",
    "pylumId": "PYLUMCLIENT_SES_WIN10-EDLAB-AIQ_000C29B6AB6D",
    "guid": "tEjQQRCi55eyTiwX",
    "fqdn": "win10-edlab-aiq1",
    "machineName": "win10-edlab-aiq1",
    "internalIpAddress": "111.11.133.21",
    "externalIpAddress": "2.16.258.145",
    "siteName": "Primary",
    "siteId": 46210509,
    "ransomwareStatus": "DETECT_SUSPEND_PREVENT",
    "preventionStatus": "ENABLED",
    "isolated": false,
    "disconnectionTime": 1628068498840,
    "lastPylumInfoMsgUpdateTime": 1628068444513,
    "lastPylumUpdateTimestampMs": 1628068498840,
    "status": "Archived",
    "serviceStatus": "Down",
    "onlineTimeMS": 0,
    "offlineTimeMS": 0,
    "staleTimeMS": 0,
    "archiveTimeMs": 1635854400487,
    "statusTimeMS": 0,
    "lastStatusAction": "None",
    "archivedOrUnarchiveComment": "Auto-archived after 60 days stale",
    "sensorArchivedByUser": "Auto-archived",
    "serverName": "ses-1-t",
    "serverId": "5e57b2dde4b06a3a515cc0eb",
    "serverIp": "10.130.8.127",
    "privateServerIp": "10.130.8.127",
    "collectiveUuid": "f9ca36d9-0c09-45e5-82d6-7e026ec1e803",
    "osType": "WINDOWS",
    "osVersionType": "Windows_10",
    "collectionStatus": "ADVANCED",
    "version": "21.1.144.0",
    "consoleVersion": null,
    "firstSeenTime": 1627316564474,
    "upTime": 695032210,
    "cpuUsage": 0.0,
    "memoryUsage": 0,
    "outdated": true,
    "amStatus": "AM_BLOCK",
    "amModeOrigin": null,
    "avDbVersion": "85274",
    "avDbLastUpdateTime": 1627468314000,
    "powerShellStatus": "PS_ENABLED",
    "remoteShellStatus": "AC_ENABLED",
    "usbStatus": "DISABLED",
    "fwStatus": "DISABLED",
    "antiExploitStatus": "AE_CAUTIOUS",
    "documentProtectionStatus": "DS_DETECT",
    "documentProtectionMode": "DM_CAUTIOUS",
    "serialNumber": "",
    "deviceModel": "Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz",
    "organizationalUnit": "",
    "antiMalwareStatus": "AM_ENABLED",
    "antiMalwareModeOrigin": null,
    "organization": "ses",
    "proxyAddress": "",
    "preventionError": "",
    "exitReason": "STOP_REQUEST_FROM_PYLUM",
    "actionsInProgress": 0,
    "pendingActions": [],
    "lastUpgradeResult": "None",
    "department": null,
    "location": null,
    "criticalAsset": null,
    "deviceType": null,
    "customTags": "CRITICAL",
    "lastUpgradeSteps": [],
    "disconnected": true,
    "staticAnalysisDetectMode": "MODERATE",
    "staticAnalysisDetectModeOrigin": null,
    "staticAnalysisPreventMode": "MODERATE",
    "staticAnalysisPreventModeOrigin": null,
    "collectionComponents": [
        "DPI",
        "Metadata",
        "File Events",
        "Registry Events"
    ],
    "sensorLastUpdate": 0,
    "fullScanStatus": "IDLE",
    "quickScanStatus": "IDLE",
    "lastFullScheduleScanSuccessTime": 0,
    "lastQuickScheduleScanSuccessTime": 0,
    "policyName": "ED_CUSTOM_POLICY",
    "deliveryTime": 1627328611652,
    "policyId": "8c1c93ff-08cb-4b4e-b253-7f5c9d3e08bc",
    "compliance": true,
    "groupId": "af617d16-b83e-4739-948d-339ce21b9177",
    "groupName": "aaa",
    "groupStickiness": true,
    "purgedSensors": false,
    "groupStickinessLabel": "Manual"
}
```

#### Delete Registry Key

This action is used to delete a registry key involved in a Malop.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|initiator_user_name|string|None|True|Initiator user name|None|user@example.com|
|malop_id|string|None|True|Malop ID to associate with the remediation actions|None|22.2787422324806222966|
|sensor|string|None|True|The unique identifier of the machine you wish to perform the quarantine/unquarantine operation on, this can be an internal IPv4 address, hostname or sensor GUID|None|-1632138521.1198775089551518743|

Example input:

```
{
  "initiator_user_name": "user@example.com",
  "malop_id": "22.2787422324806222966",
  "sensor": "hostname"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|remediate_items|True|Malop response|

Example output:

```
{
  "malopId": "22.2787422324806222966",
  "remediationId": "5144cf82-94c4-49f8-82cd-9ce1fcbd6a23",
  "start": 1624819406074,
  "initiatingUser": "user@example.com",
  "statusLog": []
}
```

#### Remediate Items

This action is used to remediate a specific process, file or registry key if remediation is possible.

This action supports the following action types: KILL_PROCESS, DELETE_REGISTRY_KEY, QUARANTINE_FILE, UNQUARANTINE_FILE, BLOCK_FILE, KILL_PREVENT_UNSUSPEND.

For more information about how to generate an `actions_by_machine` object, refer to [Cybereason documentation](https://nest.cybereason.com/documentation/api-documentation/all-versions/remediate-items#remediatemalops).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|actions_by_machine|object|None|True|Actions by machine|None|{"126811122.2298225282553311122": [{"targetId": "531122333.-3391199199911692223","actionType": "KILL_PROCESS"}]}|
|initiator_user_name|string|None|True|Initiator user name|None|user@example.com|
|malop_id|string|None|False|Malop ID to associate with the remediation actions|None|22.2787422324806222966|

Example input:

```
{
  "actions_by_machine": {
    "126811122.2298225282553311122": [
      {
        "targetId": "531122333.-3391199199911692223",
        "actionType": "KILL_PROCESS"
      }
    ]
  },
  "initiator_user_name": "user@example.com",
  "malop_id": "22.2787422324806222966"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|remediate_items|True|Malop response|

Example output:

```
{
  "malopId": "11.2189746432167327222",
  "remediationId": "5144cf82-94c4-49f8-82cd-9ce1fcbd6a23",
  "start": 1624819406074,
  "initiatingUser": "user@example.com",
  "statusLog": []
}
```

#### Quarantine File

This action is used to quarantine a detected malicious file in a secure location or unquarantine a file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|malop_id|string|None|True|Malop ID related to the file you wish to quarantine or unquarantine|None|22.2787422324806222966|
|quarantine|boolean|None|True|True to quarantine a file, False to remove file quarantine|None|True|
|sensor|string|None|True|The unique identifier of the machine you wish to perform the quarantine/unquarantine operation on, this can be an internal IPv4 address, hostname or sensor GUID|None|-1632138521.1198775089551518743|

Example input:

```
{
  "malop_id": "22.2787422324806222966",
  "quarantine": true,
  "sensor": "-1632138521.1198775089551518743"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|remediate_items_response|remediate_items|True|Remediate items response|

Example output:

```
{
  "remediate_items_response": {
    "malopId": "11.753856273233159896",
    "remediationId": "ea1a0c09-2491-4b00-b612-c51f8e7eb14a",
    "start": 1619207122620,
    "initiatingUser": "user@example.com",
    "statusLog": [
      {
        "machineId": "-626082210.1198775089551518743",
        "targetId": "-626082210.2561601065548740673",
        "status": "PENDING",
        "actionType": "QUARANTINE_FILE",
        "timestamp": 1619207122996
      }
    ]
  }
}
```

#### Isolate Machine

This action is used to isolate a machine associated with the root cause of a Malop, or to remediate a process not involved in a malop.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|malop_id|string|None|False|Malop ID to associate with the quarantine action|None|22.2787422324806222966|
|quarantine_state|boolean|True|True|True to isolate the sensor, false to un-isolate it|None|True|
|sensor|string|None|True|Sensor ID, hostname or IP address of the sensor to perform the action on|None|198.51.100.100|

Example input:

```
{
  "malop_id": "22.2787422324806222966",
  "quarantine_state": true,
  "sensor": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_id|string|True|Machine Pylum ID|
|success|boolean|True|Success|

Example output:

```
{
  "machine_id": "PYLUMCLIENT_EXAMPLE_EXAMPLE_HOSTNAME-WINS_000C29D6CBF7",
  "success": true
}
```

#### Search for Files

This action is used to find files on any machine in your environment with a Cybereason sensor installed.

Note that if the machine you are trying to search on is offline, the file search can remain open for up to 3 days.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_filter|string|None|True|A fileFilters object for filtering by machine name, folder, file creation or modification time or file size with operator Equals, NotEquals, ContainsIgnoreCase, NotContainsIgnoreCase and others|None|fileName Equals: ["sample.py"]|
|server_filter|string|None|False|A Sensor filters string for filtering sensors by different criteria such as operating system|None|machineName: ["rapid7-windows"]|

Example input:

```
{
  "file_filter": "fileName Equals: ["sample.py"]",
  "server_filter": "machineName: ["rapid7-windows"]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|True|Search file response|

Example output:

```
{
  "response": {
    "abortTime": 0,
    "abortTimeout": false,
    "actionArguments": {
      "@class": "com.cybereason.configuration.models.filesearch.FileSearchParameters",
      "fileSearchRequestConfiguration": {
        "cpuTrackingWindowMilli": 1000,
        "diskRateBytesPerMilli": 5120,
        "maxConcurrentFileSearches": 10,
        "maxDiskIOWindowMilli": 10000,
        "maxReadBytesPerFile": 110100480,
        "maxResults": 20,
        "maxYaraTimeouts": 10,
        "minFileReadPriceMilli": 1,
        "minThrottleAmountMilli": 5,
        "searchTimeoutDataScanSec": 200000,
        "searchTimeoutSec": 1200,
        "shouldUseNewAPI": false,
        "targetCpuPercentage": 20,
        "timoutPerFileScan": 9
      },
      "filters": [
        {
          "fieldName": "fileName",
          "operator": "ContainsIgnoreCase",
          "values": [
            "setup.exe"
          ]
        }
      ],
      "machines": []
    },
    "actionType": "FileSearchStart",
    "batchId": 111,
    "finalState": false,
    "globalStats": {
      "stats": {
        "AbortTimeout": 0,
        "Aborted": 0,
        "Aborting": 0,
        "AlreadyUpdated": 0,
        "BadArgument": 0,
        "ChunksRequired": 0,
        "Disconnected": 0,
        "EndedWithInvalidParam": 0,
        "EndedWithNoValidFolder": 0,
        "EndedWithSensorTimeout": 0,
        "EndedWithTooManyResults": 0,
        "EndedWithTooManySearches": 0,
        "EndedWithUnknownError": 0,
        "EndedWithUnsupportedFilter": 0,
        "EndedWithYaraCompileError": 0,
        "Failed": 0,
        "FailedSending": 0,
        "FailedSendingToServer": 0,
        "GettingChunks": 0,
        "InProgress": 0,
        "InvalidState": 0,
        "MsiFileCorrupted": 0,
        "MsiSendFail": 0,
        "NewerInstalled": 0,
        "None": 1,
        "NotSupported": 0,
        "Pending": 0,
        "Primed": 0,
        "ProbeRemoved": 0,
        "SendingMsi": 0,
        "SendingPlatform": 0,
        "Started": 0,
        "Succeeded": 0,
        "Timeout": 0,
        "TimeoutSending": 0,
        "UnauthorizedUser": 0,
        "UnknownProbe": 0,
        "partialResponse": 0
      }
    },
    "initiatorUser": "user@example.com",
    "startTime": 1614481205231,
    "totalNumberOfProbes": 1
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

* 2.2.0 - Added new actions: Get Sensor, Archive Sensor
* 2.1.0 - New action Delete Registry Key | Add support product versions
* 2.0.2 - Remove ISOLATE_MACHINE option from Remediate Items action documentation
* 2.0.1 - Fix incorrect error messaging when invalid credentials are used
* 2.0.0 - Update action Isolate Machine | New action Remediate Items
* 1.2.0 - Add new action Quarantine File
* 1.1.0 - Add new action Isolate Machine
* 1.0.0 - Initial plugin

# Links

https://nest.cybereason.com/documentation/api-documentation

## References

* [Cybereason Plugin](https://www.cybereason.com/)
* [Cybereason Plugin API](https://nest.cybereason.com/user/login?destination=/documentation/api-documentation/all-versions/cybereason-api-guide)
