# Description

Ivanti Security Controls is a unified IT management platform used for managing and protecting through Patch Management, Application Control, and Asset Inventory functionality

# Key Features

* Ability to retrieve Ivanti Security Controls known agents
* Ability to check agent status

# Requirements

* Ivanti Security Controls 2019.3 (Build: 9.4.34544) or later
* Ivanti Security Controls host and API port (default: 3121)
* Username and password of Windows account where Ivanti Security Controls is installed
* (Recommended) Ivanti Security Controls certificate in order to enforce certificate verification

# Supported Product Versions

* 2024-11-1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|None|None|
|host|string|None|True|Enter the hostname|None|example.com|None|None|
|port|integer|3121|True|Enter the port|None|3121|None|None|
|ssl_verify|boolean|True|True|Validate certificate|None|True|None|None|

Example input:

```
{
  "credentials": {
    "password": "mypassword",
    "username": "user1"
  },
  "host": "example.com",
  "port": 3121,
  "ssl_verify": true
}
```

## Technical Details

### Actions


#### Create Patch Group

This action is used to create a new patch group with CVEs

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cves|[]string|None|True|The CVEs that should be included in the new patch group|None|["cve-2019-0701", "CVE-2019-0708"]|None|None|
|name|string|None|True|The name of the new patch group|None|New Patch Group|None|None|
|path|string|None|False|The path that describes the location of the patch group within the Patch Templates and Groups list in the navigation pane|None|Lab\Servers|None|None|
  
Example input:

```
{
  "cves": [
    "cve-2019-0701",
    "CVE-2019-0708"
  ],
  "name": "New Patch Group",
  "path": "Lab\\Servers"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|patch_group|patch_group|True|Detailed information about the patch group|None|
  
Example output:

```
{
  "patch_group": {
    "id": 10,
    "links": {
      "self": {
        "href": "https://example.com:3121/st/console/api/v1.0/patch/groups/10"
      },
      "patches": {
        "href": "https://example.com:3121/st/console/api/v1.0/patch/groups/10/patches"
      },
      "usedby": {
        "href": "https://example.com:3121/st/console/api/v1.0/patch/groups/10/usedby"
      }
    },
    "name": "example-patch-group"
  }
}
```

#### Create Patch Scan Template

This action is used to create a new patch scan template

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Description that explains the purpose of this patch scan template|None|Patch Scan Template created from InsightConnect|None|None|
|name|string|None|True|Name of the patch scan template|None|ExamplePatchScanTemplate|None|None|
|patchGroupIds|[]integer|None|True|The IDs of the patch groups to use|None|1|None|None|
|path|string|None|False|Path to the location of the machine group within the Patch Scan Templates list in the navigation pane|None|Lab\Servers|None|None|
|threadCount|integer|None|False|Specifies maximum number of machines that can be simultaneously scanned during one patch scan|None|1|None|None|
  
Example input:

```
{
  "description": "Patch Scan Template created from InsightConnect",
  "name": "ExamplePatchScanTemplate",
  "patchGroupIds": 1,
  "path": "Lab\\Servers",
  "threadCount": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|patch_scan_template|patch_scan_template|True|Detailed information about the patch scan template|None|
  
Example output:

```
{
  "patch_scan_template": {
    "creator": "IVANTI-W16\\Administrator",
    "description": "Example Patch Scan Templete Description",
    "id": "4374292d-3465-4d77-b752-c4eccd91bba5",
    "isSystem": false,
    "links": {
      "self": {
        "href": "https://example.com:3121/st/console/api/v1.0/patch/scanTemplates/4374292d-3465-4d77-b752-c4eccd91bba5"
      },
      "usedby": {
        "href": "https://example.com:3121/st/console/api/v1.0/patch/scanTemplates/4374292d-3465-4d77-b752-c4eccd91bba5/usedby"
      }
    },
    "name": "example-patch-scan-template",
    "patchFilter": {
      "patchGroupFilterType": "Scan",
      "patchGroupIds": [
        2,
        3
      ],
      "patchPropertyFilter": {
        "customActions": false,
        "nonSecurityPatchSeverities": "None",
        "securityPatchSeverities": "None",
        "securityTools": false
      },
      "scanFor": "NecessaryExplicitlyInstalled",
      "softwareDistribution": false,
      "vendorFamilyProductFilter": {}
    }
  }
}
```

#### Get Patch Deployment

This action is used to retrieve information about a specific patch deployment

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deployment_id|string|None|True|Patch deployment ID|None|5dbcb89f-eec3-4182-a9aa-1e6074fb0acb|None|None|
|machine_id|integer|None|False|ID of a machine involved with a specific patch deployment|None|7|None|None|
  
Example input:

```
{
  "deployment_id": "5dbcb89f-eec3-4182-a9aa-1e6074fb0acb",
  "machine_id": 7
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine_information|machine_deploy_state|True|Information about a machine involved with the patch deployment|None|
|patch_deployment_details|patch_deployment|True|Detailed information about a specific deployment|None|
  
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

#### Get Patch Deployment Template ID

This action is used to get a Patch Deployment Template ID by searching for the Patch Deployment Template Name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|patch_deployment_template_name|string|None|True|The name of the patch deployment template|None|Patch Deployment Template created from InsightConnect|None|None|
  
Example input:

```
{
  "patch_deployment_template_name": "Patch Deployment Template created from InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|patch_deployment_template_id|string|True|The ID of the patch deployment template|01234567-89AB-CDEF-0123-456789ABCDEF|
  
Example output:

```
{
  "patch_deployment_template_id": "01234567-89AB-CDEF-0123-456789ABCDEF"
}
```

#### Get Patch Details

This action is used to retrieve information about a patch from Ivanti Security Controls.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|The vulnerability ID|None|4693|None|None|
  
Example input:

```
{
  "id": 4693
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|patch|vulnerability|True|Detailed information about a patch|None|
  
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

This action is used to find and display detailed information about patch

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|security_id|[]string|None|True|Security Vulnerability ID|None|["MS99-031", "Q240346", "CVE-2015-4485", "4693"]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerabilities|[]vulnerability|True|Details about an agent|None|
  
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

#### Start Patch Deployment

This action is used to start a patch deployment. It accepts a scan and template by ID or by name.

Note that scan names are not unique in Ivanti, in the event that there are duplicate names, the action will automatically use the latest scan. If you want a specific scan that is not the latest, pass in the scan ID instead.


##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|download_patches|boolean|None|True|Boolean to initiate patch download before starting the deployment|None|False|None|None|
|scan_identifier|string|None|True|A scan ID or scan name|None|01234567-89AB-CDEF-0123-456789ABCDEF|None|None|
|template_identifier|string|None|True|A template ID or template name|None|Deployment Template created from InsightConnect|None|None|
  
Example input:

```
{
  "download_patches": false,
  "scan_identifier": "01234567-89AB-CDEF-0123-456789ABCDEF",
  "template_identifier": "Deployment Template created from InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Start a Patch Scan

This action is used to start a patch scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credential_id|string|None|False|Credential ID|None|01234567-89AB-CDEF-0123-456789ABCDEF|None|None|
|diagnostic_trace_enabled|boolean|None|False|An indication whether diagnostics tracing should be enabled during scan|None|False|None|None|
|hostnames|[]string|None|False|Hostnames - Either hostnames or machine group IDs must be specified|None|hostname-1|None|None|
|machine_group_ids|[]string|None|False|List of machine groups to scan. Either hostnames or machine group IDs must be specified|None|["1", "2"]|None|None|
|max_poll_time|integer|300|True|Max poll time|None|300|None|None|
|name|string|None|False|Name to be given to scan|None|test-scan|None|None|
|run_as_credential_id|string|None|False|Reference to a credential to use to start a scan. Overwrites RunAsDefault behavior|None|01234567-89AB-CDEF-0123-456789ABCDEF|None|None|
|template_id|string|None|True|Patch scan template ID|None|01234567-89AB-CDEF-0123-456789ABCDEF|None|None|
|use_machine_credential|boolean|None|False|An indication whether to use machine credentials. If No is specified, then either group-level credentials, default credentials or integrated Windows authentication credentials (in that order) will be used. This parameter is only used if an endpoint name is specified|None|False|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan_details|scan_details|True|Scan details|None|
  
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

#### Update Patch Group

This action is used to add CVEs or Patch IDs to an existing patch group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|patch_group|string|None|True|Name or ID of an existing patch group|None|Patch Group created from InsightConnect|None|None|
|vulnerability_identifier|[]string|None|True|List of patch IDs or CVEs to add to an existing patch group|None|["CVE-2019-0708", "12345"]|None|None|
  
Example input:

```
{
  "patch_group": "Patch Group created from InsightConnect",
  "vulnerability_identifier": [
    "CVE-2019-0708",
    "12345"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
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
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**agent_detail**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent ID|string|None|True|The agent ID|None|
|Assigned Policy ID|string|None|False|The unique identifier of the policy that is in effect for this agent|None|
|DNS Name|string|None|False|The DNS name of the agent machine|None|
|Domain|string|None|False|The domain of the agent machine|None|
|Framework Version|string|None|False|The installed agent framework version|None|
|Is Listening|boolean|None|False|Specifies if the agent is a listening agent|None|
|Last Check-In|string|None|False|The date and time of the most recent check-in|None|
|Last Known IP Address|string|None|False|The last known IP address of the agent machine|None|
|Agent Links|object|None|False|Shows the related URLs for the agent|None|
|Listening Port|integer|None|False|The listening port number|None|
|Machine Name|string|None|False|The agent machine's host name|None|
|Reported Policy ID|string|None|False|The agent policy ID|None|
|Status|string|None|True|The current status of the agent|None|
  
**agent_status**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent ID|string|None|True|The agent ID|None|
|Framework Version|object|None|False|The installed agent framework version|None|
|Installed Packages|[]string|None|False|The list of engines installed on the agent machine|None|
|Last Check-In|string|None|False|The date and time of the most recent check-in|None|
|Agent Links|object|None|False|Shows the related URLs for the agent|None|
|Machine Name|string|None|False|The agent machine's host name|None|
|Reported On|string|None|False|The time the information was gathered from the agent machine|None|
|Running Policy ID|string|None|False|The agent's running policy ID|None|
|Running Policy Version|integer|None|False|The agent's policy ID|None|
  
**patch_scan_machine**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Completed On|string|None|False|The date and time that the machine assessment was completed|None|
|Domain|string|None|False|The domain short-name of the assessed machine|None|
|Error Description|string|None|False|Description of the patch scan or resolution error|None|
|Error Number|integer|None|False|An error code representing a resolution or assessment failure|None|
|ID|integer|None|False|The unique identifier of the machine patch assessment|None|
|Installed Patch Count|integer|None|False|The total number of installed patches found in the assessment|None|
|Links|object|None|False|Shows the related URLs|None|
|Missing Patch Count|integer|None|False|The total number of missing patches detected in the assessment|None|
|Missing Service Pack Count|integer|None|False|The total number of missing service packs detected in the assessment|None|
|Host Name|string|None|False|The resolved short-name or host name of the machine|None|
|Virtual Machine Path|string|None|False|The virtual machine path if this is a hosted VM|None|
|Virtual Server|string|None|False|The virtual machine server name if this is a hosted VM|None|
  
**scan_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Scan ID|string|None|True|Scan ID|None|
|Is Complete|boolean|None|True|Is complete|None|
|Scan Links|object|None|True|Scan links|None|
|Scan Name|string|None|False|Scan name|None|
|Scan Type|string|None|True|Scan Type|None|
|Scan Start Time|string|None|True|Scan start time|None|
|Update Time|string|None|True|Update Time|None|
|Username|string|None|True|Username|None|
  
**patch_scan_status_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Console Name|string|None|True|Console Name|None|
|Definition Date|string|None|False|Definition Date|None|
|Definition Version|string|None|False|Definition version|None|
|Expected Result Total|integer|None|True|Expected result total count|None|
|Scan ID|string|None|True|Scan ID|None|
|Is Complete|boolean|None|True|Is Complete|None|
|Links|object|None|True|Scan links|None|
|Scan Name|string|None|True|Scan name|None|
|Received Result Count|integer|None|True|Received result count|None|
|Scan Type|string|None|True|Scan Type|None|
|Scan Start Time|string|None|True|Scan start time|None|
|Update Time|string|None|True|Update time|None|
|Username|string|None|True|Username|None|
  
**detected_patch**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Bulletin ID|string|None|True|Bulletin ID|None|
|Culture Name|string|None|True|Culture name|None|
|KB|string|None|True|KB issued by the vendor of the patch|None|
|Links|object|None|False|Shows the related URLs|None|
|Patch ID|string|None|True|Patch ID|None|
|Patch Type|string|None|True|Patch Type|None|
|Product ID|string|None|True|Product ID|None|
|Product Name|string|None|True|Product name|None|
|Scan Item ID|integer|None|True|Scan ID of the patch summary|None|
|Scan State|string|None|True|The state of the patch installation|None|
|Service Pack Name|string|None|True|The name of the service pack to which the patch applies|None|
|Vendor Severity|string|None|True|The vendor-defined severity of the security risk or issue that this patch corrects|None|
  
**next**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|False|Href|None|
  
**links**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Next|next|None|False|Next|None|
  
**links_self**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Self|next|None|False|Self|None|
  
**vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Bulletin ID|string|None|False|Bulletinid|None|
|CVE|[]string|None|False|CVE|None|
|Patch ID|integer|None|False|Id|None|
|Is Supported|boolean|None|False|Issupported|None|
|Kb|string|None|False|Kb|None|
|Links|links_self|None|False|Links|None|
|Patchids|[]string|None|False|Patch IDs|None|
|Patchtype|string|None|False|Patch Type|None|
|Releasedate|string|None|False|Release Date|None|
|Replaced By|[]string|None|False|Replacedby|None|
  
**patch_deployment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Completed Machine Count|integer|None|False|Number of machines that has the deployment completed|None|
|Creator|string|None|False|Initiator of the deployment|None|
|Expected Machine Count|integer|None|False|Number of machines in this deployment|None|
|ID|string|None|True|The unique operation identifier assigned to the patch deployment|None|
|Completed|boolean|None|False|Completion status of the deployment|None|
|Last Updated On|string|None|False|Date of receipt of the last status update|None|
|Links|object|None|False|Shows the related URLs for the deployment, the machines and the template|None|
|Name|string|None|False|Name of the deployment template|None|
|Started On|string|None|False|Deployment start date|None|
  
**machine_deploy_state**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Address|string|None|False|The IP address of the machine|None|
|Completed Patches|integer|None|False|The count of in-progress patches|None|
|DNS Name|string|None|False|The DNS name of the machine|None|
|Domain|string|None|False|The domain name of the machine|None|
|Error Code|integer|None|False|The error code reported on failure by the machine|None|
|ID|integer|None|False|The unique machine identifier for the machine being deployed to|None|
|Last Updated|string|None|False|Specifies when the deployment status was last updated|None|
|Links|object|None|False|Shows the related URL for the deployment to the machine|None|
|Name|string|None|False|The hostname of the machine|None|
|Overall State|string|None|False|The overall state of the machine deployment|None|
|Patch States|[]object|None|False|The status of each patch in the deployment|None|
|Status Description|string|None|False|A description of the status of the deployment|None|
  
**patch_property_filter**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Custom Actions|boolean|None|False|Custom actions|None|
|Non Security Patch Severities|string|None|False|The non-security patch severities|None|
|Security Patch Severities|string|None|False|The security patch severities|None|
|Security Tools|boolean|None|False|Security tools|None|
  
**patch_filter**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Patch File Path|string|None|False|The patch file path|None|
|Patch Group Filter Type|string|None|False|The patch's filter describes how this filter will be applied. The values can be Scan, Skip, or None|None|
|Patch Group IDs|[]integer|None|False|The IDs of the patch groups to use|None|
|Patch Property Filter|patch_property_filter|None|False|Patch property filter (security, non-security, critical, etc.)|None|
|Scan For|string|None|False|Gets or sets the type of patches to scan for|None|
|Software Distribution|boolean|None|False|Is software distribution included in the scan|None|
|Vendor Family Product Filter|object|None|False|Vendor and family product hierarchy|None|
  
**patch_scan_template**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Creator|string|None|False|The name of the person who created the template|None|
|Description|string|None|False|Provides a description that explains the purpose of this patch scan template|None|
|ID|string|None|False|Specifies the ID of the patch scan template|None|
|Is System|boolean|None|False|Indicates if this is a system template|None|
|Links|object|None|False|Shows the related URLs for each patch scan template and for the usedby list|None|
|Name|string|None|False|Specifies the patch scan template name|None|
|Patch Filter|patch_filter|None|False|Specifies the mode|None|
|Path|string|None|False|The path that describes the location of the machine group within the Patch Scan Templates list in the navigation pane|None|
|Thread Count|integer|None|False|Specifies maximum number of machines that can be simultaneously scanned during one patch scan|None|
  
**patch_group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|The patch group ID|None|
|Links|object|None|False|Shows the related URLs for the patch group|None|
|Name|string|None|False|The name of the patch group|None|
|Path|string|None|False|The path that describes the location of the patch group within the Windows Patch Groups list in the navigation pane|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.5.1 - Bumping requirements.txt | SDK bump to 6.1.4
* 1.5.0 - New action Update Patch Group
* 1.4.0 - New actions Get Patch Deployment Template ID, Start Patch Deployment
* 1.3.0 - New actions Create Patch Group and Add CVEs, Create Patch Scan Template
* 1.2.1 - Added session credentials and changed polling method for Start Patch Scan
* 1.2.0 - New actions Get Patch Deployment, Get Patch Details and Search Patches
* 1.1.0 - Add actions Start Patch Scan, Get Patch Scan Status and Get Scanned Machine Details
* 1.0.1 - Fix issue where Get Agents action does not include filters during paging
* 1.0.0 - Initial plugin

# Links

* [Ivanti Security Controls](https://www.ivanti.com/products/security-controls)

## References

* [Ivanti Security Controls API Documentation](https://help.ivanti.com/iv/help/en_US/isec/API/Topics/Welcome.htm)