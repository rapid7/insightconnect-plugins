# Description

The Microsoft Defender for Endpoint plugin allows Rapid7 InsightConnect users to quickly take remediation actions across their organization. This plugin can isolate machines, run virus scans, and quarantine files

# Key Features

* Trigger workflows on new security alerts
* Manage isolation of network resources
* Start virus scans
* Stop execution of malicious code

# Requirements

* Windows Defender Advanced Threat Protection application credentials

# Supported Product Versions

* 2024-05-21

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|application_id|string|None|True|Application (client) ID|None|a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d|None|None|
|application_secret|credential_secret_key|None|True|Application secret|None|kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=|None|None|
|directory_id|string|None|True|Directory (tenant) ID|None|3a522933-ae5e-2b63-96ab-3c004b4f7f10|None|None|
|endpoint|string|None|True|The type of endpoint to connect to: normal service, GCC (government), GCC High (government), DoD (military)|["Normal", "GCC", "GCC High", "DoD"]|Normal|None|None|

Example input:

```
{
  "application_id": "a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d",
  "application_secret": "kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=",
  "directory_id": "3a522933-ae5e-2b63-96ab-3c004b4f7f10",
  "endpoint": "Normal"
}
```

## Technical Details

### Actions


#### Blacklist

This action is used to submit or update new indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|AlertAndBlock|False|The action that will be taken if the indicator will be discovered in the organization|["Alert", "AlertAndBlock", "Allowed", "Audit", "Block", "Warn"]|AlertAndBlock|None|None|
|application|string|None|False|The application associated with the indicator|None|demo-test|None|None|
|description|string|Indicator Blacklisted from InsightConnect|False|Description of the indicator|None|Indicator Blacklisted from InsightConnect|None|None|
|expiration_time|string|None|False|The expiration time of the indicator, default value is one year from now|None|2020-12-12T00:00:00Z|None|None|
|generate_alert|boolean|False|False|True if alert generation is required, False if this indicator shouldn't generate an alert. Please note this flag only affects the following action types [Allowed, Block, Warn]|None|True|None|None|
|indicator|string|None|True|A supported indicator to blacklist or unblacklist. Supported indicators are IP addresses, URLs, domains, and SHA1 and SHA256 hashes|None|220e7d15b011d7fac48f2bd61114db1022197f7f|None|None|
|indicator_state|boolean|False|False|True to add indicator, false to remove it from the list|None|True|None|None|
|rbac_group_names|[]string|None|False|List of RBAC group names the indicator would be applied to|None|["group1","group2"]|None|None|
|recommended_actions|string|None|False|TI indicator alert recommended actions|None|nothing|None|None|
|severity|string|High|False|The severity of the indicator|["Informational", "Low", "Medium", "High"]|High|None|None|
|title|string|None|False|Indicator alert title|None|test|None|None|
  
Example input:

```
{
  "action": "AlertAndBlock",
  "application": "demo-test",
  "description": "Indicator Blacklisted from InsightConnect",
  "expiration_time": "2020-12-12T00:00:00Z",
  "generate_alert": false,
  "indicator": "220e7d15b011d7fac48f2bd61114db1022197f7f",
  "indicator_state": false,
  "rbac_group_names": [
    "group1",
    "group2"
  ],
  "recommended_actions": "nothing",
  "severity": "High",
  "title": "test"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|indicator_action_response|indicator_action|False|A response that includes the result of the action, and supplemental information about the action taken|{'@odata.context': 'https://api.securitycenter.windows.com/api/$metadata#Indicators/$entity', 'action': 'Alert', 'application': 'application', 'category': 1, 'createdBy': '82f42fca-e931-4f03-b54c-47af94bd394d', 'createdByDisplayName': 'WindowsDefenderATPSiemConnector', 'createdBySource': 'PublicApi', 'creationTimeDateTimeUtc': '2020-07-30T19:01:56.6543461Z', 'description': 'some description', 'expirationTime': '2020-12-12T00:00:00Z', 'generateAlert': True, 'historicalDetection': False, 'id': '11', 'indicatorType': 'Url', 'indicatorValue': 'http://google.com', 'lastUpdateTime': '2020-07-30T19:02:10.9680026Z', 'lastUpdatedBy': '82f42fca-e931-4f03-b54c-47af94bd394d', 'mitreTechniques': [], 'rbacGroupIds': [], 'rbacGroupNames': [], 'recommendedActions': 'nothing', 'severity': 'Informational', 'source': 'WindowsDefenderATPSiemConnector', 'sourceType': 'AadApp', 'title': 'Title'}|
  
Example output:

```
{
  "indicator_action_response": {
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Indicators/$entity",
    "action": "Alert",
    "application": "application",
    "category": 1,
    "createdBy": "82f42fca-e931-4f03-b54c-47af94bd394d",
    "createdByDisplayName": "WindowsDefenderATPSiemConnector",
    "createdBySource": "PublicApi",
    "creationTimeDateTimeUtc": "2020-07-30T19:01:56.6543461Z",
    "description": "some description",
    "expirationTime": "2020-12-12T00:00:00Z",
    "generateAlert": true,
    "historicalDetection": false,
    "id": "11",
    "indicatorType": "Url",
    "indicatorValue": "http://google.com",
    "lastUpdateTime": "2020-07-30T19:02:10.9680026Z",
    "lastUpdatedBy": "82f42fca-e931-4f03-b54c-47af94bd394d",
    "mitreTechniques": [],
    "rbacGroupIds": [],
    "rbacGroupNames": [],
    "recommendedActions": "nothing",
    "severity": "Informational",
    "source": "WindowsDefenderATPSiemConnector",
    "sourceType": "AadApp",
    "title": "Title"
  }
}
```

#### Collect Investigation Package

This action is used to collects investigation package from a machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|Investigation package collected via InsightConnect|False|Comment to associate with the action|None|Investigation package collected via InsightConnect|None|None|
|machine|string|None|True|Machine IP address, hostname, or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
  
Example input:

```
{
  "comment": "Investigation package collected via InsightConnect",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|collect_investigation_package_response|machine_action|True|A response that includes information about the action taken|{'collect_investigation_package_response': {'requestorComment': 'Investigation package collected via InsightConnect', 'status': 'Pending', 'type': 'CollectInvestigationPackage', 'commands': [], 'creationDateTimeUtc': '2021-02-25T13:53:29.1889041Z', 'requestSource': 'PublicApi', 'id': '7de39b39-107e-4556-855b-25cf652835ef', 'lastUpdateDateTimeUtc': '2021-02-25T13:53:29.1889041Z', 'machineId': '8de370ca0e0e58ff2c2513bbc16f632ffa6e6024', 'requestor': 'b6e46392-61b9-48c0-ada3-63e3cd30d95b', '@odata.context': 'https://api.securitycenter.windows.com/api/$metada...', 'computerDnsName': 'msedgewin10', 'errorHResult': 0}}|
  
Example output:

```
{
  "collect_investigation_package_response": {
    "collect_investigation_package_response": {
      "@odata.context": "https://api.securitycenter.windows.com/api/$metada...",
      "commands": [],
      "computerDnsName": "msedgewin10",
      "creationDateTimeUtc": "2021-02-25T13:53:29.1889041Z",
      "errorHResult": 0,
      "id": "7de39b39-107e-4556-855b-25cf652835ef",
      "lastUpdateDateTimeUtc": "2021-02-25T13:53:29.1889041Z",
      "machineId": "8de370ca0e0e58ff2c2513bbc16f632ffa6e6024",
      "requestSource": "PublicApi",
      "requestor": "b6e46392-61b9-48c0-ada3-63e3cd30d95b",
      "requestorComment": "Investigation package collected via InsightConnect",
      "status": "Pending",
      "type": "CollectInvestigationPackage"
    }
  }
}
```

#### Find Machines with Installed Software

This action is used to retrieve a list of device references that have specific software installed

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|software|string|None|True|Name of the software to be searched|None|microsoft-_-edge|None|None|
  
Example input:

```
{
  "software": "microsoft-_-edge"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machines|[]machine_software|True|List of machines with provided software|[{"computerDnsName": "mseewin10", "id": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73", "osPlatform": "Windows10", "rbacGroupId": 0}]|
  
Example output:

```
{
  "machines": [
    {
      "computerDnsName": "mseewin10",
      "id": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
      "osPlatform": "Windows10",
      "rbacGroupId": 0
    }
  ]
}
```

#### Get Files from Alert

This action is used to retrieve a list of file information objects related to an alert

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|Alert ID to get files from|None|da637293198146839977_2089064327|None|None|
  
Example input:

```
{
  "alert_id": "da637293198146839977_2089064327"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file_list|[]file_type|True|The file ID related to the given alert ID|[{"sha1": "f093e7767bb63ac973b697d3fd1d40a78b87b8bf", "sha256": "470a75fe3da2ddf9d27fb3f9c96e6c665506ea7ba26ab89f0c89606f678ae4a2", "md5": "a69acb01b99959efec7c0a2a8caa7545", "globalPrevalence": 437, "globalFirstObserved": "2015-11-01T02:48:27.1103102Z", "globalLastObserved": "2020-07-05T07:58:26.8760293Z", "size": 740544, "isPeFile": True, "signerHash": "006276223396f7510653e20f0d10cd1a5d97176e", "isValidCertificate": False, "determinationType": "Unknown", "determinationValue": "HackTool:MSIL/AutoKms"}]|
  
Example output:

```
{
  "file_list": [
    {
      "determinationType": "Unknown",
      "determinationValue": "HackTool:MSIL/AutoKms",
      "globalFirstObserved": "2015-11-01T02:48:27.1103102Z",
      "globalLastObserved": "2020-07-05T07:58:26.8760293Z",
      "globalPrevalence": 437,
      "isPeFile": true,
      "isValidCertificate": false,
      "md5": "a69acb01b99959efec7c0a2a8caa7545",
      "sha1": "f093e7767bb63ac973b697d3fd1d40a78b87b8bf",
      "sha256": "470a75fe3da2ddf9d27fb3f9c96e6c665506ea7ba26ab89f0c89606f678ae4a2",
      "signerHash": "006276223396f7510653e20f0d10cd1a5d97176e",
      "size": 740544
    }
  ]
}
```

#### Get Installed Software

This action is used to retrieves a collection of installed software related to a given machine IP address, hostname, or
 machine ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname, or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|software|[]software|True|List of installed software on the machine|[{"publicExploit": True, "vendor": "microsoft", "weaknesses": 1056, "activeAlert": False, "exposedMachines": 1, "id": "microsoft-_-windows_10", "impactScore": 63.8, "name": "windows_10"}, {"exposedMachines": 0, "id": "microsoft-_-edge_chromium-based", "impactScore": 0, "name": "edge_chromium-based", "publicExploit": False, "vendor": "microsoft", "weaknesses": 0, "activeAlert": False}]|
  
Example output:

```
{
  "software": [
    {
      "activeAlert": false,
      "exposedMachines": 1,
      "id": "microsoft-_-windows_10",
      "impactScore": 63.8,
      "name": "windows_10",
      "publicExploit": true,
      "vendor": "microsoft",
      "weaknesses": 1056
    },
    {
      "activeAlert": false,
      "exposedMachines": 0,
      "id": "microsoft-_-edge_chromium-based",
      "impactScore": 0,
      "name": "edge_chromium-based",
      "publicExploit": false,
      "vendor": "microsoft",
      "weaknesses": 0
    }
  ]
}
```

#### Get Machine Action

This action is used to retrieve details about an action taken on a machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action_id|string|None|True|Action ID|None|ffd1f0cb-68ad-44ea-bf90-d01061b965ec|None|None|
  
Example input:

```
{
  "action_id": "ffd1f0cb-68ad-44ea-bf90-d01061b965ec"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine_action_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|{'@odata.context': 'https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity', 'id': '2e9da30d-27f6-4208-81f2-9cd3d67893ba', 'type': 'RunAntiVirusScan', 'requestor': 'user@example.com', 'requestorComment': 'Check machine for viruses due to alert 3212', 'status': 'InProgress', 'machineId': '1e5bc9d7e413ddd7902c2932e418702b84d0cc07', 'creationDateTimeUtc': '2018-12-04T12:18:27.1293487Z', 'lastUpdateTimeUtc': '2018-12-04T12:18:27.1293487Z', 'relatedFileInfo': None}|
  
Example output:

```
{
  "machine_action_response": {
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
    "creationDateTimeUtc": "2018-12-04T12:18:27.1293487Z",
    "id": "2e9da30d-27f6-4208-81f2-9cd3d67893ba",
    "lastUpdateTimeUtc": "2018-12-04T12:18:27.1293487Z",
    "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
    "relatedFileInfo": null,
    "requestor": "user@example.com",
    "requestorComment": "Check machine for viruses due to alert 3212",
    "status": "InProgress",
    "type": "RunAntiVirusScan"
  }
}
```

#### Get Machine Information

This action is used to get details about a machine with its ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine|machine|True|Machine information|{'@odata.context': 'https://api.securitycenter.windows.com/api/$metadata#Machines/$entity', 'id': '2df36d707c1ee5084cef77f3dbfc95db65bc4a73', 'computerDnsName': 'desktop-qo15on7', 'firstSeen': '2020-06-26T19:54:48.0962745Z', 'lastSeen': '2020-07-02T18:34:23.1871866Z', 'osPlatform': 'Windows10', 'osProcessor': 'x64', 'version': '2004', 'lastIpAddress': '198.51.100.100', 'lastExternalIpAddress': '198.51.100.100', 'agentVersion': '10.7150.19041.153', 'osBuild': 19041, 'healthStatus': 'Active', 'rbacGroupId': 0, 'riskScore': 'Medium', 'exposureLevel': 'Low', 'machineTags': []}|
  
Example output:

```
{
  "machine": {
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Machines/$entity",
    "agentVersion": "10.7150.19041.153",
    "computerDnsName": "desktop-qo15on7",
    "exposureLevel": "Low",
    "firstSeen": "2020-06-26T19:54:48.0962745Z",
    "healthStatus": "Active",
    "id": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
    "lastExternalIpAddress": "198.51.100.100",
    "lastIpAddress": "198.51.100.100",
    "lastSeen": "2020-07-02T18:34:23.1871866Z",
    "machineTags": [],
    "osBuild": 19041,
    "osPlatform": "Windows10",
    "osProcessor": "x64",
    "rbacGroupId": 0,
    "riskScore": "Medium",
    "version": "2004"
  }
}
```

#### Get Machine Vulnerabilities

This action is used to retrieves a collection of discovered vulnerabilities related to a given device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname or machine ID|None|9de5069c5afe602b2ea0a04b66beb2c0cef77fdf|None|None|
  
Example input:

```
{
  "machine": "9de5069c5afe602b2ea0a04b66beb2c0cef77fdf"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerabilities|[]vulnerability|True|List of vulnerabilities of the machine|[{"id": "CVE-2020-14711", "name": "CVE-2020-14711", "description": "Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).  Supported versions that are affected are Prior to 5.2.44, prior to 6.0.24 and  prior to 6.1.12. Easily exploitable vulnerability allows high privileged attacker with logon to the infrastructure where Oracle VM VirtualBox executes to compromise Oracle VM VirtualBox.  Successful attacks require human interaction from a person other than the attacker. Successful attacks of this vulnerability can result in takeover of Oracle VM VirtualBox.  Note: The CVE-2020-14711 is applicable to macOS host only. CVSS 3.1 Base Score 6.5 (Confidentiality, Integrity and Availability impacts).  CVSS Vector: (CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H).", "severity": "Medium", "cvssV3": 6.5, "exposedMachines": 1, "publishedOn": "2020-07-14T00:00:00Z", "updatedOn": "2020-07-27T22:00:00Z", "publicExploit": False, "exploitVerified": False, "exploitInKit": False, "exploitTypes": [], "exploitUris": []}]|
  
Example output:

```
{
  "vulnerabilities": [
    {
      "cvssV3": 6.5,
      "description": "Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).  Supported versions that are affected are Prior to 5.2.44, prior to 6.0.24 and  prior to 6.1.12. Easily exploitable vulnerability allows high privileged attacker with logon to the infrastructure where Oracle VM VirtualBox executes to compromise Oracle VM VirtualBox.  Successful attacks require human interaction from a person other than the attacker. Successful attacks of this vulnerability can result in takeover of Oracle VM VirtualBox.  Note: The CVE-2020-14711 is applicable to macOS host only. CVSS 3.1 Base Score 6.5 (Confidentiality, Integrity and Availability impacts).  CVSS Vector: (CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H).",
      "exploitInKit": false,
      "exploitTypes": [],
      "exploitUris": [],
      "exploitVerified": false,
      "exposedMachines": 1,
      "id": "CVE-2020-14711",
      "name": "CVE-2020-14711",
      "publicExploit": false,
      "publishedOn": "2020-07-14T00:00:00Z",
      "severity": "Medium",
      "updatedOn": "2020-07-27T22:00:00Z"
    }
  ]
}
```

#### Get Missing Software Updates

This action is used to retrieve a list of software updates

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|updates|[]update|True|List of updates|[{"machineMissedOn": 1, "name": "September 2020 Security Updates", "osBuild": 17763, "productsNames": ["windows_10", "internet_explorer"], "url": "https://catalog.update.microsoft.com/v7/site/Searc...", "cveAddressed": 68, "id": "4570333"}]|
  
Example output:

```
{
  "updates": [
    {
      "cveAddressed": 68,
      "id": "4570333",
      "machineMissedOn": 1,
      "name": "September 2020 Security Updates",
      "osBuild": 17763,
      "productsNames": [
        "windows_10",
        "internet_explorer"
      ],
      "url": "https://catalog.update.microsoft.com/v7/site/Searc..."
    }
  ]
}
```

#### Get Related Machines

This action is used to get machines related to an file hash(SHA1), domain or username indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|indicator|string|None|True|File hash(SHA1), domain or username indicator|None|example.com|None|None|
  
Example input:

```
{
  "indicator": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machines|[]machine|True|Machines related to an file hash(SHA1), domain or username indicator|[{"exposureLevel": "Medium", "lastIpAddress": "10.0.2.15", "machineTags": ["tag1", "tag2"], "agentVersion": "10.5850.17763.348", "lastSeen": "2020-12-08T10:37:41.2907723Z", "osBuild": 17763, "osPlatform": "Windows10", "rbacGroupId": 0, "computerDnsName": "msedgewin10", "firstSeen": "2020-12-08T09:33:03.1262943Z", "osProcessor": "x64", "version": "1809", "deviceValue": "Normal", "healthStatus": "Active", "id": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73", "isAadJoined": False, "lastExternalIpAddress": "83.220.117.67", "riskScore": "None"}]|
  
Example output:

```
{
  "machines": [
    {
      "agentVersion": "10.5850.17763.348",
      "computerDnsName": "msedgewin10",
      "deviceValue": "Normal",
      "exposureLevel": "Medium",
      "firstSeen": "2020-12-08T09:33:03.1262943Z",
      "healthStatus": "Active",
      "id": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
      "isAadJoined": false,
      "lastExternalIpAddress": "83.220.117.67",
      "lastIpAddress": "10.0.2.15",
      "lastSeen": "2020-12-08T10:37:41.2907723Z",
      "machineTags": [
        "tag1",
        "tag2"
      ],
      "osBuild": 17763,
      "osPlatform": "Windows10",
      "osProcessor": "x64",
      "rbacGroupId": 0,
      "riskScore": "None",
      "version": "1809"
    }
  ]
}
```

#### Get Security Recommendations

This action is used to retrieve a list of security recommendations

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|recommendations|[]recommendation|True|List of security recommendations|[{"activeAlert": False, "associatedThreats": [], "configScoreImpact": 0.0, "exposedMachinesCount": 1, "exposureImpact": 0.0, "id": "va-_-microsoft-_-.net_framework", "nonProductivityImpactedAssets": 0, "productName": ".net_framework", "publicExploit": False, "recommendationCategory": "Application", "recommendationName": "Update Microsoft .net Framework", "relatedComponent": ".net Framework", "remediationType": "Update", "severityScore": 0.0, "status": "Active", "totalMachineCount": 0, "vendor": "microsoft", "weaknesses": 1}]|
  
Example output:

```
{
  "recommendations": [
    {
      "activeAlert": false,
      "associatedThreats": [],
      "configScoreImpact": 0.0,
      "exposedMachinesCount": 1,
      "exposureImpact": 0.0,
      "id": "va-_-microsoft-_-.net_framework",
      "nonProductivityImpactedAssets": 0,
      "productName": ".net_framework",
      "publicExploit": false,
      "recommendationCategory": "Application",
      "recommendationName": "Update Microsoft .net Framework",
      "relatedComponent": ".net Framework",
      "remediationType": "Update",
      "severityScore": 0.0,
      "status": "Active",
      "totalMachineCount": 0,
      "vendor": "microsoft",
      "weaknesses": 1
    }
  ]
}
```

#### Isolate Machine

This action is used to isolate a machine from the network

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment to associate with the isolation action|None|Isolated by InsightConnect|None|None|
|isolation_type|string|None|True|Type of isolation to perform on target machine|["Full", "Selective"]|Full|None|None|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
  
Example input:

```
{
  "comment": "Isolated by InsightConnect",
  "isolation_type": "Full",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine_isolation_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|{'@odata.context': 'https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity', 'id': 'b89eb834-4578-496c-8be0-03f004061435', 'type': 'Isolate', 'requestor': 'user@example.com', 'requestorComment': 'Isolate machine due to alert 1234', 'status': 'InProgress', 'machineId': '1e5bc9d7e413ddd7902c2932e418702b84d0cc07', 'creationDateTimeUtc': '2017-12-04T12:12:18.9725659Z', 'lastUpdateTimeUtc': '2017-12-04T12:12:18.9725659Z', 'relatedFileInfo': None}|
  
Example output:

```
{
  "machine_isolation_response": {
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
    "creationDateTimeUtc": "2017-12-04T12:12:18.9725659Z",
    "id": "b89eb834-4578-496c-8be0-03f004061435",
    "lastUpdateTimeUtc": "2017-12-04T12:12:18.9725659Z",
    "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
    "relatedFileInfo": null,
    "requestor": "user@example.com",
    "requestorComment": "Isolate machine due to alert 1234",
    "status": "InProgress",
    "type": "Isolate"
  }
}
```

#### Manage Tags

This action is used to add or remove machine tags

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname, or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
|tag|string|None|True|The tag value|None|example tag|None|None|
|type|boolean|True|True|True to add tag, false to remove it|None|True|None|None|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
  "tag": "example tag",
  "type": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|manage_tags_response|manage_tags_response|True|A response that includes updated tags and supplemental information about the machine|{'computerDnsName': 'msedgewin10', 'deviceValue': 'Normal', 'machineTags': ['tag1', 'tag2', 'example tag'], 'riskScore': 'None', '@odata.context': 'https://api.securitycenter.windows.com/api/$metada...', 'id': '2df36d707c1ee5084cef77f3dbfc95db65bc4a73', 'osProcessor': 'x64', 'rbacGroupId': 0, 'version': '1809', 'osPlatform': 'Windows10', 'agentVersion': '10.5850.17763.348', 'exposureLevel': 'Medium', 'isAadJoined': False, 'lastExternalIpAddress': '83.220.117.67', 'lastIpAddress': '10.0.2.15', 'osBuild': 17763, 'firstSeen': '2020-12-08T09:33:03.1262943Z', 'healthStatus': 'Active', 'lastSeen': '2020-12-08T10:37:41.2907723Z'}|
  
Example output:

```
{
  "manage_tags_response": {
    "@odata.context": "https://api.securitycenter.windows.com/api/$metada...",
    "agentVersion": "10.5850.17763.348",
    "computerDnsName": "msedgewin10",
    "deviceValue": "Normal",
    "exposureLevel": "Medium",
    "firstSeen": "2020-12-08T09:33:03.1262943Z",
    "healthStatus": "Active",
    "id": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
    "isAadJoined": false,
    "lastExternalIpAddress": "83.220.117.67",
    "lastIpAddress": "10.0.2.15",
    "lastSeen": "2020-12-08T10:37:41.2907723Z",
    "machineTags": [
      "tag1",
      "tag2",
      "example tag"
    ],
    "osBuild": 17763,
    "osPlatform": "Windows10",
    "osProcessor": "x64",
    "rbacGroupId": 0,
    "riskScore": "None",
    "version": "1809"
  }
}
```

#### Run Antivirus Scan

This action is used to initiate a Windows Defender Antivirus scan on a machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment to associate with the antivirus scan action|None|InsightConnect has started an antivirus scan.|None|None|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
|scan_type|string|None|True|The type of antivirus scan to run|["Full", "Quick"]|Full|None|None|
  
Example input:

```
{
  "comment": "InsightConnect has started an antivirus scan.",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
  "scan_type": "Full"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine_action_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|{'@odata.context': 'https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity', 'id': '2e9da30d-27f6-4208-81f2-9cd3d67893ba', 'type': 'RunAntiVirusScan', 'requestor': 'user@example.com', 'requestorComment': 'Check machine for viruses due to alert 3212', 'status': 'InProgress', 'machineId': '1e5bc9d7e413ddd7902c2932e418702b84d0cc07', 'creationDateTimeUtc': '2018-12-04T12:18:27.1293487Z', 'lastUpdateTimeUtc': '2018-12-04T12:18:27.1293487Z', 'relatedFileInfo': None}|
  
Example output:

```
{
  "machine_action_response": {
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
    "creationDateTimeUtc": "2018-12-04T12:18:27.1293487Z",
    "id": "2e9da30d-27f6-4208-81f2-9cd3d67893ba",
    "lastUpdateTimeUtc": "2018-12-04T12:18:27.1293487Z",
    "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
    "relatedFileInfo": null,
    "requestor": "user@example.com",
    "requestorComment": "Check machine for viruses due to alert 3212",
    "status": "InProgress",
    "type": "RunAntiVirusScan"
  }
}
```

#### Stop and Quarantine File

This action is used to stop the execution of a file on a machine and delete it

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment to associate with the stop and quarantine action|None|InsightConnect has stopped a file.|None|None|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
|sha1|string|None|True|SHA1 hash of the file to stop and quarantine on the machine|None|ad0c0f2fa80411788e81a4567d1d8758b83cd76e|None|None|
  
Example input:

```
{
  "comment": "InsightConnect has stopped a file.",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
  "sha1": "ad0c0f2fa80411788e81a4567d1d8758b83cd76e"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|stop_and_quarantine_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|{'@odata.context': 'https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity', 'id': '141408d1-384c-4c19-8b57-ba39e378011a', 'type': 'StopAndQuarantineFile', 'requestor': 'user@example.com', 'requestorComment': 'Stop and quarantine file on machine due to alert 441688558380765161_2136280442', 'status': 'InProgress', 'machineId': '1e5bc9d7e413ddd7902c2932e418702b84d0cc07', 'creationDateTimeUtc': '2018-12-04T12:15:04.3825985Z', 'lastUpdateTimeUtc': '2018-12-04T12:15:04.3825985Z', 'relatedFileInfo': {'fileIdentifier': '87662bc3d60e4200ceaf7aae249d1c343f4b83c9', 'fileIdentifierType': 'Sha1'}}|
  
Example output:

```
{
  "stop_and_quarantine_response": {
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
    "creationDateTimeUtc": "2018-12-04T12:15:04.3825985Z",
    "id": "141408d1-384c-4c19-8b57-ba39e378011a",
    "lastUpdateTimeUtc": "2018-12-04T12:15:04.3825985Z",
    "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
    "relatedFileInfo": {
      "fileIdentifier": "87662bc3d60e4200ceaf7aae249d1c343f4b83c9",
      "fileIdentifierType": "Sha1"
    },
    "requestor": "user@example.com",
    "requestorComment": "Stop and quarantine file on machine due to alert 441688558380765161_2136280442",
    "status": "InProgress",
    "type": "StopAndQuarantineFile"
  }
}
```

#### Unisolate Machine

This action is used to restore network connectivity to a machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment to associate with the unisolate action|None|Unisolated by InsightConnect|None|None|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|None|None|
  
Example input:

```
{
  "comment": "Unisolated by InsightConnect",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine_isolation_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|{'@odata.context': 'https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity', 'id': 'b89eb834-4578-496c-8be0-03f004061435', 'type': 'Unisolate', 'requestor': 'user@example.com', 'requestorComment': 'Isolate machine due to alert 1234', 'status': 'InProgress', 'machineId': '1e5bc9d7e413ddd7902c2932e418702b84d0cc07', 'creationDateTimeUtc': '2017-12-04T12:12:18.9725659Z', 'lastUpdateTimeUtc': '2017-12-04T12:12:18.9725659Z', 'relatedFileInfo': None}|
  
Example output:

```
{
  "machine_isolation_response": {
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
    "creationDateTimeUtc": "2017-12-04T12:12:18.9725659Z",
    "id": "b89eb834-4578-496c-8be0-03f004061435",
    "lastUpdateTimeUtc": "2017-12-04T12:12:18.9725659Z",
    "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
    "relatedFileInfo": null,
    "requestor": "user@example.com",
    "requestorComment": "Isolate machine due to alert 1234",
    "status": "InProgress",
    "type": "Unisolate"
  }
}
```

#### Update Alert

This action is used to updates properties of existing alert

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_fields|object|None|True|Fields of the alert to update|None|{'status': 'Resolved', 'assignedTo': 'user@example.com', 'classification': 'FalsePositive', 'determination': 'Malware', 'comment': 'Resolve my alert and assign to secop2'}|None|None|
|alert_id|string|None|True|ID of alert to update|None|1216885583807651612136280442|None|None|
  
Example input:

```
{
  "alert_fields": {
    "assignedTo": "user@example.com",
    "classification": "FalsePositive",
    "comment": "Resolve my alert and assign to secop2",
    "determination": "Malware",
    "status": "Resolved"
  },
  "alert_id": 1216885583807651612136280442
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|Alert|True|Alert entity with the updated properties|{'id': 'da637292082891366787_322129023', 'incidentId': 1, 'investigationId': 1, 'assignedTo': 'Automation', 'severity': 'Informational', 'status': 'Resolved', 'investigationState': 'Benign', 'detectionSource': 'WindowsDefenderAv', 'category': 'Malware', 'title': 'EICAR_Test_File malware was detected', 'description': 'Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks. This detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.', 'alertCreationTime': '2020-07-01T13:51:29.0741799Z', 'firstEventTime': '2020-07-01T13:49:55.2853766Z', 'lastEventTime': '2020-07-01T13:49:55.8520351Z', 'lastUpdateTime': '2020-07-02T20:11:23.0966667Z', 'resolvedTime': '2020-07-01T14:02:24.4812386Z', 'machineId': '2df36d707c1ee508xyFf77f3dbfc95db65bc4a73', 'computerDnsName': 'example-desktop', 'aadTenantId': '5c824599-ab2c-43ab-651x-3b886d4f8f10', 'comments': [], 'evidence': []}|
  
Example output:

```
{
  "alert": {
    "aadTenantId": "5c824599-ab2c-43ab-651x-3b886d4f8f10",
    "alertCreationTime": "2020-07-01T13:51:29.0741799Z",
    "assignedTo": "Automation",
    "category": "Malware",
    "comments": [],
    "computerDnsName": "example-desktop",
    "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks. This detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
    "detectionSource": "WindowsDefenderAv",
    "evidence": [],
    "firstEventTime": "2020-07-01T13:49:55.2853766Z",
    "id": "da637292082891366787_322129023",
    "incidentId": 1,
    "investigationId": 1,
    "investigationState": "Benign",
    "lastEventTime": "2020-07-01T13:49:55.8520351Z",
    "lastUpdateTime": "2020-07-02T20:11:23.0966667Z",
    "machineId": "2df36d707c1ee508xyFf77f3dbfc95db65bc4a73",
    "resolvedTime": "2020-07-01T14:02:24.4812386Z",
    "severity": "Informational",
    "status": "Resolved",
    "title": "EICAR_Test_File malware was detected"
  }
}
```
### Triggers


#### Get Alerts Matching Key

This trigger is used to get alerts that match a given key to its value

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|10|False|Poll frequency in seconds|None|10|None|None|
|key|string|None|True|The key to look for in the alert. This key must match the case shown in the example output section in help|None|assignedTo|None|None|
|value|string|None|True|The value to look for in the alert. The value must match the case of the value returned|None|user@example.com|None|None|
  
Example input:

```
{
  "frequency": 10,
  "key": "assignedTo",
  "value": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert|True|An alert that contains the given key and matching value|{'alert': {'id': 'da637292082891366787_322129023', 'incidentId': 1, 'investigationId': 1, 'assignedTo': 'Automation', 'severity': 'Informational', 'status': 'Resolved', 'investigationState': 'Benign', 'detectionSource': 'WindowsDefenderAv', 'category': 'Malware', 'title': 'EICAR_Test_File malware was detected', 'description': 'Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.', 'alertCreationTime': '2020-07-01T13:51:29.0741799Z', 'firstEventTime': '2020-07-01T13:49:55.2853766Z', 'lastEventTime': '2020-07-01T13:49:55.8520351Z', 'lastUpdateTime': '2020-07-02T20:11:23.0966667Z', 'resolvedTime': '2020-07-01T14:02:24.4812386Z', 'machineId': '2df36d707c1ee508xyFf77f3dbfc95db65bc4a73', 'computerDnsName': 'example-desktop', 'aadTenantId': '5c824599-ab2c-43ab-651x-3b886d4f8f10', 'comments': [], 'evidence': [{'entityType': 'User', 'evidenceCreationTime': '2021-01-26T20:33:58.42Z', 'sha1': 'ff836cfb1af40252bd2a2ea843032e99a5b262ed', 'sha256': 'a4752c71d81afd3d5865d24ddb11a6b0c615062fcc448d24050c2172d2cbccd6', 'fileName': 'rundll32.exe', 'filePath': 'C:\\Windows\\SysWOW64', 'processId': 3276, 'processCommandLine': 'rundll32.exe  c:\\temp\\suspicious.dll,RepeatAfterMe', 'processCreationTime': '2021-01-26T20:31:32.9581596Z', 'parentProcessId': 8420, 'parentProcessCreationTime': '2021-01-26T20:31:32.9004163Z', 'parentProcessFileName': 'rundll32.exe', 'parentProcessFilePath': 'C:\\Windows\\System32', 'ipAddress': '8.8.8.8', 'url': None, 'registryKey': 'Test9999', 'registryHive': None, 'registryValueType': None, 'registryValue': None, 'accountName': 'name', 'domainName': 'DOMAIN', 'userSid': 'S-1-5-21-11111607-1111760036-109187956-75141', 'aadUserId': '11118379-2a59-1111-ac3c-a51eb4a3c627', 'userPrincipalName': 'user@example.com', 'detectionStatus': 'Detected'}]}}|
  
Example output:

```
{
  "alert": {
    "alert": {
      "aadTenantId": "5c824599-ab2c-43ab-651x-3b886d4f8f10",
      "alertCreationTime": "2020-07-01T13:51:29.0741799Z",
      "assignedTo": "Automation",
      "category": "Malware",
      "comments": [],
      "computerDnsName": "example-desktop",
      "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
      "detectionSource": "WindowsDefenderAv",
      "evidence": [
        {
          "aadUserId": "11118379-2a59-1111-ac3c-a51eb4a3c627",
          "accountName": "name",
          "detectionStatus": "Detected",
          "domainName": "DOMAIN",
          "entityType": "User",
          "evidenceCreationTime": "2021-01-26T20:33:58.42Z",
          "fileName": "rundll32.exe",
          "filePath": "C:\\Windows\\SysWOW64",
          "ipAddress": "8.8.8.8",
          "parentProcessCreationTime": "2021-01-26T20:31:32.9004163Z",
          "parentProcessFileName": "rundll32.exe",
          "parentProcessFilePath": "C:\\Windows\\System32",
          "parentProcessId": 8420,
          "processCommandLine": "rundll32.exe  c:\\temp\\suspicious.dll,RepeatAfterMe",
          "processCreationTime": "2021-01-26T20:31:32.9581596Z",
          "processId": 3276,
          "registryHive": null,
          "registryKey": "Test9999",
          "registryValue": null,
          "registryValueType": null,
          "sha1": "ff836cfb1af40252bd2a2ea843032e99a5b262ed",
          "sha256": "a4752c71d81afd3d5865d24ddb11a6b0c615062fcc448d24050c2172d2cbccd6",
          "url": null,
          "userPrincipalName": "user@example.com",
          "userSid": "S-1-5-21-11111607-1111760036-109187956-75141"
        }
      ],
      "firstEventTime": "2020-07-01T13:49:55.2853766Z",
      "id": "da637292082891366787_322129023",
      "incidentId": 1,
      "investigationId": 1,
      "investigationState": "Benign",
      "lastEventTime": "2020-07-01T13:49:55.8520351Z",
      "lastUpdateTime": "2020-07-02T20:11:23.0966667Z",
      "machineId": "2df36d707c1ee508xyFf77f3dbfc95db65bc4a73",
      "resolvedTime": "2020-07-01T14:02:24.4812386Z",
      "severity": "Informational",
      "status": "Resolved",
      "title": "EICAR_Test_File malware was detected"
    }
  }
}
```

#### Get Alerts

This trigger is used to return all new alerts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|10|False|Poll frequency in seconds|None|10|None|None|
  
Example input:

```
{
  "frequency": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert|True|Alert|{'id': 'da637292082891366787_322129023', 'incidentId': 1, 'investigationId': 1, 'assignedTo': 'Automation', 'severity': 'Informational', 'status': 'Resolved', 'investigationState': 'Benign', 'detectionSource': 'WindowsDefenderAv', 'category': 'Malware', 'title': 'EICAR_Test_File malware was detected', 'description': 'Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks. This detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.', 'alertCreationTime': '2020-07-01T13:51:29.0741799Z', 'firstEventTime': '2020-07-01T13:49:55.2853766Z', 'lastEventTime': '2020-07-01T13:49:55.8520351Z', 'lastUpdateTime': '2020-07-02T20:11:23.0966667Z', 'resolvedTime': '2020-07-01T14:02:24.4812386Z', 'machineId': '2df36d707c1ee508xyFf77f3dbfc95db65bc4a73', 'computerDnsName': 'example-desktop', 'aadTenantId': '5c824599-ab2c-43ab-651x-3b886d4f8f10', 'comments': [], 'evidence': []}|
  
Example output:

```
{
  "alert": {
    "aadTenantId": "5c824599-ab2c-43ab-651x-3b886d4f8f10",
    "alertCreationTime": "2020-07-01T13:51:29.0741799Z",
    "assignedTo": "Automation",
    "category": "Malware",
    "comments": [],
    "computerDnsName": "example-desktop",
    "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks. This detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
    "detectionSource": "WindowsDefenderAv",
    "evidence": [],
    "firstEventTime": "2020-07-01T13:49:55.2853766Z",
    "id": "da637292082891366787_322129023",
    "incidentId": 1,
    "investigationId": 1,
    "investigationState": "Benign",
    "lastEventTime": "2020-07-01T13:49:55.8520351Z",
    "lastUpdateTime": "2020-07-02T20:11:23.0966667Z",
    "machineId": "2df36d707c1ee508xyFf77f3dbfc95db65bc4a73",
    "resolvedTime": "2020-07-01T14:02:24.4812386Z",
    "severity": "Informational",
    "status": "Resolved",
    "title": "EICAR_Test_File malware was detected"
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**manage_tags_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|@Odata.Context|string|None|False|@odata.context|None|
|Agent Version|string|None|False|Agent version|None|
|Computer DNS Name|string|None|False|Computer DNS name|None|
|Device Value|string|None|False|Device value|None|
|Exposure Level|string|None|False|Exposure level|None|
|First Seen|string|None|False|First seen|None|
|Health Status|string|None|False|Health status|None|
|ID|string|None|False|ID|None|
|Is AAD Joined|boolean|None|False|Is AAD joined|None|
|Last External IP Address|string|None|False|Last external IP address|None|
|Last IP Address|string|None|False|Last IP address|None|
|Last Seen|string|None|False|Last seen|None|
|Machine Tags|[]string|None|False|Machine tags|None|
|OS Build|integer|None|False|OS build|None|
|OS Platform|string|None|False|OS platform|None|
|OS Processor|string|None|False|OS Processor|None|
|RBAC Group ID|integer|None|False|RBAC group ID|None|
|Risk Score|string|None|False|Risk score|None|
|Version|string|None|False|Version|None|
  
**software**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active Alert|boolean|None|False|Active alert|None|
|Exposed Machines|integer|None|False|Exposed machines|None|
|ID|string|None|False|ID|None|
|Impact Score|float|None|False|Impact score|None|
|Name|string|None|False|Name|None|
|Public Exploit|boolean|None|False|Public exploit|None|
|Vendor|string|None|False|Vendor|None|
|Weaknesses|integer|None|False|Weaknesses|None|
  
**related_user_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Domain Name|string|None|False|Domain name|None|
|User Name|string|None|False|User name|None|
  
**evidence**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AAD User ID|string|None|False|Azure Active Directory User ID|None|
|Account Name|string|None|False|Account Name|None|
|Detection Status|string|None|False|Detection Status|None|
|Domain Name|string|None|False|Domain Name|None|
|Entity Type|string|None|False|Type of evidence|None|
|Evidence Creation Time|string|None|False|Creation time of evidence in ISO 8601 format|None|
|File Name|string|None|False|File Name|None|
|File Path|string|None|False|File Path|None|
|IP Address|string|None|False|IP Address|None|
|Parent Process Creation Time|string|None|False|Parent Process Creation Time in ISO 8601 format|None|
|Parent Process File Name|string|None|False|Parent Process File Name|None|
|Parent Process File Path|string|None|False|Parent Process File Path|None|
|Parent Process ID|integer|None|False|Parent process ID|None|
|Process Command Line|string|None|False|Process Command Line|None|
|Process Creation Time|string|None|False|Process Creation Time in ISO 8601 format|None|
|Process ID|integer|None|False|Process ID|None|
|Registry Hive|string|None|False|Registry Hive|None|
|Registry Key|string|None|False|A key-level node in the Windows registry|None|
|Registry Value|string|None|False|Registry Value|None|
|Registry Value Type|string|None|False|Registry Value Type|None|
|SHA1|string|None|False|SHA1 hash|None|
|SHA256|string|None|False|SHA256 hash|None|
|URL|string|None|False|URL|None|
|User Principal Name|string|None|False|User Principal Name|None|
|User SID|string|None|False|User Secrurity ID|None|
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AAD Tenant ID|string|None|False|AAD tenant ID|None|
|Alert Creation Time|string|None|False|Alert creation time|None|
|Assigned To|string|None|False|Assigned To|None|
|Category|string|None|False|Category|None|
|Classification|string|None|False|Classification|None|
|Computer DNS Name|string|None|False|Computer DNS name|None|
|Description|string|None|False|Description|None|
|Detection Source|string|None|False|Detection source|None|
|Determination|string|None|False|Determination|None|
|Evidence|[]evidence|None|False|List of related alert evidence|None|
|First Event Time|string|None|False|First event time|None|
|ID|string|None|False|ID|None|
|Incident ID|integer|None|False|Incident ID|None|
|Investigation ID|integer|None|False|Investigation ID|None|
|Investigation State|string|None|False|Investigation state|None|
|Last Event Time|string|None|False|Last event time|None|
|Last Update Time|string|None|False|Last update time|None|
|Machine ID|string|None|False|Machine ID|None|
|RBAC Group Name|string|None|False|RBAC group name|None|
|Related User|related_user_object|None|False|Related user|None|
|Resolved Time|string|None|False|Resolved time|None|
|Severity|string|None|False|Severity|None|
|Status|string|None|False|Status|None|
|Threat Family Name|string|None|False|Threat family name|None|
|Title|string|None|False|Title|None|
  
**file_type**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Determination Type|string|None|False|Determination type|None|
|Determination Value|string|None|False|Determination value|None|
|File Product Name|string|None|False|File product name|None|
|File Publisher|string|None|False|File publisher|None|
|File Type|string|None|False|File type|None|
|Global First Observed|string|None|False|Global first observed|None|
|Global Last Observed|string|None|False|Global last observed|None|
|Global Prevalence|integer|None|False|Global prevalence|None|
|Is PE File|boolean|None|False|Is PE File|None|
|Is Valid Certificate|boolean|None|False|Is valid certificate|None|
|Issuer|string|None|False|Issuer|None|
|MD5|string|None|False|MD5|None|
|SHA1|string|None|False|SHA1|None|
|SHA256|string|None|False|SHA256|None|
|Signer|string|None|False|Signer|None|
|Signer Hash|string|None|False|Signer hash|None|
|Size|integer|None|False|Size|None|
  
**machine_software**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Computer DNS Name|string|None|False|Computer DNS name|None|
|ID|string|None|False|ID|None|
|OS Platform|string|None|False|OS platform|None|
|RBAC Group ID|number|None|False|RBAC group ID|None|
|RBAC Group Name|string|None|False|RBAC group name|None|
  
**machine**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Version|string|None|False|Agent version|None|
|Computer DNS Name|string|None|False|Computer DNS name|None|
|Exposure Level|string|None|False|Exposure level|None|
|First Seen|string|None|False|First seen|None|
|Health Status|string|None|False|Health status|None|
|ID|string|None|False|ID|None|
|Last External IP Address|string|None|False|Last external IP address|None|
|Last IP Address|string|None|False|Last IP address|None|
|Last Seen|string|None|False|Last seen|None|
|Machine Tags|[]string|None|False|Machine Tags|None|
|OS Build|integer|None|False|OS build|None|
|OS Platform|string|None|False|OS platform|None|
|OS Processor|string|None|False|OS processor|None|
|RBAC Group ID|integer|None|False|RBAC group ID|None|
|Risk Score|string|None|False|Risk score|None|
|Version|string|None|False|Version|None|
  
**machine_action**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Creation Date Time UTC|string|None|False|Creation date time UTC|None|
|Error HResult|integer|None|False|Error HResult|None|
|ID|string|None|False|ID|None|
|Last Update Date Time UTC|string|None|False|Last update date time UTC|None|
|Machine ID|string|None|False|Machine ID|None|
|Requestor|string|None|False|Requestor|None|
|Requestor Comment|string|None|False|Requestor comment|None|
|Status|string|None|False|Status|None|
  
**indicator_action**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|@Odata.Context|string|None|False|@odata.context|None|
|Action|string|None|False|The action that will be taken if the indicator will be discovered in the organization|AlertAndBlock|
|Application|string|None|False|The application associated with the indicator|demo-test|
|Created By|string|None|False|Unique identity of the user/application that submitted the indicator|test|
|Created By Display Name|string|None|False|Created by display name|None|
|Created By Source|string|None|False|Created by source|None|
|Creation Time|string|None|False|The date and time when the indicator was created|None|
|Description|string|None|False|Description of the indicator|None|
|Expiration Time|string|None|False|The expiration time of the indicator|None|
|Generate Alert|boolean|None|False|Generate alert|None|
|Historical Detection|boolean|None|False|Historical detection|None|
|Indicator ID|string|None|False|Identity of the indicator entity|None|
|Indicator Type|string|None|False|Type of the indicator|Url|
|Indicator Value|string|None|False|The potentially malicious indicator of one of the following types: IP addresses, URLs, domains, and SHA1 and SHA256 hashes|None|
|Last Update Time|string|None|False|The last time the indicator was updated|None|
|Last Updated By|string|None|False|Identity of the user/application that last updated the indicator|82f42fca-e931-4f03-b54c-47af94bd394d|
|MITRE Techniques|[]string|None|False|MITRE techniques|None|
|RBAC Group IDs|[]string|None|False|RBAC group IDs|None|
|RBAC Group Names|[]string|None|False|RBAC device group names where the indicator is exposed and active. Empty list in case it exposed to all devices|None|
|Recommended Actions|string|None|False|Recommended actions for the indicator|None|
|Severity|string|None|False|The severity of the indicator|None|
|Source|string|None|False|The name of the user/application that submitted the indicator|test|
|Source Type|string|None|False|User in case the Indicator created by a user (e.g. from the portal), AadApp in case it submitted using automated application via the API.|AadApp|
|Title|string|None|False|Indicator alert title|None|
  
**vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVSS V3|float|None|False|CVSS v3|None|
|Description|string|None|False|Description|None|
|Exploit In Kit|boolean|None|False|Exploit in kit|None|
|Exploit Types|[]string|None|False|Exploit types|None|
|Exploit URIs|[]string|None|False|Exploit URIs|None|
|Exploit Verified|boolean|None|False|Exploit verified|None|
|Exposed Machines|integer|None|False|Exposed machines|None|
|ID|string|None|False|ID|None|
|Name|string|None|False|Name|None|
|Public Exploit|boolean|None|False|Public exploit|None|
|Published On|string|None|False|Published on|None|
|Severity|string|None|False|Severity|None|
|Updated On|string|None|False|Updated on|None|
  
**recommendation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active Alert|boolean|None|False|Active alert|None|
|Associated Threats|[]string|None|False|Associated threats|None|
|Config Score Impact|float|None|False|Config score impact|None|
|Exposed Machines Count|integer|None|False|Exposed machines count|None|
|Exposure Impact|float|None|False|Exposure impact|None|
|ID|string|None|False|ID|None|
|Non Productivity Impacted Assets|integer|None|False|Non productivity impacted assets|None|
|Product Name|string|None|False|Product name|None|
|Public Exploit|boolean|None|False|Public exploit|None|
|Recommendation Category|string|None|False|Recommendation category|None|
|Recommendation Name|string|None|False|Recommendation name|None|
|Related Component|string|None|False|Related component|None|
|Remediation Type|string|None|False|Remediation type|None|
|Severity Score|float|None|False|Severity score|None|
|Status|string|None|False|Status|None|
|Total Machine Count|integer|None|False|Total machine count|None|
|Vendor|string|None|False|Vendor|None|
|Weaknesses|integer|None|False|Weaknesses|None|
  
**update**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVE Addressed|integer|None|False|Update CVE addressed|None|
|ID|string|None|False|Update ID|None|
|Machine Missed On|integer|None|False|Update machine missed on|None|
|Name|string|None|False|Update name|None|
|OS Build|integer|None|False|Update OS build|None|
|Products Names|[]string|None|False|Update products names|None|
|URL|string|None|False|Update URL|None|


## Troubleshooting

* For information on how to setup your Azure application and assign permissions go [here](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/exposed-apis-create-app-webapp)

# Version History

* 6.0.4 - Updated SDK to the latest version (6.3.10)
* 6.0.3 - Updated SDK to the latest version (6.3.3)
* 6.0.2 - Updated SDK to the latest version (6.2.5)
* 6.0.1 - Update to latest SDK (v6.2.2) | Address vulnerabilities | Rebrand to `Microsoft Defender for Endpoint`
* 6.0.0 - Updated SDK to the latest version | Initial updates for fedramp compliance
* 5.2.0 - Add new action: Update Alert
* 5.1.0 - Adding the following as new action types to `blacklist` action ['Warn', 'Block', 'Audit'] | Add a new flag in the `blacklist` action to toggle generateAlerts flag | Bump SDK to version 5.4.9
* 5.0.0 - Updated the SDK version | Cloud enabled | fixed bug when machine_id is used for find_first_machine
* 4.8.1 - Fixed a problem where some actions could not find the machine
* 4.8.0 - Add Evidence output for Get Alerts trigger and Get Alert Matching Key trigger
* 4.7.1 - Fix bug in Get Alerts trigger which caused trigger to crash
* 4.7.0 - Add new action Collect Investigation Package
* 4.6.0 - Add new actions Get Installed Software, Get Related Machines and Manage Tags
* 4.5.1 - Add `docs_url` to plugin spec with link to [plugin setup guide](https://docs.rapid7.com/insightconnect/microsoft-defender-ATP)
* 4.5.0 - Add new action Get Missing Software Updates
* 4.4.1 - Add validation MD5 hash in Blacklist action | Set default value for Title, Expiration Time and Description input in action Blacklist
* 4.4.0 - Add new action Get Security Recommendations
* 4.3.0 - Add new action Get Machine Vulnerabilities
* 4.2.0 - Add new action Blacklist
* 4.1.0 - Add new action Find Machines with Installed Software
* 4.0.0 - Add custom type to output in action Get Machine Information
* 3.0.0 - Move connection functions to their own util class | Changed `Exception` to `PluginException` | Added error handling around "Action already in progress" state in Isolate Machine, Unisolate Machine, Stop and Quarantine File, and Run Antivirus Scan actions | Rename `machine_id` to `machine` in machine-related actions to support hostnames and IP addresses in addition to machine IDs.
* 2.0.0 - Update to refactor connection and actions
* 1.5.1 - New spec and help.md format for the Extension Library
* 1.5.0 - Fix issue where triggers always returned a blank payload
* 1.4.0 - New trigger Get Alerts | New action Get Machine Action
* 1.3.0 - New actions Stop and Quarantine File and Run Antivirus Scan
* 1.2.0 - New action Get File IDs from Alert
* 1.1.0 - New actions Get Machine ID from Alert, Isolate Machine, and Unisolate Machine
* 1.0.0 - Initial plugin

# Links

* [Windows Defender for Endpoint](https://www.microsoft.com/en-us/security/business/endpoint-security/microsoft-defender-endpoint)

## References

* [Windows Defender for Endpoint API Start Page](https://learn.microsoft.com/en-us/defender-endpoint/api/apis-intro)
* [Windows Defender for Endpoint API Endpoints](https://learn.microsoft.com/en-us/defender-endpoint/api/exposed-apis-list)