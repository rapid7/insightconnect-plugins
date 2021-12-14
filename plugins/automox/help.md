# Description

Automox is Modernizing IT operations with continuous visibility, insight, and agility for your entire IT environment

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

_There are no supported product versions listed._

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

#### Automox Group

This action is used to update an Automox group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|color|string|None|False|Automox console highlight color for the group|None|#059F1D|
|group_id|integer|None|True|Identifier of the Automox group|None|1|
|name|string|None|True|Name of the group|None|None|
|notes|string|None|False|Define notes for the group|None|None|
|org_id|integer|None|False|Identifier of organization|None|1|
|parent_server_group_id|integer|None|False|Name of the parent group (Will be set to Default Group ID if not set)|None|None|
|policies|[]integer|None|False|List of policies to assign to group|None|None|
|refresh_interval|integer|1440|True|Frequency of device refreshes in minutes|None|None|

Example input:

```
{
  "color": "#059F1D",
  "group_id": 1,
  "org_id": 1
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
|device_id|integer|None|True|Identifier of device|None|1|
|patches|[]string|None|False|List of patches to be installed (Note that this only works with InstallUpdate command)|None|None|
|policy|[]string|None|False|List of patches to be installed (Note that this is only used with PolicyTest and PolicyRemediate commands)|None|None|

Example input:

```
{
  "command": "GetOS",
  "device_id": 1
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
|org_id|integer|None|False|Identifier of organization to restrict results|None|1|

Example input:

```
{
  "org_id": 1
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
|device_id|integer|None|True|Identifier of device|None|1|

Example input:

```
{
  "device_id": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|software|[]object|False|List of software on device|

Example output:

```
```

#### Delete Group

This action is used to delete an Automox group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_id|integer|None|True|Identifier of the Automox group|None|1|
|org_id|integer|None|False|Identifier of organization|None|1|

Example input:

```
{
  "group_id": 1,
  "org_id": 1
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
|name|string|None|True|Name of the group|None|None|
|notes|string|None|False|Define notes for the group|None|None|
|org_id|integer|None|False|Identifier of organization|None|1|
|parent_server_group_id|integer|None|False|Name of the parent group (Will be set to Default Group ID if not set)|None|None|
|policies|[]integer|None|False|List of policies to assign to group|None|None|
|refresh_interval|integer|1440|True|Frequency of device refreshes in minutes|None|None|

Example input:

```
{
  "color": "#059F1D",
  "org_id": 1
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
|device_id|integer|None|True|Identifier of device|None|1|
|org_id|integer|None|False|Identifier of organization|None|1|

Example input:

```
{
  "device_id": 1,
  "org_id": 1
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
|org_id|integer|None|False|Identifier of organization to restrict results|None|1|

Example input:

```
{
  "hostname": "hostname-1",
  "org_id": 1
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
|ip_address|string|None|True|IP address of device|None|https://example.com|
|org_id|integer|None|False|Identifier of organization to restrict results|None|1|

Example input:

```
{
  "ip_address": "127.0.0.1",
  "org_id": 1
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
|group_id|integer|None|False|Identifier of Server Group|None|1|
|org_id|integer|None|False|Identifier of organization to restrict results|None|1|

Example input:

```
{
  "group_id": 1,
  "org_id": 1
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
|org_id|integer|None|True|Identifier of Organization|None|1|

Example input:

```
{
  "org_id": 1
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
|org_id|integer|None|False|Identifier of organization to restrict results|None|1|

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
|device_id|integer|None|True|Identifier of device|None|1|
|exception|boolean|False|True|Exclude the device from reports and statistics|None|None|
|org_id|integer|None|False|Identifier of organization|None|1|
|server_group_id|integer|None|False|Identifier of server group|None|1|
|tags|[]string|None|False|List of tags|None|None|

Example input:

```
{
  "custom_name": "custom-name",
  "device_id": 1,
  "org_id": 1,
  "server_group_id": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
```

### Triggers

#### TODO

This trigger is used to tODO.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|event_type|string|None|True|Name of event type to be retrieved (List of event types found at https://developer.automox.com/openapi/axconsole/operation/getEvents/)|None|https://example.com|
|org_id|integer|None|False|Identifier of organization to restrict results|None|1|

Example input:

```
{
  "event_type": "user.login",
  "org_id": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|event|string|True|Event with details|

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

* [Automox](LINK TO PRODUCT/VENDOR WEBSITE)

