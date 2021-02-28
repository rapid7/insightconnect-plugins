# Description

The Cybereason platform provides military-grade cyber security with real-time awareness and detection.

# Key Features

* Search files on machines

# Requirements

* Requires an username and password

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
  "credentials": "{\"username\": \"user@example.com\", \"password\": \"mypassword\"}",
  "hostname": "example.com",
  "port": 8443
}
```

## Technical Details

### Actions

#### Isolate Machine

This action is used to isolate a machine associated with the root cause of a Malop, or to remediate a process not involved in a malop.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|actions_by_machine|object|None|False|Actions by machine|None|{"126811122.2298225282553311122": [{"targetId": "531122333.-3391199199911692223","actionType": "KILL_PROCESS"}]}|
|initiator_user_name|string|None|False|Initiator user name|None|user@example.com|
|malop_id|string|None|False|Malop ID to isolate a machine or empty to remediate process not involved in a malop|None|22.2787422324806222966|
|pylum_ids|[]string|None|False|The unique sensor ID the Cybereason platform uses for the machines to isolate|None|["PYLUMCLIENT_INTEGRATION_GDDA11-11_2222170222FC"]|

Example input:

```
{
  "actions_by_machine": "{\"126811122.2298225282553311122\": [{\"targetId\": \"531122333.-3391199199911692223\",\"actionType\": \"KILL_PROCESS\"}]}",
  "initiator_user_name": "user@example.com",
  "malop_id": "22.2787422324806222966",
  "pylum_ids": [
    "PYLUMCLIENT_INTEGRATION_GDDA11-11_2222170222FC"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|object|True|Malop response|

Example output:

```
{
  "response": {
    "PYLUMCLIENT_INTEGRATION_GDDA11-11_2222170222FC": "Succeeded"
  }
}
```

#### Search for Files

This action is used to find files on any machine in your environment with a Cybereason sensor installed.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_filter|string|None|True|A fileFilters object where you filter by machine name, folder, file creation or modification time or file size with operator Equals, NotEquals, ContainsIgnoreCase, NotContainsIgnoreCase and others|None|fileName Equals: ["sample.py"]|
|server_filter|string|None|False|A Sensor filters object where you filter sensors by different criteria such as operating system|None|machineName: ["rapid7-windows"]|

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

* 1.1.0 - Add new action Isolate Machine
* 1.0.0 - Initial plugin

# Links

## References

* [Cybereason Plugin](https://www.cybereason.com/)
* [Cybereason Plugin API](https://nest.cybereason.com/user/login?destination=/documentation/api-documentation/all-versions/cybereason-api-guide)
