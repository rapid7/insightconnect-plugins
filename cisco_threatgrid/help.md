# Description

[Cisco ThreatGrid](https://www.cisco.com/c/en/us/products/security/threat-grid/index.html) combines advanced sandboxing with threat intelligence into one unified solution to protect organizations from malware.
 The Cisco ThreatGrid InsightConnect plugin allows you to retrieve malware reports, report samples and URLs for analysis to server.

# Key Features

* Retrieve sample reports by domain, ID and SHA256
* Report samples and URLs for analysis

# Requirements

* Cisco ThreatGrid server's region
* Cisco ThreatGrid API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Enter API key e.g. 8lzx2lnr7uwyu27abc7jjo0ezo3|None|8lzx2lnr7uwyu27abc7jjo0ezo3|
|region|string|US|True|Select a region e.g. US|['US', 'Europe']|US|
|ssl_verify|boolean|False|True|SSL verify|None|False|

Example input:

```
{
  "api_key": "8lzx2lnr7uwyu27abc7jjo0ezo3",
  "region": "US",
  "ssl_verify": false
}
```

## Technical Details

### Actions

#### Search for a Sample Report by URL

This action is used to search for a sample report matching the given domain. e.g. rapid7.com.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain to search for|None|example.com|

Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sample_report|sample_report|True|Sample report matching the given domain|

Example output:

```
{
  "sample_report": {
    "properties": {},
    "tags": [],
    "vm_runtime": 120,
    "md5": "01e083cf123affd286e285684f6fe014",
    "private": false,
    "organization_id": 93361,
    "state": "succ",
    "login": "testguy",
    "sha1": "19149708ad7e2bddb1d302623f086b4c37631c06",
    "sample": "c9cd3526cf122367ae81e97f3d75f19a",
    "filename": "www.rapid7.com_.url",
    "analysis": {
      "metadata": {
        "sandcastle_env": {
          "controlsubject": "win7-x64-intel-2018.08.09",
          "vm": "win7-x64",
          "vm_id": "c9cd3526cf122367ae81e97f3d75f19a",
          "sample_executed": 1561487649,
          "analysis_end": "2019-06-25T18:36:45Z",
          "analysis_features": [],
          "analysis_start": "2019-06-25T18:33:23Z",
          "display_name": "Windows 7 64-bit",
          "run_time": 120,
          "sandcastle": "3.5.33.16246.1a4501ed0-1",
          "current_os": "7601.18798.amd64fre.win7sp1_gdr.150316-1654"
        },
        "submitted_file": {
          "magic": "MS Windows 95 Internet shortcut text (URL=<http://www.rapid7.com>), ASCII text",
          "sha1": "19149708ad7e2bddb1d302623f086b4c37631c06",
          "filename": "www.rapid7.com_.url",
          "sha256": "ddb5cd39884a96aedcc64a3609b9b61916a1902c6ca881f6707438ef66b0a6ec",
          "type": "url",
          "md5": "01e083cf123affd286e285684f6fe014"
        },
        "general_details": {
          "report_created": "2019-06-25T18:36:55Z",
          "sandbox_version": "pilot-d",
          "sandbox_id": "mtv-work-060"
        },
        "malware_desc": [
          {
            "sha1": "19149708ad7e2bddb1d302623f086b4c37631c06",
            "magic": "MS Windows 95 Internet shortcut text (URL=<http://www.rapid7.com>), ASCII text",
            "filename": "www.rapid7.com_.url",
            "size": 45,
            "sha256": "ddb5cd39884a96aedcc64a3609b9b61916a1902c6ca881f6707438ef66b0a6ec",
            "type": "url",
            "md5": "01e083cf123affd286e285684f6fe014"
          }
        ],
        "analyzed_file": {
          "magic": "MS Windows 95 Internet shortcut text (URL=<http://www.rapid7.com>), ASCII text",
          "sha1": "19149708ad7e2bddb1d302623f086b4c37631c06",
          "filename": "www.rapid7.com_.url",
          "sha256": "ddb5cd39884a96aedcc64a3609b9b61916a1902c6ca881f6707438ef66b0a6ec",
          "type": "url",
          "md5": "01e083cf123affd286e285684f6fe014"
        }
      },
      "behaviors": [
        {
          "name": "js-uses-fromcharcode",
          "threat": 40,
          "title": "JavaScript Obfuscation Using \"fromCharCode()\" Function"
        },
        {
          "name": "http-response-redirect",
          "threat": 25,
          "title": "HTTP Redirection Response"
        },
        {
          "name": "network-communications-http-get-url",
          "threat": 6,
          "title": "Outbound HTTP GET Request From URL Submission"
        },
        {
          "name": "modified-file-in-user-dir",
          "threat": 56,
          "title": "Process Modified File in a User Directory"
        },
        {
          "name": "js-contains-massive-strings",
          "threat": 64,
          "title": "Javascript Contains an Excessively Long String"
        },
        {
          "name": "network-dns-safe-categories",
          "threat": 19,
          "title": "Cisco Umbrella Detected A Likely Benign Domain"
        },
        {
          "name": "network-fast-flux-domain",
          "threat": 7,
          "title": "DNS Response Contains Low Time to Live (TTL) Value"
        },
        {
          "name": "network-only-safe-domains-contacted",
          "threat": 19,
          "title": "Sample Contacts Only Benign Domains"
        }
      ],
      "threat_score": 64
    },
    "status": "job_done",
    "submitted_at": "2019-06-25T18:33:22Z",
    "sha256": "ddb5cd39884a96aedcc64a3609b9b61916a1902c6ca881f6707438ef66b0a6ec"
  }
}
```

#### Search for a Sample Report by SHA256

This action is used to search for a sample report matching the given hash. e.g. 95fe2192da12930617b37419574exxx.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|sha256|string|None|True|SHA256 hash|None|02699626f388ed830012e5b787640e71c56d42d8|

Example input:

```
{
  "sha256": "02699626f388ed830012e5b787640e71c56d42d8"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sample_report_list|sample_report|True|Sample report list matching the given hash|

Example output:

```
{
  "sample_report_list": [
    {
      "properties": {},
      "tags": [
        "EICAR"
      ],
      "vm_runtime": 300,
      "md5": "6c9653ef2e223af8fc480c70423250fe",
      "private": false,
      "organization_id": 93361,
      "state": "succ",
      "login": "testguy",
      "sha1": "042980244914e98de9b96abf218f6c926cfed2ec",
      "sample": "87e6c357fafbc2cfcec1e1432aa03eee",
      "filename": "aadroid.net_.url",
      "analysis": {
        "metadata": {
          "sandcastle_env": {
            "controlsubject": "win7-x64-intel-2018.08.09",
            "vm": "win7-x64",
            "vm_id": "87e6c357fafbc2cfcec1e1432aa03eee",
            "sample_executed": 1561476420,
            "analysis_end": "2019-06-25T15:32:25Z",
            "analysis_features": [],
            "analysis_start": "2019-06-25T15:26:13Z",
            "display_name": "Windows 7 64-bit",
            "run_time": 300,
            "sandcastle": "3.5.33.16246.1a4501ed0-1",
            "current_os": "7601.18798.amd64fre.win7sp1_gdr.150316-1654"
          },
          "submitted_file": {
            "magic": "MS Windows 95 Internet shortcut text (URL=<http://aadroid.net>), ASCII text",
            "sha1": "042980244914e98de9b96abf218f6c926cfed2ec",
            "filename": "aadroid.net_.url",
            "sha256": "95fe2192da12930617b37419574e0e2800e61be0cd8958de2aea44d2053b9699",
            "type": "url",
            "md5": "6c9653ef2e223af8fc480c70423250fe"
          },
          "general_details": {
            "report_created": "2019-06-25T15:32:28Z",
            "sandbox_version": "pilot-d",
            "sandbox_id": "mtv-work-034"
          },
          "malware_desc": [
            {
              "sha1": "042980244914e98de9b96abf218f6c926cfed2ec",
              "magic": "MS Windows 95 Internet shortcut text (URL=<http://aadroid.net>), ASCII text",
              "filename": "aadroid.net_.url",
              "size": 42,
              "sha256": "95fe2192da12930617b37419574e0e2800e61be0cd8958de2aea44d2053b9699",
              "type": "url",
              "md5": "6c9653ef2e223af8fc480c70423250fe"
            }
          ],
          "analyzed_file": {
            "magic": "MS Windows 95 Internet shortcut text (URL=<http://aadroid.net>), ASCII text",
            "sha1": "042980244914e98de9b96abf218f6c926cfed2ec",
            "filename": "aadroid.net_.url",
            "sha256": "95fe2192da12930617b37419574e0e2800e61be0cd8958de2aea44d2053b9699",
            "type": "url",
            "md5": "6c9653ef2e223af8fc480c70423250fe"
          }
        },
        "behaviors": [
          {
            "name": "network-file-downloaded-to-disk",
            "threat": 27,
            "title": "File Downloaded to Disk"
          },
          {
            "name": "js-uses-fromcharcode",
            "threat": 40,
            "title": "JavaScript Obfuscation Using \"fromCharCode()\" Function"
          },
          {
            "name": "url-not-found",
            "threat": 6,
            "title": "URL Resulted in 404 or Empty File"
          },
          {
            "name": "network-communications-http-get-url",
            "threat": 6,
            "title": "Outbound HTTP GET Request From URL Submission"
          },
          {
            "name": "http-response-server-error",
            "threat": 25,
            "title": "HTTP Server Error Response"
          }
        ],
        "threat_score": 40
      },
      "status": "job_done",
      "submitted_at": "2019-06-25T15:26:11Z",
      "sha256": "95fe2192da12930617b37419574e0e2800e61be0cd8958de2aea44d2053b9699"
    }
  ]
}
```

#### Submit Sample

This action submits a sample to Threat Grid for analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|callback_url|string|None|False|A URL where the results will `POST` to, upon completion of analysis|None|http://www.example.com|
|email_notification|boolean|None|False|If true, sends an email to the email address of the user that submitted the sample, upon completion of the sample analysis|None|False|
|network_exit|string|None|False|Any outgoing network traffic that is generated during the analysis to appear to exit from the Network Exit Location|None|US - Pennsylvania - Philadelphia|
|playbook|string|None|False|Name of a playbook to apply to this sample run|None|Random Cursor Movement with Image Recognition|
|private|boolean|True|False|If true mark sample as private, if false mark sample as public|None|False|
|sample|file|None|True|The sample file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
|sample_filename|string|None|False|Filename to use to override the default filename|None|example.exe|
|sample_password|string|None|False|Password used to open the submitted archive or document|None|password|
|tags|string|None|False|A comma-separated list of tags applied to this sample|None|spyware, malware, phishing|
|vm|string|None|False|A string identifying a specific VM to use. See the linked configuration endpoint|None|rcn-work-022|

Example input:

```
{
  "callback_url": "http://www.example.com",
  "email_notification": false,
  "network_exit": "US - Pennsylvania - Philadelphia",
  "playbook": "Random Cursor Movement with Image Recognition",
  "private": false,
  "sample": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "sample_filename": "example.exe",
  "sample_password": "password",
  "tags": "spyware, malware, phishing",
  "vm": "rcn-work-022"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|submit_sample_results|False|Results from submit sample|

Example output:

```
{
  "results": {
    "api_version": 2,
    "id": 413318,
    "data": {
      "tags": [],
      "md5": "180986f2b6d5bb4479f7da95bebbf760",
      "submission_id": 766250744,
      "state": "wait",
      "login": "user",
      "sha1": "27dec70746d6867f24ed30b73d8c1ada9dc88351",
      "filename": "payload",
      "status": "pending",
      "submitted_at": "2019-07-08T13:39:22Z",
      "id": "8efae0f536015fef89ca6558f27a9a9a",
      "sha256": "dd3d94e544a7bfff8249a6f87fcfebb0041c1681fe075afb9c280dea39237358"
    }
  }
}

```

#### Get Sample Analysis

This action retrieves analysis on a sample with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|sample_id|string|None|True|ID in ThreatGrid of sample|None|232526zz0a501081e3058f6hwdfcfd7mp|

Example input:

```
{
  "sample_id": "232526zz0a501081e3058f6hwdfcfd7mp"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|annotations_report|annotations_report|False|Annotations analysis|
|artifact_report|artifact_report|False|Artifact analysis|
|iocs_report|iocs_report|False|IOCs analysis|
|metadata_report|metadata_report|False|Metadata analysis|
|network_streams_report|network_streams_report|False|Network streams analysis|
|processes_report|processes_report|False|Processes analysis|

Example output:

```
{
  "artifact_report": {
    "api_version": 2,
    "id": 8386878,
    "data": {
      "items": [
        {
          "antivirus": {},
          "origin": "submitted",
          "path": "687cc45706ffc2fc51fe01b25b2fd7a8e4cadd95",
          "mime-type": "message/rfc822; charset=us-ascii",
          "created-time": 0,
          "sha256": "becc98b3fa5a6a8959ffcfac516a3ed1481aeeb80205eb04f34c76d0cdd27dae",
          "sha1": "687cc45706ffc2fc51fe01b25b2fd7a8e4cadd95",
          "md5": "cc0e6e2dc4081ced9cd62fc62ef68d15",
          "entropy": 0,
          "size": 12172,
          "magic-type": "RFC 822 mail, ASCII text, with CRLF line terminators",
          "relation": {}
        }
      ]
    }
  },
  "iocs_report": {
    "api_version": 2,
    "id": 6787955,
    "data": {}
  },
  "network_streams_report": {
    "api_version": 2,
    "id": 286846,
    "data": {}
  },
  "processes_report": {
    "api_version": 2,
    "id": 2074130
    "data": {
      "items": []
    }
  },
  "annotations_report": {
    "api_version": 2,
    "id": 5340769,
    "data": {}
  },
  "metadata_report": {
    "api_version": 2,
    "id": 2697921,
    "data": {
      "general_details": {
        "report_created": 1562934267,
        "sandbox_id": "mtv-work-081",
        "sandbox_version": "pilot-d"
      },
      "malware_desc": [],
      "sandcastle_env": {
        "analysis_end": 1562934267,
        "sandcastle": "3.5.34.16298.d46c32a00-1",
        "current_os": "7601.18798.amd64fre.win7sp1_gdr.150316-1654",
        "run_time": 300,
        "controlsubject": "win7-x64-intel-2018.08.09",
        "display_name": "Windows 7 64-bit",
        "vm_id": "8c91e0431f14f5ce405e00ec6b9192b7",
        "analysis_start": 1562934267,
        "vm": "win7-x64",
        "analysis_features": []
      }
    }
  }
}

```

#### Submit URL

This action is used to submit a URL to Threat Grid for analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|callback_url|string|None|False|A URL where the results will POST to, upon completion of analysis|None|http://www.example.com|
|email_notification|boolean|None|False|If true, sends an email to the email address of the user that submitted the sample, upon completion of the sample analysis|None|False|
|network_exit|string|None|False|Any outgoing network traffic that is generated during the analysis to appear to exit from the Network Exit Location|None|US - Pennsylvania - Philadelphia|
|playbook|string|None|False|Name of a playbook to apply to this sample run|None|Random Cursor Movement with Image Recognition|
|private|string|None|False|Mark sample as private if not set to 'false' or any other value|None|False|
|tags|string|None|False|A comma-separated list of tags applied to this sample|None|malware, trojan, phishing|
|url|string|None|True|The URL to submit for analysis|None|http://www.example.com|
|vm|string|None|False|A string identifying a specific VM to use. See the linked configuration endpoint|None|rcn-work-022|

Example input:

```
{
  "callback_url": "http://www.example.com",
  "email_notification": false,
  "network_exit": "US - Pennsylvania - Philadelphia",
  "playbook": "Random Cursor Movement with Image Recognition",
  "private": false,
  "tags": "malware, trojan, phishing",
  "url": "http://www.example.com",
  "vm": "rcn-work-022"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|submit_sample_results|False|Results from submit sample|

Example output:

```
{
  "results": {
    "api_version": 2,
    "id": 8359575,
    "data": {
      "tags": [],
      "md5": "09c1bcbccc67632319c9f21f8d10db22",
      "submission_id": 828013007,
      "state": "wait",
      "login": "elijahmm",
      "sha1": "a29459aba4c45c1ec9486d5e1ebb5691c679d5a5",
      "filename": "sample",
      "status": "pending",
      "submitted_at": "2019-10-28T01:57:20Z",
      "id": "2ff0509ce5ba06ecda1716ac54129132",
      "sha256": "e0abbdb65e182ac51bc6a91b1c2ea4f6ff264e1c1827170616c7af37ad8e57ba"
    }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### ClamAV_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Product|string|False|Product|
|Product Version|string|False|Product version|
|Result|string|False|Result|
|Signature Version|string|False|Signature version|

#### actual_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|MD5|string|False|MD5|
|SHA1|string|False|SHA1|
|SHA256|string|False|SHA256|

#### analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Behaviors|[]behaviors|False|Behaviors|
|Metadata|metadata|False|Metadata|
|Threat Score|integer|False|Threat score|

#### analyzed_file

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Filename|string|False|Filename|
|Magic|string|False|Magic|
|MD5|string|False|MD5|
|SHA1|string|False|SHA1|
|SHA256|string|False|SHA256|
|Type|string|False|Type|

#### annotation_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Network|[]annotation_network|False|Network|

#### annotation_network

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ASN|integer|False|ASN|
|Country|string|False|Country|
|Country Name|string|False|Country name|
|IP|string|False|IP|
|Organization|string|False|Organization|
|Reverse DNS|[]string|False|Reverse DNS list|
|TS|integer|False|TS|

#### annotations_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Items|annotation_network|False|Items|

#### annotations_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|API Version|integer|False|API version|
|Data|annotations_analysis|False|Data|
|ID|integer|False|ID|

#### antivirus_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Clam AV|ClamAV_artifact|False|Clam AV|
|Reversing Labs|reversing_labs_artifact|False|Reversing labs|
|Yara|[]yara_artifact|False|Yara|

#### artifact_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Items|[]artifact_analysis_item|False|Items|

#### artifact_analysis_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Antivirus|antivirus_artifact|False|Antivirus|
|Created-Time|number|False|Created-time|
|Created By|[]integer|False|Created by|
|Entropy|float|False|Entropy|
|Executed From|[]integer|False|Executed from|
|Forensics|forensics_artifact|False|Forensics|
|Magic-Type|string|False|Magic-type|
|MD5|string|False|MD5|
|Mime-Type|string|False|Mime-type|
|Modified By|[]integer|False|Modified by|
|Origin|string|False|Origin|
|Path|string|False|Path|
|Read By|[]integer|False|Read by|
|Relation|relation_artifact|False|Relation|
|SHA1|string|False|SHA1|
|SHA256|string|False|SHA256|
|Size|integer|False|Size|
|Type|string|False|Type|
|Whitelist|[]object|False|Whitelist|

#### artifact_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|API Version|integer|False|API version|
|Data|artifact_analysis|False|Data|
|ID|integer|False|ID|

#### behaviors

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Name|
|Threat|integer|False|Threat|
|Title|string|False|Title|

#### certificate_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Actual|actual_artifact|False|Actual|
|Certificates|[]certificates_artifact|False|Certificates|
|Issuer|string|False|Issuer|
|Program|string|False|Program|
|Serial|string|False|Serial|
|Signature Match|boolean|False|Signature match|
|Signed|signed_artifact|False|Signed|
|Subject|string|False|Subject|
|Timestamp|string|False|Timestamp|
|URL|string|False|URL|

#### certificates_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Issuer|string|False|Issuer|
|Not After|integer|False|Not after|
|Not Before|integer|False|Not before|
|Serial|string|False|Serial|
|Subject|string|False|Subject|

#### classification_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Family Name|string|False|Family name|
|Platform|string|False|Platform|
|Type|string|False|Type|

#### data_metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|General Details|general_details_metadata|False|General details|
|Malware Desc|[]malware_desc_metadata|False|Malware desc|
|Sandcastle Env|sandcastle_env_metadata|False|Sandcastle env|

#### dos_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Checksum|integer|False|Checksum|
|Header Relocations|integer|False|Header relocations|
|Initial Code Segment|integer|False|Initial code segment|
|Initial Instruction Pointer|integer|False|Initial instruction pointer|
|Initial Stack Pointer|integer|False|Initial stack pointer|
|Initial Stack Segment|integer|False|Initial stack segment|
|Pages|integer|False|Pages|
|Size In Paragraphs|integer|False|Size in paragraphs|

#### entry_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Base Address|string|False|Base address|
|Size|string|False|Size|

#### error_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|error_process_data|False|Data|
|Timestamp|float|False|Timestamp|
|Type|string|False|Type|

#### error_process_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Error Status|string|False|Error status|
|NT Status|string|False|NT status|
|Number Of Params|integer|False|Number of params|
|Parameters|string|False|Parameters|

#### file_info_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Company Name|string|False|Company name|
|Copyright|string|False|Copyright|
|File Description|string|False|File description|
|File Version|string|False|File version|
|Internal Name|string|False|Internal name|
|Original File Name|string|False|Original file name|
|Product Name|string|False|Product name|
|Product Version|string|False|Product version|

#### file_transaction_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Path|string|False|Path|
|Rolled Back|boolean|False|Rolled back|

#### forensics_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Exports|[][]string|False|Exports|
|File Info|file_info_artifact|False|File info|
|Headers|headers_artifact|False|Headers|
|Imports|[]imports_artifact|False|Imports|
|Internal Checksum Match|boolean|False|Internal checksum match|
|Resources|[]resources_artifact|False|Resources|
|Sections|[]sections_artifact|False|Sections|
|Signatures|[]string|False|Signatures|

#### general_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Report Created|string|False|Report created|
|Sandbox ID|string|False|Sandbox ID|
|Sandbox Version|string|False|Sandbox version|

#### general_details_metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Report Created|integer|False|Report created|
|Sandbox ID|string|False|Sandbox ID|
|Sandbox Version|string|False|Sandbox version|

#### headers_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Dos|dos_artifact|False|Dos|
|PE|pe_artifact|False|PE|

#### imports_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DLL|string|False|DLL|
|Entries|[][]string|False|Entries|

#### ioc_analysis_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Category|[]string|False|Category|
|Confidence|integer|False|Confidence|
|Data|[]ioc_data|False|Data|
|Description|string|False|Description|
|Heuristic Coefficient|float|False|Heuristic coefficient|
|Hits|integer|False|Hits|
|IOC|string|False|Indicator of compromise|
|Mitre-Tactics|[]string|False|Mitre-tactics|
|Severity|integer|False|Severity|
|Tags|[]string|False|Tags|
|Title|string|False|Title|
|Truncated|boolean|False|Truncated|

#### ioc_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Antivirus Product|string|False|Antivirus product|
|Antivirus Result|string|False|Antivirus result|
|Artifact ID|integer|False|Artifact ID|
|Path|string|False|Path|

#### iocs_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Items|[]ioc_analysis_item|False|Items|

#### iocs_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|API Version|integer|False|API version|
|Data|iocs_analysis|False|Data|
|ID|integer|False|ID|

#### malware_desc

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Filename|string|False|Filename|
|Magic|string|False|Magic|
|MD5|string|False|MD5|
|SHA1|string|False|SHA1|
|SHA256|string|False|SHA256|
|Size|integer|False|Size|
|Type|string|False|Type|

#### malware_desc_metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Filename|string|False|Filename|
|Magic|string|False|Magic|
|MD5|string|False|MD5|
|SHA1|string|False|SHA1|
|SHA256|string|False|SHA256|
|Size|integer|False|Size|
|Type|string|False|Type|

#### memory_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Allocation Type|[]string|False|Allocation type|
|Entry|[]entry_process|False|Entry|
|Process|string|False|Process|
|Process Handle|string|False|Process handle|
|Protect|[]string|False|Protect|
|Zero Bits|integer|False|Zero bits|

#### metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analyzed File|analyzed_file|False|Analyzed file|
|General Details|general_details|False|General details|
|Malware Description|[]malware_desc|False|Malware description|
|Sandcastle ENV|sandcastle_env|False|Sandcastle ENV|
|Submitted File|analyzed_file|False|Submitted file|

#### metadata_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|API Version|integer|False|API version|
|Data|data_metadata|False|Data|
|ID|integer|False|ID|

#### network_decoded

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Actual Content Type|string|False|Actual content type|
|Body Len|integer|False|Body len|
|Decoded URL|string|False|Decoded URL|
|Filesystem Access User ID|[]string|False|Filesystem access user ID|
|Headers|network_headers|False|Headers|
|Host|string|False|Host|
|Method|string|False|Method|
|Port|integer|False|Port|
|Request Filename|string|False|Request filename|
|Request Path|string|False|Request path|
|SHA256|string|False|SHA256|
|TS|float|False|TS|
|Type|string|False|Type|
|URL|string|False|URL|
|Version|string|False|Version|

#### network_decoded_list

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Decoded|[]network_decoded|False|List of decoded results|

#### network_headers

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Cache-Control|string|False|Cache-control|
|Content-Length|string|False|Content-length|
|Host|string|False|Host|
|User-Agent|string|False|User-agent|

#### network_relation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Process|[]integer|False|Process|

#### network_streams_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Bytes|integer|False|Bytes|
|Bytes Missed|integer|False|Bytes missed|
|Bytes Orig|integer|False|Bytes orig|
|Bytes Orig Payload|integer|False|Bytes orig payload|
|Bytes Payload|integer|False|Bytes payload|
|Bytes Resp|integer|False|Bytes resp|
|Bytes Resp Payload|integer|False|Bytes resp payload|
|Conn State|string|False|Conn state|
|Decoded|[]network_decoded_list|False|Decoded|
|Dst|string|False|Dst|
|Dst Port|integer|False|Dst port|
|Duration|float|False|Duration|
|History|string|False|History|
|Packets|integer|False|Packets|
|Packets Orig|integer|False|Packets orig|
|Packets Resp|integer|False|Packets resp|
|Protocol|string|False|Protocol|
|Relation|network_relation|False|Relation|
|Service|string|False|Service|
|Session|integer|False|Session|
|Src|string|False|Src|
|Src Port|integer|False|Src port|
|Transport|string|False|Transport|
|TS Begin|float|False|TS begin|
|TS End|float|False|TS end|
|UID|string|False|UID|

#### network_streams_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|API Version|integer|False|API version|
|Data|network_streams_analysis|False|Data|
|ID|integer|False|ID|

#### optional_header_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Actual Checksum|integer|False|Actual checksum|
|Claimed Checksum|integer|False|Claimed checksum|
|Entrypoint Address|integer|False|Entrypoint address|
|File Alignment|integer|False|File alignment|
|Linker Major Version|integer|False|Linker major version|
|Linker Minor Version|integer|False|Linker minor version|
|Loader Flag|integer|False|Loader flag|
|Number Of Relative Virtual Addresses And Sizes|integer|False|Number of relative virtual addresses and sizes|
|Reserved Field|integer|False|Reserved field|
|Section Alignment|integer|False|Section alignment|
|Size|integer|False|Size|
|Subsystem|integer|False|Subsystem|
|Type|integer|False|Type|

#### pe_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Certificate|certificate_artifact|False|Certificate|
|Import Hash|string|False|Import hash|
|Machine|string|False|Machine|
|Number Of Symbols|integer|False|Number of symbols|
|Optional Header|optional_header_artifact|False|Optional header|
|Signed|boolean|False|Signed|
|Timestamp|integer|False|Timestamp|
|TLS Callback Address|integer|False|TLS callback address|
|TLS Callback Relative Virtual Address|integer|False|TLS callback relative virtual address|
|VT Import Hash|string|False|VT import hash|

#### process_analysis_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analyzed Because|string|False|Analyzed because|
|Atoms Added|[]string|False|Atoms added|
|Children|[]string|False|Children|
|Errors|[]error_process|False|Errors|
|File Transactions|[]file_transaction_process|False|File transactions|
|Files Checked|[]string|False|Files checked|
|Files Created|[]string|False|Files created|
|Files Deleted|[]string|False|Files deleted|
|Files Modified|[]string|False|Files modified|
|Files Read|[]string|False|Files read|
|KpID|string|False|KpID|
|Memory|[]memory_process|False|Memory|
|Monitored|boolean|False|Monitored|
|Mutants Created|[]string|False|Mutants created|
|Mutants Opened|[]string|False|Mutants opened|
|New|boolean|False|New|
|Parent|string|False|Parent|
|PID|integer|False|PID|
|PpID|integer|False|PpID|
|Process Name|string|False|Process name|
|Registry Keys Created|[]object|False|Registry keys created|
|Registry Keys Deleted|[]string|False|Registry keys deleted|
|Registry Keys Modified|[]object|False|Registry keys modified|
|Registry Keys Opened|[]object|False|Registry keys opened|
|Registry Keys Read|[]object|False|Registry keys read|
|Sockets|[]object|False|Sockets|
|Sockets Traffic|[]object|False|Sockets traffic|
|Startup Info|startup_info_process|False|Startup info|
|Threads|[]threads_process|False|Threads|
|Time|string|False|Time|

#### processes_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Items|[]process_analysis_item|False|Items|

#### processes_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|API Version|integer|False|API version|
|Data|processes_analysis|False|Data|
|ID|integer|False|ID|

#### properties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Metadata|object|False|Metadata|

#### query_hash_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|SHA256|string|False|SHA256|

#### relation_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Contains|[]string|False|Contains|
|Extracted From|[]string|False|Extracted from|
|Network|[]string|False|Network|
|Process|[]string|False|Process|

#### resources_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Codepage|integer|False|Codepage|
|Language|string|False|Language|
|Locale|string|False|Locale|
|Magic|string|False|Magic|
|MIME|string|False|MIME|
|Name|string|False|Name|
|Offset|integer|False|Offset|
|Path|string|False|Path|
|Resource SHA256|string|False|Resource SHA256|
|Size|integer|False|Size|
|Sublanguage|string|False|Sublanguage|
|Type|string|False|Type|

#### reversing_labs_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Classification|classification_artifact|False|Classification|
|First Seen|string|False|First seen|
|Last Seen|string|False|Last seen|
|Query Hash|query_hash_artifact|False|Query hash|
|Scanner Count|integer|False|Scanner count|
|Scanner Match|integer|False|Scanner match|
|Status|string|False|Status|
|Threat Level|integer|False|Threat level|
|Threat Name|string|False|Threat name|
|Trust Factor|integer|False|Trust factor|

#### sample_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analysis|analysis|False|Analysis|
|Filename|string|False|Filename|
|Login|string|False|Login|
|MD5|string|False|MD5|
|Organization ID|integer|False|Organization ID|
|Private|boolean|False|Private|
|Properties|properties|False|Properties|
|Sample|string|False|Sample|
|SHA1|string|False|SHA1|
|SHA256|string|False|SHA256|
|State|string|False|State|
|Status|string|False|Status|
|Submitted At|string|False|Submitted at|
|Tags|[]string|False|Tags|
|VM Runtime|integer|False|VM runtime|

#### sandcastle_env

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analysis End|string|False|Analysis end|
|Analysis Features|[]object|False|Analysis features|
|Analysis Start|string|False|Analysis start|
|Control Subject|string|False|Control subject|
|Current OS|string|False|Current OS|
|Display Name|string|False|Display name|
|Run Time|integer|False|Run time|
|Sample Executed|integer|False|Sample executed|
|Sandcastle|string|False|Sandcastle|
|VM|string|False|VM|
|VM ID|string|False|VM ID|

#### sandcastle_env_metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analysis End|integer|False|Analysis end|
|Analysis Start|integer|False|Analysis start|
|Control Subject|string|False|Control subject|
|Current OS|string|False|Current OS|
|Display Name|string|False|Display name|
|Run Time|integer|False|Run time|
|Sample Executed|integer|False|Sample executed|
|Sandcastle|string|False|Sandcastle|
|VM|string|False|VM|
|VM ID|string|False|VM ID|

#### sections_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Address|integer|False|Address|
|Characteristics|[]string|False|Characteristics|
|Data Pointer|integer|False|Data pointer|
|Entropy|float|False|Entropy|
|Entropy Type|[]string|False|Entropy type|
|Section|string|False|Section|
|Section Hash|string|False|Section hash|
|Size|integer|False|Size|
|Virtual Size|integer|False|Virtual size|

#### signed_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|SHA256|string|False|SHA256|

#### startup_info_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Command Line|string|False|Command line|
|Current Directory|string|False|Current directory|
|Desktop Info|string|False|Desktop info|
|DLL Path|string|False|DLL path|
|Image Pathname|string|False|Image pathname|
|Runtime Data|string|False|Runtime data|
|Shell Info|string|False|Shell info|
|TID|string|False|TID|
|UpID|integer|False|UpID|
|Uthread|integer|False|Uthread|
|Window Title|string|False|Window title|

#### submit_sample_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Filename|string|False|Filename|
|ID|string|False|ID|
|Login|string|False|Login|
|MD5|string|False|MD5|
|OS|string|False|OS|
|SHA1|string|False|SHA1|
|SHA256|string|False|SHA256|
|State|string|False|State|
|Status|string|False|Status|
|Submission ID|integer|False|Submission ID|
|Submitted At|string|False|Submitted at|
|Tags|[]string|False|Tags|
|VM|string|False|VM|

#### submit_sample_results

|Name|Type|Required|Description|
|----|----|--------|-----------|
|API Version|integer|False|API version|
|Data|submit_sample_data|False|Data|
|ID|integer|False|ID|

#### threads_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Client ID|integer|False|Client ID|
|Create Suspended|string|False|Create suspended|
|Process|string|False|Process|
|Process Handle|string|False|Process handle|
|Return|integer|False|Return|
|Thread|string|False|Thread|

#### yara_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|ID|string|False|ID|
|Tags|[]string|False|Tags|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 3.0.1 - Fix issue with set filename from file sample
* 3.0.0 - Add default value and change type to boolean for input private in action Submit Sample
* 2.1.0 - Remove quotes in titles and descriptions in custom types in plugin.spec | Remove a blank lines in plugin.spec | Change type in tags in submit_sample_data custom type | Change description for region and API key in connection | Change description for SHA256 input parameter and sample report list output parameter in Search for Sample Report by SHA256 action | Change description for sample report output parameter in Search for Sample Report by Domain action | Change example for email notification input parameter in Submit URL and Submit Sample actions | Change description for network streams report and metadata report output parameters in Get Sample Analysis action | Add custom types in help.md | Replace ConnectionTestException with PluginException in Search for Sample Report by Domain action | Update connection test to use ConnectionTestException | Add more user-friendly cause and assistance messages for status codes using PluginException | Update existing PluginExceptions | Add types for arguments in methods in api.py | Change names for arguments in search_sha256, search_domain, search_id methods in api.py | Add KeyError exception in Submit Sample action | Add IndexError exception in Search for Sample Report by Domain action
* 2.0.0 - Fix issue where Search for Sample by Domain would fail | Removed Search for Sample by ID | Update to Search for Sample Report by SHA256 to only return one output object
* 1.2.2 - New action Submit URL
* 1.2.1 - Bug fix for action Get Sample Analysis
* 1.2.0 - New action Get Sample Analysis
* 1.1.0 - New action Submit Sample
* 1.0.0 - Initial plugin

# Links

## References

* [Cisco ThreatGrid](https://www.cisco.com/c/en/us/products/security/threat-grid/index.html)
* [Cisco ThreatGrid API](https://panacea.threatgrid.com/mask/doc/mask/index)

