# Description

Broadcom Symantec Endpoint Protection delivers the most complete, integrated endpoint security platform on the planet

# Key Features

* Get details about an agent
* Blacklist hashes
* Quarantine an agent

# Requirements

* Credentials with system administrator privileges for a Broadcom Symantec Endpoint Protection server

# Supported Product Versions

* v1 2025/08/21

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username and password|None|{'username': 'example', 'password': 'test'}|None|None|
|domain|string|None|False|The Symantec Endpoint Protection Manager domain to which the username logs on|None|mydomain|None|None|
|host|string|None|True|Symantec Endpoint Protection Manager host, either IP address or domain|None|sepm-14|None|None|
|port|integer|8446|True|Symantec Endpoint Protection server port, typically 8446|None|8446|None|None|
|ssl_verify|boolean|None|True|Whether to enable SSL verification for HTTP requests|None|True|None|None|

Example input:

```
{
  "credentials": {
    "password": "test",
    "username": "example"
  },
  "domain": "mydomain",
  "host": "sepm-14",
  "port": 8446,
  "ssl_verify": true
}
```

## Technical Details

### Actions


#### Blacklist

This action is used to blacklist MD5 hashes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|True|Description for the blacklist|None|Hashes Blacklisted from InsightConnect|None|None|
|domain_id|string|None|False|ID of the domain to apply the blacklist to. Omitting this input will apply the blacklist to all domains (globally)|None|0AF740760A0414711FAA4F8BD5293158|None|None|
|hashes|[]string|None|True|MD5 hashes to add to the blacklist|None|["9de5069c5afe602b2ea0a04b66beb2c0"]|None|None|
|name|string|None|True|Name for the blacklist|None|InsightConnect Blacklist|None|None|
  
Example input:

```
{
  "description": "Hashes Blacklisted from InsightConnect",
  "domain_id": "0AF740760A0414711FAA4F8BD5293158",
  "hashes": [
    "9de5069c5afe602b2ea0a04b66beb2c0"
  ],
  "name": "InsightConnect Blacklist"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|blacklist_ids|[]string|True|IDs of the resulting blacklists|["5348023646E740128BFE65939934F22E", "5348023646E740128BFE65939934B13E"]|
  
Example output:

```
{
  "blacklist_ids": [
    "5348023646E740128BFE65939934F22E",
    "5348023646E740128BFE65939934B13E"
  ]
}
```

#### Get Agent Details

This action is used to get details about an agent by MAC address or computer hostname

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent to retrieve device from. This can be by MAC address or computer hostname|None|example|None|None|
  
Example input:

```
{
  "agent": "example"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agent|agent|False|Agent matching the search|{ "group": { "id": "18175BEC0A041471455851B8A7FC6DFA", "name": "My Company", "domain": { "id": "0AF740760A0414711FAA4F8BD5293158", "name": "Default" } }, "ipAddresses": [ "198.51.100.100", "2001:db8:8:4::2" ], "macAddresses": [ "08-00-27-E6-E5-59", "08-00-27-E6-E5-59" ], "gateways": [ "198.51.100.1" ], "subnetMasks": [ "255.255.255.0", "64" ], "dnsServers": [ "10.100.2.16", "10.3.20.98" ], "winServers": [ "0.0.0.0", "0.0.0.0" ], "computerName": "MSEDGEWIN10", "logonUserName": "IEUser", "domainOrWorkgroup": "WORKGROUP", "processorType": "Intel64 Family 6 Model 158 Stepping 9", "processorClock": 2904, "physicalCpus": 1, "logicalCpus": 0, "memory": 4294496256, "biosVersion": "VBOX   - 1 Default System BIOS", "osFunction": "Workstation", "osFlavorNumber": 72, "osName": "Windows 10", "operatingSystem": "Windows 10 Enterprise Edition", "osVersion": "10.0", "osMajor": 10, "osMinor": 0, "osServicePack": "17763", "osBitness": "x64", "uniqueId": "2B7FC95F0A0414712696BCE4A85D3078", "hardwareKey": "597057FB87284766266A402197C13D81", "uuid": "A25C0116-FD2F-0349-90FB-222743811CA4", "osLanguage": "en-US", "totalDiskSpace": 40957, "groupUpdateProvider": false, "deploymentStatus": "302456832", "deploymentTargetVersion": "14.2.5587.2100", "deploymentRunningVersion": "14.2.5587.2100", "lastDeploymentTime": 1591816149000, "virtualizationPlatform": "Unknown", "serialNumber": "0", "installType": "0", "agentVersion": "14.2.5587.2100", "publicKey": "BgIAAACkAABSU0ExAAgAAAEAAQDtx14yMTyXdwYXpOW68pSD4mfl0meHOOxGdD9nrOPELvhbaOu3Sap0Y9VvR6TzmswJThm/M/MlYTeDM173scodxCl2DAndiAJYtR5z68t7PLl5IvsewupHPM741c+EcEerC74cDVtxgQukR+lNDQPMDVYEC2E08v2I3GSOBOi+Ul2hxQXVlzY150ESaDH8MvZLYI6dSspE23sVb8Vxg3Fu0OVxhCfyoKRSpKQteB3PqaPqfq8yPklTQG6pz55/RMtVdBRjxySZ6/LYW3PMcDarB5QqYc2hCzVaMQUPv7BGeia7zNTzgfxeSDY0rmk7lMHjhwhhefOzEHZrt5iDutnH", "deleted": 0, "quarantineDesc": "Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.", "loginDomain": "LocalComputer", "agentId": "99B2418F0A0414712696BCE414F41AF9", "agentType": "105", "profileVersion": "14.2.5587", "profileSerialNo": "1817-05/13/2020 07:00:58 109", "creationTime": 1591815925623, "onlineStatus": 1, "lastUpdateTime": 1591897737728, "lastServerId": "A07CF4460A0414713B76CCCCCCD23F1A", "lastServerName": "sepm-14", "lastSiteId": "E72A08130A041471254EC66AB59640FF", "lastSiteName": "My Site", "agentTimeStamp": 1591897737774, "agentUsn": 622913, "patternIdx": "CC5409F2699A5F0322A5345A4C1E9AE9", "apOnOff": 1, "infected": 0, "worstInfectionIdx": "9999", "lastScanTime": 1591891833000, "lastVirusTime": 0, "contentUpdate": 1, "avEngineOnOff": 1, "avDefsetVersion": "200611002", "avDefsetSequence": "206913", "avDefsetRevision": "2", "tamperOnOff": 1, "majorVersion": 14, "minorVersion": 2, "rebootRequired": 0, "licenseStatus": -1, "licenseExpiry": 0, "timeZone": 480, "firewallOnOff": 1, "freeMem": 2499801088, "freeDisk": 18510696448, "lastDownloadTime": 1591815956390, "currentClientId": "EC933C970A0414712696BCE437BA1C43", "isGrace": 0, "ptpOnOff": 1, "lastHeuristicThreatTime": 0, "bashStatus": 1, "daOnOff": 1, "cidsDrvOnOff": 1, "cidsSilentMode": 0, "cidsDrvMulfCode": 2, "cidsBrowserIeOnOff": 1, "cidsBrowserFfOnOff": 1, "cidsEngineVersion": "0.0.0.0", "cidsDefsetVersion": "200610061", "elamOnOff": 1, "osElamStatus": 0, "tdadOnOff": 3, "tdadStatusId": 127, "tdadGlobalDataDownloadTime": 0, "vsicStatus": 3, "isNpvdiClient": 0, "lastConnectedIpAddr": "198.51.100.100", "pepOnOff": 1, "edrStatus": 0, "tpmDevice": "0", "dhcpServer": "10.0.2.2", "computerTimeStamp": 1591891797587, "computerUsn": 621735, "diskDrive": "C:\\", "hypervisorVendorId": "0", "bwf": 2, "fbwf": 2, "uwf": 2, "telemetryMid": "9AE3D66D-721D-47B0-9B57-A946F8337C94", "telemetryHwid": "B86FA340-96B4-1BC7-A624-A098B0195E22" }|
  
Example output:

```
{
  "agent": {
    "agentId": "99B2418F0A0414712696BCE414F41AF9",
    "agentTimeStamp": 1591897737774,
    "agentType": "105",
    "agentUsn": 622913,
    "agentVersion": "14.2.5587.2100",
    "apOnOff": 1,
    "avDefsetRevision": "2",
    "avDefsetSequence": "206913",
    "avDefsetVersion": "200611002",
    "avEngineOnOff": 1,
    "bashStatus": 1,
    "biosVersion": "VBOX   - 1 Default System BIOS",
    "bwf": 2,
    "cidsBrowserFfOnOff": 1,
    "cidsBrowserIeOnOff": 1,
    "cidsDefsetVersion": "200610061",
    "cidsDrvMulfCode": 2,
    "cidsDrvOnOff": 1,
    "cidsEngineVersion": "0.0.0.0",
    "cidsSilentMode": 0,
    "computerName": "MSEDGEWIN10",
    "computerTimeStamp": 1591891797587,
    "computerUsn": 621735,
    "contentUpdate": 1,
    "creationTime": 1591815925623,
    "currentClientId": "EC933C970A0414712696BCE437BA1C43",
    "daOnOff": 1,
    "deleted": 0,
    "deploymentRunningVersion": "14.2.5587.2100",
    "deploymentStatus": "302456832",
    "deploymentTargetVersion": "14.2.5587.2100",
    "dhcpServer": "10.0.2.2",
    "diskDrive": "C:\\",
    "dnsServers": [
      "10.100.2.16",
      "10.3.20.98"
    ],
    "domainOrWorkgroup": "WORKGROUP",
    "edrStatus": 0,
    "elamOnOff": 1,
    "fbwf": 2,
    "firewallOnOff": 1,
    "freeDisk": 18510696448,
    "freeMem": 2499801088,
    "gateways": [
      "198.51.100.1"
    ],
    "group": {
      "domain": {
        "id": "0AF740760A0414711FAA4F8BD5293158",
        "name": "Default"
      },
      "id": "18175BEC0A041471455851B8A7FC6DFA",
      "name": "My Company"
    },
    "groupUpdateProvider": false,
    "hardwareKey": "597057FB87284766266A402197C13D81",
    "hypervisorVendorId": "0",
    "infected": 0,
    "installType": "0",
    "ipAddresses": [
      "198.51.100.100",
      "2001:db8:8:4::2"
    ],
    "isGrace": 0,
    "isNpvdiClient": 0,
    "lastConnectedIpAddr": "198.51.100.100",
    "lastDeploymentTime": 1591816149000,
    "lastDownloadTime": 1591815956390,
    "lastHeuristicThreatTime": 0,
    "lastScanTime": 1591891833000,
    "lastServerId": "A07CF4460A0414713B76CCCCCCD23F1A",
    "lastServerName": "sepm-14",
    "lastSiteId": "E72A08130A041471254EC66AB59640FF",
    "lastSiteName": "My Site",
    "lastUpdateTime": 1591897737728,
    "lastVirusTime": 0,
    "licenseExpiry": 0,
    "licenseStatus": -1,
    "logicalCpus": 0,
    "loginDomain": "LocalComputer",
    "logonUserName": "IEUser",
    "macAddresses": [
      "08-00-27-E6-E5-59",
      "08-00-27-E6-E5-59"
    ],
    "majorVersion": 14,
    "memory": 4294496256,
    "minorVersion": 2,
    "onlineStatus": 1,
    "operatingSystem": "Windows 10 Enterprise Edition",
    "osBitness": "x64",
    "osElamStatus": 0,
    "osFlavorNumber": 72,
    "osFunction": "Workstation",
    "osLanguage": "en-US",
    "osMajor": 10,
    "osMinor": 0,
    "osName": "Windows 10",
    "osServicePack": "17763",
    "osVersion": "10.0",
    "patternIdx": "CC5409F2699A5F0322A5345A4C1E9AE9",
    "pepOnOff": 1,
    "physicalCpus": 1,
    "processorClock": 2904,
    "processorType": "Intel64 Family 6 Model 158 Stepping 9",
    "profileSerialNo": "1817-05/13/2020 07:00:58 109",
    "profileVersion": "14.2.5587",
    "ptpOnOff": 1,
    "publicKey": "BgIAAACkAABSU0ExAAgAAAEAAQDtx14yMTyXdwYXpOW68pSD4mfl0meHOOxGdD9nrOPELvhbaOu3Sap0Y9VvR6TzmswJThm/M/MlYTeDM173scodxCl2DAndiAJYtR5z68t7PLl5IvsewupHPM741c+EcEerC74cDVtxgQukR+lNDQPMDVYEC2E08v2I3GSOBOi+Ul2hxQXVlzY150ESaDH8MvZLYI6dSspE23sVb8Vxg3Fu0OVxhCfyoKRSpKQteB3PqaPqfq8yPklTQG6pz55/RMtVdBRjxySZ6/LYW3PMcDarB5QqYc2hCzVaMQUPv7BGeia7zNTzgfxeSDY0rmk7lMHjhwhhefOzEHZrt5iDutnH",
    "quarantineDesc": "Host Integrity check is disabled.\n Host Integrity policy has been disabled by the administrator.",
    "rebootRequired": 0,
    "serialNumber": "0",
    "subnetMasks": [
      "255.255.255.0",
      "64"
    ],
    "tamperOnOff": 1,
    "tdadGlobalDataDownloadTime": 0,
    "tdadOnOff": 3,
    "tdadStatusId": 127,
    "telemetryHwid": "B86FA340-96B4-1BC7-A624-A098B0195E22",
    "telemetryMid": "9AE3D66D-721D-47B0-9B57-A946F8337C94",
    "timeZone": 480,
    "totalDiskSpace": 40957,
    "tpmDevice": "0",
    "uniqueId": "2B7FC95F0A0414712696BCE4A85D3078",
    "uuid": "A25C0116-FD2F-0349-90FB-222743811CA4",
    "uwf": 2,
    "virtualizationPlatform": "Unknown",
    "vsicStatus": 3,
    "winServers": [
      "0.0.0.0",
      "0.0.0.0"
    ],
    "worstInfectionIdx": "9999"
  }
}
```

#### Quarantine

This action is used to quarantine (isolate) endpoint an endpoint

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent to perform quarantine action on. This must be either a MAC address or hostname|None|example_host|None|None|
|quarantine_state|boolean|True|True|True to quarantine host, false to unquarantine host|None|True|None|None|
|whitelist|[]string|None|False|MAC addresses for machines to avoid quarantining. Both hyphenated and colon-delimited formats are acceptable|None|["01:23:45:67:89:AB", "89-67-45-23-10-CD"]|None|None|
  
Example input:

```
{
  "agent": "example_host",
  "quarantine_state": true,
  "whitelist": [
    "01:23:45:67:89:AB",
    "89-67-45-23-10-CD"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether or not the quarantine/unquarantine was successful|True|
|whitelisted|boolean|True|Whether or not the quarantine/unquarantine failed due to whitelisting|True|
  
Example output:

```
{
  "success": true,
  "whitelisted": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**domain**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID|None|
|Name|string|None|False|Name|None|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Domain|domain|None|False|The Broadcom Symantec Endpoint Protection Manager domain to which this group belongs|None|
|External Reference ID|string|None|False|The external reference ID for this group, between 1 - 50|None|
|Full Path Name|string|None|False|The full path of the group including the root group, which SEPM sets. It is not user-configurable|None|
|ID|string|None|False|The group ID, which SEPM sets. It is not user-configurable|None|
|Name|string|None|False|The name of the group|None|
|Source|string|None|False|Source|None|
  
**agent**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent ID|string|None|False|Agent ID|None|
|Agent Timestamp|integer|None|False|Agent timestamp|None|
|Agent Type|string|None|False|Agent type|None|
|Agent USN|integer|None|False|Agent USN|None|
|Agent Version|string|None|False|Agent version|None|
|AP On Off|integer|None|False|AP on off|None|
|ATP Device ID|string|None|False|ATP device ID|None|
|ATP Server|string|None|False|ATP server|None|
|Attribute Extension|string|None|False|Attribute extension|None|
|AV Definition Set Revision|string|None|False|AV definition set revision|None|
|AV Definition Set Sequence|string|None|False|AV definition set sequence|None|
|AV Definition Set Version|string|None|False|AV definition set version|None|
|AV Engine On Off|integer|None|False|AV engine on off|None|
|Bash status|integer|None|False|Bash status|None|
|BIOS Version|string|None|False|BIOS version|None|
|BWF|integer|None|False|BWF|None|
|CIDS Browser FF On Off|integer|None|False|CIDS browser FF on off|None|
|CIDS Browser IE On Off|integer|None|False|CIDS browser IE on off|None|
|CIDS Definition Set Version|string|None|False|CIDS definition set version|None|
|CIDS DRV Mulf Code|integer|None|False|CIDS DRV mulf code|None|
|CIDS Drv On Off|integer|None|False|CIDS drv on off|None|
|CIDS Engine Version|string|None|False|CIDS engine version|None|
|CIDS Silent Mode|integer|None|False|CIDS silent mode|None|
|Computer Description|string|None|False|Computer description|None|
|Computer Name|string|None|False|Computer name|None|
|Computer Timestamp|integer|None|False|Computer timestamp|None|
|Computer USN|integer|None|False|Computer USN|None|
|Content Update|integer|None|False|Content update|None|
|Creation Time|integer|None|False|Creation time|None|
|Current Client ID|string|None|False|Current client ID|None|
|DA On Off|integer|None|False|DA on off|None|
|Deleted|integer|None|False|Deleted|None|
|Department|string|None|False|Department|None|
|Deployment Message|string|None|False|Deployment message|None|
|Deployment Pre-version|string|None|False|Deployment pre-version|None|
|Deployment Running Version|string|None|False|Deployment running version|None|
|Deployment Status|string|None|False|Deployment status|None|
|Deployment Target Version|string|None|False|Deployment target version|None|
|Description|string|None|False|Description|None|
|DHCP Server|string|None|False|DHCP server|None|
|Disk Drive|string|None|False|Disk drive|None|
|DNS Servers|[]string|None|False|DNS servers|None|
|Domain or Workgroup|string|None|False|Domain or workgroup|None|
|EDR Status|integer|None|False|EDR status|None|
|Elam On Off|integer|None|False|Elam on off|None|
|Email|string|None|False|Email|None|
|Employee Number|string|None|False|Employee number|None|
|Employee Status|string|None|False|Employee status|None|
|Encrypted Device Password|string|None|False|Encrypted device password|None|
|FBWF|integer|None|False|FBWF|None|
|Firewall On Off|integer|None|False|Firewall on off|None|
|Free Disk|integer|None|False|Free disk|None|
|Free Memory|integer|None|False|Free memory|None|
|Full Name|string|None|False|Full name|None|
|Gateways|[]string|None|False|Gateways|None|
|Group|group|None|True|Group that the agent belongs to|None|
|Group Update Provider|boolean|None|False|Group update provider|None|
|Hardware Key|string|None|False|Hardware key|None|
|Home Phone|string|None|False|Home phone|None|
|Hypervisor Vendor ID|string|None|False|Hypervisor vendor ID|None|
|IDS Checksum|string|None|False|IDS checksum|None|
|IDS Serial Number|string|None|False|IDS serial number|None|
|IDS Version|string|None|False|IDS version|None|
|Infected|integer|None|False|Infected|None|
|Install Type|string|None|False|Install type|None|
|IP Addresses|[]string|None|False|IP addresses|None|
|Is Grace|integer|None|False|Is grace|None|
|Is NPVDI Client|integer|None|False|Is NPVDI client|None|
|Job Title|string|None|False|Job title|None|
|Kernel|string|None|False|Kernel|None|
|Last Connected IP Address|string|None|False|Last connected IP address|None|
|Last Deployment Time|integer|None|False|Lastd eployment time|None|
|Last Download Time|integer|None|False|Last download time|None|
|Last Heuristic Threat Time|integer|None|False|Last heuristic threat time|None|
|Last Scan Time|integer|None|False|Last scan time|None|
|Last server ID|string|None|False|Last server ID|None|
|Last Server Name|string|None|False|Last server name|None|
|Last Site ID|string|None|False|Last site ID|None|
|Last Site Name|string|None|False|Last site name|None|
|Last Update Time|integer|None|False|Last update time|None|
|Last Virus Time|integer|None|False|Last virus time|None|
|License Expiry|integer|None|False|License expiry|None|
|License Id|string|None|False|License ID|None|
|License Status|integer|None|False|License status|None|
|Logical CPUs|integer|None|False|Logical CPUs|None|
|Login Domain|string|None|False|Login domain|None|
|Logon Username|string|None|False|Logon username|None|
|MAC Addresses|[]string|None|False|MAC addresses|None|
|Major Version|integer|None|False|Major version|None|
|Memory|integer|None|False|Memory|None|
|Minor Version|integer|None|False|Minor version|None|
|Mobile Phone|string|None|False|Mobile phone|None|
|Office Phone|string|None|False|Office phone|None|
|Online Status|integer|None|False|Online status|None|
|Operating System|string|None|False|Operating system|None|
|OS Bitness|string|None|False|OS bitness|None|
|OS ElAM Status|integer|None|False|OS ELAM status|None|
|OS Flavor Number|integer|None|False|OS flavor number|None|
|OS Function|string|None|False|OS function|None|
|OS Language|string|None|False|OS language|None|
|OS Major Version|integer|None|False|OS major version|None|
|OS Minor Version|integer|None|False|OS minor version|None|
|OS Name|string|None|False|OS name|None|
|OS Service Pack|string|None|False|OS service pack|None|
|OS Version|string|None|False|OS version|None|
|Pattern IDX|string|None|False|Pattern IDX|None|
|PEP On Off|integer|None|False|PEP on off|None|
|Physical CPUs|integer|None|False|Physical CPUs|None|
|Processor Clock|integer|None|False|Processor clock|None|
|Processor Type|string|None|False|Processor type|None|
|Profile Checksum|string|None|False|Profile checksum|None|
|Profile Serial Number|string|None|False|Profile serial number|None|
|Profile Version|string|None|False|Profile version|None|
|PTP On Off|integer|None|False|PTP on off|None|
|Public Key|string|None|False|Public key|None|
|Quarantine Description|string|None|False|Quarantine description|None|
|Reboot Reason|string|None|False|Reboot reason|None|
|Reboot Required|integer|None|False|Reboot required|None|
|Security Virtual Appliance|string|None|False|Security virtual appliance|None|
|Serial Number|string|None|False|Serial number|None|
|SNAC license ID|string|None|False|SNAC license ID|None|
|Subnet Masks|[]string|None|False|Subnet masks|None|
|SVA ID|string|None|False|SVA ID|None|
|Tamper On Off|integer|None|False|Tamper on off|None|
|TDAD Global Data Download Time|integer|None|False|TDAD global data download time|None|
|TDAD On Off|integer|None|False|TDAD on off|None|
|TDAD Status ID|integer|None|False|TDAD status ID|None|
|Telemetry HWID|string|None|False|Telemetry HWID|None|
|Telemetry MID|string|None|False|Telemetry MID|None|
|Time Zone|integer|None|False|Time zone|None|
|Tmp Device|string|None|False|Tmp device|None|
|Total Disk Space|integer|None|False|Total disk space|None|
|TPM Device|string|None|False|TPM device|None|
|Unique ID|string|None|False|Unique ID|None|
|UUID|string|None|False|UUID|None|
|UWF|integer|None|False|UWF|None|
|Virtualization|string|None|False|Virtualization platform|None|
|VSIC Status|integer|None|False|VSIC status|None|
|Winservers|[]string|None|False|Winservers|None|
|Worst Infection IDX|string|None|False|Worst infection IDX|None|
|Write Filters Status|string|None|False|Write filters status|None|


## Troubleshooting

* The Broadcom Symantec Endpoint Protection API does not allow for updating blacklists. The plugin will fail if it is told to create a blacklist with the name of a blacklist that already exists.
* Domain IDs are not the actual domain names - they are individual, unique IDs that come back as part of the 'Get Agent Details' action.

# Version History

* 2.0.4 - Resolving Snyk Vulnerability | SDK bump to latest version (6.3.9)
* 2.0.3 - Bumping requirements.txt ('aiohttp' package) | SDK bump to 6.2.2
* 2.0.2 - Bumping requirements.txt ('aiohttp' package) | SDK bump to 6.2.0
* 2.0.1 - Bumping requirements.txt | SDK bump to 6.1.4
* 2.0.0 - Update Connection to add `ssl_verify` parameters to enable SSL verification on HTTP requests
* 1.0.3 - Update SDK to version to 5.4.4 | Update aiohttp to 3.9.2
* 1.0.2 - Update Blacklist action to not accept SHA256 hashes
* 1.0.1 - Workflow usability fixes
* 1.0.0 - Initial plugin

# Links

* [Symantec Enterprise API Documentation](https://apidocs.securitycloud.symantec.com/#/)

## References

* [Broadcom Symantec Endpoint Protection](https://www.broadcom.com/products/cyber-security/endpoint/end-user)