# Description

[SentinelOne](https://www.sentinelone.com/) is a next-gen cybersecurity company focused on protecting the enterprise through the endpoint. The SentinelOne plugin allows you to manage and mitigate all your security operations through SentinelOne.

This plugin utilizes the SentinelOne API, the documentation is located in the SentinelOne console.

# Key Features

* Quarantine endpoints
* Execute scans
* Blacklist hashes
* Trigger workflows on security alerts
* Manage threats
* Fetch Threats File

# Requirements

* Sentinel one API administrative credentials

# Supported Product Versions

* 2.0.0
* 2.1.0

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username": "user@example.com", "password": "mypassword"}|
|url|string|None|True|SentinelOne Console URL|None|https://example.sentinelone.com|

Example input:

```
{
  "credentials": {
    "username": "user@example.com",
    "password": "mypassword"
  },
  "url": "https://example.sentinelone.com"
}
```

## Technical Details

### Actions

#### Update Incident Status

This action is used to update incident status.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incident_ids|[]string|None|True|A list of alert or threat IDs to update the incident status on|None|["1118189762920424575", "1118189762920424576"]|
|incident_status|string|None|True|Incident status|['unresolved', 'in progress', 'resolved']|resolved|
|type|string|None|True|Type of incidents|['threats', 'alerts']|threats|

Example input:

```
{
  "incident_ids": [
    "1118189762920424575",
    "1118189762920424576"
  ],
  "incident_status": "resolved",
  "type": "threats"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 2
}
```

#### Update Analyst Verdict

This action is used to update analyst verdict.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analyst_verdict|string|None|True|Analyst verdict|['true positive', 'suspicious', 'false positive', 'undefined']|true positive|
|incident_ids|[]string|None|True|A list of alert or threat IDs on which we may update the analyst verdict|None|["1118189762920424575", "1118189762920424576"]|
|type|string|None|True|Type of incidents|['threats', 'alerts']|threats|

Example input:

```
{
  "analyst_verdict": "true positive",
  "incident_ids": [
    "1118189762920424575",
    "1118189762920424576"
  ],
  "type": "threats"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 2
}
```

#### Get Events by Type

This action is used to get Deep Visibility results from the query that matches the given event type.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event_type|string|None|True|Event type for Autocomplete|['Process Exit', 'Process Modification', 'Process Creation', 'Duplicate Process Handle', 'Duplicate Thread Handle', 'Open Remote Process Handle', 'Remote Thread Creation', 'Remote Process Termination', 'Command Script', 'IP Connect', 'IP Listen', 'File Modification', 'File Creation', 'File Scan', 'File Deletion', 'File Rename', 'Pre Execution Detection', 'Login', 'Logout', 'GET', 'OPTIONS', 'POST', 'PUT', 'DELETE', 'CONNECT', 'HEAD', 'DNS Resolved', 'DNS Unresolved', 'Task Register', 'Task Update', 'Task Start', 'Task Trigger', 'Task Delete', 'Registry Key Create', 'Registry Key Rename', 'Registry Key Delete', 'Registry Key Export', 'Registry Key Security Changed', 'Registry Key Import', 'Registry Value Modified', 'Registry Value Create', 'Registry Value Delete', 'Behavioral Indicators', 'Module Load']|Registry Key Create|
|limit|integer|None|False|Limit number of returned items (1-1000), if no limit is provided returns all the results up to 20,000|None|10|
|query_id|string|None|True|QueryId obtained when creating a query under Create Query|None|qd94e330ac025d525b5948bdf897b955e|
|sub_query|string|None|False|Sub query to run on the data that was already pulled|None|AgentName IS NOT EMPTY|

Example input:

```
{
  "event_type": "Registry Key Create",
  "limit": 10,
  "query_id": "qd94e330ac025d525b5948bdf897b955e",
  "sub_query": "AgentName IS NOT EMPTY"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|get_events_response|False|SentinelOne API call response data|

Example output:

```
{
  "response": {
    "data": [
      {
        "agentDomain": "WORKGROUP",
        "agentGroupId": "123123456712356789",
        "agentId": "123123456712356789",
        "agentInfected": false,
        "agentIp": "192.168.50.1",
        "agentIsActive": true,
        "agentIsDecommissioned": false,
        "agentMachineType": "server",
        "agentName": "example-agent",
        "agentNetworkStatus": "connected",
        "agentOs": "windows",
        "agentTimestamp": "2021-03-22T12:20:34.441Z",
        "agentUuid": "28db47168fa54f89aeed99769ac8d4dc",
        "agentVersion": "4.1.4.82",
        "attributes": [
          {
            "display": "Endpoint Name",
            "display_all_events": "Endpoint Name",
            "display_attribute": true,
            "enriched_in_mgmt": false,
            "field_id": "endpointName",
            "in_all_events": false,
            "queryable": true,
            "section": "Endpoint Details",
            "value": "example-agent"
          },
          {
            "display": "Endpoint OS",
            "display_all_events": "Endpoint OS",
            "display_attribute": true,
            "enriched_in_mgmt": false,
            "field_id": "endpointOs",
            "in_all_events": false,
            "queryable": true,
            "section": "Endpoint Details",
            "value": "windows"
          },
          {
            "display": "Agent UUID",
            "display_all_events": "Agent UUID",
            "display_attribute": false,
            "enriched_in_mgmt": false,
            "field_id": "agentUuid",
            "in_all_events": false,
            "queryable": true,
            "section": "Endpoint Details",
            "value": "28db47168fa54f89aeed99769ac8d4dc"
          }
        ],
        "childProcCount": "0",
        "createdAt": "2021-03-22T12:20:34.441000Z",
        "crossProcCount": "0",
        "crossProcDupRemoteProcHandleCount": "0",
        "crossProcDupThreadHandleCount": "0",
        "crossProcOpenProcCount": "0",
        "crossProcOutOfStorylineCount": "0",
        "crossProcThreadCreateCount": "0",
        "dnsCount": "0",
        "endpointMachineType": "server",
        "endpointName": "example-agent",
        "endpointOs": "windows",
        "eventTime": "2021-03-22T12:20:34.441Z",
        "eventType": "Task Start",
        "id": "538501898938548224",
        "indicatorBootConfigurationUpdateCount": "0",
        "indicatorEvasionCount": "0",
        "indicatorExploitationCount": "0",
        "indicatorGeneralCount": "0",
        "indicatorInfostealerCount": "0",
        "indicatorInjectionCount": "0",
        "indicatorPersistenceCount": "0",
        "indicatorPostExploitationCount": "0",
        "indicatorRansomwareCount": "0",
        "indicatorReconnaissanceCount": "0",
        "metaEventName": "SCHEDTASKSTART",
        "moduleCount": "0",
        "netConnCount": "0",
        "netConnInCount": "0",
        "netConnOutCount": "0",
        "objectType": "scheduled_task",
        "parentPid": "1576",
        "parentProcessName": "GoogleUpdateSetup.exe",
        "parentProcessStartTime": "2021-02-05T04:15:29.040Z",
        "parentProcessUniqueKey": "0B457A0EEDCCDE79",
        "pid": "2124",
        "processCmd": "\"C:\\Program Files (x86)\\Google\\Temp\\GUMFD36.tmp\\GoogleUpdate.exe\" /update /sessionid \"{A93A4584-B89A-4960-BF6B-7D22327D555B}\"",
        "processDisplayName": "Google Installer",
        "processGroupId": "010F0690CE863720",
        "processImagePath": "C:\\Program Files (x86)\\Google\\Temp\\GUMFD36.tmp\\GoogleUpdate.exe",
        "processIntegrityLevel": "SYSTEM",
        "processIsRedirectedCommandProcessor": "False",
        "processIsWow64": "True",
        "processName": "GoogleUpdate.exe",
        "processRoot": "False",
        "processSessionId": "0",
        "processStartTime": "2021-02-05T04:15:30.704Z",
        "processSubSystem": "SYS_WIN32",
        "processUniqueKey": "0B457A0EEDCCDE79",
        "registryChangeCount": "0",
        "relatedToThreat": "False",
        "siteId": "521580416395045459",
        "siteName": "Rapid7",
        "srcProcCmdLine": "\"C:\\Program Files (x86)\\Google\\Temp\\GUMFD36.tmp\\GoogleUpdate.exe\" /update /sessionid \"{A93A4584-B89A-4960-BF6B-7D22327D555B}\"",
        "srcProcDisplayName": "Google Installer",
        "srcProcImagePath": "C:\\Program Files (x86)\\Google\\Temp\\GUMFD36.tmp\\GoogleUpdate.exe",
        "srcProcIntegrityLevel": "SYSTEM",
        "srcProcIsNative64Bit": "True",
        "srcProcIsRedirectCmdProcessor": "False",
        "srcProcIsStorylineRoot": "False",
        "srcProcName": "GoogleUpdate.exe",
        "srcProcParentImagePath": "C:\\Program Files (x86)\\Google\\Update\\Install\\{D0BA3C2C-8787-4281-9646-FB4B6EE87E66}\\GoogleUpdateSetup.exe",
        "srcProcParentName": "GoogleUpdateSetup.exe",
        "srcProcParentPid": "1576",
        "srcProcParentProcUid": "022700598B3061C5",
        "srcProcParentStartTime": "2021-02-05T04:15:29.040Z",
        "srcProcParentUid": "022700598B3061C5",
        "srcProcPid": "2124",
        "srcProcRelatedToThreat": "False",
        "srcProcSessionId": "0",
        "srcProcStartTime": "2021-02-05T04:15:30.704Z",
        "srcProcStorylineId": "010F0690CE863720",
        "srcProcSubsystem": "SYS_WIN32",
        "srcProcTid": "2116",
        "srcProcUid": "0B457A0EEDCCDE79",
        "srcProcUser": "NT AUTHORITY\\SYSTEM",
        "storyline": "010F0690CE863720",
        "taskName": "\\GoogleUpdateTaskMachineUA",
        "taskPath": "C:\\Program Files (x86)\\Google\\Update\\GoogleUpdate.exe",
        "tgtFileCreationCount": "0",
        "tgtFileDeletionCount": "0",
        "tgtFileModificationCount": "0",
        "tid": "2116",
        "trueContext": "010F0690CE863720",
        "user": "NT AUTHORITY\\SYSTEM"
      }
    ],
    "pagination": {
      "nextCursor": "eyJpZF9jb2x1bW4iOiAiaWQiLCAiaWRfdmFsdWUiOiAiNTM4NTAxODk4OTM4NTQ4MjI0IiwgInNvcnRfYnlfY29sdW1uIjogImFnZW50VGltZXN0YW1wIiwgInNvcnRfYnlfdmFsdWUiOiAiMjAyMS0wMy0yMlQxMjoyMDozNC40NDFaIiwgInNvcnRfb3JkZXIiOiAiZGVzYyJ9",
      "totalItems": 1000
    }
  }
}
```

#### Get Events

This action is used to get all Deep Visibility events from a queryId.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|limit|integer|None|False|Limit number of returned items (1-1000), if no limit is provided returns all the results up to 20,000|None|10|
|query_id|string|None|True|QueryId obtained when creating a query under Create Query|None|qd94e330ac025d525b5948bdf897b955e|
|sub_query|string|None|False|Sub query to run on the data that was already pulled|None|AgentName IS NOT EMPTY|

Example input:

```
{
  "limit": 10,
  "query_id": "qd94e330ac025d525b5948bdf897b955e",
  "sub_query": "AgentName IS NOT EMPTY"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|get_events_response|False|SentinelOne API call response data|

Example output:

```
{
  "response": {
    "data": [
      {
        "agentDomain": "WORKGROUP",
        "agentGroupId": "123123456712356789",
        "agentId": "123123456712356789",
        "agentInfected": false,
        "agentIp": "192.168.50.1",
        "agentIsActive": true,
        "agentIsDecommissioned": false,
        "agentMachineType": "server",
        "agentName": "example-agent",
        "agentNetworkStatus": "connected",
        "agentOs": "windows",
        "agentTimestamp": "2021-03-22T12:20:34.441Z",
        "agentUuid": "28db47168fa54f89aeed99769ac8d4dc",
        "agentVersion": "4.1.4.82",
        "attributes": [
          {
            "display": "Endpoint Name",
            "display_all_events": "Endpoint Name",
            "display_attribute": true,
            "enriched_in_mgmt": false,
            "field_id": "endpointName",
            "in_all_events": false,
            "queryable": true,
            "section": "Endpoint Details",
            "value": "example-agent"
          },
          {
            "display": "Endpoint OS",
            "display_all_events": "Endpoint OS",
            "display_attribute": true,
            "enriched_in_mgmt": false,
            "field_id": "endpointOs",
            "in_all_events": false,
            "queryable": true,
            "section": "Endpoint Details",
            "value": "windows"
          },
          {
            "display": "Agent UUID",
            "display_all_events": "Agent UUID",
            "display_attribute": false,
            "enriched_in_mgmt": false,
            "field_id": "agentUuid",
            "in_all_events": false,
            "queryable": true,
            "section": "Endpoint Details",
            "value": "28db47168fa54f89aeed99769ac8d4dc"
          }
        ],
        "childProcCount": "0",
        "createdAt": "2021-03-22T12:20:34.441000Z",
        "crossProcCount": "0",
        "crossProcDupRemoteProcHandleCount": "0",
        "crossProcDupThreadHandleCount": "0",
        "crossProcOpenProcCount": "0",
        "crossProcOutOfStorylineCount": "0",
        "crossProcThreadCreateCount": "0",
        "dnsCount": "0",
        "endpointMachineType": "server",
        "endpointName": "example-agent",
        "endpointOs": "windows",
        "eventTime": "2021-03-22T12:20:34.441Z",
        "eventType": "Task Start",
        "id": "538501898938548224",
        "indicatorBootConfigurationUpdateCount": "0",
        "indicatorEvasionCount": "0",
        "indicatorExploitationCount": "0",
        "indicatorGeneralCount": "0",
        "indicatorInfostealerCount": "0",
        "indicatorInjectionCount": "0",
        "indicatorPersistenceCount": "0",
        "indicatorPostExploitationCount": "0",
        "indicatorRansomwareCount": "0",
        "indicatorReconnaissanceCount": "0",
        "metaEventName": "SCHEDTASKSTART",
        "moduleCount": "0",
        "netConnCount": "0",
        "netConnInCount": "0",
        "netConnOutCount": "0",
        "objectType": "scheduled_task",
        "parentPid": "1576",
        "parentProcessName": "GoogleUpdateSetup.exe",
        "parentProcessStartTime": "2021-02-05T04:15:29.040Z",
        "parentProcessUniqueKey": "0B457A0EEDCCDE79",
        "pid": "2124",
        "processCmd": "\"C:\\Program Files (x86)\\Google\\Temp\\GUMFD36.tmp\\GoogleUpdate.exe\" /update /sessionid \"{A93A4584-B89A-4960-BF6B-7D22327D555B}\"",
        "processDisplayName": "Google Installer",
        "processGroupId": "010F0690CE863720",
        "processImagePath": "C:\\Program Files (x86)\\Google\\Temp\\GUMFD36.tmp\\GoogleUpdate.exe",
        "processIntegrityLevel": "SYSTEM",
        "processIsRedirectedCommandProcessor": "False",
        "processIsWow64": "True",
        "processName": "GoogleUpdate.exe",
        "processRoot": "False",
        "processSessionId": "0",
        "processStartTime": "2021-02-05T04:15:30.704Z",
        "processSubSystem": "SYS_WIN32",
        "processUniqueKey": "0B457A0EEDCCDE79",
        "registryChangeCount": "0",
        "relatedToThreat": "False",
        "siteId": "521580416395045459",
        "siteName": "Rapid7",
        "srcProcCmdLine": "\"C:\\Program Files (x86)\\Google\\Temp\\GUMFD36.tmp\\GoogleUpdate.exe\" /update /sessionid \"{A93A4584-B89A-4960-BF6B-7D22327D555B}\"",
        "srcProcDisplayName": "Google Installer",
        "srcProcImagePath": "C:\\Program Files (x86)\\Google\\Temp\\GUMFD36.tmp\\GoogleUpdate.exe",
        "srcProcIntegrityLevel": "SYSTEM",
        "srcProcIsNative64Bit": "True",
        "srcProcIsRedirectCmdProcessor": "False",
        "srcProcIsStorylineRoot": "False",
        "srcProcName": "GoogleUpdate.exe",
        "srcProcParentImagePath": "C:\\Program Files (x86)\\Google\\Update\\Install\\{D0BA3C2C-8787-4281-9646-FB4B6EE87E66}\\GoogleUpdateSetup.exe",
        "srcProcParentName": "GoogleUpdateSetup.exe",
        "srcProcParentPid": "1576",
        "srcProcParentProcUid": "022700598B3061C5",
        "srcProcParentStartTime": "2021-02-05T04:15:29.040Z",
        "srcProcParentUid": "022700598B3061C5",
        "srcProcPid": "2124",
        "srcProcRelatedToThreat": "False",
        "srcProcSessionId": "0",
        "srcProcStartTime": "2021-02-05T04:15:30.704Z",
        "srcProcStorylineId": "010F0690CE863720",
        "srcProcSubsystem": "SYS_WIN32",
        "srcProcTid": "2116",
        "srcProcUid": "0B457A0EEDCCDE79",
        "srcProcUser": "NT AUTHORITY\\SYSTEM",
        "storyline": "010F0690CE863720",
        "taskName": "\\GoogleUpdateTaskMachineUA",
        "taskPath": "C:\\Program Files (x86)\\Google\\Update\\GoogleUpdate.exe",
        "tgtFileCreationCount": "0",
        "tgtFileDeletionCount": "0",
        "tgtFileModificationCount": "0",
        "tid": "2116",
        "trueContext": "010F0690CE863720",
        "user": "NT AUTHORITY\\SYSTEM"
      }
    ],
    "pagination": {
      "nextCursor": "eyJpZF9jb2x1bW4iOiAiaWQiLCAiaWRfdmFsdWUiOiAiNTM4NTAxODk4OTM4NTQ4MjI0IiwgInNvcnRfYnlfY29sdW1uIjogImFnZW50VGltZXN0YW1wIiwgInNvcnRfYnlfdmFsdWUiOiAiMjAyMS0wMy0yMlQxMjoyMDozNC40NDFaIiwgInNvcnRfb3JkZXIiOiAiZGVzYyJ9",
      "totalItems": 1000
    }
  }
}
```

#### Cancel Running Query

This action is used to stop a Deep Visibility Query by queryId.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query_id|string|None|True|QueryId obtained when creating a query under Create Query|None|qd94e330ac025d525b5948bdf897b955e|

Example input:

```
{
  "query_id": "qd94e330ac025d525b5948bdf897b955e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|cancel_query_response|False|SentinelOne API call response data|

Example output:

```
{
  "response": {
    "success": true
  }
}
```

#### Get Query Status

This action is used to get that status of a Deep Visibility Query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query_id|string|None|True|QueryId obtained when creating a query under Create Query|None|qd94e330ac025d525b5948bdf897b955e|

Example input:

```
{
  "query_id": "qd94e330ac025d525b5948bdf897b955e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|get_query_status_response|False|SentinelOne API call response data|

Example output:

```
{
  "response": {
    "data": {
      "progressStatus": 50,
      "responseState": "RUNNING"
    }
  }
}
```

#### Create Query

This action is used to start a Deep Visibility Query and get the queryId. You can use the queryId for other commands, such as Get Events and Get Query Status.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_ids|[]string|None|False|List of account IDs to filter by|None|["225494730938491234", "225494730938491235"]|
|from_date|string|None|True|From date|None|2021-03-01 04:49:26.257525|
|to_date|string|None|True|Events created before or at this timestamp|None|2021-03-20 04:49:26.257525|
|group_ids|[]string|None|False|List of group IDs to filter by|None|["225494730938491234", "225494730938491235"]|
|is_verbose|boolean|None|False|Show all fields or just priority fields|None|True|
|limit|integer|None|False|Limit number of returned items (1-20000)|None|10|
|query|string|None|True|Events matching the query search term will be returned|None|AgentName IS NOT EMPTY|
|query_type|[]string|None|False|Query search type|None|["events"]|
|site_ids|[]string|None|False|List of site IDs to filter by|None|["225494730938491234", "225494730938491235"]|
|tenant|boolean|None|False|Indicates a Global (tenant) scope request|None|True|

Example input:

```
{
  "account_ids": [
    "225494730938491234",
    "225494730938491235"
  ],
  "from_date": "2021-03-01T04:49:26.257525Z",
  "group_ids": [
    "225494730938491234",
    "225494730938491235"
  ],
  "is_verbose": true,
  "limit": 10,
  "query": "AgentName IS NOT EMPTY",
  "query_type": [
    "events"
  ],
  "site_ids": [
    "225494730938491234",
    "225494730938491235"
  ],
  "tenant": true,
  "to_date": "2021-03-20T04:49:26.257525Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|create_query_response|False|SentinelOne API call response data|

Example output:

```
{
  "response": {
    "data": {
      "queryId": "qef4d0d2de7141756ff16959180015e75"
    }
  }
}
```

#### Enable Agent

This action is used to enable agents that match the filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|False|Agent to perform disable action on. Accepts IP address, MAC address, hostname, UUID or agent ID. Leave empty to perform action on all applicable Agents|None|hostname123|
|filter|object|None|False|Filter to apply action on specified agents. Leave empty to perform action on all applicable Agents|None|{ "updatedAt__gt": "2019-02-27T04:49:26.257525Z" }|
|reboot|boolean|None|True|Set true to reboot the endpoint, false to skip rebooting|None|True|

Example input:

```
{
  "agent": "hostname123",
  "filter": {
    "updatedAt__gt": "2019-02-27T04:49:26.257525Z"
  },
  "reboot": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|True|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

#### Disable Agent

This action is used to disable agents that match the filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|False|Agent to perform disable action on. Accepts IP address, MAC address, hostname, UUID or agent ID. Leave empty to perform action on all applicable Agents|None|hostname123|
|expiration_time|string|None|False|Agents will be re-enabled after this timestamp|None|2020-02-27 04:49:26.257525|
|expiration_timezone|string|Central Standard Time (North America) [CST]|False|Timezone for the expiration timestamp. Set with expiration time|['Australian Central Daylight Saving Time [ACDT]', 'Australian Central Standard Time [ACST]', 'Acre Time [ACT]', 'Atlantic Daylight Time [ADT]', 'Australian Eastern Daylight Saving Time [AEDT]', 'Australian Eastern Standard Time [AEST]', 'Australian Eastern Time [AET]', 'Afghanistan Time [AFT]', 'Alaska Daylight Time [AKDT]', 'Alaska Standard Time [AKST]', 'Alma-Ata Time [ALMT]', 'Amazon Summer Time (Brazil) [AMST]', 'Amazon Time (Brazil) [AMT]', 'Armenia Time [AMT]', 'Anadyr Time [ANAT]', 'Aqtobe Time [AQTT]', 'Argentina Time [ART]', 'Arabia Standard Time [AST]', 'Atlantic Standard Time [AST]', 'Australian Western Standard Time [AWST]', 'Azores Summer Time [AZOST]', 'Azores Standard Time [AZOT]', 'Azerbaijan Time [AZT]', 'Brunei Time [BNT]', 'British Indian Ocean Time [BIOT]', 'Baker Island Time [BIT]', 'Bolivia Time [BOT]', 'Brasilia Summer Time [BRST]', 'Brasilia Time [BRT]', 'Bangladesh Standard Time [BST]', 'Bougainville Standard Time [BST]', 'Bhutan Time [BTT]', 'Central Africa Time [CAT]', 'Cocos Islands Time [CCT]', 'Central Daylight Time (North America) [CDT]', 'Cuba Daylight Time [CDT]', 'Central European Summer Time [CEST]', 'Central European Time [CET]', 'Chatham Daylight Time [CHADT]', 'Chatham Standard Time [CHAST]', 'Choibalsan Standard Time [CHOT]', 'Choibalsan Summer Time [CHOST]', 'Chamorro Standard Time [CHST]', 'Chuuk Time [CHUT]', 'Clipperton Island Standard Time [CIST]', 'Central Indonesia Time [WITA]', 'Cook Island Time [CKT]', 'Chile Summer Time [CLST]', 'Chile Standard Time [CLT]', 'Colombia Summer Time [COST]', 'Colombia Time [COT]', 'Central Standard Time (North America) [CST]', 'China Standard Time [CST]', 'Cuba Standard Time [CST]', 'Central Time [CT]', 'Cape Verde Time [CVT]', 'Christmas Island Time [CXT]', 'Davis Time [DAVT]', 'Dumont dUrville Time [DDUT]', 'AIX-specific equivalent of Central European Time [DFT]', 'Easter Island Summer Time [EASST]', 'Easter Island Standard Time [EAST]', 'East Africa Time [EAT]', 'Ecuador Time [ECT]', 'Eastern Daylight Time (North America) [EDT]', 'Eastern European Summer Time [EEST]', 'Eastern European Time [EET]', 'Eastern Greenland Summer Time [EGST]', 'Eastern Greenland Time [EGT]', 'Eastern Indonesian Time [WIT]', 'Eastern Standard Time (North America) [EST]', 'Further-eastern European Time [FET]', 'Fiji Time [FJT]', 'Falkland Islands Summer Time [FKST]', 'Falkland Islands Time [FKT]', 'Fernando de Noronha Time [FNT]', 'Galapagos Time [GALT]', 'Gambier Islands Time [GAMT]', 'Georgia Standard Time [GET]', 'French Guiana Time [GFT]', 'Gilbert Island Time [GILT]', 'Gambier Island Time [GIT]', 'Greenwich Mean Time [GMT]', 'South Georgia and the South Sandwich Islands Time [GST]', 'Gulf Standard Time [GST]', 'Guyana Time [GYT]', 'Hawaii-Aleutian Daylight Time [HDT]', 'Heure Avancee Europe Centrale French-language name for CEST [HAEC]', 'Hawaii-Aleutian Standard Time [HST]', 'Hong Kong Time [HKT]', 'Heard and McDonald Islands Time [HMT]', 'Hovd Time [HOVT]', 'Indochina Time [ICT]', 'International Day Line West time zone [IDLW]', 'Israel Daylight Time [IDT]', 'Indian Ocean Time [IOT]', 'Iran Daylight Time [IRDT]', 'Irkutsk Time [IRKT]', 'Iran Standard Time [IRST]', 'Indian Standard Time [IST]', 'Irish Standard Time [IST]', 'Israel Standard Time [IST]', 'Japan Standard Time [JST]', 'Kaliningrad Time [KALT]', 'Kyrgyzstan Time [KGT]', 'Kosrae Time [KOST]', 'Krasnoyarsk Time [KRAT]', 'Korea Standard Time [KST]', 'Lord Howe Standard Time [LHST]', 'Lord Howe Summer Time [LHST]', 'Line Islands Time [LINT]', 'Magadan Time [MAGT]', 'Marquesas Islands Time [MART]', 'Mawson Station Time [MAWT]', 'Mountain Daylight Time (North America) [MDT]', 'Middle European Time [MET]', 'Middle European Summer Time [MEST]', 'Marshall Islands Time [MHT]', 'Macquarie Island Station Time [MIST]', 'Marquesas Islands Time [MIT]', 'Myanmar Standard Time [MMT]', 'Moscow Time [MSK]', 'Malaysia Standard Time [MST]', 'Mountain Standard Time (North America) [MST]', 'Mauritius Time [MUT]', 'Maldives Time [MVT]', 'Malaysia Time [MYT]', 'New Caledonia Time [NCT]', 'Newfoundland Daylight Time [NDT]', 'Norfolk Island Time [NFT]', 'Novosibirsk Time [NOVT]', 'Nepal Time [NPT]', 'Newfoundland Standard Time [NST]', 'Newfoundland Time [NT]', 'Niue Time [NUT]', 'New Zealand Daylight Time [NZDT]', 'New Zealand Standard Time [NZST]', 'Omsk Time [OMST]', 'Oral Time [ORAT]', 'Pacific Daylight Time (North America) [PDT]', 'Peru Time [PET]', 'Kamchatka Time [PETT]', 'Papua New Guinea Time [PGT]', 'Phoenix Island Time [PHOT]', 'Philippine Time [PHT]', 'Pakistan Standard Time [PKT]', 'Saint Pierre and Miquelon Daylight Time [PMDT]', 'Saint Pierre and Miquelon Standard Time [PMST]', 'Pohnpei Standard Time [PONT]', 'Pacific Standard Time (North America) [PST]', 'Philippine Standard Time [PST]', 'Palau Time [PWT]', 'Paraguay Summer Time [PYST]', 'Paraguay Time [PYT]', 'Reunion Time [RET]', 'Rothera Research Station Time [ROTT]', 'Sakhalin Island Time [SAKT]', 'Samara Time [SAMT]', 'South African Standard Time [SAST]', 'Solomon Islands Time [SBT]', 'Seychelles Time [SCT]', 'Samoa Daylight Time [SDT]', 'Singapore Time [SGT]', 'Sri Lanka Standard Time [SLST]', 'Srednekolymsk Time [SRET]', 'Suriname Time [SRT]', 'Samoa Standard Time [SST]', 'Singapore Standard Time [SST]', 'Showa Station Time [SYOT]', 'Tahiti Time [TAHT]', 'Thailand Standard Time [THA]', 'French Southern and Antarctic Time [TFT]', 'Tajikistan Time [TJT]', 'Tokelau Time [TKT]', 'Timor Leste Time [TLT]', 'Turkmenistan Time [TMT]', 'Turkey Time [TRT]', 'Tonga Time [TOT]', 'Tuvalu Time [TVT]', 'Ulaanbaatar Summer Time [ULAST]', 'Ulaanbaatar Standard Time [ULAT]', 'Coordinated Universal Time [UTC]', 'Uruguay Summer Time [UYST]', 'Uruguay Standard Time [UYT]', 'Uzbekistan Time [UZT]', 'Venezuelan Standard Time [VET]', 'Vladivostok Time [VLAT]', 'Volgograd Time [VOLT]', 'Vostok Station Time [VOST]', 'Vanuatu Time [VUT]', 'Wake Island Time [WAKT]', 'West Africa Summer Time [WAST]', 'West Africa Time [WAT]', 'Western European Summer Time [WEST]', 'Western European Time [WET]', 'Western Indonesian Time [WIB]', 'West Greenland Summer Time [WGST]', 'West Greenland Time [WGT]', 'Western Standard Time [WST]', 'Yakutsk Time [YAKT]', 'Yekaterinburg Time [YEKT]']|Central Standard Time (North America) [CST]|
|filter|object|None|False|Filter to apply action on specified agents. Leave empty to perform action on all applicable Agents|None|{ "updatedAt__gt": "2019-02-27T04:49:26.257525Z" }|
|reboot|boolean|None|True|Set true to reboot the endpoint, false to skip rebooting|None|True|
|expiration_time|string|None|False|Agents will be re-enabled after this timestamp|None|2020-02-27 04:49:26.257525+00:00|

Example input:

```
{
  "agent": "hostname123",
  "expiration_time": "2020-02-27T04:49:26.257525Z",
  "expiration_timezone": "Central Standard Time (North America) [CST]",
  "filter": {
    "updatedAt__gt": "2019-02-27T04:49:26.257525Z"
  },
  "reboot": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|True|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

#### Run Agent Action

This action is used to perform actions relating to your SentinelOne agents. This will help manage your assets connected to your SentinelOne console. Documentation for these actions can be found at https://yoururl.sentinelone.net/api-doc/api-details?category=agent-actions.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|Agent action to run|['abort-scan', 'connect', 'decommission', 'disconnect', 'fetch-logs', 'initiate-scan', 'restart-machine', 'shutdown', 'uninstall']|connect|
|filter|object|{}|True|Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents. Note - decommission, disconnect, restart-machine, shutdown and uninstall actions require that one of the following filter arguments be supplied - ids, groupIds, or filterId|None|{"ids": ["1000000000000000000"]}|

Example input:

```
{
  "action": "connect",
  "filter": {
    "ids": [
      "1000000000000000000"
    ]
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

```
{
  "affected": 0
}
```

#### Fetch Threats File

This action is used to fetch a file associated with the threat that matches the filter. Your user role must have permissions to Fetch Threat File - Admin, IR Team, SOC.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Threat ID|None|939039647215561624|
|password|password|None|True|File encryption password, min. length 10 characters and cannot contain whitespace|None|Rapid7 Insightconnect|

Example input:

```
{
  "id": "939039647215561624",
  "password": "Rapid7 Insightconnect"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|file|True|Base64 encoded threat file|

Example output:

```
{
  "file": {
    "filename": "report.txt",
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
  }
}
```

#### Get Activities

This action is used to get a list of activities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_ids|[]string|None|False|List of Account IDs to filter by|None|["400000000000000000"]|
|activity_types|[]string|None|False|Return only these activity codes|None|["22", "23"]|
|agent_ids|[]string|None|False|Return activities related to specified agent ids|None|["9000000000000000"]|
|count_only|boolean|None|False|If true, only total number of items will be returned, without any of the actual objects|None|True|
|created_at_between|string|None|False|Return activities created within this range (inclusive), example 1514978764288-1514978999999|None|1514978764288-1514978999999|
|created_at_gt|string|None|False|Return activities created after or at this date in ISO-8601, example 2020-12-18T18:49:26.257525Z|None|2020-12-18T18:49:26.257525Z|
|created_at_gte|string|None|False|Return activities created after or at this date in ISO-8601, example 2020-12-18T18:49:26.257525Z|None|2020-12-20T18:49:26.257525Z|
|created_at_lt|string|None|False|Return activities created before this date in ISO-8601|None|2020-12-20T18:49:26.257525Z|
|created_at_lte|string|None|False|Return activities created before or at this date in ISO-8601, example 2020-12-18T18:49:26.257525Z|None|2020-12-20T18:49:26.257525Z|
|group_ids|[]string|None|False|List of Group IDs|None|["500000000000000000"]|
|ids|[]string|None|False|List of Activity IDs|None|["800000000000000008"]|
|include_hidden|boolean|None|False|Include internal activities hidden from display|None|True|
|limit|integer|10|False|Limit number of returned items (1-1000)|None|10|
|site_ids|[]string|None|False|List of Site IDs to filter by|None|["5000000000000001"]|
|skip|integer|None|False|Skip first number of items (0-1000). Will return the number entries specified in the 'limit' input (default is 10)|None|1|
|skip_count|boolean|None|False|If true, total number of items will not be calculated, which speeds up execution time|None|True|
|sort_by|string|createdAt|False|The column to sort the results by|['id', 'activityType', 'createdAt']|createdAt|
|sort_order|string|asc|False|Sort direction|['asc', 'desc']|asc|
|threat_ids|[]string|None|False|Return only these activity codes|None|["1"]|
|user_emails|[]string|None|False|Email of the user who invoked the activity (If applicable)|None|["user@example.com"]|
|user_ids|[]string|None|False|The user who invoked the activity (If applicable)|None|["500000000000000003"]|

Example input:

```
{
  "account_ids": [
    "400000000000000000"
  ],
  "activity_types": [
    "22",
    "23"
  ],
  "agent_ids": [
    "9000000000000000"
  ],
  "count_only": true,
  "created_at_between": "1514978764288-1514978999999",
  "created_at_gt": "2020-12-18T18:49:26.257525Z",
  "created_at_gte": "2020-12-20T18:49:26.257525Z",
  "created_at_lt": "2020-12-20T18:49:26.257525Z",
  "created_at_lte": "2020-12-20T18:49:26.257525Z",
  "group_ids": [
    "500000000000000000"
  ],
  "ids": [
    "800000000000000008"
  ],
  "include_hidden": true,
  "limit": 10,
  "site_ids": [
    "5000000000000001"
  ],
  "skip": 1,
  "skip_count": true,
  "sort_by": "createdAt",
  "sort_order": "asc",
  "threat_ids": [
    "1"
  ],
  "user_emails": [
    "user@example.com"
  ],
  "user_ids": [
    "500000000000000003"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]activities_list|True|Result of activities list|

#### Get Activity Types

This action is used to get a list of activity types.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activity_types|[]activities_types|True|Result of activities types|

Example output:

```
{
  "activity_types": [
    {
      "id": 0,
      "descriptionTemplate": "string",
      "action": "string"
    }
  ]
}
```

#### Agents Reload

This action is used to reload an agent module (applies to Windows agents only).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents|None|{"ids": ["1000000000000000000"]}|
|module|string|None|True|Agent module to reload|['monitor', 'static', 'agent', 'log']|monitor|

Example input:

```
{
  "filter": {
    "ids": [
      "1000000000000000000"
    ]
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 0
}
```

#### Count Summary

This action is used to summary of agents by numbers.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_ids|[]string|None|False|List of Account IDs to filter by|None|["4000000000000000000"]|
|site_ids|[]string|None|False|List of Site IDs to filter by|None|["500000000000000000"]|

Example input:

```
{
  "account_ids": [
    "4000000000000000000"
  ],
  "site_ids": [
    "500000000000000000"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decommissioned|integer|False|Number of decommissioned agents|
|infected|integer|False|Number of agents with at least one active threat|
|online|integer|False|Number of online agents|
|out_of_date|integer|False|Number of agents running an older software version|
|total|integer|False|Number of installed active agents|
|up_to_date|integer|False|Number of agents with the most up-to-date software version|

Example output:

```
{
  "decommissioned": 4,
  "infected": 0,
  "out_of_date": 0,
  "online": 1,
  "total": 2,
  "up_to_date": 2
}
```

#### Agents Applications

This action is used to retrieve running applications for a specific agent.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ids|[]string|None|True|Agent ID list|None|["1000000000000000000"]|

Example input:

```
{
  "ids": [
    "1000000000000000000"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]agent_applications|True|List of installed applications|

#### Blacklist

This action is used to blacklist and unblacklist a SHA1 hash. The blacklist is attempted for Linux, Windows, and MacOS operating systems and for all sites that the user has permission to manage.
Note that when attempting to unblacklist a SHA1 hash by setting `blacklist_state` to `false`, the SentinelOne API will always return success even if the hash was not blacklisted to begin with.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|blacklist_state|boolean|True|True|True to create blacklist hash, false to unblacklist hash|None|True|
|description|string|Hash Blacklisted from InsightConnect|False|Description for why the hash is blacklisted|None|Hash Blacklisted from InsightConnect|
|hash|string|None|True|Create a blacklist item from a SHA1 hash|None|3395856ce81f2b7382dee72602f798b642f14140|

Example input:

```
{
  "blacklist_state": true,
  "description": "Hash Blacklisted from InsightConnect",
  "hash": "3395856ce81f2b7382dee72602f798b642f14140"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if blacklist item was created or deleted|

Example output:

```
{
  "success": true
}
```

#### Blacklist by Content Hash

This action is used to add hashed content to global blacklist. The input makes use of contentHash from the threat summary.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|Content hash to add to blacklist|None|3395856ce81f2b7382dee72602f798b642f14140|

Example input:

```
{
  "blacklist_state": true,
  "description": "Hash Blacklisted from InsightConnect",
  "hash": "3395856ce81f2b7382dee72602f798b642f14140"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "blacklist_data": {
    "affected": 127
  }
}
```

#### Create IOC Threat

This action is used to create a threat from an IOC event.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agentId|string|None|True|Agent ID for the slim threat|None|1000000000000000000|
|groupId|string|None|False|Group ID|None|1000000000000000001|
|hash|string|None|True|SHA1 hash|None|A94A8FE5CCB19BA61C4C0873D391E987982FBBD3|
|note|string|None|False|Note|None|Note|
|path|string|None|False|Path|None|path|

Example input:

```
{
  "agentId": "1000000000000000000",
  "groupId": "1000000000000000001",
  "hash": "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3",
  "note": "Note",
  "path": "path"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

#### Get Agent Details

This action is used to retrieve agent details.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, MAC address, hostname, UUID or agent ID|None|hostname123|
|case_sensitive|boolean|True|True|Looks up the specified Agent in a case-sensitive manner. Setting this to false may result in longer run times and unintended results|None|True|
|operational_state|string|Any|False|Agent operational state|['Any', 'na', 'fully_disabled', 'partially_disabled', 'disabled_error']|na|

Example input:

```
{
  "agent": "hostname123",
  "case_sensitive": true,
  "operational_state": "na"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent_data|False|Detailed information about agent found|

Example output:

```
{
  "agent": {
    "accountId": "433241117337583618",
    "accountName": "SentinelOne",
    "activeDirectory": {
      "computerDistinguishedName": "None",
      "computerMemberOf": [],
      "lastUserDistinguishedName": "None",
      "lastUserMemberOf": []
    },
    "activeThreats": 0,
    "agentVersion": "4.1.4.82",
    "allowRemoteShell": false,
    "appsVulnerabilityStatus": "up_to_date",
    "cloudProviders": {},
    "computerName": "so-agent-win12",
    "consoleMigrationStatus": "N/A",
    "coreCount": 1,
    "cpuCount": 1,
    "cpuId": "Intel(R) Xeon(R) CPU E5-2690 v2 @ 3.00GHz",
    "createdAt": "2020-05-28T14:53:03.014660Z",
    "domain": "WORKGROUP",
    "encryptedApplications": false,
    "externalId": "",
    "externalIp": "198.51.100.100",
    "firewallEnabled": true,
    "groupId": "521580416411822676",
    "groupIp": "198.51.100.x",
    "groupName": "Default Group",
    "id": "901345720792880606",
    "inRemoteShellSession": false,
    "infected": false,
    "installerType": ".exe",
    "isActive": true,
    "isDecommissioned": false,
    "isPendingUninstall": false,
    "isUninstalled": false,
    "isUpToDate": true,
    "lastActiveDate": "2020-06-05T18:32:56.748620Z",
    "lastIpToMgmt": "10.4.24.55",
    "lastLoggedInUserName": "",
    "licenseKey": "",
    "locationEnabled": true,
    "locationType": "fallback",
    "locations": [
      {
        "id": "629380164464502476",
        "name": "Fallback",
        "scope": "global"
      }
    ],
    "machineType": "server",
    "mitigationMode": "protect",
    "mitigationModeSuspicious": "detect",
    "modelName": "VMware, Inc. - VMware Virtual Platform",
    "networkInterfaces": [
      {
        "id": "901345720801269215",
        "inet": [
          "198.51.100.100"
        ],
        "inet6": [
          "2001:db8:8:4::2"
        ],
        "name": "Ethernet",
        "physical": "00:50:56:94:17:08"
      }
    ],
    "networkQuarantineEnabled": false,
    "networkStatus": "disconnected",
    "operationalState": "na",
    "operationalStateExpiration": "None",
    "osArch": "64 bit",
    "osName": "Windows Server 2012 Standard",
    "osRevision": "9200",
    "osStartTime": "2020-05-28T14:59:36Z",
    "osType": "windows",
    "osUsername": "None",
    "rangerStatus": "NotApplicable",
    "rangerVersion": "None",
    "registeredAt": "2020-05-28T14:53:03.010853Z",
    "remoteProfilingState": "disabled",
    "remoteProfilingStateExpiration": "None",
    "scanAbortedAt": "None",
    "scanFinishedAt": "2020-05-28T22:24:59.420166Z",
    "scanStartedAt": "2020-05-28T21:12:58.216807Z",
    "scanStatus": "finished",
    "siteId": "521580416395045459",
    "siteName": "Rapid7",
    "threatRebootRequired": false,
    "totalMemory": 1023,
    "updatedAt": "2020-06-05T15:39:10.754112Z",
    "userActionsNeeded": [],
    "uuid": "28db47168fa54f89aeed99769ac8d4dc"
  }
}
```

#### Get Threat Summary

This action gets summary of all threats.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]threat_data|False|Data|
|errors|[]object|False|Errors|
|pagination|pagination|False|Pagination|

Example output:

```
{
  "data": [
    {
      "agentOsType": "windows",
      "automaticallyResolved": false,
      "cloudVerdict": "black",
      "id": "566535959618699500",
      "indicators": [],
      "engines": [
        "reputation"
      ],
      "fileContentHash": "3395856ce81f2b7382dee72602f798b642f14140",
      "fromCloud": false,
      "mitigationMode": "protect",
      "mitigationReport": {
        "network_quarantine": {},
        "quarantine": {
          "status": "success"
        },
        "remediate": {},
        "rollback": {},
        "unquarantine": {},
        "kill": {
          "status": "success"
        }
      },
      "rank": 7,
      "siteName": "Rapid7",
      "whiteningOptions": [
        "hash"
      ],
      "agentComputerName": "vagrant-pc",
      "collectionId": "433377870883088367",
      "createdAt": "2019-02-21T16:05:49.251201Z",
      "mitigationStatus": "active",
      "classificationSource": "Static",
      "resolved": true,
      "accountName": "SentinelOne",
      "fileVerificationType": "NotSigned",
      "siteId": "521580416395045459",
      "fileIsExecutable": false,
      "fromScan": false,
      "agentNetworkStatus": "disconnecting",
      "createdDate": "2019-02-21T16:05:49.175000Z",
      "accountId": "433241117337583618",
      "initiatedBy": "agentPolicy",
      "initiatedByDescription": "Agent Policy",
      "threatAgentVersion": "3.0.1.3",
      "username": "vagrant-pc\\vagrant",
      "agentVersion": "3.0.1.3",
      "classifierName": "STATIC",
      "fileExtensionType": "Executable",
      "agentDomain": "WORKGROUP",
      "fileIsSystem": false,
      "agentInfected": false,
      "isCertValid": false,
      "isInteractiveSession": false,
      "isPartialStory": false,
      "updatedAt": "2020-05-28T21:53:36.064425Z",
      "agentId": "560700200554747611",
      "agentMachineType": "desktop",
      "classification": "Malware",
      "markedAsBenign": false,
      "threatName": "EICAR.com",
      "agentIsDecommissioned": true,
      "description": "malware detected - not mitigated yet (static engin...",
      "fileDisplayName": "EICAR.com",
      "agentIp": "198.51.100.100",
      "agentIsActive": false,
      "fileObjectId": "F0F63E0588AAC528",
      "filePath": "\\Device\\HarddiskVolume2\\Users\\vagrant\\Desktop\\EICA...",
      "maliciousGroupId": "542D14600CEBA01D"
    }
  ],
  "pagination": {
    "totalItems": 1
  }
}
```

#### Mark as Benign

This action is used to mark a threat as resolved.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|target_scope|string|None|True|Scope to be used for exclusions|['group', 'site', 'tenant']|site|
|threat_id|string|None|True|ID of a threat|None|1000000000000000000|
|whitening_option|string|None|False|Selected whitening option|['', 'browser-type', 'certificate', 'file-type', 'file_hash', 'path']|path|

Example input:

```
{
  "target_scope": "site",
  "threat_id": "1000000000000000000",
  "whitening_option": "path"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

#### Mark as Threat

This action is used to mark a suspicious threat as a threat.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|target_scope|string|None|True|Scope to be used for exclusions|['group', 'site', 'tenant']|site|
|threat_id|string|None|True|ID of a threat|None|1000000000000000000|
|whitening_option|string|None|False|Selected whitening option|['', 'browser-type', 'certificate', 'file-type', 'file_hash', 'path']|path|

Example input:

```
{
  "target_scope": "site",
  "threat_id": 1000000000000000000,
  "whitening_option": "path"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

#### Mitigate Threat

This action is used to apply a mitigation action to a threat.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|Mitigation action|['rollback-remediation', 'quarantine', 'kill', 'remediate', 'un-quarantine']|quarantine|
|threat_id|string|None|True|ID of a threat|None|1000000000000000000|

Example input:

```
{
  "action": "quarantine",
  "threat_id": 1000000000000000000
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Number of entities affected by the requested operation|

Example output:

```
{
  "affected": 1
}
```

#### Available Name

This action is the account name available for this account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Account Name to validate|None|example|

Example input:

```
{
  "name": "example"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|available|boolean|True|Account Name to validate|

Example output:

```
{
  "available": true
}
```

#### Quarantine

This action is used to isolate (quarantine) endpoint from the network.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to perform quarantine action on. Accepts IP address, MAC address, hostname, UUID or agent ID|None|hostname123|
|case_sensitive|boolean|True|True|Looks up the specified Agent in a case-sensitive manner. Setting this value to false may result in longer run times and unintended results|None|True|
|quarantine_state|boolean|None|True|True to quarantine host, false to unquarantine host|None|True|
|whitelist|[]string|None|False|This list contains a set of devices that should not be blocked. This can include IPs, hostnames, UUIDs and agent IDs|None|["198.51.100.100", "hostname123", "901345720792880606", "28db47168fa54f89aeed99769ac8d4dc"]|

Example input:

```
{
  "agent": "hostname123",
  "case_sensitive": true,
  "quarantine_state": true,
  "whitelist": [
    "198.51.100.100",
    "hostname123",
    "901345720792880606",
    "28db47168fa54f89aeed99769ac8d4dc"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|quarantine_response|False|SentinelOne API call response data|

Example output:

```
{
  "response": {
    "response": {
      "data": {
        "affected": 0
      }
    }
  }
}
```

#### Search Agents

This action searches for agents by IP address, MAC address, hostname, or device ID. It can also return all active or inactive agents when no agent address is provided using the `agent_active` parameter.
Note that retrieving all active agents can return a very large amount of data depending on the number of agents you have in your environment.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|False|Agent to retrieve device information from. Accepts IP address, MAC address, hostname, UUID or agent ID. If empty, this action will return all active or inactive agents depending on the value of the Agent Active input|None|hostname123|
|agent_active|boolean|True|False|Return a list of all active or inactive agents when Agent input is not specified. Note that setting this to true for Active agents can return a very large amount of data|None|True|
|case_sensitive|boolean|True|True|Looks up agents in a case-sensitive manner. Setting this value to false may result in longer run times and unintended results|None|True|
|operational_state|string|Any|False|Agent operational state|['Any', 'na', 'fully_disabled', 'partially_disabled', 'disabled_error']|na|

Example input:

```
{
  "agent": "hostname123",
  "agent_active": true,
  "case_sensitive": true,
  "operational_state": "na"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents|[]agent_data|False|Detailed information about agents found|

Example output:

```
{
  "agents": [
    {
      "accountId": "433241117337583618",
      "accountName": "SentinelOne",
      "activeDirectory": {
        "computerDistinguishedName": "None",
        "computerMemberOf": [],
        "lastUserDistinguishedName": "None",
        "lastUserMemberOf": []
      },
      "activeThreats": 0,
      "agentVersion": "4.1.4.82",
      "allowRemoteShell": false,
      "appsVulnerabilityStatus": "up_to_date",
      "cloudProviders": {},
      "computerName": "so-agent-win12",
      "consoleMigrationStatus": "N/A",
      "coreCount": 1,
      "cpuCount": 1,
      "cpuId": "Intel(R) Xeon(R) CPU E5-2690 v2 @ 3.00GHz",
      "createdAt": "2020-05-28T14:53:03.014660Z",
      "domain": "WORKGROUP",
      "encryptedApplications": false,
      "externalId": "",
      "externalIp": "198.51.100.100",
      "firewallEnabled": true,
      "groupId": "521580416411822676",
      "groupIp": "198.51.100.x",
      "groupName": "Default Group",
      "id": "901345720792880606",
      "inRemoteShellSession": false,
      "infected": false,
      "installerType": ".exe",
      "isActive": true,
      "isDecommissioned": false,
      "isPendingUninstall": false,
      "isUninstalled": false,
      "isUpToDate": true,
      "lastActiveDate": "2020-06-05T18:32:56.748620Z",
      "lastIpToMgmt": "10.4.24.55",
      "lastLoggedInUserName": "",
      "licenseKey": "",
      "locationEnabled": true,
      "locationType": "fallback",
      "locations": [
        {
          "id": "629380164464502476",
          "name": "Fallback",
          "scope": "global"
        }
      ],
      "machineType": "server",
      "mitigationMode": "protect",
      "mitigationModeSuspicious": "detect",
      "modelName": "VMware, Inc. - VMware Virtual Platform",
      "networkInterfaces": [
        {
          "id": "901345720801269215",
          "inet": [
            "198.51.100.100"
          ],
          "inet6": [
            "2001:db8:8:4::2"
          ],
          "name": "Ethernet",
          "physical": "00:50:56:94:17:08"
        }
      ],
      "networkQuarantineEnabled": false,
      "networkStatus": "disconnected",
      "operationalState": "na",
      "operationalStateExpiration": "None",
      "osArch": "64 bit",
      "osName": "Windows Server 2012 Standard",
      "osRevision": "9200",
      "osStartTime": "2020-05-28T14:59:36Z",
      "osType": "windows",
      "osUsername": "None",
      "rangerStatus": "NotApplicable",
      "rangerVersion": "None",
      "registeredAt": "2020-05-28T14:53:03.010853Z",
      "remoteProfilingState": "disabled",
      "remoteProfilingStateExpiration": "None",
      "scanAbortedAt": "None",
      "scanFinishedAt": "2020-05-28T22:24:59.420166Z",
      "scanStartedAt": "2020-05-28T21:12:58.216807Z",
      "scanStatus": "finished",
      "siteId": "521580416395045459",
      "siteName": "Rapid7",
      "threatRebootRequired": false,
      "totalMemory": 1023,
      "updatedAt": "2020-06-05T15:39:10.754112Z",
      "userActionsNeeded": [],
      "uuid": "28db47168fa54f89aeed99769ac8d4dc"
    }
  ]
}
```

### Triggers

#### Get Threats

This trigger is used to get threats.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_is_active|boolean|True|False|Include agents currently connected to the management console|None|True|
|classifications|[]string|None|False|List of classifications to search|None|[""]|
|engines|[]string|None|False|Included engines|None|[""]|
|frequency|integer|5|False|Poll frequency in seconds|None|5|
|resolved|boolean|None|False|Include resolved threats|None|True|

Example input:

```
{
  "agent_is_active": true,
  "classifications": [
    ""
  ],
  "engines": [
    ""
  ],
  "frequency": 5,
  "resolved": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threat|threat_data|False|Threat|

Example output:

```
{
  'threat': {
    'agentComputerName':'vagrant-pc',
    'agentDomain':'WORKGROUP',
    'agentId':'560700200554747611',
    'agentInfected':False,
    'agentIp':'xxx.xxx.xxx.xxx',
    'agentIsActive':True,
    'agentIsDecommissioned':False,
    'agentMachineType':'desktop',
    'agentNetworkStatus':'connected',
    'agentOsType':'windows',
    'agentVersion':'3.0.1.3',
    'annotation':None,
    'annotationUrl':None,
    'browserType':None,
    'certId':'',
    'classification':'Malware',
    'classificationSource':'Engine',
    'classifierName':'BLACKLIST',
    'cloudVerdict':'black',
    'collectionId':'433377870883088367',
    'createdAt':'2019-02-13T15:05:21.948892Z',
    'createdDate':'2019-02-13T15:05:21.605000Z',
    'description':'malware detected - not mitigated yet (static engine)',
    'engines':[
        'reputation'
    ],
    'fileContentHash':'3395856ce81f2b7382dee72602f798b642f14140',
    'fileCreatedDate':None,
    'fileDisplayName':'{D5EEFA7C-3EA6-4B78-BED3-56CB49156FD1}-EICAR.com',
    'fileExtensionType':'Executable',
    'fileIsDotNet':None,
    'fileIsExecutable':False,
    'fileIsSystem':False,
    'fileMaliciousContent':None,
    'fileObjectId':'49E6C98245C9F0D8',
    'filePath':'\\Device\\HarddiskVolume2\\ProgramData\\Microsoft\\Windows Defender\\LocalCopy\\{D5EEFA7C-3EA6-4B78-BED3-56CB49156FD1}-EICAR.com',
    'fileSha256':None,
    'fileVerificationType':'NotSigned',
    'fromCloud':False,
    'fromScan':False,
    'id':'560707325754496894',
    'indicators':[

    ],
    'isCertValid':False,
    'isInteractiveSession':False,
    'isPartialStory':False,
    'maliciousGroupId':'B5930C761E06E0CD',
    'maliciousProcessArguments':None,
    'markedAsBenign':None,
    'mitigationMode':'protect',
    'mitigationReport':{
        'kill':{
          'status':'success'
        },
        'network_quarantine':{
          'status':None
        },
        'quarantine':{
          'status':'success'
        },
        'remediate':{
          'status':None
        },
        'rollback':{
          'status':None
        }
    },
    'mitigationStatus':'mitigated',
    'publisher':'',
    'rank':7,
    'resolved':False,
    'siteId':'521580416395045459',
    'siteName':'Rapid7',
    'threatAgentVersion':'3.0.1.3',
    'threatName':None,
    'updatedAt':'2019-02-13T15:05:22.274291Z',
    'username':'',
    'whiteningOptions':[
        'hash'
    ]
  }
}
```

### Custom Output Types

#### activities_list

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account ID|string|False|Related account (If applicable)|
|Activity Type|integer|False|Activity type|
|Agent ID|string|False|Related agent (If applicable)|
|Agent Updated Version|string|False|Agent's new version (If applicable)|
|Comments|string|False|Comments|
|Created At|string|False|Activity creation time (UTC)|
|Data|object|False|Extra activity specific data|
|Description|string|False|Extra activity information|
|Group ID|string|False|Related group (If applicable)|
|Hash|string|False|Threat file hash (If applicable)|
|ID|string|False|Activity ID|
|OS Family|string|False|Agent's OS type (if applicable)|
|Primary Description|string|False|Primary description|
|Secondary Description|string|False|Secondary description|
|Site ID|string|False|Related site (If applicable)|
|Threat ID|string|False|Related threat (If applicable)|
|Updated At|string|False|Activity last updated time (UTC)|
|UserId|string|False|The user who invoked the activity (If applicable)|

#### activities_types

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action|string|False|Action described in the activity|
|Description Template|string|False|Activity description template as seen in activity page|
|Type ID|float|False|Activity type ID|

#### agent_applications

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Installed Date|string|False|Date when application installed|
|Name|string|False|Name of installed application|
|Publisher|string|False|Publisher of installed application|
|Size|string|False|Size of installed application|
|Version|string|False|Version of installed application|

#### agent_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account ID|string|False|A reference to the containing account|
|Account Name|string|False|Name of the containing account|
|Active Directory|object|False|Active Directory data|
|Active Threats|integer|False|Current number of active threats|
|Agent Version|string|False|Agent version|
|Allow Remote Shell|boolean|False|Agent is capable and policy enabled for remote shell|
|Apps Vulnerability Status|string|False|Apps vulnerability status|
|Computer Name|string|False|Computer name|
|Console Migration Status|string|False|What step the agent is at in the process of migrating to another console, if any|
|Core Count|integer|False|Number of CPU cores|
|CPU Count|integer|False|Number of CPUs|
|CPU ID|string|False|CPU model|
|Created At|string|False|Created at date|
|Domain|string|False|Network domain|
|Encrypted Applications|boolean|False|Disk encryption status|
|External ID|string|False|External id set by customer|
|External IP|string|False|External IPv4 address|
|Group ID|string|False|A reference to the containing network group|
|Group IP|string|False|IP Address subnet|
|Group Name|string|False|Name of the containing network group|
|Group Updated At|string|False|Date of when the group was last updated|
|ID|string|False|Agent ID|
|In Remote Shell Session|boolean|False|Is the Agent in a remote shell session|
|Infected|boolean|False|Indicates if the Agent has active threats|
|Installer Type|string|False|Installer package type (file extension)|
|Is Active|boolean|False|Indicates if the agent was recently active|
|Is Decommissioned|boolean|False|Is Agent decommissioned|
|Is Pending Uninstall|boolean|False|Agent with a pending uninstall request|
|Is Uninstalled|boolean|False|Indicates if Agent was removed from the device|
|Is Up To Date|boolean|False|Indicates if the agent version is up to date|
|Last Active Date|string|False|Last active date|
|Last Logged In User Name|string|False|Last logged in user name|
|License Key|string|False|License key|
|Location Type|string|False|Reported location type|
|Locations|[]object|False|A list of locations reported by the Agent|
|Machine Type|string|False|Machine type|
|Mitigation Mode|string|False|Agent mitigation mode policy|
|Mitigation Mode Suspicious|string|False|Mitigation mode policy for suspicious activity|
|Model Name|string|False|Model name|
|Network Interfaces|[]object|False|Device's network interfaces|
|Network Status|string|False|Agent's network connectivity status|
|OS Arch|string|False|OS Arch|
|OS Name|string|False|Os name|
|OS Revision|string|False|OS revision|
|OS Start Time|string|False|Last boot time|
|OS Type|string|False|OS type|
|OS Username|string|False|Os username|
|Policy Updated At|string|False|Date of when the policy was last updated|
|Ranger Status|string|False|Is Agent disabled as a Ranger|
|Ranger Version|string|False|The version of Ranger|
|Registered At|string|False|Time of first registration to management console (similar to createdAt)|
|Scan Aborted At|string|False|Abort time of last scan|
|Scan Finished At|string|False|Finish time of last scan|
|Scan Started At|string|False|Start time of last scan|
|Scan Status|string|False|Last scan status|
|Site ID|string|False|A reference to the containing site|
|Site Name|string|False|Name of the containing site|
|Threat Reboot Required|boolean|False|Has at least one threat with at least one mitigation action that is pending reboot to succeed|
|Total Memory|integer|False|Memory size (MB)|
|Updated at|string|False|Last updated date|
|User Actions Needed|[]string|False|A list of pending user actions|
|UUID|string|False|Agent's universally unique identifier|

#### blacklist_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Affected|integer|False|Affected|

#### threat_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent Computer Name|string|False|Agent computer name|
|Agent Domain|string|False|Agent domain|
|Agent ID|string|False|Agent ID|
|Agent Infected|boolean|False|Agent infected|
|Agent IP|string|False|Agent IP|
|Agent is Active|boolean|False|Agent is Active|
|Agent is Decommissioned|boolean|False|Agent is Decommissioned|
|Agent Machine Type|string|False|Agent machine type|
|Agent Network Status|string|False|Agent network status|
|Agent OS Type|string|False|Agent OS type|
|Agent Version|string|False|Agent version|
|Annotation|string|False|Annotation|
|Annotation URL|string|False|Annotation URL|
|Browser Type|string|False|Browser type|
|Cert ID|string|False|Cert ID|
|Classification|string|False|Classification|
|Classification Source|string|False|Classification source|
|Classifiername|string|False|Classifiername|
|Cloud Verdict|string|False|Cloud verdict|
|Collection ID|string|False|Collection ID|
|Created At|string|False|Created At|
|Created Date|string|False|Created date|
|Description|string|False|Description|
|Engines|[]string|False|Engines|
|File Content Hash|string|False|File content hash|
|File Created Date|string|False|File created date|
|File Data|object|False|File data|
|File Display Name|string|False|File display name|
|File Extension Type|string|False|File extension type|
|File is Dotnet|boolean|False|File is dotnet|
|File is Executable|boolean|False|File is executable|
|File is System|boolean|False|File is system|
|File Malicious Content|boolean|False|File malicious content|
|File Object ID|string|False|File object ID|
|File Path|string|False|File path|
|File SHA 256|string|False|File SHA 256|
|File Verification Type|string|False|File verification type|
|From Cloud|boolean|False|From cloud|
|From Scan|boolean|False|From scan|
|ID|string|False|ID|
|In Quarantine|boolean|False|In quarantine|
|Indicators|[]integer|False|Indicators|
|Is Cert Valid|boolean|False|Is cert valid|
|Is Interactive Session|boolean|False|Is interactive session|
|Is Partial Story|boolean|False|Is partial story|
|Malicious Group ID|string|False|Malicious group ID|
|Malicious Process Arguments|string|False|Malicious process arguments|
|Marked as Benign|boolean|False|Marked as Benign|
|Mitigation Actions|[]string|False|Mitigation actions|
|Mitigation Mode|string|False|Mitigation mode|
|Mitigation Report|object|False|Mitigation report|
|Mitigation Status|string|False|Mitigation status|
|Publisher|string|False|Publisher|
|Rank|integer|False|Rank|
|Resolved|boolean|False|Resolved|
|Site ID|string|False|Site ID|
|Site Name|string|False|Site name|
|Threat Agent Version|string|False|Threat agent version|
|Threat Name|string|False|Threat name|
|Updated At|string|False|Updated at|
|Username|string|False|Username|
|Whitening Options|[]string|False|Whitening options|

#### pagination

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Next Cursor|string|False|Next cursor|
|Total Items|integer|False|Total items|

#### quarantine_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|object|False|Response data|
|Errors|[]object|False|Errors|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 6.3.0 - Add new actions Update Analyst Verdict and Update Incident Status | Fix Get Agent Details and Search Agents actions to handle more response scenarios
* 6.2.0 - New actions Create Query, Get Query Status, Cancel Running Query, Get Events, Get Events By Type
* 6.1.0 - Add new actions Disable Agent and Enable Agent
* 6.0.0 - Add `operational_state` field to input of Get Agent Details and Search Agent actions | Update schema to return new outputs such as Active Directory, firewall, location, and quarantine information for Get Agent Details and Search Agent actions | Use API version 2.1 | Update capitalization according to style in Activities List action for Created Than Date and Less Than Dates inputs to Greater than Date and Less than Date
* 5.0.1 - Correct spelling in help.md
* 5.0.0 - Consolidate various Agent actions | Use API version 2.1 where possible | Delete obsolete Blacklist by IOC Hash and Agent Processes
* 4.1.1 - Update the Get Threat Summary action to return all threat summaries instead of 10
* 4.1.0 - Add case sensitivity option for Agent lookups
* 4.0.1 - Fix Agent Active parameter in Get Agent Details action | Update Quarantine action whitelist for IP addresses
* 4.0.0 - Update ID input for Fetch Threats File action to a string
* 3.1.0 - Add new action Fetch Threats File
* 3.0.0 - Update help.md for the Extension Library | Update title in action Blacklist by IOC Hash, Get Activities, Count Summary and Connect to Network
* 2.1.1 - Upgrade trigger Get Threats to only return threats since trigger start
* 2.1.0 - Add `agent_active` field to input in action Search Agents
* 2.0.0 - Upgrade trigger input Agent is Active to default true
* 1.4.0 - New actions Quarantine, Get Agent Details, Search Agents
* 1.3.0 - Add new action Blacklist
* 1.2.2 - Update error message in Connection
* 1.2.1 - Update to use the `komand/python-3-37-slim-plugin` Docker image to reduce plugin size
* 1.2.0 - New spec and help.md format for the Extension Library | New actions activities_list, activities_types, agents_abort_scan, agents_connect, agents_decommission, agents_disconnect, agents_fetch_logs, agents_initiate, agents_processes, agents_reload, agents_restart, agents_shutdown, agents_summary, agents_uninstall, apps_by_agent_ids, name_available
* 1.1.0 - New trigger Get Threats | New actions Mitigate Threat, Mark as Benign, Mark as Threat and Create IOC Threat
* 1.0.1 - Update to add Blacklist by IOC Hash and Blacklist by Content Hash
* 1.0.0 - Initial plugin

# Links

## References

* [SentinelOne Product Page](https://www.sentinelone.com/)
