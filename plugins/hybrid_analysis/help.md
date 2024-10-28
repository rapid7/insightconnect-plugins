# Description

[Hybrid Analysis](https://www.hybrid-analysis.com/) is a free malware analysis service powered by Payload Security that detects and analyzes unknown threats using a unique Hybrid Analysis technology. This plugin provides the ability to lookup file hashes to determine whether or not they are malicious.

# Key Features

* Lookup a file hash to identify known and unknown threats using Hybrid Analysis technology

# Requirements

* A HybridAnalysis API key and token

# Supported Product Versions

* Hybrid Analysis API v2

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|API key|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|url|string|https://www.hybrid-analysis.com|True|Hybrid Analysis API server URL|None|https://www.hybrid-analysis.com|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "url": "https://www.hybrid-analysis.com"
}
```

## Technical Details

### Actions


#### Lookup by Hash

This action is used to get summary information for a given hash

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hash|string|None|True|Hash to lookup. Must be MD5, SHA1, or SHA256|None|44d88612fea8a8f36de82e1278abb02f|None|None|
  
Example input:

```
{
  "hash": "44d88612fea8a8f36de82e1278abb02f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|True|
|reports|[]report|False|Reports|None|
|threatscore|integer|False|Threat Score (max found)|0|
  
Example output:

```
{
  "found": true,
  "reports": [
    {
      "analysis_start_time": "2021-11-09T19:12:21+00:00",
      "av_detect": 0,
      "certificates": [],
      "classification_tags": [],
      "compromised_hosts": [],
      "domains": [],
      "environment_description": "Static Analysis",
      "extracted_files": [],
      "hosts": [],
      "interesting": false,
      "machine_learning_models": [],
      "md5": "40451f20371329b992fb1b85c754d062",
      "mitre_attcks": [],
      "network_mode": "default",
      "processes": [],
      "sha1": "89504d91c5539a366e153894c1bc17277116342b",
      "sha256": "3919059a1e0d38d6116f24945b0bb2aa5e98b85ac688b3aba270d7997bb64a0d",
      "sha512": "acfaca234c48f055c0f532e16bd5879f1637ecd639938c3d301b528b08af79988fcd6f0b61e4fd51901b250e72c90a48aca60d20d1b54036373aa6996baae326",
      "size": 27298,
      "state": "SUCCESS",
      "submissions": [
        {
          "created_at": "2021-11-10T20:09:28+00:00",
          "filename": "file",
          "submission_id": "618c26f8099c0e23c541f405"
        },
        {
          "created_at": "2021-11-09T19:12:21+00:00",
          "filename": "file",
          "submission_id": "618ac815742aee567341009c"
        }
      ],
      "submit_name": "file",
      "tags": [],
      "threat_level": 0,
      "total_network_connections": 0,
      "total_processes": 0,
      "total_signatures": 0,
      "type": "PE32 executable (DLL) (GUI) Intel 80386, for MS Windows",
      "type_short": [
        "pedll",
        "executable"
      ],
      "url_analysis": false,
      "verdict": "no specific threat"
    }
  ],
  "threatscore": 0
}
```

#### Search Database

This action is used to search the database using API v2 provided at https://www.hybrid-analysis.com/docs/api/v2.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|country|string|None|False|Country must be specified in the ISO 3166-1 standard|None|AFG|None|None|
|domain|string|None|False|Domain which will be analyzed|None|example.com|None|None|
|filename|string|None|False|File name|None|setup.exe|None|None|
|filetype|string|None|False|File type|None|docx|None|None|
|host|string|None|False|Information about the host which will be analyzed|None|198.51.100.1|None|None|
|port|integer|8080|False|Port number which is associated with an IP address|None|8080|None|None|
|similar_to|string|None|False|SHA256 hash of the similar file|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|None|None|
|tag|string|None|False|Hashtag by which the analysis will be performed|None|ransomware|None|None|
|url|string|None|False|URL to analyze|None|https://example.com|None|None|
|verdict|string|whitelisted|False|A decision on a submitted term|["whitelisted", "no verdict", "no specific threat", "suspicious", "malicious"]|whitelisted|None|None|
  
Example input:

```
{
  "country": "AFG",
  "domain": "example.com",
  "filename": "setup.exe",
  "filetype": "docx",
  "host": "198.51.100.1",
  "port": 8080,
  "similar_to": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "tag": "ransomware",
  "url": "https://example.com",
  "verdict": "whitelisted"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of results returned|1|
|result|[]result|False|List of results|None|
|search_terms|[]search_term|True|List of key value pairs. Where the key is the parameter specified and its value|None|
  
Example output:

```
{
  "count": 1,
  "result": [
    {
      "analysis_start_time": "2021-09-02 18:58:23",
      "av_detect": "0",
      "environment_description": "Windows 7 64 bit",
      "environment_id": 120,
      "job_id": "61311eca7a48ee7a9e3041d7",
      "sha256": "82b43762a5bc9c0ab7b5d1f96dc47b34700924b598070a7ccb30c92eb5ee1599",
      "size": 18944,
      "submit_name": "ew_usbccgpfilter.sys",
      "type_short": "64-bit service",
      "verdict": "whitelisted"
    }
  ],
  "search_terms": [
    {
      "id": "filename",
      "value": "setup.exe"
    },
    {
      "id": "verdict",
      "value": "1"
    }
  ]
}
```

#### Retrieve Report

This action is used to retrieve report by providing SHA256 hash.
##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hash|string|None|True|SHA256 hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|None|None|
  
Example input:

```
{
  "hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|error|string|False|An error that occurred during the analysis|File \"testing.com.txt\" was detected as \"unknown\", this format is not supported on WINDOWS|
|error_origin|string|False|Error origin|CLIENT|
|error_type|string|False|Type of error that occurred|FILE_TYPE_BAD_ERROR|
|related_reports|[]related_reports|False|Related reports which contained analysis information on linked data|None|
|state|string|True|State in which the analysis is in|ERROR|
  
Example output:

```
{
  "related_reports": [
    {
      "job_id": "61dc148b0cad612f7371d2d3",
      "environment_id": 300,
      "state": "SUCCESS",
      "sha256": "275a021bbfb6489e54d411499f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
    }
  ],
  "state": "SUCCESS"
}
```

#### Submit File

This action is used to submit file for analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|custom_cmd_line|string|None|False|Optional command line that should be passed to the file analysis|None|command|None|None|
|document_password|string|None|False|Optional document password that will be used to fill-in Adobe/Office password prompts|None|somepassword|None|None|
|environment_id|string|Linux (Ubuntu 16.04, 64 bit)|False|Environment ID on which the analysis will be performed|["Linux (Ubuntu 16.04, 64 bit)", "Android Static Analysis", "Windows 7 64 bit", "Windows 7 32 bit (HWP Support)", "Windows 7 32 bit"]|Linux (Ubuntu 16.04, 64 bit)|None|None|
|experimental_anti_evasion|boolean|True|False|When set to true, will set all experimental anti-evasion options of the Kernelmode Monitor|None|True|None|None|
|file|file|None|True|File to be analyzed|None|{"filename": "setup.exe", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==" }|None|None|
|hybrid_analysis|boolean|True|False|When set to false, no memory dumps or memory dump analysis will take place|None|True|None|None|
|script_logging|boolean|False|False|When set to true, will set the in-depth script logging engine of the Kernelmode Monitor|None|True|None|None|
|submit_name|string|None|False|Optional property which will be used for file type detection and analysis|None|testName|None|None|
  
Example input:

```
{
  "custom_cmd_line": "command",
  "document_password": "somepassword",
  "environment_id": "Linux (Ubuntu 16.04, 64 bit)",
  "experimental_anti_evasion": true,
  "file": {
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
    "filename": "setup.exe"
  },
  "hybrid_analysis": true,
  "script_logging": false,
  "submit_name": "testName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|environment_id|integer|False|The environment that was used for analysis|300|
|job_id|string|False|Job ID which will be generated by server|61dc148b0cad612f7371d2d3|
|sha256|string|False|SHA256 hash for report retrieval|6617aa88a72e6b526b88cbceda388a7b52a0e856148a12d9b8...|
|submission_id|string|False|Submission ID which will be generated by server|61dc148b0cad612f7371d2d3|
  
Example output:

```
{
  "environment_id": 300,
  "job_id": "61dc148b0cad612f7371d2d3",
  "sha256": "6617aa88a72e6b526b88cbceda388a7b52a0e856148a12d9b8...",
  "submission_id": "61dc148b0cad612f7371d2d3"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**certificates**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Issuer|string|None|False|Issuer|None|
|MD5|string|None|False|MD5|None|
|Owner|string|None|False|Owner|None|
|Serial Number|string|None|False|Serial number|None|
|SHA1|string|None|False|SHA1|None|
|Valid From|string|None|False|Valid from|None|
|Valid Until|string|None|False|Valid until|None|
  
**extracted_files**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Available Label|string|None|False|Available label|None|
|Available Matched|integer|None|False|Available matched|None|
|Available Total|integer|None|False|Available total|None|
|Description|string|None|False|Description|None|
|File Available To Download|boolean|None|False|File available to download|None|
|File Path|string|None|False|File path|None|
|File Size|integer|None|False|File size|None|
|MD5|string|None|False|MD5|None|
|Name|string|None|False|Name|None|
|Runtime Process|string|None|False|Runtime process|None|
|SHA1|string|None|False|SHA1|None|
|SHA256|string|None|False|SHA256|None|
|Threat Level|integer|None|False|Threat level|None|
|Threat Level Readable|string|None|False|Threat level readable|None|
|Type Tags|[]string|None|False|Type tags|None|
  
**file_metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|File Analysis|[]string|None|False|File analysis|None|
|File Compositions|[]string|None|False|File compositions|None|
|Imported Objects|[]string|None|False|Imported objects|None|
|Total File Compositions Imports|integer|None|False|Total file compositions imports|None|
  
**created_files**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|File|string|None|False|File|None|
|Null Byte|boolean|None|False|Null byte|None|
  
**file_accesses**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Mask|string|None|False|Mask|None|
|Path|string|None|False|Path|None|
|Type|string|None|False|Type|None|
  
**handles**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Path|string|None|False|Path|None|
|Type|string|None|False|Type|None|
  
**process_flags**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Data|string|None|False|Data|None|
|Image|string|None|False|Image|None|
|Name|string|None|False|Name|None|
  
**registry**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key|string|None|False|Key|None|
|Operation|string|None|False|Operation|None|
|Path|string|None|False|Path|None|
|Status|string|None|False|Status|None|
|Status Human Readable|string|None|False|Status human readable|None|
|Value|string|None|False|Value|None|
  
**parameters**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Argument Number|integer|None|False|Argument number|None|
|Comment|string|None|False|Comment|None|
|Meaning|string|None|False|Meaning|None|
|Name|string|None|False|Name|None|
|Value|string|None|False|Value|None|
  
**script_calls**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Cls ID|string|None|False|Cls ID|None|
|Dispatch ID|string|None|False|Dispatch ID|None|
|Matched Malicious Signatures|[]string|None|False|Matched malicious signatures|None|
|Parameters|[]parameters|None|False|Parameters|None|
|Result|string|None|False|Result|None|
|Status|string|None|False|Status|None|
  
**matched_signatures**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID|None|
|Value|string|None|False|Value|None|
  
**streams**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Executed|boolean|None|False|Executed|None|
|File Name|string|None|False|File name|None|
|Human Keywords|string|None|False|Human keywords|None|
|Instructions|[]string|None|False|Instructions|None|
|Matched Signatures|[]matched_signatures|None|False|Matched signatures|None|
|UID|string|None|False|UID|None|
  
**processes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Available Label|string|None|False|Available label|None|
|Available Matched|integer|None|False|Available matched|None|
|Available Total|integer|None|False|Available total|None|
|Command Line|string|None|False|Command line|None|
|Created Files|[]created_files|None|False|Created files|None|
|File Accesses|[]file_accesses|None|False|File accesses|None|
|Handles|[]handles|None|False|Handles|None|
|Icon|string|None|False|Icon|None|
|Mutants|[]string|None|False|Mutants|None|
|Name|string|None|False|Name|None|
|Normalized Path|string|None|False|Normalized path|None|
|Parent UID|string|None|False|Parent UID|None|
|PID|string|None|False|PID|None|
|Process Flags|[]process_flags|None|False|Process flags|None|
|Registry|[]registry|None|False|Registry|None|
|Script Calls|[]script_calls|None|False|Script calls|None|
|SHA256|string|None|False|SHA256|None|
|Streams|[]streams|None|False|Streams|None|
|UID|string|None|False|UID|None|
  
**mitre_attcks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attck ID|string|None|False|Attck ID|None|
|Attck ID Wiki|string|None|False|Attck ID wiki|None|
|Informative Identifiers|[]string|None|False|Informative identifiers|None|
|Informative Identifiers Count|integer|None|False|Informative identifiers count|None|
|Malicious Identifiers|[]string|None|False|Malicious identifiers|None|
|Malicious Identifiers Count|integer|None|False|Malicious identifiers count|None|
|Suspicious Identifiers|[]string|None|False|Suspicious identifiers|None|
|Suspicious Identifiers Count|integer|None|False|Suspicious identifiers count|None|
|Tactic|string|None|False|Tactic|None|
|Technique|string|None|False|Technique|None|
  
**submissions**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|string|None|False|Created at|None|
|Filename|string|None|False|File name|None|
|Submission ID|string|None|False|Submission ID|None|
|URL|string|None|False|URL|None|
  
**machine_learning_models**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|string|None|False|Created at|None|
|Data|[]matched_signatures|None|False|Data|None|
|Name|string|None|False|Name|None|
|Status|string|None|False|Status|None|
|Version|string|None|False|Version|None|
  
**report**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Analysis Start Time|string|None|False|Analysis start time|None|
|Antivirus Detect|integer|None|False|Antivirus detect|None|
|Certificates|[]certificates|None|False|Certificates|None|
|Classification Tags|[]string|None|False|Classification tags|None|
|Compromised Hosts|[]string|None|False|Compromised hosts|None|
|Domains|[]string|None|False|Domains|None|
|Environment Description|string|None|False|Environment description|None|
|Environment ID|integer|None|False|The environment that was used for analysis|None|
|Error Origin|string|None|False|Error origin|None|
|Error Type|string|None|False|Type of error that occurred|None|
|Extracted Files|[]extracted_files|None|False|Extracted files|None|
|File Metadata|file_metadata|None|False|File metadata|None|
|Hosts|[]string|None|False|Hosts|None|
|IMP Hash|string|None|False|IMP Hash|None|
|Interesting|boolean|None|False|Interesting|None|
|Job ID|string|None|False|Job ID which is generated by server|None|
|Machine Learning Models|[]machine_learning_models|None|False|Machine learning models|None|
|MD5|string|None|False|MD5|None|
|MITRE Attcks|[]mitre_attcks|None|False|MITRE attcks|None|
|Network Mode|string|None|False|Network mode|None|
|Processes|[]processes|None|False|Processes|None|
|SHA1|string|None|False|SHA1|None|
|SHA256|string|None|False|SHA256|None|
|SHA512|string|None|False|SHA512|None|
|Size|integer|None|False|Size|None|
|SS Deep|string|None|False|SS Deep|None|
|State|string|None|False|State in which the analysis is in|None|
|Submissions|[]submissions|None|False|Submissions|None|
|Submit Name|string|None|False|Submit name|None|
|Tags|[]string|None|False|Tags|None|
|Target URL|string|None|False|Target URL|None|
|Threat Level|integer|None|False|Threat level|None|
|Threat Score|integer|None|False|Threat score|None|
|Total Network Connections|integer|None|False|Total network connections|None|
|Total Processes|integer|None|False|Total processes|None|
|Total Signatures|integer|None|False|Total signatures|None|
|Type|string|None|False|Type|None|
|Type Short|[]string|None|False|Type short|None|
|URL Analysis|boolean|None|False|URL analysis|None|
|Verdict|string|None|False|Verdict|None|
|VX Family|string|None|False|VX family|None|
  
**search_term**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Name of search term which was used|None|
|Value|string|None|False|Value of search term|None|
  
**result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Analysis Start Time|string|None|False|The time at which the analysis began|None|
|AV detect|string|None|False|AV MultiScan Detection Percentage|None|
|Environment Description|string|None|False|Description of the environment on which analysis was conducted|None|
|Environment ID|integer|None|False|The environment that was used for analysis|None|
|Job ID|string|None|False|Job ID when file was submited|None|
|SHA256|string|None|False|SHA256 hash|None|
|File Size|integer|None|False|File size in bytes|None|
|Submit Name|string|None|False|Submit name|None|
|Threat score|integer|None|False|Confidence value of VxStream Sandbox in the verdict; lies between 0 and 100|None|
|Type|string|None|False|Type|None|
|File Extension|string|None|False|File type e.g. exe|None|
|Verdict|string|None|False|File verdict e.g. malicious|None|
|VX Family|string|None|False|VX Family e.g. Trojan.Generic|None|
  
**related_reports**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Environment ID|integer|None|False|The environment that was used for analysis|None|
|Error Origin|string|None|False|Error origin|None|
|Error Type|string|None|False|Type of error that occurred|None|
|Job ID|string|None|False|Job ID which is generated by server|None|
|SHA256|string|None|False|SHA256|None|
|State|string|None|False|State in which the analysis is in|None|
|Verdict|string|None|False|Verdict|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 3.0.1 - Bumping requirements.txt | SDK bump to 6.1.4
* 3.0.0 - Update to support version 2 API | Created new actions which was moved from plugin **vxstream_sandbox** such as: Submit File, Lookup by Hash, Search Database, Retrieve Report
* 2.0.2 - Fix threatscore KeyError
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Update to new secret key credential type
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Hybrid Analysis](https://www.hybrid-analysis.com/)

## References

* [Hybrid Analysis](https://www.hybrid-analysis.com/)