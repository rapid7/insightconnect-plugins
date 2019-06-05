
# Cuckoo Sandbox

## About

[Cuckoo](https://cuckoosandbox.org/) is a malware analysis system, enabling tracing of API calls,
file behavior, and analysis of memory and network traffic. This plugin utilizes
the [Cuckoo API](http://docs.cuckoosandbox.org/en/latest/usage/api/) and enables you to interact
with your running Cuckoo instance.

For brevity and readability, the term "base64-encoded file" is used in examples
throughout this documentation in place of real base64-encoded data.

## Actions

### View Task

This action is used to return details on the task associated with the specified ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|task_id|integer|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|None|
|task|task|True|None|

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

### List Tasks

This action is used to return list of tasks.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|limit|integer|None|False|Maximum number of returned tasks|None|
|offset|integer|None|False|Data offset|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tasks|[]task|True|None|

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

### Delete Task

This action is used to remove the given task from the database and delete the results.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|task_id|integer|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|True|Status Code, i.e., 200 - no error, 404 - task not found, 500 - unable to delete task|
|message|string|True|Message associated with status code|

Example output:

```

{
  "status_code": 200,
  "message": "OK"
}

```

### Reschedule Task

This action is used to reschedule a task with the specified ID and priority (default priority is 1).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|priority|integer|None|False|None|None|
|task_id|integer|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|None|
|task_id|integer|True|None|

Example output:

```

{
  "status": "OK",
  "task_id": 1
}

```

### View Machine

This action is used to return details on the analysis machine associated with the given name.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|machine_name|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machine|machine|True|Machine details|

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

### Cuckoo Status

This action is used to return the status of the cuckoo server.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tasks|tasks|True|Details about analysis tasks|
|diskspace|diskspace|True|Free, total and used diskspace of $CUCKOO/storage/analyses/, $CUCKOO/storage/binaries/, and specified tmppath|
|hostname|string|True|None|
|cpuload|[]float|True|CPU load for the past 1, 5 and 15 minutes respectively|
|version|string|True|None|
|mem_total|integer|True|None|
|memory|boolean|True|None|
|mem_avail|integer|True|None|
|machines|machines|True|Details about available and total analysis machines|

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

### Get Screenshots

This action is used to return one (JPEG) or all (ZIP) screenshots associated with the specified task ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|screenshot_id|string|None|False|None|None|
|task_id|integer|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|None|
|screenshots|bytes|True|None|

Example output:

```

{
  "found": true,
  "screenshots": [base64-encoded files]
}

```

### Get Report

This action is used to return the report associated with the specified task ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|task_id|integer|None|True|None|None|
|format|string|None|False|One of [json/html/all/dropped/package_files]. Details on formats here\: http\://docs.cuckoosandbox.org/en/latest/usage/api/#tasks-report|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|bytes|True|None|
|message|string|True|None|

Example output:

```

  {
    "message": "OK",
    "report": base64-encoded file
  }

```

### Get Memory

This action is used to return one memory dump file associated with the specified task ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pid|string|None|True|None|None|
|task_id|integer|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|None|
|contents|bytes|True|None|

Example output:

```

{
  "found": true,
  "contents": [base64-encoded files]
}

```

### VPN Status

This action is used to return VPN status.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|Message returned in event of error|
|vpns|[]vpn|True|None|

This action is currently not supported by Cuckoo for Mac OS and will return a 500.

### List Machines

This action is used to return a list with details on the analysis machines available to Cuckoo.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|machines|[]machine|True|List of machines available to Cuckoo|

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

### Get PCAP

This action is used to return the content of the PCAP associated with the given task.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|task_id|integer|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|None|
|contents|bytes|True|PCAP contents|

Example output:

```

{
  "found": true,
  "contents": [base64-encoded files]
}

```

### Submit Files

This action is used to add one or more files and/or files embedded in archives to the list of pending tasks.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|files|[]file|None|True|List of files of the format\: {'filename'\: 'blah.exe', 'contents'\: 'YmFzZTY0Cg=='}|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submit_id|integer|True|None|
|message|string|True|Reason for failed submission|
|errors|[]string|True|None|
|success|boolean|True|None|
|task_id|integer|True|None|

Example output:

```

{
  "success": true,
  "task_id": 1,
  "submit_id": 1
}

```

### View File

This action is used to return details on the file matching either the specified MD5 hash, SHA256 hash or ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sha256|string|None|False|None|None|
|id|integer|None|False|None|None|
|md5|string|None|False|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sample|sample|True|None|
|found|boolean|True|None|

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

### Submit URL

This action is used to add a file (from URL) to the list of pending tasks.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to analyze (multipart encoded content)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|task_id|integer|True|None|

Example output:

```

{
  "task_id" : 1
}

```

### List Memory

This action is used to return a list of memory dump files or one memory dump file associated with the specified task ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|task_id|integer|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|None|
|dump_files|[]string|True|None|

Example output:

```

{
  "found": true,
  "dump_files": ["Win32Test.exe"]
}

```

### Exit

This action is used to shut down the server if in debug mode and using the werkzeug server.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|True|Status Code, i.e., 200 - success, 403 - call can be made only in debug mode, 500 - error|
|message|string|True|Message associated with status code|

Example output:

```

{
  "status_code": 200,
  "message": "OK"
}

```

### Reboot Task

This action is used to add a reboot task to the database from an existing analysis ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|task_id|integer|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reboot_id|integer|True|None|
|success|boolean|True|None|
|task_id|integer|True|None|

Example output:

```

{
  "success": true,
  "task_id": 1,
  "reboot_id": 3
}

```

### Rerun Report

This action is used to re-run reporting for a task associated with the specified task ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|task_id|integer|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|None|

Example output:

```

{
  "success": true
}

```

### Get File

This action is used to return the binary content of the file matching the specified SHA256 hash.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sha256|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|None|
|contents|bytes|True|Binary contents|

Example output:

```

{
  "found": true,
  "contents": [base64-encoded files]
}

```

### Re-run Reporting

This action is used to re-run reporting for a task associated with the specified task ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|task_id|integer|None|True|Task ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Action success or failure|

Example output:

```
```

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:
|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|http\://localhost\:8090/api|True|Cuckoo Sandbox API URL|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Submit malware for analysis

## Versions

* 0.1.0 - Initial plugin
* 0.2.0 - Rewrite
* 0.2.1 - SSL bug fix in SDK
* 0.2.2 - URL endpoints not ending in `/`, rename server to URL in connection, and bug fix for file submission
* 0.2.3 - Bug fix for Cuckoo API version 2.0.5
* 1.0.0 - Support web server mode | Bug fix for testing outputs | Semver compliance
* 1.0.1 - Bug fix for Submit Files where Submit ID was required

## References

* [Cuckoo Sandbox](https://cuckoosandbox.org/)
* [Cuckoo API](http://docs.cuckoosandbox.org/en/latest/)
