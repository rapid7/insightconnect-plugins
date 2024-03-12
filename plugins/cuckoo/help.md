# Description

Cuckoo Sandbox is an open source automated malware analysis system. Using the Cuckoo Sandbox plugin for Rapid7 InsightConnect, users can analyze files and URLs, manage tasks, and more

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
* 2024-03-12

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|url|string|http://localhost:8090/api|True|Cuckoo Sandbox API URL|None|http://localhost:8090/api|
  
Example input:

```
{
  "url": "http://localhost:8090/api"
}
```

## Technical Details

### Actions


#### Cuckoo Status
  
This action is used to returns status of the cuckoo server

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|cpuload|[]float|True|CPU load for the past 1, 5 and 15 minutes respectively|[0.123]|
|diskspace|diskspace|True|Free, total and used diskspace of $CUCKOO/storage/analyses/, $CUCKOO/storage/binaries/, and specified tmppath|100|
|hostname|string|True|Cuckoo hostname|Example Hostname|
|machines|machines|True|Details about available and total analysis machines|{'available': 10, 'total': 10}|
|tasks|tasks|True|Details about analysis tasks|[{"completed": 1, "pending": 1, "reported": 1, "running": 1, "total": 1}]|
|version|string|True|Cuckoo version|2.0.7|
  
Example output:

```
{
  "cpuload": [
    0.123
  ],
  "diskspace": 100,
  "hostname": "Example Hostname",
  "machines": {
    "available": 10,
    "total": 10
  },
  "tasks": [
    {
      "completed": 1,
      "pending": 1,
      "reported": 1,
      "running": 1,
      "total": 1
    }
  ],
  "version": "2.0.7"
}
```

#### Delete Task
  
This action is used to removes the given task from the database and deletes the results

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task_id|integer|None|True|Task ID|None|12345678910|
  
Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|error|boolean|True|Error true or false|True|
|error_value|string|True|Error message|Error|
|message|string|True|Message associated with status code|Bad Request|
  
Example output:

```
{
  "error": true,
  "error_value": "Error",
  "message": "Bad Request"
}
```

#### Exit
  
This action is used to shuts down the server if in debug mode and using the werkzeug server

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|Exit message|Exit Message|
  
Example output:

```
{
  "message": "Exit Message"
}
```

#### Get File
  
This action is used to returns the binary content of the file matching the specified SHA256 hash

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|sha256|string|None|True|SHA256 Hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
  
Example input:

```
{
  "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|contents|bytes|True|Binary contents|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "contents": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Get Memory
  
This action is used to returns one memory dump file associated with the specified task ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
| :--- | :--- | :--- | :--- | :--- |
|contents|bytes|True|Base64 encoded contents|VGhpcyBpcyBhbiBleGFtcGxl|
  
Example output:

```
{
  "contents": "VGhpcyBpcyBhbiBleGFtcGxl"
}
```

#### Get PCAP
  
This action is used to returns the content of the PCAP associated with the given task

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task_id|integer|None|True|Task ID|None|12345678910|
  
Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|contents|bytes|True|PCAP contents|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "contents": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Get Report
  
This action is used to returns the report associated with the specified task ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|report|bytes|True|Base64 encoded report|VGhpcyBpcyBhbiBleGFtcGxl|
  
Example output:

```
{
  "report": "VGhpcyBpcyBhbiBleGFtcGxl"
}
```

#### Get Screenshots
  
This action is used to returns one (jpeg) or all (zip) screenshots associated with the specified task ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
| :--- | :--- | :--- | :--- | :--- |
|screenshots|bytes|True|Base64 encoded screenshot|VGhpcyBpcyBhbiBleGFtcGxl|
  
Example output:

```
{
  "screenshots": "VGhpcyBpcyBhbiBleGFtcGxl"
}
```

#### List Machines
  
This action is used to returns a list with details on the analysis machines available to Cuckoo

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machines|[]machine|True|List of machines available to Cuckoo|["Example Machine"]|
  
Example output:

```
{
  "machines": [
    "Example Machine"
  ]
}
```

#### List Memory
  
This action is used to returns a list of memory dump files or one memory dump file associated with the specified task ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task_id|integer|None|True|Task ID|None|12345678910|
  
Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|dump_files|[]string|True|Dumped Files|["Example file"]|
  
Example output:

```
{
  "dump_files": [
    "Example file"
  ]
}
```

#### List Tasks
  
This action is used to returns list of tasks

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
| :--- | :--- | :--- | :--- | :--- |
|tasks|[]task|True|Cuckoo tasks|[{"completed": 1, "pending": 1, "reported": 1, "running": 1, "total": 1}]|
  
Example output:

```
{
  "tasks": [
    {
      "completed": 1,
      "pending": 1,
      "reported": 1,
      "running": 1,
      "total": 1
    }
  ]
}
```

#### Reboot Task
  
This action is used to add a reboot task to database from an existing analysis ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task_id|integer|None|True|Task ID|None|12345678910|
  
Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reboot_id|integer|True|Reboot ID|1234678910|
|task_id|integer|True|Task ID|12345678910|
  
Example output:

```
{
  "reboot_id": 1234678910,
  "task_id": 12345678910
}
```

#### Re-run Reporting
  
This action is used to re-run reporting for task associated with the specified task ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task_id|integer|None|True|Task ID|None|12345678910|
  
Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Action success or failure|True|
  
Example output:

```
{
  "success": true
}
```

#### Reschedule Task
  
This action is used to reschedule a task with the specified ID and priority (default priority is 1)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|task_id|integer|True|Task ID|12345678910|
  
Example output:

```
{
  "task_id": 12345678910
}
```

#### Submit Files
  
This action is used to adds one or more files and/or files embedded in archives to the list of pending tasks

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|files|[]file|None|True|List of files of the format: {'filename': 'blah.exe', 'contents': '<b64-encoded-bytes>'}|None|[{"filename": "example.exe", "contents": "VGhpcyBpcyBhbiBleGFtcGxl"}]|
  
Example input:

```
{
  "files": [
    {
      "contents": "VGhpcyBpcyBhbiBleGFtcGxl",
      "filename": "example.exe"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|errors|[]string|False|Errors if any|["ExampleError"]|
|submit_id|integer|False|Submission ID|12345678910|
|task_id|integer|True|Task ID|1234678910|
  
Example output:

```
{
  "errors": [
    "ExampleError"
  ],
  "submit_id": 12345678910,
  "task_id": 1234678910
}
```

#### Submit URL
  
This action is used to adds a file (from URL) to the list of pending tasks

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|url|string|None|True|URL to analyze (multipart encoded content)|None|www.example.com|
  
Example input:

```
{
  "url": "www.example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|task_id|integer|True|Task ID|12345678910|
  
Example output:

```
{
  "task_id": 12345678910
}
```

#### View File
  
This action is used to returns details on the file matching either the specified MD5 hash, SHA256 hash or ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
| :--- | :--- | :--- | :--- | :--- |
|data|data|True|Data|3395856ce81f2b7382dee72602f798b642f14140|
|error|boolean|True|Error information|True|
  
Example output:

```
{
  "data": "3395856ce81f2b7382dee72602f798b642f14140",
  "error": true
}
```

#### View Machine
  
This action is used to returns details on the analysis machine associated with the given name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine_name|string|None|True|Machine name|None|example_machine|
  
Example input:

```
{
  "machine_name": "example_machine"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine|machine|True|Machine details|Example Machine|
  
Example output:

```
{
  "machine": "Example Machine"
}
```

#### View Task
  
This action is used to returns details on the task associated with the specified ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task_id|integer|None|True|Task ID|None|12345678910|
  
Example input:

```
{
  "task_id": 12345678910
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|task|task|True|Cuckoo task|{'task_id': 1}|
  
Example output:

```
{
  "task": {
    "task_id": 1
  }
}
```

#### VPN Status
  
This action is used to returns VPN status

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vpns|[]vpn|True|VPN status array|[{"name": "Example", "status": "Running"}]|
  
Example output:

```
{
  "vpns": [
    {
      "name": "Example",
      "status": "Running"
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**vpn**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|None|None|None|
|status|string|None|None|None|None|
  
**guest**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|None|None|
|label|string|None|None|None|None|
|manager|string|None|None|None|None|
|name|string|None|None|None|None|
|Shutdown On|date|None|None|None|None|
|Started On|date|None|None|None|None|
|Task ID|integer|None|None|None|None|
  
**file**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|contents|bytes|None|None|None|None|
|filename|string|None|None|None|None|
  
**data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CRC-32|string|None|None|None|None|
|File Size|integer|None|None|None|None|
|File Type|string|None|None|None|None|
|ID|integer|None|None|None|None|
|MD5|string|None|None|None|None|
|SHA1|string|None|None|None|None|
|SHA256|string|None|None|None|None|
|SHA512|string|None|None|None|None|
|SSDeep Fuzzy Hash|string|None|None|None|None|
  
**sample**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CRC-32|string|None|None|None|None|
|error|boolean|None|None|None|None|
|File Size|integer|None|None|None|None|
|File Type|string|None|None|None|None|
|ID|integer|None|None|None|None|
|MD5|string|None|None|None|None|
|SHA1|string|None|None|None|None|
|SHA256|string|None|None|None|None|
|SHA512|string|None|None|None|None|
|SSDeep Fuzzy Hash|string|None|None|None|None|
  
**option**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|option|string|None|None|None|None|
|value|string|None|None|None|None|
  
**task**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Added On|date|None|None|None|None|
|category|string|None|None|None|None|
|clock|date|None|None|None|None|
|Completed On|date|None|None|None|None|
|custom|string|None|None|None|None|
|Enforce Timeout?|boolean|None|None|None|None|
|errors|[]string|None|None|None|None|
|guest|guest|None|None|None|None|
|ID|integer|None|None|None|None|
|machine|string|None|None|None|None|
|options|[]option|None|None|None|None|
|owner|string|None|None|None|None|
|package|string|None|None|None|None|
|platform|string|None|None|None|None|
|priority|integer|None|None|None|None|
|processing|string|None|None|None|None|
|route|string|None|None|None|None|
|sample|sample|None|None|None|None|
|sample_id|integer|None|None|None|None|
|Started On|date|None|None|None|None|
|status|string|None|None|None|None|
|submit_id|integer|None|None|None|None|
|tags|[]string|None|None|None|None|
|target|string|None|None|None|None|
|timeout|integer|None|None|Timeout in seconds|None|
  
**machine**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|None|None|None|
|interface|string|None|None|None|None|
|IP|string|None|None|None|None|
|label|string|None|None|None|None|
|Locked?|boolean|None|None|None|None|
|Date on which locked status was changed|date|None|None|None|None|
|name|string|None|None|None|None|
|platform|string|None|None|None|None|
|Resultserver IP|string|None|None|None|None|
|Resultserver Port|integer|None|None|None|None|
|snapshot|string|None|None|None|None|
|status|string|None|None|None|None|
|status_changed_on|date|None|None|Date on which status was changed|None|
|tags|[]string|None|None|None|None|
  
**tasks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|completed|integer|None|None|None|None|
|pending|integer|None|None|None|None|
|reported|integer|None|None|None|None|
|running|integer|None|None|None|None|
|total|integer|None|None|None|None|
  
**machines**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|available|integer|None|None|None|None|
|total|integer|None|None|None|None|
  
**temporary**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|free|integer|None|None|Free diskspace|None|
|total|integer|None|None|Total diskspace|None|
|used|integer|None|None|Used diskspace|None|
  
**binaries**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|free|integer|None|None|Free diskspace|None|
|total|integer|None|None|Total diskspace|None|
|used|integer|None|None|Used diskspace|None|
  
**analyses**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|free|integer|None|None|Free diskspace|None|
|total|integer|None|None|Total diskspace|None|
|used|integer|None|None|Used diskspace|None|
  
**diskspace**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|analyses|analyses|None|None|None|None|
|binaries|binaries|None|None|None|None|
|temporary|temporary|None|None|None|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History
  
*This plugin does not contain a version history.*

# Links


## References
  
*This plugin does not contain any references.*