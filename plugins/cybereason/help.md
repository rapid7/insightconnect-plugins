# Description

The Cybereason platform provides military-grade cyber security with real-time awareness and detection. Respond to threats and remediate in seconds using the Cybereason plugin

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

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|False|Username and password|None|{"username": "user@example.com", "password": "mypassword"}|None|None|
|hostname|string|None|True|Enter the hostname|None|example.com|None|None|
|port|integer|8443|True|Enter the port|None|8443|None|None|

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

This action is used to archive sensor

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|argument|string|None|True|The reason for archiving the sensor or sensors|None|Sensors are no longer in use|None|None|
|sensor_ids|[]string|None|True|The unique identifier of the machine(s) you wish to perform the operation on|None|["58ae74fae4b06dca39c1d4bc:PYLUMCLIENT_ORG1-PROD_WINTEST-PC_005056A104F9"]|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
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

#### Delete Registry Key

This action is used to delete a registry key involved in a Malop

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|initiator_user_name|string|None|True|Initiator user name|None|user@example.com|None|None|
|malop_id|string|None|True|Malop ID to associate with the remediation actions|None|22.2787422324806222966|None|None|
|sensor|string|None|True|The unique identifier of the machine you wish to perform the quarantine/unquarantine operation on, this can be an internal IPv4 address, hostname or sensor GUID|None|-1632138521.1198775089551518743|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
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

#### Get Sensor

This action is used to get sensor

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|indicator|string|None|True|The unique identifier of the machine you wish to perform the operation on, this can be an internal IPv4 address, hostname or sensor GUID|None|104.31.2.164|None|None|
|limit|integer|None|True|The number of sensors to which to send the request|None|1|None|None|
|offset|integer|None|True|Set to 0 to receive the first limit set of sensors|None|0|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|sensor|sensor|True|Sensor|{}|
  
Example output:

```
{
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
        "collectiveUuid": "70b8b433-1ab2-1234-1ab2-1c0d95c62120",
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
        "fqdn": "cybereasonsensor",
        "fullScanStatus": "IDLE",
        "fwStatus": "DISABLED",
        "groupId": "9f0fabc3-a12b-1234-a12b-dbab187e3409",
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
        "machineName": "cybereasonsensor",
        "memoryUsage": 0,
        "offlineTimeMS": 0,
        "onlineTimeMS": 0,
        "organization": "integration",
        "osType": "WINDOWS",
        "osVersionType": "Windows_10",
        "outdated": false,
        "pendingActions": [],
        "policyId": "81ae6eb3-1234-1234-1234-25f98d55d5fa",
        "policyName": "Default",
        "powerShellStatus": "PS_DISABLED",
        "preventionStatus": "DISABLED",
        "privateServerIp": "10.146.1.168",
        "purgedSensors": false,
        "pylumId": "PYLUMCLIENT_INTEGRATION_CYBEREASON_0000000000ABC",
        "quickScanStatus": "IDLE",
        "ransomwareStatus": "DISABLED",
        "remoteShellStatus": "AC_DISABLED",
        "sensorArchivedByUser": "user@example.com",
        "sensorId": "5e77777ab4b1234ddcf824ef:PYLUMCLIENT_INTEGRATION_CYBEREASON_0000000000ABC",
        "sensorLastUpdate": 0,
        "serialNumber": "VMware-42 14 9f a1 c5 c6 b4 ad-34 41 0e 80 6a a4 21 2c",
        "serverId": "1a22333de4b0575ddcf123ab",
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

#### Isolate Machine

This action is used to isolate a machine associated with the root cause of a Malop, or to remediate a process not involved in a malop

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|malop_id|string|None|False|Malop ID to associate with the quarantine action|None|22.2787422324806222966|None|None|
|quarantine_state|boolean|True|True|True to isolate the sensor, false to un-isolate it|None|True|None|None|
|sensor|string|None|True|Sensor ID, hostname or IP address of the sensor to perform the action on|None|198.51.100.100|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|machine_id|string|True|Machine Pylum ID|PYLUMCLIENT_INTEGRATION_DESKTOP-EXAMPLE_1234567AB12C|
|success|boolean|True|Success|True|
  
Example output:

```
{
  "machine_id": "PYLUMCLIENT_INTEGRATION_DESKTOP-EXAMPLE_1234567AB12C",
  "success": true
}
```

#### Quarantine File

This action is used to quarantine a detected malicious file in a secure location or unquarantine a file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|malop_id|string|None|True|Malop ID related to the file you wish to quarantine or unquarantine|None|22.2787422324806222966|None|None|
|quarantine|boolean|None|True|True to quarantine a file, False to remove file quarantine|None|True|None|None|
|sensor|string|None|True|The unique identifier of the machine you wish to perform the quarantine/unquarantine operation on, this can be an internal IPv4 address, hostname or sensor GUID|None|-1632138521.1198775089551518743|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
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

#### Remediate Items

This action is used to remediate a specific process, file or registry key if remediation is possible.

This action supports the following action types: KILL_PROCESS, DELETE_REGISTRY_KEY, QUARANTINE_FILE, UNQUARANTINE_FILE, BLOCK_FILE, KILL_PREVENT_UNSUSPEND.

For more information about how to generate an `actions_by_machine` object, refer to [Cybereason documentation](https://nest.cybereason.com/documentation/api-documentation/all-versions/remediate-items#remediatemalops).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|actions_by_machine|object|None|True|Actions by machine|None|{"126811122.2298225282553311122": [{"targetId": "531122333.-3391199199911692223","actionType": "KILL_PROCESS"}]}|None|None|
|initiator_user_name|string|None|True|Initiator user name|None|user@example.com|None|None|
|malop_id|string|None|False|Malop ID to associate with the remediation actions|None|22.2787422324806222966|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
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

#### Search for Files

This action is used to find files on any machine in your environment with a Cybereason sensor installed.

Note that if the machine you are trying to search on is offline, the file search can remain open for up to 3 days.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_filter|string|None|True|A fileFilters object for filtering by machine name, folder, file creation or modification time or file size with operator Equals, NotEquals, ContainsIgnoreCase, NotContainsIgnoreCase and others|None|fileName Equals: ["sample.py"]|None|None|
|server_filter|string|None|False|A Sensor filters string for filtering sensors by different criteria such as operating system|None|machineName: ["rapid7-windows"]|None|None|
  
Example input:

```
{
  "file_filter": "fileName Equals: ['sample.py']",
  "server_filter": "machineName: ['rapid7-windows']"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
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
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**fileSearchRequestConfiguration**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CPU Tracking Window Milli|integer|None|False|CPU tracking window milli|None|
|Disk Rate Bytes Per Milli|integer|None|False|Disk rate bytes per milli|None|
|Max Concurrent File Searches|integer|None|False|Max concurrent file searches|None|
|Max Disk IOWindow Milli|integer|None|False|Max disk IO window milli|None|
|Max Read Bytes Per File|integer|None|False|Max read bytes per file|None|
|Max Results|integer|None|False|Max results|None|
|Max Yara timeouts|integer|None|False|Max yara timeouts|None|
|Min File Read Price Milli|integer|None|False|Min file read price milli|None|
|Min Throttle Amount Milli|integer|None|False|Min throttle amount milli|None|
|Search Timeout Data Scan Sec|integer|None|False|Search timeout data scan sec|None|
|Search Timeout Sec|integer|None|False|Search timeout sec|None|
|Should Use New API|boolean|None|False|Should use new API|None|
|Target CPU Percentage|integer|None|False|Target CPU percentage|None|
|Timout Per File Scan|integer|None|False|Timout per file scan|None|
  
**filters**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Field Name|string|None|False|Field name|None|
|Operator|string|None|False|Operator|None|
|Values|[]string|None|False|Values|None|
  
**actionArguments**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|File Search Request Configuration|fileSearchRequestConfiguration|None|False|File search request configuration|None|
|Filters|[]filters|None|False|Filters|None|
|Machines|[]string|None|False|Machines|None|
|Yara Name|string|None|False|Yara name|None|
  
**stats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Abort Timeout|integer|None|False|Abort timeout|None|
|Aborted|integer|None|False|Aborted|None|
|Aborting|integer|None|False|Aborting|None|
|Already Updated|integer|None|False|Already updated|None|
|Bad Argument|integer|None|False|Bad argument|None|
|Chunks Required|integer|None|False|Chunks required|None|
|Disconnected|integer|None|False|Disconnected|None|
|Ended With Invalid Param|integer|None|False|Ended with invalid param|None|
|Ended With No Valid Folder|integer|None|False|Ended with no valid folder|None|
|Ended With Sensor Timeout|integer|None|False|Ended with sensor timeout|None|
|Ended With Too Many Results|integer|None|False|Ended with too many results|None|
|Ended With Too Many Searches|integer|None|False|Ended with too many searches|None|
|Ended With Unknown Error|integer|None|False|Ended with unknown error|None|
|Ended With Unsupported Filter|integer|None|False|Ended with unsupported filter|None|
|Ended With Yara Compile Error|integer|None|False|Ended with yara compile error|None|
|Failed|integer|None|False|Failed|None|
|Failed Sending|integer|None|False|Failed sending|None|
|Failed Sending To Server|integer|None|False|Failed sending to server|None|
|Getting Chunks|integer|None|False|Getting chunks|None|
|In Progress|integer|None|False|In progress|None|
|Invalid State|integer|None|False|Invalid state|None|
|MSI File Corrupted|integer|None|False|MSI file corrupted|None|
|MSI Send Fail|integer|None|False|MSI Send Fail|None|
|Newer Installed|integer|None|False|Newer installed|None|
|None|integer|None|False|None|None|
|Not Supported|integer|None|False|Not supported|None|
|Pending|integer|None|False|Pending|None|
|Primed|integer|None|False|Primed|None|
|Probe Removed|integer|None|False|Probe removed|None|
|Sending MSI|integer|None|False|Sending MSI|None|
|Sending Platform|integer|None|False|Sending platform|None|
|Started|integer|None|False|Started|None|
|Succeeded|integer|None|False|Succeeded|None|
|Timeout|integer|None|False|Timeout|None|
|Timeout Sending|integer|None|False|Timeout sending|None|
|Unauthorized User|integer|None|False|Unauthorized user|None|
|Unknown Probe|integer|None|False|Unknown probe|None|
|Partial Response|integer|None|False|Partial response|None|
  
**sensorStats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Abort Timeout|integer|None|False|Abort timeout|None|
|Aborted|integer|None|False|Aborted|None|
|Already Updated|integer|None|False|Already updated|None|
|Chunks Required|integer|None|False|Chunks required|None|
|Disconnected|integer|None|False|Disconnected|None|
|Ended With Invalid Param|integer|None|False|Ended with invalid param|None|
|Ended With Sensor Timeout|integer|None|False|Ended with sensor timeout|None|
|Ended With Too Many Results|integer|None|False|Ended with too many results|None|
|Ended With Too Many Searches|integer|None|False|Ended with too many searches|None|
|Ended With Unknown Error|integer|None|False|Ended with unknown error|None|
|Failed|integer|None|False|Failed|None|
|Failed Sending|integer|None|False|Failed sending|None|
|Failed Sending To Server|integer|None|False|Failed sending to server|None|
|Getting Chunks|integer|None|False|Getting chunks|None|
|In Progress|integer|None|False|In progress|None|
|Invalid State|integer|None|False|Invalid state|None|
|MSI File Corrupted|integer|None|False|MSI file corrupted|None|
|MSI Send Fail|integer|None|False|MSI Send Fail|None|
|Newer Installed|integer|None|False|Newer installed|None|
|None|integer|None|False|None|None|
|Not Supported|integer|None|False|Not supported|None|
|Partial Response|integer|None|False|Partial response|None|
|Pending|integer|None|False|Pending|None|
|Primed|integer|None|False|Primed|None|
|Probe Removed|integer|None|False|Probe removed|None|
|Sending MSI|integer|None|False|Sending MSI|None|
|Started|integer|None|False|Started|None|
|Succeeded|integer|None|False|Succeeded|None|
|Timeout|integer|None|False|Timeout|None|
|Timeout Sending|integer|None|False|Timeout sending|None|
|Unauthorized User|integer|None|False|Unauthorized user|None|
|Unknown Probe|integer|None|False|Unknown probe|None|
  
**lastUpgradeSteps**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|name of step|None|
|Start Time|integer|None|True|time in epoch that the step started|None|
  
**globalStats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Stats|stats|None|False|Stats|None|
  
**globalSensorStats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|sensorStats|sensorStats|None|False|Stats|None|
  
**archiveSensorResponse**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Abort HTTP Status Code|string|None|False|The code sent by the server to abort the operation. This field only exists if the operation was aborted|None|
|Abort Time|integer|None|False|The time (in epoch) when the operation was aborted. This field only exists if the operation was aborted|None|
|Abort Timeout|boolean|None|True|Indicates whether there is a timeout value for timing out the request to abort|None|
|Aborter User|string|None|False|The user name of the user who aborted the operation. This field only exists if the operation was aborted|None|
|Action Arguments|string|None|False|The arguments passed for the operation|None|
|Action Type|string|None|True|The action taken on the sensor|None|
|Batch ID|integer|None|True|The ID for the operation. You may need this number for other operations|None|
|Final State|boolean|None|True|Indicates whether the sensor is in the state indicated by the operation|None|
|Global Stats|globalSensorStats|None|True|Collection of items about the operation|None|
|Initiator User|string|None|True|The user name of the user who performed this operation|None|
|Start Time|integer|None|True|The start time of the operation|None|
|Total Number Of Probes|integer|None|True|None|None|
  
**response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Abort HTTP Status Code|string|None|False|Abort HTTP status code|None|
|Abort Time|integer|None|False|Abort time|None|
|Abort Timeout|boolean|None|False|Abort timeout|None|
|Aborter User|string|None|False|Aborter user|None|
|Action Arguments|actionArguments|None|False|Action arguments|None|
|Action Type|string|None|False|Action type|None|
|Batch ID|integer|None|False|Batch ID|None|
|Final State|boolean|None|False|Final state|None|
|Global Stats|globalStats|None|False|Global stats|None|
|Initiator User|string|None|False|Initiator user|None|
|Start Time|integer|None|False|Start time|None|
|Total Number Probes|integer|None|False|Total number of probes|None|
  
**statusLog**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action Type|string|None|False|The type of action you attempted to perform|None|
|Machine ID|string|None|False|The unique ID for the machine or machines on which the remediation was performed|None|
|Status|string|None|False|The status of the remediation request|None|
|Target ID|string|None|False|Reports a null value|None|
|Timestamp|integer|None|False|The time (in epoch) of the status report for the remediation request|None|
  
**error**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Error Type|string|None|False|The type of error|None|
|Message|string|None|False|A description of the error|None|
  
**remediate_items**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|End|integer|None|False|The time (in epoch) that the remediation operation ended|None|
|Error|[]error|None|False|An object containing details of the error|None|
|Initiating User|string|None|False|The Cybereason user name of the user initiating the remediation|None|
|Malop ID|string|None|False|The numerical identifier of the Malop assigned by Cybereason|None|
|Remediation ID|string|None|False|The numerical identifier of the Malop assigned by Cybereason|None|
|Start|integer|None|False|The time (in epoch) that the remediation operation began|None|
|Status Log|[]statusLog|None|False|An object containing information about the remediation|None|
  
**sensors**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actions In Progress|integer|None|False|The number of actions in progress (i.e. Not Resolved) on the machine|0|
|Anti-Malware Status|string|None|False|The Anti-Malware installation status for the sensor|AM_QUARANTINE|
|Anti Exploit Status|string|None|False|The status of the Exploit Prevention feature. This field returns a value only if you have enabled Exploit Prevention.|AE_CAUTIOUS|
|Anti Malware Status|string|None|False|The Anti-Malware prevention mode for the sensor|AM_ENABLED|
|Archive Time MS|integer|None|False|The time (in epoch) when the sensor was archived|1635854400487|
|Archived Or Unarchive Comment|string|None|False|The comment added when a sensor was archived or unarchived|Auto-archived after 60 days stale|
|AV DB Last Update Time|integer|None|False|The time when the Anti-Malware Signatures database on the machine where the sensor is installed was last updated|1627468314000|
|AV DB Version|string|None|False|The version of the Anti-Malware Signatures database on the machine where the sensor is installed|85274|
|Collection Components|[]string|None|False|Any special collections enabled on the server and/or sensor|DPI|
|Collection Status|string|None|False|States whether the machine has data collection enabled|ADVANCED|
|Collective UUID|string|None|False|The identifier for the Registration server for the sensor|f9ca36d9-0c09-45e5-82d6-7e026ec1e803|
|Compliance|boolean|None|False|Indicates whether the current sensor settings match the policy settings|True|
|CPU Usage|float|None|False|The amount of CPU used by the machine (expressed as a percentage)|0.0|
|Delivery Time|integer|None|False|The time (in epoch) when the last policy update was delivered to the sensor|1627328611652|
|Device Model|string|None|False|The model added for a device in the allowed devices section of the Endpoint Controls settings|Intel(R) Core(TM) i9-9880H CPU 2.30GHz|
|Disconnected|boolean|None|False|Indicates whether a sensor is currently disconnected|True|
|Disconnection Time|integer|None|False|Time the machine was disconnected. Returns 0 if this is the first connection time. After the first connection, this is the time it was last connected|1628068498840|
|Document Protection Mode|string|None|False|The mode set for the Document Protection mode|DM_CAUTIOUS|
|Document Protection Status|string|None|False|The status for the Document Protection mode|DS_DETECT|
|Exit Reason|string|None|False|The reason the sensor service (minionhost.exe) stopped|STOP_REQUEST_FROM_PYLUM|
|External IP Address|string|None|False|The machine's external IP address for the local network|2.16.258.145|
|First Seen Time|integer|None|False|The first time the machine was recognized. Timestamp values are returned in epoch|1627316564474|
|Fully Qualified Domain Name|string|None|False|the fully qualified domain name (fqdn) for the machine|tEjQQRCi55eyTwiX|
|Full Scan Status|string|None|False|The status set for the sensor for the full scan|IDLE|
|Fire Wall Status|string|None|False|The status of the Personal Firewall Control feature. This field returns a value only if you have enabled Endpoint Controls.|DISABLED|
|Group ID|string|None|False|The identifier the Cybereason platform uses for the group to which the sensor is assigned|af617d16-b83e-4739-948d-339ce21b9177|
|Group Name|string|None|False|The name for the group to which the sensor is assigned|aaa|
|Group Stickiness|boolean|None|False|Indicates whether this sensor is automatically assigned back to the group based on an assignment rule|True|
|Group Stickiness Label|string|None|False|The method by which the sensor was assigned to the group|Manual|
|Global Unique ID|string|None|False|The globally unique sensor identifier|tEjQQRCi55eyTwiX|
|Internal IP Address|string|None|False|The machine's internal IP address as identified by the sensor|111.11.133.21|
|Isolated|boolean|None|False|States whether the machine is isolated. Returns true if the machine is isolated|false|
|Last Full Schedule Scan Success Time|integer|None|False|The time (in epoch) that the sensor last did a successful full scan|0|
|Last Quick Pylum Info Message Update Time|integer|None|False|The time (in epoch) that the last quick pylum info message updated|0|
|Last Quick Pylum Update Timestamp|integer|None|False|The time (in epoch) that the last pylum updated|0|
|Last Quick Schedule Scan Success Time|integer|None|False|The time (in epoch) that the sensor last did a successful quick scan|0|
|Last Status Action|string|None|False|The last action taken that changed the sensor status|None|
|Last Upgrade Result|string|None|False|The result of the last upgrade process|None|
|Last Upgrade Steps|[]lastUpgradeSteps|None|False|A list of step taken in the upgrade process. If there is a failure to upgrade the sensor, this list shows the failure|[]|
|Machine Name|string|None|False|The name of the machine|win10-edlab-aiq1|
|Memory Usage|integer|None|False|The amount of RAM on the hosting computer used by the sensor|0|
|Offline Time MS|integer|None|False|he last time (in epoch) that the sensor was offline|0|
|Online Time MS|integer|None|False|The last time the sensor was seen online|0|
|Organization|string|None|False|The organization name for the machine on which the sensor is installed|ses|
|OS Type|string|None|False|The operating system running on the machine|WINDOWS|
|OS Version Type|string|None|False|collectionStatus|Windows_10|
|Outdated|boolean|None|False|States whether or not the sensor version is out of sync with the server version|True|
|Pending Actions|[]integer|None|False|An array containing batch numbers for actions pending to run on the sensor|[]|
|Policy ID|string|None|False|The unique identifier the Cybereason platform uses for the policy assigned to the sensor|8c1c93ff-08cb-4b4e-b253-7f5c9d3e08bc|
|Policy Name|string|None|False|The name of the policy assigned to this sensor|ED_CUSTOM_POLICY|
|Power Shell Status|string|None|False|The PowerShell Prevention mode|PS_ENABLED|
|Prevention Status|string|None|False|The Execution Prevention mode|ENABLE|
|Private Server IP|string|None|False|The private IP address for the Detection server for the sensor|10.130.8.127|
|Purged Sensors|boolean|None|False|Indicates whether this sensor was removed from the Sensors screen|False|
|Pylum ID|string|None|False|The unique identifier assigned by Cybereason to the sensor|PYLUMCLIENT_SES_WIN10-EDLAB-AIQ_000C29B6AB6D|
|Quick Scan Status|string|None|False|The status set for the sensor for a quick scan|IDLE|
|Ransomware Status|string|None|False|The Anti-Ransomware mode|DETECT_SUSPEND_PREVENT|
|Remote Shell Status|string|None|False|Whether or not the Remote Shell utility is enabled for the sensor. This field returns a value only if you have enabled Remote Shell for your Cybereason server|AC_ENABLED|
|Sensor Archived By User|string|None|False|The Cybereason user name for the user who archived the selected sensor|Auto-archived|
|Sensor ID|string|None|False|The unique identifier for a sensor|5e57b2dde4b06a3a515cc0eb:PYLUMCLIENT_SES_WIN10-EDLAB-AIQ_000C29B6AB6D|
|Sensor Last Update|integer|None|False|The last time (in epoch) that the sensor was updated|0|
|Serial Number|string|None|False|The serial number added for a device in the allowed devices section of the Endpoint Controls settings|1234567|
|Server ID|string|None|False|The unique identifier for the Detection server for the sensor|5e57b2dde4b06a3a515cc0eb|
|Server IP|string|None|False|The IP address for the Detection server for the sensor|10.130.8.127|
|Server Name|string|None|False|The name of the server for the sensor|ses-1-t|
|Service Status|string|None|False|Indicates the current value of the Anti-Malware service|Down|
|Machine Name|integer|None|False|The identifier for the sensor's site|46210509|
|Site Name|string|None|False|The name of the site for the sensor|Primary|
|Stale Time MS|integer|None|False|The time (in epoch) when the Sensor was classified as Stale|0|
|Static Analysis Detect Mode|string|None|False|The value for the Artificial Intelligence Detect mode in the Anti-Malware settings|MODERATE|
|Static Analysis Prevent Mode|string|None|False|The value for the Artificial Intelligence Prevent Mode in the Anti-Malware settings|MODERATE|
|Status|string|None|False|The status of the sensor|Archived|
|Status Time MS|integer|None|False|The last time (in epoch) when the sensor sent a status|0|
|Up Time|integer|None|False|The time the sensors have been in the UP state|695032210|
|USB Status|string|None|False|The status of the Device Control feature. This field returns a value only if you have enabled Endpoint Controls.|DISABLED|
|Version|string|None|False|The sensor version number|21.1.144.0|
  
**getSensorStats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Advanced Count|integer|None|None|How many sensors are advanced|0|
|Archived Count|integer|None|None|How many sensors are archived|0|
|Class|string|None|None|class of object|.SensorsStatusOverview|
|Offline Count|integer|None|None|How many sensors are offline|0|
|Online Count|integer|None|None|How many sensors are online|0|
|Outdated Count|integer|None|None|How many sensors are outdated|0|
|Service Error Count|integer|None|None|How many sensors are experiencing service errors|0|
|Stale Count|integer|None|None|How many sensors are stale|0|
|Suspended Count|integer|None|None|How many sensors are suspended|0|
|Turned Off Count|integer|None|None|How many sensors are turned off|0|
|Turned On Count|integer|None|None|How many sensors are turned on|0|
  
**sensor**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Has More Results|boolean|None|True|Was there more possible results that were excluded because of limit|False|
|Sensor Status|getSensorStats|None|None|sensors status|{}|
|Sensors|[]sensors|None|None|list of dictionaries containing sensor information|[]|
|Total Results|integer|None|None|how many sensors did we get information from|1|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 3.0.1 - Bumping requirements.txt | SDK bump to 6.2.0
* 3.0.0 - Fix Output for `Get Sensor`
* 2.2.0 - Added new actions: `Get Sensor` & `Archive Sensor`
* 2.1.0 - New action Delete Registry Key | Add support product versions
* 2.0.2 - Remove ISOLATE_MACHINE option from Remediate Items action documentation
* 2.0.1 - Fix incorrect error messaging when invalid credentials are used
* 2.0.0 - Update action Isolate Machine | New action Remediate Items
* 1.2.0 - Add new action Quarantine File
* 1.1.0 - Add new action Isolate Machine
* 1.0.0 - Initial plugin

# Links

* [Cybereason Plugin](https://www.cybereason.com/)

## References

* [Cybereason Plugin API](https://nest.cybereason.com/documentation/api-documentation)
* [Cybereason Plugin API](https://nest.cybereason.com/user/login?destination=/documentation/api-documentation/all-versions/cybereason-api-guide)