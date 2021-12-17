# Description

Automox is modernizing IT operations through cloud-native efficiency and upending the old ways of legacy on-premise 
tools. Keeping you continuously connected to all your endpoints, regardless of location, environment, and operating
system type. Now you can manage and apply operating system and third-party patches, enforce security configurations, 
deploy software, and execute any action across Windows, macOS, and Linux systems. 

Utilizing this plugin allows for the orchestration of IT operations such as device management, triggering remote 
outcomes on endpoints, and basic Automox platform administration. 

# Key Features

* Ability to retrieve and manage Automox managed devices
* Ability to managed Automox groups
* Ability to initiate Vulnerability Sync uploads and remediation of issues
* Ability to trigger workflows based on Automox platform events

# Requirements

* Requires an Automox API Key

# Supported Product Versions

* All

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Enter organization API key|None|abc12345-abc1-2345-abc1-abc123456789|

Example input:

```
{
  "api_key": "abc12345-abc1-2345-abc1-abc123456789"
}
```

## Technical Details

### Actions

#### Upload Vulnerability Sync File

This action is used to upload CSV file to vulnerability sync for processing.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|csv_file|bytes|None|True|Base64 encoded CSV data from which to create the vulnerabiulity sync batch|None|PGgxPlJhcGlkNzwvaDE+|
|csv_file_name|string|https://example.com|False|Name for CSV file uploaded and shown within Automox|None|insightconnect-uploaded-report.csv|
|org_id|integer|None|True|Identifier of organization|None|1234|

Example input:

```
{
  "csv_file": "PGgxPlJhcGlkNzwvaDE+",
  "csv_file_name": "insightconnect-uploaded-report.csv",
  "org_id": 1234
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
        "firstname": "Peter",
        "id": 44688,
        "lastname": "Pflaster",
        "email": "user@example.com"
      },
      "status": "in_progress",
      "task_type": "patch-now",
      "created_by_user": {
        "email": "user@example.com",
        "firstname": "Peter",
        "id": 44688,
        "lastname": "Pflaster"
      },
      "id": 266,
      "organization_id": 9237,
      "payload": {
        "severity": "medium",
        "package_versions": [
          {
            "display_name": "2021-06 Cumulative Update for Windows 10 Version 2...",
            "id": "232850978",
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
      "id": 379,
      "organization_id": 9237,
      "source": "report.csv",
      "status": "awaiting_approval",
      "created_by_user": {
        "lastname": "Youtz",
        "email": "user@example.com",
        "firstname": "Zachary",
        "id": 43852
      },
      "unknown_host_count": 41,
      "updated_at": "2021-12-02T20:24:09+0000",
      "updated_by_user": {
        "id": 43852,
        "lastname": "Youtz",
        "email": "user@example.com",
        "firstname": "Zachary"
      },
      "created_at": "2021-12-02T20:24:08+0000"
    },
    {
      "id": 355,
      "updated_by_user": {
        "email": "user@example.com",
        "firstname": "Zachary",
        "id": 43852,
        "lastname": "Youtz"
      },
      "created_at": "2021-11-23T17:51:04+0000",
      "created_by_user": {
        "email": "user@example.com",
        "firstname": "Zachary",
        "id": 43852,
        "lastname": "Youtz"
      },
      "organization_id": 9237,
      "source": "report.csv",
      "status": "awaiting_approval",
      "unknown_host_count": 41,
      "updated_at": "2021-11-23T17:51:06+0000"
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
    "organization_id": 9237,
    "status": "approved",
    "impacted_device_count": 6,
    "issue_count": 3,
    "source": "peter.csv",
    "unknown_host_count": 2,
    "updated_by": {
      "firstname": "Peter",
      "id": 44688,
      "lastname": "Pflaster",
      "email": "user@example.com"
    },
    "created_at": "2021-09-24T18:45:04+0000",
    "created_by": {
      "email": "user@example.com",
      "firstname": "Peter",
      "id": 44688,
      "lastname": "Pflaster"
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
```

#### Automox Group

This action is used to update an Automox group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|color|string|None|False|Automox console highlight color for the group|None|#059F1D|
|group_id|integer|None|True|Identifier of the Automox group|None|1234|
|name|string|None|True|Name of the group|None|Group1|
|notes|string|None|False|Define notes for the group|None|Example notes go here|
|org_id|integer|None|False|Identifier of organization|None|1234|
|parent_server_group_id|integer|None|False|Name of the parent group (Will be set to Default Group ID if not set)|None|1234|
|policies|[]integer|None|False|List of policies to assign to group|None|[1, 2, 3]|
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
```

#### Run Device Command

This action is used to run a command on the device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|command|string|None|True|Identifier of device|['GetOS', 'InstallUpdate', 'InstallAllUpdates', 'PolicyTest', 'PolicyRemediate', 'Reboot']|GetOS|
|device_id|integer|None|True|Identifier of device|None|1234|
|org_id|integer|None|False|Identifier of organization|None|1234|
|patches|[]string|None|False|List of patches to be installed (Note that this only works with InstallUpdate command)|None|[""]|
|policy_id|integer|None|False|Identifier of policy|None|1234|

Example input:

```
{
  "command": "GetOS",
  "device_id": 1234,
  "org_id": 1234,
  "patches": [
    ""
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
|software|[]object|False|List of software on device|

Example output:

```
{
  "software": [
    {
      "display_name": "NetworkManager-libnm.x86_64",
      "organization_id": 9237,
      "repo": "Linux",
      "version": "1.30.2-1.fc34",
      "create_time": "2021-04-06T08:11:00+0000",
      "id": 1235371145,
      "is_managed": true,
      "os_name": "Fedora",
      "os_version_id": 4416,
      "name": "NetworkManager-libnm.x86_64",
      "os_version": "34",
      "package_id": 225916374,
      "installed": true,
      "package_version_id": 231241032,
      "server_id": 1123617,
      "software_id": 10648
    },
    {
      "id": 1235371146,
      "os_version_id": 4416,
      "version": "1.30.2-1.fc34",
      "display_name": "NetworkManager.x86_64",
      "is_managed": true,
      "name": "NetworkManager.x86_64",
      "os_name": "Fedora",
      "package_id": 225916389,
      "create_time": "2021-04-06T08:11:01+0000",
      "installed": true,
      "package_version_id": 231241047,
      "repo": "Linux",
      "server_id": 1123617,
      "organization_id": 9237,
      "os_version": "34",
      "software_id": 10666
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

```

#### Create Group

This action is used to create an Automox group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|color|string|None|False|Automox console highlight color for the group|None|#059F1D|
|name|string|None|True|Name of the group|None|Group1|
|notes|string|None|False|Define notes for the group|None|Example notes go here|
|org_id|integer|None|False|Identifier of organization|None|1234|
|parent_server_group_id|integer|None|False|Name of the parent group (Will be set to Default Group ID if not set)|None|1234|
|policies|[]integer|None|False|List of policies to assign to group|None|[1, 2, 3]|
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
|group|group|True|Detailed infromation about the created group|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "group": {
    "organization_id": 9237,
    "parent_server_group_id": 30599,
    "refresh_interval": 1440,
    "ui_color": "#059F1D",
    "id": 119981,
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
```

#### List Devices

This action is used to retrieve Automox managed devices.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_id|integer|None|False|Identifier of Server Group|None|1234|
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

#### List Organization Users

This action is used to retrieve users of the Automox organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|org_id|integer|None|True|Identifier of Organization|None|1234|

Example input:

```
{
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]users|False|List of Automox users|

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
{
  "organizations": [
    {
      "access_key": "5ded37d8-2e58-4653-9e21-4c8391e439c8",
      "bill_overages": true,
      "create_time": "2019-08-27T21:59:19+0000",
      "device_count": 21,
      "metadata": {
        "patchServersDone": true
      },
      "name": "Automox Worklet Test Org",
      "sub_plan": "FULL",
      "id": 9237,
      "legacy_billing": true,
      "parent_id": 65,
      "rate_id": 1
    },
    {
      "metadata": {
        "patchServersDone": true
      },
      "name": "Automox - SE",
      "parent_id": 65,
      "rate_id": 1,
      "sub_plan": "FULL",
      "access_key": "1911ce44-4c92-4242-8565-1b4d91d60445",
      "billing_email": "user@example.com",
      "billing_name": "Automox - SE",
      "create_time": "2020-05-19T18:57:01+0000",
      "device_count": 64,
      "id": 16943,
      "legacy_billing": true,
      "bill_overages": true
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
      "create_time": "2021-03-03T21:29:09+0000",
      "schedule_time": "00:00",
      "server_groups": [
        85579,
        86754
      ],
      "configuration": {
        "custom_notification_reboot_message_mac": "An important update will be installed; reboot may ...",
        "notify_deferred_reboot_user": true,
        "patch_rule": "all",
        "custom_notification_patch_message": "System Update: An important update will be install...",
        "custom_notification_reboot_message": "An important update will be installed; reboot may ...",
        "custom_pending_reboot_notification_deferment_periods": [
          1,
          4
        ],
        "custom_pending_reboot_notification_message_mac": "Updates require reboot: Please save your work.",
        "filter_type": "all",
        "auto_patch": true,
        "custom_notification_patch_message_mac": "System Update: An important update will be install...",
        "custom_pending_reboot_notification_max_delays": 3,
        "notify_user": true,
        "custom_notification_max_delays": 3,
        "custom_pending_reboot_notification_message": "Updates require reboot: Please save your work.",
        "notify_reboot_user": true,
        "auto_reboot": true,
        "custom_notification_deferment_periods": [
          1,
          4
        ]
      },
      "name": "Amelia Patch All",
      "next_remediation": "2021-12-15T00:00:00+0000",
      "organization_id": 9237,
      "policy_type_name": "patch",
      "schedule_days": 254,
      "schedule_months": 8190,
      "schedule_weeks_of_month": 62,
      "id": 112411,
      "server_count": 1
    },
    {
      "configuration": {
        "package_version": "7.8.4",
        "os_family": "Windows",
        "package_name": "NotepadPlusPlus"
      },
      "next_remediation": "2021-12-15T00:00:00+0000",
      "schedule_days": 254,
      "schedule_months": 8190,
      "schedule_time": "00:00",
      "schedule_weeks_of_month": 62,
      "server_groups": [
        85579,
        86754
      ],
      "create_time": "2021-03-03T21:35:39+0000",
      "id": 112418,
      "name": "Amelia RSP",
      "organization_id": 9237,
      "policy_type_name": "required_software",
      "server_count": 1
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
|event_type|string|None|True|Name of event type to be retrieved (List of event types found at https://developer.automox.com/openapi/axconsole/operation/getEvents/)|None|https://example.com|
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

* 1.0.0 - Initial plugin

# Links

## References

* [Automox](https://www.automox.com/)
* [Automox Developer Portal](https://developer.automox.com/)
* [Managing API Keys](https://support.automox.com/help/managing-keys)

