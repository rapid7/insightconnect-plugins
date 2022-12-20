# Description

CrowdStrike Falcon Intelligence is used to automatically investigate incidents and accelerate alert triage and response. Built into the Falcon Platform, it is operational in seconds.

# Key Features

* Get full or short report
* Submit file for analysis
* Check analysis status
* Get submissions ids
* Get reports ids

# Requirements

The following information are required for using this plugin:
* URL of your Crowdstrike Platform instance
* Client ID
* Client Secret

# Supported Product Versions

* 2022-11-28 Crowdstrike API v2

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|baseUrl|string|https://example.com|True|The Base URL provided in the API Clients and Keys settings|None|https://example.com|
|clientId|string|None|True|CrowdStrike Client ID|None|eXaMpl3Cli3ntID|
|clientSecret|credential_secret_key|None|True|CrowdStrike Secret Key|None|eXaMpl3S3cr3tK3Y|

Example input:

```
{
  "baseUrl": "https://api.crowdstrike.com",
  "clientId": "eXaMpl3Cli3ntID",
  "clientSecret": "eXaMpl3S3cr3tK3Y"
}
```

## Technical Details

### Actions

#### Get Submissions IDs

This action is used to find submissions IDs for uploaded files by providing an FQL filter and paging details. Returns a set of submission IDs that match your criteria.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|string|None|False|Filter and sort criteria in the form of an FQL query. For more information about FQL queries, see https://falcon.crowdstrike.com/documentation/45/falcon-query-language-fql|None|state: 'running'|
|limit|integer|None|False|Maximum number of report IDs to return - less or equal to 5000|None|324|
|offset|integer|None|False|The offset to start retrieving reports from|None|5|

Example input:

```
{
  "filter": "state: 'running'",
  "limit": 324,
  "offset": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-----|
|submissionIds|[]string|True|List of submission IDs|["9382986b58cb4b44935e7eba071142f3_92c8b7525e2b4888bd9e2jj7391c7104"]|

Example output:

```
{
  "submissionIds": [
    "9382986b58cb4b44935c2eba079842f3_0a54f7a33701461299899f294c2eb53d",
    "9382986b58cb4b44935c2eba079842f3_a17b8037186f4c8a9129d88b9d40fc9d",
    "9382986b58cb4b44935c2eba079842f3_11f08e0a490d4bc9912a7375af4664bc",
  ]
}
```

#### Get Reports IDs

This action is used to find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs that match your criteria.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|string|None|False|Filter and sort criteria in the form of an FQL query. For more information about FQL queries, see https://falcon.crowdstrike.com/documentation/45/falcon-query-language-fql|None|verdict: 'no verdict'|
|limit|integer|None|False|Maximum number of report IDs to return - less or equal to 5000|None|324|
|offset|integer|None|False|The offset to start retrieving reports from|None|5|

Example input:

```
{
  "filter": "verdict: 'no verdict'",
  "limit": 324,
  "offset": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-----|
|reportIds|[]string|True|List of report IDs|["9382986b58cb4b44935e7eba071142f3_92c8b7525e2b4888bd9e2jj7391c7104"]|

Example output:

```
{
  "reportIds": [
    "9de5069c5afe602b2ea0a04b612eb2c0_9de5069c5afe602b2bb0a04b66beb2c0",
    "9de5069c5afe602b2ea0a04b612eb2c0_9de5069c5afe602b2bb0a04b66beb2c0",
  ]
}
```

#### Check Analysis Status

This action is used to check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ids|[]string|None|True|List of submitted malware samples ids. Find a submission ID from the response when submitting a malware sample or search with `Get Submissions IDs` action|None|Md29sKvzxiddHJ0k3qnC8iDyhfZ3UZrFqOSSdKn3NhLrQR4eCsvQvOesmuXX5pra|

Example input:

```
{
  "ids": "Md29sKvzxiddHJ0k3qnC8iDyhfZ3UZrFqOSSdKn3NhLrQR4eCsvQvOesmuXX5pra"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-----|
|submissions|[]submission|True|List of submissions|[]|

Example output:

```
{
  "submissions": [
    {
      "id": "9382986b58cb4b44935e7eba079842f3_7c6d4bf5ab0c4459b855aaa345f4bcf9",
      "cid": "9382986b58cb4b44935e7eba079842f3",
      "userId": "3e7da174cb6944e8a4cd8a5a59a76727",
      "userName": "user@example.com",
      "userUuid": "a149764d-21ee-42af-ac9f-023f5d23ab81",
      "origin": "uiproxy",
      "state": "error",
      "createdTimestamp": "2022-08-30T09:25:35Z",
      "sandbox": [
        {
          "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
          "environmentId": 300,
          "submitName": "action.py"
        }
      ]
    },
    {
      "id": "9382986b58cb4b44935e7eba079842f3_63aca0772bf342648b2a8779c7bfcadd",
      "cid": "9382986b58cb4b44935e7eba079842f3",
      "userId": "3e7da174cb6944e8a4cd8a5a59a76727",
      "userName": "user@example.com",
      "userUuid": "a149764d-21ee-42af-ac9f-023f5d23ab81",
      "origin": "uiproxy",
      "state": "error",
      "createdTimestamp": "2022-08-30T09:21:00Z",
      "sandbox": [
        {
          "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
          "environmentId": 100,
          "submitName": "Archive.zip"
        }
      ]
    }
  ]
}
```

#### Download Artifact

This action is used to download IOC packs, PCAP files, memory dumps, and other analysis artifacts. Find an artifact ID with `Get Full Report` action

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|ID of an JSON artifact, such as an IOC pack, PCAP file, memory dump, or actor image. Find an artifact ID with `Get Full Report` action|None|Md29sKvzxiddHJ0k3qnC8iDyhfZ3UZrFqOSSdKn3NhLrQR4eCsvQvOesmuXX5pra|

Example input:

```
{
  "id": "Md29sKvzxiddHJ0k3qnC8iDyhfZ3UZrFqOSSdKn3NhLrQR4eCsvQvOesmuXX5pra"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-----|
|artifacts|[]artifact|True|List of artifacts|[]|

Example output:

```
{
  "artifacts": [
    {
      "ioc": "44d88612fea8a8f36de82e1278abb02f",
      "source": "extracted",
      "type": "md5"
    },
    {
      "ioc": "44d88612fea8a8f36de82e1278abb02f",
      "source": "extracted",
      "type": "md5"
    },
    {
      "ioc": "44d88612fea8a8f36de82e1278abb02f",
      "source": "extracted",
      "type": "md5"
    },
    {
      "ioc": "44d88612fea8a8f36de82e1278abb02f",
      "source": "extracted",
      "type": "md5"
    },
    {
      "ioc": "3395856ce81f2b7382dee72602f798b642f14140",
      "source": "extracted",
      "type": "sha1"
    },
    {
      "ioc": "3395856ce81f2b7382dee72602f798b642f14140",
      "source": "extracted",
      "type": "sha1"
    },
    {
      "ioc": "3395856ce81f2b7382dee72602f798b642f14140",
      "source": "extracted",
      "type": "sha1"
    },
    {
      "ioc": "3395856ce81f2b7382dee72602f798b642f14140",
      "source": "extracted",
      "type": "sha1"
    },
    {
      "ioc": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "source": "extracted",
      "type": "sha256"
    },
    {
      "ioc": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "source": "extracted",
      "type": "sha256"
    },
    {
      "ioc": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "source": "extracted",
      "type": "sha256"
    },
    {
      "ioc": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "source": "extracted",
      "type": "sha256"
    },
    {
      "ioc": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "source": "input",
      "type": "sha256"
    },
    {
      "ioc": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "source": "runtime",
      "type": "sha256"
    },
    {
      "ioc": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "source": "runtime",
      "type": "sha256"
    }
  ]
}
```

#### Get Full Report

This action is used to get a full sandbox report.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ids|[]string|None|True|List of summary IDs. Find a summary ID from the response when submitting a malware sample or search with `Get Reports IDs` action|None|["9de5069c5afe602b2ea0a11b66beb2c0_9aa5069c5afe602b2ea0a04b66beb2c0"]|

Example input:

```
{
  "ids": [
    "9de5069c5afe602b2ea0a11b66beb2c0_9aa5069c5afe602b2ea0a04b66beb2c0"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-----|
|reports|[]report|True|List of sandbox reports|[]|

Example output:

```
{
  "reports": [
    {
      "id": "9de5069c5afe602b2ea0a11b66beb2c0_9aa5069c5afe602b2ea0a04b66beb2c0",
      "cid": "9de5069c5afe602b2ea0a11b66beb2c0",
      "created_timestamp": "2022-11-30T14:09:35Z",
      "origin": "apigateway",
      "verdict": "whitelisted",
      "sandbox": [
        {
          "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
          "environment_id": 100,
          "environment_description": "Windows 7 32 bit",
          "file_type": "data",
          "file_type_short": [
            "data"
          ],
          "submit_name": "Test Analysis",
          "submission_type": "file",
          "error_message": "File \"Test Analysis\" was detected as \"raw data\", this format is not supported on WINDOWS",
          "error_type": "FILE_TYPE_BAD_ERROR",
          "error_origin": "CLIENT"
        }
      ]
    }
  ]
}
```

#### Get Short Report

This action is used to get a short summary version of a sandbox report.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ids|[]string|None|True|List of summary IDs. Find a summary ID from the response when submitting a malware sample or search with `Get Reports IDs` action|None|["9382986b58cb4bb4935e7eba079842f3_d1ce821d74484545897f2fd5db40d0a7"]|

Example input:

```
{
  "ids": [
    "9382986b58cb4bb4935e7eba079842f3_d1ce821d74484545897f2fd5db40d0a7"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-----|
|reports|[]reportShort|True|List of short sandbox reports|[]|

Example output:

```
{
  "reports": [
    {
      "cid": "9382986b58cb4bb4935e7eba079842f3",
      "createdTimestamp": "2022-09-28T07:45:34Z",
      "id": "9382986b58cb4bb4935e7eba079842f3_d1ce821d74484545897f2fd5db40d0a7",
      "origin": "uiproxy",
      "sandbox": [
        {
          "environmentDescription": "Windows 7 32 bit",
          "environmentId": 100,
          "errorMessage": "The file \"Dockerfile\" has the file format \"text\", which is not supported",
          "errorOrigin": "CLIENT",
          "errorType": "FILE_TYPE_BAD_ERROR",
          "fileType": "ASCII text",
          "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
          "submissionType": "file",
          "submitName": "Dockerfile"
        }
      ],
      "userId": "9de5069c5afe602b2ea0a04b66beb2c0",
      "userName": "https://example.com",
      "verdict": "no verdict"
    }
  ]
}
```

#### Submit Analysis

This action is used to submit an uploaded file or a URL for sandbox analysis. Time required for analysis varies but is usually less than 15 minutes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|actionScript|string|None|False|Runtime script for sandbox analysis|['default', 'default_maxantievasion', 'default_randomfiles', 'default_randomtheme', 'default_openie', '']|default_openie|
|commandLine|string|None|False|Command line script passed to the submitted file at runtime. Max length is 2048 characters|None|/example /command|
|documentPassword|password|None|False|Auto-filled for Adobe or Office files that prompt for a password. Max length is 32 characters|None|3xamp13Pa55w0rd|
|environmentId|integer|None|True|Specifies the sandbox environment used for analysis. Example values 300 - Linux Ubuntu 16.04, 64-bit; 200 - Android (static analysis); 160 - Windows 10, 64-bit; 110 - Windows 7, 64-bit; 100 - Windows 7, 32-bit|[100, 110, 160, 200, 300]|110|
|networkSettings|string|None|False|Specifies the sandbox network_settings used for analysis|['default', 'tor', 'simulated', 'offline', '']|tor|
|submitName|string|None|False|Name of the malware sample that's used for file type detection and analysis|None|my_sample|
|sha256|string|None|False|ID of the sample, which is a SHA256 hash value. Find a sample ID from the response when uploading a malware sample or search with `Get Submissions IDs` action. The `url` parameter must be unset if `sha256` is used|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|url|string|None|False|A web page or file URL. It can be HTTP(S) or FTP. The `SHA256` parameter must be unset if `url` is used|None|https://www.example.com/images/default/sample.pdf|
|systemDateTime|date|None|False|System date and time|None|2022-11-01 00:00:00+02:00|

Example input:

```
{
  "actionScript": "default_openie",
  "commandLine": "/example /command",
  "documentPassword": "3xamp13Pa55w0rd",
  "environmentId": 110,
  "networkSettings": "tor",
  "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "submitName": "my_sample",
  "systemDateTime": "2022-11-01T00:00:00+02:00",
  "url": "https://www.example.com/images/default/sample.pdf"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-----|
|submission|submission|True|Submission|{}|

Example output:

```
{
  "submission": {
    "cid": "9de5069c5mne602b2ea0a04b66beb2c0",
    "createdTimestamp": "2022-11-22T06:10:42Z",
    "id": "9de5069c5mne602b2ea0a04b66beb2c0_8de5069c5afe602b2ea0a04b66beb2c0",
    "origin": "apigateway",
    "sandbox": [
      {
        "actionScript": "default_openie",
        "environmentId": 110,
        "networkSettings": "tor",
        "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
        "submitName": "my_sample",
        "systemDate": "2022-12-22",
        "systemTime": "17:33"
      }
    ],
    "state": "created"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IOC|string|False|IOC|
|Source|string|False|Source|
|Type|string|False|Type|

#### extractedFiles

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|File Path|string|False|File path|
|File Size|integer|False|File size|
|MD5|string|False|MD5|
|Runtime Process|string|False|Runtime process|
|SHA1|string|False|SHA1|
|SHA256|string|False|SHA256|
|Threat Level Readable|string|False|Threat level readable|
|Type Tags|[]string|False|Type tags|

#### extractedInterestingStrings

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Process|string|False|Process|
|Source|string|False|Source|
|Type|string|False|Type|
|Value|string|False|Value|

#### fileAccess

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Mask|string|False|Mask|
|Path|string|False|Path|
|Type|string|False|Type|

#### handle

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|ID|
|Path|string|False|Path|
|Type|string|False|Type|

#### malquery

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Input|string|False|Input|
|Type|string|False|Type|
|Verdict|string|False|Verdict|

#### process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Command Line|string|False|Command line|
|File Accesses|[]fileAccess|False|File accesses|
|Handles|[]handle|False|Handles|
|Icon Artifact ID|string|False|Icon artifact ID|
|Mutants|[]string|False|Mutants|
|Normalized Path|string|False|Normalized path|
|PID|integer|False|PID|
|Registry|[]registry|False|Registry|
|SHA256|string|False|SHA256|
|UID|string|False|UID|

#### registry

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Key|string|False|Key|
|Operation|string|False|Operation|
|Path|string|False|Path|
|Status|string|False|Status|
|Status Human Readable|string|False|Status human readable|

#### report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CID|string|False|CID of the report|
|Created Timestamp|date|False|Time when the report was created|
|ID|string|False|ID of the report|
|IOC Report Broad CSV Artifact ID|string|False|IOC report broad CSV artifact ID|
|IOC Report Broad JSON Artifact ID|string|False|IOC report broad JSON artifact ID|
|IOC Report Broad Maec Artifact ID|string|False|IOC report broad maec artifact ID|
|IOC Report Broad STIX Artifact ID|string|False|IOC report broad STIX artifact ID|
|IOC Report Strict CSV Artifact ID|string|False|IOC report strict CSV artifact ID|
|IOC Report Strict JSON Artifact ID|string|False|IOC report strict JSON artifact ID|
|IOC Report Strict Maec Artifact ID|string|False|IOC report strict maec artifact ID|
|IOC Report Strict STIX Artifact ID|string|False|IOC report strict STIX artifact ID|
|Malquery|[]malquery|False|Malquery|
|Origin|string|False|Origin|
|Sandbox|[]sandbox|False|Sandbox details|
|User ID|string|False|ID of the user|
|User Name|string|False|Name of the user|
|User UUID|string|False|UUID of the user|
|Verdict|string|False|Verdict of the report|

#### reportShort

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CID|string|False|CID of the report|
|Created Timestamp|date|False|Time when the report was created|
|ID|string|False|ID of the report|
|IOC Report Broad CSV Artifact ID|string|False|IOC report broad CSV artifact ID|
|IOC Report Broad JSON Artifact ID|string|False|IOC report broad JSON artifact ID|
|IOC Report Broad Maec Artifact ID|string|False|IOC report broad maec artifact ID|
|IOC Report Broad STIX Artifact ID|string|False|IOC report broad STIX artifact ID|
|IOC Report Strict CSV Artifact ID|string|False|IOC report strict CSV artifact ID|
|IOC Report Strict JSON Artifact ID|string|False|IOC report strict JSON artifact ID|
|IOC Report Strict Maec Artifact ID|string|False|IOC report strict maec artifact ID|
|IOC Report Strict STIX Artifact ID|string|False|IOC report strict STIX artifact ID|
|Origin|string|False|Origin|
|Sandbox|[]sandboxShort|False|Sandbox details|
|User ID|string|False|ID of the user|
|User Name|string|False|Name of the user|
|Verdict|string|False|Verdict of the report|

#### sandbox

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Architecture|string|False|Architecture|
|Environment Description|string|False|Environment description|
|Environment ID|integer|False|Environment ID|
|Error Message|string|False|Error message|
|Error Origin|string|False|Error origin|
|Error Type|string|False|Error type|
|Extracted Files|[]extractedFiles|False|Extracted files|
|Extracted Interesting Strings|[]extractedInterestingStrings|False|Extracted interesting strings|
|File Size|integer|False|File size|
|File Type|string|False|File type|
|File Type Short|[]string|False|File type short|
|Memory Dumps Artifact ID|string|False|Memory dumps artifact ID|
|Memory Strings Artifact ID|string|False|Memory strings artifact ID|
|Network Settings|string|False|Network settings|
|PCAP Report Artifact ID|string|False|PCAP report artifact ID|
|Processes|[]process|False|Processes|
|Sample Flags|[]string|False|Sample flags|
|Screenshots Artifact IDs|[]string|False|Screenshots artifact IDs|
|SHA256|string|False|SHA256|
|Signatures|[]signature|False|Signatures|
|Submission Type|string|False|Submission type|
|Submit Name|string|False|Submit name|
|Submit URL|string|False|Submit URL|
|Verdict|string|False|Verdict|
|Windows Version Bitness|integer|False|Windows version bitness|
|Windows Version Edition|string|False|Windows version edition|
|Windows Version Name|string|False|Windows version name|
|Windows Version Service Pack|string|False|Windows version service pack|
|Windows Version Version|string|False|Windows version version|

#### sandboxShort

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action Script|string|False|Action script|
|Document Password|string|False|Document password|
|Environment Description|string|False|Environment description|
|Environment ID|integer|False|Environment ID|
|Error Message|string|False|Error message|
|Error Origin|string|False|Error origin|
|Error Type|string|False|Error type|
|File Type|string|False|File type|
|Network Settings|string|False|Network settings|
|Sample Flags|[]string|False|Sample flags|
|SHA256|string|False|SHA256|
|Submission Type|string|False|Submission type|
|Submit Name|string|False|Submit name|
|Submit URL|string|False|Submit URL|
|System Date|string|False|System date|
|System Time|string|False|System time|
|URL|string|False|URL|
|Verdict|string|False|Verdict|

#### signature

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Category|string|False|Category|
|Description|string|False|Description|
|Identifier|string|False|Identifier|
|Origin|string|False|Origin|
|Relevance|integer|False|Relevance|
|Threat Level Human|string|False|Threat level human|
|Type|integer|False|Type|

#### submission

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Cid|string|False|Cid|
|Created Timestamp|string|False|Created timestamp|
|ID|string|False|ID|
|Origin|string|False|Origin|
|Sandbox|[]sandboxShort|False|Sandbox|
|State|string|False|State|
|User ID|string|False|User ID|
|User Name|string|False|User name|
|User Tags|[]string|False|User Tags|
|User UUID|string|False|User UUID|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin | Check Analysis Status, Download Artifact, Get Full Report, Get Reports IDs, Get Short Report, Get Submissions IDs, Submit Analysis

# Links

* [CrowdStrike Falcon Intelligence](https://www.crowdstrike.com/products/threat-intelligence/falcon-intelligence-automated-intelligence/)

## References

* [CrowdStrike Falcon Intelligence](https://www.crowdstrike.com/products/threat-intelligence/falcon-intelligence-automated-intelligence/)

