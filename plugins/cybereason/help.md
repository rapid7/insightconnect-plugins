# Description

The Cybereason platform provides military-grade cyber security with real-time awareness and detection. Respond to threats and remediate in seconds using the Cybereason plugin.

# Key Features

* Quickly respond to threats by quarantining (isolating) a machine associated with a Malop
* Search files on machines

# Requirements

* Requires a Cybereason username and password
* Cybereason account configured as shown [here](https://nest.cybereason.com/user/login?destination=/documentation/product-documentation/191/search-and-browse-files-machines-0#pre-requisites) for File Search capabilities

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

#### Remediate Items

This action is used to remediate a specific process, file or registry key if remediation is possible.

This action supports the following action types: KILL_PROCESS, DELETE_REGISTRY_KEY, QUARANTINE_FILE, UNQUARANTINE_FILE, BLOCK_FILE, KILL_PREVENT_UNSUSPEND, ISOLATE_MACHINE.

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
  "file_filter": "fileName Equals: [\"sample.py\"]",
  "server_filter": "machineName: [\"rapid7-windows\"]"
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

* 2.0.0 - Update action Isolate Machine | New action Remediate Items
* 1.2.0 - Add new action Quarantine File
* 1.1.0 - Add new action Isolate Machine
* 1.0.0 - Initial plugin

# Links

## References

* [Cybereason Plugin](https://www.cybereason.com/)
* [Cybereason Plugin API](https://nest.cybereason.com/user/login?destination=/documentation/api-documentation/all-versions/cybereason-api-guide)
