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
* Authentication and Resource URLs for your instance of Windows ATP

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|auth_url|string|None|True|Server used to obtain OAuth token. Example\: https\://login.windows.net/{Azure Tenant ID}/oauth2/token|None|
|client_id|string|None|True|Client ID obtained from Windows Defender Security Center API settings|None|
|client_secret|string|None|True|Client secret obtained when authorizing an application to connect to Windows Defender|None|
|host|string|https\://wdatp-alertexporter-us.securitycenter.windows.com|True|Base URL for endpoints, e.g. https\://wdatp-alertexporter-us.securitycenter.windows.com|None|
|resource_url|string|https\://api.securitycenter.windows.com|False|This will be the server that will return information from the plug-in requests. This will typically be https\://graph.windows.net (for alert information) or https\://api.securitycenter.windows.com (for machine information and actions).|None|
|seconds_ago|integer|0|False|Seconds before the first run of the trigger to check for alerts. If left blank, the trigger will start scanning from the time the workflow begins.|None|

## Technical Details

### Actions

### Get Computer ID from Machine Name

This action is used to translate a machine name to computer ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|machine_name|string|None|True|Machine Name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_id|string|True|Machine ID|

Example output:

```
{
    "machine_name": "MyComputer"
}
```

### Get Machine ID from Alert

This action is used to retrieve the machine ID related to an alert.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|alert_id|string|None|True|Alert ID to get a machine ID from|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_information|machine_information_type|True|The machine ID related to the given Alert ID|

Example output:

```
{
   "machine_information":{
      "@odata.context":"https://api.securitycenter.windows.com/api/$metadata#Machines/$entity",
      "id":"c6944fa14970633xxxxxxxx104167ef12557a6f",
      "computerDnsName":"xxxxxxxx",
      "firstSeen":"2018-11-07T17:59:46.4708884Z",
      "lastSeen":"2018-11-28T07:29:48.8372663Z",
      "osPlatform":"Windows10",
      "lastIpAddress":"10.4.18.162",
      "lastExternalIpAddress":"128.177.65.3",
      "agentVersion":"10.4850.17134.191",
      "osBuild":17134,
      "healthStatus":"Active",
      "rbacGroupId":0,
      "riskScore":"Medium",
      "isAadJoined":false,
      "machineTags":[]
   }
}
```

#### Get File ID from Alert

This action is used to retrieve the file ID related to an alert.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|alert_id|string|None|True|Alert ID to get files from|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_information|file_information|True|The file ID related to the given alert ID|

Example output:

```
{
    "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Files",
    "value": [
        {
            "sha1": "654f19c41d9662cf86be21bf0af5a88c38c56a9d",
            "sha256": "2f905feec2798cee6f63da2c26758d86bfeaab954c01e20ac7085bf55fedde87",
            "md5": "82849dc81d94056224445ea73dc6153a",
            "globalPrevalence": 33,
            "globalFirstObserved": "2018-07-17T18:17:27.5909748Z",
            "globalLastObserved": "2018-08-06T16:07:12.9414137Z",
            "windowsDefenderAVThreatName": null,
            "size": 801112,
            "fileType": "PortableExecutable",
            "isPeFile": true,
            "filePublisher": null,
            "fileProductName": null,
            "signer": "Microsoft Windows",
            "issuer": "Microsoft Development PCA 2014",
            "signerHash": "9e284231a4d1c53fc8d4492b09f65116bf97447f",
            "isValidCertificate": true
        }
    ]
}
```

#### Isolate Machine

This action is used to isolate a machine from the network, but keep the connection to windows atp open.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|machine_id|string|None|True|Machine ID|None|
|isolation_type|string|None|True|Type of isolation to perform on target machine|['Full', 'Selective']|
|comment|string|None|True|Comment to associate with the isolation action|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_isolation_response|machine_action_response|True|A response that includes the result of the action, and supplemental information about the action taken|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|machine_id|string|None|True|Machine ID|None|
|comment|string|None|True|Comment to associate with the unisolate action|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_isolation_response|machine_action_response|True|A response that includes the result of the action, and supplemental information about the action taken|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|machine_id|string|None|True|Machine ID|None|
|comment|string|None|True|Comment to associate with the stop and quarantine action|None|
|sha1|string|None|True|SHA1 of the file to stop and quarantine on the machine|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stop_and_quarantine_response|stop_and_quarantine_response|True|A response that includes the result of the action, and supplemental information about the action taken|

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
      "fileIdentifierType": "SHA1"
  }
}
```

#### Run Antivirus Scan

This action is used to initiate a Windows Defender antivirus scan on a machine.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|machine_id|string|None|True|Machine ID|None|
|comment|string|None|True|Comment to associate with the antivirus scan action|None|
|scan_type|string|None|True|The type of antivirus scan to run|['Full', 'Quick']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_action_response|machine_action_response|True|A response that includes the result of the action, and supplemental information about the action taken|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|action_id|string|None|True|Action ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine_action_response|machine_action_response|True|A response that includes the result of the action, and supplemental information about the action taken|

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

#### Get Alerts for ID

This trigger is used to get alerts by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|ID to get|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]alert|True|All alerts that match the given ID|

Example output:

```
{
   "results":[
      {
         "AlertTime":"2018-11-07T18:59:10.2582627Z",
         "ComputerDnsName":"xxxxxxxx",
         "AlertTitle":"Suspicious Powershell commandline",
         "Category":"SuspiciousActivity",
         "Severity":"Medium",
         "AlertId":"636772141692393966_614861963",
         "LinkToWDATP":"https://securitycenter.windows.com/alert/636772141692393966_614861963",
         "SHA1":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "FileName":"powershell.exe",
         "FilePath":"C:\\Windows\\System32\\WindowsPowerShell\\v1.0",
         "IoaDefinitionId":"7f1c3609-a3ff-40e2-995b-c01770161d68",
         "AlertPart":0,
         "FullId":"636772141692393966_614861963:DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco=",
         "LastProcessedTimeUtc":"2018-11-07T19:05:01.8993766Z",
         "Source":"EDR",
         "Md5":"95000560239032bc68b4c2fdfcdef913",
         "Sha256":"d3f8fade829d2b7bd596c4504a6dae5c034e789b6a3defbe013bda7d14466677",
         "LogOnUsers":"XXXXXXXX\\Administrator",
         "MachineName":"XXXXXX",
         "InternalIPv4List":"XXX.XXX.XXX.XXX",
         "InternalIPv6List":"XXXXXXXXXX",
         "FileHash":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "DeviceID":"c6944fa14970633adeecbabc104167ef12557a6f",
         "Description":"A suspicious Powershell commandline was found on the machine. This commandline might be used during installation, exploration, or in some cases with lateral movement activities which are used by attackers to invoke modules, download external payloads, and get more information about the system. Attackers usually use Powershell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.\r\nThe process powershell.exe was executing suspicious commandline \r\npowershell.exe  -NoExit -ExecutionPolicy Bypass -WindowStyle Hidden (New-Object System.Net.WebClient).DownloadFile('http://127.0.0.1/1.exe', 'C:\\test-WDATP-test\\invoice.exe'); Start-Process 'C:\\test-WDATP-test\\invoice.exe'",
         "ExternalId":"418AE8AD3F8A1B26F9D02B09E0583A0AEBAC93E7",
         "IocUniqueId":"DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco="
      }
   ]
}
```

#### Get Alerts for Domain

This trigger is used to get alerts by domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain to get|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]alert|True|All alerts that match the given domain|

Example output:

```
{
   "results":[
      {
         "AlertTime":"2018-11-07T18:59:10.2582627Z",
         "ComputerDnsName":"xxxxxxxx",
         "AlertTitle":"Suspicious Powershell commandline",
         "Category":"SuspiciousActivity",
         "Severity":"Medium",
         "AlertId":"636772141692393966_614861963",
         "LinkToWDATP":"https://securitycenter.windows.com/alert/636772141692393966_614861963",
         "SHA1":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "FileName":"powershell.exe",
         "FilePath":"C:\\Windows\\System32\\WindowsPowerShell\\v1.0",
         "IoaDefinitionId":"7f1c3609-a3ff-40e2-995b-c01770161d68",
         "AlertPart":0,
         "FullId":"636772141692393966_614861963:DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco=",
         "LastProcessedTimeUtc":"2018-11-07T19:05:01.8993766Z",
         "Source":"EDR",
         "Md5":"95000560239032bc68b4c2fdfcdef913",
         "Sha256":"d3f8fade829d2b7bd596c4504a6dae5c034e789b6a3defbe013bda7d14466677",
         "LogOnUsers":"XXXXXXXX\\Administrator",
         "MachineName":"XXXXXX",
         "InternalIPv4List":"XXX.XXX.XXX.XXX",
         "InternalIPv6List":"XXXXXXXXXX",
         "FileHash":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "DeviceID":"c6944fa14970633adeecbabc104167ef12557a6f",
         "Description":"A suspicious Powershell commandline was found on the machine. This commandline might be used during installation, exploration, or in some cases with lateral movement activities which are used by attackers to invoke modules, download external payloads, and get more information about the system. Attackers usually use Powershell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.\r\nThe process powershell.exe was executing suspicious commandline \r\npowershell.exe  -NoExit -ExecutionPolicy Bypass -WindowStyle Hidden (New-Object System.Net.WebClient).DownloadFile('http://127.0.0.1/1.exe', 'C:\\test-WDATP-test\\invoice.exe'); Start-Process 'C:\\test-WDATP-test\\invoice.exe'",
         "ExternalId":"418AE8AD3F8A1B26F9D02B09E0583A0AEBAC93E7",
         "IocUniqueId":"DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco="
      }
   ]
}
```

#### Get Alerts for Actor

This trigger is used to get alerts by an actor.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|actor|string|None|True|Actor to get|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]alert|True|All alerts that match the given actor|

Example output:

```
{
   "results":[
      {
         "AlertTime":"2018-11-07T18:59:10.2582627Z",
         "ComputerDnsName":"xxxxxxxx",
         "AlertTitle":"Suspicious Powershell commandline",
         "Category":"SuspiciousActivity",
         "Severity":"Medium",
         "AlertId":"636772141692393966_614861963",
         "LinkToWDATP":"https://securitycenter.windows.com/alert/636772141692393966_614861963",
         "SHA1":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "FileName":"powershell.exe",
         "FilePath":"C:\\Windows\\System32\\WindowsPowerShell\\v1.0",
         "IoaDefinitionId":"7f1c3609-a3ff-40e2-995b-c01770161d68",
         "AlertPart":0,
         "FullId":"636772141692393966_614861963:DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco=",
         "LastProcessedTimeUtc":"2018-11-07T19:05:01.8993766Z",
         "Source":"EDR",
         "Md5":"95000560239032bc68b4c2fdfcdef913",
         "Sha256":"d3f8fade829d2b7bd596c4504a6dae5c034e789b6a3defbe013bda7d14466677",
         "LogOnUsers":"XXXXXXXX\\Administrator",
         "MachineName":"XXXXXX",
         "InternalIPv4List":"XXX.XXX.XXX.XXX",
         "InternalIPv6List":"XXXXXXXXXX",
         "FileHash":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "DeviceID":"c6944fa14970633adeecbabc104167ef12557a6f",
         "Description":"A suspicious Powershell commandline was found on the machine. This commandline might be used during installation, exploration, or in some cases with lateral movement activities which are used by attackers to invoke modules, download external payloads, and get more information about the system. Attackers usually use Powershell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.\r\nThe process powershell.exe was executing suspicious commandline \r\npowershell.exe  -NoExit -ExecutionPolicy Bypass -WindowStyle Hidden (New-Object System.Net.WebClient).DownloadFile('http://127.0.0.1/1.exe', 'C:\\test-WDATP-test\\invoice.exe'); Start-Process 'C:\\test-WDATP-test\\invoice.exe'",
         "ExternalId":"418AE8AD3F8A1B26F9D02B09E0583A0AEBAC93E7",
         "IocUniqueId":"DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco="
      }
   ]
}
```

#### Get Alerts by File Name

This trigger is used to get alerts by file name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filename|string|None|True|File name to get|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]alert|True|All alerts that match the given file name|

Example output:

```
{
   "results":[
      {
         "AlertTime":"2018-11-07T18:59:10.2582627Z",
         "ComputerDnsName":"xxxxxxxx",
         "AlertTitle":"Suspicious Powershell commandline",
         "Category":"SuspiciousActivity",
         "Severity":"Medium",
         "AlertId":"636772141692393966_614861963",
         "LinkToWDATP":"https://securitycenter.windows.com/alert/636772141692393966_614861963",
         "SHA1":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "FileName":"powershell.exe",
         "FilePath":"C:\\Windows\\System32\\WindowsPowerShell\\v1.0",
         "IoaDefinitionId":"7f1c3609-a3ff-40e2-995b-c01770161d68",
         "AlertPart":0,
         "FullId":"636772141692393966_614861963:DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco=",
         "LastProcessedTimeUtc":"2018-11-07T19:05:01.8993766Z",
         "Source":"EDR",
         "Md5":"95000560239032bc68b4c2fdfcdef913",
         "Sha256":"d3f8fade829d2b7bd596c4504a6dae5c034e789b6a3defbe013bda7d14466677",
         "LogOnUsers":"XXXXXXXX\\Administrator",
         "MachineName":"XXXXXX",
         "InternalIPv4List":"XXX.XXX.XXX.XXX",
         "InternalIPv6List":"XXXXXXXXXX",
         "FileHash":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "DeviceID":"c6944fa14970633adeecbabc104167ef12557a6f",
         "Description":"A suspicious Powershell commandline was found on the machine. This commandline might be used during installation, exploration, or in some cases with lateral movement activities which are used by attackers to invoke modules, download external payloads, and get more information about the system. Attackers usually use Powershell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.\r\nThe process powershell.exe was executing suspicious commandline \r\npowershell.exe  -NoExit -ExecutionPolicy Bypass -WindowStyle Hidden (New-Object System.Net.WebClient).DownloadFile('http://127.0.0.1/1.exe', 'C:\\test-WDATP-test\\invoice.exe'); Start-Process 'C:\\test-WDATP-test\\invoice.exe'",
         "ExternalId":"418AE8AD3F8A1B26F9D02B09E0583A0AEBAC93E7",
         "IocUniqueId":"DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco="
      }
   ]
}
```

#### Get Alerts Matching Key

This trigger is used to get alerts that match a given key to its value.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|key|string|None|True|The key to look for in the alert|None|
|value|string|None|True|The value to look for in the alert|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]alert|True|All alerts that contain the given key and match its value|

Example output:

```
{
   "results":[
      {
         "AlertTime":"2018-11-07T18:59:10.2582627Z",
         "ComputerDnsName":"xxxxxxxx",
         "AlertTitle":"Suspicious Powershell commandline",
         "Category":"SuspiciousActivity",
         "Severity":"Medium",
         "AlertId":"636772141692393966_614861963",
         "LinkToWDATP":"https://securitycenter.windows.com/alert/636772141692393966_614861963",
         "SHA1":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "FileName":"powershell.exe",
         "FilePath":"C:\\Windows\\System32\\WindowsPowerShell\\v1.0",
         "IoaDefinitionId":"7f1c3609-a3ff-40e2-995b-c01770161d68",
         "AlertPart":0,
         "FullId":"636772141692393966_614861963:DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco=",
         "LastProcessedTimeUtc":"2018-11-07T19:05:01.8993766Z",
         "Source":"EDR",
         "Md5":"95000560239032bc68b4c2fdfcdef913",
         "Sha256":"d3f8fade829d2b7bd596c4504a6dae5c034e789b6a3defbe013bda7d14466677",
         "LogOnUsers":"XXXXXXXX\\Administrator",
         "MachineName":"XXXXXX",
         "InternalIPv4List":"XXX.XXX.XXX.XXX",
         "InternalIPv6List":"XXXXXXXXXX",
         "FileHash":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "DeviceID":"c6944fa14970633adeecbabc104167ef12557a6f",
         "Description":"A suspicious Powershell commandline was found on the machine. This commandline might be used during installation, exploration, or in some cases with lateral movement activities which are used by attackers to invoke modules, download external payloads, and get more information about the system. Attackers usually use Powershell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.\r\nThe process powershell.exe was executing suspicious commandline \r\npowershell.exe  -NoExit -ExecutionPolicy Bypass -WindowStyle Hidden (New-Object System.Net.WebClient).DownloadFile('http://127.0.0.1/1.exe', 'C:\\test-WDATP-test\\invoice.exe'); Start-Process 'C:\\test-WDATP-test\\invoice.exe'",
         "ExternalId":"418AE8AD3F8A1B26F9D02B09E0583A0AEBAC93E7",
         "IocUniqueId":"DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco="
      }
   ]
}
```

#### Get Alerts

This trigger is used to return all new alerts.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|frequency|integer|5|False|Poll frequency in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]alert|True|All new alerts are returned|

Example output:

```
{
   "results":[
      {
         "AlertTime":"2018-11-07T18:59:10.2582627Z",
         "ComputerDnsName":"xxxxxxxx",
         "AlertTitle":"Suspicious Powershell commandline",
         "Category":"SuspiciousActivity",
         "Severity":"Medium",
         "AlertId":"636772141692393966_614861963",
         "LinkToWDATP":"https://securitycenter.windows.com/alert/636772141692393966_614861963",
         "SHA1":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "FileName":"powershell.exe",
         "FilePath":"C:\\Windows\\System32\\WindowsPowerShell\\v1.0",
         "IoaDefinitionId":"7f1c3609-a3ff-40e2-995b-c01770161d68",
         "AlertPart":0,
         "FullId":"636772141692393966_614861963:DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco=",
         "LastProcessedTimeUtc":"2018-11-07T19:05:01.8993766Z",
         "Source":"EDR",
         "Md5":"95000560239032bc68b4c2fdfcdef913",
         "Sha256":"d3f8fade829d2b7bd596c4504a6dae5c034e789b6a3defbe013bda7d14466677",
         "LogOnUsers":"XXXXXXXX\\Administrator",
         "MachineName":"XXXXXX",
         "InternalIPv4List":"XXX.XXX.XXX.XXX",
         "InternalIPv6List":"XXXXXXXXXX",
         "FileHash":"1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
         "DeviceID":"c6944fa14970633adeecbabc104167ef12557a6f",
         "Description":"A suspicious Powershell commandline was found on the machine. This commandline might be used during installation, exploration, or in some cases with lateral movement activities which are used by attackers to invoke modules, download external payloads, and get more information about the system. Attackers usually use Powershell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.\r\nThe process powershell.exe was executing suspicious commandline \r\npowershell.exe  -NoExit -ExecutionPolicy Bypass -WindowStyle Hidden (New-Object System.Net.WebClient).DownloadFile('http://127.0.0.1/1.exe', 'C:\\test-WDATP-test\\invoice.exe'); Start-Process 'C:\\test-WDATP-test\\invoice.exe'",
         "ExternalId":"418AE8AD3F8A1B26F9D02B09E0583A0AEBAC93E7",
         "IocUniqueId":"DEkMrsut7_rqWkwqIaCEcsytUIOl_Dvi56ShSB9wKco="
      }
   ]
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.6.0 - New action Get Machine ID from Alert
* 1.5.1 - New spec and help.md format for the Hub
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

