# Description

The [BlackBerry CylancePROTECT](https://www.cylance.com/en-us/platform/products/cylance-protect.html) plugin allows you to automate response operations for CylancePROTECT and CylanceOPTICS.

# Key Features

* Get agent details
* Blacklist a malicious hash
* Quarantine endpoints
* Search threats

# Requirements

* CylancePROTECT configured with an Custom Application

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|application_id|credential_secret_key|None|True|Application ID for CylancePROTECT instance|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|application_secret|credential_secret_key|None|True|Generated token that allows access to Cylance Resources|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|tenant_id|credential_secret_key|None|True|The unique tenant ID of the tenant that the device belongs to|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|url|string|https://protectapi.cylance.com|True|Web API URL|None|https://protectapi.cylance.com|

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

#### Delete Device(s) from Console

This action is used to delete assets/devices from the Console.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agents|[]string|None|True|Device(s) to delete. Accepts IP address, MAC address, hostname, or device ID|None|["Example-Hostname", "198.51.100.1"]|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be deleted. This can include IPs, hostnames or device IDs|None|["198.51.100.100", "Example-Hostname", "1abc234d-5efa-6789-bcde-0f1abcde23f5"]|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deleted|[]string|False|List of assets that were deleted|
|not_deleted|[]string|False|List of assets that were not deleted, either because of whitelist or because they were not found|
|success|boolean|True|Return true if at least one device was deleted|

Example output:

```
```

#### Delete Device(s) from Console

This action is used to delete assets/devices from the Console.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agents|[]string|None|True|Device(s) to delete. Accepts IP address, MAC address, hostname, or device ID|None|["Example-Hostname", "198.51.100.1"]|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be deleted. This can include IPs, hostnames or device IDs|None|["198.51.100.100", "Example-Hostname", "1abc234d-5efa-6789-bcde-0f1abcde23f5"]|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if the device was deleted|

Example output:

```
```

#### Delete Device(s) from Console

This action is used to delete assets/devices from the Console.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agents|[]string|None|True|Device(s) to delete. Accepts IP address, MAC address, hostname, or device ID|None|["Example-Hostname", "198.51.100.1"]|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be deleted. This can include IPs, hostnames or device IDs|None|["198.51.100.100", "Example-Hostname", "1abc234d-5efa-6789-bcde-0f1abcde23f5"]|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if the device was deleted|

Example output:

```
```

#### Delete Device(s) from Console

This action is used to delete assets/devices from the Console.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agents|[]string|None|True|Device(s) to delete. Accepts IP address, MAC address, hostname, or device ID|None|["Example-Hostname", "198.51.100.1"]|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be deleted. This can include IPs, hostnames or device IDs|None|["198.51.100.100", "Example-Hostname", "1abc234d-5efa-6789-bcde-0f1abcde23f5"]|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if the device was deleted|

Example output:

```
```

#### Update Agent Threat

This action updates the status (waive or quarantine) of a convicted threat on a selected device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Device to update threat on. Accepts IP address, MAC address, hostname, or device ID|None|Example-Hostname|
|quarantine_state|boolean|None|True|True to quarantine threat, false to waive threat|None|True|
|threat_identifier|string|None|True|The threat to search for. The input should be a threat name, MD5 or SHA256 hash|None|44d88612fea8a8f36de82e1278abb02f|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if the threat was updated|

Example output:

```
{
  "success": true
}
```

#### Update Agent

This action adds or removes zones and/or updates the policy of a specific Console device resource belonging to a Tenant.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|add_zones|[]string|None|False|The list of zone identifiers which the device is to be assigned. The input should be an array of zone IDs|None|["1abc234d-5efa-6789-bcde-0f1abcde23f5"]|
|agent|string|None|True|Agent to update device information from. Accepts IP address, MAC address, hostname, or device ID|None|Example-Hostname|
|policy|string|None|False|The unique identifier for the policy to assign to the device. Specify policy, or leave the string empty to remove the current policy from the device|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|remove_zones|[]string|None|False|The list of zone identifiers from which the device is to be removed. The input should be an array of zone IDs|None|["1abc234d-5efa-6789-bcde-0f1abcde23f5"]|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if the agent was updated|

Example output:

```
{
  "success": true
}
```

#### Search Agents

This action searches for agents and returns device information details about them.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, MAC address, name, or device ID|None|EXAMPLE-HOSTNAME|

Example input:

```
{
  "agent": "EXAMPLE-HOSTNAME"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents|[]agents|True|Detailed information about agents found|

Example output:

```
{
  "agents": [
    {
      "mac_addresses": [
        "08-00-27-2F-43-60"
      ],
      "name": "Example-Hostname",
      "policy": {
        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
        "name": "Default"
      },
      "state": "Offline",
      "agent_version": "2.0.1540",
      "date_first_registered": "2020-06-21T15:53:43",
      "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
      "ip_addresses": [
        "198.51.100.100"
      ]
    }
  ]
}
```

#### Search Threats

This action finds and displays detailed information about one or more threats.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|score|integer|None|False|Filter the search by the Cylance score assigned to the threat. Accepts an integer within the range [-1,1]|None|-1|
|threat_identifier|[]string|None|True|The threat(s) to search for. The input should be an array of threat names, MD5, or SHA256 hashes|None|["44d88612fea8a8f36de82e1278abb02f", "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f", "Example-Threat-Name"]|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threats|[]threat|True|Detailed information about threats found|

Example output:

```
{
  "threats": [
    {
      "file_size": 109395,
      "md5": "9DE5069C5AFE602B2EA0A04B66BEB2C0",
      "safelisted": false,
      "unique_to_cylance": true,
      "classification": "Malware",
      "cylance_score": -1,
      "global_quarantined": false,
      "last_found": "2020-05-29T10:12:45",
      "name": "honeyhashx86.exe",
      "sha256": "02699626F388ED830012E5B787640E71C56D42D8",
      "sub_classification": "Exploit"
    }
  ]
}
```

#### Get Devices Affected by Threat

This action is used to retrieve a list of devices affected by a threat.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|threat_identifier|string|None|True|The threat to search for. The input should be a threat name, MD5, or SHA256 hash|None|44d88612fea8a8f36de82e1278abb02f|

Example input:

```
{
  "threat_identifier": "44d88612fea8a8f36de82e1278abb02f"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents|[]threat_device|True|Detailed information about threat agents found|

Example output:

```
{
  "agents": [
    {
      "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
      "name": "Example-Hostname",
      "state": "OffLine",
      "agent_version": "2.0.1540",
      "policy_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
      "date_found": "2020-05-29T10:12:45",
      "file_status": "Default",
      "file_path": "C:\\Program Files (x86)\\Rapid7\\Endpoint Agent\\honeyhashx86.exe",
      "ip_addresses": [
        "198.51.100.100"
      ],
      "mac_addresses": [
        "00-60-26-26-D5-19"
      ]
    }
  ]
}
```

#### Quarantine

This action is used to quarantine (isolate) an endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Device to perform quarantine action on. Accepts IP address, MAC address, hostname, or device ID|None|Example-Hostname|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be blocked. This can include IPs, hostnames or device IDs|None|["198.51.100.100", "Example-Hostname", "1abc234d-5efa-6789-bcde-0f1abcde23f5"]|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|lockdown_details|lockdown_response|True|Detailed information about the device lockdown|

Example output:

```
{
  "status": "COMPLETE",
  "data": {
      "id": "1ABC234D5EFA6789BCDE0F1ABCDE23F5",
      "hostname": "Example-Hostname",
      "tenant_id": "1abc234d5efa6789bcde0f1abcde23f5",
      "connection_status": "locked",
      "optics_device_version": "2.4.2100.1015",
      "password": "unlock-pa22-w0rd",
      "lockdown_expiration": "2020-07-11T21:15:29Z",
      "lockdown_initiated": "2020-07-08T21:15:29Z"
  }
}
```

#### Blacklist

This action is used to blacklist (quarantine) a hash globally.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|blacklist_state|boolean|None|True|True to blacklist hash, false to unblacklist hash|None|True|
|description|string|Hash Blacklisted from InsightConnect|True|Description for why the hash is blacklisted|None|Hash Blacklisted from InsightConnect|
|hash|string|None|True|Create a blacklist item from a SHA256 hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|

Example input:

```
{
  "blacklist_state": true,
  "description": "Hash Blacklisted from InsightConnect",
  "hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if blacklist item was created or deleted|

Example output:

```
{
  "success": true
}
```

#### Get Agent Details

This action is used to obtain agent information.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts MAC address, hostname, or agent ID|None|cylance-agent-win12|

Example input:

```
{
  "agent": "cylance-agent-win12"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent|True|Details for an agent|

Example output:

```
{
  "agent": {
    "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
    "name": "NA-TESTX-NAM11",
    "host_name": "na-testx-nam11",
    "os_version": "Microsoft Windows Server 2012 Standard",
    "state": "Online",
    "agent_version": "2.0.1540",
    "policy": {
      "id": "00000000-0000-0000-0000-000000000000",
      "name": "Default"
    },
    "last_logged_in_user": "NA-TESTX-NAM11\\Administrator",
    "update_available": false,
    "background_detection": false,
    "is_safe": false,
    "date_first_registered": "2020-05-28T14:00:50",
    "ip_addresses": [
      "198.51.100.100"
    ],
    "mac_addresses": [
      "00-60-26-26-D5-19"
    ]
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.4.0 - New actions Update Agent Threat, Update Agent
* 1.3.0 - New action Search Agents
* 1.2.0 - New actions Search Threats, Get Devices Affected by Threat
* 1.1.0 - New action Quarantine
* 1.0.3 - Match official branding in plugin title
* 1.0.2 - Update to fix connection test
* 1.0.1 - Add SHA256 input validation in Blacklist action
* 1.0.0 - Initial plugin

# Links

## References

* [BlackBerry CylancePROTECT](https://www.cylance.com)
