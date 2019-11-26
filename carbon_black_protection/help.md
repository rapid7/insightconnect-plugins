# Description

[Carbon Black Protection](https://www.carbonblack.com/products/cb-protection/) allows users to lock down and harden systems to prevent malware, ransomware, and more. The InsigthConnect plugin can ban and unban files, as well as manage approval requests.

This plugin utilizes the [Carbon Black Protection API](https://developer.carbonblack.com/reference/enterprise-protection/7.2/rest-api/).

# Key Features

* Ban and unban files
* Approve files
* Resolve approval requests

# Requirements

* Requires an API Key from Carbon Black Protection

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Root Host URL|None|
|ssl_verify|boolean|True|True|True for Certificate Validation|None|
|api_key|credential_secret_key|None|True|API key|None|

## Technical Details

### Actions

#### Unban File

This action is used to unban a file globally or by policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_ids|[]integer|None|False|List of policy IDs. Only fill in this field if ban is by policy|None|
|hash|string|None|True|Hash for file to unban|None|
|new_state|string|Approved|True|New state of the file. Either approved or unapproved|['Approved', 'Unapproved']|
|method|string|Globally|True|Unban globally or by policy|['Globally', 'Policy']|

##### Output

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

#### Ban File

This action is used to ban a file globally or by policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy_ids|[]integer|None|False|List of policy IDs. Only fill in this field if ban is by policy|None|
|hash|string|None|True|Hash for file to ban|None|
|method|string|Globally|True|Ban globally or by policy|['Globally', 'Policy']|

##### Output

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

#### Approve File Locally

This action is used to approve a file locally.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|integer|None|True|File ID of file to approve locally|None|

##### Output

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

#### Unapprove File Locally

This action is used to remove local approval for a file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|integer|None|True|File ID of file to remove local approval for|None|

##### Output

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

#### Create File Rule

This action creates a file rule, this allows for the creation and editing of file Approvals and Bans.

##### Input

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

##### Output

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

#### Get Approval Request

This action is used to get an Approval Request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|approval_request_id|integer|None|True|Approval Request ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|approval_request|object|False|Approval Request|

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

#### Get File Rule

This action is used to get a File Rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_rule_id|integer|None|True|File rule ID|None|

##### Output

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

#### Resolve Approval Request

This action is used to resolve approval requests with a desired status.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|approval_request_id|string|None|True|Resolve an approval request with the desired status|None|
|resolution|string|Not Resolved|True|Method for resolving the approval request|['Not Resolved', 'Rejected', 'Resolved - Approved', 'Resolved - Rule Change', 'Resolved - Installer', 'Resolved - Updater', 'Resolved - Publisher', 'Resolved - Other']|

##### Output

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

#### Retrieve File Catalog Entry

This action is used to retrieve a file catalog entry for a file given the file catalog ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_catalog_id|integer|None|True|File catalog ID for a file|None|

##### Output

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

#### Retrieve File Instance

This action retrieves a local file instance ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|computer_id|int|None|True|Name of the target computer for this file instance|None|
|file_catalog_id|integer|None|True|File catalog ID for a file|None|

##### Output

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

### Triggers

#### New Approval Request

This trigger is used to trigger when a new approval request is created.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|poll_rate|integer|10|True|How often to poll for new approval requests, in seconds|None|

##### Output

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

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Carbon Black Protection schedules events to happen, therefore what you see in output may not be accurate as the Carbon Black Protection server may not yet have processed the event

# Version History

* 2.2.2 - New spec and help.md format for the Hub
* 2.2.1 - New spec and help.md format for the Hub
* 2.2.0 - Update to add Status to Resolve Approval Request | New action Get Approval Reqeust
* 2.1.0 - Add Action: Create File Rule | Add Action: Get File Rule
* 2.0.0 - Fix for Approve File Locally action | Fix for Unapprove File Locally action | Update to rename Unapprove Local Approval action to Unapprove File Locally
* 1.1.0 - New action Retrieve File Instance
* 1.0.2 - Fix Approve File Locally action request payload | Update to Python 3.7 Slim SDK (plugin size reduction)
* 1.0.1 - Fix bug where SSL Verify option was passed incorrectly
* 1.0.0 - Support web server mode | Update to new credential types
* 0.4.1 - SSL bug fix in SDK
* 0.4.0 - Add action: Retrieve File Catalog Entry
* 0.3.0 - Add trigger: New Approval Request
* 0.2.0 - Add Resolve Approval Request action
* 0.1.0 - Initial plugin

# Links

## References

* [Carbon Black Protection REST API](https://developer.carbonblack.com/reference/enterprise-protection/7.2/rest-api/)

