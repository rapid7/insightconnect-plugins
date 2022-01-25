# Description

[FireEye HX](https://www.fireeye.com/solutions/hx-endpoint-security-products.html) is an integrated endpoint solution that detects, prevents and responds effectively to known malware and threats traditional anti-virus endpoint security products miss. The FireEye plugin will allow you to get alerts from a given host.

This plugin utilizes the FireEye HX API. Documentation for the API is located in your FireEye HX appliance.

# Key Features

* Get alerts for a host
* Get host ID from hostname

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

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Add new actions Quarantine Host, Unquarantine Host and Check Quarantine Status | Add `ssl_verify` input in connection | Add missing input examples | Code refactor 
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [FireEye HX](https://www.fireeye.com/solutions/hx-endpoint-security-products.html)

