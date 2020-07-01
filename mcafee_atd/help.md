# Description

[McAfee Advanced Threat Defense](https://www.mcafee.com/enterprise/en-us/products/advanced-threat-defense.html) provides an API framework for external applications to access core McAfeeATD functions through the REST protocol.

# Key Features

* Check if a hash is blacklisted
* Check the analysis status
* Submit a URL for analysis
* Submit a file for analysis
* Display the analyzer profiles to which the user has access
* Download the analysis report files

# Requirements

* Username and password
* Base URL for McAfee ATD

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|
|port|integer|443|False|The port number for provided host|None|443|
|url|string|None|True|Base URL for the McAfee Advanced Threat Defense server|None|https://www.example.com|
|verify_ssl|boolean|True|False|Verify the server's TLS/SSL certificate|None|True|

Example input:

```
{
  "credentials": {
    "username":"user1",
    "password":"mypassword"
  },
  "port": 443,
  "url": "https://www.example.com",
  "verify_ssl": true
}
```

## Technical Details

### Actions

#### Get Report

This action is used to download the analysis report files for given parameter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The Task ID, job ID, or MD5 value for the prepared analysis report|None|13|
|report_type|string|HTML|False|The file type of the report to return in the file output|['HTML', 'TXT', 'ZIP', 'XML', 'IOC', 'STIX', 'PDF', 'SAMPLE']|HTML|
|type_id|string|MD5|False|Type of given ID parameter, the type must match the value of the ID field. The default value is MD5|['MD5', 'TASK ID', 'JOB ID']|TASK ID|

Example input:

```
{
  "id": 13,
  "report_type": "HTML",
  "type_id": "TASK ID"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|Prepared analysis report|
|report|object|False|Return report in JSON|

Example output:

```
{
  "file": "PGh0bWw+CjxoZWFkPgo8bWV0YSBodHRwLWVxdWl2PSJDb250ZW50LVR5cGUiIGNvbnRlbnQ9InRleHQvaHRtbDsgY2hhcnNldD11dGYtOCI+Cjx0aXRsZT5NYWx3YXJlIFN1bW1hcnk8L3RpdGxlPgo8bGluayBocmVmPSIvaW1hZ2VzL3N0YW5kYXJkLmNzcyIgcmVsPSJzdHlsZXNoZWV0Ij4KPCEtLSA8bGluayBocmVmPSIvaW1hZ2VzL3N0YW5kYXJkMjAxNS5jc3MiIHJlbD0ic3R5bGVzaGVldCI+IC0tPgo8bGluayBocmVmPSIvaW1hZ2VzL2Jvb3RzdHJhcC5taW4uY3NzIiByZWw9InN0eWxlc2hlZXQiPgo8c3R5bGUgdHlwZT0idGV4dC9jc3MiPgpkaXYuY2Zvb3RlciB7bWFyZ2luLXRvcDo0MHB4OyBwYWRkaW5nLXRvcDoyMHB4OyBib3JkZXItdG9wOjdweCBkb3VibGUgI2NhYjJkMjsgbWFyZ2luLXJpZ2h0OjE1JX0KPC9zdHlsZT4KPC9oZWFkPgo8Ym9keT4KPCEtLQo8ZGl2IGNsYXNzPSJtYWludGl0bGUiPlRocmVhdCBBbmFseXNpcyBSZXBvcnQ8L2Rpdj4KPGltZyBzcmM9Ii9pbWFnZXMvaW50X1NlY3VyaXR5LnBuZyIgc3R5bGU9ImZsb2F0OnJpZ2h0OyBtYXJnaW4tcmlnaHQ6MjAwcHg7ICI+CjxkaXYgc3R5bGU9ImNsZWFyOmJvdGg7Ij48L2Rpdj4KLS0+CjxkaXYgY2xhc3M9Im1haW50aXRsZSI+CjxpbWcgc3JjPSIvaW1hZ2VzL21jbG9nby1idy5qcGciIGhlaWdodD0iMjUiIHdpZHRoPSIxMjUiIGFsaWduPSJ0b3AiPiAmZW5zcDsgJmVuc3A7fCZlbnNwOyA8Zm9udCBzaXplPSI1IiBjb2xvcj0iIzQxNDQ0OCIgPiAgVGhyZWF0IEFuYWx5c2lzIFJlcG9ydDwvZm9udD48L2Rpdj4KPHAgYWxpZ249InJpZ2h0Ij48Zm9udCBzaXplPSIrMSI+TWNBZmVlIEFkdmFuY2VkIFRocmVhdCBEZWZlbnNlPC9mb250PjwvcD4KPGJyPjxicj4KPGgyPlN1bW1hcnk8L2gyPgo8cD5TYW1wbGUgTmFtZTogdGVzdC50eHQ8L3A+CjxwPk1ENSBIYXNoIElkZW50aWZpZXI6IDBCNDdGNjcxQkM2MzI4NjIzREZBMTA4NTFENDE4RTU1PC9wPgoKPHAgY2xhc3M9Im1hbGkiPlNldmVyaXR5OiAtMjwvcD4KPHAgY2xhc3M9Im1hbGkiPkRlc2NyaXB0aW9uOiBSZXBvcnQgbm90IGF2YWlsYWJsZSAtIEFuYWx5c2lzIGluY29tcGxldGU8L3A+Cgo8ZGl2IHN0eWxlPSJib3JkZXItdG9wOjFweCBzb2xpZCByZ2IoMjIzLDIyMywyMjMpOyBwYWRkaW5nLXRvcDoyNXB4OyBtYXJnaW4tdG9wOjUwcHg7ICI+Q29weXJpZ2h0IMKpIDIwMTkgTWNBZmVlLCBMTEMuIEFsbCByaWdodHMgcmVzZXJ2ZWQuPGJyPiA8YSBocmVmPSJodHRwOi8vd3d3Lm1jYWZlZS5jb20iPnd3dy5tY2FmZWUuY29tPC9hPgo8L2Rpdj4KPC9ib2R5Pgo8L2h0bWw+Cgo=",
  "report": {
    "Summary": {
      "Subject": {
        "Name": "test.txt",
        "md5": "0B47F671BC6328623DFA10851D418E55"
      },
      "Verdict": {
        "Description": "Invalid file type, or invalid file size, or local heuristics determine the file to have a low probability of being malicious, or contain malicious intent.",
        "Severity": "-2"
      }
    }
  }
}
```

#### List Analyzer Profiles

This action is used to display the analyzer profiles to which the user has access.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|profiler_results|[]profiler_results|True|Displays the analyzer profiles, which the user can access|
|success|boolean|True|Returns true if found information about analyzer profiles|

Example output:

```
{
  "profiler_results": [
    {
      "artimas": 0,
      "asm": 0,
      "aviraAV": 0,
      "consoleLog": 0,
      "createTime": "2020-06-25 17:33:30",
      "customrules": 0,
      "defaultVM": 0,
      "dnnEnable": 0,
      "dropZip": 0,
      "dumpZip": 0,
      "family": 0,
      "flp": 0,
      "gam": 1,
      "gml": 0,
      "gtiTS": 1,
      "gtiURLRep": 0,
      "heuristic": 0,
      "imageid": 0,
      "internet": 0,
      "lastChange": "2020-06-25 17:33:30",
      "locBlackList": 0,
      "locWhiteList": 1,
      "logZip": 0,
      "maxExecTime": 0,
      "memorydump": 0,
      "mfeAV": 1,
      "minExecTime": 0,
      "name": "Test",
      "netLog": 0,
      "netdriveZip": 0,
      "noPDF": 0,
      "ntvLog": 0,
      "openarchive": 1,
      "overrideOS": 0,
      "pe32": 0,
      "reAnalysis": 1,
      "recusiveAnalysis": 0,
      "sandbox": 0,
      "sophosAV": 0,
      "ssAPIid": 0,
      "ssKeyid": 0,
      "ssLevelid": 0,
      "summary": 1,
      "userLog": 0,
      "userid": 1,
      "vmProfileid": 11,
      "xMode": 0,
      "yaraScan": 0,
      "yararules": 0
    }
  ],
  "success": true
}
```

#### Submit File

This action is used to upload a file for dynamic analysis. It accepts an option to also submit the URL from which the file is downloaded. In this case, a McAfee GTI URL look up is done on the submitted URL in addition to file analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|file|None|True|File for analysis|None|{"filename": "setup.exe", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}|
|url_for_file|string|None|False|You can also submit the URL from which the file is downloaded. In this case, a McAfee GTI URL look up is done on the submitted URL in addition to file analysis|None|https://www.example.com/download/latest|

Example input:

```
{
  "file": {
    "filename": "setup.exe",
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
  },
  "url_for_file": "https://www.example.com/download/latest"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submit_file_info|submit_info|False|Information about submitted file|

Example output:

```
{
  "submit_file_info": {
    "estimatedTime": 0,
    "fileId": "",
    "filesWait": 0,
    "mimeType": "text/plain",
    "results": [
      {
        "cache": 3,
        "destIp": "",
        "file": "amas_filename",
        "md5": "EA4B93CD8A68F72ACB1FB63B0AB7543B",
        "messageId": "",
        "sha1": "FC1E325DFBB631B82B53648A570750E329380417",
        "sha256": "0F84347E49EB9A2E8259A7EAABF190575BCCEDFA60B1AF11373D00BE442E2783",
        "size": "48",
        "srcIp": "",
        "submitType": "0",
        "taskId": 58,
        "url": ""
      }
    ],
    "subId": 58,
    "success": true
  }
}
```

#### Submit URL

This action is used to submit a URL for dynamic analysis. The `submit_type` options allows you to choose between a URL to analyze (e.g. https://www.example.com) and a URL that points to a file to analyze (e.g. https://www.example.com/PDF/14274les19.pdf).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|submit_type|string|URL submission|False|URL to submit for analysis (https://www.example.com) or file to analyze from a URL (e.g. https://www.example.com/PDF/14274les19.pdf)|['URL submission', 'File from URL']|None|
|url|string|None|True|URL for analysis|None|https://www.example.com|

Example input:

```
{
  "url": "https://www.example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submit_url_info|submit_info|False|Information about submitted URL|

Example output:

```
{
  "submit_url_info": {
    "estimatedTime": 0,
    "fileId": "",
    "filesWait": 0,
    "mimeType": "application/url",
    "results": [
      {
        "cache": 0,
        "destIp": "",
        "file": "https://example.com",
        "md5": "03C63305A49C1342D4FA9988B635973E",
        "messageId": "",
        "sha1": "",
        "sha256": "",
        "size": "18",
        "srcIp": "",
        "submitType": "1",
        "taskId": 29,
        "url": "https://example.com"
      }
    ],
    "subId": 29,
    "success": true
  }
}
```

#### Check Analysis Status

This action checks the analysis status.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analysis_id|integer|None|True|Task ID or job ID value which is returned in submission step|None|13|
|type|string|task|False|Type of ID, default value is task|['task', 'job']|None|

Example input:

```
{
  "analysis_id": 13
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job_results|job|False|Return information about given Job ID|
|results|output|False|Return information about given Task ID|
|success|boolean|False|Success status of analysis ID|

Example output:

```
{
  "results": {
    "PEInfo": "0",
    "asmListing": "0",
    "family": "0",
    "filename": "test.txt",
    "istate": 1,
    "jobid": 13,
    "md5": "0B47F671BC6328623DFA10851D418E55",
    "status": "Completed",
    "submitTime": "2020-06-20 19: 11: 44",
    "summaryFiles": "0",
    "taskid": 13,
    "useLogs": "0",
    "userid": 1,
    "vmDesc": "Only Down Selectors",
    "vmName": "Analyzer Profile 1",
    "vmProfile": "1"
  },
  "success": true
}
```

#### Check Hash Status

This action is used to check if a user submitted hash value is either blacklisted or whitelisted.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|MD5 Hash to submit|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|True|Return information about given MD5 Hash|
|success|boolean|True|Success status of submit Hash request|

Example output:

```
{
  "results": {
    "9de5069c5afe602b2ea0a04b66beb2c0": "Previously submitted"
  },
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.5.0 - New action Get Report
* 1.4.0 - New action List Analyzer Profiles
* 1.3.0 - New action Submit File
* 1.2.0 - New action Submit URL
* 1.1.0 - New action Check Analysis Status
* 1.0.0 - Initial plugin

# Links

## References

* [McAfee Advanced Threat Defense](https://www.mcafee.com/enterprise/en-us/products/advanced-threat-defense.html)
