# Description

The [Insight Agent](https://docs.rapid7.com/insight-agent/overview/) collects live system information, easily centralizing and monitoring data on the Insight platform. Using the Insight Agent plugin from InsightConnect, you can quarantine, unquarantine and monitor potentially malicious IPs, addresses, hostnames, and devices across your organization.

The agent is used by [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/) and [InsightVM](https://www.rapid7.com/products/insightvm/) customers to monitor endpoints.

# Key Features

* Get details about devices
* Quarantine and unquarantine devices

# Requirements

* [Platform API Key](https://docs.rapid7.com/insight/managing-platform-api-keys/)
* Administrator access to InsightIDR

# Supported Product Versions

* Rapid7 Insight Agent

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

This action is used to get the online status and quarantine state of an agent.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_id|string|None|True|The ID of the agent on the device to get the status from|None|a1cfb273c8e7d46a9e2a0e2dae01a0ce|

Example input:

```
{
  "agent_id": "a1cfb273c8e7d46a9e2a0e2dae01a0ce"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|is_asset_online|boolean|True|Indicates that the agent is connected to the Insight platform. This means the device is powered on and is connected to Rapid7|
|is_currently_quarantined|boolean|True|Is the device currently quarantined|
|is_quarantine_requested|boolean|True|Is a quarantine action pending on this device|
|is_unquarantine_requested|boolean|True|Is there a pending request to release quarantine on this device|

Example output:

```
{
  "is_currently_quarantined": true,
  "is_asset_online": true,
  "is_quarantine_requested": false,
  "is_unquarantine_requested": false
}
```

#### Quarantine

This action is used to quarantine or release quarantine on a device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Get Agent Details

This action is used to find and display detailed information about a device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|IP address, MAC address, or hostname of the device to get information from|None|Example-Hostname|

Example input:

```
{
  "agent": "Example-Hostname"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent|True|Agent information|

Example output:

```
{
  "agent": {
    "id": "15eec979a15f75ad70567d58ad8a0aef",
    "vendor": "Microsoft",
    "version": "SP1",
    "description": "Microsoft Windows 7 Professional SP1",
    "hostNames": [
      {
        "name": "joey-w7-vagrant-pc"
      }
    ],
    "primaryAddress": {
      "ip": "10.0.2.15",
      "mac": "08-00-27-33-9F-CE"
    },
    "uniqueIdentity": [
      {
        "source": "Endpoint Agent",
        "id": "15eec979a15f75ad70567d58ad8a0aef"
      },
      {
        "source": "CSPRODUCT",
        "id": "030B19C0-F12D-6643-B86E-FA7C08A4A838"
      }
    ],
    "attributes": [
      {
        "key": "cpuinfo",
        "value": "Intel(R) Core(TM) i7-6920HQ CPU @ 2.90GHz"
      },
      {
        "key": "timezone",
        "value": "GMT-7"
      },
      {
        "key": "release",
        "value": "7"
      },
      {
        "key": "proxies",
        "value": "{}"
      }
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

* 1.0.4 - Add new supported regions for API
* 1.0.3 - Documentation update
* 1.0.2 - Fix for a case-sensitive agent hostname
* 1.0.1 - Documentation update
* 1.0.0 - Initial plugin

# Links

## References

* [Rapid7 Insight Agent](https://docs.rapid7.com/insight-agent/overview/)
* [Manage Platform API Keys](https://docs.rapid7.com/insight/managing-platform-api-keys/)
