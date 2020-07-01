# Description

Ivanti Security Controls is a unified IT management platform used for managing and protecting through Patch Management, Application Control, and Asset Inventory functionality.

# Key Features

* Ability to retrieve Ivanti Security Controls known agents
* Ability to check agent status

# Requirements

* Ivanti Security Controls 2019.3 (Build: 9.4.34544) or later
* Ivanti Security Controls host and API port (default: 3121)
* Username and password of Windows account where Ivanti Security Controls is installed 
* (Recommended) Ivanti Security Controls certificate in order to enforce certificate verification

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|
|host|string|None|True|Enter the hostname|None|example.com|
|port|integer|3121|True|Enter the port|None|3121|
|ssl_verify|boolean|True|True|Validate certificate|None|True|

Example input:

```
{
  "credentials": "{\"username\":\"user1\", \"password\":\"mypassword\"}",
  "host": "example.com",
  "port": 3121,
  "ssl_verify": true
}
```

## Technical Details

### Actions

#### Start Patch Deployment

This action is used to start patch deployment.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|download_patches|boolean|None|True|Boolean to initiate patch download before starting the deployment|None|False|
|scan_identifier|string|None|True|A scan ID or scan name|None|01234567-89AB-CDEF-0123-456789ABCDEF|
|template_identifier|string|None|True|A template ID or template name|None|Template created from InsightConnect|

Example input:

```
{
  "download_patches": false,
  "scan_identifier": "01234567-89AB-CDEF-0123-456789ABCDEF",
  "template_identifier": "Template created from InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
```

#### Get Patch Deployment Template ID

This action is used to get a Patch Deployment Template ID by searching for the Patch Deployment Template Name.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|patch_deployment_template_name|string|None|True|The name of the patch deployment template|None|Patch Deployment Template created from InsightConnect|

Example input:

```
{
  "patch_deployment_template_name": "example-template-name"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|patch_deployment_template_id|string|False|The ID of the patch deployment template|

Example output:

```
```

#### Get Patch Deployment

This action is used to retrieve information about a specific patch deployment.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|deployment_id|string|None|True|Patch deployment ID|None|5dbcb89f-eec3-4182-a9aa-1e6074fb0acb|
|machine_id|integer|None|False|ID of a machine involved with a specific patch deployment|None|7|

Example input:

```
{
  "deployment_id": "5dbcb89f-eec3-4182-a9aa-1e6074fb0acb",
  "machine_id": 7
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_information|machine_deploy_state|True|Information about a machine involved with the patch deployment|
|patch_deployment_details|patch_deployment|True|Detailed information about a specific deployment|

Example output:

```
{
  "patch_deployment_details": {
    "completedMachineCount": 1,
    "creator": "IVANTI-W16\\Administrator",
    "expectedMachineCount": 1,
    "id": "282cbbf9-276d-4d36-a96d-6e55c8a7271e",
    "isComplete": true,
    "lastUpdatedOn": "2020-05-08T13:38:37.987Z",
    "links": {
      "self": {
        "href": "https://example.com:3121/st/console/api/v1.0/patch/deployments/282cbbf9-276d-4d36-a96d-6e55c8a7271e"
      },
      "machines": {
        "href": "https://example.com:3121/st/console/api/v1.0/patch/deployments/282cbbf9-276d-4d36-a96d-6e55c8a7271e/machines"
      },
      "template": {
        "href": "https://example.com:3121/st/console/api/v1.0/patch/deploytemplates/7b5bc7e4-7437-47ac-ae2e-569ffdb0ccf8"
      }
    },
    "name": "Standard",
    "startedOn": "2020-05-08T13:33:39.077Z"
  },
  "machine_information": [
    {
      "address": "10.4.27.111",
      "completedPatches": 1,
      "domain": "WORKGROUP",
      "id": 36,
      "lastUpdated": "2020-05-08T13:38:37.987Z",
      "links": {
        "self": {
          "href": "https://example.com:3121/st/console/api/v1.0/patch/deployments/282cbbf9-276d-4d36-a96d-6e55c8a7271e/machines/36"
        }
      },
      "name": "splunk-724-w12",
      "overallState": "Complete",
      "patchStates": [
        {
          "bulletinId": "MS20-02-AFP-4537759",
          "finishedOn": "2020-05-08T13:34:54.6",
          "hasExecuted": true,
          "kb": "Q4537759",
          "lastUpdated": "2020-05-08T13:34:54.6",
          "nativeCode": 0,
          "overallState": "Complete",
          "overallStateDescription": "Complete",
          "patchId": "00030eb2-0000-0000-0000-000000000000",
          "scheduledOn": "2020-05-08T06:33:40.47",
          "startedOn": "2020-05-08T13:34:42.463",
          "status": "VerifiedFixed",
          "statusDescription": "Successfully installed"
        }
      ],
      "statusDescription": "Finished"
    }
  ]
}

```

#### Get Patch Details

This action is used to retrieve information about a patch from Ivanti Security Controls.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|integer|None|True|The vulnerability ID|None|4693|

Example input:

```
{
  "id": 4693
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|patch|vulnerability|True|Detailed information about a patch|

Example output:

```
{
  "patch": {
    "bulletinId": "MS15-022",
    "cve": [
      "CVE-2015-0085",
      "CVE-2015-0097"
    ],
    "id": 5033,
    "isSupported": true,
    "kb": "Q2920812",
    "links": {
      "self": {
        "href": "https://example.com:3121/st/console/api/v1.0/patches/5033"
      }
    },
    "patchIds": [
      "0000df6d-0000-0000-0000-000000000000",
      "0000dfb5-0000-0000-0000-000000000000",
      "0000dfd4-0000-0000-0000-000000000000"
    ],
    "patchType": "SecurityPatch",
    "releaseDate": "2015-03-10T00:00:00",
    "replacedBy": []
  }
}
```

#### Search Patches

This action is used to find and display detailed information about patch.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|security_id|[]string|None|True|Security Vulnerability ID|None|["MS99-031", "Q240346", "CVE-2015-4485", "4693"]|

Example input:

```
{
  "security_id": [
    "MS99-031",
    "Q240346",
    "CVE-2015-4485",
    "4693"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|vulnerabilities|[]vulnerability|True|Details about an agent|

Example output:

```
{
  "vulnerabilities": [
    {
      "bulletinId": "MS15-022",
      "cve": [
        "CVE-2015-0085",
        "CVE-2015-0097"
      ],
      "id": 5033,
      "isSupported": true,
      "kb": "Q2920812",
      "links": {
        "self": {
          "href": "https://example.com:3121/st/console/api/v1.0/patches/5033"
        }
      },
      "patchIds": [
        "0000df6d-0000-0000-0000-000000000000",
        "0000dfb5-0000-0000-0000-000000000000",
        "0000dfd4-0000-0000-0000-000000000000"
      ],
      "patchType": "SecurityPatch",
      "releaseDate": "2015-03-10T00:00:00",
      "replacedBy": []
    }
  ]
}
```

#### Start a Patch Scan

This action is used to start a patch scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credential_id|string|None|False|Credential ID|None|01234567-89AB-CDEF-0123-456789ABCDEF|
|diagnostic_trace_enabled|boolean|None|False|An indication whether diagnostics tracing should be enabled during scan|None|False|
|hostnames|[]string|None|False|Hostnames - Either hostnames or machine group IDs must be specified|None|hostname-1|
|machine_group_ids|[]string|None|False|List of machine groups to scan. Either hostnames or machine group IDs must be specified|None|["1", "2"]|
|max_poll_time|integer|300|True|Max poll time|None|300|
|name|string|None|False|Name to be given to scan|None|test-scan|
|run_as_credential_id|string|None|False|Reference to a credential to use to start a scan. Overwrites RunAsDefault behavior|None|01234567-89AB-CDEF-0123-456789ABCDEF|
|template_id|string|None|True|Patch scan template ID|None|01234567-89AB-CDEF-0123-456789ABCDEF|
|use_machine_credential|boolean|None|False|An indication whether to use machine credentials. If No is specified, then either group-level credentials, default credentials or integrated Windows authentication credentials (in that order) will be used. This parameter is only used if an endpoint name is specified|None|False|

Example input:

```
{
  "credential_id": "01234567-89AB-CDEF-0123-456789ABCDEF",
  "diagnostic_trace_enabled": false,
  "hostnames": "hostname-1",
  "machine_group_ids": [
    "1",
    "2"
  ],
  "max_poll_time": 300,
  "name": "test-scan",
  "run_as_credential_id": "01234567-89AB-CDEF-0123-456789ABCDEF",
  "template_id": "01234567-89AB-CDEF-0123-456789ABCDEF",
  "use_machine_credential": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_details|scan_details|True|Scan details|

Example output:

```
{
  "scan_details": {
    "links": {
      "self": {
        "href": "https://localhost:3121/st/con..."
      }
    },
    "name": "",
    "scanType": "Patch",
    "startedOn": "2020-05-13T14:42:33.0044884Z",
    "updatedOn": "2020-05-13T14:42:33.0044884Z",
    "user": "NT AUTHORITY\\SYSTEM",
    "id": "01234567-89AB-CDEF-0123-456789ABCDEF",
    "isComplete": false
  }
}
```

#### Get Scanned Machine Details

This action is used to get scanned machine details.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|True|Hostname|None|hostname-1|
|scan_id|string|None|True|Scan ID|None|01234567-89AB-CDEF-0123-456789ABCDEF|

Example input:

```
{
  "hostname": "hostname-1",
  "scan_id": "01234567-89AB-CDEF-0123-456789ABCDEF"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|detected_patches|[]detected_patch|True|Detected patches|
|patch_scan_machine|patch_scan_machine|True|Patch scan machine|

Example output:

```
{
  "patch_scan_status_details": {
    "consoleName": "hostname-1",
    "definitionDate": "2020-05-07T22:31:23.48",
    "expectedResultTotal": 1,
    "id": "f447bd51-de32-4bd6-a28e-ad834694d5ac",
    "isComplete": true,
    "links": {
      "machines": {
        "href": "https://localhost:3121/st/con..."
      },
      "self": {
        "href": "https://localhost:3121/st/con..."
      },
      "template": {
        "href": "https://localhost:3121/st/con..."
      }
    },
    "name": "API - ivanti-w16",
    "receivedResultCount": 1,
    "scanType": "Patch",
    "startedOn": "2020-05-12T21:53:55.28Z",
    "definitionVersion": "2.0.3.275",
    "updatedOn": "2020-05-12T21:53:57.78Z",
    "user": "WORKGROUP\\IVANTI-W16$"
  }
}
```

#### Get Patch Scan Status

This action is used to get patch scan status.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|Scan ID|None|01234567-89AB-CDEF-0123-456789ABCDEF|

Example input:

```
{
  "scan_id": "01234567-89AB-CDEF-0123-456789ABCDEF"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|patch_scan_status_details|patch_scan_status_details|True|Patch scan status details|

Example output:

```
{
  "detected_patches": [
    {
      "bulletinId": "MSNS18-05-4132216",
      "cultureName": "en-US",
      "kb": "Q4132216",
      "links": {
        "download": {
          "href": "https://localhost:3121/st/console/api/v1.0/patch/downloads/0001e03b-0000-0000-0000-000000000000?culture=en-US"
        }
      },
      "patchId": "0001e03b-0000-0000-0000-000000000000",
      "patchType": "SecurityPatch",
      "productId": "00003f1f-0000-0000-0000-000000000000",
      "productName": "Windows Server 2016 Standard",
      "scanItemId": 1100,
      "scanState": "FoundPatch",
      "servicePackName": "1607",
      "vendorSeverity": "Critical"
    },
    {
      "bulletinId": "MS18-11-SSU-4465659",
      "cultureName": "en-US",
      "kb": "Q4465659",
      "links": {
        "download": {
          "href": "https://localhost.com:3121/st/console/api/v1.0/patch/downloads/0001f77f-0000-0000-0000-000000000000?culture=en-US"
        }
      },
      "patchId": "0001f77f-0000-0000-0000-000000000000",
      "patchType": "SecurityPatch",
      "productId": "00003f1f-0000-0000-0000-000000000000",
      "productName": "Windows Server 2016 Standard",
      "scanItemId": 1101,
      "scanState": "FoundPatch",
      "servicePackName": "1607",
      "vendorSeverity": "Critical"
    }
  ],
  "patch_scan_machine": {
        "completedOn": "2020-05-12T21:53:57.71Z",
        "domain": "WORKGROUP",
        "errorNumber": 0,
        "id": 72,
        "installedPatchCount": 16,
        "links": {
          "patches": {
            "href": "https://localhost:3121/st/console/api/v1.0/patch/scans/f447bd51-de32-4bd6-a28e-ad834694d5ac/machines/72/patches"
          }
        },
        "missingPatchCount": 3,
        "missingServicePackCount": 1,
        "name": "hostname-1"
  }
}
```

#### Get Agents

This action is used to retrieve Agent from Ivanti Security Controls.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_configuration_filter|string|All|False|Filters agents based on listening configuration|['Listening', 'Not Listening', 'All']|All|
|name_filter|string|None|False|Filters agents where host or DNS name equals this value|None|hostname-1|

Example input:

```
{
  "agent_configuration_filter": "All",
  "name_filter": "hostname-1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents|[]agent_detail|False|List of agent details|
|count|integer|False|Number of agents returned|

Example output:

```
{
  "agents": [
    {
      "agentId": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD",
      "assignedPolicyId": "6b98cab4-1da7-4a4a-827b-bfd303e4c813",
      "domain": "WORKGROUP",
      "frameworkVersion": "9.4.34534.0",
      "isListening": false,
      "lastCheckIn": "2020-04-28T19:02:20.473",
      "links": {
        "checkin": {
          "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/checkin"
        },
        "queuedTasks": {
          "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/queuedTask"
        },
        "self": {
          "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
        },
        "status": {
          "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/status"
        },
        "tasks": {
          "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/tasks"
        }
      },
      "machineName": "hostname-1",
      "reportedPolicyId": "6b98cab4-1da7-4a4a-827b-bfd303e4c813",
      "status": "Installed"
    }
  ],
  "count": 1
}
```

#### Get Agent Status

This action is used to retrieve Agent Status from Ivanti Security Controls.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Agent Identifier|None|ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD|

Example input:

```
{
  "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent_status|agent_status|True|Agent status with details|

Example output:

```
{
  "agent_status": {
    "agentId": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD",
    "frameworkVersion": {
      "build": 34534,
      "major": 9,
      "majorRevision": 0,
      "minor": 4,
      "minorRevision": 0,
      "revision": 0
    },
    "installedPackages": [
      "AGENTASSET64"
    ],
    "lastCheckIn": "2020-04-28T15:05:48.1909093Z",
    "links": {
      "self": {
        "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
      }
    },
    "machineName": "iase-win10",
    "reportedOn": "2020-04-28T19:28:19.5756267Z",
    "runningPolicyId": "916f3bae-1667-4354-8203-234309e31e00",
    "runningPolicyVersion": 18005
  }
}
```

#### Get Agent

This action is used to retrieve Agent from Ivanti Security Controls.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Agent Identifier|None|ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD|

Example input:

```
{
  "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent_detail|True|Details about an agent|

Example output:

```
{
  "agent": {
    "agentId": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD",
    "assignedPolicyId": "6b98cab4-1da7-4a4a-827b-bfd303e4c813",
    "domain": "WORKGROUP",
    "frameworkVersion": "9.4.34534.0",
    "isListening": false,
    "lastCheckIn": "2020-04-28T19:02:20.473",
    "links": {
      "checkin": {
        "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/checkin"
      },
      "queuedTasks": {
        "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/queuedTask"
      },
      "self": {
        "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
      },
      "status": {
        "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/status"
      },
      "tasks": {
        "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/tasks"
      }
    },
    "machineName": "splunk-724-w12",
    "reportedPolicyId": "6b98cab4-1da7-4a4a-827b-bfd303e4c813",
    "status": "Installed"
  }
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### agent_detail

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent ID|string|True|The agent ID|
|Assigned Policy ID|string|False|The unique identifier of the policy that is in effect for this agent|
|DNS Name|string|False|The DNS name of the agent machine|
|Domain|string|False|The domain of the agent machine|
|Framework Version|string|False|The installed agent framework version|
|Is Listening|boolean|False|Specifies if the agent is a listening agent|
|Last Check-In|string|False|The date and time of the most recent check-in|
|Last Known IP Address|string|False|The last known IP address of the agent machine|
|Agent Links|object|False|Shows the related URLs for the agent|
|Listening Port|integer|False|The listening port number|
|Machine Name|string|False|The agent machine's host name|
|Reported Policy ID|string|False|The agent policy ID|
|Status|string|True|The current status of the agent|

#### agent_status

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent ID|string|True|The agent ID|
|Framework Version|object|False|The installed agent framework version|
|Installed Packages|[]string|False|The list of engines installed on the agent machine|
|Last Check-In|string|False|The date and time of the most recent check-in|
|Agent Links|object|False|Shows the related URLs for the agent|
|Machine Name|string|False|The agent machine's host name|
|Reported On|string|False|The time the information was gathered from the agent machine|
|Running Policy ID|string|False|The agent's running policy ID|
|Running Policy Version|integer|False|The agent's policy ID|

#### detected_patch

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Bulletin ID|string|True|Bulletin ID|
|Culture Name|string|True|Culture Name|
|KB|string|True|KB issued by the vendor of the patch|
|Links|object|False|Shows the related URLs|
|Patch ID|string|True|Patch ID|
|Patch Type|string|True|Patch Type|
|Product ID|string|True|Product ID|
|Product Name|string|True|Product name|
|Scan Item ID|integer|True|Scan ID of the patch summary|
|Scan State|string|True|The state of the patch installation|
|Service Pack Name|string|True|The name of the service pack to which the patch applies|
|Vendor Severity|string|True|The vendor-defined severity of the security risk or issue that this patch corrects.|

#### patch_scan_machine

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Completed On|string|False|The date and time that the machine assessment was completed|
|Domain|string|False|The domain short-name of the assessed machine|
|Error Description|string|False|Description of the patch scan or resolution error|
|Error Number|integer|False|An error code representing a resolution or assessment failure|
|ID|integer|False|The unique identifier of the machine patch assessment|
|Installed Patch Count|integer|False|The total number of installed patches found in the assessment|
|Links|object|False|Shows the related URLs|
|Missing Patch Count|integer|False|The total number of missing patches detected in the assessment|
|Missing Service Pack Count|integer|False|The total number of missing service packs detected in the assessment|
|Host Name|string|False|The resolved short-name or host name of the machine|
|Virtual Machine Path|string|False|The virtual machine path if this is a hosted VM|
|Virtual Server|string|False|The virtual machine server name if this is a hosted VM|

#### patch_scan_status_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Console Name|string|True|Console Name|
|Definition Date|string|False|Definition Date|
|Definition Version|string|False|Definition version|
|Expected Result Total|integer|True|Expected result total count|
|Scan ID|string|True|Scan ID|
|Is Complete|boolean|True|Is Complete|
|Links|object|True|Scan links|
|Scan Name|string|True|Scan name|
|Received Result Count|integer|True|Received result count|
|Scan Type|string|True|Scan Type|
|Scan Start Time|string|True|Scan start time|
|Update Time|string|True|Update Time|
|Username|string|True|Username|

#### scan_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Scan ID|string|True|Scan ID|
|Is Complete|boolean|True|Is complete|
|Scan Links|object|True|Scan links|
|Scan Name|string|False|Scan name|
|Scan Type|string|True|Scan Type|
|Scan Start Time|string|True|Scan start time|
|Update Time|string|True|Update Time|
|Username|string|True|Username|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.4.0 - New actions Get Patch Deployment Template ID, Start Patch Deployment
* 1.2.1 - Added session credentials and changed polling method for Start Patch Scan
* 1.2.0 - New actions Get Patch Deployment, Get Patch Details and Search Patches
* 1.1.0 - Add actions Start Patch Scan, Get Patch Scan Status and Get Scanned Machine Details
* 1.0.1 - Fix issue where Get Agents action does not include filters during paging
* 1.0.0 - Initial plugin

# Links

## References

* [Ivanti Security Controls](https://www.ivanti.com/products/security-controls)
* [Ivanti Security Controls API Documentation](https://help.ivanti.com/iv/help/en_US/isec/API/Topics/Welcome.htm)
