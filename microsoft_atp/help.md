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

# Documentation

## Setup

This plugin uses the Windows Defender ATP API. It will use an Azure application to connect to the API and run
actions from InsightConnect.

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
|machine|object|True|Machine information|

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
  "key": "assignedTo",
  "value": "Automation",
  "frequency": 10
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
      "evidence":[]
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

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

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
