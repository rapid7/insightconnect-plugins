# Description

[Cuckoo Sandbox](https://cuckoosandbox.org/) is an open source automated malware analysis system. It enables
tracing of API calls, file behavior, and analysis of memory and network traffic. Using the Cuckoo Sandbox plugin for
Rapid7 InsightConnect, users can analyze files and URLs, manage tasks, and more.

Use Cuckoo Sandbox in your automation workflows to manage tasks and analyze PCAPs or suspicious files obtained through
investigations. Automatically report findings to your favorite ticketing system when this plugin is used in combination
with any of our available ticketing plugins.

For brevity and readability, the term "base64-encoded file" is used in examples
throughout this documentation in place of real base64-encoded data.

# Key Features

* File analysis
* Manage tasks

# Requirements

* Cuckoo Sandbox API URL for your Cuckoo instance

# Supported Product Versions

* 2019-06-19

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|http://localhost:8090/api|True|Cuckoo Sandbox API URL|None|http://localhost:8090/api|

Example input:

```
{
  "url": "http://localhost:8090/api"
}
```

## Technical Details

### Actions

#### View Task

This action is used to return details on the task associated with the specified ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|task_id|integer|None|True|Task ID|None|12345678910|

Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|task|task|True|Cuckoo task|{'task_id': 1}|

Example output:

```

{
  "found": true,
  "task": {
      "category": "url",
      "machine": null,
      "errors": [],
      "target": "http://www.malicious.site",
      "package": null,
      "sample_id": null,
      "guest": {},
      "custom": null,
      "owner": "",
      "priority": 1,
      "platform": null,
      "options": null,
      "status": "pending",
      "enforce_timeout": false,
      "timeout": 0,
      "memory": false,
      "tags": [
                  "32bit",
                  "acrobat_6",
              ],
      "id": 1,
      "added_on": "2012-12-19 14:18:25",
      "completed_on": null
  }
}

```

#### List Tasks

This action is used to return list of tasks.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|limit|integer|None|False|Maximum number of returned tasks|None|10|
|offset|integer|None|False|Data offset|None|5|

Example input:

```
{
  "limit": 10,
  "offset": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|tasks|[]task|True|Cuckoo tasks|[{"completed": 1, "pending": 1, "reported": 1, "running": 1, "total": 1}]|

Example output:

```

{
  "tasks": [
      {
          "category": "url",
          "machine": null,
          "errors": [],
          "target": "http://www.malicious.site",
          "package": null,
          "sample_id": null,
          "guest": {},
          "custom": null,
          "owner": "",
          "priority": 1,
          "platform": null,
          "options": null,
          "status": "pending",
          "enforce_timeout": false,
          "timeout": 0,
          "memory": false,
          "tags": []
          "id": 1,
          "added_on": "2012-12-19 14:18:25",
          "completed_on": null
      },
      {
          "category": "file",
          "machine": null,
          "errors": [],
          "target": "/tmp/malware.exe",
          "package": null,
          "sample_id": 1,
          "guest": {},
          "custom": null,
          "owner": "",
          "priority": 1,
          "platform": null,
          "options": null,
          "status": "pending",
          "enforce_timeout": false,
          "timeout": 0,
          "memory": false,
          "tags": [
                      "32bit",
                      "acrobat_6",
                  ],
          "id": 2,
          "added_on": "2012-12-19 14:18:25",
          "completed_on": null
      }
  ]
}

```

#### Delete Task

This action is used to remove the given task from the database and delete the results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|task_id|integer|None|True|Task ID|None|12345678910|

Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|------|
|error|boolean|True|Error true or false|True|
|error_value|string|True|Error message|Error|
|message|string|True|Message associated with status code|Bad Request|

Example output:

```

{
  "status_code": 200,
  "message": "OK"
}

```

#### Reschedule Task

This action is used to reschedule a task with the specified ID and priority (default priority is 1).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|priority|integer|None|False|Priority|None|1|
|task_id|integer|None|True|Task ID|None|12345678910|

Example input:

```
{
  "priority": 1,
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|task_id|integer|True|Task ID|12345678910|

Example output:

```

{
  "status": "OK",
  "task_id": 12345678910
}

```

#### View Machine

This action is used to return details on the analysis machine associated with the given name.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|machine_name|string|None|True|Machine name|None|example_machine|

Example input:

```
{
  "machine_name": "example_machine"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|machine|machine|True|Machine details|Example Machine|

Example output:

```

{
  "machine": {
      "status": null,
      "locked": false,
      "name": "cuckoo1",
      "resultserver_ip": "192.168.56.1",
      "ip": "192.168.56.101",
      "tags": [
                  "32bit",
                  "acrobat_6",
              ],
      "label": "cuckoo1",
      "locked_changed_on": null,
      "platform": "windows",
      "snapshot": null,
      "interface": null,
      "status_changed_on": null,
      "id": 1,
      "resultserver_port": 2042
  }
}

```

#### Cuckoo Status

This action is used to return the status of the cuckoo server.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cpuload|[]float|True|CPU load for the past 1, 5 and 15 minutes respectively|[0.123]|
|diskspace|diskspace|True|Free, total and used diskspace of $CUCKOO/storage/analyses/, $CUCKOO/storage/binaries/, and specified tmppath|100|
|hostname|string|True|Cuckoo hostname|Example Hostname|
|machines|machines|True|Details about available and total analysis machines|{'available': 10, 'total': 10}|
|tasks|tasks|True|Details about analysis tasks|[{"completed": 1, "pending": 1, "reported": 1, "running": 1, "total": 1}]|
|version|string|True|Cuckoo version|2.0.7|

The contents of this output vary greatly based on Cuckoo's internal settings.

Example output:

```

{
  "tasks": {
      "reported": 165,
      "running": 2,
      "total": 167,
      "completed": 0,
      "pending": 0
  },
  "diskspace": {
      "analyses": {
          "total": 491271233536,
          "free": 71403470848,
          "used": 419867762688
      },
      "binaries": {
          "total": 491271233536,
          "free": 71403470848,
          "used": 419867762688
      },
      "temporary": {
          "total": 491271233536,
          "free": 71403470848,
          "used": 419867762688
      }
  },
  "version": "1.0",
  "protocol_version": 1,
  "hostname": "Patient0",
  "machines": {
      "available": 4,
      "total": 5
  }
}

```

#### Get Screenshots

This action is used to return one (JPEG) or all (ZIP) screenshots associated with the specified task ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|screenshot_id|string|None|False|Screenshot ID|None|12345678910|
|task_id|integer|None|True|Task ID|None|12345678910|

Example input:

```
{
  "screenshot_id": 12345678910,
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|screenshots|bytes|True|Base64 encoded screenshot|VGhpcyBpcyBhbiBleGFtcGxl|

Example output:

```

{
  "found": true,
  "screenshots": [base64-encoded files]
}

```

#### Get Report

This action is used to return the report associated with the specified task ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|format|string|None|False|One of [json/html/all/dropped/package_files]. Details on formats here: http://docs.cuckoosandbox.org/en/latest/usage/api/#tasks-report|None|json|
|task_id|integer|None|True|Task ID|None|12345678910|

Example input:

```
{
  "format": "json",
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|bytes|True|Base64 encoded report|VGhpcyBpcyBhbiBleGFtcGxl|

Example output:

```

  {
    "message": "OK",
    "report": VGhpcyBpcyBhbiBleGFtcGxl
  }

```

#### Get Memory

This action is used to return one memory dump file associated with the specified task ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|pid|string|None|True|Process ID|None|12345678910|
|task_id|integer|None|True|Task ID|None|12345678910|

Example input:

```
{
  "pid": 12345678910,
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|contents|bytes|True|Base64 encoded contents|VGhpcyBpcyBhbiBleGFtcGxl|

Example output:

```

{
  "found": true,
  "contents": [base64-encoded files]
}

```

#### VPN Status

This action is used to return VPN status.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|vpns|[]vpn|True|VPN status array|[{"name": "Example", "status": "Running"}]|

This action is currently not supported by Cuckoo for MAC OS and will return a 500.

#### List Machines

This action is used to return a list with details on the analysis machines available to Cuckoo.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|machines|[]machine|True|List of machines available to Cuckoo|["Example Machine"]|

Example output:

```

{
  "machines": [
      {
          "status": null,
          "locked": false,
          "name": "cuckoo1",
          "resultserver_ip": "192.168.56.1",
          "ip": "192.168.56.101",
          "tags": [
                      "32bit",
                      "acrobat_6",
                  ],
          "label": "cuckoo1",
          "locked_changed_on": null,
          "platform": "windows",
          "snapshot": null,
          "interface": null,
          "status_changed_on": null,
          "id": 1,
          "resultserver_port": 2042
      }
  ]
}

```

#### Get PCAP

This action is used to return the content of the PCAP associated with the given task.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|task_id|integer|None|True|Task ID|None|12345678910|

Example input:

```
{
  task_id: 1234568910
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|contents|bytes|True|PCAP contents|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|

Example output:

```

{
  "found": true,
  "contents": [base64-encoded files]
}

```

#### Submit Files

This action is used to add one or more files and/or files embedded in archives to the list of pending tasks.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|files|[]file|None|True|List of files of the format: {'filename': 'blah.exe', 'contents': '<b64-encoded-bytes>'}|None|[{"filename": "example.exe", "contents": "VGhpcyBpcyBhbiBleGFtcGxl"}]|

Example input:

```
{
  "files": [{"filename": "example.exe", "contents": "VGhpcyBpcyBhbiBleGFtcGxl"}]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|errors|[]string|False|Errors if any||
|submit_id|integer|False|Submission ID||
|task_id|integer|True|Task ID|1234678910|', '|submit_id|integer|False|Submission ID|12345678910|', '|errors|[]string|False|Errors if any|["ExampleError"]|

Example output:

```

{
  "success": true,
  "task_id": 1,
  "submit_id": 1
}

```

#### View File

This action is used to return details on the file matching either the specified MD5 hash, SHA256 hash or ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|integer|None|False|ID|None|12345678910|
|md5|string|None|False|MD5 Hash|None|9de5069c5afe602b2ea0a04b66beb2c0|
|sha256|string|None|False|SHA256 Hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|

Example input:

```
{
  "id": 12345678910,
  "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
  "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|data|data|True|Data|3395856ce81f2b7382dee72602f798b642f14140|
|error|boolean|True|Error information|True|

Example output:

```

{
  "found": true,
  "sample": {
      "sha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
      "file_type": "empty",
      "file_size": 0,
      "crc32": "00000000",
      "ssdeep": "3::",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "sha512": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
      "id": 1,
      "md5": "d41d8cd98f00b204e9800998ecf8427e"
  }
}

```

#### Submit URL

This action is used to add a file (from URL) to the list of pending tasks.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|URL to analyze (multipart encoded content)|None|www.example.com|

Example input:

```
{
  "url": "www.example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|task_id|integer|True|Task ID|12345678910|

Example output:

```

{
  "task_id" : 1
}

```

#### List Memory

This action is used to return a list of memory dump files or one memory dump file associated with the specified task ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|task_id|integer|None|True|Task ID|None|12345678910|

Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|dump_files|[]string|True|Dumped Files|["Example file"]|

Example output:

```

{
  "found": true,
  "dump_files": ["Win32Test.exe"]
}

```

#### Exit

This action is used to shut down the server if in debug mode and using the werkzeug server.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|message|string|True|Exit message|Exit Message|

Example output:

```

{
  "status_code": 200,
  "message": "OK"
}

```

#### Reboot Task

This action is used to add a reboot task to the database from an existing analysis ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|task_id|integer|None|True|Task ID|None|12345678910|
Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|reboot_id|integer|True|Reboot ID|1234678910|
|task_id|integer|True|Task ID|12345678910|

Example output:

```

{
  "success": true,
  "task_id": 1,
  "reboot_id": 3
}

```

#### Get File

This action is used to return the binary content of the file matching the specified SHA256 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|sha256|string|None|True|SHA256 Hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|

Example input:

```
{
  "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|contents|bytes|True|Binary contents|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|

Example output:

```

{
  "found": true,
  "contents": [base64-encoded files]
}

```

#### Re-run Reporting

This action is used to re-run reporting for a task associated with the specified task ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|task_id|integer|None|True|Task ID|None|12345678910|

Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|------|
|success|boolean|True|Action success or failure|True|

Example output:

```
{
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

* 2.0.0 - Updated Requests version to 2.20.0
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Bug fix for Submit Files where Submit ID was required
* 1.0.0 - Support web server mode | Bug fix for testing outputs | Semver compliance
* 0.2.3 - Bug fix for Cuckoo API version 2.0.5
* 0.2.2 - URL endpoints not ending in `/`, rename server to URL in connection, and bug fix for file submission
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Rewrite
* 0.1.0 - Initial plugin

# Links

* [cuckoo](https://cuckoosandbox.org/)

## References

* [Cuckoo Sandbox](https://cuckoosandbox.org/)
* [Cuckoo API](http://docs.cuckoosandbox.org/en/latest/)

