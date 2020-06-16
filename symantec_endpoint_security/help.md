# Description

Broadcom Symantec Endpoint Security delivers the most complete, integrated endpoint security platform on the planet

# Key Features

* Get details about an agent

# Requirements

* Credentials with system administrator privileges for a Broadcom Symantec Endpoint Protection server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username": example, "password": "test"}|
|domain|string|None|True|The Symantec Endpoint Protection Manager domain to which the username logs on|None|mydomain|
|host|string|None|True|Symantec Endpoint Protection Manager host, either IP address or domain|None|sepm-14|
|port|integer|8446|True|Symantec Endpoint Protection server port, typically 8446|None|8446|

Example input:

```
{
  "credentials": {"username": example, "password": "test"},
  "domain": "mydomain",
  "host": "sepm-14",
  "port": 8446
}
```
## Technical Details

### Actions

#### Blacklist

This action is used to blacklist MD5 or SHA256 hashes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|True|Description for the blacklist|None|Hashes banned via InsightConnect|
|domain_id|string|None|False|ID of the domain to apply the blacklist to. Omitting this input will apply the blacklist to all domains (globally)|None|0AF740760A0414711FAA4F8BD5293158|
|hashes|[]string|None|True|Hashes (MD5 or SHA256) to add to the blacklist. Note: only one type of hash is allowed at a time|None|["9de5069c5afe602b2ea0a04b66beb2c0"]|
|name|string|None|True|Name for the blacklist|None|Insightconnect Blacklist|

Example input:

```
{
  "description": "Hashes banned via InsightConnect",
  "domain_id": "0AF740760A0414711FAA4F8BD5293158",
  "hashes": ["9de5069c5afe602b2ea0a04b66beb2c0"],
  "name": "Hashes Blacklisted from InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|blacklist_ids|[]string|True|IDs of the resulting blacklists|

Example output:

```
{
  "blacklist_id": "5348023646E740128BFE65939934F22E"
}
```

#### Get Agent Details

This action is used to get details about an agent by MAC address or computer hostname.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device from. This can be by MAC address or computer hostname|None|example|

Example input:

```
{
  "agent": "example"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent|False|Agent matching the search|

Example output:

```
{
  "agent": {
    "group": {
      "id": "18175BEC0A041471455851B8A7FC6DFA",
      "name": "My Company",
      "domain": {
        "id": "0AF740760A0414711FAA4F8BD5293158",
        "name": "Default"
      }
    },
    "ipAddresses": [
      "10.0.2.15",
      "FE80:0000:0000:0000:C50D:519F:96A4:E108"
    ],
    "macAddresses": [
      "08-00-27-E6-E5-59",
      "08-00-27-E6-E5-59"
    ],
    "gateways": [
      "10.0.2.2",
      "10.0.2.2",
      "0.0.0.0",
      "0.0.0.0"
    ],
    "subnetMasks": [
      "255.255.255.0",
      "64"
    ],
    "dnsServers": [
      "10.100.2.16",
      "10.3.20.98"
    ],
    "winServers": [
      "0.0.0.0",
      "0.0.0.0"
    ],
    "computerName": "MSEDGEWIN10",
    "logonUserName": "IEUser",
    "domainOrWorkgroup": "WORKGROUP",
    "processorType": "Intel64 Family 6 Model 158 Stepping 9",
    "processorClock": 2904,
    "physicalCpus": 1,
    "logicalCpus": 0,
    "memory": 4294496256,
    "biosVersion": "VBOX   - 1 Default System BIOS",
    "osFunction": "Workstation",
    "osFlavorNumber": 72,
    "osName": "Windows 10",
    "operatingSystem": "Windows 10 Enterprise Edition",
    "osVersion": "10.0",
    "osMajor": 10,
    "osMinor": 0,
    "osServicePack": "17763",
    "osBitness": "x64",
    "uniqueId": "2B7FC95F0A0414712696BCE4A85D3078",
    "hardwareKey": "597057FB87284766266A402197C13D81",
    "uuid": "A25C0116-FD2F-0349-90FB-222743811CA4",
    "osLanguage": "en-US",
    "totalDiskSpace": 40957,
    "groupUpdateProvider": false,
    "deploymentStatus": "302456832",
    "deploymentTargetVersion": "14.2.5587.2100",
    "deploymentRunningVersion": "14.2.5587.2100",
    "lastDeploymentTime": 1591816149000,
    "virtualizationPlatform": "Unknown",
    "serialNumber": "0",
    "installType": "0",
    "agentVersion": "14.2.5587.2100",
    "publicKey": "BgIAAACkAABSU0ExAAgAAAEAAQDtx14yMTyXdwYXpOW68pSD4mfl0meHOOxGdD9nrOPELvhbaOu3Sap0Y9VvR6TzmswJThm/M/MlYTeDM173scodxCl2DAndiAJYtR5z68t7PLl5IvsewupHPM741c+EcEerC74cDVtxgQukR+lNDQPMDVYEC2E08v2I3GSOBOi+Ul2hxQXVlzY150ESaDH8MvZLYI6dSspE23sVb8Vxg3Fu0OVxhCfyoKRSpKQteB3PqaPqfq8yPklTQG6pz55/RMtVdBRjxySZ6/LYW3PMcDarB5QqYc2hCzVaMQUPv7BGeia7zNTzgfxeSDY0rmk7lMHjhwhhefOzEHZrt5iDutnH",
    "deleted": 0,
    "quarantineDesc": "Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.",
    "loginDomain": "LocalComputer",
    "agentId": "99B2418F0A0414712696BCE414F41AF9",
    "agentType": "105",
    "profileVersion": "14.2.5587",
    "profileSerialNo": "1817-05/13/2020 07:00:58 109",
    "creationTime": 1591815925623,
    "onlineStatus": 1,
    "lastUpdateTime": 1591897737728,
    "lastServerId": "A07CF4460A0414713B76CCCCCCD23F1A",
    "lastServerName": "sepm-14",
    "lastSiteId": "E72A08130A041471254EC66AB59640FF",
    "lastSiteName": "My Site",
    "agentTimeStamp": 1591897737774,
    "agentUsn": 622913,
    "patternIdx": "CC5409F2699A5F0322A5345A4C1E9AE9",
    "apOnOff": 1,
    "infected": 0,
    "worstInfectionIdx": "9999",
    "lastScanTime": 1591891833000,
    "lastVirusTime": 0,
    "contentUpdate": 1,
    "avEngineOnOff": 1,
    "avDefsetVersion": "200611002",
    "avDefsetSequence": "206913",
    "avDefsetRevision": "2",
    "tamperOnOff": 1,
    "majorVersion": 14,
    "minorVersion": 2,
    "rebootRequired": 0,
    "licenseStatus": -1,
    "licenseExpiry": 0,
    "timeZone": 480,
    "firewallOnOff": 1,
    "freeMem": 2499801088,
    "freeDisk": 18510696448,
    "lastDownloadTime": 1591815956390,
    "currentClientId": "EC933C970A0414712696BCE437BA1C43",
    "isGrace": 0,
    "ptpOnOff": 1,
    "lastHeuristicThreatTime": 0,
    "bashStatus": 1,
    "daOnOff": 1,
    "cidsDrvOnOff": 1,
    "cidsSilentMode": 0,
    "cidsDrvMulfCode": 2,
    "cidsBrowserIeOnOff": 1,
    "cidsBrowserFfOnOff": 1,
    "cidsEngineVersion": "0.0.0.0",
    "cidsDefsetVersion": "200610061",
    "elamOnOff": 1,
    "osElamStatus": 0,
    "tdadOnOff": 3,
    "tdadStatusId": 127,
    "tdadGlobalDataDownloadTime": 0,
    "vsicStatus": 3,
    "isNpvdiClient": 0,
    "lastConnectedIpAddr": "10.3.20.8",
    "pepOnOff": 1,
    "edrStatus": 0,
    "tpmDevice": "0",
    "dhcpServer": "10.0.2.2",
    "computerTimeStamp": 1591891797587,
    "computerUsn": 621735,
    "diskDrive": "C:\\",
    "hypervisorVendorId": "0",
    "bwf": 2,
    "fbwf": 2,
    "uwf": 2,
    "telemetryMid": "9AE3D66D-721D-47B0-9B57-A946F8337C94",
    "telemetryHwid": "B86FA340-96B4-1BC7-A624-A098B0195E22"
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

* [Broadcom Symantec Endpoint Security](https://www.broadcom.com/products/cyber-security/endpoint/end-user)
