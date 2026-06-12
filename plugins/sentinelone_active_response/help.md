# Description

Orchestrate endpoint response operations against SentinelOne-managed endpoints with a single autonomous action that resolves, executes, monitors, and reports

# Key Features

* Autonomously contain or uncontain endpoints with a single action
* Automatically resolve endpoint identifiers (hostname, IP, MAC, agent ID) to SentinelOne agents
* Monitor containment operations and confirm state transitions with configurable timeout
* Return comprehensive structured reports suitable for incident documentation

# Requirements

* SentinelOne API token with permissions to query agents and perform network actions
* SentinelOne management console instance URL

# Supported Product Versions

* SentinelOne API v2.1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|SentinelOne API token|None|{"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"}|None|None|
|instance|string|None|True|SentinelOne instance subdomain (e.g. usea1-partners)|None|usea1-partners|None|None|

Example input:

```
{
  "api_key": {
    "secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"
  },
  "instance": "usea1-partners"
}
```

## Technical Details

### Actions


#### Execute Response

This action is used to autonomously resolve an endpoint, execute the requested response operation, monitor for 
confirmation, and return a comprehensive report

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint_identifier|string|None|True|Hostname, IP address, MAC address, or SentinelOne agent ID of the target endpoint|None|WORKSTATION-01|None|None|
|intent|string|None|True|Desired response operation to perform|["contain", "uncontain", "status", "info"]|contain|None|None|
|polling_interval|integer|10|False|Seconds between status checks during the monitoring phase|None|10|None|None|
|timeout|integer|120|False|Maximum seconds to wait during the monitoring phase|None|120|None|None|
  
Example input:

```
{
  "endpoint_identifier": "WORKSTATION-01",
  "intent": "contain",
  "polling_interval": 10,
  "timeout": 120
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|report|response_report|True|Comprehensive structured report of the operation result|{"action_performed": "contain", "result_status": "success", "network_status": "disconnected", "summary": "Successfully contained endpoint WORKSTATION-01 (disconnected confirmed in 15s)", "timestamp": "2024-01-15T10:30:00Z", "elapsed_time": 15.2, "agent": {"agent_id": "1234567890123456789", "hostname": "WORKSTATION-01", "ip_address": "192.168.1.100", "mac_address": "00:1A:2B:3C:4D:5E", "operating_system": "Windows 10 Pro", "network_status": "disconnected", "site_name": "Default Site", "group_name": "Default Group", "active_threats": 0, "agent_version": "23.1.2.400"}}|
  
Example output:

```
{
  "report": {
    "action_performed": "contain",
    "agent": {
      "active_threats": 0,
      "agent_id": "1234567890123456789",
      "agent_version": "23.1.2.400",
      "group_name": "Default Group",
      "hostname": "WORKSTATION-01",
      "ip_address": "192.168.1.100",
      "mac_address": "00:1A:2B:3C:4D:5E",
      "network_status": "disconnected",
      "operating_system": "Windows 10 Pro",
      "site_name": "Default Site"
    },
    "elapsed_time": 15.2,
    "network_status": "disconnected",
    "result_status": "success",
    "summary": "Successfully contained endpoint WORKSTATION-01 (disconnected confirmed in 15s)",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**agent_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active Threats|integer|None|False|Number of active threats on the agent|0|
|Agent ID|string|None|True|SentinelOne agent identifier|1234567890123456789|
|Agent Version|string|None|False|SentinelOne agent software version|23.1.2.400|
|Group Name|string|None|False|SentinelOne group name|Default Group|
|Hostname|string|None|False|Agent computer name|WORKSTATION-01|
|IP Address|string|None|False|Agent primary IP address|192.168.1.100|
|MAC Address|string|None|False|Agent primary MAC address|00:1A:2B:3C:4D:5E|
|Network Status|string|None|False|Current network connectivity status|connected|
|Operating System|string|None|False|Agent OS name|Windows 10 Pro|
|Site Name|string|None|False|SentinelOne site name|Default Site|
  
**response_report**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action Performed|string|None|True|The intent that was executed|contain|
|Agent|agent_details|None|False|Resolved agent details|None|
|Elapsed Time|float|None|False|Time in seconds spent in the monitoring phase|15.2|
|Error Cause|string|None|False|Cause of the error if operation failed||
|Error Remediation|string|None|False|Suggested remediation if operation failed||
|Network Status|string|None|False|Agent network status at report time|disconnected|
|Result Status|string|None|True|Outcome of the operation (success, already_actioned, timeout, error)|success|
|Summary|string|None|True|Human-readable summary of the operation result|Successfully contained endpoint WORKSTATION-01 (disconnected confirmed in 15s)|
|Timestamp|string|None|True|ISO 8601 timestamp when the report was generated|2024-01-15T10:30:00Z|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.0 - Initial plugin with execute_response orchestrator action

# Links

* [SentinelOne](https://www.sentinelone.com/)

## References

* [SentinelOne API Documentation](https://usea1-partners.sentinelone.net/api-doc/overview)