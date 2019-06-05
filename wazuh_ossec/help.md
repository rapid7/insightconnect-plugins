
# Wazuh OSSEC

## About

[Wazuh](https://www.wazuh.com) is an open source project that provides security visibility, compliance and infrastructure monitoring capabilities.
The project was born as a fork of OSSEC HIDS. This plugin utilizes the [Wazuh API](https://documentation.wazuh.com/current/user-manual/api/reference.html).

## Actions

### Manager Logs Summary

This action is used to return a summary about the 3 last months of ossec.log.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|wazuh-modulesd|summary_log|False|None|
|ossec-testrule|summary_log|False|None|
|wazuh-modulesd:oscap|summary_log|False|None|
|ossec-rootcheck|summary_log|False|None|
|ossec-monitord|summary_log|False|None|
|ossec-logcollector|summary_log|False|None|
|ossec-execd|summary_log|False|None|
|ossec-remoted|summary_log|False|None|
|ossec-syscheckd|summary_log|False|None|
|error|integer|True|None|
|ossec-analysisd|summary_log|False|None|
|wazuh-modulesd:database|summary_log|False|None|

Example output:

```

{
  "ossec-monitord": {
    "info": 21,
    "error": 0,
    "all": 21
  },
  "wazuh-modulesd": {
    "info": 1,
    "error": 0,
    "all": 1
  },
  "ossec-testrule": {
    "info": 79,
    "error": 0,
    "all": 79
  },
  "wazuh-modulesd:oscap": {
    "info": 1,
    "error": 0,
    "all": 1
  },
  "ossec-execd": {
    "info": 1,
    "error": 0,
    "all": 1
  },
  "ossec-rootcheck": {
    "info": 15,
    "error": 0,
    "all": 15
  },
  "ossec-remoted": {
    "info": 4,
    "error": 0,
    "all": 4
  },
  "ossec-syscheckd": {
    "info": 37,
    "error": 0,
    "all": 37
  },
  "ossec-logcollector": {
    "info": 5,
    "error": 0,
    "all": 5
  },
  "ossec-authd": {
    "info": 1,
    "error": 0,
    "all": 1
  },
  "ossec-analysisd": {
    "info": 177,
    "error": 0,
    "all": 177
  },
  "wazuh-modulesd:database": {
    "info": 1,
    "error": 83,
    "all": 84
  },
  "error": 0
}

```

### Agent Restart

This action is used to restart all agents, or a specified agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|agent_id|string|None|True|Agent ID e.g. 003. If no agent is specified, all agents will be restarted|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Status message|
|error|integer|True|None|

### Manager Information

This action is used to return basic information about the manager.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|max_agents|string|True|None|
|openssl_support|string|True|None|
|ruleset_version|string|True|None|
|tz_name|string|True|None|
|tz_offset|string|True|None|
|installation_date|string|True|None|
|version|string|True|None|
|error|integer|True|None|
|path|string|True|None|
|type|string|True|None|

### Manager Stats

This action is used to returns OSSEC statistical information of current date.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|date|string|None|False|Selects the date for getting the statistical information. Format\: YYYYMMDD|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stats|[]stats|True|None|
|error|integer|True|None|

Example output:

```

{
  "stats": [
    {
      "totalAlerts": 70,
      "firewall": 0,
      "events": 98,
      "hour": 0,
      "syscheck": 0,
      "alerts": [
        {
          "sigid": 530,
          "times": 70,
          "level": 0
        }
      ]
    },
    {
      "totalAlerts": 63,
      "firewall": 0,
      "events": 90,
      "hour": 1,
      "syscheck": 0,
      "alerts": [
        {
          "sigid": 530,
          "times": 63,
          "level": 0
        }
      ]
    },
    {
      "totalAlerts": 85,
      "firewall": 0,
      "events": 1802,
      "hour": 2,
      "syscheck": 1689,
      "alerts": [
        {
          "sigid": 530,
          "times": 70,
          "level": 0
        },
        {
          "sigid": 515,
          "times": 4,
          "level": 0
        },
        {
          "sigid": 516,
          "times": 11,
          "level": 3
        }
      ]
    }
  ],
  "error": 0
}

```

### Syscheck Database

This action is used to return the syscheck files of an agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sort|string|None|False|Sorts the collection by a field or fields (separated by comma). Use +/- at the begining to ascending or descending order. Allowed sort fields\: group, user, file, modificationDate, scanDate, and size|None|
|search|string|None|False|Looks for elements with the specified string|None|
|sha1|string|None|False|Returns the files with the specified SHA1 hash|None|
|hash|string|None|False|Returns the files with the specified hash (MD5 or SHA1)|None|
|filetype|string|None|False|Selects type of file|['All', 'File', 'Registry']|
|limit|integer|None|False|Maximum number of elements to return|None|
|agent_id|string|None|True|Agent ID e.g. 003|None|
|file|string|None|False|Filters file by filename|None|
|offset|integer|None|False|First element to return in the collection|None|
|event|string|None|False|Filters files by event|['All', 'Added', 'Readded', 'Modified', 'Deleted']|
|md5|string|None|False|Returns the files with the specified MD5 hash|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|totalItems|integer|True|None|
|syscheck_events|[]rootcheck_events|True|None|
|error|integer|True|None|

### Agent Delete

This action is used to removes an agent. You must restart OSSEC after removing an agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|agent_id|string|None|True|Agent ID e.g. 003|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Status message|
|error|integer|True|Error code|

### Agent Info

This action is used to return the information of an agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|agent_id|string|None|True|Agent ID e.g. 003|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|None|
|name|string|True|None|
|ip|string|True|None|
|dateAdd|string|True|None|
|version|string|True|None|
|os_family|string|True|None|
|error|integer|True|None|
|lastKeepAlive|string|True|None|
|os|string|True|None|
|id|string|True|None|

### Syscheck Delete

This action is used to clear the syscheck database for all agents, or a specified agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|agent_id|string|None|False|Agent ID e.g. 003. If no agent is specified, the database will be cleared for all agents|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Status message|
|error|integer|True|Error code|

### Manager Stats Hourly

This action is used to return OSSEC statistical information per hour. Each item in averages field represents the average of alerts per hour.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|interactions|integer|True|None|
|averages|[]integer|True|None|
|error|integer|True|None|

### Rootcheck Info

This action is used to return the timestamp of the last rootcheck scan.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|agent_id|string|None|True|Agent ID e.g. 003|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rootcheckEndTime|string|True|None|
|rootcheckTime|string|True|None|
|error|integer|True|Error code|

### Agent Key

This action is used to return the key of an agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|agent_id|string|None|True|Agent ID e.g. 003|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|key|string|True|None|
|error|integer|True|None|

### Syscheck Info

This action is used to return the timestamp of the last syscheck scan.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|agent_id|string|None|True|Agent ID e.g. 003|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|syscheckTime|string|True|None|
|syscheckEndTime|string|True|None|
|error|integer|True|Error code|

### Rootcheck Database

This action is used to return the rootcheck database of an agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sort|string|None|False|Sorts the collection by a field or fields (separated by comma). Use +/- at the begining to ascending or descending order. Allowed sort fields\: status, oldDay, event, and readDay|None|
|cis|string|None|False|Filters by CIS|None|
|search|string|None|False|Looks for elements with the specified string|None|
|pci|string|None|False|Filters by PCI requirement|None|
|limit|integer|None|False|Maximum number of elements to return|None|
|agent_id|string|None|True|Agent ID e.g. 003|None|
|offset|integer|None|False|First element to return in the collection|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|totalItems|integer|True|None|
|rootcheck_events|[]rootcheck_events|True|None|
|error|integer|True|None|

### Rootcheck Delete

This action is used to clear the rootcheck database for all agents, or a specified agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|agent_id|string|None|False|Agent ID e.g. 003. If no agent is specified, the database will be cleared for all agents|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Status message|
|error|integer|True|Error code|

### Manager Status

This action is used to return the manager processes that are running.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|wazuh-modulesd|string|True|None|
|ossec-authd|string|True|None|
|ossec-monitord|string|True|None|
|ossec-logcollector|string|True|None|
|ossec-execd|string|True|None|
|ossec-remoted|string|True|None|
|ossec-syscheckd|string|True|None|
|error|integer|True|None|
|ossec-analysisd|string|True|None|
|ossec-maild|string|True|None|

### Manager Logs

This action is used to return the 3 last months of ossec.log.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sort|string|None|False|Sorts the collection by a field or fields (separated by comma). Use +/- at the begining to ascending or descending order|None|
|category|string|None|False|Filters by category of log|None|
|search|string|None|False|Looks for elements with the specified string|None|
|type_log|string|None|False|Filters by type of log|['All', 'Error', 'Info']|
|limit|integer|None|False|Maximum number of elements to return|None|
|offset|integer|None|False|First element to return in the collection|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|totalItems|integer|True|None|
|logs|[]string|True|None|
|error|integer|True|None|

### Agent Summary

This action is used to return a summary of the available agents.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Active|integer|True|Active agents|
|Never_connected|integer|True|Never connected agents|
|Total|integer|True|Total agents|
|Disconnected|integer|True|Disconnected agents|
|error|integer|True|None|

### Agents List

This action is used to return a list with the available agents.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sort|string|None|False|Sorts the collection by a field or fields (separated by comma). Use +/- at the begining to ascending or descending order. Allowed sort fields are status, ip, id, and name|None|
|status|string|None|False|Filters by agent status|['All', 'Active', 'Never Connected', 'Disconnected']|
|search|string|None|False|Looks for elements with the specified string|None|
|limit|integer|None|False|Maximum number of elements to return|None|
|offset|integer|None|False|First element to return in the collection|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|totalItems|integer|True|None|
|agents|[]agents|True|None|
|error|integer|True|Error code|

Example output:

```

{
  "error": 0,
  "agents": [
    {
      "name": "wazuh-manager",
      "id": "000",
      "status": "Active",
      "ip": "127.0.0.1"
    },
    {
      "name": "wazuh-agent",
      "id": "001",
      "status": "Active",
      "ip": "192.168.1.100"
    }
  ],
  "totalItems": 2
}

```

### Agent Add

This action is used to add a new agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip|string|None|False|If you do not include this param, the API will get the IP automatically. If you are behind a proxy, you must set the option config.BehindProxyServer to yes at config.js.|None|
|force|string|None|False|Remove old agent with same IP if disconnected since force seconds|None|
|name|string|None|True|Agent name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|True|Agent ID|
|error|integer|True|Error code|

### Agent Scan

This action is used to run syscheck and rootcheck on all agents, or a specified agent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|agent_id|string|None|False|Agent ID e.g. 003. If no agent is specified, scans will take place on all agents|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Status message|
|error|integer|True|Error code|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Wazuh API URL e.g. https\://127.0.0.1\:55000|None|
|username|string|None|True|Wazuh API Username|None|
|password|string|None|True|Wazuh API Password|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

* Agent management
* Alert enrichment

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types

## References

* [Wazuh](https://wazuh.com)
* [Wazuh API](https://documentation.wazuh.com/current/user-manual/api/reference.html)
