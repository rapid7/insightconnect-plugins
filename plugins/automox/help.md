# Description

Automox is modernizing IT operations through cloud-native efficiency and upending the old ways of legacy on-premise 
tools. Keeping you continuously connected to all your endpoints, regardless of location, environment, and operating
system type. Now you can manage and apply operating system and third-party patches, enforce security configurations, 
deploy software, and execute any action across Windows, macOS, and Linux systems. 

Utilizing this plugin allows for the orchestration of IT operations such as device management, triggering remote 
outcomes on endpoints, and basic Automox platform administration. 

# Key Features

* Retrieve and manage Automox managed devices
* Manage Automox groups
* Initiate Vulnerability Sync uploads and remediation of issues
* Trigger workflows based on Automox platform events

# Requirements

* Automox API Key

# Supported Product Versions

* All as of 10/13/2023

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Organization API key|None|abc12345-abc1-2345-abc1-abc123456789|

Example input:

```
{
  "api_key": "abc12345-abc1-2345-abc1-abc123456789"
}
```

## Technical Details

### Actions


#### Upload Vulnerability Sync File

This action is used to upload a CSV file to vulnerability sync for processing.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|csv_file|bytes|None|True|Base64 encoded CSV data from which to create the vulnerability sync batch|None|PGgxPlJhcGlkNzwvaDE+|
|csv_file_name|string|https://example.com|False|Name for CSV file uploaded and shown within Automox|None|https://example.com|
|org_id|integer|None|True|Identifier of organization|None|1234|
|report_source|string|generic|False|The third-party source of the vulnerability report|['generic', 'crowd-strike', 'rapid7', 'tenable', 'qualys']|rapid7|

Example input:

```
{
  "csv_file": "PGgxPlJhcGlkNzwvaDE+",
  "csv_file_name": "insightconnect-uploaded-report.csv",
  "org_id": 1234,
  "report_source": "rapid7"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|Identifier of the vulnerability sync action set|
|status|string|True|Status of the vulnerability sync action set|

Example output:

```
{
  "$success": true,
  "id": 1234,
  "status": "building"
}
```

#### Update Group

This action is used to update an Automox group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|color|string|None|False|Automox console highlight color for the group. Value should be a valid Hex color code|None|#059F1D|
|group_id|integer|None|True|Identifier of the Automox group|None|1234|
|name|string|None|True|Name of the group|None|Group1|
|notes|string|None|False|Define notes for the group|None|Example notes go here|
|org_id|integer|None|False|Identifier of organization|None|1234|
|parent_server_group_id|integer|None|False|Name of the parent group. Defaults to Default Group ID if omitted|None|1234|
|policies|[]integer|None|False|List of policy IDs to assign to group|None|[1, 2, 3]|
|refresh_interval|integer|1440|True|Frequency of device refreshes in minutes|None|1440|

Example input:

```
{
  "color": "#059F1D",
  "group_id": 1234,
  "name": "Group1",
  "notes": "Example notes go here",
  "org_id": 1234,
  "parent_server_group_id": 1234,
  "policies": [
    1,
    2,
    3
  ],
  "refresh_interval": 1440
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "$success": true,
  "success": true
}
```

#### Update Device

This action is used to update Automox device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|custom_name|string|None|False|Custom name to set on device|None|custom-name|
|device_id|integer|None|True|Identifier of device|None|1234|
|exception|boolean|False|True|Exclude the device from reports and statistics|None|False|
|org_id|integer|None|False|Identifier of organization|None|1234|
|server_group_id|integer|None|False|Identifier of server group|None|1234|
|tags|[]string|None|False|List of tags|None|["tag1", "tag2"]|

Example input:

```
{
  "custom_name": "custom-name",
  "device_id": 1234,
  "exception": false,
  "org_id": 1234,
  "server_group_id": 1234,
  "tags": [
    "tag1",
    "tag2"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "$success": true,
  "success": true
}
```

#### Run Device Command

This action is used to run a command on a device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|command|string|None|True|Command to run on device|['GetOS', 'InstallUpdate', 'InstallAllUpdates', 'PolicyTest', 'PolicyRemediate', 'Reboot']|GetOS|
|device_id|integer|None|True|Identifier of device|None|1234|
|org_id|integer|None|False|Identifier of organization|None|1234|
|patches|[]string|None|False|List of patches to be installed by name (Note: this only works with the InstallUpdate command)|None|["Security Update (KB4549947)"]|
|policy_id|integer|None|False|Identifier of policy|None|1234|

Example input:

```
{
  "command": "GetOS",
  "device_id": 1234,
  "org_id": 1234,
  "patches": [
    "Security Update (KB4549947)"
  ],
  "policy_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "$success": true,
  "success": true
}
```

#### List Vulnerability Sync Action Sets

This action is used to retrieve list of vulnerability sync batches.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|configuration_id_equals|string|None|False|Filter by configuration ID|None|00000000-0000-0000-0000-000000000000|
|configuration_id_is_set|boolean|None|False|Filter based on whether the configuration ID is set|None|True|
|group_sort|string|None|False|Sort results by field|['asc', 'desc', 'latest_updated_at:asc', 'latest_updated_at:desc', 'source:asc', 'source:desc', '']|latest_updated_at:desc|
|include_all_runs_equals|boolean|None|False|Whether to include all runs in the response|None|True|
|org_id|integer|None|True|Identifier of organization|None|1234|
|sort|string|None|False|Sort results by field|['created_at', 'updated_at', 'status', 'source_type', 'source_name', 'configuration_id', '']|created_at|
|source_type_in|[]string|None|False|Filter by source type|None|["Generic Report", "CrowdStrike", "Rapid7", "TenableIO", "Qualys"]|
|status_in|[]string|None|False|Filter by status|None|["building", "ready", "error"]|
|status_not_in|[]string|None|False|Filter by status|None|["building", "ready", "error"]|

Example input:

```
{
  "configuration_id_equals": "00000000-0000-0000-0000-000000000000",
  "configuration_id_is_set": true,
  "group_sort": "latest_updated_at:desc",
  "include_all_runs_equals": true,
  "org_id": 1234,
  "sort": "created_at",
  "source_type_in": [
    "Generic Report",
    "CrowdStrike",
    "Rapid7",
    "TenableIO",
    "Qualys"
  ],
  "status_in": [
    "building",
    "ready",
    "error"
  ],
  "status_not_in": [
    "building",
    "ready",
    "error"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|action_sets|[]action_set|False|List of vulnerability sync action sets|

Example output:

```
{
  "$success": true,
  "action_sets": [
    {
      "created_at": "2023-10-10T03:45:26+0000",
      "created_by_user": {
        "email": "engineer@example.com",
        "firstname": "Engineer",
        "id": 1234,
        "lastname": "Example"
      },
      "id": 1234,
      "organization_id": 1234,
      "source": {
        "name": "insightconnect-uploaded-report.csv",
        "type": "generic"
      },
      "statistics": {
        "issues": {
          "unknown-host": {
            "count": 4
          }
        },
        "solutions": {
          "patch-with-worklet": {
            "count": 1,
            "device_count": 18,
            "vulnerability_count": 1
          }
        }
      },
      "status": "ready",
      "updated_at": "2023-10-10T03:45:30+0000",
      "updated_by_user": {
        "email": "engineer@example.com",
        "firstname": "Engineer",
        "id": 1234,
        "lastname": "Example"
      }
    }
  ]
}
```

#### List Vulnerability Sync Action Set Solutions

This action is used to retrieve a list of vulnerability sync remediations.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action_set_id|integer|None|True|Filter by action set identifier|None|1234|
|org_id|integer|None|True|Identifier of organization|None|1234|
|remediation_type_in|[]string|None|False|Filter by remediation type|None|["patch-now", "patch-with-worklet"]|
|severity_in|[]string|None|False|Filter by severity|None|["critical", "high", "medium", "low", "unknown"]|
|vulnerability_in|[]string|None|False|Filter by vulnerability|None|["CVE-2020-1234", "CVE-2020-5678"]|

Example input:

```
{
  "action_set_id": 1234,
  "org_id": 1234,
  "remediation_type_in": [
    "patch-now",
    "patch-with-worklet"
  ],
  "severity_in": [
    "critical",
    "high",
    "medium",
    "low",
    "unknown"
  ],
  "vulnerability_in": [
    "CVE-2020-1234",
    "CVE-2020-5678"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|solutions|[]solution|False|List of vulnerability sync Solutions|

Example output:

```
{
  "$success": true,
  "solutions": [
    {
      "device_ids": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18
      ],
      "devices": [
        {
          "custom_name": "Unknown",
          "id": 1,
          "ip_addrs_private": [
            "10.0.0.68",
            "fe80::98ad:4391:f22f:d3ae"
          ],
          "name": "demo-windows2019-0",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "id": 2,
          "ip_addrs_private": [
            "10.0.0.244",
            "fe80::6910:9c6e:8be4:7b35"
          ],
          "name": "demo-windows2019-3",
          "status": "timed_out"
        },
        {
          "custom_name": "ip-10-0-0-28",
          "id": 3,
          "ip_addrs_private": [
            "10.0.0.28",
            "fe80::9ddf:1baa:ef6f:32b8"
          ],
          "name": "ip-10-0-0-28",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "id": 4,
          "ip_addrs_private": [
            "10.0.0.209",
            "fe80::e112:6743:d6ba:aac"
          ],
          "name": "ip-10-0-0-209",
          "status": "timed_out"
        },
        {
          "custom_name": "ip-10-0-0-40",
          "id": 5,
          "ip_addrs_private": [
            "10.0.0.40",
            "fe80::f842:e66a:b80e:c396"
          ],
          "name": "ip-10-0-0-40",
          "status": "timed_out"
        },
        {
          "custom_name": "DESKTOP",
          "id": 6,
          "ip_addrs_private": [
            "10.0.0.133",
            "fe80::ad22:6aa1:6cf1:18b7"
          ],
          "name": "DESKTOP",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "id": 7,
          "ip_addrs_private": [
            "10.0.0.119",
            "fe80::b58e:5cd8:c618:3036"
          ],
          "name": "demo-windows2019-7",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "id": 8,
          "ip_addrs_private": [
            "10.0.0.116",
            "fe80::9871:3b0e:56c0:8ddc"
          ],
          "name": "demo-windows2019-2",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "id": 9,
          "ip_addrs_private": [
            "10.0.0.74",
            "fe80::9c8b:5ae8:6ce9:40d0"
          ],
          "name": "demo-windows2019-8",
          "status": "timed_out"
        },
        {
          "custom_name": "ip-10-0-0-22",
          "id": 10,
          "ip_addrs_private": [
            "10.0.0.22",
            "fe80::8008:8027:7533:c02d"
          ],
          "name": "ip-10-0-0-22",
          "status": "timed_out"
        },
        {
          "custom_name": "DESKTOP",
          "id": 11,
          "ip_addrs_private": [
            "10.0.0.14",
            "10.0.0.15",
            "169.254.178.151",
            "fe80::7894:fefd:f512:4af9",
            "fe80::cc6e:37c9:687d:3edc"
          ],
          "name": "DESKTOP",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "id": 12,
          "ip_addrs_private": [
            "10.0.0.173",
            "fe80::552:fc9b:fcad:3dbf"
          ],
          "name": "demo-windows2019-1",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "id": 13,
          "ip_addrs_private": [
            "10.0.0.160",
            "fe80::540c:5365:3ef2:56de"
          ],
          "name": "demo-windows2019-4",
          "status": "timed_out"
        },
        {
          "custom_name": "ip-10-0-0-227",
          "id": 14,
          "ip_addrs_private": [
            "10.0.0.227",
            "fe80::a1eb:2ed7:5d55:a009"
          ],
          "name": "ip-10-0-0-227",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "id": 15,
          "ip_addrs_private": [
            "10.0.0.6",
            "fe80::79ec:127f:8af1:2266"
          ],
          "name": "demo-windows2019-6",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "id": 16,
          "ip_addrs_private": [
            "10.0.0.214",
            "fe80::f5f3:b5b2:972c:b51f"
          ],
          "name": "demo-windows2019-5",
          "status": "timed_out"
        },
        {
          "custom_name": "ip-10-0-0-42",
          "id": 17,
          "ip_addrs_private": [
            "10.0.0.42",
            "fe80::18a5:516d:6c66:c516"
          ],
          "name": "ip-10-0-0-42",
          "status": "timed_out"
        },
        {
          "custom_name": "Unknown",
          "deleted": true,
          "id": 18,
          "ip_addrs_private": [
            "10.0.0.253",
            "fe80::e141:1176:a4e0:6093"
          ],
          "name": "demo-windows2019-9",
          "status": "timed_out"
        }
      ],
      "id": 1234,
      "organization_id": 1234,
      "remediation_type": "patch-with-worklet",
      "solution_type": "unmatched",
      "vulnerabilities": [
        {
          "id": "CVE-2021-24111",
          "severity": "high",
          "title": ".NET Framework Denial of Service Vulnerability"
        }
      ]
    }
  ]
}
```

#### List Vulnerability Sync Action Set Issues

This action is used to retrieve the issues identified for a specified vulnerability sync action set.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action_set_id|integer|None|True|Identifier of the action set|None|1234|
|issue_type_in|[]string|None|False|Filter by issue type|None|["unknown-host"]|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```
{
  "action_set_id": 1234,
  "issue_type_in": [
    "unknown-host"
  ],
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|[]action_set_issue|True|Issues associated with the specified vulnerability sync action_set|

Example output:

```
{
  "$success": true,
  "issues": [
    {
      "id": 1237,
      "issue_details": {
        "hostname": "win2016-demo"
      },
      "issue_type": "unknown-host"
    },
    {
      "id": 1236,
      "issue_details": {
        "hostname": "Win10-VM-1"
      },
      "issue_type": "unknown-host"
    },
    {
      "id": 1235,
      "issue_details": {
        "hostname": "windows2019-1"
      },
      "issue_type": "unknown-host"
    },
    {
      "id": 1234,
      "issue_details": {
        "hostname": "windows2019-0"
      },
      "issue_type": "unknown-host"
    }
  ]
}
```

#### List Policies

This action is used to retrieve Automox policies.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|org_id|integer|None|False|Identifier of organization to restrict results|None|1234|

Example input:

```
{
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|policies|[]policy|False|List of Automox policies|

Example output:

```
```

#### List Organizations

This action is used to retrieve Automox organizations.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|organizations|[]organization|True|List of Automox organizations|

Example output:

```
```

#### List Organization Users

This action is used to retrieve users of the Automox organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]user|False|List of Automox users|

Example output:

```
```

#### List Groups

This action is used to list Automox groups.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|org_id|integer|None|False|Identifier of organization to restrict results|None|1234|

Example input:

```
{
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|groups|[]group|False|List of Automox groups|

Example output:

```
```

#### Get Vulnerability Sync Action Set

This action is used to retrieve details for a specified vulnerability sync action set.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action_set_id|integer|None|True|Identifier of the action set|None|1234|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```
{
  "action_set_id": 1234,
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|action_set|action_set|True|Details of a specified vulnerability sync action_set|

Example output:

```
{
  "$success": true,
  "action_set": {
    "created_at": "2023-10-29T21:25:18+0000",
    "created_by_user": {
      "email": "engineer@example.com",
      "firstname": "Engineer",
      "id": 1234,
      "lastname": "Example"
    },
    "id": 1234,
    "organization_id": 1234,
    "source": {
      "name": "insightconnect-uploaded-report.csv",
      "type": "generic"
    },
    "status": "building",
    "updated_at": "2023-10-29T21:25:18+0000",
    "updated_by_user": {
      "email": "engineer@example.com",
      "firstname": "Engineer",
      "id": 1234,
      "lastname": "Example"
    }
  }
}
```

#### Get Device by IP Address

This action is used to find an Automox device by IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|IP address of device|None|https://example.com|
|org_id|integer|None|False|Identifier of organization to restrict results|None|1234|

Example input:

```
{
  "ip_address": "192.168.0.1",
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|device|device|False|The matched Automox device|

Example output:

```
```

#### Get Device by Hostname

This action is used to find an Automox device by hostname.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|True|Hostname of device|None|hostname-1|
|org_id|integer|None|False|Identifier of organization to restrict results|None|1234|

Example input:

```
{
  "hostname": "hostname-1",
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|device|device|False|The matched Automox device|

Example output:

```
```

#### Create Group

This action is used to create an Automox group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|color|string|None|False|Automox console highlight color for the group. Value should be a valid Hex color code|None|#059F1D|
|name|string|None|True|Name of the group|None|Group1|
|notes|string|None|False|Define notes for the group|None|Example notes go here|
|org_id|integer|None|False|Identifier of organization|None|1234|
|parent_server_group_id|integer|None|False|Name of the parent group. Defaults to Default Group ID if this is omitted|None|1234|
|policies|[]integer|None|False|List of policy IDs to assign to group|None|[1, 2, 3]|
|refresh_interval|integer|1440|True|Frequency of device refreshes in minutes|None|1440|

Example input:

```
{
  "color": "#059F1D",
  "name": "Group1",
  "notes": "Example notes go here",
  "org_id": 1234,
  "parent_server_group_id": 1234,
  "policies": [
    1,
    2,
    3
  ],
  "refresh_interval": 1440
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|group|group|True|Detailed information about the created group|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "$success": true,
  "group": {
    "id": 1234,
    "name": "InsightConnect",
    "organization": {
      "bill_overages": true,
      "billing_interval": "month",
      "billing_interval_count": 1,
      "create_time": "2022-06-03 20:22:52.261394",
      "id": 1234,
      "legacy_billing": true,
      "name": "InsightConnect",
      "rate_id": 1234,
      "sub_plan": "TIER3",
      "updated_at": "2022-06-03 20:22:52.261394",
      "uuid": "a4f7ceab-4bc2-4588-abe7-25af271f1156"
    },
    "organization_id": 1234,
    "parent_server_group_id": 1234,
    "refresh_interval": 1440
  },
  "success": true
}
```

#### Delete Device

This action is used to delete an Automox device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device_id|integer|None|True|Identifier of device|None|1234|
|org_id|integer|None|False|Identifier of organization|None|1234|

Example input:

```
{
  "device_id": 1234,
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "$success": true,
  "success": true
}
```

#### Delete Group

This action is used to delete an Automox group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_id|integer|None|True|Identifier of the Automox group|None|1234|
|org_id|integer|None|False|Identifier of organization|None|1234|

Example input:

```
{
  "group_id": 1234,
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "$success": true,
  "success": true
}
```

#### Delete Vulnerability Sync Action Set

This action is used to delete a vulnerability sync action set and all associated data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action_set_id|integer|None|True|Identifier of the action set|None|1234|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```
{
  "action_set_id": 1234,
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "$success": true,
  "success": true
}
```

#### Execute Vulnerability Sync Actions

This action is used to launch remediation for patch and worklet remediations.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action_set_id|integer|None|True|Identifier of the action set|None|1234|
|actions|[]action_set_action|None|True|List of remediations to execute|None|[None, None]|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "$success": true,
  "success": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|device|device|False|The matched Automox device|

Example output:

```
```

#### Get Device Software

This action is used to retrieve a list of software installed on a device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device_id|integer|None|True|Identifier of device|None|1234|
|org_id|integer|None|False|Identifier of organization|None|1234|

Example input:

```
{
  "device_id": 1234,
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|software|[]device_software|False|List of software on device|

Example output:

```
```

#### List Devices

This action is used to retrieve Automox managed devices.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_id|integer|None|False|Identifier of server group|None|1234|
|org_id|integer|None|False|Identifier of organization to restrict results|None|1234|

Example input:

```
{
  "group_id": 1234,
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|devices|[]device|False|List of Automox managed devices|

Example output:

```
```

### Triggers

#### Get Automox Events

This trigger is used to retrieve Automox events to trigger workflows.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event_type|string|None|True|Name of event type to be retrieved (list of event types found at https://developer.automox.com/openapi/axconsole/operation/getEvents/#!in=query&path=eventName&t=request)|None|https://example.com|
|org_id|integer|None|False|Identifier of organization to restrict results|None|1234|

Example input:

```
{
  "event_type": "user.login",
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|event|event|True|Event with details|

Example output:

```
```

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Fix Vulnerability Sync API Actions | Add Delete Vulnerability Sync Action Set action | Add Execute
  Vulnerability Sync Actions action | Add List Vulnerability Sync Action Set Issues
  action | Add List Vulnerability Sync Action Set Solutions action | Add List Vulnerability Sync Action Sets action |
  | Add Get Vulnerability Sync Action Set action | Update Upload Vulnerability Sync File action 
  | Update Get Devices action | Remove Action on Vulnerability Sync Batch | Remove Action on Vulnerability Sync Task
  | Remove Get Vulnerability Sync Batch | Remove List Vulnerability Sync Batches | Remove List Vulnerability Sync Tasks
* 1.2.0 - Get device by IP and Get device by hostname: fix validation issue when IP or hostname not found | Add unit
  tests
* 1.1.1 - Fix undefined org ID passed to actions when not required | Record outcome of connection tests
* 1.1.0 - Add `report source` as optional input parameter to Upload Vulnerability Sync File action | Add report source
  to batch type
* 1.0.0 - Initial plugin

# Links

* [Automox](https://www.automox.com/)

## References

* [Automox Developer Portal](https://developer.automox.com/)
* [Managing API Keys](https://support.automox.com/help/managing-keys)
* [Event Types for Get Automox Events action](https://developer.automox.com/openapi/axconsole/operation/getEvents/#!in=query&path=eventName&t=request)

