# Description

The [BlackBerry CylancePROTECT](https://www.cylance.com/en-us/platform/products/cylance-protect.html) plugin allows you to automate response operations for CylancePROTECT and CylanceOPTICS

# Key Features

* Get agent details
* Blacklist a malicious hash
* Quarantine endpoints
* Search threats
* Delete assets

# Requirements

* CylancePROTECT configured with an Custom Application

* Setup

You must create a Custom Application by following this procedure from the CylancePROTECT console:

1. Go to the Integrations tab on the Settings page
2. Click `Add Application`
3. Provide a name for the integration and choose the permissions related to the actions you want to use
4. Copy and paste the `Application ID`, `Application Secret`, and `Tenant ID` (from the Integrations tab) into the connection

# Supported Product Versions

* v2

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|application_id|credential_secret_key|None|True|Application ID for CylancePROTECT instance|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|None|None|
|application_secret|credential_secret_key|None|True|Generated token that allows access to Cylance Resources|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|None|None|
|tenant_id|credential_secret_key|None|True|The unique tenant ID of the tenant that the device belongs to|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|None|None|
|url|string|https://protectapi.cylance.com|True|Web API URL|None|https://protectapi.cylance.com|None|None|

Example input:

```
{
  "application_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "application_secret": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "tenant_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "url": "https://protectapi.cylance.com"
}
```

## Technical Details

### Actions


#### Blacklist

This action is used to blacklist (quarantine) a hash globally

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|blacklist_state|boolean|None|True|True to blacklist hash, false to unblacklist hash|None|True|None|None|
|description|string|Hash Blacklisted from InsightConnect|True|Description for why the hash is blacklisted|None|Hash Blacklisted from InsightConnect|None|None|
|hash|string|None|True|Create a blacklist item from a SHA256 hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|None|None|
  
Example input:

```
{
  "blacklist_state": true,
  "description": "Hash Blacklisted from InsightConnect",
  "hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Return true if blacklist item was created or deleted|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Asset

This action is used to delete assets/devices from the Console

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agents|[]string|None|True|Device(s) to delete. Accepts IP address, MAC address, hostname, or device ID|None|["Example-Hostname", "198.51.100.1"]|None|None|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be deleted. This can include IPs, hostnames or device IDs|None|["198.51.100.100","Example-Hostname", "1abc234d-5efa-6789-bcde-0f1abcde23f5"]|None|None|
  
Example input:

```
{
  "agents": [
    "Example-Hostname",
    "198.51.100.1"
  ],
  "whitelist": [
    "198.51.100.100",
    "Example-Hostname",
    "1abc234d-5efa-6789-bcde-0f1abcde23f5"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|deleted|[]string|False|List of assets that were deleted|["10.0.2.15"]|
|not_deleted|[]string|False|List of assets that were not deleted, either because of whitelist or because they were not found|["2.2.2.2","3.3.3.3"]|
|success|boolean|True|Return true if at least one device was deleted|True|
  
Example output:

```
{
  "deleted": [
    "10.0.2.15"
  ],
  "not_deleted": [
    "2.2.2.2",
    "3.3.3.3"
  ],
  "success": true
}
```

#### Get Agent Details

This action is used to retrieve agent information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent to retrieve device information from. Accepts MAC address, hostname, or agent ID|None|cylance-agent-win12|None|None|
  
Example input:

```
{
  "agent": "cylance-agent-win12"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agent|agent|True|Details for an agent|{'agent': {'id': '1abc234d-5efa-6789-bcde-0f1abcde23f5', 'name': 'NA-TESTX-NAM11', 'host_name': 'na-testx-nam11', 'os_version': 'Microsoft Windows Server 2012 Standard', 'state': 'Online', 'agent_version': '2.0.1540', 'policy': {'id': '00000000-0000-0000-0000-000000000000', 'name': 'Default'}, 'last_logged_in_user': 'NA-TESTX-NAM11\\Administrator', 'update_available': False, 'background_detection': False, 'is_safe': False, 'date_first_registered': '2020-05-28T14:00:50', 'ip_addresses': ['198.51.100.100'], 'mac_addresses': ['00-60-26-26-D5-19']}}|
  
Example output:

```
{
  "agent": {
    "agent": {
      "agent_version": "2.0.1540",
      "background_detection": false,
      "date_first_registered": "2020-05-28T14:00:50",
      "host_name": "na-testx-nam11",
      "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
      "ip_addresses": [
        "198.51.100.100"
      ],
      "is_safe": false,
      "last_logged_in_user": "NA-TESTX-NAM11\\Administrator",
      "mac_addresses": [
        "00-60-26-26-D5-19"
      ],
      "name": "NA-TESTX-NAM11",
      "os_version": "Microsoft Windows Server 2012 Standard",
      "policy": {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": "Default"
      },
      "state": "Online",
      "update_available": false
    }
  }
}
```

#### Quarantine

This action is used to quarantine (isolate) an endpoint

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Device to perform quarantine action on. Accepts IP address, MAC address, hostname, or device ID|None|Example-Hostname|None|None|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be blocked. This can include IPs, hostnames or device IDs|None|["198.51.100.100", "Example-Hostname", "1abc234d-5efa-6789-bcde-0f1abcde23f5"]|None|None|
  
Example input:

```
{
  "agent": "Example-Hostname",
  "whitelist": [
    "198.51.100.100",
    "Example-Hostname",
    "1abc234d-5efa-6789-bcde-0f1abcde23f5"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|lockdown_details|lockdown_response|True|Detailed information about the device lockdown|{'status': 'COMPLETE', 'data': {'id': '1ABC234D5EFA6789BCDE0F1ABCDE23F5', 'hostname': 'Example-Hostname', 'tenant_id': '1abc234d5efa6789bcde0f1abcde23f5', 'connection_status': 'locked', 'optics_device_version': '2.4.2100.1015', 'password': 'unlock-pa22-w0rd', 'lockdown_expiration': '2020-07-11T21:15:29Z', 'lockdown_initiated': '2020-07-08T21:15:29Z'}}|
  
Example output:

```
{
  "lockdown_details": {
    "data": {
      "connection_status": "locked",
      "hostname": "Example-Hostname",
      "id": "1ABC234D5EFA6789BCDE0F1ABCDE23F5",
      "lockdown_expiration": "2020-07-11T21:15:29Z",
      "lockdown_initiated": "2020-07-08T21:15:29Z",
      "optics_device_version": "2.4.2100.1015",
      "password": "unlock-pa22-w0rd",
      "tenant_id": "1abc234d5efa6789bcde0f1abcde23f5"
    },
    "status": "COMPLETE"
  }
}
```

#### Search Agents

This action is used to this action searches for agents and returns device information details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, MAC address, name, or device ID|None|EXAMPLE-HOSTNAME|None|None|
  
Example input:

```
{
  "agent": "EXAMPLE-HOSTNAME"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agents|[]agents|True|Detailed information about agents found|{'agents': [{'mac_addresses': ['08-00-27-2F-43-60'], 'name': 'Example-Hostname', 'policy': {'id': '1abc234d-5efa-6789-bcde-0f1abcde23f5', 'name': 'Default'}, 'state': 'Offline', 'agent_version': '2.0.1540', 'date_first_registered': '2020-06-21T15:53:43', 'id': '1abc234d-5efa-6789-bcde-0f1abcde23f5', 'ip_addresses': ['198.51.100.100']}]}|
  
Example output:

```
{
  "agents": {
    "agents": [
      {
        "agent_version": "2.0.1540",
        "date_first_registered": "2020-06-21T15:53:43",
        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
        "ip_addresses": [
          "198.51.100.100"
        ],
        "mac_addresses": [
          "08-00-27-2F-43-60"
        ],
        "name": "Example-Hostname",
        "policy": {
          "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
          "name": "Default"
        },
        "state": "Offline"
      }
    ]
  }
}
```

#### Get Devices Affected by Threat

This action is used to retrieve a list of devices affected by a threat

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|threat_identifier|string|None|True|The threat to search for. The input should be a threat name, MD5, or SHA256 hash|None|44d88612fea8a8f36de82e1278abb02f|None|None|
  
Example input:

```
{
  "threat_identifier": "44d88612fea8a8f36de82e1278abb02f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agents|[]threat_device|True|Detailed information about threat agents found|{'agents': [{'id': '1abc234d-5efa-6789-bcde-0f1abcde23f5', 'name': 'Example-Hostname', 'state': 'OffLine', 'agent_version': '2.0.1540', 'policy_id': '1abc234d-5efa-6789-bcde-0f1abcde23f5', 'date_found': '2020-05-29T10:12:45', 'file_status': 'Default', 'file_path': 'C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe', 'ip_addresses': ['198.51.100.100'], 'mac_addresses': ['00-60-26-26-D5-19']}]}|
  
Example output:

```
{
  "agents": {
    "agents": [
      {
        "agent_version": "2.0.1540",
        "date_found": "2020-05-29T10:12:45",
        "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
        "file_status": "Default",
        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
        "ip_addresses": [
          "198.51.100.100"
        ],
        "mac_addresses": [
          "00-60-26-26-D5-19"
        ],
        "name": "Example-Hostname",
        "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
        "state": "OffLine"
      }
    ]
  }
}
```

#### Search Threats

This action is used to finds and displays detailed information about one or more threats

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|score|integer|None|False|Filter the search by the Cylance score assigned to the threat. Accepts an integer within the range [-1,1]|None|-1|None|None|
|threat_identifier|[]string|None|True|The threat(s) to search for. The input should be an array of threat names, MD5, or SHA256 hashes|None|["44d88612fea8a8f36de82e1278abb02f", "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f", "Example-Threat-Name"]|None|None|
  
Example input:

```
{
  "score": -1,
  "threat_identifier": [
    "44d88612fea8a8f36de82e1278abb02f",
    "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
    "Example-Threat-Name"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|threats|[]threat|True|Detailed information about threats found|{'threats': [{'file_size': 109395, 'md5': '9DE5069C5AFE602B2EA0A04B66BEB2C0', 'safelisted': False, 'unique_to_cylance': True, 'classification': 'Malware', 'cylance_score': -1, 'global_quarantined': False, 'last_found': '2020-05-29T10:12:45', 'name': 'honeyhashx86.exe', 'sha256': '02699626F388ED830012E5B787640E71C56D42D8', 'sub_classification': 'Exploit'}]}|
  
Example output:

```
{
  "threats": {
    "threats": [
      {
        "classification": "Malware",
        "cylance_score": -1,
        "file_size": 109395,
        "global_quarantined": false,
        "last_found": "2020-05-29T10:12:45",
        "md5": "9DE5069C5AFE602B2EA0A04B66BEB2C0",
        "name": "honeyhashx86.exe",
        "safelisted": false,
        "sha256": "02699626F388ED830012E5B787640E71C56D42D8",
        "sub_classification": "Exploit",
        "unique_to_cylance": true
      }
    ]
  }
}
```

#### Update Agent

This action is used to adds or removes zones and/or updates the policy of a specific Console device resource belonging 
to a Tenant

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|add_zones|[]string|None|False|The list of zone identifiers which the device is to be assigned. The input should be an array of zone IDs|None|["1abc234d-5efa-6789-bcde-0f1abcde23f5"]|None|None|
|agent|string|None|True|Agent to update device information from. Accepts IP address, MAC address, hostname, or device ID|None|Example-Hostname|None|None|
|policy|string|None|False|The unique identifier for the policy to assign to the device. Specify policy, or leave the string empty to remove the current policy from the device|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|None|None|
|remove_zones|[]string|None|False|The list of zone identifiers from which the device is to be removed. The input should be an array of zone IDs|None|["1abc234d-5efa-6789-bcde-0f1abcde23f5"]|None|None|
  
Example input:

```
{
  "add_zones": [
    "1abc234d-5efa-6789-bcde-0f1abcde23f5"
  ],
  "agent": "Example-Hostname",
  "policy": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "remove_zones": [
    "1abc234d-5efa-6789-bcde-0f1abcde23f5"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Return true if the agent was updated|True|
  
Example output:

```
{
  "success": true
}
```

#### Update Agent Threat

This action is used to updates the status (waive or quarantine) of a convicted threat on a selected device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Device to update threat on. Accepts IP address, MAC address, hostname, or device ID|None|Example-Hostname|None|None|
|quarantine_state|boolean|None|True|True to quarantine threat, false to waive threat|None|True|None|None|
|threat_identifier|string|None|True|The threat to search for. The input should be a threat name, MD5 or SHA256 hash|None|44d88612fea8a8f36de82e1278abb02f|None|None|
  
Example input:

```
{
  "agent": "Example-Hostname",
  "quarantine_state": true,
  "threat_identifier": "44d88612fea8a8f36de82e1278abb02f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Return true if the threat was updated|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**policy**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID|None|
|Name|string|None|False|Name|None|
  
**agent**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Version|string|None|False|Agent version|None|
|Background Detection|boolean|None|False|Background detection|None|
|Date First Registered|string|None|False|Date first registered|None|
|Date Last Modified|string|None|False|Date last modified|None|
|Date Offline|string|None|False|Date offline|None|
|Distinguished Name|string|None|False|Distinguished name|None|
|Host Name|string|None|False|Host name|None|
|ID|string|None|False|ID|None|
|IP Addresses|[]string|None|False|IP addresses|None|
|Is Safe|boolean|None|False|Is safe|None|
|Last Logged In User|string|None|False|Last logged in user|None|
|MAC Addresses|[]string|None|False|MAC addresses|None|
|Name|string|None|False|Name|None|
|OS Version|string|None|False|OS version|None|
|Policy|policy|None|False|Policy|None|
|State|string|None|False|State|None|
|Update Available|boolean|None|False|Update available|None|
|Update Type|string|None|False|Update type|None|
  
**lockdown_history**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Command|string|None|False|The command that was executed|None|
|Timestamp|string|None|False|The timestamp (in UTC) of when the command was initiated|None|
|User ID|string|None|False|The unique ID of the user who locked down the device|None|
  
**lockdown**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Connection Status|string|None|False|Whether or not the device is connected to Cylance's cloud services|None|
|Hostname|string|None|False|The hostname of the device that the lockdown command was issued to|None|
|ID|string|None|False|The unique device ID that the lockdown command was issued to|None|
|Lockdown Expiration|string|None|False|The timestamp (in UTC) of when the current device lockdown is set to expire|None|
|Lockdown History|[]lockdown_history|None|False|A list of historical device lockdown commands issued to this particular device|None|
|Lockdown Initiated|string|None|False|The timestamp (in UTC) of when the current device lockdown was initiated|None|
|Optics Device Version|string|None|False|The numerical version of CylanceOPTICS running on the device|None|
|Password|string|None|False|The password required to unlock the device|None|
|Tenant ID|string|None|False|The unique tenant ID of the tenant that the device belongs to|None|
  
**lockdown_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Lockdown Details|lockdown|None|False|Detailed information about the lockdown action performed|None|
|Status|string|None|False|Status of the action performed|None|
  
**agents**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Version|string|None|False|Agent version|None|
|Date First Registered|string|None|False|Date first registered|None|
|ID|string|None|False|ID|None|
|IP Addresses|[]string|None|False|IP addresses|None|
|MAC Addresses|[]string|None|None|MAC addresses|None|
|Name|string|None|False|Name|None|
|Policy|policy|None|False|Policy|None|
|State|string|None|False|State|None|
  
**threat**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AV Industry|float|None|False|The score provided by the antivirus industry|None|
|Classification|string|None|False|The threat classification for the threat|None|
|Cylance Score|float|None|False|The Cylance Score assigned to the threat|None|
|File Size|int|None|False|The size of the file, in bytes|None|
|Global Quarantined|boolean|None|False|Identifies if the threat is on the Global Quarantine list|None|
|Last Found|string|None|False|The date and time the threat was last found on any device in your organization|None|
|MD5|string|None|False|The MD5 hash for the threat|None|
|Name|string|None|False|The name of the threat|None|
|Safelisted|boolean|None|False|Identifies if the threat is on the Safe List|None|
|SHA256|string|None|False|The SHA256 hash for the threat|None|
|Sub Classification|string|None|False|The threat sub-classification for the threat|None|
|Unique to Cylance|boolean|None|False|The threat was identifies by Cylance but not by other antivirus sources|None|
  
**threat_device**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Version|string|None|False|The CylancePROTECT Agent version installed on the device|None|
|Date Found|string|None|False|The date and time (in UTC) when the threat was found on the device|None|
|File Path|string|None|False|The path where the file was found on the device|None|
|File Status|string|None|False|Current quarantine status of the file on the device|None|
|ID|string|None|False|The endpoint's unique identifier|None|
|IP Addressess|[]string|None|False|The list of IP addresses for the device|None|
|MAC Addressess|[]string|None|False|The list of MAC addresses for the device|None|
|Name|string|None|False|The name of the device|None|
|Policy ID|string|None|False|The unique identifier for the policy assigned to the device, or null if no policy is assigned|None|
|State|string|None|False|The state of the device|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.5.5 - Resolved Snyk Vulnerability | SDK bump to latest version (6.3.7)
* 1.5.4 - Resolved Snyk Vulnerability | SDK bump to latest version (6.3.6)
* 1.5.3 - Bumping requirements.txt | SDK bump to 6.1.4
* 1.5.2 - Bumped the version of the SDK used | Bumped versions of all pythion packages used | Ran refresh to bring code up to latest standard | Added unit tests for all actions
* 1.5.1 - Bug fixes in Delete Asset, hostname whitelisting, and IP address inputs
* 1.5.0 - New action Delete Asset | Rework utility function
* 1.4.0 - New actions Update Agent Threat, Update Agent
* 1.3.0 - New action Search Agents
* 1.2.0 - New actions Search Threats, Get Devices Affected by Threat
* 1.1.0 - New action Quarantine
* 1.0.3 - Match official branding in plugin title
* 1.0.2 - Update to fix connection test
* 1.0.1 - Add SHA256 input validation in Blacklist action
* 1.0.0 - Initial plugin

# Links

* [BlackBerry CylancePROTECT](https://www.cylance.com)

## References

* [BlackBerry CylancePROTECT API](https://docs.blackberry.com/en/unified-endpoint-security/blackberry-ues/Cylance-API-user-guide/Application_Management)