# Description

CrowdStrike Falcon Intelligence is used to automatically investigate incidents and accelerate alert triage and response. Built into the Falcon Platform, it is operational in seconds

# Key Features

* Get full or short report
* Submit file for analysis
* Check analysis status
* Get submissions ids
* Get reports ids

# Requirements

* URL of your Crowdstrike Platform instance
* Client ID
* Client Secret

# Supported Product Versions

* 2022-11-28 Crowdstrike API v2

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|baseUrl|string|https://api.crowdstrike.com|True|The Base URL provided in the API Clients and Keys settings|None|https://api.crowdstrike.com|None|None|
|clientId|string|None|True|CrowdStrike Client ID|None|eXaMpl3Cli3ntID|None|None|
|clientSecret|credential_secret_key|None|True|CrowdStrike Secret Key|None|eXaMpl3S3cr3tK3Y|None|None|

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


#### Check Analysis Status

This action is used to check the status of a sandbox analysis. Time required for analysis varies but is usually less 
than 15 minutes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ids|[]string|None|True|List of submitted malware samples ids. Find a submission ID from the response when submitting a malware sample or search with `Get Submissions IDs` action|None|Md29sKvzxiddHJ0k3qnC8iDyhfZ3UZrFqOSSdKn3NhLrQR4eCsvQvOesmuXX5pra|None|None|
  
Example input:

```
{
  "ids": "Md29sKvzxiddHJ0k3qnC8iDyhfZ3UZrFqOSSdKn3NhLrQR4eCsvQvOesmuXX5pra"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submissions|[]submission|True|List of submissions|[{"id":"9382986b58cb4b44935e7eba079842f3_7c6d4bf5ab0c4459b855aaa345f4bcf9","cid":"9382986b58cb4b44935e7eba079842f3","userId":"3e7da174cb6944e8a4cd8a5a59a76727","userName":"user@example.com","userUuid":"a149764d-21ee-42af-ac9f-023f5d23ab81","origin":"uiproxy","state":"error","createdTimestamp":"2022-08-30T09:25:35Z","sandbox":[{"sha256":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","environmentId":300,"submitName":"action.py"}]},{"id":"9382986b58cb4b44935e7eba079842f3_63aca0772bf342648b2a8779c7bfcadd","cid":"9382986b58cb4b44935e7eba079842f3","userId":"3e7da174cb6944e8a4cd8a5a59a76727","userName":"user@example.com","userUuid":"a149764d-21ee-42af-ac9f-023f5d23ab81","origin":"uiproxy","state":"error","createdTimestamp":"2022-08-30T09:21:00Z","sandbox":[{"sha256":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","environmentId":100,"submitName":"Archive.zip"}]}]|
  
Example output:

```
{
  "submissions": [
    {
      "cid": "9382986b58cb4b44935e7eba079842f3",
      "createdTimestamp": "2022-08-30T09:25:35Z",
      "id": "9382986b58cb4b44935e7eba079842f3_7c6d4bf5ab0c4459b855aaa345f4bcf9",
      "origin": "uiproxy",
      "sandbox": [
        {
          "environmentId": 300,
          "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
          "submitName": "action.py"
        }
      ],
      "state": "error",
      "userId": "3e7da174cb6944e8a4cd8a5a59a76727",
      "userName": "user@example.com",
      "userUuid": "a149764d-21ee-42af-ac9f-023f5d23ab81"
    },
    {
      "cid": "9382986b58cb4b44935e7eba079842f3",
      "createdTimestamp": "2022-08-30T09:21:00Z",
      "id": "9382986b58cb4b44935e7eba079842f3_63aca0772bf342648b2a8779c7bfcadd",
      "origin": "uiproxy",
      "sandbox": [
        {
          "environmentId": 100,
          "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
          "submitName": "Archive.zip"
        }
      ],
      "state": "error",
      "userId": "3e7da174cb6944e8a4cd8a5a59a76727",
      "userName": "user@example.com",
      "userUuid": "a149764d-21ee-42af-ac9f-023f5d23ab81"
    }
  ]
}
```

#### Download Artifact

This action is used to download IOC packs, PCAP files, memory dumps, and other analysis artifacts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|ID of an JSON artifact, such as an IOC pack, PCAP file, memory dump, or actor image. Find an artifact ID with `Get Full Report` action|None|Md29sKvzxiddHJ0k3qnC8iDyhfZ3UZrFqOSSdKn3NhLrQR4eCsvQvOesmuXX5pra|None|None|
  
Example input:

```
{
  "id": "Md29sKvzxiddHJ0k3qnC8iDyhfZ3UZrFqOSSdKn3NhLrQR4eCsvQvOesmuXX5pra"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|artifacts|[]artifact|True|List of artifacts|[{"ioc":"44d88612fea8a8f36de82e1278abb02f","source":"extracted","type":"md5"},{"ioc":"44d88612fea8a8f36de82e1278abb02f","source":"extracted","type":"md5"},{"ioc":"44d88612fea8a8f36de82e1278abb02f","source":"extracted","type":"md5"},{"ioc":"44d88612fea8a8f36de82e1278abb02f","source":"extracted","type":"md5"},{"ioc":"3395856ce81f2b7382dee72602f798b642f14140","source":"extracted","type":"sha1"},{"ioc":"3395856ce81f2b7382dee72602f798b642f14140","source":"extracted","type":"sha1"},{"ioc":"3395856ce81f2b7382dee72602f798b642f14140","source":"extracted","type":"sha1"},{"ioc":"3395856ce81f2b7382dee72602f798b642f14140","source":"extracted","type":"sha1"},{"ioc":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","source":"extracted","type":"sha256"},{"ioc":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","source":"extracted","type":"sha256"},{"ioc":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","source":"extracted","type":"sha256"},{"ioc":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","source":"extracted","type":"sha256"},{"ioc":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","source":"input","type":"sha256"},{"ioc":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","source":"runtime","type":"sha256"},{"ioc":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","source":"runtime","type":"sha256"}]|
  
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

This action is used to get a full sandbox report

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ids|[]string|None|True|List of summary IDs. Find a summary ID from the response when submitting a malware sample or search with `Get Reports IDs` action|None|["9de5069c5afe602b2ea0a11b66beb2c0_9aa5069c5afe602b2ea0a04b66beb2c0"]|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|reports|[]report|True|List of sandbox reports|["9de5069c5afe602b2ea0a11b66beb2c0_9aa5069c5afe602b2ea0a04b66beb2c0"]|
  
Example output:

```
{
  "reports": [
    "9de5069c5afe602b2ea0a11b66beb2c0_9aa5069c5afe602b2ea0a04b66beb2c0"
  ]
}
```

#### Get Reports IDs

This action is used to find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs 
that match your criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|Filter and sort criteria in the form of an FQL query. For more information about FQL queries, see https://falcon.crowdstrike.com/documentation/45/falcon-query-language-fql|None|verdict: 'no verdict'|None|None|
|limit|integer|None|False|Maximum number of report IDs to return - less or equal to 5000|None|324|None|None|
|offset|integer|None|False|The offset to start retrieving reports from|None|5|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|reportIds|[]string|True|List of report IDs|["9382986b58cb4b44935e7eba071142f3_92c8b7525e2b4888bd9e2jj7391c7104"]|
  
Example output:

```
{
  "reportIds": [
    "9382986b58cb4b44935e7eba071142f3_92c8b7525e2b4888bd9e2jj7391c7104"
  ]
}
```

#### Get Short Report

This action is used to get a short summary version of a sandbox report

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ids|[]string|None|True|List of summary IDs. Find a summary ID from the response when submitting a malware sample or search with `Get Reports IDs` action|None|["9382986b58cb4bb4935e7eba079842f3_d1ce821d74484545897f2fd5db40d0a7"]|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|reports|[]reportShort|True|List of short sandbox reports|[{"cid":"9382986b58cb4bb4935e7eba079842f3","createdTimestamp":"2022-09-28T07:45:34Z","id":"9382986b58cb4bb4935e7eba079842f3_d1ce821d74484545897f2fd5db40d0a7","origin":"uiproxy","sandbox":[{"environmentDescription":"Windows 7 32 bit","environmentId":100,"errorMessage":"The file \"Dockerfile\" has the file format \"text\", which is not supported","errorOrigin":"CLIENT","errorType":"FILE_TYPE_BAD_ERROR","fileType":"ASCII text","sha256":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","submissionType":"file","submitName":"Dockerfile"}],"userId":"9de5069c5afe602b2ea0a04b66beb2c0","userName":"https://example.com","verdict":"no verdict"}]|
  
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

#### Get Submissions IDs

This action is used to find submissions IDs for uploaded files by providing an FQL filter and paging details. Returns a
 set of submission IDs that match your criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|Filter and sort criteria in the form of an FQL query. For more information about FQL queries, see https://falcon.crowdstrike.com/documentation/45/falcon-query-language-fql|None|state: 'running'|None|None|
|limit|integer|None|False|Maximum number of report IDs to return - less or equal to 5000|None|324|None|None|
|offset|integer|None|False|The offset to start retrieving reports from|None|5|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|submissionIds|[]string|True|List of submission IDs|["9382986b58cb4b44935e7eba071142f3_92c8b7525e2b4888bd9e2jj7391c7104"]|
  
Example output:

```
{
  "submissionIds": [
    "9382986b58cb4b44935e7eba071142f3_92c8b7525e2b4888bd9e2jj7391c7104"
  ]
}
```

#### Submit Analysis

This action is used to submit an uploaded file or a URL for sandbox analysis. Time required for analysis varies but is 
usually less than 15 minutes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|actionScript|string|None|False|Runtime script for sandbox analysis|["", "default", "default_maxantievasion", "default_randomfiles", "default_randomtheme", "default_openie"]|default_openie|None|None|
|commandLine|string|None|False|Command line script passed to the submitted file at runtime. Max length is 2048 characters|None|/example /command|None|None|
|documentPassword|password|None|False|Auto-filled for Adobe or Office files that prompt for a password. Max length is 32 characters|None|3xamp13Pa55w0rd|None|None|
|environmentId|integer|None|True|Specifies the sandbox environment used for analysis. Example values 300 - Linux Ubuntu 16.04, 64-bit; 200 - Android (static analysis); 160 - Windows 10, 64-bit; 110 - Windows 7, 64-bit; 100 - Windows 7, 32-bit|[100, 110, 160, 200, 300]|110|None|None|
|networkSettings|string|None|False|Specifies the sandbox network_settings used for analysis|["", "default", "tor", "simulated", "offline"]|tor|None|None|
|sha256|string|None|False|ID of the sample, which is a SHA256 hash value. Find a sample ID from the response when uploading a malware sample or search with `Get Submissions IDs` action. The `url` parameter must be unset if `sha256` is used|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|None|None|
|submitName|string|None|False|Name of the malware sample that's used for file type detection and analysis|None|my_sample|None|None|
|systemDateTime|date|None|False|System date and time|None|2022-11-01 00:00:00+02:00|None|None|
|url|string|None|False|A web page or file URL. It can be HTTP(S) or FTP. The `SHA256` parameter must be unset if `url` is used|None|https://www.example.com/images/default/sample.pdf|None|None|
  
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
  "systemDateTime": "2022-11-01 00:00:00+02:00",
  "url": "https://www.example.com/images/default/sample.pdf"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submission|submission|True|Submission|{"cid":"9de5069c5mne602b2ea0a04b66beb2c0","createdTimestamp":"2022-11-22T06:10:42Z","id":"9de5069c5mne602b2ea0a04b66beb2c0_8de5069c5afe602b2ea0a04b66beb2c0","origin":"apigateway","sandbox":[{"actionScript":"default_openie","environmentId":110,"networkSettings":"tor","sha256":"275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f","submitName":"my_sample","systemDate":"2022-12-22","systemTime":"17:33"}],"state":"created"}|
  
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

#### Upload Malware Samples

This action is used to upload malware sample

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|A descriptive comment to identify the file for other users|None|ExampleComment|None|None|
|filename|string|None|True|The name of file to be used to override the default filename|None|ExampleFilename.exe|None|None|
|isConfidential|boolean|True|False|Defines visibility of this file in Falcon MalQuery, either via the API or the Falcon console. `True` means that file is only shown to users within your customer account. `False` means that file can be seen by other CrowdStrike customers|None|True|None|None|
|sample|file|None|True|The samples of file to be sent for analysis (max file size is 256 MB)|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|None|None|
  
Example input:

```
{
  "comment": "ExampleComment",
  "filename": "ExampleFilename.exe",
  "isConfidential": true,
  "sample": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|fileName|string|True|The name of uploaded malware sample file|ExampleMalwareSampleFile.exe|
|sha256|string|True|The ID of the sample, which is a SHA256 hash value|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
  
Example output:

```
{
  "fileName": "ExampleMalwareSampleFile.exe",
  "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**extractedInterestingStrings**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Process|string|None|False|Process|AcroRd32.exe|
|Source|string|None|False|Source|Runtime Data|
|Type|string|None|False|Type|Ansi|
|Value|string|None|False|Value|%GUID:"Computer"%|
  
**extractedFiles**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description|data|
|File Path|string|None|False|File path|%APPDATA%\Adobe\Acrobat\DC\Security\CRLCache\0FDED5CEB68C302B1CDB2BDDD9D0000E76539CB0.crl|
|File Size|integer|None|False|File size|637|
|MD5|string|None|False|MD5|44d88612fea8a8f36de82e1278abb02f|
|Runtime Process|string|None|False|Runtime process|AcroRd32.exe (PID: 2464)|
|SHA1|string|None|False|SHA1|3395856ce81f2b7382dee72602f798b642f14140|
|SHA256|string|None|False|SHA256|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|Threat Level Readable|string|None|False|Threat level readable|no specific threat|
|Type Tags|[]string|None|False|Type tags|["data"]|
  
**fileAccess**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Mask|string|None|False|Mask|FILE_READ_DATA|
|Path|string|None|False|Path|\DEVICE\NETBT_TCPIP_{E29AC6C2-7037-11DE-816D-806E6F6E6963}|
|Type|string|None|False|Type|CREATE|
  
**handle**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|1|
|Path|string|None|False|Path|HKCU\Software\Adobe\CommonFiles\Usage\Reader DC|
|Type|string|None|False|Type|KeyHandle|
  
**registry**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key|string|None|False|Key|DEBUGPROCESSHEAPONLY|
|Operation|string|None|False|Operation|Query|
|Path|string|None|False|Path|HKLM/SOFTWARE/MICROSOFT/WINDOWS NT/CURRENTVERSION/IMAGE FILE EXECUTION OPTIONS/ACRORD32.EXE/DEBUGPROCESSHEAPONLY|
|Status|string|None|False|Status|c0000034|
|Status Human Readable|string|None|False|Status human readable|STATUS_OBJECT_NAME_NOT_FOUND|
  
**process**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Command Line|string|None|False|Command line|C:/test.pdf|
|File Accesses|[]fileAccess|None|False|File accesses|[]|
|Handles|[]handle|None|False|Handles|[]|
|Icon Artifact ID|string|None|False|Icon artifact ID|fb3d245e52890c452df97787e773961f60a1d0a2449a3cac6b259df43adda88a|
|Mutants|[]string|None|False|Mutants|["/Sessions/1/BaseNamedObjects/Local/Acrobat Instance Mutex", "/Session/s1/BaseNamedObjects/DBWinMutex", "DBWinMutex", "Local/Acrobat Instance Mutex"]|
|Normalized Path|string|None|False|Normalized path|%PROGRAMFILES%/Adobe/Acrobat Reader DC/Reader/AcroRd32.exe/|
|PID|integer|None|False|PID|2464|
|Registry|[]registry|None|False|Registry|[]|
|SHA256|string|None|False|SHA256|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|UID|string|None|False|UID|00000000-00002464|
  
**signature**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|False|Category|General|
|Description|string|None|False|Description|Spawned process "RdrCEF.exe" with commandline "--backgroundcolor=16448250"(UID: 00000000-00003660)\n Spawned process "RdrCEF.exe" with commandline "--type=renderer --primordial-pipe-token=9C6380B3089134F0668BD8E2 ..." (UID: 00000000-00003632)\n Spawned process "RdrCEF.exe" with commandline "--type=renderer\--primordial-pipe-token=2A1B0CA713F65BDBBEF8417F ..."|
|Identifier|string|None|False|Identifier|target-25|
|Origin|string|None|False|Origin|Monitored Target|
|Relevance|integer|None|False|Relevance|3|
|Threat Level Human|string|None|False|Threat level human|informative|
|Type|integer|None|False|Type|9|
  
**sandbox**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Architecture|string|None|False|Architecture|WINDOWS|
|Environment Description|string|None|False|Environment description|Windows 7 32 bit|
|Environment ID|integer|None|False|Environment ID|100|
|Error Message|string|None|False|Error message|The file "Dockerfile" has the file format "text", which is not supported|
|Error Origin|string|None|False|Error origin|CLIENT|
|Error Type|string|None|False|Error type|FILE_TYPE_BAD_ERROR|
|Extracted Files|[]extractedFiles|None|False|Extracted files|[]|
|Extracted Interesting Strings|[]extractedInterestingStrings|None|False|Extracted interesting strings|[]|
|File Size|integer|None|False|File size|15007|
|File Type|string|None|False|File type|PDF document, version 1.5|
|File Type Short|[]string|None|False|File type short|["pdf"]|
|Memory Dumps Artifact ID|string|None|False|Memory dumps artifact ID|774fb1bb4d52bd1de58385abbef347ed0a557bbaef1f2330520da1e5d96ad26b|
|Memory Strings Artifact ID|string|None|False|Memory strings artifact ID|b588943e02558755f0c4c84adc5b42ff6642f216313c78b70ff02231ff129f9e|
|Network Settings|string|None|False|Network settings|default|
|PCAP Report Artifact ID|string|None|False|PCAP report artifact ID|31481ec4027e67cf7acf76d56ccebbbf133bb7b36dea1c750c1699f53abe6403|
|Processes|[]process|None|False|Processes|[]|
|Sample Flags|[]string|None|False|Sample flags|["Extracted Files"]|
|Screenshots Artifact IDs|[]string|None|False|Screenshots artifact IDs|["22782c460dc9e2662ae9c5420142c1ecdf84c122745ab0b61780f1685a2e8751","d7e025e31e87ddffb56f6203f5e69acc639c423ce9128068186071d1b94bcae3"]|
|SHA256|string|None|False|SHA256|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|Signatures|[]signature|None|False|Signatures|[]|
|Submission Type|string|None|False|Submission type|file|
|Submit Name|string|None|False|Submit name|test.pdf|
|Submit URL|string|None|False|Submit URL|https://example.com/test.pdf|
|Verdict|string|None|False|Verdict|no specific threat|
|Windows Version Bitness|integer|None|False|Windows version bitness|32|
|Windows Version Edition|string|None|False|Windows version edition|Professional|
|Windows Version Name|string|None|False|Windows version name|Windows 7|
|Windows Version Service Pack|string|None|False|Windows version service pack|Service Pack 1|
|Windows Version Version|string|None|False|Windows version version|6.1 (build 7601)|
  
**sandboxShort**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action Script|string|None|False|Action script|default_randomfiles|
|Environment Description|string|None|False|Environment description|Windows 7 32 bit|
|Environment ID|integer|None|False|Environment ID|100|
|Error Message|string|None|False|Error message|The file "Dockerfile" has the file format "text", which is not supported|
|Error Origin|string|None|False|Error origin|CLIENT|
|Error Type|string|None|False|Error type|FILE_TYPE_BAD_ERROR|
|File Type|string|None|False|File type|PDF document, version 1.5|
|Network Settings|string|None|False|Network settings|default|
|Sample Flags|[]string|None|False|Sample flags|["Extracted Files"]|
|SHA256|string|None|False|SHA256|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|Submission Type|string|None|False|Submission type|file|
|Submit Name|string|None|False|Submit name|test.pdf|
|Submit URL|string|None|False|Submit URL|https://example.com/test.pdf|
|System Date|string|None|False|System date|2022-09-22 00:00:00|
|System Time|string|None|False|System time|!!python/object/apply:datetime.time !!binary | DDcAAAAA|
|URL|string|None|False|URL|https://example.com/test.pdf|
|Verdict|string|None|False|Verdict|no specific threat|
  
**submission**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Cid|string|None|False|Cid|9382986b58cb4b44935e7eba079842f3|
|Created Timestamp|string|None|False|Created timestamp|2022-08-30T10:09:18Z|
|ID|string|None|False|ID|9382986b58cb4b44935e7eba079842f3_a345bda609ba46d3a6df3dcf38e30145|
|Origin|string|None|False|Origin|uiproxy|
|Sandbox|[]sandboxShort|None|False|Sandbox|[]|
|State|string|None|False|State|success|
|User ID|string|None|False|User ID|6f888e357b5043c6906c51b204c4091b|
|User Name|string|None|False|User name|user@example.com|
|User Tags|[]string|None|False|User tags|["my_tag"]|
|User UUID|string|None|False|User UUID|a149764d-21ee-42af-ac9f-023f5d23ab81|
  
**artifact**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IOC|string|None|False|IOC|974e8536b8767ac5be204f35d16f73e8|
|Source|string|None|False|Source|extracted|
|Type|string|None|False|Type|md5|
  
**malquery**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Input|string|None|False|Input|53d23839e0f75e7772d1c4ea9e7384f5468ba911c7a6ff16c83e077aa53959d7|
|Type|string|None|False|Type|sha256|
|Verdict|string|None|False|Verdict|unknown|
  
**reportShort**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CID|string|None|False|CID of the report|9382986b58cb4b44447ereba079842f3|
|Created Timestamp|date|None|False|Time when the report was created|2022-08-30T10:08:49Z|
|ID|string|None|False|ID of the report|9382986b58cb4b44447ereba079842f3_4c95cb1fc7314509a5b9012352e9c4ff|
|IOC Report Broad CSV Artifact ID|string|None|False|IOC report broad CSV artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Broad JSON Artifact ID|string|None|False|IOC report broad JSON artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Broad Maec Artifact ID|string|None|False|IOC report broad maec artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Broad STIX Artifact ID|string|None|False|IOC report broad STIX artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Strict CSV Artifact ID|string|None|False|IOC report strict CSV artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Strict JSON Artifact ID|string|None|False|IOC report strict JSON artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Strict Maec Artifact ID|string|None|False|IOC report strict maec artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Strict STIX Artifact ID|string|None|False|IOC report strict STIX artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|Origin|string|None|False|Origin|uiproxy|
|Sandbox|[]sandboxShort|None|False|Sandbox details|[]|
|User ID|string|None|False|ID of the user|6f998e327b5043c6906c51b204p4091b|
|User Name|string|None|False|Name of the user|user@example.com|
|Verdict|string|None|False|Verdict of the report|no specific threat|
  
**report**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CID|string|None|False|CID of the report|9382986b58cb4b44447ereba079842f3|
|Created Timestamp|date|None|False|Time when the report was created|2022-08-30T10:08:49Z|
|ID|string|None|False|ID of the report|9382986b58cb4b44447ereba079842f3_4c95cb1fc7314509a5b9012352e9c4ff|
|IOC Report Broad CSV Artifact ID|string|None|False|IOC report broad CSV artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Broad JSON Artifact ID|string|None|False|IOC report broad JSON artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Broad Maec Artifact ID|string|None|False|IOC report broad maec artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Broad STIX Artifact ID|string|None|False|IOC report broad STIX artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Strict CSV Artifact ID|string|None|False|IOC report strict CSV artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Strict JSON Artifact ID|string|None|False|IOC report strict JSON artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Strict Maec Artifact ID|string|None|False|IOC report strict maec artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|IOC Report Strict STIX Artifact ID|string|None|False|IOC report strict STIX artifact ID|1248b73905ba1b8ef5fdca2d3604e41a331bhy43659ccfc714467153c706d00|
|Malquery|[]malquery|None|False|Malquery|[]|
|Origin|string|None|False|Origin|uiproxy|
|Sandbox|[]sandbox|None|False|Sandbox details|[]|
|User ID|string|None|False|ID of the user|6f998e327b5043c6906c51b204p4091b|
|User Name|string|None|False|Name of the user|user@example.com|
|User UUID|string|None|False|UUID of the user|a149114d-21ee-42af-ac9f-04kf5d23ab81|
|Verdict|string|None|False|Verdict of the report|no specific threat|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.1.0 - New action added: `Upload Malware Sample` | Updated SDK to the latest version
* 1.0.0 - Initial plugin | Check Analysis Status, Download Artifact, Get Full Report, Get Reports IDs, Get Short Report, Get Submissions IDs, Submit Analysis

# Links

* [CrowdStrike Falcon Intelligence](https://www.crowdstrike.com/products/threat-intelligence/falcon-intelligence-automated-intelligence/)

## References

* [CrowdStrike Falcon Intelligence](https://www.crowdstrike.com/products/threat-intelligence/falcon-intelligence-automated-intelligence/)