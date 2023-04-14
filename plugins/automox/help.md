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

* All as of 1/21/2022

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
  "success": true
}
```

#### Upload Vulnerability Sync File

This action is used to upload CSV file to vulnerability sync for processing.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|csv_file|bytes|None|True|Base64 encoded CSV data from which to create the vulnerability sync batch|None|PGgxPlJhcGlkNzwvaDE+|
|csv_file_name|string|insightconnect-uploaded-report.csv|False|Name for CSV file uploaded and shown within Automox|None|insightconnect-uploaded-report.csv|
|org_id|integer|None|True|Identifier of organization|None|1234|
|report_source|string|Generic Report|False|The third-party source of the vulnerability report|['Generic Report', 'CrowdStrike', 'Rapid7', 'TenableIO', 'Qualys']|Rapid7|

Example input:

```
{
  "csv_file": "PGgxPlJhcGlkNzwvaDE+",
  "csv_file_name": "insightconnect-uploaded-report.csv",
  "org_id": 1234,
  "report_source": "Rapid7"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|batch_id|integer|True|Identifier of vulnerability sync batch|

Example output:

```
{
  "batch_id": 424
}
```

#### List Vulnerability Sync Tasks

This action is used to retrieve list of vulnerability sync tasks.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|batch_id|integer|None|False|Filter by batch identifier|None|1234|
|org_id|integer|None|True|Identifier of organization|None|1234|
|status|string|None|False|Filter by status of tasks|None|in_progress|

Example input:

```
{
  "batch_id": 1234,
  "org_id": 1234,
  "status": "in_progress"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tasks|[]task|False|List of vulnerability sync tasks|

Example output:

```
{
  "tasks": [
    {
      "created_at": "2021-09-24T18:45:04+0000",
      "last_updated_by_user": {
        "firstname": "John",
        "id": 1234,
        "lastname": "Smith",
        "email": "user@example.com"
      },
      "status": "in_progress",
      "task_type": "patch-now",
      "created_by_user": {
        "email": "user@example.com",
        "firstname": "John",
        "id": 1234,
        "lastname": "Smith"
      },
      "id": 1234,
      "organization_id": 1234,
      "payload": {
        "severity": "medium",
        "package_versions": [
          {
            "display_name": "2021-06 Cumulative Update for Windows 10 Version 2...",
            "id": "1234",
            "name": "f2ac1cd6-4c7f-4481-bf8c-abf3ed49d39b",
            "version": "1"
          }
        ],
        "patch_id": "CVE-2021-31952"
      },
      "source": "Automox",
      "updated_at": "2021-09-24T18:47:11+0000"
    }
  ]
}
```

#### List Vulnerability Sync Batches

This action is used to retrieve list of vulnerability sync batches.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```
{
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|batches|[]batch|False|List of vulnerability sync batches|

Example output:

```
{
  "batches": [
    {
      "id": 1234,
      "organization_id": 1234,
      "source": "report.csv",
      "status": "awaiting_approval",
      "created_by_user": {
        "lastname": "Smith",
        "email": "user@example.com",
        "firstname": "John",
        "id": 1234
      },
      "unknown_host_count": 41,
      "updated_at": "2021-12-02T20:24:09+0000",
      "updated_by_user": {
        "id": 43852,
        "lastname": "Smith",
        "email": "user@example.com",
        "firstname": "John"
      },
      "created_at": "2021-12-02T20:24:08+0000"
    }
  ]
}
```

#### Get Vulnerability Sync Batch

This action is used to retrieve details for a specified vulnerability sync batch.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|batch_id|integer|None|True|Identifier of batch|None|1234|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```
{
  "batch_id": 1234,
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|batch|batch|True|Details of a specified vulnerability sync batch|

Example output:

```
{
  "batch": {
    "task_count": 2,
    "updated_at": "2021-09-24T18:46:22+0000",
    "cve_count": 2,
    "organization_id": 1234,
    "status": "approved",
    "impacted_device_count": 6,
    "issue_count": 3,
    "source": "example.csv",
    "unknown_host_count": 2,
    "updated_by": {
      "firstname": "John",
      "id": 1234,
      "lastname": "Smith",
      "email": "user@example.com"
    },
    "created_at": "2021-09-24T18:45:04+0000",
    "created_by": {
      "email": "user@example.com",
      "firstname": "John",
      "id": 1234,
      "lastname": "Smith"
    },
    "id": 45
  }
}
```

#### Execute or Cancel Vulnerability Sync Task

This action is used to take action to execute or cancel vulnerability sync task.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|Action to take on vulnerability sync task|['execute', 'cancel']|execute|
|org_id|integer|None|True|Identifier of organization|None|1234|
|task_id|integer|None|True|Identifier of task|None|1234|

Example input:

```
{
  "action": "execute",
  "org_id": 1234,
  "task_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Accept or Reject Vulnerability Sync Batch

This action is used to take action to approve or reject vulnerability sync batch.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|Action to take on batch|['accept', 'reject']|accept|
|batch_id|integer|None|True|Identifier of batch|None|1234|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```
{
  "action": "accept",
  "batch_id": 1234,
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
  "success": true
}
```

#### Run Device Command

This action is used to run a command on the device.

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
  "success": true
}
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
{
  "groups": [
    {
      "id": 1234,
      "organization_id": 1234,
      "parent_server_group_id": 1234,
      "policies": [
        1234,
        5678
      ],
      "refresh_interval": 360,
      "server_count": 6,
      "ui_color": "#059F1D",
      "wsus_config": {
        "created_at": "2020-11-03T00:22:06+0000",
        "id": 21606,
        "server_group_id": 0,
        "updated_at": "2020-11-03T00:22:06+0000"
      }
    }
  ]
}
```

#### Get Device Software

This action is used to retrieve a list of software installed on the device.

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
{
  "software": [
    {
      "display_name": "NetworkManager-libnm.x86_64",
      "organization_id": 1234,
      "repo": "Linux",
      "version": "1.30.2-1.fc34",
      "create_time": "2021-04-06T08:11:00+0000",
      "id": 1235371145,
      "is_managed": true,
      "os_name": "Fedora",
      "os_version_id": 4416,
      "name": "NetworkManager-libnm.x86_64",
      "os_version": "34",
      "package_id": 1234,
      "installed": true,
      "package_version_id": 1234,
      "server_id": 1234,
      "software_id": 1234
    }
  ]
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
  "success": true
}
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
  "group": {
    "organization_id": 1234,
    "parent_server_group_id": 0,
    "refresh_interval": 1440,
    "ui_color": "#059F1D",
    "id": 1234,
    "name": "InsightConnect Test Group",
    "notes": "Hello World"
  },
  "success": true
}
```

#### Delete Device

This action is used to delete Automox device.

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
  "success": true
}
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
{
  "device": {
    "agent_version": "1.0-33",
    "compliant": true,
    "create_time": "2021-08-03T15:53:59+0000",
    "detail": {
      "CPU": "Intel(R) Core(TM) i5-1038NG7 CPU @ 2.00GHz",
      "FQDNS": [
        "hostname.local"
      ],
      "IPS": [
        "192.168.0.1"
      ]
    },
    "display_name": "hostname",
    "id": 1234,
    "ip_addrs": [
      "192.168.0.1"
    ],
    "ip_addrs_private": [
      "192.168.0.1"
    ],
    "is_compatible": true,
    "last_disconnect_time": "2021-10-22T13:56:46+0000",
    "last_logged_in_user": "jsmith",
    "last_refresh_time": "2021-10-22T13:54:10+0000",
    "name": "hostname.local",
    "organization_id": 1234,
    "os_family": "Mac",
    "os_name": "OS X",
    "os_version": "11.4",
    "os_version_id": 4476,
    "patches": 4,
    "policy_status": [
      {
        "create_time": "2021-10-22T13:54:10+0000",
        "id": 1234,
        "organization_id": 1234,
        "policy_id": 1234,
        "policy_name": "Manual Patching",
        "policy_type_name": "patch",
        "result": "{}",
        "server_id": 1234,
        "status": 1
      }
    ],
    "refresh_interval": 360,
    "serial_number": "abcd",
    "server_group_id": 1234,
    "status": {
      "agent_status": "disconnected",
      "device_status": "not-ready",
      "policy_status": "compliant",
      "policy_statuses": [
        {
          "compliant": true,
          "id": 1234
        }
      ]
    },
    "tags": [
      "tag1"
    ],
    "timezone": "UTC-0700",
    "total_count": 5,
    "uuid": "abc12345-abc1-2345-abc1-abc123456789"
  }
}
```

#### Get Device by IP Address

This action is used to find an Automox device by IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip_address|string|None|True|IP address of device|None|192.168.0.1|
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
{
  "device": {
    "agent_version": "1.0-33",
    "compliant": true,
    "create_time": "2021-08-03T15:53:59+0000",
    "detail": {
      "CPU": "Intel(R) Core(TM) i5-1038NG7 CPU @ 2.00GHz",
      "FQDNS": [
        "hostname.local"
      ],
      "IPS": [
        "192.168.0.1"
      ]
    },
    "display_name": "hostname",
    "id": 1234,
    "ip_addrs": [
      "192.168.0.1"
    ],
    "ip_addrs_private": [
      "192.168.0.1"
    ],
    "is_compatible": true,
    "last_disconnect_time": "2021-10-22T13:56:46+0000",
    "last_logged_in_user": "jsmith",
    "last_refresh_time": "2021-10-22T13:54:10+0000",
    "name": "hostname.local",
    "organization_id": 1234,
    "os_family": "Mac",
    "os_name": "OS X",
    "os_version": "11.4",
    "os_version_id": 4476,
    "patches": 4,
    "policy_status": [
      {
        "create_time": "2021-10-22T13:54:10+0000",
        "id": 1234,
        "organization_id": 1234,
        "policy_id": 1234,
        "policy_name": "Manual Patching",
        "policy_type_name": "patch",
        "result": "{}",
        "server_id": 1234,
        "status": 1
      }
    ],
    "refresh_interval": 360,
    "serial_number": "abcd",
    "server_group_id": 1234,
    "status": {
      "agent_status": "disconnected",
      "device_status": "not-ready",
      "policy_status": "compliant",
      "policy_statuses": [
        {
          "compliant": true,
          "id": 1234
        }
      ]
    },
    "tags": [
      "tag1"
    ],
    "timezone": "UTC-0700",
    "total_count": 5,
    "uuid": "abc12345-abc1-2345-abc1-abc123456789"
  }
}
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
{
  "devices": [
    {
      "agent_version": "1.0-33",
      "compliant": true,
      "create_time": "2021-08-03T15:53:59+0000",
      "detail": {
        "CPU": "Intel(R) Core(TM) i5-1038NG7 CPU @ 2.00GHz",
        "FQDNS": [
          "hostname.local"
        ],
        "IPS": [
          "192.168.0.1"
        ]
      },
      "display_name": "hostname",
      "id": 1234,
      "ip_addrs": [
        "192.168.0.1"
      ],
      "ip_addrs_private": [
        "192.168.0.1"
      ],
      "is_compatible": true,
      "last_disconnect_time": "2021-10-22T13:56:46+0000",
      "last_logged_in_user": "jsmith",
      "last_refresh_time": "2021-10-22T13:54:10+0000",
      "name": "hostname.local",
      "organization_id": 1234,
      "os_family": "Mac",
      "os_name": "OS X",
      "os_version": "11.4",
      "os_version_id": 4476,
      "patches": 4,
      "policy_status": [
        {
          "create_time": "2021-10-22T13:54:10+0000",
          "id": 1234,
          "organization_id": 1234,
          "policy_id": 1234,
          "policy_name": "Manual Patching",
          "policy_type_name": "patch",
          "result": "{}",
          "server_id": 1234,
          "status": 1
        }
      ],
      "refresh_interval": 360,
      "serial_number": "abcd",
      "server_group_id": 1234,
      "status": {
        "agent_status": "disconnected",
        "device_status": "not-ready",
        "policy_status": "compliant",
        "policy_statuses": [
          {
            "compliant": true,
            "id": 1234
          }
        ]
      },
      "tags": [
        "tag1"
      ],
      "timezone": "UTC-0700",
      "total_count": 5,
      "uuid": "abc12345-abc1-2345-abc1-abc123456789"
    }
  ]
}
```

#### List Organization Users

This action is used to retrieve users of the Automox organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```
{
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]user|False|List of Automox users|

Example output:

```
{
  "users": [
    {
      "email": "user@example.com",
      "features": {
        "mo": true
      },
      "firstname": "John",
      "id": 1234,
      "lastname": "Smith",
      "orgs": [
        {
          "id": 1234,
          "name": "Organization"
        }
      ],
      "prefs": [
        {
          "pref_name": "notify.system.add",
          "user_id": 1234,
          "value": "true"
        }
      ],
      "rbac_roles": [
        {
          "description": "Provides full administrative rights to the entire Automox System.",
          "id": 1,
          "name": "Full Administrator",
          "organization_id": 1234
        }
      ],
      "tags": [
        "tag1"
      ],
      "uuid": "abc12345-abc1-2345-abc1-abc123456789"
    }
  ]
}
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
{
  "organizations": [
    {
      "access_key": "abc12345-abc1-2345-abc1-abc123456789",
      "bill_overages": true,
      "create_time": "2019-08-27T21:59:19+0000",
      "device_count": 21,
      "metadata": {
        "patchServersDone": true
      },
      "name": "Automox Org",
      "sub_plan": "FULL",
      "id": 1234,
      "legacy_billing": true,
      "parent_id": 1,
      "rate_id": 1
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
{
  "policies": [
    {
      "configuration": {
        "auto_patch": true,
        "auto_reboot": true
      },
      "create_time": "2021-03-03T21:29:09+0000",
      "id": 1234,
      "name": "Patch All",
      "next_remediation": "2021-12-15T00:00:00+0000",
      "organization_id": 1234,
      "policy_type_name": "patch",
      "schedule_days": 254,
      "schedule_months": 8190,
      "schedule_time": "00:00",
      "schedule_weeks_of_month": 62,
      "server_count": 1,
      "server_groups": [
        1234,
        5678
      ]
    }
  ]
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
  "success": true
}
```

### Triggers

#### Get Automox Events

This trigger is used to retrieve Automox events to trigger workflows.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event_type|string|None|True|Name of event type to be retrieved (list of event types found at https://developer.automox.com/openapi/axconsole/operation/getEvents/#!in=query&path=eventName&t=request)|None|user.login|
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
{
  "event": {
    "id": 1234,
    "name": "system.delete",
    "server_id": 1234,
    "organization_id": 1234,
    "data": {
      "ip": "192.168.0.1",
      "os": "Ubuntu",
      "systemname": "hostname-1"
    },
    "server_name": "hostname-1",
    "create_time": "2021-12-16 06:20:38.153713"
  }
}
```

### Custom Output Types

#### device

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Device ID|integer|True|The device ID|
|Device Name|string|True|The device name|
|Organization ID|integer|True|The organization ID of the device|
|Server Group ID|integer|True|The server group ID of the device|
|Device UUID|string|True|The device unique identifier|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.0 - Get device by IP and Get device by hostname: fix validation issue when IP or hostname not found | Add unit tests 
* 1.1.1 - Fix undefined org ID passed to actions when not required | Record outcome of connection tests
* 1.1.0 - Add `report source` as optional input parameter to Upload Vulnerability Sync File action | Add report source to batch type
* 1.0.0 - Initial plugin

# Links

## References

* [Automox](https://www.automox.com/)
* [Automox Developer Portal](https://developer.automox.com/)
* [Managing API Keys](https://support.automox.com/help/managing-keys)
* [Event Types for Get Automox Events action](https://developer.automox.com/openapi/axconsole/operation/getEvents/#!in=query&path=eventName&t=request)

