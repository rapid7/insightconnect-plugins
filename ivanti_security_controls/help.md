# Description

Ivanti Security Controls is a unified IT management platform used for managing and protecting through Patch Management, Application Control, and Asset Inventory functionality.

# Key Features

* Ability to retrieve Ivanti Security Controls known agents
* Ability to check agent status

# Requirements

* Ivanti Security Controls host and API port (default: 3121)
* Username and password of Windows account where Ivanti Security Controls is installed 
* (Recommended) Ivanti Security Controls certificate in order to enforce certificate verification

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|
|host|string|None|True|Enter the hostname|None|hostname-1|
|port|integer|3121|True|Enter the port|None|3121|
|ssl_verify|boolean|True|True|Validate certificate|None|True|

## Technical Details

### Actions

#### Get Agents

This action is used to retrieve Agent from Ivanti Security Controls.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_configuration_filter|string|All|False|Filters agents based on listening configuration|['Listening', 'Not Listening', 'All']|All|
|name_filter|string|None|False|Filters agents where host or DNS name equals this value|None|hostname-1|

Example input:

```
{
  "agent_configuration_filter": "All",
  "name_filter": "hostname-1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents|[]agent_detail|False|List of agent details|
|count|integer|False|Number of agents returned|

Example output:

```
{
  "agents": [
    {
      "agentId": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD",
      "assignedPolicyId": "6b98cab4-1da7-4a4a-827b-bfd303e4c813",
      "domain": "WORKGROUP",
      "frameworkVersion": "9.4.34534.0",
      "isListening": false,
      "lastCheckIn": "2020-04-28T19:02:20.473",
      "links": {
        "checkin": {
          "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/checkin"
        },
        "queuedTasks": {
          "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/queuedTask"
        },
        "self": {
          "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
        },
        "status": {
          "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/status"
        },
        "tasks": {
          "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/tasks"
        }
      },
      "machineName": "hostname-1",
      "reportedPolicyId": "6b98cab4-1da7-4a4a-827b-bfd303e4c813",
      "status": "Installed"
    }
  ],
  "count": 1
}
```

#### Get Agent Status

This action is used to retrieve Agent Status from Ivanti Security Controls.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Agent Identifier|None|ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD|

Example input:

```
{
  "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent_status|agent_status|True|Agent status with details|

Example output:

```
{
  "agent_status": {
    "agentId": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD",
    "frameworkVersion": {
      "build": 34534,
      "major": 9,
      "majorRevision": 0,
      "minor": 4,
      "minorRevision": 0,
      "revision": 0
    },
    "installedPackages": [
      "AGENTASSET64"
    ],
    "lastCheckIn": "2020-04-28T15:05:48.1909093Z",
    "links": {
      "self": {
        "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
      }
    },
    "machineName": "iase-win10",
    "reportedOn": "2020-04-28T19:28:19.5756267Z",
    "runningPolicyId": "916f3bae-1667-4354-8203-234309e31e00",
    "runningPolicyVersion": 18005
  }
}
```

#### Get Agent

This action is used to retrieve Agent from Ivanti Security Controls.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Agent Identifier|None|ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD|

Example input:

```
{
  "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent_detail|True|Details about an agent|

Example output:

```
{
  "agent": {
    "agentId": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD",
    "assignedPolicyId": "6b98cab4-1da7-4a4a-827b-bfd303e4c813",
    "domain": "WORKGROUP",
    "frameworkVersion": "9.4.34534.0",
    "isListening": false,
    "lastCheckIn": "2020-04-28T19:02:20.473",
    "links": {
      "checkin": {
        "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/checkin"
      },
      "queuedTasks": {
        "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/queuedTask"
      },
      "self": {
        "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD"
      },
      "status": {
        "href": "https://localhost:3121/st/console/api/v1.0/agents/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/status"
      },
      "tasks": {
        "href": "https://localhost:3121/st/console/api/v1.0/agenttasks/ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD/tasks"
      }
    },
    "machineName": "splunk-724-w12",
    "reportedPolicyId": "6b98cab4-1da7-4a4a-827b-bfd303e4c813",
    "status": "Installed"
  }
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### agent_detail

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent ID|string|True|The agent ID|
|Assigned Policy ID|string|False|The unique identifier of the policy that is in effect for this agent|
|DNS Name|string|False|The DNS name of the agent machine|
|Domain|string|False|The domain of the agent machine|
|Framework Version|string|False|The installed agent framework version|
|Is Listening|boolean|False|Specifies if the agent is a listening agent|
|Last Check-In|string|False|The date and time of the most recent check-in|
|Last Known IP Address|string|False|The last known IP address of the agent machine|
|Agent Links|object|False|Shows the related URLs for the agent|
|Listening Port|integer|False|The listening port number|
|Machine Name|string|False|The agent machine's host name|
|Reported Policy ID|string|False|The agent policy ID|
|Status|string|True|The current status of the agent|

#### agent_status

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent ID|string|True|The agent ID|
|Framework Version|object|False|The installed agent framework version|
|Installed Packages|[]string|False|The list of engines installed on the agent machine|
|Last Check-In|string|False|The date and time of the most recent check-in|
|Agent Links|object|False|Shows the related URLs for the agent|
|Machine Name|string|False|The agent machine's host name|
|Reported On|string|False|The time the information was gathered from the agent machine|
|Running Policy ID|string|False|The agent's running policy ID|
|Running Policy Version|integer|False|The agent's policy ID|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Ivanti Security Controls](https://www.ivanti.com/products/security-controls)
* [Ivanti Security Controls API Documentation](https://help.ivanti.com/iv/help/en_US/isec/API/Topics/Welcome.htm)
