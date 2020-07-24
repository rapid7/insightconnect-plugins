# Description

Investigate and mitigate vulnerabilities across your organization using the power of the [Insight Agent](https://docs.rapid7.com/insight-agent/overview/). 

# Key Features

* Get details about devices
* Qurantine and unquarantine devices

# Requirements

* Platform API Key: [Mange Platform API Keys](https://docs.rapid7.com/insight/managing-platform-api-keys/)
* Organization ID: (See Page 10 of the GraphQL API doc)

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|User or Organization Key from the Insight Platform|None|a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99|
|org_id|credential_secret_key|None|True|Organization ID|None|2cg99z6y-795n-7bzf-hj67-12355h554974|
|region|string|United States|True|Region|['United States', 'Europe', 'Canada', 'Australia', 'Japan']|United States|

Example input:

```
{
  "api_key": "a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99",
  "org_id": "2cg99z6y-795n-7bzf-hj67-12355h554974",
  "region": "United States"
}
```

## Technical Details

### Actions

#### Quarantine

This action is used to quarantine or release quarantine on a device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_id|string|None|True|The ID of the agent on the device to quarantine|None|a1cfb273c8e7d46a9e2a0e2dae01a0ce|
|interval|int|604800|True|Length in time in seconds to try to take action on a device. This is also called Advertisement Period|None|604800|
|quarantine_state|boolean|True|True|Set to true to quarantine a host, set to false to release quarantine|None|True|

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

This action this action is used to find and display detailed information about a device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|IP address, MAC address, or host name of the device to get information from|None|MaliciousHost|

Example input:

```
{
  "agent": "MaliciousHost"
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

* 1.0.0 - Initial plugin

# Links

## References

* [Rapid7 Insight Agent](https://docs.rapid7.com/insight-agent/overview/)
* [Mange Platform API Keys](https://docs.rapid7.com/insight/managing-platform-api-keys/)
*  
