# Description

[FireEye HX](https://www.fireeye.com/solutions/hx-endpoint-security-products.html) is an integrated endpoint solution that detects, prevents and responds effectively to known malware and threats traditional anti-virus endpoint security products miss. The FireEye plugin will allow you to get alerts from a given host.

This plugin utilizes the FireEye HX API. Documentation for the API is located in your FireEye HX appliance.

# Key Features

* Get alerts for a host
* Get host ID from hostname
* Quarantine and unquarantine a host
* Check quarantine status

# Requirements

* FireEye credentials

# Supported Product Versions

* 5.2.0.958244

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ssl_verify|boolean|True|True|Validate SSL certificate|None|True|
|url|string|None|True|URL to the appliance, e.g. https://test.fireeye.com|None|https://example.com|
|username_password|credential_username_password|None|True|Username and password to authenticate with FireEye HX|None|{"username": "user", "password": "password"}|

Example input:

```
{
  "ssl_verify": true,
  "url": "https://example.com",
  "username_password": {
    "username": "user",
    "password": "password"
  }
}
```

## Technical Details

### Actions

#### Unquarantine Host

This action is used to remove a host from quarantine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_id|string|None|False|The ID of the agent you want to unisolate|None|44d88612fea8a8f36de82e|

Example input:

```
{
  "agent_id": "44d88612fea8a8f36de82e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the action was successful|

Example output:

```
{
  "success": true
}
```

#### Quarantine Host

This action is used to quarantine a host.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_id|string|None|False|The ID of the agent you want to isolate|None|44d88612fea8a8f36de82e|

Example input:

```
{
  "agent_id": "44d88612fea8a8f36de82e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the action was successful|

Example output:

```
{
  "success": true
}
```

#### Check Host Quarantine Status

This action is used to check whether a host is quarantined or not.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_id|string|None|False|The ID of the agent you want to check|None|44d88612fea8a8f36de82e|

Example input:

```
{
  "agent_id": "44d88612fea8a8f36de82e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|data|False|Results obtained for a specific agent|

Example output:

```
{
  "results": {
    "_id": "44d88612fea8a8f36de82e",
    "last_sysinfo": "2022-01-05T04:14:47.419Z",
    "requested_by_actor": {
      "_id": 1000,
      "username": "admin"
    },
    "requested_on": "2022-01-05T16:56:52.718Z",
    "contained_by_actor": {
      "_id": 1000,
      "username": "admin"
    },
    "contained_on": "2022-01-05T16:56:52.718Z",
    "queued": true,
    "excluded": false,
    "missing_software": false,
    "reported_clone": false,
    "state": "uncontaining",
    "state_update_time": "2022-01-05T17:11:03.276Z",
    "url": "/hx/api/v3/hosts/44d88612fea8a8f36de82e"
  }
}
```

#### Get Host ID from Hostname

This action is used to get a host ID from a given hostname.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|True|Hostname|None|example_hostname|

Example input:

```
{
  "hostname": "example_hostname"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|host_id|string|False|ID for the host|
|success|boolean|True|Whether or not a match was found|

Example output:

```
{
  "success": true,
  "host_id": "BoT1FTG1l92f2LeJVh6e3p"
}
```

#### Get Alerts by Host ID

This action is used to get alerts for a host given the host ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|host_id|string|None|True|Host ID|None|44d88612fea8a8f36de82e|

Example input:

```
{
  "host_id": "44d88612fea8a8f36de82e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert|False|Alerts|

Example output:

```
{
  "alerts": [{
    "_id": 1,
    "agent": {
      "_id": "44d88612fea8a8f36de82e",
      "url": "/hx/api/v3/hosts/44d88612fea8a8f36de82e",
      "containment_state": "normal"
    },
    "condition": {
      "_id": "G7fmpVr1gxFU2JKXUIu2Cg==",
      "url": "/hx/api/v3/conditions/G7fmpVr1gxFU2JKXUIu2Cg=="
    },
    "indicator": {
      "_id": "9db96bbe-2417-4c4f-ba33-4f5895244d88",
      "url": "/hx/api/v3/indicators/custom/website",
      "uri_name": "website"
    },
    "event_at": "2019-04-09T19:50:53.115Z",
    "matched_at": "2019-04-09T19:53:47.000Z",
    "reported_at": "2019-04-09T19:54:07.251Z",
    "source": "IOC",
    "matched_source_alerts": [],
    "resolution": "ALERT",
    "is_false_positive": false,
    "url": "/hx/api/v3/alerts/1",
    "event_id": 4887,
    "event_type": "ipv4NetworkEvent",
    "event_values": {
      "ipv4NetworkEvent/timestamp": "2019-04-09T19:50:53.115Z",
      "ipv4NetworkEvent/remoteIP": "8.8.8.8",
      "ipv4NetworkEvent/remotePort": 0,
      "ipv4NetworkEvent/localIP": "10.0.2.15",
      "ipv4NetworkEvent/localPort": 0,
      "ipv4NetworkEvent/protocol": "ICMP",
      "ipv4NetworkEvent/pid": 0
    }
  }]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### agent

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Agent ID|
|Containment State|string|False|Containment state of the agent|
|URL|string|False|Relative URL for the agent|

#### alert

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert ID|number|False|Alert ID|
|Agent|agent|False|Agent associated with the alert|
|Condition|condition|False|Condition associated with the alert|
|Event At|date|False|Timestamp for the alert|
|Event ID|number|False|ID of the event|
|Event Type|string|False|Type of alert event that occurred|
|Event Values|event_values|False|Information about the alert. These properties may/may not be available depending on the 'Event Type' property|
|Indicator|indicator|False|Alert indicator|
|Is False Positive|boolean|False|Whether or not the alert is a false positive|
|Matched At|date|False|When the alert rule matched|
|Matched Source Alerts|[]object|False|Matched source alerts|
|Reported At|date|False|Timestamp for the alert report|
|Resolution|string|False|Resolution|
|Source|string|False|Alert source|
|Subtype|string|False|Alert subtype|

#### condition

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Condition ID|
|URL|string|False|Relative URL for the condition|

#### data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Contained By Actor|user|False|Contained by actor|
|Contained On|string|False|Contained on|
|Excluded|boolean|False|Excluded|
|Last System Info|string|False|Last System Info|
|Missing Software|boolean|False|Missing software|
|Queued|boolean|False|Queued|
|Reported Clone|boolean|False|Reported clone|
|Requested By Actor|user|False|Requested by actor|
|Requested On|string|False|Requested on|
|State|string|False|State|
|State Update Time|string|False|State update time|
|URL|string|False|URL|

#### event_values

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DNS Lookup Event Hostname|string|False|Hostname|
|DNS Lookup Event PID|number|False|PID|
|DNS Lookup Event Process|string|False|Process|
|DNS Lookup Event Process Path|string|False|Process path|
|DNS Lookup Event Timestamp|date|False|Timestamp of the DNS lookup event|
|DNS Lookup Event Username|string|False|Username|
|File Write Event Closed|number|False|Closed|
|File Write Event Data at Lowest Offset|string|False|Data at lowest offset, base64-encoded|
|File Write Event Device Path|string|False|Device path|
|File Write Event Drive|string|False|Drive|
|File Write Event File Extension|string|False|File extension|
|File Write Event File Name|string|False|File name|
|File Write Event File Path|string|False|File path|
|File Write Event Full Path|string|False|Full path|
|File Write Event Lowest File Offset Seen|number|False|Lowest file offset seen|
|File Write Event MD5|string|False|MD5 hash|
|File Write Event Number of Bytes Seen Written|number|False|Number of bytes seen written|
|File Write Event PID|number|False|PID|
|File Write Event Process|string|False|Process|
|File Write Event Process Path|string|False|Process path|
|File Write Event Size|number|False|number|
|File Write Event Text at Lowest Offset|string|False|Text at lowest offset|
|File Write Event Timestamp|date|False|Timestamp of the file write event|
|File Write Event Username|string|False|Username|
|File Write Event Writes|number|False|Amount of file writes|
|IPv4 Network Event Local IP Address|string|False|Local IP address|
|IPv4 Network Event Local Port|number|False|Local port|
|IPv4 Network Event PID|number|False|PID|
|IPv4 Network Event Protocol|string|False|Protocol, e.g. 'ICMP'|
|IPv4 Network Event Remote IP Address|string|False|Remote IP address|
|IPv4 Network Event Remote Port|number|False|Remote port|
|IPv4 Network Event Timestamp|date|False|Event timestamp|

#### indicator

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Indicator ID|
|Display Name|string|False|Indicator display name|
|URI Name|string|False|URI name|
|URL|string|False|Relative URL for the indicator|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|ID|
|Username|string|False|Username|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Add new actions Quarantine Host, Unquarantine Host and Check Quarantine Status | Add `SSL Verify` input in connection | Add missing input examples | Correct type for `subtype` in custom output for Get Alerts from Host ID action | Code refactor
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [FireEye HX](https://www.fireeye.com/solutions/hx-endpoint-security-products.html)

