# Description

Powered by Cyber AI, [Darktrace’s Enterprise Immune System](https://www.darktrace.com/en/) detects and responds to unpredictable cyber-threats across your dynamic workforce – from email, cloud, and collaboration platforms, to distributed clients and the corporate network.

# Key Features

* Add or remove watched domains

# Requirements

* Requires a public and private API token

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_private_token|credential_secret_key|None|True|Enter API private token|None|1452d258-7c12-7c12-7c12-1452d25874c2|
|api_public_token|credential_secret_key|None|True|Enter API public token|None|1452d258-7c12-7c12-7c12-1452d25874c2|
|url|string|None|True|API URL|None|None|

Example input:

```
{
  "api_private_token": "1452d258-7c12-7c12-7c12-1452d25874c2",
  "api_public_token": "1452d258-7c12-7c12-7c12-1452d25874c2"
}
```

## Technical Details

### Actions

#### Update Watched Domains

This action is used to add or remove items from the Watched Domains list. If an indicator is added, Darktrace will monitor network traffic for that URL and create alerts from it.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|Watched Domains managed by InsightConnect|False|Description of the indicator|None|Watched Domains managed by InsightConnect|
|entry|string|None|True|An external domain, hostname or IP address|None|192.168.10.10|
|expiration_time|string|None|False|Expiration time of an indicator|None|2020-04-03 15:23:20|
|hostname|boolean|None|False|Set to true to treat the added items as hostnames rather than domains|None|True|
|source|string|InsightConnect|False|Source of an indicator|None|InsightConnect|
|watched_domain_status|boolean|None|True|Determine whether item should be added or remove from the list. Set True to add, set false to remove|None|True|

Example input:

```
{
  "description": "Watched Domains managed by InsightConnect",
  "entry": "192.168.10.10",
  "expiration_time": "2020-04-03 15:23:20",
  "hostname": true,
  "source": "InsightConnect",
  "watched_domain_status": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|added|integer|False|Added|
|success|boolean|True|Success|
|updated|integer|False|Updated|

Example output:

```
{
  "added": 1,
  "success": true,
  "updated": 0
}
```

### Triggers

#### Get Alerts

This trigger is used to trigger workflows on model breach alerts and logs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|did|integer|None|False|ID of device modelled in the Darktrace system|None|1|
|frequency|integer|300|False|Poll frequency in seconds|None|300|
|minscore|integer|None|False|Return only breaches with a minimum score. Valid values are 0-100.|None|10|
|pbid|integer|None|False|Only return the model breach with the specified policy breach ID|None|300|
|pid|integer|None|False|Only return model breaches for the specified model|None|300|
|uuid|string|None|False|Only return model breaches for the specified model|None|fc707223-d2d2-475c-b09b-dec4e800eb2e|

Example input:

```
{
  "did": 1,
  "frequency": 300,
  "minscore": 10,
  "pbid": 300,
  "pid": 300,
  "uuid": "fc707223-d2d2-475c-b09b-dec4e800eb2e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]results|True|Alerts results|

Example output:

```
{
  "creationTime": 1599807740000,
  "commentCount": 0,
  "pbid": 11,
  "time": 1599807736000,
  "model": {
    "then": {
      "name": "System::Packet Loss",
      "pid": 371,
      "phid": 371,
      "uuid": "b81117bc-2d11-4ed6-11d0-9dd2958cfbff",
      "logic": {
        "data": [
          780
        ],
        "type": "componentList",
        "version": 1
      },
      "throttle": 86400,
      "sharedEndpoints": false,
      "actions": {
        "alert": true,
        "antigena": {},
        "breach": true,
        "model": true,
        "setPriority": false,
        "setTag": false,
        "setType": false
      },
      "tags": [],
      "interval": 3600,
      "sequenced": false,
      "active": true,
      "modified": "2020-09-01 00:11:34",
      "activeTimes": {
        "devices": {},
        "tags": {},
        "type": "exclusions",
        "version": 2
      },
      "priority": 0,
      "autoUpdatable": true,
      "autoUpdate": true,
      "autoSuppress": true,
      "description": "Packet loss is higher than 30%. Sustained packet loss at or above this level will significantly impact Darktrace detections.\\n\\nAction: Investigate why Darktrace is missing so much traffic. Use the status page to see if the loss is occurring on specific subnets. This model indicates the packet loss is occurring before Darktrace ingestion rather than a problem with the appliance.",
      "behaviour": "decreasing",
      "defeats": [],
      "created": {
        "by": "System"
      },
      "edited": {
        "by": "Nobody"
      },
      "version": 10
    },
    "now": {
      "name": "System::Packet Loss",
      "pid": 371,
      "phid": 371,
      "uuid": "b81117bc-2d11-4ed6-11d0-9dd2958cfbff",
      "logic": {
        "data": [
          780
        ],
        "type": "componentList",
        "version": 1
      },
      "throttle": 86400,
      "sharedEndpoints": false,
      "actions": {
        "alert": true,
        "antigena": {},
        "breach": true,
        "model": true,
        "setPriority": false,
        "setTag": false,
        "setType": false
      },
      "tags": [],
      "interval": 3600,
      "sequenced": false,
      "active": true,
      "modified": "2020-09-01 00:11:34",
      "activeTimes": {
        "devices": {},
        "tags": {},
        "type": "exclusions",
        "version": 2
      },
      "priority": 0,
      "autoUpdatable": true,
      "autoUpdate": true,
      "autoSuppress": true,
      "description": "Packet loss is higher than 30%. Sustained packet loss at or above this level will significantly impact Darktrace detections.\\n\\nAction: Investigate why Darktrace is missing so much traffic. Use the status page to see if the loss is occurring on specific subnets. This model indicates the packet loss is occurring before Darktrace ingestion rather than a problem with the appliance.",
      "behaviour": "decreasing",
      "defeats": [],
      "created": {
        "by": "System"
      },
      "edited": {
        "by": "Nobody"
      },
      "message": "Increasing cooldown to 24 hours, as the 3.1 software update improved the recognition and reporting of packet loss feeding into Darktrace, which has resulted in this model firing more frequently than required.",
      "version": 10
    }
  },
  "triggeredComponents": [
    {
      "time": 1599807735000,
      "cbid": 11,
      "cid": 780,
      "chid": 780,
      "size": 1,
      "threshold": 0,
      "interval": 3600,
      "logic": {
        "data": {
          "left": "A"
        },
        "version": "v0.1"
      },
      "metric": {
        "mlid": 256,
        "name": "capturelosstoomuchloss",
        "label": "Capture loss Detected upstream"
      },
      "triggeredFilters": [
        {
          "cfid": 7657,
          "id": "A",
          "filterType": "Message",
          "arguments": {
            "value": ".*rate above [3-9][0-9]\\..*\\%$"
          },
          "comparatorType": "matches regular expression",
          "trigger": {
            "value": "Host ip-192-168-10-1: The capture loss script detected an estimated loss rate above 45.679%, worker drop rate: 0.000%"
          }
        }
      ]
    }
  ],
  "score": 0.278,
  "device": {
    "did": -1
  }
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.1 - Updated help.md file
* 2.0.0 - Fix input `0` for parameters DID, PBID, Min Score and PID in trigger Get Alerts | Create new custom type for trigger Get Alerts | Change type of input parameter Min Score to integer in trigger Get Alerts
* 1.1.0 - Add new trigger Pull Alerts
* 1.0.0 - Initial plugin

# Links

## References

* [Darktrace](https://www.darktrace.com/)
