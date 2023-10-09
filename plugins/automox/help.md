#### Triggers

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

#### Actions

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
```

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
```

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Fix Vulnerability Sync API Actions
* 1.2.0 - Get device by IP and Get device by hostname: fix validation issue when IP or hostname not found | Add unit
  tests
* 1.1.1 - Fix undefined org ID passed to actions when not required | Record outcome of connection tests
* 1.1.0 - Add `report source` as optional input parameter to Upload Vulnerability Sync File action | Add report source
  to batch type
* 1.0.0 - Initial plugin

# Links

## References

* [Automox](https://www.automox.com/)
* [Automox Developer Portal](https://developer.automox.com/)
* [Managing API Keys](https://support.automox.com/help/managing-keys)
* [Event Types for Get Automox Events action](https://developer.automox.com/openapi/axconsole/operation/getEvents/#!in=query&path=eventName&t=request)

