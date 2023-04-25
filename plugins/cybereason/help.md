# Description

The Cybereason platform provides military-grade cyber security with real-time awareness and detection. Respond to threats and remediate in seconds using the Cybereason plugin.

# Key Features

* Quickly respond to threats by quarantining (isolating) a machine associated with a Malop
* Search files on machines

# Requirements

* Requires a Cybereason username and password
* Cybereason account configured as shown [here](https://nest.cybereason.com/user/login?destination=/documentation/product-documentation/191/search-and-browse-files-machines-0#pre-requisites) for File Search capabilities

# Supported Product Versions

* Cybereason API 2023-04-12

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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|archive_sensor_response|archiveSensorResponse|True|Archive sensor response|{}|

Example output:

```
{
  "batchId": 605064018,
  "actionType": "Archive",
  "actionArguments": null,
  "globalStats": {
    "stats": {
      "failedSending": 0,
      "invalidState": 0,
      "probeRemoved": 0,
      "timeoutSending": 0,
      "pending": 0,
      "chunksRequired": 0,
      "msiFileCorrupted": 0,
      "sendingMsi": 0,
      "newerInstalled": 0,
      "msiSendFail": 0,
      "partialResponse": 0,
      "endedWithSensorTimeout": 0,
      "failedSendingToServer": 0,
      "gettingChunks": 0,
      "aborted": 0,
      "started": 0,
      "inProgress": 0,
      "disconnected": 0,
      "failed": 0,
      "timeout": 0,
      "endedWithTooManyResults": 0,
      "alreadyUpdated": 0,
      "endedWithTooManySearches": 0,
      "succeeded": 0,
      "notSupported": 0,
      "endedWithUnknownError": 0,
      "none": 1,
      "primed": 0,
      "endedWithInvalidParam": 0,
      "unknownProbe": 0,
      "abortTimeout": 0,
      "unauthorizedUser": 0
    }
  },
  "finalState": false,
  "totalNumberOfProbes": 1,
  "initiatorUser": "user@example.com",
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
|indicator|string|None|True|The unique identifier of the machine you wish to perform the operation on, this can be an internal IPv4 address, hostname or sensor GUID|None|104.31.2.164|
|limit|integer|None|True|The number of sensors to which to send the request|None|1|
|offset|integer|None|True|Set to 0 to receive the first limit set of sensors|None|0|

Example input:

```
{
  "indicator": "104.31.2.164",
  "limit": 1,
  "offset": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|sensor|sensor|True|Sensor|{}|

Example output:

```
{
  "$success": true,
  "sensor": {
    "hasMoreResults": false,
    "sensors": [
      {
        "actionsInProgress": 0,
        "amStatus": "AM_QUARANTINE",
        "antiExploitStatus": "AE_DISABLED",
        "antiMalwareStatus": "AM_ENABLED",
        "archiveTimeMs": 1682425952496,
        "archivedOrUnarchiveComment": "icon_test",
        "avDbLastUpdateTime": 1681997830000,
        "avDbVersion": "90436",
        "collectionComponents": [
          "Metadata"
        ],
        "collectionStatus": "ADVANCED",
        "collectiveUuid": "70b8b433-e8ba-4375-8eb5-1c0d95c62120",
        "compliance": true,
        "cpuUsage": 0,
        "deliveryTime": 1681892958527,
        "deviceModel": "Intel(R) Xeon(R) CPU E5-2690 v2 @ 3.00GHz",
        "disconnected": true,
        "disconnectionTime": 1681999288065,
        "documentProtectionMode": "DM_CAUTIOUS",
        "documentProtectionStatus": "DS_DISABLED",
        "exitReason": "STOP_REQUEST_FROM_PYLUM",
        "externalIpAddress": "128.177.65.3",
        "firstSeenTime": 1681892763453,
        "fqdn": "tomascybereasonsensor",
        "fullScanStatus": "IDLE",
        "fwStatus": "DISABLED",
        "groupId": "9f0fabc3-9a6e-4247-b235-dbab187e3409",
        "groupName": "Perimeter 2",
        "groupStickiness": false,
        "groupStickinessLabel": "Dynamic",
        "guid": "J1zJSBCi55eyTiwX",
        "internalIpAddress": "10.4.84.0",
        "isolated": false,
        "lastFullScheduleScanSuccessTime": 0,
        "lastPylumInfoMsgUpdateTime": 1681998983712,
        "lastPylumUpdateTimestampMs": 1681999288065,
        "lastQuickScheduleScanSuccessTime": 1681296325000,
        "lastStatusAction": "Archive",
        "lastUpgradeResult": "AlreadyUpdated",
        "lastUpgradeSteps": [
          {
            "name": "Started",
            "startTime": 1681906178901
          },
          {
            "name": "AlreadyUpdated",
            "startTime": 1681906178904
          }
        ],
        "machineName": "tomascybereasonsensor",
        "memoryUsage": 0,
        "offlineTimeMS": 0,
        "onlineTimeMS": 0,
        "organization": "integration",
        "osType": "WINDOWS",
        "osVersionType": "Windows_10",
        "outdated": false,
        "pendingActions": [],
        "policyId": "81ae6eb3-2491-4249-8884-25f98d55d5fa",
        "policyName": "Default",
        "powerShellStatus": "PS_DISABLED",
        "preventionStatus": "DISABLED",
        "privateServerIp": "10.146.1.168",
        "purgedSensors": false,
        "pylumId": "PYLUMCLIENT_INTEGRATION_TOMASCYBEREASON_005056945ADC",
        "quickScanStatus": "IDLE",
        "ransomwareStatus": "DISABLED",
        "remoteShellStatus": "AC_DISABLED",
        "sensorArchivedByUser": "wayne_johnstone@rapid7.com",
        "sensorId": "5e77883de4b0575ddcf824ef:PYLUMCLIENT_INTEGRATION_TOMASCYBEREASON_005056945ADC",
        "sensorLastUpdate": 0,
        "serialNumber": "VMware-42 14 9f a1 c5 c6 b4 ad-34 41 0e 80 6a a4 21 2c",
        "serverId": "5e77883de4b0575ddcf824ef",
        "serverIp": "10.146.1.168",
        "serverName": "integration-1-t",
        "serviceStatus": "Down",
        "siteId": 0,
        "siteName": "Default",
        "staleTimeMS": 0,
        "staticAnalysisDetectMode": "DISABLED",
        "staticAnalysisPreventMode": "DISABLED",
        "status": "Archived",
        "statusTimeMS": 0,
        "upTime": 1632708,
        "usbStatus": "DISABLED",
        "version": "22.1.169.0"
      }
    ],
    "sensorsStatus": {
      "@class": ".SensorsStatusOverview",
      "advancedCount": 0,
      "archivedCount": 1,
      "offlineCount": 0,
      "onlineCount": 0,
      "outdatedCount": 0,
      "serviceErrorCount": 0,
      "staleCount": 0,
      "suspendedCount": 0,
      "turnedOffCount": 0,
      "turnedOnCount": 0
    },
    "totalResults": 1
  }
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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|remediate_items|True|Malop response|{}|

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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|remediate_items|True|Malop response|{}|

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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|remediate_items_response|remediate_items|True|Remediate items response|{}|

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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|machine_id|string|True|Machine Pylum ID|PYLUMCLIENT_INTEGRATION_DESKTOP-EXAMPLE_1234567AB12C|
|success|boolean|True|Success|True|

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
  "file_filter": "fileName Equals: ['sample.py']",
  "server_filter": "machineName: ['rapid7-windows']"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|True|Search file response|{}|

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

* 2.3.0 - Fix Output for `Get Sensor` 
* 2.2.0 - Added new actions: `Get Sensor` & `Archive Sensor`
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
