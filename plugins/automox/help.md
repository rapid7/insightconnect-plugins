# Description

Automox is modernizing IT operations with continuous visibility, insight, and agility for your entire IT environment

# Key Features
  
* Device Management  
* Patch Management

# Requirements


# Supported Product Versions
  
* All as of 12/29/2023

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
  
This action is used to create an Automox group

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
|group|group|True|Detailed information about the created group|{"id":1234,"organization_id":1234,"name":"Default","refresh_interval":1440,"parent_server_group_id":0,"ui_color":"#059F1D","server_count":5,"wsus_config":{"id":1234,"server_group_id":1234,"created_at":"2022-09-13T14:26:19+0000","updated_at":"2022-09-13T14:26:19+0000"},"policies":[1234,1235]}|
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "group": {
    "id": 1234,
    "name": "Default",
    "organization_id": 1234,
    "parent_server_group_id": 0,
    "policies": [
      1234,
      1235
    ],
    "refresh_interval": 1440,
    "server_count": 5,
    "ui_color": "#059F1D",
    "wsus_config": {
      "created_at": "2022-09-13T14:26:19+0000",
      "id": 1234,
      "server_group_id": 1234,
      "updated_at": "2022-09-13T14:26:19+0000"
    }
  },
  "success": true
}
```

#### Delete Device
  
This action is used to delete an Automox device

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
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Group
  
This action is used to delete an Automox group

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
  
This action is used to delete a vulnerability sync action set and all associated data

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
  
This action is used to launch remediation for patch and worklet remediations

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
  
This action is used to find an Automox device by hostname

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
|device|device|False|The matched Automox device|{"id":1234,"agent_version":"1.42.13","compliant":true,"create_time":"2023-04-13T19:45:45+0000","detail":{"RAM":"8589934592","CPU":"Intel(R) Core(TM) i7-8700B CPU @ 3.20GHz","MDM_SERVER":"none","VERSION":"MacBookPro16,1","NICS":[{"CONNECTED":true,"VENDOR":"Apple","DEVICE":"en0","TYPE":"enet","MAC":"00:00:00:00:00:00","IPS":["192.168.1.1"]}],"VOLUME":[{"FSTYPE":"APFS","LABEL":"macOS","AVAIL":"62704803840","FREE":"21316517888","IS_SYSTEM_DISK":"true","VOLUME":"/dev/disk1s5s1"},{"VOLUME":"/dev/disk1s3","FSTYPE":"APFS","LABEL":"Recovery","AVAIL":"62704803840","FREE":"21316517888","IS_SYSTEM_DISK":"false"}],"VENDOR":"Apple","MDM_PROFILE_INSTALLED":"false","LAST_USER_LOGON":{"SRC":"console","USER":"root","TIME":"2023-04-14 16:05"},"UPDATE_SOURCE_CHECK":{"CONNECTED":"true","ERROR":"Succeded"},"SERIAL":"C00000000001","DISKS":[{"TYPE":"VMware Virtual NVMe Disk","SIZE":"62914560000"}],"IPS":["192.168.1.1"],"MODEL":"MacBook Pro","AUTO_UPDATE_OPTIONS":{"OPTIONS":"Automatic Check for Updates, Install system data updates, Install system security updates","ENABLED":"0"}},"display_name":"apple","ip_addrs":["0.0.0.0"],"ip_addrs_private":["192.168.1.1"],"is_compatible":true,"last_disconnect_time":"2023-04-14T23:07:04+0000","last_logged_in_user":"root","last_process_time":"2023-04-14T22:40:56+0000","last_refresh_time":"2023-04-14T23:06:27+0000","last_update_time":"2023-04-14T22:51:10+0000","name":"apple","needs_attention":true,"organization_id":1234,"os_family":"Mac","os_name":"OS X","os_version":"12.6.6","os_version_id":1234,"refresh_interval":1440,"serial_number":"C00000000001","server_group_id":1234,"status":{"device_status":"not-ready","agent_status":"disconnected","policy_status":"unmanaged"},"timezone":"UTC-0700","total_count":5,"uptime":"88632","uuid":"00000000-0000-0000-0000-000000000000"}|
  
Example output:

```
{
  "device": {
    "agent_version": "1.42.13",
    "compliant": true,
    "create_time": "2023-04-13T19:45:45+0000",
    "detail": {
      "AUTO_UPDATE_OPTIONS": {
        "ENABLED": "0",
        "OPTIONS": "Automatic Check for Updates, Install system data updates, Install system security updates"
      },
      "CPU": "Intel(R) Core(TM) i7-8700B CPU @ 3.20GHz",
      "DISKS": [
        {
          "SIZE": "62914560000",
          "TYPE": "VMware Virtual NVMe Disk"
        }
      ],
      "IPS": [
        "192.168.1.1"
      ],
      "LAST_USER_LOGON": {
        "SRC": "console",
        "TIME": "2023-04-14 16:05",
        "USER": "root"
      },
      "MDM_PROFILE_INSTALLED": "false",
      "MDM_SERVER": "none",
      "MODEL": "MacBook Pro",
      "NICS": [
        {
          "CONNECTED": true,
          "DEVICE": "en0",
          "IPS": [
            "192.168.1.1"
          ],
          "MAC": "00:00:00:00:00:00",
          "TYPE": "enet",
          "VENDOR": "Apple"
        }
      ],
      "RAM": "8589934592",
      "SERIAL": "C00000000001",
      "UPDATE_SOURCE_CHECK": {
        "CONNECTED": "true",
        "ERROR": "Succeded"
      },
      "VENDOR": "Apple",
      "VERSION": "MacBookPro16,1",
      "VOLUME": [
        {
          "AVAIL": "62704803840",
          "FREE": "21316517888",
          "FSTYPE": "APFS",
          "IS_SYSTEM_DISK": "true",
          "LABEL": "macOS",
          "VOLUME": "/dev/disk1s5s1"
        },
        {
          "AVAIL": "62704803840",
          "FREE": "21316517888",
          "FSTYPE": "APFS",
          "IS_SYSTEM_DISK": "false",
          "LABEL": "Recovery",
          "VOLUME": "/dev/disk1s3"
        }
      ]
    },
    "display_name": "apple",
    "id": 1234,
    "ip_addrs": [
      "0.0.0.0"
    ],
    "ip_addrs_private": [
      "192.168.1.1"
    ],
    "is_compatible": true,
    "last_disconnect_time": "2023-04-14T23:07:04+0000",
    "last_logged_in_user": "root",
    "last_process_time": "2023-04-14T22:40:56+0000",
    "last_refresh_time": "2023-04-14T23:06:27+0000",
    "last_update_time": "2023-04-14T22:51:10+0000",
    "name": "apple",
    "needs_attention": true,
    "organization_id": 1234,
    "os_family": "Mac",
    "os_name": "OS X",
    "os_version": "12.6.6",
    "os_version_id": 1234,
    "refresh_interval": 1440,
    "serial_number": "C00000000001",
    "server_group_id": 1234,
    "status": {
      "agent_status": "disconnected",
      "device_status": "not-ready",
      "policy_status": "unmanaged"
    },
    "timezone": "UTC-0700",
    "total_count": 5,
    "uptime": "88632",
    "uuid": "00000000-0000-0000-0000-000000000000"
  }
}
```

#### Get Device by IP Address
  
This action is used to find an Automox device by IP address

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
|device|device|False|The matched Automox device|{"id":1234,"agent_version":"1.42.13","compliant":true,"create_time":"2023-04-13T19:45:45+0000","detail":{"RAM":"8589934592","CPU":"Intel(R) Core(TM) i7-8700B CPU @ 3.20GHz","MDM_SERVER":"none","VERSION":"MacBookPro16,1","NICS":[{"CONNECTED":true,"VENDOR":"Apple","DEVICE":"en0","TYPE":"enet","MAC":"00:00:00:00:00:00","IPS":["192.168.1.1"]}],"VOLUME":[{"FSTYPE":"APFS","LABEL":"macOS","AVAIL":"62704803840","FREE":"21316517888","IS_SYSTEM_DISK":"true","VOLUME":"/dev/disk1s5s1"},{"VOLUME":"/dev/disk1s3","FSTYPE":"APFS","LABEL":"Recovery","AVAIL":"62704803840","FREE":"21316517888","IS_SYSTEM_DISK":"false"}],"VENDOR":"Apple","MDM_PROFILE_INSTALLED":"false","LAST_USER_LOGON":{"SRC":"console","USER":"root","TIME":"2023-04-14 16:05"},"UPDATE_SOURCE_CHECK":{"CONNECTED":"true","ERROR":"Succeded"},"SERIAL":"C00000000001","DISKS":[{"TYPE":"VMware Virtual NVMe Disk","SIZE":"62914560000"}],"IPS":["192.168.1.1"],"MODEL":"MacBook Pro","AUTO_UPDATE_OPTIONS":{"OPTIONS":"Automatic Check for Updates, Install system data updates, Install system security updates","ENABLED":"0"}},"display_name":"apple","ip_addrs":["0.0.0.0"],"ip_addrs_private":["192.168.1.1"],"is_compatible":true,"last_disconnect_time":"2023-04-14T23:07:04+0000","last_logged_in_user":"root","last_process_time":"2023-04-14T22:40:56+0000","last_refresh_time":"2023-04-14T23:06:27+0000","last_update_time":"2023-04-14T22:51:10+0000","name":"apple","needs_attention":true,"organization_id":1234,"os_family":"Mac","os_name":"OS X","os_version":"12.6.6","os_version_id":1234,"refresh_interval":1440,"serial_number":"C00000000001","server_group_id":1234,"status":{"device_status":"not-ready","agent_status":"disconnected","policy_status":"unmanaged"},"timezone":"UTC-0700","total_count":5,"uptime":"88632","uuid":"00000000-0000-0000-0000-000000000000"}|
  
Example output:

```
{
  "device": {
    "agent_version": "1.42.13",
    "compliant": true,
    "create_time": "2023-04-13T19:45:45+0000",
    "detail": {
      "AUTO_UPDATE_OPTIONS": {
        "ENABLED": "0",
        "OPTIONS": "Automatic Check for Updates, Install system data updates, Install system security updates"
      },
      "CPU": "Intel(R) Core(TM) i7-8700B CPU @ 3.20GHz",
      "DISKS": [
        {
          "SIZE": "62914560000",
          "TYPE": "VMware Virtual NVMe Disk"
        }
      ],
      "IPS": [
        "192.168.1.1"
      ],
      "LAST_USER_LOGON": {
        "SRC": "console",
        "TIME": "2023-04-14 16:05",
        "USER": "root"
      },
      "MDM_PROFILE_INSTALLED": "false",
      "MDM_SERVER": "none",
      "MODEL": "MacBook Pro",
      "NICS": [
        {
          "CONNECTED": true,
          "DEVICE": "en0",
          "IPS": [
            "192.168.1.1"
          ],
          "MAC": "00:00:00:00:00:00",
          "TYPE": "enet",
          "VENDOR": "Apple"
        }
      ],
      "RAM": "8589934592",
      "SERIAL": "C00000000001",
      "UPDATE_SOURCE_CHECK": {
        "CONNECTED": "true",
        "ERROR": "Succeded"
      },
      "VENDOR": "Apple",
      "VERSION": "MacBookPro16,1",
      "VOLUME": [
        {
          "AVAIL": "62704803840",
          "FREE": "21316517888",
          "FSTYPE": "APFS",
          "IS_SYSTEM_DISK": "true",
          "LABEL": "macOS",
          "VOLUME": "/dev/disk1s5s1"
        },
        {
          "AVAIL": "62704803840",
          "FREE": "21316517888",
          "FSTYPE": "APFS",
          "IS_SYSTEM_DISK": "false",
          "LABEL": "Recovery",
          "VOLUME": "/dev/disk1s3"
        }
      ]
    },
    "display_name": "apple",
    "id": 1234,
    "ip_addrs": [
      "0.0.0.0"
    ],
    "ip_addrs_private": [
      "192.168.1.1"
    ],
    "is_compatible": true,
    "last_disconnect_time": "2023-04-14T23:07:04+0000",
    "last_logged_in_user": "root",
    "last_process_time": "2023-04-14T22:40:56+0000",
    "last_refresh_time": "2023-04-14T23:06:27+0000",
    "last_update_time": "2023-04-14T22:51:10+0000",
    "name": "apple",
    "needs_attention": true,
    "organization_id": 1234,
    "os_family": "Mac",
    "os_name": "OS X",
    "os_version": "12.6.6",
    "os_version_id": 1234,
    "refresh_interval": 1440,
    "serial_number": "C00000000001",
    "server_group_id": 1234,
    "status": {
      "agent_status": "disconnected",
      "device_status": "not-ready",
      "policy_status": "unmanaged"
    },
    "timezone": "UTC-0700",
    "total_count": 5,
    "uptime": "88632",
    "uuid": "00000000-0000-0000-0000-000000000000"
  }
}
```

#### Get Device Software
  
This action is used to retrieve a list of software installed on a device

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
|software|[]device_software|False|List of software on device|[{"id":1234,"server_id":1234,"package_id":1234,"software_id":1234,"installed":true,"name":"com.apple.appleseed.FeedbackAssistant","display_name":"Feedback Assistant","version":"5.1","repo":"Apple-System","package_version_id":1234,"os_name":"OS X","os_version":"12.2","os_version_id":1234,"create_time":"2021-12-20T16:21:21+0000","organization_id":1234},{"id":1234,"server_id":1234,"package_id":1234,"software_id":1234,"installed":true,"name":"com.apple.calculator","display_name":"Calculator","version":"10.16","repo":"Apple-System","package_version_id":1234,"os_name":"OS X","os_version":"12.2","os_version_id":1234,"create_time":"2021-12-26T17:23:19+0000","organization_id":1234}]|
  
Example output:

```
{
  "software": [
    {
      "create_time": "2021-12-20T16:21:21+0000",
      "display_name": "Feedback Assistant",
      "id": 1234,
      "installed": true,
      "name": "com.apple.appleseed.FeedbackAssistant",
      "organization_id": 1234,
      "os_name": "OS X",
      "os_version": "12.2",
      "os_version_id": 1234,
      "package_id": 1234,
      "package_version_id": 1234,
      "repo": "Apple-System",
      "server_id": 1234,
      "software_id": 1234,
      "version": "5.1"
    },
    {
      "create_time": "2021-12-26T17:23:19+0000",
      "display_name": "Calculator",
      "id": 1234,
      "installed": true,
      "name": "com.apple.calculator",
      "organization_id": 1234,
      "os_name": "OS X",
      "os_version": "12.2",
      "os_version_id": 1234,
      "package_id": 1234,
      "package_version_id": 1234,
      "repo": "Apple-System",
      "server_id": 1234,
      "software_id": 1234,
      "version": "10.16"
    }
  ]
}
```

#### Get Vulnerability Sync Action Set
  
This action is used to retrieve details for a specified vulnerability sync action set

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
|action_set|action_set|True|Details of a specified vulnerability sync action_set|{"created_at":"2023-10-04T02:55:55+0000","created_by_user":{"email":"user@example.com","firstname":"User","id":1234,"lastname":"Example"},"id":1234,"organization_id":1234,"source":{"name":"example.csv","type":"generic"},"statistics":{"issues":{"unknown-host":{"count":1}},"solutions":{"patch-now":{"count":0,"device_count":0,"vulnerability_count":0},"patch-with-worklet":{"count":0,"device_count":0,"vulnerability_count":0}}},"status":"ready","updated_at":"2023-10-04T02:56:00+0000","updated_by_user":{"email":"user@example.com","firstname":"User","id":1234,"lastname":"Example"}}|
  
Example output:

```
{
  "action_set": {
    "created_at": "2023-10-04T02:55:55+0000",
    "created_by_user": {
      "email": "user@example.com",
      "firstname": "User",
      "id": 1234,
      "lastname": "Example"
    },
    "id": 1234,
    "organization_id": 1234,
    "source": {
      "name": "example.csv",
      "type": "generic"
    },
    "statistics": {
      "issues": {
        "unknown-host": {
          "count": 1
        }
      },
      "solutions": {
        "patch-now": {
          "count": 0,
          "device_count": 0,
          "vulnerability_count": 0
        },
        "patch-with-worklet": {
          "count": 0,
          "device_count": 0,
          "vulnerability_count": 0
        }
      }
    },
    "status": "ready",
    "updated_at": "2023-10-04T02:56:00+0000",
    "updated_by_user": {
      "email": "user@example.com",
      "firstname": "User",
      "id": 1234,
      "lastname": "Example"
    }
  }
}
```

#### List Devices
  
This action is used to retrieve Automox managed devices

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
|devices|[]device|False|List of Automox managed devices|[{"id":1234,"agent_version":"1.42.22","compliant":true,"create_time":"2023-11-14T00:32:23+0000","detail":{"CPU":"Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz","VENDOR":"Xen","MODEL":"HVM domU","VERSION":"4.11.amazon","RAM":"1014943744","LAST_USER_LOGON":{"TIME":"2023-11-14T20:23:00+00:00"},"SERIAL":"00000000-0000-0000-0000-000000009001","IPS":["10.1.1.1","1234::1234:1234:1234:1234"],"DISKS":[{"SIZE":"8589934592","TYPE":"unknown"}],"NICS":[{"IPS":["10.1.1.1","1234::1234:1234:1234:1234"],"CONNECTED":true,"VENDOR":"Unknown","DEVICE":"eth0","TYPE":"enet","MAC":"11:11:11:11:11:11"}],"VOLUME":[{"IS_SYSTEM_DISK":"true","VOLUME":"/dev/root","FSTYPE":"ext4","LABEL":"cloudimg-rootfs","AVAIL":"8141574144","FREE":"6285549568"},{"FSTYPE":"vfat","LABEL":"UEFI","AVAIL":"109422592","FREE":"103973888","IS_SYSTEM_DISK":"false","VOLUME":"/dev/xvda15"}],"FQDNS":["youubuntu.example.com"]},"display_name":"youbuntu","instance_id":"i-0b466e0e804798a23","ip_addrs":["0.0.0.0"],"ip_addrs_private":["10.1.1.1","1234::1234:1234:1234:1234"],"is_compatible":true,"last_disconnect_time":"2023-11-14T00:52:27+0000","last_refresh_time":"2023-11-14T00:33:12+0000","name":"youbuntu","organization_id":1234,"os_family":"Linux","os_name":"Ubuntu","os_version":"20.04.4","os_version_id":6220,"patches":201,"refresh_interval":1440,"serial_number":"00000000-0000-0000-0000-000000000000","server_group_id":1234,"status":{"device_status":"ready","agent_status":"connected","policy_status":"compliant"},"timezone":"UTC+0000","total_count":5,"uptime":"392","uuid":"00000000-0000-0000-0000-000000000000"}]|
  
Example output:

```
{
  "devices": [
    {
      "agent_version": "1.42.22",
      "compliant": true,
      "create_time": "2023-11-14T00:32:23+0000",
      "detail": {
        "CPU": "Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz",
        "DISKS": [
          {
            "SIZE": "8589934592",
            "TYPE": "unknown"
          }
        ],
        "FQDNS": [
          "youubuntu.example.com"
        ],
        "IPS": [
          "10.1.1.1",
          "1234::1234:1234:1234:1234"
        ],
        "LAST_USER_LOGON": {
          "TIME": "2023-11-14T20:23:00+00:00"
        },
        "MODEL": "HVM domU",
        "NICS": [
          {
            "CONNECTED": true,
            "DEVICE": "eth0",
            "IPS": [
              "10.1.1.1",
              "1234::1234:1234:1234:1234"
            ],
            "MAC": "11:11:11:11:11:11",
            "TYPE": "enet",
            "VENDOR": "Unknown"
          }
        ],
        "RAM": "1014943744",
        "SERIAL": "00000000-0000-0000-0000-000000009001",
        "VENDOR": "Xen",
        "VERSION": "4.11.amazon",
        "VOLUME": [
          {
            "AVAIL": "8141574144",
            "FREE": "6285549568",
            "FSTYPE": "ext4",
            "IS_SYSTEM_DISK": "true",
            "LABEL": "cloudimg-rootfs",
            "VOLUME": "/dev/root"
          },
          {
            "AVAIL": "109422592",
            "FREE": "103973888",
            "FSTYPE": "vfat",
            "IS_SYSTEM_DISK": "false",
            "LABEL": "UEFI",
            "VOLUME": "/dev/xvda15"
          }
        ]
      },
      "display_name": "youbuntu",
      "id": 1234,
      "instance_id": "i-0b466e0e804798a23",
      "ip_addrs": [
        "0.0.0.0"
      ],
      "ip_addrs_private": [
        "10.1.1.1",
        "1234::1234:1234:1234:1234"
      ],
      "is_compatible": true,
      "last_disconnect_time": "2023-11-14T00:52:27+0000",
      "last_refresh_time": "2023-11-14T00:33:12+0000",
      "name": "youbuntu",
      "organization_id": 1234,
      "os_family": "Linux",
      "os_name": "Ubuntu",
      "os_version": "20.04.4",
      "os_version_id": 6220,
      "patches": 201,
      "refresh_interval": 1440,
      "serial_number": "00000000-0000-0000-0000-000000000000",
      "server_group_id": 1234,
      "status": {
        "agent_status": "connected",
        "device_status": "ready",
        "policy_status": "compliant"
      },
      "timezone": "UTC+0000",
      "total_count": 5,
      "uptime": "392",
      "uuid": "00000000-0000-0000-0000-000000000000"
    }
  ]
}
```

#### List Groups
  
This action is used to list Automox groups

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
|groups|[]group|False|List of Automox groups|[{"id":1234,"organization_id":1234,"name":"Default","refresh_interval":1440,"parent_server_group_id":0,"ui_color":"#059F1D","server_count":5,"wsus_config":{"id":1234,"server_group_id":1234,"created_at":"2022-09-13T14:26:19+0000","updated_at":"2022-09-13T14:26:19+0000"},"policies":[1234,1235]},{"id":1235,"organization_id":1234,"name":"A Server Group","refresh_interval":1440,"parent_server_group_id":1234,"ui_color":"#059F1D","wsus_config":{"id":1234,"server_group_id":1234,"created_at":"2022-09-13T14:26:32+0000","updated_at":"2022-09-13T14:26:32+0000"},"policies":[1234,1235]}]|
  
Example output:

```
{
  "groups": [
    {
      "id": 1234,
      "name": "Default",
      "organization_id": 1234,
      "parent_server_group_id": 0,
      "policies": [
        1234,
        1235
      ],
      "refresh_interval": 1440,
      "server_count": 5,
      "ui_color": "#059F1D",
      "wsus_config": {
        "created_at": "2022-09-13T14:26:19+0000",
        "id": 1234,
        "server_group_id": 1234,
        "updated_at": "2022-09-13T14:26:19+0000"
      }
    },
    {
      "id": 1235,
      "name": "A Server Group",
      "organization_id": 1234,
      "parent_server_group_id": 1234,
      "policies": [
        1234,
        1235
      ],
      "refresh_interval": 1440,
      "ui_color": "#059F1D",
      "wsus_config": {
        "created_at": "2022-09-13T14:26:32+0000",
        "id": 1234,
        "server_group_id": 1234,
        "updated_at": "2022-09-13T14:26:32+0000"
      }
    }
  ]
}
```

#### List Organization Users
  
This action is used to retrieve users of the Automox organization

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
|users|[]user|False|List of Automox users|[{"id":1234,"uuid":"00000000-0000-0000-0000-000000000000","firstname":"User","lastname":"Example","email":"user@example.com","prefs":[{"user_id":1234,"pref_name":"notify.system.add","value":"false"},{"user_id":1234,"pref_name":"notify.weeklydigest","value":"true"},{"user_id":1234,"pref_name":"user.tfa","value":"email"}],"orgs":[{"id":1234,"zone_id":"00000000-0000-0000-0000-000000000000","name":"Global Zone","trial_end_time":"2024-02-03T00:00:00+00:00","create_time":"2021-10-20T04:03:25+0000","plan":"manage","access_key":"00000000-0000-0000-0000-000000000000"},{"id":1235,"zone_id":"00000000-0000-0000-0000-000000000000","name":"Local Zone","trial_end_time":"2021-11-03T00:00:00+00:00","trial_expired":true,"create_time":"2021-10-26T08:14:25+0000","plan":"manage","parent_id":1234,"access_key":"00000000-0000-0000-0000-000000000000"}]}]|
  
Example output:

```
{
  "users": [
    {
      "email": "user@example.com",
      "firstname": "User",
      "id": 1234,
      "lastname": "Example",
      "orgs": [
        {
          "access_key": "00000000-0000-0000-0000-000000000000",
          "create_time": "2021-10-20T04:03:25+0000",
          "id": 1234,
          "name": "Global Zone",
          "plan": "manage",
          "trial_end_time": "2024-02-03T00:00:00+00:00",
          "zone_id": "00000000-0000-0000-0000-000000000000"
        },
        {
          "access_key": "00000000-0000-0000-0000-000000000000",
          "create_time": "2021-10-26T08:14:25+0000",
          "id": 1235,
          "name": "Local Zone",
          "parent_id": 1234,
          "plan": "manage",
          "trial_end_time": "2021-11-03T00:00:00+00:00",
          "trial_expired": true,
          "zone_id": "00000000-0000-0000-0000-000000000000"
        }
      ],
      "prefs": [
        {
          "pref_name": "notify.system.add",
          "user_id": 1234,
          "value": "false"
        },
        {
          "pref_name": "notify.weeklydigest",
          "user_id": 1234,
          "value": "true"
        },
        {
          "pref_name": "user.tfa",
          "user_id": 1234,
          "value": "email"
        }
      ],
      "uuid": "00000000-0000-0000-0000-000000000000"
    }
  ]
}
```

#### List Organizations
  
This action is used to retrieve Automox organizations

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|organizations|[]organization|True|List of Automox organizations|[{"id":1234,"name":"GlobalZone","create_time":"2021-10-20T04:03:25+0000","access_key":"00000000-0000-0000-0000-000000000000","trial_end_time":"2024-02-03T00:00:00+0000","sub_plan":"FULL","rate_id":1,"billing_name":"Test","billing_email":"user@example.com","uuid":"00000000-0000-0000-0000-0000000000000","device_count":2},{"id":1235,"name":"AnotherOne","create_time":"2021-10-26T08:14:25+0000","access_key":"00000000-0000-0000-0000-000000000000","trial_end_time":"2021-11-03T00:00:00+0000","trial_expired":true,"sub_plan":"FULL","rate_id":1,"parent_id":1234,"uuid":"00000000-0000-0000-0000-000000000000"}]|
  
Example output:

```
{
  "organizations": [
    {
      "access_key": "00000000-0000-0000-0000-000000000000",
      "billing_email": "user@example.com",
      "billing_name": "Test",
      "create_time": "2021-10-20T04:03:25+0000",
      "device_count": 2,
      "id": 1234,
      "name": "GlobalZone",
      "rate_id": 1,
      "sub_plan": "FULL",
      "trial_end_time": "2024-02-03T00:00:00+0000",
      "uuid": "00000000-0000-0000-0000-0000000000000"
    },
    {
      "access_key": "00000000-0000-0000-0000-000000000000",
      "create_time": "2021-10-26T08:14:25+0000",
      "id": 1235,
      "name": "AnotherOne",
      "parent_id": 1234,
      "rate_id": 1,
      "sub_plan": "FULL",
      "trial_end_time": "2021-11-03T00:00:00+0000",
      "trial_expired": true,
      "uuid": "00000000-0000-0000-0000-000000000000"
    }
  ]
}
```

#### List Policies
  
This action is used to retrieve Automox policies

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
|policies|[]policy|False|List of Automox policies|[{"id":1234,"uuid":"00000000-0000-0000-0000-000000000000","name":"Test notification","policy_type_name":"custom","organization_id":103871,"configuration":{"os_family":"Windows","notify_reboot_user":true,"notify_deferred_reboot_user":true,"pending_reboot_deferral_enabled":true,"custom_pending_reboot_notification_message":"Updates require restart: Please save your work.","notify_deferred_reboot_user_message_timeout":15,"custom_pending_reboot_notification_max_delays":3,"custom_pending_reboot_notification_message_mac":"Updates require restart: Please save your work.","custom_pending_reboot_notification_deferment_periods":[1,4,8]},"schedule_time":"00:00","create_time":"2023-10-25T21:56:48+0000","server_groups":[1234],"server_count":5,"status":"inactive"}]|
  
Example output:

```
{
  "policies": [
    {
      "configuration": {
        "custom_pending_reboot_notification_deferment_periods": [
          1,
          4,
          8
        ],
        "custom_pending_reboot_notification_max_delays": 3,
        "custom_pending_reboot_notification_message": "Updates require restart: Please save your work.",
        "custom_pending_reboot_notification_message_mac": "Updates require restart: Please save your work.",
        "notify_deferred_reboot_user": true,
        "notify_deferred_reboot_user_message_timeout": 15,
        "notify_reboot_user": true,
        "os_family": "Windows",
        "pending_reboot_deferral_enabled": true
      },
      "create_time": "2023-10-25T21:56:48+0000",
      "id": 1234,
      "name": "Test notification",
      "organization_id": 103871,
      "policy_type_name": "custom",
      "schedule_time": "00:00",
      "server_count": 5,
      "server_groups": [
        1234
      ],
      "status": "inactive",
      "uuid": "00000000-0000-0000-0000-000000000000"
    }
  ]
}
```

#### List Vulnerability Sync Action Set Issues
  
This action is used to retrieve the issues identified for a specified vulnerability sync action set

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
|issues|[]action_set_issue|True|Issues associated with the specified vulnerability sync action_set|[{"id":1234,"issue_details":{"hostname":"WINDOWS-1234"},"issue_type":"unknown-host"},{"id":1234,"issue_details":{"hostname":"example-test-1234"},"issue_type":"unknown-host"}]|
  
Example output:

```
{
  "issues": [
    {
      "id": 1234,
      "issue_details": {
        "hostname": "WINDOWS-1234"
      },
      "issue_type": "unknown-host"
    },
    {
      "id": 1234,
      "issue_details": {
        "hostname": "example-test-1234"
      },
      "issue_type": "unknown-host"
    }
  ]
}
```

#### List Vulnerability Sync Action Set Solutions
  
This action is used to retrieve a list of vulnerability sync remediations

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
|solutions|[]solution|False|List of vulnerability sync Solutions|[{"device_ids":[1,2,3],"devices":[{"custom_name":"example1","id":1,"ip_addrs_private":["10.0.0.1","ffff::ffff:ffff:ffff:ffff"],"name":"example1","status":"pending"},{"custom_name":"example2","id":2,"ip_addrs_private":["10.0.0.2","ffff::ffff:ffff:ffff:ffff"],"name":"example2","status":"pending"},{"custom_name":"example3","id":3,"ip_addrs_private":["10.0.0.3","ffff::ffff:ffff:ffff:ffff"],"name":"example3","status":"pending"}],"id":1234,"organization_id":1234,"remediation_type":"patch-with-worklet","solution_type":"unmatched","vulnerabilities":[{"id":"CVE-2021-24111","severity":"high","title":".NET Framework Denial of Service Vulnerability"}]}]|
  
Example output:

```
{
  "solutions": [
    {
      "device_ids": [
        1,
        2,
        3
      ],
      "devices": [
        {
          "custom_name": "example1",
          "id": 1,
          "ip_addrs_private": [
            "10.0.0.1",
            "ffff::ffff:ffff:ffff:ffff"
          ],
          "name": "example1",
          "status": "pending"
        },
        {
          "custom_name": "example2",
          "id": 2,
          "ip_addrs_private": [
            "10.0.0.2",
            "ffff::ffff:ffff:ffff:ffff"
          ],
          "name": "example2",
          "status": "pending"
        },
        {
          "custom_name": "example3",
          "id": 3,
          "ip_addrs_private": [
            "10.0.0.3",
            "ffff::ffff:ffff:ffff:ffff"
          ],
          "name": "example3",
          "status": "pending"
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

#### List Vulnerability Sync Action Sets
  
This action is used to retrieve list of vulnerability sync batches

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
|action_sets|[]action_set|False|List of vulnerability sync action sets|[{"created_at":"2023-10-04T02:55:55+0000","created_by_user":{"email":"user@example.com","firstname":"User","id":1234,"lastname":"Example"},"id":1234,"organization_id":1234,"source":{"name":"example.csv","type":"generic"},"statistics":{"issues":{"unknown-host":{"count":1}},"solutions":{"patch-now":{"count":0,"device_count":0,"vulnerability_count":0},"patch-with-worklet":{"count":0,"device_count":0,"vulnerability_count":0}}},"status":"ready","updated_at":"2023-10-04T02:56:00+0000","updated_by_user":{"email":"user@example.com","firstname":"User","id":1234,"lastname":"Example"}}]|
  
Example output:

```
{
  "action_sets": [
    {
      "created_at": "2023-10-04T02:55:55+0000",
      "created_by_user": {
        "email": "user@example.com",
        "firstname": "User",
        "id": 1234,
        "lastname": "Example"
      },
      "id": 1234,
      "organization_id": 1234,
      "source": {
        "name": "example.csv",
        "type": "generic"
      },
      "statistics": {
        "issues": {
          "unknown-host": {
            "count": 1
          }
        },
        "solutions": {
          "patch-now": {
            "count": 0,
            "device_count": 0,
            "vulnerability_count": 0
          },
          "patch-with-worklet": {
            "count": 0,
            "device_count": 0,
            "vulnerability_count": 0
          }
        }
      },
      "status": "ready",
      "updated_at": "2023-10-04T02:56:00+0000",
      "updated_by_user": {
        "email": "user@example.com",
        "firstname": "User",
        "id": 1234,
        "lastname": "Example"
      }
    }
  ]
}
```

#### Run Device Command
  
This action is used to run a command on a device

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
  
This action is used to update Automox device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|custom_name|string|None|False|Custom name to set on device|None|custom-name|
|device_id|integer|None|True|Identifier of device|None|1234|
|exception|boolean|False|True|Exclude the device from reports and statistics|None|False|
|org_id|integer|None|False|Identifier of organization|None|1234|
|server_group_id|integer|None|False|Identifier of server group|None|1234|
|tags|[]string|None|False|List of tags|None|['tag1', 'tag2']|
  
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
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Update Group
  
This action is used to update an Automox group

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
  
This action is used to upload a CSV file to vulnerability sync for processing

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
  
This action is used to retrieve Automox events to trigger workflows

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
|event|event|True|Event with details|{"id":0,"name":"system.add","user_id":0,"server_id":0,"organization_id":0,"policy_id":0,"data":{"firstname":"string","lastname":"string","email":"string","orgname":"string","ip":"string","os":"string","systemname":"string","text":"string","status":0,"patches":"string"},"server_name":"string","policy_name":"string","policy_type_name":"patch","create_time":"2019-08-24T14:15:22Z"}|
  
Example output:

```
{
  "event": {
    "create_time": "2019-08-24T14:15:22Z",
    "data": {
      "email": "string",
      "firstname": "string",
      "ip": "string",
      "lastname": "string",
      "orgname": "string",
      "os": "string",
      "patches": "string",
      "status": 0,
      "systemname": "string",
      "text": "string"
    },
    "id": 0,
    "name": "system.add",
    "organization_id": 0,
    "policy_id": 0,
    "policy_name": "string",
    "policy_type_name": "patch",
    "server_id": 0,
    "server_name": "string",
    "user_id": 0
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
|Access Key|string|None|False|The access key of the organization|None|
|Creation Time|string|None|False|The datetime of when the organization was created|None|
|Organization ID|integer|None|True|The organization identifier of the user|None|
|Name|string|None|False|The name of the organization|None|
|Parent Organization ID|integer|None|False|The parent organization identifier|None|
|Plan|string|None|False|The plan of the organization|None|
|Trial End Time|string|None|False|The datetime of when the trial ends for the organization|None|
|Trial Expired|boolean|None|False|Whether the trial has expired for the organization|None|
|Zone ID|string|None|True|The zone identifier of the organization|None|
  
**user_rbac_role**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Role ID|integer|None|True|The role identifier|None|
|Name|string|None|False|The name of the role|None|
|Organization ID|integer|None|True|The organization identifier of the user role|None|
  
**user_pref**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Preference Name|string|None|True|The name of the preference|None|
|User ID|integer|None|True|The user identifier|None|
|Value|string|None|True|The value of the preference|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|False|The email of the user|None|
|Features|object|None|False|The features enabled for the user|None|
|First Name|string|None|False|The first name of the user|None|
|User ID|integer|None|True|The user identifier|None|
|Last Name|string|None|False|The last name of the user|None|
|Organizations|[]user_org|None|False|The organizations for which the user has access|None|
|Prefs|[]user_pref|None|None|The preferences for the user|None|
|Roles|[]user_rbac_role|None|False|The roles assigned to the user|None|
|SAML Enabled|boolean|None|False|Whether SAML has been enabled for the user|None|
|SSO Enabled|boolean|None|False|Whether SSO has been enabled for the user|None|
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
|Last Logged in User|string|None|False|The last logged in user of a device|None|
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
  
**action_set_issue_count**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Issue Count|integer|None|False|Number of issues associated with the action set|None|
  
**action_set_issues**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Unknown Host|action_set_issue_count|None|False|Hosts that are unknown to Automox within the action set|None|
  
**action_set_statistics**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Issues|action_set_issues|None|False|Issues associated with the action set|None|
|Solutions|action_set_solution_summary|None|False|Solutions associated with the action set|None|
  
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
  
* 3.0.0 - `Action`: Fixed -  Get Vulnerability Sync Action Set | `Action`: Fixed - List Vulnerability Sync Action Sets |
 `Action`: Updated - List Organization Users  
* 2.0.0 - Fix Vulnerability Sync API Actions | `Action`: Added - Delete Vulnerability Sync Action Set | `Action`: Added 
- Execute Vulnerability Sync Actions | `Action`: Added - List Vulnerability Sync Action Set Issues | `Action`: Added - 
List Vulnerability Sync Action Set Solutions | `Action`: Added - List Vulnerability Sync Action Sets | `Action`: Added -
 Get Vulnerability Sync Action Set | `Action`: Updated - Upload Vulnerability Sync File | `Action`: Updated - Get 
Devices | `Action`: Deleted - Action on Vulnerability Sync Batch | `Action`: Deleted - Vulnerability Sync Task | 
`Action`: Deleted - Get Vulnerability Sync Batch | `Action`: Deleted - List Vulnerability Sync Batches | `Action`: 
Deleted - List Vulnerability Sync Tasks  
* 1.2.0 - Get device by IP and Get device by hostname: fix validation issue when IP or hostname not found | Add unit 
tests  
* 1.1.1 - Fix undefined org ID passed to actions when not required | Record outcome of connection tests  
* 1.1.0 - Add `report source` as optional input parameter to Upload Vulnerability Sync File action | Add report source 
to batch type  
* 1.0.0 - Initial plugin

# Links


## References
  
* [Automox](https://www.automox.com/)  
* [Automox Developer Portal](https://developer.automox.com/developer-portal/)