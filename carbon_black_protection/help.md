
# Carbon Black Protection

## About

[Carbon Black Protection](https://www.carbonblack.com/products/cb-protection/) allows users to lock down and harden systems to prevent malware, ransomware, and more.

This plugin utilizes the [Carbon Black Protection API](https://developer.carbonblack.com/reference/enterprise-protection/7.2/rest-api/).

## Actions

### Unban File

This action is used to unban a file globally or by policy.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_ids|[]integer|None|False|List of policy IDs. Only fill in this field if ban is by policy|None|
|hash|string|None|True|Hash for file to unban|None|
|new_state|string|Approved|True|New state of the file. Either approved or unapproved|['Approved', 'Unapproved']|
|method|string|Globally|True|Unban globally or by policy|['Globally', 'Policy']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_rule|fileRule|False|Updated file rule|

Example output:

```

{
    "file_rule": {
      "dateCreated": "2017-09-29T17:02:50.803Z",
      "sourceId": 0,
      "hash": "8a7f245f77fe0509a7ebd37fa248052b507b2c37642c67deeedec3f68e86f25e",
      "sourceType": 5,
      "name": "iexplore.exe",
      "platformFlags": 0,
      "forceInstaller": false,
      "modifiedBy": "admin",
      "createdBy": "admin",
      "clVersion": 934,
      "reputationApprovalsEnabled": true,
      "fileState": 2,
      "createdByUserId": 0,
      "modifiedByUserId": 0,
      "forceNotInstaller": false,
      "reportOnly": false,
      "fileCatalogId": 15275,
      "id": 801,
      "dateModified": "2017-10-02T23:47:18.443Z"
}

```

### Ban File

This action is used to ban a file globally or by policy.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_ids|[]integer|None|False|List of policy IDs. Only fill in this field if ban is by policy|None|
|hash|string|None|True|Hash for file to ban|None|
|method|string|Globally|True|Ban globally or by policy|['Globally', 'Policy']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_rule|fileRule|False|Updated file rule|

Example output:

```

{
      "createdByUserId": 1,
      "modifiedBy": "api_admin",
      "reputationApprovalsEnabled": true,
      "sourceType": 5,
      "id": 791,
      "dateCreated": "2017-09-29T16:43:33.12Z",
      "hash": "06E77B5F6BB60E11A377B68BA4AA1DA7",
      "sourceId": 0,
      "createdBy": "api_admin",
      "modifiedByUserId": 1,
      "fileState": 3,
      "platformFlags": 0,
      "clVersion": 932,
      "dateModified": "2017-09-29T19:45:10.507Z",
      "forceInstaller": false,
      "fileCatalogId": 0,
      "reportOnly": false,
      "forceNotInstaller": false
}

```

### Approve File Locally

This action is used to approve a file locally.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|integer|None|True|File ID of file to approve locally|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_instance|fileInstance|False|Updated file instance|

Example output:

```

{
    "file_instance": {
      "fileInstanceGroupId": 1,
      "fileName": "wab.exe",
      "executed": true,
      "dateCreated": "2017-09-28T21:59:10Z",
      "fileCatalogId": 741,
      "computerId": 1,
      "detachedPublisherId": 4,
      "detachedCertificateId": 22,
      "id": 1000,
      "pathName": "c:\\program files (x86)\\windows mail",
      "localState": 2,
      "detailedLocalState": 4
}

```

### Unapprove File Locally

This action is used to remove local approval for a file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|integer|None|True|File ID of file to remove local approval for|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_instance|fileInstance|False|Updated file instance|

Example output:

```

{
    "file_instance": {
      "dateCreated": "2017-09-28T21:59:10Z",
      "pathName": "c:\\program files (x86)\\windows mail",
      "computerId": 1,
      "detailedLocalState": 4,
      "detachedCertificateId": 22,
      "id": 1000,
      "fileCatalogId": 741,
      "detachedPublisherId": 4,
      "localState": 2,
      "fileInstanceGroupId": 1,
      "executed": true,
      "fileName": "wab.exe"
}

```

### Create File Rule

This action creates a file rule, this allows for the creation and editing of file Approvals and Bans.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|description|string|None|True|Description of this rule|None|
|file_catalog_id|integer|None|False|Id of fileCatalog entry associated with this fileRule. Can be 0 if creating/modifying rule based on hash or file name|None|
|file_state|integer|1|False|File state for this rule. Can be one of 1=Unapproved, 2=Approved, 3=Banned|None|
|force_installer|boolean|False|False|True if this file is forced to act as installer, even if product detected it as ‘not installer’|None|
|force_not_installer|boolean|False|False|True if this file is forced to act as ‘not installer’, even if product detected it as installer|None|
|hash|string|None|False|Hash associated with this rule. This parameter is not required if fileCatalogId is supplied|None|
|name|string|None|True|Name of this rule|None|
|platform_flags|string|1, 2, 4|False|Comma separated list of platform flags where this file rule will be valid. combination of 1 = Windows, 2 = Mac, 4 = Linux|None|
|policy_ids|string|0|False|Comma separated list of IDs of policies where this rule applies. 0 if this is a global rule|None|
|report_only|boolean|False|False|Set to true to create a report-only ban. Note - fileState has to be set to 1 (unapproved) before this flag can be set|None|
|reputation_approvals_enabled|boolean|False|False|True if reputation approvals are enabled for this file|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_rule|fileRule|False|Updated file rule|

Example output:

```
{
  "file_rule": {
    "id": 1341,
    "fileCatalogId": 5025,
    "name": "KomandFileRule",
    "description": "Komand File Rule test description",
    "fileState": 1,
    "reputationApprovalsEnabled": false,
    "reportOnly": false,
    "forceInstaller": false,
    "forceNotInstaller": false,
    "lazyApproval": false,
    "sourceType": 0,
    "sourceId": 0,
    "hash": "926ca7d813f5248e66f124ddd223534f67b7603ea6dd077dc1b552bc2266d519",
    "dateCreated": "2019-05-30T16:39:31.68Z",
    "dateModified": "2019-05-30T17:20:05.41Z",
    "createdBy": "joey",
    "modifiedBy": "joey",
    "clVersion": 0,
    "platformFlags": 124,
    "createdByUserId": 3,
    "modifiedByUserId": 3,
    "idUnique": "07a94192-3bb2-446f-a181-330ad81cf5cc",
    "fileRuleType": "Unapproved",
    "version": 1076229,
    "visible": false
  }
}
```

### Get File Rule

This action is used to get a File Rule.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_rule_id|integer|None|True|File rule ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_rule|fileRule|False|Updated file rule|

Example output:

```
{
  "file_rule": {
    "id": 1341,
    "fileCatalogId": 5025,
    "name": "KomandFileRule",
    "description": "Komand File Rule test description",
    "fileState": 1,
    "reputationApprovalsEnabled": false,
    "reportOnly": false,
    "forceInstaller": false,
    "forceNotInstaller": false,
    "lazyApproval": false,
    "sourceType": 0,
    "sourceId": 0,
    "hash": "926ca7d813f5248e66f124ddd223534f67b7603ea6dd077dc1b552bc2266d519",
    "dateCreated": "2019-05-30T16:39:31.68Z",
    "dateModified": "2019-05-30T17:20:05.41Z",
    "createdBy": "joey",
    "modifiedBy": "joey",
    "clVersion": 0,
    "platformFlags": 124,
    "createdByUserId": 3,
    "modifiedByUserId": 3,
    "idUnique": "07a94192-3bb2-446f-a181-330ad81cf5cc",
    "fileRuleType": "Unapproved",
    "version": 1076229,
    "visible": false
  }
}
```

### Resolve Approval Request

This action is used to resolve approval requests with a desired status.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|approval_request_id|string|None|True|Resolve an approval request with the desired status|None|
|resolution|string|Not Resolved|True|Method for resolving the approval request|['Not Resolved', 'Rejected', 'Resolved - Approved', 'Resolved - Rule Change', 'Resolved - Installer', 'Resolved - Updater', 'Resolved - Publisher', 'Resolved - Other']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|approval_request|approvalRequest|False|The updated approval request|

Example output:

```

{
  "localState": 2,
  "fileCatalogId": 16,
  "dateCreated": "2017-09-28T21:57:30Z",
  "id": 1,
  "fileName": "parity.exe",
  "computerId": 1,
  "pathName": "c:\\program files (x86)\\bit9\\parity agent",
  "detailedLocalState": 11,
  "executed": true,
  "fileInstanceGroupId": 7
}

```

### Retrieve File Catalog Entry

This action is used to retrieve a file catalog entry for a file given the file catalog ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_catalog_id|integer|None|True|File catalog ID for a file|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_catalog_entry|fileCatalog|False|File catalog entry for the file|

Example output:

```

{
  "id": 5025,
  "dateCreated": "2017-09-28T22:12:51.633Z",
  "pathName": "c:\\windows\\system32",
  "fileName": "mspaint.exe",
  "fileExtension": "exe",
  "md5": "4a6e008f312b6dd9c7f9149bbb6d7ef8",
  "sha1": "7ff26048a2469933a69af6200b114f24e18e8917",
  "sha256": "ea9c25f8226e393c188475bb0c748e753bacdec611b3deed1ff8ce6cd9a5bcf5",
  "sha256HashType": 5,
  "fileType": "Application",
  "fileSize": 6684672,
  "productName": "Microsoft Windows Operating System",
  "publisher": "",
  "company": "Microsoft Corporation",
  "publisherOrCompany": "Microsoft Corporation",
  "productVersion": "6.2.9200.16384",
  "trust": -1,
  "effectiveState": "Banned",
  "publisherState": 0,
  "approvedByReputation": false,
  "reputationEnabled": false,
  "reputationAvailable": false,
  "trustMessages": "",
  "threat": -2,
  "category": "Unknown",
  "prevalence": 1,
  "fileState": 3,
  "fileFlags": 421550082,
  "installedProgramName": "",
  "computerId": 1,
  "publisherId": 0,
  "certificateId": 0,
  "certificateState": 0
}

```

### Retrieve File Instance

This action retrieves a local file instance ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|computer_id|int|None|True|Name of the target computer for this file instance|None|
|file_catalog_id|integer|None|True|File catalog ID for a file|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_instance|[]file_catalog_entry_object|False|File instance|

Example output:

```
{
  "file_catalog_entry": [
    {
      "id": 7075,
      "fileInstanceGroupId": 3,
      "fileCatalogId": 5025,
      "computerId": 2,
      "policyId": 6,
      "dateCreated": "2019-04-24T20:14:00Z",
      "fileName": "mscorlib.resources.dll",
      "pathName": "c:\\program files\\microsoft silverlight\\5.1.50428.0\\sl",
      "executed": true,
      "localState": 2,
      "detailedLocalState": 4,
      "certificateId": 53,
      "initialized": true,
      "topLevel": false
    }
  ]
}
```

## Triggers

### New Approval Request

This trigger is used to trigger when a new approval request is created.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|poll_rate|integer|10|True|How often to poll for new approval requests, in seconds|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|approval_request|approvalRequest|False|The new approval request|

Example output:

```

{
  "requestorEmail": "john@smith.com",
  "createdByUserId": 6,
  "priority": 1,
  "fileName": "mspaint.exe",
  "installerFileCatalogId": 0,
  "policyId": 7,
  "createdBy": "WIN-M8DFE5GM8KZ\\Administrator",
  "modifiedByUserId": 6,
  "customRuleId": 19,
  "status": 1,
  "multipleBlocks": true,
  "enforcementLevel": 40,
  "computerId": 1,
  "computerName": "WORKGROUP\\WIN-M8DFE5GM8KO",
  "requestType": 1,
  "pathName": "c:\\windows\\system32",
  "fileCatalogId": 5025,
  "resolution": 0,
  "dateModified": "2017-10-04T22:22:00.387Z",
  "processFileCatalogId": 0,
  "dateCreated": "2017-10-04T22:22:00.387Z",
  "process": "c:\\windows\\explorer.exe",
  "id": 7,
  "requestorComments": "I would like to paint"
}

```

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Root Host URL|None|
|ssl_verify|boolean|True|True|True for Certificate Validation|None|
|api_key|credential_secret_key|None|True|API key|None|

## Troubleshooting

Carbon Black Protection schedules events to happen, therefore what you see in output may not be accurate as the Carbon Black Protection server may not yet have processed the event

## Workflows

Examples:

* Prevent malicious executables from running

## Versions

* 0.1.0 - Initial plugin
* 0.2.0 - Add Resolve Approval Request action
* 0.3.0 - Add trigger: New Approval Request
* 0.4.0 - Add action: Retrieve File Catalog Entry
* 0.4.1 - SSL bug fix in SDK
* 1.0.0 - Support web server mode | Update to new credential types
* 1.0.1 - Fix bug where SSL Verify option was passed incorrectly
* 1.0.2 - Fix Approve File Locally action request payload | Update to Python 3.7 Slim SDK (plugin size reduction)
* 1.1.0 - New action Retrieve File Instance
* 2.0.0 - Fix for Approve File Locally action | Fix for Unapprove File Locally action | Update to rename Unapprove Local Approval action to Unapprove File Locally
* 2.1.0 - Add Action: Create File Rule | Add Action: Get File Rule

## References

* [Carbon Black Protection REST API](https://developer.carbonblack.com/reference/enterprise-protection/7.2/rest-api/)

## Custom Output Types

### file_catalog_entry_object

|Name|Type|Required|Description|
|----|----|--------|-----------|
|certificateId|integer|False|Certificateid|
|computerId|integer|False|Computerid|
|dateCreated|string|False|Datecreated|
|detailedLocalState|integer|False|Detailedlocalstate|
|executed|boolean|False|Executed|
|fileCatalogId|integer|False|Filecatalogid|
|fileInstanceGroupId|integer|False|Fileinstancegroupid|
|fileName|string|False|Filename|
|id|integer|False|Id|
|initialized|boolean|False|Initialized|
|localState|integer|False|Localstate|
|pathName|string|False|Pathname|
|policyId|integer|False|Policyid|
|topLevel|boolean|False|Toplevel|

### approvalRequest

|Name|Type|Required|Description|
|----|----|--------|-----------|
|computerId|integer|False|Id of computer where Request Originated|
|computerName|string|False|Name of computer where Request Originated|
|customRuleId|integer|False|Id of customRule that Caused File Block|
|dateCreated|date|False|Datetime when Created (UTC)|
|dateModified|date|False|Datetime when Last Modified (UTC)|
|enforcementLevel|integer|False|Enforcement Level of Agent|
|fileCatalogId|integer|False|Id of fileCatalog Entry Associated with File|
|fileName|string|False|Name of file on Agent|
|id|integer|False|Unique approvalRequestId|
|installerFileCatalogId|integer|False|Id of fileCatalog Entry Associated with Installer|
|modifiedBy|string|False|User That Last Modified Request|
|multipleBlocks|boolean|False|True if File Referenced Had Multiple Blocks|
|pathName|string|False|Path of file on Agent|
|policyId|integer|False|Id of policy for Computer When Request Arrived|
|priority|integer|False|Priority of Request|
|process|string|False|Process that Attempted to Execute file on Agent|
|processFileCatalogId|integer|False|Id of fileCatalog Entry Associated with Process|
|requestType|integer|False|Type of Request|
|requestorComments|string|False|Comments by User that Created Request|
|requestorEmail|string|False|Email of User that Created Request|
|resolution|integer|False|Resolution of Request|
|resolutionComments|string|False|Comments by Request Resolver|
|status|integer|False|Request Status|

### certificate

|Name|Type|Required|Description|
|----|----|--------|-----------|
|certificateEffectiveState|integer|False|Effective State Taking into Account Other certificate in Chain|
|certificateState|integer|False|Assigned State|
|clVersion|integer|False|CL Version Associated with certificate|
|cosigner|boolean|False|True if certificate Was Seen Counter-Signing a File|
|dateCreated|date|False|Datetime certificate Was Created|
|dateModified|date|False|Datetime State or Description Was Modified|
|description|string|False|Description of Certificate Given by User|
|detached|boolean|False|True if certificate Was Seen as Detached Signer of File|
|embedded|boolean|False|True if certificate Was Seen as Embedded Signer of File|
|firstSeenComputerId|integer|False|Id of computer where Certificate First Seen|
|id|integer|False|Unique Certificate Id|
|intermediary|boolean|False|True if certificate is Intermediary Certificate in Chain|
|modifiedByUser|string|False|User that Last Modified State or Description|
|parentCertificateId|integer|False|Id of a Parent certificate in a Certificate Chain|
|publicKeyAlgorithm|string|False|Certificate Public Key Algorithm|
|publicKeySize|integer|False|Certificate Public Key Size in Bits|
|publisherId|integer|False|Id of publisher|
|serialNumber|string|False|Certificate Serial Number|
|signatureAlgorithm|string|False|Certificate Signature Algorithm|
|signer|boolean|False|True if certificate Was Seen Signing a File|
|sourceType|integer|False|Mechanism that Changed Publisher State|
|subjectName|string|False|Certificate Subject Name|
|thumbprint|string|False|Thumbprint Hash|
|thumbprintAlgorithm|string|False|Algorithm Used to Calculate Thumbprint|
|valid|boolean|False|True if certificate Valid|
|validFrom|date|False|Certificate Valid from Datetime|
|validTo|date|False|Certificate Valid to Datetime|

### computer

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CLIPassword|string|False|CLI Password for This computer|
|SCEPStatus|integer|False|Status of SCEP Protection|
|agentCacheSize|integer|False|Number of Files Agent Is Tracking|
|agentMemoryDumps|boolean|False|True if Agent Has Memory Dumps|
|agentQueueSize|integer|False|Number of Unsent File Operations in Agent Queue|
|agentVersion|string|False|Version of Cb Protection Platform Agent|
|automaticPolicy|boolean|False|True if policy Is Assigned Automatically Through AD|
|cbSensorFlags|integer|False|Carbon Black Sensor Flags|
|cbSensorId|integer|False|ID of Carbon Black Sensor|
|cbSensorVersion|string|False|Carbon Black Sensor Version|
|ccFlags|integer|False|Cache Consistency Check Flags Set for Agent|
|ccLevel|integer|False|Cache Consistency Check Level Set for Agent|
|clVersion|integer|False|Current CL Version|
|computerTag|string|False|Custom computer Tag|
|connected|boolean|False|True if computer Is Connected|
|dateCreated|date|False|Date computer Was First Registered|
|daysOffline|integer|False|Number of Days computer Was Offline|
|debugDuration|integer|False|Debug Duration in Minutes|
|debugFlags|integer|False|Debug Flags|
|debugLevel|integer|False|Current Debug Level of Agent|
|deleted|boolean|False|True if computer Is Disabled|
|description|string|False|Description of computer|
|disconnectedEnforcementLevel|integer|False|Current Enforcement Level for Disconnected computers|
|enforcementLevel|integer|False|Current Enforcement Level|
|forceUpgrade|boolean|False|True if Upgrade is Forced|
|hasHealthCheckErrors|boolean|False|True if computer Has Health Check Errors|
|id|integer|False|Unique computer Id|
|initializing|boolean|False|True if Agent is Initializing|
|ipAddress|string|False|Last Known IP|
|kernelDebugLevel|integer|False|Current Kernel Debug Level of Agent|
|lastPollDate|date|False|Last Datetime Contacted Server|
|lastRegisterDate|date|False|Last Datetime Registered to Server|
|localApproval|boolean|False|True if computer Is in Local Approval Mode|
|macAddress|string|False|MAC Address of Adapter Used to Connect to the CB Server|
|machineModel|string|False|None|
|memorySize|integer|False|None|
|name|string|False|Computer Name|
|osName|string|False|OS Name|
|osShortName|string|False|Short OS Name|
|platformId|integer|False|Platform Id|
|policyId|integer|False|Id of policy the computer Belongs to|
|policyName|string|False|Name of policy the computer Belongs to|
|policyStatusDetails|string|False|Detailed Status of Policy on Agent|
|prioritized|boolean|False|True if computer is Prioritized|
|processorCount|integer|False|Number of Processor Cores|
|processorModel|string|False|None|
|processorSpeed|number|False|None|
|refreshFlags|integer|False|Refresh Flags for Agent|
|supportedKernel|boolean|False|True if Current computer Kernel Version Supported|
|syncFlags|integer|False|Status of Synchronization on Agent|
|syncPercent|integer|False|Synchronization Percentage for File Operations|
|systemMemoryDumps|boolean|False|True if Agent has System Memory Dumps|
|tamperProtectionActive|boolean|False|True if Agent Tamper Protection Active|
|tdCount|integer|False|Count of Trusted Directories Hosted by Agent|
|template|boolean|False|True if computer Is Template|
|templateCLoneCleanupTime|integer|False|Time Unit Specified in templateCloneCleanupTimeScale|
|templateCloneCleanupMode|integer|False|None|
|templateCloneCleanupTimeScale|integer|False|1=hours,2=days,3=weeks|
|templateComputerId|integer|False|Id of Parent Template computer|
|templateDate|date|False|Datetime when computer Was Templated|
|templateTrackModsOnly|boolean|False|If True Clones of Template Will Track Only New and Modified Files|
|uninstalled|boolean|False|True if computer Was Uninstalled|
|upgradeError|string|False|Last Upgrade Error|
|upgradeErrorCount|integer|False|Number of Times Last Upgrade Error Occurred|
|upgradeErrorTime|date|False|Last Time Upgrade Error Changed|
|upgradeStatus|string|False|None|
|users|string|False|List of Last Logged in Users|
|virtualPlatform|string|False|Platform for Virtualization|
|virtualized|string|False|True if computer Is Virtualized|

### connector

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analysisEnabled|boolean|False|True if Analysis Component of connector is Enabled|
|analysisName|string|False|Name for Analysis Component of the connector|
|analysisTargets|[]string|False|Array of Possible Analysis Targets|
|canAnalyze|boolean|False|True if connector Can Analyze Files|
|connectorVersion|string|False|None|
|enabled|boolean|False|True if connector Is Enabled|
|id|integer|False|Unique connector Id|
|isInternal|boolean|False|True if This is Internal connector|
|name|string|False|Name of the connector|

### event

|Name|Type|Required|Description|
|----|----|--------|-----------|
|banName|string|False|None|
|commandLine|string|False|Full Command Line|
|computerId|integer|False|Id of computer Associated with event|
|computerName|string|False|Name of computer Associated with event|
|description|string|False|None|
|fileCatalogId|integer|False|Id of fileCatalog Entry Associated with File|
|fileName|string|False|None|
|id|integer|False|Unique event Id|
|indicatorName|string|False|None|
|installerFileCatalogId|integer|False|Id of fileCatalog Entry Associated with Installer|
|installerFileName|string|False|None|
|ipAddress|string|False|IP Address Associated with event|
|param1|string|False|Internal String Parameter|
|param2|string|False|Internal String Parameter|
|param3|string|False|Internal String Parameter|
|pathName|string|False|None|
|policyId|integer|False|Id of policy where Agent Was at Time of event|
|policyName|string|False|Name of policy where Agent Was at Time of event|
|processFileCatalogId|integer|False|Id of fileCatalog Entry Associated with Process|
|processFileName|string|False|None|
|processKey|string|False|Key to Uniquely Identify Process|
|processPathName|string|False|None|
|receivedTimestamp|date|False|Datetime When event Received by Server|
|ruleName|string|False|None|
|severity|integer|False|Event Severity|
|stringId|integer|False|Internal String Id Used for Description|
|subtype|integer|False|Event Subtype|
|subtypeName|string|False|Event subtype as string|
|timestamp|date|False|Datetime When event Created|
|type|integer|False|Event Type|
|updaterName|string|False|None|
|userName|string|False|None|

### fileAnalysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analysisResult|integer|False|None|
|analysisStatus|integer|False|None|
|analysisTarget|string|False|Connector-dependent|
|computerId|integer|False|Id of computer Entry Associated with Analysis|
|connectorId|integer|False|Id of connector Associated with Analysis|
|createdBy|string|False|User that Requested Analysis|
|dateCreated|date|False|Datetime when fileAnalysis Was Created (UTC)|
|dateModified|date|False|Datetime when fileAnalysis Was Last Modified (UTC)|
|fileCatalogId|integer|False|Id of fileCatalog Entry Associated with Analysis|
|fileName|string|False|Name of the File where File Exists on Endpoint|
|id|integer|False|Unique fileAnalysis Id|
|pathName|string|False|Name of the Path where File Exists on Endpoint|
|priority|integer|False|fileAnalysis Priority in range [-2,2], where 2 Is Highest Priority|

### fileCatalog

|Name|Type|Required|Description|
|----|----|--------|-----------|
|approvedByReputation|boolean|False|True if File Approved by Reputation|
|category|string|False|None|
|certificateId|integer|False|None|
|certificateState|integer|False|None|
|company|string|False|Name of Company Associiated with File in VERSIONINFO|
|computerId|integer|False|ID of computer where File First Seen|
|dateCreated|date|False|Datetime when Unique Hash First Seen (Database Local Time)|
|effectiveState|string|False|None|
|fileExtension|string|False|None|
|fileFlags|integer|False|None|
|fileName|string|False|None|
|fileSize|integer|False|Size in Bytes|
|fileState|integer|False|None|
|fileType|string|False|None|
|id|integer|False|Unique fileCatalog Id|
|installedProgramName|string|False|Name of Product Associated with File in MSI Package|
|md5|string|False|None|
|pathName|string|False|None|
|prevalence|integer|False|Number of Endpoints that Have This File|
|productName|string|False|Name of Product Associated with File in VERSIONINFO|
|productVersion|string|False|Version of File in VERSIONINFO|
|publisher|string|False|Subject Name of Certificate that Signed this File|
|publisherId|integer|False|None|
|publisherOrCompany|string|False|Publisher Name if Exists or Company Name from VERSIONINFO|
|publisherState|integer|False|None|
|reputationAvailable|boolean|False|True if Reputation Information Has Arrived|
|reputationEnabled|boolean|False|True if Reputation Approvals Are Enabled for File|
|sha1|string|False|None|
|sha256|string|False|None|
|sha256HashType|integer|False|5=regular,6=fuzzy|
|threat|integer|False|None|
|trust|integer|False|Trust of file (0-10), -1=unknown|
|trustMessages|string|False|More Details about Trust of File|

### fileInstance

|Name|Type|Required|Description|
|----|----|--------|-----------|
|computerId|integer|False|None|
|dateCreated|date|False|Datetime when File Was Created (UTC)|
|detachedCertificateId|integer|False|Id of Detached Certificate That Signed This File through the Catalog|
|detachedPublisherId|integer|False|Id of Detached Publisher That Signed This File through the Catalog|
|detailedLocalState|integer|False|None|
|executed|boolean|False|True if File Was Ever Executed on Agent|
|fileCatalogId|integer|False|None|
|fileInstanceGroupId|integer|False|None|
|fileName|string|False|None|
|id|integer|False|None|
|localState|integer|False|None|
|pathName|string|False|None|

### fileInstanceDeleted

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dateCreated|date|False|Datetime when File Was Created on Agent (UTC)|
|dateDeleted|date|False|Datetime when File Was Deleted (UTC)|
|detachedCertificateId|integer|False|None|
|detachedPublisherId|integer|False|None|
|fileCatalogId|integer|False|None|
|fileInstanceGroupId|integer|False|None|
|fileName|string|False|None|
|id|integer|False|None|
|pathName|string|False|None|

### fileInstanceGroup

|Name|Type|Required|Description|
|----|----|--------|-----------|
|computerId|integer|False|None|
|dateCreated|date|False|Datetime when File Was Created on Agent (UTC)|
|fileCatalogId|integer|False|None|
|fileName|string|False|None|
|groupType|integer|False|0=initialization,1=topLevel,2=process,3=MSI|
|id|integer|False|None|
|installedProgramName|string|False|User Associated with Group Creation on Agent|
|pathName|string|False|None|
|userName|string|False|User Associated with Group Creation on Agent|

### fileRule

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clVersion|integer|False|None|
|createdBy|string|False|User that Created Rule|
|dateCreated|date|False|Datetime when Rule Created (UTC)|
|dateModified|date|False|Datetime when Rule Last Modified (UTC)|
|description|string|False|None|
|fileCatalogId|integer|False|None|
|fileState|integer|False|1=unapproved,2=approved,3=banned|
|forceInstaller|boolean|False|True if File is Forced to Act as Installer, Even if Product Detected as Not Installer|
|forceNotInstaller|boolean|False|True if File is Forced to Act as Not Installer, Even if Product Detected as Installer|
|hash|string|False|Hash Only Available If Rule Created Through MD5 or SHA-1|
|id|integer|False|None|
|modifiedBy|string|False|User that Last Modified Rule|
|name|string|False|None|
|platformFlags|integer|False|1=Windows,2=Mac,3=Linux|
|policyIds|string|False|List of IDs of Policies where Rule Applies, 0 if Global|
|reportOnly|boolean|False|True if this Has a Report-Only Ban|
|reputationApprovalsEnabled|boolean|False|True if Reputation Approvals Are Enabled|
|sourceId|integer|False|Can Be Event Rule ID or Trusted Directory ID|
|sourceType|integer|False|Mechanism that Created Rule|

### fileUpload

|Name|Type|Required|Description|
|----|----|--------|-----------|
|computerId|integer|False|None|
|createdBy|string|False|User that Requested Upload|
|dateCreated|date|False|Datetime when Upload Requested (UTC)|
|dateModified|date|False|Datetime when Upload Last Modified by System (UTC)|
|fileCatalogId|integer|False|None|
|fileName|string|False|None|
|id|integer|False|None|
|pathName|string|False|None|
|priority|integer|False|Upload Priority in Range [-2,2], where 2 Is Highest Priority|
|uploadPath|string|False|Local Upload Path for File on Server. File IS Compressed in ZIP|
|uploadStatus|integer|False|None|
|uploadedFileSize|integer|False|Will Be 0 unless uploadStatus=3|

### internalEvent

|Name|Type|Required|Description|
|----|----|--------|-----------|
|banName|string|False|None|
|commandLine|string|False|Full Command Line|
|computerId|integer|False|Id of computer Associated with event|
|computerName|string|False|Name of computer Associated with event|
|description|string|False|None|
|fileCatalogId|integer|False|Id of fileCatalog Entry Associated with File|
|fileName|string|False|None|
|id|integer|False|Unique event Id|
|indicatorName|string|False|None|
|installerFileCatalogId|integer|False|Id of fileCatalog Entry Associated with Installer|
|installerFileName|string|False|None|
|ipAddress|string|False|IP Address Associated with event|
|param1|string|False|Internal String Parameter|
|param2|string|False|Internal String Parameter|
|param3|string|False|Internal String Parameter|
|pathName|string|False|None|
|policyId|integer|False|Id of policy where Agent Was at Time of event|
|policyName|string|False|Name of policy where Agent Was at Time of event|
|processFileCatalogId|integer|False|Id of fileCatalog Entry Associated with Process|
|processFileName|string|False|None|
|processKey|string|False|Key to Uniquely Identify Process|
|processPathName|string|False|None|
|receivedTimestamp|date|False|Datetime When event Received by Server|
|ruleName|string|False|None|
|severity|integer|False|Event Severity|
|stringId|integer|False|Internal String Id Used for Description|
|subtype|integer|False|Event Subtype|
|subtypeName|string|False|Event subtype as string|
|timestamp|date|False|Datetime When event Created|
|type|integer|False|Event Type|
|updaterName|string|False|None|
|userName|string|False|None|

### meteredExecution

|Name|Type|Required|Description|
|----|----|--------|-----------|
|computerId|integer|False|None|
|data|string|False|Data from Definition of Meter|
|description|string|False|Description of Meter Associated with Execution|
|eventId|integer|False|None|
|fileCatalogId|integer|False|None|
|id|integer|False|None|
|meterId|integer|False|Id of Meter Associated with this Execution|
|name|string|False|Name of Meter Associated with Execution|
|timestamp|date|False|Datetime Associated with this Execution|
|type|integer|False|None|
|userName|string|False|User Name Associated with this Execution|

### notifier

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bgImageLocation|string|False|Background Image of Notifier Dialog|
|clVersion|integer|False|None|
|createdBy|string|False|None|
|dateCreated|date|False|Datetime when Created (UTC)|
|dateModified|date|False|Datetime when Last Modified (UTC)|
|defaultRuleGroupId|integer|False|None|
|defaultRuleType|integer|False|Default customRule Type for this Notifier|
|eventLogText|string|False|None|
|fgImageLocation|string|False|Foreground Image of Notifier Dialog|
|flags|integer|False|1=showApprovalRequestFields,2=showJustificationFields|
|id|integer|False|None|
|logoUrl|string|False|URL to the Logo Image|
|messageText|string|False|Full Message Text Appearing in Notifier Dialog|
|modifiedBy|string|False|None|
|name|string|False|None|
|showLogo|boolean|False|True to Show Logo on Dialog|
|systemNotifier|boolean|False|True if System Notifier|
|timeout|integer|False|Timeout of Notifier in Seconds|
|title|string|False|Notifier Dialog Title|
|url|string|False|None|
|usageCount|integer|False|Number of customRule Objects that Reference this Notifier|

### pendingAnalysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analysisError|string|False|None|
|analysisResult|integer|False|0=NA,1=clean,2=potentialThreat,3=malicious|
|analysisStatus|integer|False|None|
|analysisTarget|string|False|None|
|connectorId|integer|False|None|
|createdBy|string|False|None|
|dateCreated|date|False|Datetime when fileAnalysis Created (UTC)|
|dateModified|date|False|Datetime when fileAnalysis Last Modified (UTC)|
|fileCatalogId|integer|False|None|
|fileName|string|False|None|
|id|integer|False|None|
|md5|string|False|None|
|pathName|string|False|None|
|priority|integer|False|None|
|sha1|string|False|None|
|sha256|string|False|None|
|uplaoded|boolean|False|True if File is Available|
|uploadPath|string|False|Local Upload Path for File on Server. File is Compressed in ZIP|
|uploadedFileSize|integer|False|Will be 0 of analysisStatus is 0|

### policy

|Name|Type|Required|Description|
|----|----|--------|-----------|
|allowAgentUpgrades|boolean|False|True if Agents Can Be Upgraded|
|automatic|boolean|False|True if AD Mapping Enabled|
|automaticApprovalsOnTransition|boolean|False|True if Agents Automatically Locally Approve Files when Transitioning into High Enforcement|
|clVersionMax|integer|False|Max Target CL Version for Agents|
|customLogo|boolean|False|True if Notifiers Use Custom Logo|
|dateCreated|date|False|Datetime when Policy was Created (UTC)|
|dateModified|date|False|Datetime when Policy was Last Modified (UTC)|
|description|string|False|None|
|disconnectedEnforcementLevel|integer|False|None|
|enforcementLevel|integer|False|None|
|fileTrackingEnabled|boolean|False|True if File Tracking Enabled|
|helpDeskUrl|string|False|Helpdesk URL for Notifiers in this Policy|
|hidden|boolean|False|True if Policy Hidden in UI|
|id|integer|False|None|
|imageUrl|string|False|Image Logo URL for Notifiers in this Policy|
|loadAgentInSafeMode|boolean|False|True if Agents Will Be Loaded when Machine Booted in Safe Mode|
|name|string|False|None|
|packageName|string|False|None|
|readOnly|boolean|False|True if Read-Only|
|reputationEnabled|boolean|False|True if Reputation Approvals Enabled|

### publisher

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clVersion|integer|False|None|
|dateCreated|date|False|Datetime when Publisher First Seen (UTC)|
|dateModified|date|False|Datetime when Publisher Last Modified (UTC)|
|description|string|False|None|
|firstSeenComputerId|integer|False|Id of computer where Publisher Was First Seen|
|hidden|boolean|False|True if Not Seen on Enpoints or Modified Yet|
|id|integer|False|None|
|modifiedBy|string|False|None|
|name|string|False|None|
|platformFlags|integer|False|Flags where Publisher Will Be Approved/Banned, 1=windows,2=mac,4=linux|
|policyIds|string|False|List of IDs of Policies where Rule Applies, Empty if Global|
|publisherReputation|integer|False|0=notTrusted,1=low,2=medium,3=high|
|publisherState|integer|False|1=unapproved,2=approved,3=banned|
|reputationApprovalsEnabled|boolean|False|True if Publisher Can Be Approved by Reputation|
|signedCertificateCount|integer|False|None|
|signedFilesCount|integer|False|None|
|sourceType|integer|False|1=manual,3=reputation,5=external(API)|

### serverConfig

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dateModified|date|False|Datetime when Property was Last Modified (UTC)|
|id|integer|False|None|
|modifiedBy|string|False|None|
|name|string|False|None|
|value|string|False|None|

### serverPerformance

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agentFileBacklog|integer|False|Size of All Agent File Change Queues|
|agentProcessingRate|integer|False|Daily Processing Rate from Agent Queue|
|avgDiskDataReadStallMs|number|False|None|
|avgDiskDataWriteStallMs|number|False|None|
|avgDiskIndexWriteStallMs|number|False|None|
|avgDiskLogWriteStallMs|number|False|None|
|connectedAgents|integer|False|Average Number of Connected Agents|
|dateCreated|date|False|Datetime of Entry (UTC)|
|diskDataIOPS|number|False|None|
|diskDataRead|integer|False|Disk Data File Read Rate in B/second|
|diskDataWrite|integer|False|Disk Data File Write Rate in B/second|
|diskIndexIOPS|number|False|None|
|diskIndexRead|integer|False|Disk Index File Read Rate in B/second|
|diskIndexWrite|integer|False|Disk Index File Write Rate in B/second|
|diskLogIOPS|number|False|None|
|diskLogWrite|integer|False|Disk Log File Write Rate in B/second|
|id|integer|False|Id of Entry. Id Is Ordinal and Cannot be Persisted|
|serverFileBacklog|integer|False|Size of Server File Backlog|
|serverFiles|integer|False|Toatl Number of Inventory Files Server Is Tracking|
|serverProcessingRate|integer|False|Daily Processing Rate of Agent File Changes|
|sqlInsertLatencyMs|number|False|Average Network Latency between CB Protection Server and SQL Server when Inserting Data|
|sqlLatencyMs|number|False|Average Network Latency between CB Protection Server and SQL Server|
|sqlMemoryPressure|number|False|Memory Pressure of SQL Server in % of Maximum Recommended Value|

### updater

|Name|Type|Required|Description|
|----|----|--------|-----------|
|clVersion|integer|False|None|
|createdBy|string|False|None|
|dateCreated|date|False|Datetime when Created (UTC)|
|dateModified|date|False|Datetime when Last Modified (UTC)|
|enabled|boolean|False|None|
|id|integer|False|None|
|modifiedBy|string|False|None|
|name|string|False|None|
|platformFlags|integer|False|1=windows,2=mac,4=linux|
|version|string|False|None|