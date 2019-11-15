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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API Key|None|
|region|string|US|True|Region|['US', 'Europe']|

## Technical Details

### Actions

#### Search for a Sample Report by URL

This action is used to search for a sample report matching the given domain. e.g. rapid7.com.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain to search for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sample_report|sample_report|True|Sample report|

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

#### Search for a Sample Report by ID

This action is used to search for a sample report matching the given ID. e.g. rapid7.com.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sample_id|string|None|True|Sample ID to search for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sample_report|sample_report|True|Sample report|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sha256|string|None|True|SHA256|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sample_report_list|[]sample_report|True|Sample report list|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|callback_url|string|None|False|A URL where the results will `POST` to, upon completion of analysis|None|
|email_notification|boolean|None|False|If true, sends an email to the email address of the user that submitted the sample, upon completion of the sample analysis|None|
|network_exit|string|None|False|Any outgoing network traffic that is generated during the analysis to appear to exit from the Network Exit Location|None|
|playbook|string|None|False|Name of a playbook to apply to this sample run|None|
|private|string|None|False|If present, and set to any value but `false` the sample will be marked private|None|
|sample|file|None|True|The sample file|None|
|sample_filename|string|None|False|Filename to use to override the default filename|None|
|sample_password|string|None|False|Password used to open the submitted archive or document|None|
|tags|string|None|False|A comma-separated list of tags applied to this sample|None|
|vm|string|None|False|A string identifying a specific VM to use. See the linked configuration endpoint|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|False|Results from submit sample|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sample_id|string|None|True|ID in ThreadGrid of sample|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|annotations_report|annotations_report|False|Annotations analysis|
|artifact_report|artifact_report|False|Artifact analysis|
|iocs_report|iocs_report|False|IOCs analysis|
|metadata_report|metadata_report|False|Metadata Analysis|
|network_streams_report|network_streams_report|False|Network Streams Report|
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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|callback_url|string|None|False|A URL where the results will `POST` to, upon completion of analysis|None|
|email_notification|boolean|None|False|If true, sends an email to the email address of the user that submitted the sample, upon completion of the sample analysis|None|
|network_exit|string|None|False|Any outgoing network traffic that is generated during the analysis to appear to exit from the Network Exit Location|None|
|playbook|string|None|False|Name of a playbook to apply to this sample run|None|
|private|string|None|False|If present, and set to any value but `false` the sample will be marked private|None|
|tags|string|None|False|A comma-separated list of tags applied to this sample|None|
|url|string|None|True|The URL to submit for analysis|None|
|vm|string|None|False|A string identifying a specific VM to use. See the linked configuration endpoint|None|

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

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.2 - New action Submit URL
* 1.2.1 - Bug fix for action Get Sample Analysis
* 1.2.0 - New action Get Sample Analysis
* 1.1.0 - New action Submit Sample
* 1.0.0 - Initial plugin

# Links

## References

* [Cisco ThreatGrid](https://www.cisco.com/c/en/us/products/security/threat-grid/index.html)
* [Cisco ThreatGrid API](https://panacea.threatgrid.com/mask/doc/mask/index)

