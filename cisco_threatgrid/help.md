# Cisco ThreatGrid

## About

[Cisco ThreatGrid](https://www.cisco.com/c/en/us/products/security/threat-grid/index.html) combines advanced sandboxing with threat intelligence into one unified solution to protect organizations from malware.

## Actions

### Search for a Sample Report by URL

This action is used to search for a sample report matching the given domain. e.g. rapid7.com.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain to search for|None|

#### Output

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

### Search for a Sample Report by ID

This action is used to search for a sample report matching the given ID. e.g. rapid7.com.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sample_id|string|None|True|Sample ID to search for|None|

#### Output

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

### Search for a Sample Report by SHA256

This action is used to search for a sample report matching the given hash. e.g. 95fe2192da12930617b37419574exxx.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sha256|string|None|True|SHA256|None|

#### Output

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

### Submit Sample

This action submits a sample to Threat Grid for analysis.

#### Input

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

#### Output

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

### Get Sample Analysis

This action retrieves analysis on a sample with the given ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sample_id|string|None|True|ID in ThreadGrid of sample|None|

#### Output

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

### Submit URL

This action is used to submit a URL to Threat Grid for analysis.

#### Input

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

#### Output

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

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API Key|None|
|region|string|US|True|Region|['US', 'Europe']|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Get a sample report

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - New action Submit Sample
* 1.2.0 - New action Get Sample Analysis
* 1.2.1 - Bug fix for action Get Sample Analysis
* 1.2.2 - New action Submit URL

## References

* [Cisco ThreatGrid](https://www.cisco.com/c/en/us/products/security/threat-grid/index.html)
* [Cisco ThreatGrid API](https://panacea.threatgrid.com/mask/doc/mask/index)

## Custom Output Types

### behaviors

|Name|Type|Required|Description|
|----|----|--------|-----------|
|name|string|False|Name|
|threat|integer|False|Threat|
|title|string|False|Title|

### analyzed_file

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filename|string|False|Filename|
|magic|string|False|Magic|
|md5|string|False|MD5|
|sha1|string|False|SHA1|
|sha256|string|False|SHA256|
|type|string|False|Type|

### general_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report_created|string|False|Report created|
|sandbox_id|string|False|Sandbox ID|
|sandbox_version|string|False|Sandbox version|

### malware_desc

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filename|string|False|Filename|
|magic|string|False|Magic|
|md5|string|False|MD5|
|sha1|string|False|SHA1|
|sha256|string|False|SHA256|
|size|integer|False|Size|
|type|string|False|Type|

### sandcastle_env

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analysis_end|string|False|Analysis end|
|analysis_features|[]object|False|Analysis features|
|analysis_start|string|False|Analysis start|
|controlsubject|string|False|Control Subject|
|current_os|string|False|Current OS|
|display_name|string|False|Display name|
|run_time|integer|False|Run time|
|sample_executed|integer|False|Sample executed|
|sandcastle|string|False|Sandcastle|
|vm|string|False|VM|
|vm_id|string|False|VM ID|

### metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analyzed_file|analyzed_file|False|Analyzed file|
|general_details|general_details|False|General details|
|malware_desc|[]malware_desc|False|Malware description|
|sandcastle_env|sandcastle_env|False|Sandcastle ENV|
|submitted_file|analyzed_file|False|Submitted file|

### analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|behaviors|[]behaviors|False|Behaviors|
|metadata|metadata|False|Metadata|
|threat_score|integer|False|Threat score|

### properties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|metadata|object|False|Metadata|

### sample_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analysis|analysis|False|Analysis|
|filename|string|False|Filename|
|login|string|False|Login|
|md5|string|False|MD5|
|organization_id|integer|False|Organization ID|
|private|boolean|False|Private|
|properties|properties|False|Properties|
|sample|string|False|Sample|
|sha1|string|False|SHA1|
|sha256|string|False|SHA256|
|state|string|False|State|
|status|string|False|Status|
|submitted_at|string|False|Submitted at|
|tags|[]string|False|Tags|
|vm_runtime|integer|False|VM runtime|

### submit_sample_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filename|string|False|Filename|
|id|string|False|ID|
|login|string|False|Login|
|md5|string|False|MD5|
|os|string|False|OS|
|sha1|string|False|SHA1|
|sha256|string|False|SHA256|
|state|string|False|State|
|status|string|False|Status|
|submission_id|integer|False|Submission ID|
|submitted_at|string|False|Submitted at|
|tags|[]object|False|Tags|
|vm|string|False|VM|

### submit_sample_results

|Name|Type|Required|Description|
|----|----|--------|-----------|
|api_version|integer|False|API version|
|data|submit_sample_data|False|Data|
|id|integer|False|ID|

### file_transaction_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|path|string|False|Path|
|rolled_back|boolean|False|Rolled back|

### error_process_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|error_status|string|False|Error status|
|nt_status|string|False|Nt status|
|number_of_params|integer|False|Number of params|
|parameters|string|False|Parameters|

### error_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|error_process_data|False|Data|
|timestamp|float|False|Timestamp|
|type|string|False|Type|

### entry_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|base_address|string|False|Base address|
|size|string|False|Size|

### memory_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|allocation_type|[]string|False|Allocation type|
|entry|[]entry_process|False|Entry|
|process|string|False|Process|
|process_handle|string|False|Process handle|
|protect|[]string|False|Protect|
|zero_bits|integer|False|Zero bits|

### startup_info_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|command_line|string|False|Command line|
|current_directory|string|False|Current directory|
|desktop_info|string|False|Desktop info|
|dll_path|string|False|Dll path|
|image_pathname|string|False|Image pathname|
|runtime_data|string|False|Runtime data|
|shell_info|string|False|Shell info|
|tid|string|False|Tid|
|upid|integer|False|Upid|
|uthread|integer|False|Uthread|
|window_title|string|False|Window title|

### threads_process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|client_id|integer|False|Client id|
|create_suspended|string|False|Create suspended|
|process|string|False|Process|
|process_handle|string|False|Process handle|
|return|integer|False|Return|
|thread|string|False|Thread|

### process_analysis_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analyzed_because|string|False|Analyzed because|
|atoms_added|[]string|False|Atoms added|
|children|[]string|False|Children|
|errors|[]error_process|False|Errors|
|file_transactions|[]file_transaction_process|False|File transactions|
|files_checked|[]string|False|Files checked|
|files_created|[]string|False|Files created|
|files_deleted|[]string|False|Files deleted|
|files_modified|[]string|False|Files modified|
|files_read|[]string|False|Files read|
|kpid|string|False|Kpid|
|memory|[]memory_process|False|Memory|
|monitored|boolean|False|Monitored|
|mutants_created|[]string|False|Mutants created|
|mutants_opened|[]string|False|Mutants opened|
|new|boolean|False|New|
|parent|string|False|Parent|
|pid|integer|False|Pid|
|ppid|integer|False|Ppid|
|process_name|string|False|Process name|
|registry_keys_created|[]object|False|Registry keys created|
|registry_keys_deleted|[]string|False|Registry keys deleted|
|registry_keys_modified|[]object|False|Registry keys modified|
|registry_keys_opened|[]object|False|Registry keys opened|
|registry_keys_read|[]object|False|Registry keys read|
|sockets|[]object|False|Sockets|
|sockets_traffic|[]object|False|Sockets traffic|
|startup_info|startup_info_process|False|Startup info|
|threads|[]threads_process|False|Threads|
|time|string|False|Time|

### ClamAV_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|product|string|False|Product|
|product_version|string|False|Product version|
|result|string|False|Result|
|signature_version|string|False|Signature version|

### classification_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|family_name|string|False|Family name|
|platform|string|False|Platform|
|type|string|False|Type|

### query_hash_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha256|string|False|SHA256|

### reversing_labs_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|classification|classification_artifact|False|Classification|
|first_seen|string|False|First seen|
|last_seen|string|False|Last seen|
|query_hash|query_hash_artifact|False|Query hash|
|scanner_count|integer|False|Scanner count|
|scanner_match|integer|False|Scanner match|
|status|string|False|Status|
|threat_level|integer|False|Threat level|
|threat_name|string|False|Threat name|
|trust_factor|integer|False|Trust factor|

### yara_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|description|string|False|Description|
|id|string|False|Id|
|tags|[]string|False|Tags|

### antivirus_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ClamAV|ClamAV_artifact|False|Clamav|
|reversing_labs|reversing_labs_artifact|False|Reversing labs|
|yara|[]yara_artifact|False|Yara|

### file_info_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|company_name|string|False|Company name|
|copyright|string|False|Copyright|
|file_description|string|False|File description|
|file_version|string|False|File version|
|internal_name|string|False|Internal name|
|original_file_name|string|False|Original file name|
|product_name|string|False|Product name|
|product_version|string|False|Product version|

### dos_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|checksum|integer|False|Checksum|
|header_relocations|integer|False|Header relocations|
|initial_code_segment|integer|False|Initial code segment|
|initial_instruction_pointer|integer|False|Initial instruction pointer|
|initial_stack_pointer|integer|False|Initial stack pointer|
|initial_stack_segment|integer|False|Initial stack segment|
|pages|integer|False|Pages|
|size_in_paragraphs|integer|False|Size in paragraphs|

### optional_header_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|actual_checksum|integer|False|Actual checksum|
|claimed_checksum|integer|False|Claimed checksum|
|entrypoint_address|integer|False|Entrypoint address|
|file_alignment|integer|False|File alignment|
|linker_major_version|integer|False|Linker major version|
|linker_minor_version|integer|False|Linker minor version|
|loader_flag|integer|False|Loader flag|
|number_of_rva_and_sizes|integer|False|Number of rva and sizes|
|reserved_field|integer|False|Reserved field|
|section_alignment|integer|False|Section alignment|
|size|integer|False|Size|
|subsystem|integer|False|Subsystem|
|type|integer|False|Type|

### actual_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|md5|string|False|Md5|
|sha1|string|False|Sha1|
|sha256|string|False|SHA256|

### certificates_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issuer|string|False|Issuer|
|not_after|integer|False|Not after|
|not_before|integer|False|Not before|
|serial|string|False|Serial|
|subject|string|False|Subject|

### signed_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha256|string|False|SHA256|

### certificate_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|actual|actual_artifact|False|Actual|
|certificates|[]certificates_artifact|False|Certificates|
|issuer|string|False|Issuer|
|program|string|False|Program|
|serial|string|False|Serial|
|signature_match|boolean|False|Signature match|
|signed|signed_artifact|False|Signed|
|subject|string|False|Subject|
|timestamp|string|False|Timestamp|
|url|string|False|URL|

### pe_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|certificate|certificate_artifact|False|Certificate|
|import_hash|string|False|Import hash|
|machine|string|False|Machine|
|number_of_symbols|integer|False|Number of symbols|
|optional_header|optional_header_artifact|False|Optional header|
|signed|boolean|False|Signed|
|timestamp|integer|False|Timestamp|
|tls_callback_addr|integer|False|TLS callback address|
|tls_callback_rva|integer|False|Tls callback rva|
|vt_import_hash|string|False|VT import hash|

### headers_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dos|dos_artifact|False|Dos|
|pe|pe_artifact|False|PE|

### imports_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dll|string|False|DLL|
|entries|[][]string|False|Entries|

### resources_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|codepage|integer|False|Codepage|
|language|string|False|Language|
|locale|string|False|Locale|
|magic|string|False|Magic|
|mime|string|False|Mime|
|name|string|False|Name|
|offset|integer|False|Offset|
|path|string|False|Path|
|resource_sha256|string|False|Resource SHA256|
|size|integer|False|Size|
|sublanguage|string|False|Sublanguage|
|type|string|False|Type|

### sections_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address|integer|False|Address|
|characteristics|[]string|False|Characteristics|
|data_pointer|integer|False|Data pointer|
|entropy|float|False|Entropy|
|entropy_type|[]string|False|Entropy type|
|section|string|False|Section|
|section_hash|string|False|Section hash|
|size|integer|False|Size|
|virtual_size|integer|False|Virtual size|

### forensics_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|exports|[][]string|False|Exports|
|file_info|file_info_artifact|False|File info|
|headers|headers_artifact|False|Headers|
|imports|[]imports_artifact|False|Imports|
|internal_checksum_match|boolean|False|Internal checksum match|
|resources|[]resources_artifact|False|Resources|
|sections|[]sections_artifact|False|Sections|
|signatures|[]string|False|Signatures|

### relation_artifact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|contains|[]string|False|Contains|
|extracted_from|[]string|False|Extracted from|
|network|[]string|False|Network|
|process|[]string|False|Process|

### artifact_analysis_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|antivirus|antivirus_artifact|False|Antivirus|
|created-time|number|False|Created-time|
|created_by|[]integer|False|Created by|
|entropy|float|False|Entropy|
|executed_from|[]integer|False|Executed from|
|forensics|forensics_artifact|False|Forensics|
|magic-type|string|False|Magic-type|
|md5|string|False|Md5|
|mime-type|string|False|Mime-type|
|modified_by|[]integer|False|Modified by|
|origin|string|False|Origin|
|path|string|False|Path|
|read_by|[]integer|False|Read by|
|relation|relation_artifact|False|Relation|
|sha1|string|False|Sha1|
|sha256|string|False|SHA256|
|size|integer|False|Size|
|type|string|False|Type|
|whitelist|[]object|False|Whitelist|

### ioc_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Antivirus_Product|string|False|Antivirus product|
|Antivirus_Result|string|False|Antivirus result|
|Artifact_ID|integer|False|Artifact ID|
|Path|string|False|Path|

### ioc_analysis_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|category|[]string|False|Category|
|confidence|integer|False|Confidence|
|data|[]ioc_data|False|Data|
|description|string|False|Description|
|heuristic_coefficient|float|False|Heuristic coefficient|
|hits|integer|False|Hits|
|ioc|string|False|Ioc|
|mitre-tactics|[]string|False|Mitre-tactics|
|severity|integer|False|Severity|
|tags|[]string|False|Tags|
|title|string|False|Title|
|truncated|boolean|False|Truncated|

### annotation_network

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asn|integer|False|ASN|
|country|string|False|Country|
|country_name|string|False|Country name|
|ip|string|False|IP|
|org|string|False|Organization|
|reverse_dns|[]string|False|Reverse DNS list|
|ts|integer|False|TS|

### annotation_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|network|[]annotation_network|False|Network|

### artifact_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|items|[]artifact_analysis_item|False|Items|

### iocs_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|items|[]ioc_analysis_item|False|Items|

### network_headers

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cache-control|string|False|Cache-control|
|content-length|string|False|Content-length|
|host|string|False|Host|
|user-agent|string|False|User-agent|

### network_decoded

|Name|Type|Required|Description|
|----|----|--------|-----------|
|actual_content_type|string|False|Actual content type|
|body_len|integer|False|Body len|
|decoded_url|string|False|Decoded URL|
|fuids|[]string|False|Filesystem access user ID|
|headers|network_headers|False|Headers|
|host|string|False|Host|
|method|string|False|Method|
|port|integer|False|Port|
|request_filename|string|False|Request filename|
|request_path|string|False|Request path|
|sha256|string|False|SHA256|
|ts|float|False|Ts|
|type|string|False|Type|
|url|string|False|URL|
|version|string|False|Version|

### network_relation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|process|[]integer|False|Process|

### network_decoded_list

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decoded|[]network_decoded|False|List of decoded results|

### network_streams_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bytes|integer|False|Bytes|
|bytes_missed|integer|False|Bytes missed|
|bytes_orig|integer|False|Bytes orig|
|bytes_orig_payload|integer|False|Bytes orig payload|
|bytes_payload|integer|False|Bytes payload|
|bytes_resp|integer|False|Bytes resp|
|bytes_resp_payload|integer|False|Bytes resp payload|
|conn_state|string|False|Conn state|
|decoded|[]network_decoded_list|False|Decoded|
|dst|string|False|Dst|
|dst_port|integer|False|Dst port|
|duration|float|False|Duration|
|history|string|False|History|
|packets|integer|False|Packets|
|packets_orig|integer|False|Packets orig|
|packets_resp|integer|False|Packets resp|
|protocol|string|False|Protocol|
|relation|network_relation|False|Relation|
|service|string|False|Service|
|session|integer|False|Session|
|src|string|False|Src|
|src_port|integer|False|Src port|
|transport|string|False|Transport|
|ts_begin|float|False|Ts begin|
|ts_end|float|False|Ts end|
|uid|string|False|Uid|

### processes_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|items|[]process_analysis_item|False|Items|

### annotations_analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|items|annotation_network|False|Items|

### general_details_metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report_created|integer|False|Report created|
|sandbox_id|string|False|Sandbox id|
|sandbox_version|string|False|Sandbox version|

### malware_desc_metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filename|string|False|Filename|
|magic|string|False|Magic|
|md5|string|False|Md5|
|sha1|string|False|Sha1|
|sha256|string|False|SHA256|
|size|integer|False|Size|
|type|string|False|Type|

### sandcastle_env_metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analysis_end|integer|False|Analysis end|
|analysis_start|integer|False|Analysis start|
|controlsubject|string|False|Controlsubject|
|current_os|string|False|Current OS|
|display_name|string|False|Display name|
|run_time|integer|False|Run time|
|sample_executed|integer|False|Sample executed|
|sandcastle|string|False|Sandcastle|
|vm|string|False|Vm|
|vm_id|string|False|Vm id|

### data_metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|general_details|general_details_metadata|False|General details|
|malware_desc|[]malware_desc_metadata|False|Malware desc|
|sandcastle_env|sandcastle_env_metadata|False|Sandcastle env|

### artifact_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|api_version|integer|False|API version|
|data|artifact_analysis|False|Data|
|id|integer|False|ID|

### iocs_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|api_version|integer|False|API version|
|data|iocs_analysis|False|Data|
|id|integer|False|ID|

### network_streams_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|api_version|integer|False|API version|
|data|network_streams_analysis|False|Data|
|id|integer|False|ID|

### processes_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|api_version|integer|False|API version|
|data|processes_analysis|False|Data|
|id|integer|False|ID|

### annotations_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|api_version|integer|False|API version|
|data|annotations_analysis|False|Data|
|id|integer|False|ID|

### metadata_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|api_version|integer|False|API version|
|data|data_metadata|False|Data|
|id|integer|False|ID|
