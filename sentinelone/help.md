# Description

[SentinelOne](https://www.sentinelone.com/) is a next-gen cybersecurity company focused on protecting the enterprise through the endpoint. The SentinelOne plugin allows you to manage and mitigate all your security operations through SentinelOne.

This plugin utilizes the SentinelOne API, the documentation is located in the SentinelOne console.

# Key Features

* Quarantine endpoints
* Execute scans
* Blacklist hashes
* Trigger workflows on security alerts
* Manage threats

# Requirements

* Sentinel one API administrative credentials

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
    "password": "mypassword
  },
  "url": "https://example.sentinelone.com"
}
```

## Technical Details

### Actions

#### Search Agents

This action searches for agents by IP address, MAC address, hostname, or device ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, MAC address, hostname, or device ID|None|hostname123|

Example input:

```
{
  "agent": "hostname123"
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
      "installerType": ".exe",
      "threatRebootRequired": false,
      "groupIp": "198.51.100.x",
      "modelName": "VMware, Inc. - VMware Virtual Platform",
      "machineType": "server",
      "groupName": "Default Group",
      "lastActiveDate": "2020-06-03T18:53:56.748663Z",
      "registeredAt": "2020-05-28T14:53:03.010853Z",
      "scanStatus": "finished",
      "allowRemoteShell": false,
      "appsVulnerabilityStatus": "up_to_date",
      "coreCount": 1,
      "inRemoteShellSession": false,
      "isDecommissioned": false,
      "siteId": "521580416395045459",
      "accountName": "SentinelOne",
      "isActive": true,
      "isUpToDate": true,
      "networkStatus": "disconnected",
      "osType": "windows",
      "updatedAt": "2020-06-03T18:53:39.584577Z",
      "createdAt": "2020-05-28T14:53:03.014660Z",
      "siteName": "Rapid7",
      "lastLoggedInUserName": "",
      "domain": "WORKGROUP",
      "externalId": "",
      "scanAbortedAt": "None",
      "computerName": "so-agent-win12",
      "id": "901345720792880606",
      "locationType": "fallback",
      "mitigationMode": "protect",
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
      "scanStartedAt": "2020-05-28T21:12:58.216807Z",
      "userActionsNeeded": [],
      "activeDirectory": {
        "computerDistinguishedName": "None",
        "computerMemberOf": [],
        "lastUserDistinguishedName": "None",
        "lastUserMemberOf": []
      },
      "externalIp": "198.51.100.100",
      "isUninstalled": false,
      "licenseKey": "",
      "osArch": "64 bit",
      "totalMemory": 1023,
      "accountId": "433241117337583618",
      "consoleMigrationStatus": "N/A",
      "groupId": "521580416411822676",
      "isPendingUninstall": false,
      "locations": [
        {
          "scope": "global",
          "id": "629380164464502476",
          "name": "Fallback"
        }
      ],
      "osStartTime": "2020-05-28T14:59:33Z",
      "scanFinishedAt": "2020-05-28T22:24:59.420166Z",
      "cpuCount": 1,
      "osUsername": "None",
      "rangerVersion": "None",
      "agentVersion": "4.1.4.82",
      "osRevision": "9200",
      "uuid": "28db47168fa54f89aeed99769ac8d4dc",
      "mitigationModeSuspicious": "detect",
      "cpuId": "Intel(R) Xeon(R) CPU E5-2690 v2 @ 3.00GHz",
      "infected": false,
      "encryptedApplications": false,
      "osName": "Windows Server 2012 Standard",
      "rangerStatus": "NotApplicable",
      "activeThreats": 0
    }
  ]
}
```

#### Quarantine

This action is used to isolate (quarantine) endpoint from the network.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to perform quarantine action on. Accepts IP address, MAC address, hostname, or device ID|None|hostname123|
|quarantine_state|boolean|None|True|True to quarantine host, false to unquarantine host|None|True|
|whitelist|[]string|None|False|This list contains a set of devices that should not be blocked. This can include IPs, hostnames, and device IDs|None|["198.51.100.100", "225494730938493804"]|

Example input:

```
{
  "agent": "hostname123",
  "quarantine_state": true,
  "whitelist": [
    "198.51.100.100",
    "225494730938493804"
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

#### Get Agent Details

This action retrieves agent details.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, MAC address, hostname, or device ID|None|hostname123|

Example input:

```
{
  "agent": "hostname123"
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
    "lastLoggedInUserName": "",
    "licenseKey": "",
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
    "networkStatus": "disconnected",
    "osArch": "64 bit",
    "osName": "Windows Server 2012 Standard",
    "osRevision": "9200",
    "osStartTime": "2020-05-28T14:59:36Z",
    "osType": "windows",
    "osUsername": "None",
    "rangerStatus": "NotApplicable",
    "rangerVersion": "None",
    "registeredAt": "2020-05-28T14:53:03.010853Z",
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

This action is used to get a list of activities.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|account_ids|[]string|None|False|List of Account IDs to filter by|None|
|activity_types|[]string|None|False|Return only these activity codes|None|
|agent_ids|[]string|None|False|Return activities related to specified agent ids|None|
|count_only|boolean|None|False|If true, only total number of items will be returned, without any of the actual objects|None|
|created_at_between|string|None|False|Return activities created within this range (inclusive), example 1514978764288-1514978999999|None|
|created_at_gt|string|None|False|Return activities created after or at this date in ISO-8601, example 2018-02-27T04:49:26.257525Z.|None|
|created_at_gte|string|None|False|Return activities created after or at this date in ISO-8601, example 2018-02-27T04:49:26.257525Z|None|
|created_at_lt|string|None|False|Return activities created before this date in ISO-8601, example 2018-02-27T04:49:26.257525Z.|None|
|created_at_lte|string|None|False|Return activities created before or at this date in ISO-8601, example 2018-02-27T04:49:26.257525Z.|None|
|cursor|string|None|False|Cursor position returned by the last request. Should be used for iterating over more than 1000 items, example YWdlbnRfaWQ6NTgwMjkzODE=|None|
|group_ids|[]string|None|False|Get a list of activities|None|
|ids|[]string|None|False|If true, total number of items will not be calculated, which speeds up execution time|None|
|include_hidden|boolean|None|False|Include internal activities hidden from display?|None|
|limit|integer|None|False|Limit number of returned items (1-100)|None|
|site_ids|[]string|None|False|List of Site IDs to filter by|None|
|skip|integer|None|False|Skip first number of items (0-1000). For iterating over more than a 1000 items please use cursor instead.|None|
|skip_count|boolean|None|False|If true, total number of items will not be calculated, which speeds up execution time|None|
|sort_by|string|None|False|The column to sort the results by|['id', 'activityType', 'createdAt']|
|sort_order|string|None|False|Sort direction|['asc', 'desc']|
|threat_ids|[]string|None|False|Return only these activity codes|None|
|user_emails|[]string|None|False|Email of the user who invoked the activity (If applicable)|None|
|user_ids|[]string|None|False|The user who invoked the activity (If applicable)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]activities_list|True|Result of activities list|
|pagination|pagination|True|Pagination object|

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

#### Get Activities

This action is used to get a list of activities.

#### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_ids|[]string|None|False|List of Account IDs to filter by|None|None|
|activity_types|[]string|None|False|Return only these activity codes|None|None|
|agent_ids|[]string|None|False|Return activities related to specified agent ids|None|None|
|count_only|boolean|None|False|If true, only total number of items will be returned, without any of the actual objects|None|None|
|created_at_between|string|None|False|Return activities created within this range (inclusive), example 1514978764288-1514978999999|None|None|
|created_at_gt|string|None|False|Return activities created after or at this date in ISO-8601, example 2018-02-27T04:49:26.257525Z|None|None|
|created_at_gte|string|None|False|Return activities created after or at this date in ISO-8601, example 2018-02-27T04:49:26.257525Z|None|None|
|created_at_lt|string|None|False|Return activities created before this date in ISO-8601, example 2018-02-27T04:49:26.257525Z|None|None|
|created_at_lte|string|None|False|Return activities created before or at this date in ISO-8601, example 2018-02-27T04:49:26.257525Z|None|None|
|cursor|string|None|False|Cursor position returned by the last request. Should be used for iterating over more than 1000 items, example YWdlbnRfaWQ6NTgwMjkzODE=|None|None|
|group_ids|[]string|None|False|Get a list of activities|None|None|
|ids|[]string|None|False|If true, total number of items will not be calculated, which speeds up execution time|None|None|
|include_hidden|boolean|None|False|Include internal activities hidden from display?|None|None|
|limit|integer|None|False|Limit number of returned items (1-100)|None|None|
|site_ids|[]string|None|False|List of Site IDs to filter by|None|None|
|skip|integer|None|False|Skip first number of items (0-1000). For iterating over more than a 1000 items please use cursor instead|None|None|
|skip_count|boolean|None|False|If true, total number of items will not be calculated, which speeds up execution time|None|None|
|sort_by|string|None|False|The column to sort the results by|['id', 'activityType', 'createdAt']|None|
|sort_order|string|None|False|Sort direction|['asc', 'desc']|None|
|threat_ids|[]string|None|False|Return only these activity codes|None|None|
|user_emails|[]string|None|False|Email of the user who invoked the activity (If applicable)|None|None|
|user_ids|[]string|None|False|The user who invoked the activity (If applicable)|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]activities_list|True|Result of activities list|
|pagination|pagination|True|Pagination object|

Example output:

```
```

#### Get Activity Types

This action is used to get a list of activity types.

Example input:

```
```

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

#### Agents Abort Scan

This action aborts running scan on all agents matching the input filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents|None|None|

Example input:

```
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

#### Connect to network

This action sends a connect to network command to all agents matching the input filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents|None|None|

Example input:

```
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

#### Agent Decommission

This action decommissions all agents matching the input filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Note - one of the following filter arguments must be supplied - ids, groupIds, filterId|None|None|

Example input:

```
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

#### Disconnect Agents

This action disconnects agents associated to marked threats from network.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Use any of the filtering options to control the list of affected threats. You can also leave this field empty to apply to all available threats|None|None|

Example input:

```
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

#### Agents Fetch Logs

This action sends a fetch logs command to all agents matching the input filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents|None|None|

Example input:

```
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

#### Initiate scan

This action sends a scan command to all agents matching the input filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents|None|None|

Example input:

```
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

#### Agents Processes

This action is used to retrieve running processes for a specific agent.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ids|[]string|None|True|Agent ID list|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents_processes|[]agents_processes|False|Agents processes entities|

Example output:

```
```

#### Agents Reload

This action is used to reload an agent module (applies to Windows agents only).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents|None|None|
|module|string|None|True|Agent module to reload|['monitor', 'static', 'agent', 'log']|None|

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
  "affected": 0
}
```

#### Agents Restart

This action sends a restart command to all agents matching the input filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Note - One of the following filter arguments must be supplied - ids, groupIds, filterId|None|None|

Example input:

```
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

#### Agents Shutdown

This action sends a shutdown command to all agents matching the input filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Note - one of the following filter arguments must be supplied - ids, groupIds, filterId|None|None|

Example input:

```
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
|account_ids|[]string|None|False|List of Account IDs to filter by|None|None|
|site_ids|[]string|None|False|List of Site IDs to filter by|None|None|

Example input:

```
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
```

#### Uninstall

This action sends an uninstall command to all agents matching the input filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Note - one of the following filter arguments must be supplied - ids, groupIds, filterId|None|None|

Example input:

```
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

#### Agents Applications

This action is used to retrieve running applications for a specific agent.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ids|[]string|None|True|Agent ID list|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]agent_applications|True|List of installed applications|

Example output:

```
```

#### Blacklist by Content Hash

This action is used to add hashed content to global blacklist. The input for this action makes use of `contentHash` from the threat summary.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|Content hash to add to blacklist|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|blacklist_data|True|Result of hashing operation|

Example output:

```
{
  "blacklist_data": {
    "affected": 127
  }
}
```

#### Blacklist by IoC Hash

This action is used to add hashed indicator of compromise to global blacklist.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_id|string|None|True|Agent ID|None|None|
|hash|string|None|True|Indicator of compromise hash to add to blacklist|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|blacklist_data|True|Result of hashing operation|

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
|agent_id|string|None|True|Agent ID for the slim threat|None|None|
|annotation|string|None|True|Vigilance annotation|None|None|
|annotation_url|string|None|True|Vigilance annotation URL|None|None|
|group_id|string|None|False|Group ID|None|None|
|hash|string|None|True|SHA1 hash|None|None|
|path|string|None|False|Path|None|None|

Example input:

```
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

#### Get Threat Summary

This action gets summary of all threats.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]data|False|Data|
|errors|[]object|False|Errors|
|pagination|pagination|False|Pagination|

Example output:

```
```

#### Mark as Benign

This action is used to mark a threat as resolved.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|target_scope|string|None|True|Scope to be used for exclusions|['group', 'site', 'tenant']|None|
|threat_id|string|None|True|ID of a threat|None|None|
|whitening_option|string|None|False|Selected whitening option|['', 'browser-type', 'certificate', 'file-type', 'file_hash', 'path']|None|

Example input:

```
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
|target_scope|string|None|True|Scope to be used for exclusions|['group', 'site', 'tenant']|None|
|threat_id|string|None|True|ID of a threat|None|None|
|whitening_option|string|None|False|Selected whitening option|['', 'browser-type', 'certificate', 'file-type', 'file_hash', 'path']|None|

Example input:

```
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
|action|string|None|True|Mitigation action|['rollback-remediation', 'quarantine', 'kill', 'remediate', 'un-quarantine']|None|
|threat_id|string|None|True|ID of a threat|None|None|

Example input:

```
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
|name|string|None|True|Account Name to validate|None|None|

Example input:

```
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

### Triggers

#### Get Threats

This trigger is used to get threats.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_is_active|boolean|None|False|Include agents currently connected to the management console|None|None|
|classifications|[]string|None|False|List of classifications to search|None|None|
|engines|[]string|None|False|Included engines|None|None|
|frequency|integer|5|False|Poll frequency in seconds|None|None|
|resolved|boolean|None|False|Include resolved threats|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threat|data|False|Threat|

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

#### activities_types

|Name|Type|Required|Description|
|----|----|--------|-----------|
|action|string|False|Action descripted in the activity|
|descriptionTemplate|string|False|Activity description template as seen in activity page|
|id|float|False|Activity type ID|

#### activities_list

|Name|Type|Required|Description|
|----|----|--------|-----------|
|accountId|string|False|Related account (If applicable)|
|activityType|integer|False|Activity type|
|agentId|string|False|Related agent (If applicable)|
|agentUpdatedVersion|string|False|Agent's new version (If applicable)|
|comments|string|False|Comments|
|createdAt|string|False|Activity creation time (UTC)|
|data|object|False|Extra activity specific data|
|description|string|False|Extra activity information|
|groupId|string|False|Related group (If applicable)|
|hash|string|False|Threat file hash (If applicable)|
|id|string|False|Activity ID|
|osFamily|string|False|Agent's OS type (if applicable)|
|primaryDescription|string|False|Primary description|
|secondaryDescription|string|False|Secondary description|
|siteId|string|False|Related site (If applicable)|
|threatId|string|False|Related threat (If applicable)|
|updatedAt|string|False|Activity last updated time (UTC)|
|userId|string|False|The user who invoked the activity (If applicable)|

#### agent_applications

|Name|Type|Required|Description|
|----|----|--------|-----------|
|installedDate|string|False|Date when application installed|
|name|string|False|Name of installed application|
|publisher|string|False|Publisher of installed application|
|size|string|False|Size of installed application|
|version|string|False|Version of installed application|

#### agents_processes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cpuUsage|integer|False|CPU Usage (%)|
|executablePath|string|False|Executable path|
|memoryUsage|integer|False|Memory usage (MB)|
|pid|integer|False|Process ID|
|processName|string|False|Process name|
|startTime|string|False|Start time|

#### blacklist_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|affected|integer|False|Affected|

#### pagination

|Name|Type|Required|Description|
|----|----|--------|-----------|
|nextCursor|string|False|Next cursor|
|totalItems|integer|False|Total items|

#### data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agentComputerName|string|False|Agent computer name|
|agentDomain|string|False|Agent domain|
|agentId|string|False|Agent ID|
|agentInfected|boolean|False|Agent infected|
|agentIp|string|False|Agent IP|
|agentIsActive|boolean|False|Agent is Active|
|agentIsDecommissioned|boolean|False|Agent is Decommissioned|
|agentMachineType|string|False|Agent machine type|
|agentNetworkStatus|string|False|Agent network status|
|agentOsType|string|False|Agent OS type|
|agentVersion|string|False|Agent version|
|annotation|string|False|Annotation|
|annotationUrl|string|False|Annotation URL|
|browserType|string|False|Browser type|
|certId|string|False|Cert ID|
|classification|string|False|Classification|
|classificationSource|string|False|Classification source|
|classifierName|string|False|Classifiername|
|cloudVerdict|string|False|Cloud verdict|
|collectionId|string|False|Collection ID|
|createdAt|string|False|Created At|
|createdDate|string|False|Created date|
|description|string|False|Description|
|engines|[]string|False|Engines|
|fileContentHash|string|False|File content hash|
|fileCreatedDate|string|False|File created date|
|fileData|object|False|File data|
|fileDisplayName|string|False|File display name|
|fileExtensionType|string|False|File extension type|
|fileIsDotNet|boolean|False|File is dotnet|
|fileIsExecutable|boolean|False|File is executable|
|fileIsSystem|boolean|False|File is system|
|fileMaliciousContent|boolean|False|File malicious content|
|fileObjectId|string|False|File object ID|
|filePath|string|False|File path|
|fileSha256|string|False|File SHA 256|
|fileVerificationType|string|False|File verification type|
|fromCloud|boolean|False|From cloud|
|fromScan|boolean|False|From scan|
|id|string|False|ID|
|inQuarantine|boolean|False|In quarantine|
|indicators|[]integer|False|Indicators|
|isCertValid|boolean|False|Is cert valid|
|isInteractiveSession|boolean|False|Is interactive session|
|isPartialStory|boolean|False|Is partial story|
|maliciousGroupId|string|False|Malicious group ID|
|maliciousProcessArguments|string|False|Malicious process arguments|
|markedAsBenign|boolean|False|Marked as Benign|
|mitigationActions|[]string|False|Mitigation actions|
|mitigationMode|string|False|Mitigation mode|
|mitigationReport|object|False|Mitigation report|
|mitigationStatus|string|False|Mitigation status|
|publisher|string|False|Publisher|
|rank|integer|False|Rank|
|resolved|boolean|False|Resolved|
|siteId|string|False|Site ID|
|siteName|string|False|Site name|
|threatAgentVersion|string|False|Threat agent version|
|threatName|string|False|Threat name|
|updatedAt|string|False|Updated at|
|username|string|False|Username|
|whiteningOptions|[]string|False|Whitening options|

#### agent_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account Id|string|False|A reference to the containing account|
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
|External Ip|string|False|External IPv4 address|
|Group Id|string|False|A reference to the containing network group|
|Group IP|string|False|IP Address subnet|
|Group Name|string|False|Name of the containing network group|
|Group Updated At|string|False|Date of when the group was last updated|
|id|string|False|Agent ID|
|In Remote Shell Session|boolean|False|Is the Agent in a remote shell session|
|infected|boolean|False|Indicates if the Agent has active threats|
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
|Site Id|string|False|A reference to the containing site|
|Site Name|string|False|Name of the containing site|
|Threat Reboot Required|boolean|False|Has at least one threat with at least one mitigation action that is pending reboot to succeed|
|Total Memory|integer|False|Memory size (MB)|
|Updated at|string|False|Last updated date|
|User Actions Needed|[]string|False|A list of pending user actions.|
|UUID|string|False|Agent's universally unique identifier|

#### quarantine_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|object|False|Response data|
|Errors|[]object|False|Errors|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.4.0 - New actions Quarantine, Get Agent Details, Search Agents
* 1.3.0 - Add new action Blacklist
* 1.2.2 - Update error message in Connection
* 1.2.1 - Update to use the `komand/python-3-37-slim-plugin` Docker image to reduce plugin size
* 1.2.0 - New spec and help.md format for the Extension Library | New actions activities_list, activities_types, agents_abort_scan, agents_connect, agents_decommission, agents_disconnect, agents_fetch_logs, agents_initiate, agents_processes, agents_reload, agents_restart, agents_shutdown, agents_summary, agents_uninstall, apps_by_agent_ids, name_available
* 1.1.0 - New trigger Get Threats | New actions Mitigate Threat, Mark as Benign, Mark as Threat and Create IOC Threat
* 1.0.1 - Update to add Blacklist by IoC Hash and Blacklist by Content Hash
* 1.0.0 - Initial plugin

# Links

## References

* [SentinelOne Product Page](https://www.sentinelone.com/)
