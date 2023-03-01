# Description

The [Windows Defender ATP](https://www.microsoft.com/en-us/windowsforbusiness/windows-atp) plugin allows preventative protection, post-breach detection, automated investigation, and response on Windows Defender Advanced Threat Protection enabled Office 365 instances.

This plugin utilizes the [Microsoft ATP API](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-atp/use-apis).

# Key Features

* Trigger workflows on new security alerts
* Manage isolation of network resources
* Start virus scans
* Stop execution of malicious code

# Requirements

* Windows Defender Advanced Threat Protection application credentials

# Supported Product Versions

* 2022-05-20

# Documentation

## Setup

This plugin uses the Windows Defender ATP API. It will use an Azure application to connect to the API and run actions from InsightConnect.

For information on how to setup your application and assign permissions go here:
https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/exposed-apis-create-app-webapp

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|application_id|string|None|True|Application (client) ID|None|a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d|
|application_secret|credential_secret_key|None|True|Application secret|None|kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=|
|directory_id|string|None|True|Directory (tenant) ID|None|3a522933-ae5e-2b63-96ab-3c004b4f7f10|

Example input:

```
{
  "application_id": "a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d",
  "application_secret": "kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=",
  "directory_id": "3a522933-ae5e-2b63-96ab-3c004b4f7f10"
}
```

## Technical Details

### Actions

#### Collect Investigation Package

This action collects investigation package from a machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|Investigation package collected via InsightConnect|False|Comment to associate with the action|None|Investigation package collected via InsightConnect|
|machine|string|None|True|Machine IP address, hostname, or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|

Example input:

```
{
  "comment": "Investigation package collected via InsightConnect",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|collect_investigation_package_response|machine_action|True|A response that includes information about the action taken|

Example output:

```
{
  "collect_investigation_package_response": {
    "requestorComment": "Investigation package collected via InsightConnect",
    "status": "Pending",
    "type": "CollectInvestigationPackage",
    "commands": [],
    "creationDateTimeUtc": "2021-02-25T13:53:29.1889041Z",
    "requestSource": "PublicApi",
    "id": "7de39b39-107e-4556-855b-25cf652835ef",
    "lastUpdateDateTimeUtc": "2021-02-25T13:53:29.1889041Z",
    "machineId": "8de370ca0e0e58ff2c2513bbc16f632ffa6e6024",
    "requestor": "b6e46392-61b9-48c0-ada3-63e3cd30d95b",
    "@odata.context": "https://api.securitycenter.windows.com/api/$metada...",
    "computerDnsName": "msedgewin10",
    "errorHResult": 0
  }
}
```

#### Get Related Machines

This action is used to get machines related to an file hash(SHA1), domain or username indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator|string|None|True|File hash(SHA1), domain or username indicator|None|example.com|

Example input:

```
{
  "indicator": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machines|[]machine|True|Machines related to an file hash(SHA1), domain or username indicator|

Example output:

```
{
  "machines": [
    {
      "exposureLevel": "Medium",
      "lastIpAddress": "10.0.2.15",
      "machineTags": [
        "tag1",
        "tag2"
      ],
      "agentVersion": "10.5850.17763.348",
      "lastSeen": "2020-12-08T10:37:41.2907723Z",
      "osBuild": 17763,
      "osPlatform": "Windows10",
      "rbacGroupId": 0,
      "computerDnsName": "msedgewin10",
      "firstSeen": "2020-12-08T09:33:03.1262943Z",
      "osProcessor": "x64",
      "version": "1809",
      "deviceValue": "Normal",
      "healthStatus": "Active",
      "id": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
      "isAadJoined": false,
      "lastExternalIpAddress": "83.220.117.67",
      "riskScore": "None"
    }
  ]
}
```

#### Manage Tags

This action is used to add or remove machine tags.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|machine|string|None|True|Machine IP address, hostname, or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
|tag|string|None|True|The tag value|None|example tag|
|type|boolean|True|True|True to add tag, false to remove it|None|True|

Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
  "tag": "example tag",
  "type": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|manage_tags_response|manage_tags_response|True|A response that includes updated tags and supplemental information about the machine|

Example output:

```
{
  "manage_tags_response": {
    "computerDnsName": "msedgewin10",
    "deviceValue": "Normal",
    "machineTags": ["tag1", "tag2", "example tag"],
    "riskScore": "None",
    "@odata.context": "https://api.securitycenter.windows.com/api/$metada...",
    "id": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
    "osProcessor": "x64",
    "rbacGroupId": 0,
    "version": "1809",
    "osPlatform": "Windows10",
    "agentVersion": "10.5850.17763.348",
    "exposureLevel": "Medium",
    "isAadJoined": false,
    "lastExternalIpAddress": "83.220.117.67",
    "lastIpAddress": "10.0.2.15",
    "osBuild": 17763,
    "firstSeen": "2020-12-08T09:33:03.1262943Z",
    "healthStatus": "Active",
    "lastSeen": "2020-12-08T10:37:41.2907723Z"
  }
}
```

#### Get Installed Software

This action retrieves a collection of installed software related to a given machine IP address, hostname, or machine ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|machine|string|None|True|Machine IP address, hostname, or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|

Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|software|[]software|True|List of installed software on the machine|

Example output:

```
{
  "software": [
    {
      "publicExploit": true,
      "vendor": "microsoft",
      "weaknesses": 1056,
      "activeAlert": false,
      "exposedMachines": 1,
      "id": "microsoft-_-windows_10",
      "impactScore": 63.8,
      "name": "windows_10"
    },
    {
      "exposedMachines": 0,
      "id": "microsoft-_-edge_chromium-based",
      "impactScore": 0,
      "name": "edge_chromium-based",
      "publicExploit": false,
      "vendor": "microsoft",
      "weaknesses": 0,
      "activeAlert": false
    }
  ]
}
```

#### Get Missing Software Updates

This action is used to retrieve a list of software updates.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|machine|string|None|True|Machine IP address, hostname or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|

Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|updates|[]update|True|List of updates|

Example output:

```
{
  "updates": [
    {
      "machineMissedOn": 1,
      "name": "September 2020 Security Updates",
      "osBuild": 17763,
      "productsNames": [
        "windows_10",
        "internet_explorer"
      ],
      "url": "https://catalog.update.microsoft.com/v7/site/Searc...",
      "cveAddressed": 68,
      "id": "4570333"
    }
  ]
}
```

#### Get Security Recommendations

This action is used to retrieve a list of security recommendations.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|machine|string|None|True|Machine IP address, hostname or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|

Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|recommendations|[]recommendation|True|List of security recommendations|

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

#### Blacklist

This action is used to submit or update new indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|AlertAndBlock|False|The action that will be taken if the indicator will be discovered in the organization|['Alert', 'AlertAndBlock', 'Allowed']|AlertAndBlock|
|application|string|None|False|The application associated with the indicator|None|demo-test|
|description|string|Indicator Blacklisted from InsightConnect|False|Description of the indicator|None|Indicator Blacklisted from InsightConnect|
|expiration_time|string|None|False|The expiration time of the indicator, default value is one year from now|None|2020-12-12T00:00:00Z|
|indicator|string|None|True|A supported indicator to blacklist or unblacklist. Supported indicators are IP addresses, URLs, domains, and SHA1 and SHA256 hashes|None|220e7d15b011d7fac48f2bd61114db1022197f7f|
|indicator_state|boolean|False|False|True to add indicator, false to remove it from the list|None|True|
|rbac_group_names|[]string|None|False|List of RBAC group names the indicator would be applied to|None|["group1","group2"]|
|recommended_actions|string|None|False|TI indicator alert recommended actions|None|nothing|
|severity|string|High|False|The severity of the indicator|['Informational', 'Low', 'Medium', 'High']|High|
|title|string|None|False|Indicator alert title|None|test|

Example input:

```
{
  "action": "AlertAndBlock",
  "application": "demo-test",
  "description": "Indicator Blacklisted from InsightConnect",
  "expiration_time": "2020-12-12T00:00:00Z",
  "indicator": "220e7d15b011d7fac48f2bd61114db1022197f7f",
  "indicator_state": true,
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|indicator_action_response|indicator_action|False|A response that includes the result of the action, and supplemental information about the action taken|

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

#### Get Machine Vulnerabilities

This action retrieves a collection of discovered vulnerabilities related to a given device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|machine|string|None|True|Machine IP address, hostname or machine ID|None|9de5069c5afe602b2ea0a04b66beb2c0cef77fdf|

Example input:

```
{
  "machine": "9de5069c5afe602b2ea0a04b66beb2c0cef77fdf"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|vulnerabilities|[]vulnerability|True|List of vulnerabilities of the machine|

Example output:

```
{
  "vulnerabilities": [
    {
      "id": "CVE-2020-14711",
      "name": "CVE-2020-14711",
      "description": "Vulnerability in the Oracle VM VirtualBox product of Oracle Virtualization (component: Core).  Supported versions that are affected are Prior to 5.2.44, prior to 6.0.24 and  prior to 6.1.12. Easily exploitable vulnerability allows high privileged attacker with logon to the infrastructure where Oracle VM VirtualBox executes to compromise Oracle VM VirtualBox.  Successful attacks require human interaction from a person other than the attacker. Successful attacks of this vulnerability can result in takeover of Oracle VM VirtualBox.  Note: The CVE-2020-14711 is applicable to macOS host only. CVSS 3.1 Base Score 6.5 (Confidentiality, Integrity and Availability impacts).  CVSS Vector: (CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H).",
      "severity": "Medium",
      "cvssV3": 6.5,
      "exposedMachines": 1,
      "publishedOn": "2020-07-14T00:00:00Z",
      "updatedOn": "2020-07-27T22:00:00Z",
      "publicExploit": false,
      "exploitVerified": false,
      "exploitInKit": false,
      "exploitTypes": [],
      "exploitUris": []
    }
  ]
}

```

#### Find Machines with Installed Software

This action is used to retrieve a list of device references that have specific software installed.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|software|string|None|True|Name of the software to be searched|None|microsoft-_-edge|

Example input:

```
{
  "software": "microsoft-_-edge"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machines|[]machine_software|True|List of machines with provided software|

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

#### Get Machine Information

This action is used to get details about a machine from its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|

Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine|machine|True|Machine information|

Example output:

```
{
  "machine": {
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Machines/$entity",
    "id": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
    "computerDnsName": "desktop-qo15on7",
    "firstSeen": "2020-06-26T19:54:48.0962745Z",
    "lastSeen": "2020-07-02T18:34:23.1871866Z",
    "osPlatform": "Windows10",
    "osProcessor": "x64",
    "version": "2004",
    "lastIpAddress": "198.51.100.100",
    "lastExternalIpAddress": "198.51.100.100",
    "agentVersion": "10.7150.19041.153",
    "osBuild": 19041,
    "healthStatus": "Active",
    "rbacGroupId": 0,
    "riskScore": "Medium",
    "exposureLevel": "Low",
    "machineTags": []
  }
}
```

#### Get Files from Alert

This action is used to retrieve a list of file information objects related to an alert.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert ID to get files from|None|da637293198146839977_2089064327|

Example input:

```
{
  "alert_id": "da637293198146839977_2089064327"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_list|[]file_type|True|The file ID related to the given alert ID|

Example output:

```
{
  "file_list": [
    {
      "sha1": "f093e7767bb63ac973b697d3fd1d40a78b87b8bf",
      "sha256": "470a75fe3da2ddf9d27fb3f9c96e6c665506ea7ba26ab89f0c89606f678ae4a2",
      "md5": "a69acb01b99959efec7c0a2a8caa7545",
      "globalPrevalence": 437,
      "globalFirstObserved": "2015-11-01T02:48:27.1103102Z",
      "globalLastObserved": "2020-07-05T07:58:26.8760293Z",
      "size": 740544,
      "isPeFile": true,
      "signerHash": "006276223396f7510653e20f0d10cd1a5d97176e",
      "isValidCertificate": false,
      "determinationType": "Unknown",
      "determinationValue": "HackTool:MSIL/AutoKms"
    }
  ]
}
```

#### Isolate Machine

This action is used to isolate a machine from the network, but keep the connection to windows atp open.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Comment to associate with the isolation action|None|Isolated by InsightConnect|
|isolation_type|string|None|True|Type of isolation to perform on target machine|['Full', 'Selective']|Full|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|

Example input:

```
{
  "comment": "Isolated by InsightConnect",
  "isolation_type": "Full",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_isolation_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|

Example output:

```
{
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
    "id": "b89eb834-4578-496c-8be0-03f004061435",
    "type": "Isolate",
    "requestor": "user@example.com",
    "requestorComment": "Isolate machine due to alert 1234",
    "status": "InProgress",
    "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
    "creationDateTimeUtc": "2017-12-04T12:12:18.9725659Z",
    "lastUpdateTimeUtc": "2017-12-04T12:12:18.9725659Z",
    "relatedFileInfo": null
}
```

#### Unisolate Machine

This action is used to restore network connectivity to a machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Comment to associate with the unisolate action|None|Unisolated by InsightConnect|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|

Example input:

```
{
  "comment": "Unisolated by InsightConnect",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_isolation_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|

Example output:

```
{
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
    "id": "b89eb834-4578-496c-8be0-03f004061435",
    "type": "Unisolate",
    "requestor": "user@example.com",
    "requestorComment": "Isolate machine due to alert 1234",
    "status": "InProgress",
    "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
    "creationDateTimeUtc": "2017-12-04T12:12:18.9725659Z",
    "lastUpdateTimeUtc": "2017-12-04T12:12:18.9725659Z",
    "relatedFileInfo": null
}
```

#### Stop and Quarantine File

This action is used to stop the execution of a file on a machine and delete it.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Comment to associate with the stop and quarantine action|None|InsightConnect has stopped a file.|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
|sha1|string|None|True|SHA1 hash of the file to stop and quarantine on the machine|None|ad0c0f2fa80411788e81a4567d1d8758b83cd76e|

Example input:

```
{
  "comment": "InsightConnect has stopped a file.",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
  "sha1": "ad0c0f2fa80411788e81a4567d1d8758b83cd76e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stop_and_quarantine_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|

Example output:

```
{
  "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
  "id": "141408d1-384c-4c19-8b57-ba39e378011a",
  "type": "StopAndQuarantineFile",
  "requestor": "user@example.com",
  "requestorComment": "Stop and quarantine file on machine due to alert 441688558380765161_2136280442",
  "status": "InProgress",
  "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
  "creationDateTimeUtc": "2018-12-04T12:15:04.3825985Z",
  "lastUpdateTimeUtc": "2018-12-04T12:15:04.3825985Z",
  "relatedFileInfo": {
      "fileIdentifier": "87662bc3d60e4200ceaf7aae249d1c343f4b83c9",
      "fileIdentifierType": "Sha1"
  }
}
```

#### Run Antivirus Scan

This action is used to initiate a Windows Defender antivirus scan on a machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Comment to associate with the antivirus scan action|None|InsightConnect has started an antivirus scan.|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
|scan_type|string|None|True|The type of antivirus scan to run|['Full', 'Quick']|Full|

Example input:

```
{
  "comment": "InsightConnect has started an antivirus scan.",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
  "scan_type": "Full"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_action_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|

Example output:

```
{
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
    "id": "2e9da30d-27f6-4208-81f2-9cd3d67893ba",
    "type": "RunAntiVirusScan",
    "requestor": "user@example.com",
    "requestorComment": "Check machine for viruses due to alert 3212",
    "status": "InProgress",
    "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
    "creationDateTimeUtc": "2018-12-04T12:18:27.1293487Z",
    "lastUpdateTimeUtc": "2018-12-04T12:18:27.1293487Z",
    "relatedFileInfo": null
}
```

#### Get Machine Action

This action is used to retrieve details about an action taken on a machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action_id|string|None|True|Action ID|None|ffd1f0cb-68ad-44ea-bf90-d01061b965ec|

Example input:

```
{
  "action_id": "ffd1f0cb-68ad-44ea-bf90-d01061b965ec"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_action_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|

Example output:

```
{
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
    "id": "2e9da30d-27f6-4208-81f2-9cd3d67893ba",
    "type": "RunAntiVirusScan",
    "requestor": "user@example.com",
    "requestorComment": "Check machine for viruses due to alert 3212",
    "status": "InProgress",
    "machineId": "1e5bc9d7e413ddd7902c2932e418702b84d0cc07",
    "creationDateTimeUtc": "2018-12-04T12:18:27.1293487Z",
    "lastUpdateTimeUtc": "2018-12-04T12:18:27.1293487Z",
    "relatedFileInfo": null
}
```

### Triggers

#### Get Alerts Matching Key

This trigger is used to get alerts that match a given key to its value.

The valid key names are shown in the example output for this action. The key names and values must be exact case when
looking for a match.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|integer|10|False|Poll frequency in seconds|None|10|
|key|string|None|True|The key to look for in the alert. This key must match the case shown in the example output section in help|None|assignedTo|
|value|string|None|True|The value to look for in the alert. The value must match the case of the value returned|None|user@example.com|

Example input:

```
{
  "frequency": 10,
  "key": "assignedTo",
  "value": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert|True|An alert that contains the given key and matching value|

Example output:

```
{
   "alert":{
      "id":"da637292082891366787_322129023",
      "incidentId":1,
      "investigationId":1,
      "assignedTo":"Automation",
      "severity":"Informational",
      "status":"Resolved",
      "investigationState":"Benign",
      "detectionSource":"WindowsDefenderAv",
      "category":"Malware",
      "title":"'EICAR_Test_File' malware was detected",
      "description":"Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
      "alertCreationTime":"2020-07-01T13:51:29.0741799Z",
      "firstEventTime":"2020-07-01T13:49:55.2853766Z",
      "lastEventTime":"2020-07-01T13:49:55.8520351Z",
      "lastUpdateTime":"2020-07-02T20:11:23.0966667Z",
      "resolvedTime":"2020-07-01T14:02:24.4812386Z",
      "machineId":"2df36d707c1ee508xyFf77f3dbfc95db65bc4a73",
      "computerDnsName":"example-desktop",
      "aadTenantId":"5c824599-ab2c-43ab-651x-3b886d4f8f10",
      "comments":[

      ],
      "evidence":[
        {
          "entityType": "User",
          "evidenceCreationTime": "2021-01-26T20:33:58.42Z",
          "sha1": "ff836cfb1af40252bd2a2ea843032e99a5b262ed",
          "sha256": "a4752c71d81afd3d5865d24ddb11a6b0c615062fcc448d24050c2172d2cbccd6",
          "fileName": "rundll32.exe",
          "filePath": "C:\\Windows\\SysWOW64",
          "processId": 3276,
          "processCommandLine": "rundll32.exe  c:\\temp\\suspicious.dll,RepeatAfterMe",
          "processCreationTime": "2021-01-26T20:31:32.9581596Z",
          "parentProcessId": 8420,
          "parentProcessCreationTime": "2021-01-26T20:31:32.9004163Z",
          "parentProcessFileName": "rundll32.exe",
          "parentProcessFilePath": "C:\\Windows\\System32",
          "ipAddress": "8.8.8.8",
          "url": null,
          "registryKey": "Test9999",
          "registryHive": null,
          "registryValueType": null,
          "registryValue": null,
          "accountName": "name",
          "domainName": "DOMAIN",
          "userSid": "S-1-5-21-11111607-1111760036-109187956-75141",
          "aadUserId": "11118379-2a59-1111-ac3c-a51eb4a3c627",
          "userPrincipalName": "user@example.com",
          "detectionStatus": "Detected"
        }
      ]
   }
}
```

#### Get Alerts

This trigger is used to return all new alerts.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|integer|10|False|Poll frequency in seconds|None|10|

Example input:

```
{
  "frequency": 10
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert|True|Alert|

Example output:

```
{
   "alert":{
      "id":"da637292082891366787_322129023",
      "incidentId":1,
      "investigationId":1,
      "assignedTo":"Automation",
      "severity":"Informational",
      "status":"Resolved",
      "investigationState":"Benign",
      "detectionSource":"WindowsDefenderAv",
      "category":"Malware",
      "title":"'EICAR_Test_File' malware was detected",
      "description":"Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nThis detection might indicate that the malware was stopped from delivering its payload. However, it is prudent to check the machine for signs of infection.",
      "alertCreationTime":"2020-07-01T13:51:29.0741799Z",
      "firstEventTime":"2020-07-01T13:49:55.2853766Z",
      "lastEventTime":"2020-07-01T13:49:55.8520351Z",
      "lastUpdateTime":"2020-07-02T20:11:23.0966667Z",
      "resolvedTime":"2020-07-01T14:02:24.4812386Z",
      "machineId":"2df36d707c1ee508xyFf77f3dbfc95db65bc4a73",
      "computerDnsName":"example-desktop",
      "aadTenantId":"5c824599-ab2c-43ab-651x-3b886d4f8f10",
      "comments":[],
      "evidence":[]
   }
}
```

### Custom Output Types

#### alert

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AAD Tenant ID|string|False|AAD tenant ID|
|Alert Creation Time|string|False|Alert creation time|
|Assigned To|string|False|Assigned To|
|Category|string|False|Category|
|Classification|string|False|Classification|
|Computer DNS Name|string|False|Computer DNS name|
|Description|string|False|Description|
|Detection Source|string|False|Detection source|
|Determination|string|False|Determination|
|First Event Time|string|False|First event time|
|ID|string|False|ID|
|Incident ID|integer|False|Incident ID|
|Investigation ID|integer|False|Investigation ID|
|Investigation State|string|False|Investigation state|
|Last Event Time|string|False|Last event time|
|Last Update Time|string|False|Last update time|
|Machine ID|string|False|Machine ID|
|RBAC Group Name|string|False|RBAC group name|
|Related User|related_user_object|False|Related user|
|Resolved Time|string|False|Resolved time|
|Severity|string|False|Severity|
|Status|string|False|Status|
|Threat Family Name|string|False|Threat family name|
|Title|string|False|Title|

#### file_type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Determination Type|string|False|Determination type|
|Determination Value|string|False|Determination value|
|File Product Name|string|False|File product name|
|File Publisher|string|False|File publisher|
|File Type|string|False|File type|
|Global First Observed|string|False|Global first observed|
|Global Last Observed|string|False|Global last observed|
|Global Prevalence|integer|False|Global prevalence|
|Is PE File|boolean|False|Is PE File|
|Is Valid Certificate|boolean|False|Is valid certificate|
|Issuer|string|False|Issuer|
|MD5|string|False|MD5|
|SHA1|string|False|SHA1|
|SHA256|string|False|SHA256|
|Signer|string|False|Signer|
|Signer Hash|string|False|Signer hash|
|Size|integer|False|Size|

#### indicator_action

|Name|Type|Required|Description|
|----|----|--------|-----------|
|@Odata.Context|string|False|@odata.context|
|Action|string|False|The action that will be taken if the indicator will be discovered in the organization|
|Application|string|False|The application associated with the indicator|
|Created By|string|False|Unique identity of the user/application that submitted the indicator|
|Created By Display Name|string|False|Created by display name|
|Created By Source|string|False|Created by source|
|Creation Time|string|False|The date and time when the indicator was created|
|Description|string|False|Description of the indicator|
|Expiration Time|string|False|The expiration time of the indicator|
|Generate Alert|boolean|False|Generate alert|
|Historical Detection|boolean|False|Historical detection|
|Indicator ID|string|False|Identity of the indicator entity|
|Indicator Type|string|False|Type of the indicator|
|Indicator Value|string|False|The potentially malicious indicator of one of the following types: IP addresses, URLs, domains, and SHA1 and SHA256 hashes|
|Last Update Time|string|False|The last time the indicator was updated|
|Last Updated By|string|False|Identity of the user/application that last updated the indicator|
|MITRE Techniques|[]string|False|MITRE techniques|
|RBAC Group IDs|[]string|False|RBAC group IDs|
|RBAC Group Names|[]string|False|RBAC device group names where the indicator is exposed and active. Empty list in case it exposed to all devices|
|Recommended Actions|string|False|Recommended actions for the indicator|
|Severity|string|False|The severity of the indicator|
|Source|string|False|The name of the user/application that submitted the indicator|
|Source Type|string|False|User in case the Indicator created by a user (e.g. from the portal), AadApp in case it submitted using automated application via the API.|
|Title|string|False|Indicator alert title|

#### machine

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent Version|string|False|Agent version|
|Computer DNS Name|string|False|Computer DNS name|
|Exposure Level|string|False|Exposure level|
|First Seen|string|False|First seen|
|Health Status|string|False|Health status|
|ID|string|False|ID|
|Last External IP Address|string|False|Last external IP address|
|Last IP Address|string|False|Last IP address|
|Last Seen|string|False|Last seen|
|Machine Tags|[]string|False|Machine Tags|
|OS Build|integer|False|OS build|
|OS Platform|string|False|OS platform|
|OS Processor|string|False|OS processor|
|RBAC Group ID|integer|False|RBAC group ID|
|Risk Score|string|False|Risk score|
|Version|string|False|Version|

#### machine_action

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Creation Date Time UTC|string|False|Creation date time UTC|
|Error HResult|integer|False|Error HResult|
|ID|string|False|ID|
|Last Update Date Time UTC|string|False|Last update date time UTC|
|Machine ID|string|False|Machine ID|
|Requestor|string|False|Requestor|
|Requestor Comment|string|False|Requestor comment|
|Status|string|False|Status|

#### machine_software

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Computer DNS Name|string|False|Computer DNS name|
|ID|string|False|ID|
|OS Platform|string|False|OS platform|
|RBAC Group ID|number|False|RBAC group ID|
|RBAC Group Name|string|False|RBAC group name|

#### manage_tags_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|@Odata.Context|string|False|@odata.context|
|Agent Version|string|False|Agent version|
|Computer DNS Name|string|False|Computer DNS name|
|Device Value|string|False|Device value|
|Exposure Level|string|False|Exposure level|
|First Seen|string|False|First seen|
|Health Status|string|False|Health status|
|ID|string|False|ID|
|Is AAD Joined|boolean|False|Is AAD joined|
|Last External IP Address|string|False|Last external IP address|
|Last IP Address|string|False|Last IP address|
|Last Seen|string|False|Last seen|
|Machine Tags|[]string|False|Machine tags|
|OS Build|integer|False|OS build|
|OS Platform|string|False|OS platform|
|OS Processor|string|False|OS Processor|
|RBAC Group ID|integer|False|RBAC group ID|
|Risk Score|string|False|Risk score|
|Version|string|False|Version|

#### recommendation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Active Alert|boolean|False|Active alert|
|Associated Threats|[]string|False|Associated threats|
|Config Score Impact|float|False|Config score impact|
|Exposed Machines Count|integer|False|Exposed machines count|
|Exposure Impact|float|False|Exposure impact|
|ID|string|False|ID|
|Non Productivity Impacted Assets|integer|False|Non productivity impacted assets|
|Product Name|string|False|Product name|
|Public Exploit|boolean|False|Public exploit|
|Recommendation Category|string|False|Recommendation category|
|Recommendation Name|string|False|Recommendation name|
|Related Component|string|False|Related component|
|Remediation Type|string|False|Remediation type|
|Severity Score|float|False|Severity score|
|Status|string|False|Status|
|Total Machine Count|integer|False|Total machine count|
|Vendor|string|False|Vendor|
|Weaknesses|integer|False|Weaknesses|

#### related_user_object

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Domain Name|string|False|Domain name|
|User Name|string|False|User name|

#### software

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Active Alert|boolean|False|Active alert|
|Exposed Machines|integer|False|Exposed machines|
|ID|string|False|ID|
|Impact Score|float|False|Impact score|
|Name|string|False|Name|
|Public Exploit|boolean|False|Public exploit|
|Vendor|string|False|Vendor|
|Weaknesses|integer|False|Weaknesses|

#### update

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CVE Addressed|integer|False|Update CVE addressed|
|ID|string|False|Update ID|
|Machine Missed On|integer|False|Update machine missed on|
|Name|string|False|Update name|
|OS Build|integer|False|Update OS build|
|Products Names|[]string|False|Update products names|
|URL|string|False|Update URL|

#### vulnerability

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CVSS V3|float|False|CVSS v3|
|Description|string|False|Description|
|Exploit In Kit|boolean|False|Exploit in kit|
|Exploit Types|[]string|False|Exploit types|
|Exploit URIs|[]string|False|Exploit URIs|
|Exploit Verified|boolean|False|Exploit verified|
|Exposed Machines|integer|False|Exposed machines|
|ID|string|False|ID|
|Name|string|False|Name|
|Public Exploit|boolean|False|Public exploit|
|Published On|string|False|Published on|
|Severity|string|False|Severity|
|Updated On|string|False|Updated on|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

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

## References

* [Windows Defender ATP](https://www.microsoft.com/en-us/windowsforbusiness/windows-atp)
* [Windows Defender ATP API Start Page](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-atp/use-apis)
* [Windows Defender ATP API Endpoints](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-atp/exposed-apis-list)
