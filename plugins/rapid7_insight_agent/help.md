# Description

Using the Insight Agent plugin from InsightConnect, you can quarantine, unquarantine and monitor potentially malicious IPs, addresses, hostnames, and devices across your organization

# Key Features

* The agent is used by [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/) and [InsightVM](https://www.rapid7.com/products/insightvm/) customers to monitor endpoints.

# Requirements

* [Platform API Key](https://docs.rapid7.com/insight/managing-platform-api-keys/)
* Administrator access to InsightIDR

# Supported Product Versions

* Rapid7 Insight Agent 2024-08-23

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|User or Organization Key from the Insight Platform|None|a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99|None|None|
|region|string|United States|True|Region|["United States", "United States 2", "United States 3", "Europe", "Canada", "Australia", "Japan"]|United States|None|None|

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

This action is used to get the online status and quarantine state of an agent

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent_id|string|None|True|The ID of the agent on the device to get the status from|None|a1cfb273c8e7d46a9e2a0e2dae01a0ce|None|None|
  
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

This action is used to find and display detailed information about a device. If additional pages of agents are 
available, the action should be run again with the returned next cursor

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|IP address, MAC address, or hostname of the device to get information from|None|Example-Hostname|None|None|
|next_cursor|string|None|False|The next page cursor to continue an existing query and search additional pages of agents|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "agent": "Example-Hostname",
  "next_cursor": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agent|agent|False|Agent information|{"id":"ExampleID","platform":"windows","publicIpAddress":"192.168.0.1","host":{"vendor":"Microsoft","version":"10","description":"ExampleDescription","hostNames":[{"name":"ExampleHostname"}],"primaryAddress":{"ip":"12.43.13.43","mac":""},"uniqueIdentity":[],"attributes":[]},"agent_info":{"agentSemanticVersion":"ExampleVersion","agentStatus":"STALE","quarantineState":{"currentState":"QUARANTINED"}}}|
|next_cursor|string|False|The next page cursor, if available, to continue the query and search additional pages of agents|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example output:

```
{
  "agent": {
    "agent_info": {
      "agentSemanticVersion": "ExampleVersion",
      "agentStatus": "STALE",
      "quarantineState": {
        "currentState": "QUARANTINED"
      }
    },
    "host": {
      "attributes": [],
      "description": "ExampleDescription",
      "hostNames": [
        {
          "name": "ExampleHostname"
        }
      ],
      "primaryAddress": {
        "ip": "12.43.13.43",
        "mac": ""
      },
      "uniqueIdentity": [],
      "vendor": "Microsoft",
      "version": "10"
    },
    "id": "ExampleID",
    "platform": "windows",
    "publicIpAddress": "192.168.0.1"
  },
  "next_cursor": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

#### Get All Agents by IP Address
  
This action is used to find all agents that share the same public or private IP address and display details about them. 
If additional pages of agents are available, the action should be run again with the returned next cursor

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|The public or private IP address for all the agents to be searched for|None|192.168.0.1|None|None|
|next_cursor|string|None|False|The next page cursor to continue an existing query and search additional pages of agents|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "ip_address": "192.168.0.1",
  "next_cursor": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agents|[]agent|False|The list of all found agents|[[{"id":"ExampleID1","platform":"linux","publicIpAddress":"192.168.0.2","host":{"vendor":"Ubuntu","version":"20.04","description":"ExampleDescription1","hostNames":[{"name":"ExampleHostname1"}],"primaryAddress":{"ip":"10.20.30.40","mac":"00:11:22:33:44:55"},"uniqueIdentity":["1234567890"],"attributes":["attribute1","attribute2"]},"agent_info":{"agentSemanticVersion":"ExampleVersion1","agentStatus":"ACTIVE","quarantineState":{"currentState":"QUARANTINED"}}},{"id":"ExampleID2","platform":"mac","publicIpAddress":"192.168.0.3","host":{"vendor":"Apple","version":"11","description":"ExampleDescription2","hostNames":[{"name":"ExampleHostname2"}],"primaryAddress":{"ip":"50.60.70.80","mac":"AA:BB:CC:DD:EE:FF"},"uniqueIdentity":["0987654321"],"attributes":["attribute3","attribute4"]},"agent_info":{"agentSemanticVersion":"ExampleVersion2","agentStatus":"INACTIVE","quarantineState":{"currentState":"QUARANTINED"}}},{"id":"ExampleID3","platform":"windows","publicIpAddress":"192.168.0.4","host":{"vendor":"Microsoft","version":"11","description":"ExampleDescription3","hostNames":[{"name":"ExampleHostname3"}],"primaryAddress":{"ip":"90.80.70.60","mac":"11:22:33:44:55:66"},"uniqueIdentity":["2468135790"],"attributes":["attribute5","attribute6"]},"agent_info":{"agentSemanticVersion":"ExampleVersion3","agentStatus":"STALE","quarantineState":{"currentState":"QUARANTINED"}}}]]|
|next_cursor|string|False|The next page cursor, if available, to continue the query and search additional pages of agents|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example output:

```
{
  "agents": [
    [
      {
        "agent_info": {
          "agentSemanticVersion": "ExampleVersion1",
          "agentStatus": "ACTIVE",
          "quarantineState": {
            "currentState": "QUARANTINED"
          }
        },
        "host": {
          "attributes": [
            "attribute1",
            "attribute2"
          ],
          "description": "ExampleDescription1",
          "hostNames": [
            {
              "name": "ExampleHostname1"
            }
          ],
          "primaryAddress": {
            "ip": "10.20.30.40",
            "mac": "00:11:22:33:44:55"
          },
          "uniqueIdentity": [
            "1234567890"
          ],
          "vendor": "Ubuntu",
          "version": "20.04"
        },
        "id": "ExampleID1",
        "platform": "linux",
        "publicIpAddress": "192.168.0.2"
      },
      {
        "agent_info": {
          "agentSemanticVersion": "ExampleVersion2",
          "agentStatus": "INACTIVE",
          "quarantineState": {
            "currentState": "QUARANTINED"
          }
        },
        "host": {
          "attributes": [
            "attribute3",
            "attribute4"
          ],
          "description": "ExampleDescription2",
          "hostNames": [
            {
              "name": "ExampleHostname2"
            }
          ],
          "primaryAddress": {
            "ip": "50.60.70.80",
            "mac": "AA:BB:CC:DD:EE:FF"
          },
          "uniqueIdentity": [
            "0987654321"
          ],
          "vendor": "Apple",
          "version": "11"
        },
        "id": "ExampleID2",
        "platform": "mac",
        "publicIpAddress": "192.168.0.3"
      },
      {
        "agent_info": {
          "agentSemanticVersion": "ExampleVersion3",
          "agentStatus": "STALE",
          "quarantineState": {
            "currentState": "QUARANTINED"
          }
        },
        "host": {
          "attributes": [
            "attribute5",
            "attribute6"
          ],
          "description": "ExampleDescription3",
          "hostNames": [
            {
              "name": "ExampleHostname3"
            }
          ],
          "primaryAddress": {
            "ip": "90.80.70.60",
            "mac": "11:22:33:44:55:66"
          },
          "uniqueIdentity": [
            "2468135790"
          ],
          "vendor": "Microsoft",
          "version": "11"
        },
        "id": "ExampleID3",
        "platform": "windows",
        "publicIpAddress": "192.168.0.4"
      }
    ]
  ],
  "next_cursor": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

#### Quarantine

This action is used to quarantine or unquarantine on a device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent_id|string|None|True|The ID of the agent on the device to quarantine|None|a1cfb273c8e7d46a9e2a0e2dae01a0ce|None|None|
|interval|int|604800|True|Length of time in seconds to try to take action on a device. This is also called Advertisement Period|None|604800|None|None|
|quarantine_state|boolean|True|True|Set to true to quarantine a host, set to false to unquarantine|None|True|None|None|
  
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

This action is used to quarantine or unquarantine multiple hosts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent_array|[]string|None|True|Agent hostnames to quarantine or unquarantine|None|["abcdef123", "abcdef123"]|None|None|
|interval|int|604800|True|Length of time in seconds to try to take action on a device. This is also called Advertisement Period|None|604800|None|None|
|quarantine_state|boolean|True|True|Set to true to quarantine a host, set to false to unquarantine|None|True|None|None|
  
Example input:

```
{
  "agent_array": [
    "abcdef123",
    "abcdef123"
  ],
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
  "completed": [
    "abcdef123"
  ],
  "failed": [
    {
      "error": "Hostname could not be found",
      "hostname": "abcdef123"
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
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
  
**location**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|City|string|None|False|The name of the city where the agent is located|None|
|Continent|string|None|False|The name of the continent where the agent is located|None|
|Country Code|string|None|False|The code of the country where the agent is located|None|
|Country Name|string|None|False|The name of the country where the agent is located|None|
|Region|string|None|False|The name of the region where the agent is located|None|
  
**agent**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Information|agent_info|None|False|Agent information|None|
|Host|host|None|False|Host|None|
|ID|string|None|False|ID|None|
|Location|location|None|False|The agent's location details|None|
|Platform|string|None|False|Platform|None|
|Public IP Address|string|None|False|The agent's public IP address|None|
  
**quarantine_multiple_error**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Error|string|None|False|Error|None|
|Hostname|string|None|False|Hostname|None|


## Troubleshooting

* If the actions `Get Agent Details` and `Get All Agents by IP` return a `next cursor` value, it is an indication that more pages of data are available to be reviewed. In this instance, it is recommended to run the action multiple times and pass the `next cursor` value, recording all agents found.

# Version History

* 3.0.6 - Remove use of session from the connection object to prevent session timeouts
* 3.0.5 - Updated SDK to the latest version (6.3.10)
* 3.0.4 - Updated SDK to the latest version (6.3.3)
* 3.0.3 - Updated SDK to the latest version (6.2.5)
* 3.0.2 - Updated to use latest buildpack to address vulnerabilities | Update `Get Agent Details`:  extended output to include `agent` field when no assets are found
* 3.0.1 - Update 'Get Agent Details' to allow no assets to be returned | SDK bump to latest version
* 3.0.0 - Update `Get Agent Details` and `Get All Agents by IP` to return the next page token if more pages are available to search | Update `Get Agent Details` to return agent location details | Initial updates for fedramp compliance | Updated SDK to the latest version
* 2.1.2 - Improve logging | Update SDK
* 2.1.1 - `Get All Agents by IP Address`: Fixed issue where action failed when agent did not have a primary address, and extended output to include agent location details | `Get Agent Details`: Extended output to include agent's public IP address and location
* 2.1.0 - Updated SDK to the latest version | New action added `Get All Agents by IP Address`
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