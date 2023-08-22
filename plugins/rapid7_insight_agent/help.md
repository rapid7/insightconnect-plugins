# Description

Using the Insight Agent plugin from InsightConnect, you can quarantine, unquarantine and monitor potentially malicious IPs, addresses, hostnames, and devices across your organization

# Key Features
  
* The agent is used by [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/) and [InsightVM](https://www.rapid7.com/products/insightvm/) customers to monitor endpoints. 

# Requirements

* [Platform API Key](https://docs.rapid7.com/insight/managing-platform-api-keys/)  
* Administrator access to InsightIDR  

# Supported Product Versions
  
* Rapid7 Insight Agent 2023-08-18

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|User or Organization Key from the Insight Platform|None|a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99|
|region|string|United States|True|Region|['United States', 'United States 2', 'United States 3', 'Europe', 'Canada', 'Australia', 'Japan']|United States|
  
Example input:

```
{
  "api_key": "a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99",
  "region": "United States"
}
```

## Technical Details

### Actions


#### Check Agent Status
  
Get the online status and quarantine state of an agent

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent_id|string|None|True|The ID of the agent on the device to get the status from|None|a1cfb273c8e7d46a9e2a0e2dae01a0ce|
  
Example input:

```
{
  "agent_id": "a1cfb273c8e7d46a9e2a0e2dae01a0ce"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|is_asset_online|boolean|True|Indicates that the agent is connected to the Insight platform. This means the device is powered on and is connected to Rapid7|True|
|is_currently_quarantined|boolean|True|Is the device currently quarantined|True|
|is_quarantine_requested|boolean|True|Is a quarantine action pending on this device|True|
|is_unquarantine_requested|boolean|True|Is there a pending request to release quarantine on this device|True|
  
Example output:

```
{
  "is_asset_online": true,
  "is_currently_quarantined": true,
  "is_quarantine_requested": true,
  "is_unquarantine_requested": true
}
```

#### Get Agent Details
  
This action is used to find and display detailed information about a device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|IP address, MAC address, or hostname of the device to get information from|None|Example-Hostname|
  
Example input:

```
{
  "agent": "Example-Hostname"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agent|agent|True|Agent information|{}|
  
Example output:

```
{
  "agent": {}
}
```

#### Quarantine
  
Quarantine or unquarantine on a device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent_id|string|None|True|The ID of the agent on the device to quarantine|None|a1cfb273c8e7d46a9e2a0e2dae01a0ce|
|interval|int|604800|True|Length of time in seconds to try to take action on a device. This is also called Advertisement Period|None|604800|
|quarantine_state|boolean|True|True|Set to true to quarantine a host, set to false to unquarantine|None|True|
  
Example input:

```
{
  "agent_id": "a1cfb273c8e7d46a9e2a0e2dae01a0ce",
  "interval": 604800,
  "quarantine_state": true
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

#### Quarantine Multiple
  
Quarantine or unquarantine multiple hosts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent_array|[]string|None|True|Agent hostnames to quarantine or unquarantine|None|["abcdef123", "abcdef123"]|
|interval|int|604800|True|Length of time in seconds to try to take action on a device. This is also called Advertisement Period|None|604800|
|quarantine_state|boolean|True|True|Set to true to quarantine a host, set to false to unquarantine|None|True|
  
Example input:

```
{
  "agent_array": "abcdef123",
  "interval": 604800,
  "quarantine_state": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|completed|[]string|False|List of successfully quarantined hosts|["abcdef123"]|
|failed|[]quarantine_multiple_error|False|List of unsuccessfully quarantined hosts|[{"hostname": "abcdef123", "error": "Hostname could not be found"}]|
  
Example output:

```
{
  "completed": "abcdef123",
  "failed": {
    "error": "Hostname could not be found",
    "hostname": "abcdef123"
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Output Types
  
**attribute**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key|string|None|False|Key|None|
|Value|string|None|False|Value|None|
  
**quarantineState_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Current State|string|None|False|Current state|None|
  
**agent_info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Semantic Version|string|None|False|Agent semantic version|None|
|Agent Status|string|None|False|Agent status|None|
|Quarantine State|quarantineState_object|None|False|Quarantine state|None|
  
**hostName**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
  
**primaryAddress**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP Address|string|None|False|IP address|None|
|MAC Address|string|None|False|MAC address|None|
  
**uniqueIdentity_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID|None|
|Source|string|None|False|Source|None|
  
**host**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attributes|[]attribute|None|False|Attributes|None|
|Description|string|None|False|Description|None|
|Hostnames|[]hostName|None|False|Hostnames|None|
|Primary Address|primaryAddress|None|False|Primary address|None|
|Unique Identity|[]uniqueIdentity_object|None|False|Unique identity|None|
|Vendor|string|None|False|Vendor|None|
|Version|string|None|False|Version|None|
  
**agent**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Information|agent_info|None|False|Agent information|None|
|Host|host|None|False|Host|None|
|ID|string|None|False|ID|None|
|Platform|string|None|False|Platform|None|
  
**quarantine_multiple_error**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Error|string|None|False|Error|None|
|Hostname|string|None|False|Hostname|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 2.0.1 - Update `Connection Test` to identify if `Region` is incorrect  | Update Plugin runtime to version 5
* 2.0.0 - Update action `Quarantine Multiple` outputs to Completed and Failed, removed All Operations Successful, replaced output Agent IDs with Hostname  
* 1.2.0 - New action: `Quarantine Multiple`  
* 1.1.1 - Quarantine: Fix incorrect behavior for unquarantine when the agent ID is wrong  
* 1.1.0 - Cloud enabled  
* 1.0.4 - Add new supported regions for API | Create unit tests for actions Check Agent Status, Quarantine, Get Agent Details    
* 1.0.3 - Documentation update  
* 1.0.2 - Fix for a case-sensitive agent hostname  
* 1.0.1 - Documentation update  
* 1.0.0 - Initial plugin  

# Links

* [Rapid7 Insight Agent](https://docs.rapid7.com/insight-agent/overview/)  

## References
  
* [Manage Platform API Keys](https://docs.rapid7.com/insight/managing-platform-api-keys/)  