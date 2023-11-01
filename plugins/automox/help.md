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
  
* All as of 10/09/2023

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Organization API key|None|abc12345-abc1-2345-abc1-abc123456789|
  
Example input:

```
{
  "api_key": "abc12345-abc1-2345-abc1-abc123456789"
}
```

## Technical Details

### Actions


#### Create Group
  
Create an Automox group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
  "policies": 1,
  "refresh_interval": 1440
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|group|group|True|Detailed information about the created group|None|
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "group": {
    "Color": {},
    "Device Count": {},
    "Enable OS Auto Update": "true",
    "Group ID": 0,
    "Group Name": "",
    "Notes": {},
    "Organization ID": {},
    "Parent Server Group ID": {},
    "Policies": [
      {}
    ],
    "Refresh Interval": {}
  },
  "success": true
}
```

#### Delete Device
  
Delete an Automox device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|None|
  
Example output:

```
{
  "success": true
}
```

#### Delete Group
  
Delete an Automox group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Vulnerability Sync Action Set
  
Delete a vulnerability sync action set and all associated data

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Execute Vulnerability Sync Actions
  
Launch remediation for patch and worklet remediations

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action_set_id|integer|None|True|Identifier of the action set|None|1234|
|actions|[]action_set_action|None|True|List of remediations to execute|None|[{'action': 'patch-now', 'solution_id': 1234, 'device_ids': [1234, 5678]}, {'action': 'patch-with-worklet', 'solution_id': 1234, 'worklet_id': 1234, 'device_ids': [1234, 5678]}]|
|org_id|integer|None|True|Identifier of organization|None|1234|
  
Example input:

```
{
  "action_set_id": 1234,
  "actions": {
    "action": "patch-now",
    "device_ids": [
      1234,
      5678
    ],
    "solution_id": 1234
  },
  "org_id": 1234
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

#### Get Device by Hostname
  
Find an Automox device by hostname

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|device|device|False|The matched Automox device|None|
  
Example output:

```
{
  "device": {
    "Agent Version": {},
    "Compliant": {},
    "Connected": {},
    "Create Time": {},
    "Custom Name": {},
    "Deleted": {},
    "Detail": {},
    "Device ID": 0,
    "Device Name": "",
    "Display Name": {},
    "IP Addresses": {},
    "Is Compatible": {},
    "Is Delayed By User": {},
    "Is Delayed by Notification": {},
    "Last Disconnect Time": {},
    "Last Logged In User": {},
    "Last Refresh Time": {},
    "Last Scan Failed": {},
    "Last Update Time": {},
    "Needs Attention": {},
    "Needs Reboot": "true",
    "Next Patch Time": {},
    "Operating System": {},
    "Operating System Family": {},
    "Operating System Version": {},
    "Organization ID": {},
    "Patches": {},
    "Pending": {},
    "Pending Patches": {},
    "Private IP Addresses": {},
    "Reboot Is Delayed By Notification": {},
    "Reboot Is Delayed By User": {},
    "Serial Number": {},
    "Server Group ID": {},
    "Status": {
      "Agent Status": {},
      "Device Status": {},
      "Policy Status": {},
      "Policy Statuses": [
        {
          "Compliant": {},
          "Policy ID": {}
        }
      ]
    },
    "Tags": [
      {}
    ]
  }
}
```

#### Get Device by IP Address
  
Find an Automox device by IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|device|device|False|The matched Automox device|None|
  
Example output:

```
{
  "device": {
    "Agent Version": {},
    "Compliant": {},
    "Connected": {},
    "Create Time": {},
    "Custom Name": {},
    "Deleted": {},
    "Detail": {},
    "Device ID": 0,
    "Device Name": "",
    "Display Name": {},
    "IP Addresses": {},
    "Is Compatible": {},
    "Is Delayed By User": {},
    "Is Delayed by Notification": {},
    "Last Disconnect Time": {},
    "Last Logged In User": {},
    "Last Refresh Time": {},
    "Last Scan Failed": {},
    "Last Update Time": {},
    "Needs Attention": {},
    "Needs Reboot": "true",
    "Next Patch Time": {},
    "Operating System": {},
    "Operating System Family": {},
    "Operating System Version": {},
    "Organization ID": {},
    "Patches": {},
    "Pending": {},
    "Pending Patches": {},
    "Private IP Addresses": {},
    "Reboot Is Delayed By Notification": {},
    "Reboot Is Delayed By User": {},
    "Serial Number": {},
    "Server Group ID": {},
    "Status": {
      "Agent Status": {},
      "Device Status": {},
      "Policy Status": {},
      "Policy Statuses": [
        {
          "Compliant": {},
          "Policy ID": {}
        }
      ]
    },
    "Tags": [
      {}
    ]
  }
}
```

#### Get Device Software
  
Retrieve a list of software installed on a device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|software|[]device_software|False|List of software on device|None|
  
Example output:

```
{
  "software": [
    {
      "CVE Score": {},
      "CVEs": [
        {}
      ],
      "Creation Time": {},
      "Deferred Until": "",
      "Device ID": {},
      "Ignored Status": {},
      "Installed Status": "true",
      "Is Uninstallable": {},
      "Operating System Name": {},
      "Operating System Version": {},
      "Organization ID": {},
      "Package ID": {},
      "Requires Reboot": {},
      "Severity": {},
      "Software Display Name": {},
      "Software ID": {},
      "Software Name": {},
      "Version": {}
    }
  ]
}
```

#### Get Vulnerability Sync Action Set
  
Retrieve details for a specified vulnerability sync action set

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|action_set|action_set|True|Details of a specified vulnerability sync action_set|None|
  
Example output:

```
{
  "action_set": {
    "Action Set ID": 0,
    "Action Set Source": {
      "Source Name": {},
      "Source Type": {}
    },
    "Action Set Statistics": {
      "Issues": {
        "Unknown Host Count": {}
      }
    },
    "Action Set Status": {},
    "Configuration ID": "",
    "Created At": {},
    "Created By": {
      "Email": {},
      "First Name": {},
      "Last Name": {},
      "User ID": {}
    },
    "Organization ID": {},
    "Solutions": {
      "Patch Now": {
        "Device Count": {},
        "Solution Count": {},
        "Vulnerability Count": {}
      },
      "Patch with Worklet": {}
    },
    "Uploaded At": {}
  }
}
```

#### List Devices
  
Retrieve Automox managed devices

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|devices|[]device|False|List of Automox managed devices|None|
  
Example output:

```
{
  "devices": [
    {
      "Agent Version": {},
      "Compliant": {},
      "Connected": {},
      "Create Time": {},
      "Custom Name": {},
      "Deleted": {},
      "Detail": {},
      "Device ID": 0,
      "Device Name": "",
      "Display Name": {},
      "IP Addresses": {},
      "Is Compatible": {},
      "Is Delayed By User": {},
      "Is Delayed by Notification": {},
      "Last Disconnect Time": {},
      "Last Logged In User": {},
      "Last Refresh Time": {},
      "Last Scan Failed": {},
      "Last Update Time": {},
      "Needs Attention": {},
      "Needs Reboot": "true",
      "Next Patch Time": {},
      "Operating System": {},
      "Operating System Family": {},
      "Operating System Version": {},
      "Organization ID": {},
      "Patches": {},
      "Pending": {},
      "Pending Patches": {},
      "Private IP Addresses": {},
      "Reboot Is Delayed By Notification": {},
      "Reboot Is Delayed By User": {},
      "Serial Number": {},
      "Server Group ID": {},
      "Status": {
        "Agent Status": {},
        "Device Status": {},
        "Policy Status": {},
        "Policy Statuses": [
          {
            "Compliant": {},
            "Policy ID": {}
          }
        ]
      },
      "Tags": [
        {}
      ]
    }
  ]
}
```

#### List Groups
  
List Automox groups

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|org_id|integer|None|False|Identifier of organization to restrict results|None|1234|
  
Example input:

```
{
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|groups|[]group|False|List of Automox groups|None|
  
Example output:

```
{
  "groups": [
    {
      "Color": {},
      "Device Count": {},
      "Enable OS Auto Update": "true",
      "Group ID": 0,
      "Group Name": "",
      "Notes": {},
      "Organization ID": {},
      "Parent Server Group ID": {},
      "Policies": [
        {}
      ],
      "Refresh Interval": {}
    }
  ]
}
```

#### List Organization Users
  
Retrieve users of the Automox organization

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|org_id|integer|None|True|Identifier of organization|None|1234|
  
Example input:

```
{
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|users|[]user|False|List of Automox users|None|
  
Example output:

```
{
  "users": [
    {
      "Email": {},
      "Features": {},
      "First Name": "",
      "Last Name": {},
      "Organizations": [
        {
          "Name": {},
          "Organization ID": {}
        }
      ],
      "Roles": [
        {
          "Name": {},
          "Organization ID": {},
          "Role ID": {}
        }
      ],
      "SAML Enabled": "true",
      "Tags": [
        {}
      ],
      "User ID": 0
    }
  ]
}
```

#### List Organizations
  
Retrieve Automox organizations

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|organizations|[]organization|True|List of Automox organizations|None|
  
Example output:

```
{
  "organizations": [
    {
      "Creation Time": {},
      "Device Count": {},
      "Device Limit": {},
      "Organization ID": 0,
      "Organization Name": "",
      "Parent Organization ID": {},
      "Server Limit": {}
    }
  ]
}
```

#### List Policies
  
Retrieve Automox policies

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|org_id|integer|None|False|Identifier of organization to restrict results|None|1234|
  
Example input:

```
{
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|policies|[]policy|False|List of Automox policies|None|
  
Example output:

```
{
  "policies": [
    {
      "Device Group IDs": [
        {}
      ],
      "Organization ID": {},
      "Policy Configuration": {},
      "Policy ID": 0,
      "Policy Name": "",
      "Policy Type Name": {}
    }
  ]
}
```

#### List Vulnerability Sync Action Set Issues
  
Retrieve the issues identified for a specified vulnerability sync action set

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action_set_id|integer|None|True|Identifier of the action set|None|1234|
|issue_type_in|[]string|None|False|Filter by issue type|None|['unknown-host']|
|org_id|integer|None|True|Identifier of organization|None|1234|
  
Example input:

```
{
  "action_set_id": 1234,
  "issue_type_in": "unknown-host",
  "org_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|issues|[]action_set_issue|True|Issues associated with the specified vulnerability sync action_set|None|
  
Example output:

```
{
  "issues": [
    {
      "Issue Details": {},
      "Issue ID": 0,
      "Issue Type": ""
    }
  ]
}
```

#### List Vulnerability Sync Action Set Solutions
  
Retrieve a list of vulnerability sync remediations

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action_set_id|integer|None|True|Filter by action set identifier|None|1234|
|org_id|integer|None|True|Identifier of organization|None|1234|
|remediation_type_in|[]string|None|False|Filter by remediation type|None|['patch-now', 'patch-with-worklet']|
|severity_in|[]string|None|False|Filter by severity|None|['critical', 'high', 'medium', 'low', 'unknown']|
|vulnerability_in|[]string|None|False|Filter by vulnerability|None|['CVE-2020-1234', 'CVE-2020-5678']|
  
Example input:

```
{
  "action_set_id": 1234,
  "org_id": 1234,
  "remediation_type_in": "patch-now",
  "severity_in": "critical",
  "vulnerability_in": "CVE-2020-1234"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|solutions|[]solution|False|List of vulnerability sync Solutions|None|
  
Example output:

```
{
  "solutions": [
    {
      "Device IDs": 1234,
      "Devices": {
        "custom_name": "custom-name",
        "deleted": false,
        "id": 1234,
        "ip_addrs_private": [
          "10.0.0.1"
        ],
        "name": "device-1",
        "status": "in_progress"
      },
      "Remediation Type": {},
      "Solution Details": {
        "solution_fix": "Install Office Click-To-Run updates through any installed Office application. Go to File &gt; Account (or Office Account if you opened Outlook). Under Product Information, choose Update Options &gt; Update Now.",
        "solution_id": "office-click-to-run-upgrade-latest",
        "solution_summary": "Upgrade to the latest version of Microsoft Office",
        "solution_type": "workaround"
      },
      "Solution ID": 1234,
      "Solution Type": "rapid7-solution",
      "Vulnerabilities": {
        "id": "CVE-2019-1297",
        "severity": "high",
        "summary": "A remote code execution vulnerability exists in Microsoft Excel software when the software fails to properly handle objects in memory. An attacker who successfully exploited the vulnerability could run arbitrary code in the context of the current user. If the current user is logged on with administrative user rights, an attacker could take control of the affected system. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights. Users whose accounts are configured to have fewer user rights on the system could be less impacted than users who operate with administrative user rights. Exploitation of the vulnerability requires that a user open a specially crafted file with an affected version of Microsoft Excel. In an email attack scenario, an attacker could exploit the vulnerability by sending the specially crafted file to the user and convincing the user to open the file. In a web-based attack scenario, an attacker could host a website (or leverage a compromised website that accepts or hosts user-provided content) containing a specially crafted file designed to exploit the vulnerability. An attacker would have no way to force users to visit the website. Instead, an attacker would have to convince users to click a link, typically by way of an enticement in an email or instant message, and then convince them to open the specially crafted file. The security update addresses the vulnerability by correcting how Microsoft Excel handles objects in memory.",
        "title": "Microsoft Excel Remote Code Execution Vulnerability"
      }
    }
  ]
}
```

#### List Vulnerability Sync Action Sets
  
Retrieve list of vulnerability sync batches

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|configuration_id_equals|string|None|False|Filter by configuration ID|None|00000000-0000-0000-0000-000000000000|
|configuration_id_is_set|boolean|None|False|Filter based on whether the configuration ID is set|None|True|
|group_sort|string|None|False|Sort results by field|['asc', 'desc', 'latest_updated_at:asc', 'latest_updated_at:desc', 'source:asc', 'source:desc', '']|latest_updated_at:desc|
|include_all_runs_equals|boolean|None|False|Whether to include all runs in the response|None|True|
|org_id|integer|None|True|Identifier of organization|None|1234|
|sort|string|None|False|Sort results by field|['created_at', 'updated_at', 'status', 'source_type', 'source_name', 'configuration_id', '']|created_at|
|source_type_in|[]string|None|False|Filter by source type|None|['Generic Report', 'CrowdStrike', 'Rapid7', 'TenableIO', 'Qualys']|
|status_in|[]string|None|False|Filter by status|None|['building', 'ready', 'error']|
|status_not_in|[]string|None|False|Filter by status|None|['building', 'ready', 'error']|
  
Example input:

```
{
  "configuration_id_equals": "00000000-0000-0000-0000-000000000000",
  "configuration_id_is_set": true,
  "group_sort": "latest_updated_at:desc",
  "include_all_runs_equals": true,
  "org_id": 1234,
  "sort": "created_at",
  "source_type_in": "Generic Report",
  "status_in": "building",
  "status_not_in": "building"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|action_sets|[]action_set|False|List of vulnerability sync action sets|[{'created_at': '2023-10-10T03:45:26+0000', 'created_by_user': {'email': 'user@example.com', 'firstname': 'User', 'id': 1, 'lastname': 'Name'}, 'id': 1234, 'organization_id': 1, 'source': {'name': 'insightconnect-uploaded-report.csv', 'type': 'generic'}, 'statistics': {'issues': {'unknown-host': {'count': 4}}, 'solutions': {'patch-with-worklet': {'count': 1, 'device_count': 18, 'vulnerability_count': 1}}}, 'status': 'ready', 'updated_at': '2023-10-10T03:45:30+0000', 'updated_by_user': {'email': 'user@example.com', 'firstname': 'User', 'id': 1, 'lastname': 'Name'}}]|
  
Example output:

```
{
  "action_sets": {
    "created_at": "2023-10-10T03:45:26+0000",
    "created_by_user": {
      "email": "user@example.com",
      "firstname": "User",
      "id": 1,
      "lastname": "Name"
    },
    "id": 1234,
    "organization_id": 1,
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
      "email": "user@example.com",
      "firstname": "User",
      "id": 1,
      "lastname": "Name"
    }
  }
}
```

#### Run Device Command
  
Run a command on a device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|command|string|None|True|Command to run on device|['GetOS', 'InstallUpdate', 'InstallAllUpdates', 'PolicyTest', 'PolicyRemediate', 'Reboot']|GetOS|
|device_id|integer|None|True|Identifier of device|None|1234|
|org_id|integer|None|False|Identifier of organization|None|1234|
|patches|[]string|None|False|List of patches to be installed by name (Note: this only works with the InstallUpdate command)|None|['Security Update (KB4549947)']|
|policy_id|integer|None|False|Identifier of policy|None|1234|
  
Example input:

```
{
  "command": "GetOS",
  "device_id": 1234,
  "org_id": 1234,
  "patches": "Security Update (KB4549947)",
  "policy_id": 1234
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

#### Update Device
  
Update Automox device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
  "tags": "tag1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|None|
  
Example output:

```
{
  "success": true
}
```

#### Update Group
  
Update an Automox group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
  "policies": 1,
  "refresh_interval": 1440
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

#### Upload Vulnerability Sync File
  
Upload a CSV file to vulnerability sync for processing

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|csv_file|bytes|None|True|Base64 encoded CSV data from which to create the vulnerability sync batch|None|PGgxPlJhcGlkNzwvaDE+|
|csv_file_name|string|insightconnect-uploaded-report.csv|False|Name for CSV file uploaded and shown within Automox|None|insightconnect-uploaded-report.csv|
|org_id|integer|None|True|Identifier of organization|None|1234|
|report_source|string|generic|False|The third-party source of the vulnerability report|['generic', 'crowd-strike', 'rapid7', 'tenable', 'qualys']|rapid7|
  
Example input:

```
{
  "csv_file": "PGgxPlJhcGlkNzwvaDE+",
  "csv_file_name": "insightconnect-uploaded-report.csv",
  "org_id": 1234,
  "report_source": "generic"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|Identifier of the vulnerability sync action set|1234|
|status|string|True|Status of the vulnerability sync action set|building|
  
Example output:

```
{
  "id": 1234,
  "status": "building"
}
```
### Triggers


#### Get Automox Events
  
Retrieve Automox events to trigger workflows

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|event|event|True|Event with details|None|
  
Example output:

```
{
  "event": {
    "Creation Time": {},
    "Device ID": {},
    "Device Name": {},
    "Event Data": {},
    "Event ID": 0,
    "Event name": "",
    "Organization ID": {},
    "Policy ID": {},
    "Policy Name": {},
    "Policy Type": {},
    "User ID": {}
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**organization**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Creation Time|string|None|False|The datetime of when the organization was created|None|
|Device Count|integer|None|False|The organization device count|None|
|Device Limit|integer|None|False|The organization device limit|None|
|Organization ID|integer|None|True|The organization identifier|None|
|Organization Name|string|None|True|The organization name|None|
|Parent Organization ID|integer|None|False|The parent organization identifier|None|
|Server Limit|integer|None|False|The organization server limit|None|
  
**user_org**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Organization ID|integer|None|True|The organization identifier of the user|None|
|Name|string|None|False|The name of the organization|None|
  
**user_rbac_role**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Role ID|integer|None|True|The role identifier|None|
|Name|string|None|False|The name of the role|None|
|Organization ID|integer|None|True|The organization identifier of the user role|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|False|The email of the user|None|
|Features|object|None|False|The features enabled for the user|None|
|First Name|string|None|False|The first name of the user|None|
|User ID|integer|None|True|The user identifier|None|
|Last Name|string|None|False|The last name of the user|None|
|Organizations|[]user_org|None|False|The organizations for which the user has access|None|
|Roles|[]user_rbac_role|None|False|The roles assigned to the user|None|
|SAML Enabled|boolean|None|False|Whether SAML has been enabled for the user|None|
|Tags|[]string|None|False|The user defined tags|None|
  
**device_policy_status**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Compliant|boolean|None|False|Whether a device is compliant to given status|None|
|Policy ID|integer|None|False|The identifier of the policy|None|
  
**device_status_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Status|string|None|False|The status of a device agent|None|
|Device Status|string|None|False|The status of a device|None|
|Policy Status|string|None|False|The overall status of all policies assigned to a device|None|
|Policy Statuses|[]device_policy_status|None|False|A list of policy statuses with compliant details|None|
  
**device**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Version|string|None|False|The agent version of a device|None|
|Compliant|boolean|None|False|Whether a device is compliant|None|
|Connected|boolean|None|False|Whether a device is currently connected to the Automox platform|None|
|Create Time|string|None|False|The time a device was created in the Automox platform|None|
|Custom Name|string|None|False|The custom name of a device|None|
|Deleted|boolean|None|False|Whether a device is deleted|None|
|Detail|object|None|False|Additional details of a device|None|
|Display Name|string|None|False|The display name of a device|None|
|Device ID|integer|None|False|The device ID|None|
|IP Addresses|[]string|None|False|List of IP addresses for a device|None|
|Private IP Addresses|[]string|None|False|List of private IP addresses for a device|None|
|Is Compatible|boolean|None|False|Whether a device is compatible with the Automox platform|None|
|Is Delayed by Notification|boolean|None|False|Whether patching is delayed by a device notificiation|None|
|Is Delayed By User|boolean|None|False|Whether patching is delayed by a user|None|
|Last Disconnect Time|string|None|False|The last time a device disconnected from the Automox platform|None|
|Last Logged In User|string|None|False|The last logged in user of a device|None|
|Last Refresh Time|string|None|False|The last time a device was refreshed|None|
|Last Scan Failed|boolean|None|False|Whether the last scan failed on a device|None|
|Last Update Time|string|None|False|The last time a device was updated in the Automox platform|None|
|Device Name|string|None|False|The device name|None|
|Needs Attention|boolean|None|False|Whether a device currently needs attention|None|
|Needs Reboot|boolean|None|False|Whether a device needs rebooted|None|
|Next Patch Time|string|None|False|The time for the next device patch|None|
|Organization ID|integer|None|False|The organization identifier of a device|None|
|Operating System Family|string|None|False|The operating system family of a device|None|
|Operating System|string|None|False|The name of the operating system of a device|None|
|Operating System Version|string|None|False|The operating system version of a device|None|
|Patches|integer|None|False|The number of patches currently identified for a device|None|
|Pending|boolean|None|False|Whether work is pending on a device|None|
|Pending Patches|integer|None|False|The number of pending patches for a device|None|
|Reboot Is Delayed By Notification|boolean|None|False|Whether rebooting is delayed by a device notification|None|
|Reboot Is Delayed By User|boolean|None|False|Whether rebooting is delayed by a user|None|
|Serial Number|string|None|False|The serial number of a device|None|
|Server Group ID|integer|None|False|The server group identifier of a device|None|
|Status|device_status_details|None|False|The device status details|None|
|Tags|[]string|None|False|List of tags|None|
  
**device_software**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Creation Time|string|None|False|The time when the software package was known|None|
|CVE Score|string|None|False|The CVE score associated with the software package|None|
|CVEs|[]string|None|False|List of CVEs associated to software package|None|
|Deferred Until|string|None|False|The datetime for when the software package was deferred for installation|None|
|Software Display Name|string|None|False|The display name of the software package|None|
|Software ID|integer|None|True|The software ID|None|
|Ignored Status|boolean|None|False|Whether the software package is ignored on the device|None|
|Installed Status|boolean|None|False|Whether the software package is installed on the device|None|
|Is Uninstallable|boolean|None|False|Whether the software package can be uninstalled|None|
|Software Name|string|None|True|The name of the software package|None|
|Organization ID|integer|None|False|The organization identifier of the software package|None|
|Operating System Name|string|None|False|The operating system associated with the software package|None|
|Operating System Version|string|None|False|The operating system version associated with the software package|None|
|Package ID|integer|None|True|The software package ID|None|
|Requires Reboot|boolean|None|False|Whether the device requires reboot for the software package to be installed|None|
|Device ID|integer|None|True|The device identifier for where the software exists|None|
|Severity|string|None|False|The severity associated with the software package|None|
|Software ID|integer|None|True|The software ID|None|
|Version|string|None|False|The version of the software package|None|
  
**policy**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Policy Configuration|object|None|False|The configuration of the policy|None|
|Policy ID|integer|None|True|The policy identifier|None|
|Policy Name|string|None|False|The name of the policy|None|
|Organization ID|integer|None|True|The organization identifier of the policy|None|
|Policy Type Name|string|None|False|The type of policy|None|
|Device Group IDs|[]integer|None|False|List of identifiers for device groups assigned to the policy|None|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Enable OS Auto Update|boolean|None|False|Enable operating system auto update|None|
|Group ID|integer|None|True|The group identifier|None|
|Group Name|string|None|False|The name of the group|None|
|Notes|string|None|False|Notes defined for the group|None|
|Organization ID|integer|None|True|The organization identifier of the group|None|
|Parent Server Group ID|integer|None|False|The identifier of the parent group|None|
|Policies|[]integer|None|False|List of policies assigned to group|None|
|Refresh Interval|integer|None|False|Frequency of device refreshes in minutes|None|
|Device Count|integer|None|False|Number of devices assigned to group|None|
|Color|string|None|False|Automox console highlight color for the group|None|
  
**event**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Creation Time|string|None|False|Creation time of event|None|
|Event Data|object|None|False|Data included with event|None|
|Event ID|integer|None|True|Identifier of event|None|
|Event name|string|None|True|Name of event|None|
|Organization ID|integer|None|False|Identifier of organization|None|
|Policy ID|integer|None|False|Identifier of policy|None|
|Policy Name|string|None|False|Name of policy|None|
|Policy Type|string|None|False|Type of policy|None|
|Device ID|integer|None|False|Identifier of device|None|
|Device Name|string|None|False|Name of device|None|
|User ID|integer|None|False|Identifier of user|None|
  
**action_set_user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|False|The email of the user|None|
|First Name|string|None|False|The first name of the user|None|
|User ID|integer|None|True|The user identifier|None|
|Last Name|string|None|False|The last name of the user|None|
  
**action_set_issues**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Unknown Host Count|integer|None|False|Number of hosts that are unknown within the action set|None|
  
**action_set_statistics**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Issues|action_set_issues|None|False|Issues associated with the action set|None|
  
**action_set_source**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Source Name|string|None|False|Name of the source|None|
|Source Type|string|None|False|Type of the source|None|
  
**action_set_solution_counts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Solution Count|integer|None|False|Number of solutions associated with the action set|None|
|Device Count|integer|None|False|Number of devices associated with the action set|None|
|Vulnerability Count|integer|None|False|Number of vulnerabilities associated with the action set|None|
  
**action_set_solution_summary**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Patch Now|action_set_solution_counts|None|False|Number of devices that will be patched immediately|None|
|Patch with Worklet|action_set_solution_counts|None|False|Number of devices that will be patched with a worklet|None|
  
**action_set**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Configuration ID|string|None|False|Identifier of the configuration, only applicable for Automated Vulnerability Remediation (AVR) action sets|None|
|Created At|string|None|False|Datetime the action set was created|None|
|Created By|action_set_user|None|False|action set creation details|None|
|Action Set ID|integer|None|True|Identifier of the action set|None|
|Organization ID|integer|None|False|Identifier of the organization|None|
|Solutions|action_set_solution_summary|None|False|Solutions associated with the action set|None|
|Action Set Source|action_set_source|None|False|Source of the action set|None|
|Action Set Statistics|action_set_statistics|None|False|Statistics of the action set|None|
|Action Set Status|string|None|False|Status of the action set|None|
|Uploaded At|string|None|False|Datetime the action set was uploaded|None|
  
**action_set_action**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|patch-now|True|The action to execute for the associated remediation|None|
|Solution ID|integer|None|True|The solution ID associated with the action|None|
  
**action_set_issue**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Issue ID|integer|None|True|Identifier of the issue|None|
|Issue Details|object|None|True|Details of the issue|None|
|Issue Type|string|None|True|Type of issue|None|
  
**solution_device**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Custom Name|string|None|False|Custom name of the device|None|
|Deleted|boolean|None|False|Whether the device is deleted from Automox|None|
|Device ID|integer|None|True|Identifier of device|None|
|Private IP Addresses|[]string|None|False|List of private IP addresses for the device|None|
|Device Name|string|None|False|Name of the device|None|
|Device Status|string|None|False|Status of remediation for the device|None|
  
**solution_vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Vulneability ID|string|None|True|Identifier of the vulnerability, typically a CVE|None|
|Severity|string|None|False|Severity of the vulnerability|None|
|Summary|string|None|False|Summary of the vulnerability|None|
|Title|string|None|False|Title of the vulnerability|None|
  
**solution**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Device IDs|[]integer|None|False|List of device identifiers associated with the solution. This is a helper field to make executing actions easier. It does not exist on the Automox API.|[1234, 5678]|
|Devices|[]solution_device|None|False|List of devices associated with the solution|[{'id': 1234, 'name': 'device-1', 'custom_name': 'custom-name', 'status': 'in_progress', 'deleted': False, 'ip_addrs_private': ['10.0.0.1']}]|
|Solution ID|integer|None|True|Identifier of solution|1234|
|Remediation Type|string|None|False|Type of remediation|patch-with-worklet|
|Solution Details|object|None|False|Details of the solution. This can include package information and other details depending on the solution type|{'solution_id': 'office-click-to-run-upgrade-latest', 'solution_type': 'workaround', 'solution_summary': 'Upgrade to the latest version of Microsoft Office', 'solution_fix': 'Install Office Click-To-Run updates through any installed Office application. Go to File &gt; Account (or Office Account if you opened Outlook). Under Product Information, choose Update Options &gt; Update Now.'}|
|Solution Type|string|None|False|Type of solution|rapid7-solution|
|Vulnerabilities|[]solution_vulnerability|None|False|List of vulnerabilities associated with the solution|[{'id': 'CVE-2019-1297', 'title': 'Microsoft Excel Remote Code Execution Vulnerability', 'summary': 'A remote code execution vulnerability exists in Microsoft Excel software when the software fails to properly handle objects in memory. An attacker who successfully exploited the vulnerability could run arbitrary code in the context of the current user. If the current user is logged on with administrative user rights, an attacker could take control of the affected system. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights. Users whose accounts are configured to have fewer user rights on the system could be less impacted than users who operate with administrative user rights. Exploitation of the vulnerability requires that a user open a specially crafted file with an affected version of Microsoft Excel. In an email attack scenario, an attacker could exploit the vulnerability by sending the specially crafted file to the user and convincing the user to open the file. In a web-based attack scenario, an attacker could host a website (or leverage a compromised website that accepts or hosts user-provided content) containing a specially crafted file designed to exploit the vulnerability. An attacker would have no way to force users to visit the website. Instead, an attacker would have to convince users to click a link, typically by way of an enticement in an email or instant message, and then convince them to open the specially crafted file. The security update addresses the vulnerability by correcting how Microsoft Excel handles objects in memory.', 'severity': 'high'}, {'id': 'CVE-2021-42292', 'title': 'Microsoft Excel Security Feature Bypass Vulnerability', 'summary': '', 'severity': 'high'}]|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 2.0.0 - Fix Vulnerability Sync API Actions | `Action`: Added - Delete Vulnerability Sync Action Set | `Action`: Added - Execute Vulnerability Sync Actions | `Action`: Added - List Vulnerability Sync Action Set Issues |`Action`: Added - List Vulnerability Sync Action Set Solutions | `Action`: Added - List Vulnerability Sync Action Sets | `Action`: Added - Get Vulnerability Sync Action Set | `Action`: Updated - Upload Vulnerability Sync File | `Action`: Updated - Get Devices | `Action`: Deleted - Action on Vulnerability Sync Batch | `Action`: Deleted - Vulnerability Sync Task | `Action`: Deleted - Get Vulnerability Sync Batch | `Action`: Deleted - List Vulnerability Sync Batches | `Action`: Deleted - List Vulnerability Sync Tasks
* 1.2.0 - Get device by IP and Get device by hostname: fix validation issue when IP or hostname not found | Add unit tests
* 1.1.1 - Fix undefined org ID passed to actions when not required | Record outcome of connection tests
* 1.1.0 - Add `report source` as optional input parameter to Upload Vulnerability Sync File action | Add report source to batch type
* 1.0.0 - Initial plugin

# Links

* [Automox](https://www.automox.com/)

## References

* [Automox Developer Portal](https://developer.automox.com/)
* [Managing API Keys](https://support.automox.com/help/managing-keys)
* [Event Types for Get Automox Events action](https://developer.automox.com/openapi/axconsole/operation/getEvents/#!in=query&path=eventName&t=request)

