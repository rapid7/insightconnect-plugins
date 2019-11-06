# Description

[FireEye HX](https://www.fireeye.com/solutions/hx-endpoint-security-products.html) is an integrated endpoint solution that detects, prevents and responds effectively to known malware and threats traditional anti-virus endpoint security products miss.

This plugin utilizes the FireEye HX API. Documentation for the API is located in your FireEye HX appliance.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username_password|credential_username_password|None|True|Username and password to authenticate with FireEye HX|None|
|url|string|None|True|URL to the appliance, e.g. https\://test.fireeye.com|None|

## Technical Details

### Actions

#### Get Host ID from Hostname

This action is used to get a host ID from a given hostname.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|Hostname|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host_id|string|None|True|Host ID|None|

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
      "_id": "BoT1FTG1l92f2LeJVh6e3p",
      "url": "/hx/api/v3/hosts/BoT1FTG1l92f2LeJVh6e3p",
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

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [FireEye HX](https://www.fireeye.com/solutions/hx-endpoint-security-products.html)

