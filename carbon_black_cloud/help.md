# Description

The VMware Carbon Black Cloud is a cloud-native endpoint protection platform (EPP) that combines the intelligent system hardening and behavioral prevention needed to keep emerging threats at bay, using a single lightweight agent and an easy-to-use console

# Key Features

* Get device information

# Requirements

* API Credentials
* Base URL

# Documentation

## Setup

For information on how to get the API credentials and your base URL please see the [Carbon Black Authentication](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication/) documentation.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_id|string|None|True|API ID|None|ADFF2QLIIZ|
|api_secret_key|credential_secret_key|None|True|API secret key|None|Z1PXFRDZI321LXQVAB9IJKKZ|
|org_key|string|None|True|Organization Key|None|1ABZY2FJ|
|url|string|https://defense.conferdeploy.net|True|API URL|None|https://defense.conferdeploy.net|

Example input:

```
{
  "api_id": "ADFF2QLIIZ",
  "api_secret_key": "Z1PXFRDZI321LXQVAB9IJKKZ",
  "org_key": "1ABZY2FJ",
  "url": "https://defense.conferdeploy.net"
}
```

## Technical Details

### Actions

#### Quarantine

This action is used to quarantine an agent.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, hostname, or device ID. Search results are case-sensitive|None|198.51.100.100|
|quarantine_state|boolean|True|True|Would you like to qarantine the agent. Set to true to quarantine the agent, set to false to unquarantine an agent|None|True|
|whitelist|[]string|None|False|An array of IPs, hostnames, or device ID that a user can pass in that will not be quarantined|None|["198.51.100.100", "win-test"]|

Example input:

```
{
  "agent": "198.51.100.100",
  "quarantine_state": true,
  "whitelist": [
    "198.51.100.100",
    "win-test"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|quarantined|boolean|True|Is the agent quarantined|

Example output:

```
```

#### Get Agent Details

This action is used to get Agent Details.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, hostname, or device ID. Search results are case-sensitive|None|198.51.100.100|

Example input:

```
{
  "agent": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent|False|Details about the agent|

Example output:

```
{
  "agent": {
    "adGroupId": 0,
    "policyOverride": false,
    "currentSensorPolicyName": null,
    "deviceMetaDataItemList": null,
    "lastDevicePolicyRequestedTime": null,
    "lastDevicePolicyChangedTime": null,
    "lastPolicyUpdatedTime": null,
    "loginUserName": null,
    "messages": null,
    "lastReportedTime": 1591962280381,
    "uninstallCode": null,
    "organizationId": 1105,
    "deviceId": 3466056,
    "createTime": null,
    "deviceGuid": null,
    "email": "user@example.com",
    "deviceSessionId": null,
    "deviceType": "WINDOWS",
    "assignedToId": null,
    "assignedToName": null,
    "lastName": "User",
    "firstName": "Test",
    "middleName": null,
    "deviceOwnerId": 12345,
    "activationCode": "1A2B3C",
    "targetPriorityType": "HIGH",
    "organizationName": "example.com",
    "sensorVersion": "3.5.0.1680",
    "activationCodeExpiryTime": 1234567891011,
    "sensorKitType": null,
    "osVersion": "Server 2012 x64",
    "registeredTime": 1234567891011,
    "lastContact": 1234567891011,
    "windowsPlatform": null,
    "vdiBaseDevice": null,
    "avStatus": [
      "AV_ACTIVE",
      "ONDEMAND_SCAN_DISABLED"
    ],
    "deregisteredTime": null,
    "sensorStates": [
      "ACTIVE",
      "LIVE_RESPONSE_NOT_RUNNING",
      "LIVE_RESPONSE_NOT_KILLED",
      "LIVE_RESPONSE_ENABLED",
      "SECURITY_CENTER_OPTLN_DISABLED"
    ],
    "rootedBySensor": false,
    "rootedBySensorTime": null,
    "quarantined": false,
    "lastInternalIpAddress": "198.51.100.100",
    "macAddress": "000000000000",
    "lastExternalIpAddress": "198.51.100.100",
    "lastLocation": "OFFSITE",
    "sensorOutOfDate": false,
    "avUpdateServers": null,
    "passiveMode": false,
    "lastResetTime": 0,
    "lastShutdownTime": 0,
    "scanStatus": null,
    "scanLastActionTime": 0,
    "scanLastCompleteTime": 0,
    "linuxKernelVersion": null,
    "avEngine": "4.13.0.207-ave.8.3.60.40:avpack.8.5.0.60:vdf.8.18.2.56:apc.2.10.0.149",
    "avProductVersion": "4.13.0.207",
    "avAveVersion": "8.3.60.40",
    "avPackVersion": "8.5.0.60",
    "avVdfVersion": "8.18.2.56",
    "avLastScanTime": 0,
    "virtualMachine": false,
    "virtualizationProvider": "UNKNOWN",
    "sensorPendingUpdate": false,
    "rootedByAnalytics": false,
    "rootedByAnalyticsTime": null,
    "avMaster": false,
    "firstVirusActivityTime": 0,
    "lastVirusActivityTime": 0,
    "testId": -1,
    "uninstalledTime": null,
    "encodedActivationCode": null,
    "originEventHash": null,
    "name": "example-host",
    "status": "REGISTERED",
    "policyId": 12345,
    "policyName": "test"
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

* [Carbon Black Cloud](https://www.carbonblack.com/products/vmware-carbon-black-cloud)
* [Carbon Black Authentication](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication/)
