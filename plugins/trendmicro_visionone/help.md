# Description

Trend Vision One is an enhanced threat defense platform, surpassing standard XDR solutions. It offers comprehensive detection and response across various security layers and automates data correlation for rapid response, effectively preventing most attacks

# Key Features

* Add Alert Note
* Add Custom Script
* Add to Block List
* Add to Exception List
* Add to Suspicious List
* Collect File
* Create API Keys
* Delete Custom Script
* Delete Email Message
* Delete API Keys
* Disable Account
* Download Custom Script
* Download Sandbox Analysis Result
* Download Sandbox Investigation Package
* Edit Alert Status
* Enable Account
* Get Alert Details
* Get Alert List
* Get API Key
* Get Custom Script List
* Get Email Activity Data
* Get Email Activity Data Count
* Get Endpoint Activity Data
* Get Endpoint Activity Data Count
* Get Endpoint Data
* Get Exception List
* Get OAT List
* Get Sandbox Analysis Result
* Get Sandbox Submission Status
* Get Sandbox Suspicious List
* Get Suspicious List
* Get Task Result
* Isolate Endpoint
* List API Keys
* Poll Alert List
* Poll OAT List
* Poll Sandbox Suspicious List
* Quarantine Email Message
* Remove from Block List
* Remove from Exception List
* Remove from Suspicious List
* Reset Password Account
* Restore Email Message
* Restore Endpoint
* Run Custom Script
* Sign out Account
* Submit File to Sandbox
* Submit URLs to Sandbox
* Terminate Process
* Update API Key
* Update Custom Script

# Requirements

* Requires a Trend Vision One API Key
* API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

* Trend Vision One API v3

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|default|True|Vision One API Token|None|12345678-ABCD-1234-ABCD-123456789012:ABCDEFGH-1234-ABCD-1234-ABCDEFGHIJKL:12345678901234567890123456789012345678901234|None|None|
|api_url|string|https://api.xdr.trendmicro.com|True|URL of Trend Vision One|None|https://tmv1-mock.trendmicro.com|None|None|
|verify_ssl|boolean|True|True|Verify if connection uses SSL|None|True|None|None|

Example input:

```
{
  "api_key": "default",
  "api_url": "https://api.xdr.trendmicro.com",
  "verify_ssl": true
}
```

## Technical Details

### Actions


#### Add Alert Note
  
This action is used to attaches a note to a workbench alert

**API key role permissions required:**

**Workbench**

- Modify alert details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|Unique alphanumeric string that identifies a Workbench alert|None|WB-14-20190709-00003|None|None|
|content|string|None|True|Unique alphanumeric string that identifies a Workbench alert|None|Suspected False Positive, please verify|None|None|
  
Example input:

```
{
  "alert_id": "WB-14-20190709-00003",
  "content": "Suspected False Positive, please verify"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|note_id|string|True|ID of the note created|345|
|result_code|string|True|Result message of adding workbench note|202|
  
Example output:

```
{
  "note_id": 345,
  "result_code": 202
}
```

#### Add Custom Script

This action is used to uploads a custom script. Supported file extensions are .ps1, .sh; Custom scripts must use UTF-8 
encoding

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- View, filter and search (Custom Scripts tab)
- Manage custom scripts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Task Description|None|example desc|None|None|
|file|file|None|False|Custom Script (dict of {filename(string) & content(base64(bytes))})|None|{"content":"dGVzdA==","filename":"r7-test11.sh"}|None|None|
|file_type|string|bash|True|File type of custom script|["powershell", "bash"]|bash|None|None|
  
Example input:

```
{
  "description": "example desc",
  "file": {
    "content": "dGVzdA==",
    "filename": "r7-test11.sh"
  },
  "file_type": "bash"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|script_id|string|True|ID of added script file|44c99cb0-8c5f-4182-af55-62135dbe32f1|
  
Example output:

```
{
  "script_id": "44c99cb0-8c5f-4182-af55-62135dbe32f1"
}
```

#### Add to Block List

This action is used to adds an email address, file SHA-1, domain, IP address, or URL to the Suspicious Object List, 
which blocks the objects on subsequent detections

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Add to block list

**Suspicious Object Management**

- View, filter, and search
- Manage lists and configure settings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|block_objects|[]block_objects|None|True|Objects made up of type, value and description|None|[{"object_type":"ip","object_value":"6.6.6.6","description":"block"}]|None|None|
  
Example input:

```
{
  "block_objects": [
    {
      "description": "block",
      "object_type": "ip",
      "object_value": "6.6.6.6"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Add To Block List Response Array|[{"status":202,"task_id":"00002134"},{"status":202,"task_id":"00002135"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002134"
    },
    {
      "status": 202,
      "task_id": "00002135"
    }
  ]
}
```

#### Add to Exception List

This action is used to adds domains, file SHA-1 values, IP addresses, or URLs to the Exception List and prevents these 
objects from being added to the Suspicious Object List

**API key role permissions required:**

**Suspicious Object Management**

- View, filter, and search
- Manage lists and configure settings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|block_objects|[]block_objects|None|True|Objects made up of type, value and description|None|[{"object_type":"ip","object_value":"1.2.6.9"}]|None|None|
  
Example input:

```
{
  "block_objects": [
    {
      "object_type": "ip",
      "object_value": "1.2.6.9"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Add To Exception List Response Array|[{"status":201,"task_id":"None"},{"status":201,"task_id":"None"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 201,
      "task_id": "None"
    },
    {
      "status": 201,
      "task_id": "None"
    }
  ]
}
```

#### Add to Suspicious List

This action is used to adds domains, file SHA-1/SHA-256 values, IP addresses, senderMailAddress, or URLs to the Block 
Object List

**API key role permissions required:**

**Suspicious Object Management**

- View, filter, and search
- Manage lists and configure settings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|suspicious_block_objects|[]suspicious_block_objects|None|True|Suspicious Objects made up of type, value and scan_action, risk_level and days_to_expiration|None|[{"risk_level":"high","expiry_days":"30","object_type":"ip","scan_action":"block","object_value":"6.6.6.3"}]|None|None|
  
Example input:

```
{
  "suspicious_block_objects": [
    {
      "expiry_days": "30",
      "object_type": "ip",
      "object_value": "6.6.6.3",
      "risk_level": "high",
      "scan_action": "block"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Add To Suspicious List Response Array|[{"status":201,"task_id":"None"},{"status":201,"task_id":"None"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 201,
      "task_id": "None"
    },
    {
      "status": 201,
      "task_id": "None"
    }
  ]
}
```

#### Collect File
  
This action is used to collects a file from one or more endpoints and then sends the files to Trend Micro Vision One in 
a password-protected archive Note- You can specify either the computer name- endpointName or the GUID of the installed 
agent program- agentGuid

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Collect file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|collect_files|[]collect_files|None|True|Collect file input JSON containing endpoint, file path and description|None|[{"endpoint_name":"client1","agent_guid":"cb9c8412-1f64-4fa0-a36b-76bf41a07ede","file_path":"C:/virus.exe","description":"collect malicious file"}]|None|None|
  
Example input:

```
{
  "collect_files": [
    {
      "agent_guid": "cb9c8412-1f64-4fa0-a36b-76bf41a07ede",
      "description": "collect malicious file",
      "endpoint_name": "client1",
      "file_path": "C:/virus.exe"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Add To Block List Response Array|[{"status":202,"task_id":"00002195"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002195"
    }
  ]
}
```

#### Create API Keys
  
This action is used to generates API keys that allow third-party applications to access the Trend Vision One APIs

**API key role permissions required:**

**API Keys**

- View
- Configure Settings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_keys_objects|[]api_keys_objects|None|True|List of JSON objects containing data for API keys creation|None|[{"name":"TestKey","role":"Analyst","months_to_expiration":"1","description":"Test API Key create","status":"enabled"}]|None|None|
  
Example input:

```
{
  "api_keys_objects": [
    {
      "description": "Test API Key create",
      "months_to_expiration": "1",
      "name": "TestKey",
      "role": "Analyst",
      "status": "enabled"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|api_keys_resp|[]api_keys_resp|True|List of API keys responses|[{"status":200,"id":"d367abdd-7739-4129-a36a-862c4ec018b4","value":"API-KEY","expiredDateTime":"2025-02-06T10:00:00Z"}]|
  
Example output:

```
{
  "api_keys_resp": [
    {
      "expiredDateTime": "2025-02-06T10:00:00Z",
      "id": "d367abdd-7739-4129-a36a-862c4ec018b4",
      "status": 200,
      "value": "API-KEY"
    }
  ]
}
```

#### Delete API Keys
  
This action is used to deletes the specified API keys

**API key role permissions required:**

**API Keys**

- View
- Configure Settings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|[]string|None|True|List of unique identifiers of the API keys|None|["d367abdd-7739-4129-a36a-862c4ec018b4","b667abdd-7739-4129-a36a-862c4ec019se"]|None|None|
  
Example input:

```
{
  "id": [
    "d367abdd-7739-4129-a36a-862c4ec018b4",
    "b667abdd-7739-4129-a36a-862c4ec019se"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|True|The Status Code of the API key update|207|
  
Example output:

```
{
  "status": 207
}
```

#### Delete Custom Script
  
This action is used to deletes custom script

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- View, filter and search (Custom Scripts tab)
- Manage custom scripts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|script_id|string|None|True|Unique alphanumeric string that identifies a script file|None|44c99cb0-8c5f-4182-af55-62135dbe32f1|None|None|
  
Example input:

```
{
  "script_id": "44c99cb0-8c5f-4182-af55-62135dbe32f1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result_code|string|True|Result Code of the delete request|SUCCESS|
  
Example output:

```
{
  "result_code": "SUCCESS"
}
```

#### Delete Email Message
  
This action is used to deletes a message from a mailbox

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Delete messages

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email_identifiers|[]email_identifiers|None|True|Email Identifiers consisting of message id, mailbox and description|None|[{"description":"delete email message r7","mailbox":"user@example.com","message_id":"AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AAhCCNvg5sEua0nNjgfLS2AABNpgLcwAA"}]|None|None|
  
Example input:

```
{
  "email_identifiers": [
    {
      "description": "delete email message r7",
      "mailbox": "user@example.com",
      "message_id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AAhCCNvg5sEua0nNjgfLS2AABNpgLcwAA"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Delete Email Message Response Array|[{"status":202,"task_id":"00002127"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002127"
    }
  ]
}
```

#### Disable Account

This action is used to signs the user out of all active application and browser sessions, and prevents the user from 
signing in any new session. Supported IAM systems - Azure AD and Active Directory (on-premises)

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Enable/Disable user account, force sign out, force password reset
 
##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_identifiers|[]account_identifiers|None|True|User Account Identifiers containing account name and description|None|[{"account_name":"user@example.com","description":"disable account r7"}]|None|None|
  
Example input:

```
{
  "account_identifiers": [
    {
      "account_name": "user@example.com",
      "description": "disable account r7"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Disable Account Response Array|[{"status":202,"task_id":"00002129"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002129"
    }
  ]
}
```

#### Download Custom Script
  
This action is used to downloads custom script

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- View, filter and search (Custom Scripts tab)
- Download custom scripts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|script_id|string|None|True|Unique alphanumeric string that identifies a script file|None|44c99cb0-8c5f-4182-af55-62135dbe32f1|None|None|
  
Example input:

```
{
  "script_id": "44c99cb0-8c5f-4182-af55-62135dbe32f1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file|file|True|The response is a .sh or .ps1 file|{"content":"IyEvYmluL2Jhc2gKbHM=","filename":"r7-test11.sh"}|
  
Example output:

```
{
  "file": {
    "content": "IyEvYmluL2Jhc2gKbHM=",
    "filename": "r7-test11.sh"
  }
}
```

#### Download Sandbox Analysis Result

This action is used to downloads the analysis result for an object submitted to sandbox for analysis based on the 
submission ID

**API key role permissions required:**

**Sandbox Analysis**

- View, filter, and search
- Submit objects

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Unique alphanumeric string that identifies the analysis results of a submission|None|6345645|None|None|
|poll|boolean|True|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|None|None|
|poll_time_sec|float|30|False|Maximum time to wait for the result to be available|None|15.5|None|None|
  
Example input:

```
{
  "id": 6345645,
  "poll": true,
  "poll_time_sec": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file|file|True|The response is a .pdf file|{"content":"dGVzdA==","filename":"r7-test11.pdf"}|
  
Example output:

```
{
  "file": {
    "content": "dGVzdA==",
    "filename": "r7-test11.pdf"
  }
}
```

#### Download Sandbox Investigation Package
  
This action is used to downloads the investigation package based on submission ID

**API key role permissions required:**

**Sandbox Analysis**

- View, filter, and search
- Submit objects

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Unique alphanumeric string that identifies the analysis results of a submission|None|6345645|None|None|
|poll|boolean|True|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|None|None|
|poll_time_sec|float|30|False|Maximum time to wait for the result to be available|None|15.5|None|None|
  
Example input:

```
{
  "id": 6345645,
  "poll": true,
  "poll_time_sec": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file|file|True|The output is a .zip file|{"content":"dGVzdA==","filename":"r7-test11.zip"}|
  
Example output:

```
{
  "file": {
    "content": "dGVzdA==",
    "filename": "r7-test11.zip"
  }
}
```

#### Edit Alert Status
  
This action is used to updates the status of a workbench alert

**API key role permissions required:**

**Workbench**

- Modify alert details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Workbench alert ID|None|WB-14-20190709-00003|None|None|
|if_match|string|None|False|The target resource will be updated only if it matches ETag of the target one|None|d41d8cd98f00b204e9800998ecf8427e|None|None|
|status|string|None|True|ID of the workbench you would like to update the status for|["New", "In Progress", "True Positive", "False Positive"]|New|None|None|
  
Example input:

```
{
  "id": "WB-14-20190709-00003",
  "if_match": "d41d8cd98f00b204e9800998ecf8427e",
  "status": "New"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result_code|string|True|Result code of response|202|
  
Example output:

```
{
  "result_code": 202
}
```

#### Enable Account
  
This action is used to allows the user to sign in to new application and browser sessions. Supported IAM systems - Azure
 AD and Active Directory (on-premises)

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Enable/Disable user account, force sign out, force password reset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_identifiers|[]account_identifiers|None|True|User Account Identifiers containing account name and description|None|[{"account_name":"user@example.com","description":"enable jdoe account, r7 test"}]|None|None|
  
Example input:

```
{
  "account_identifiers": [
    {
      "account_name": "user@example.com",
      "description": "enable jdoe account, r7 test"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Enable Account Response Array|[{"status":202,"task_id":"00002148"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002148"
    }
  ]
}
```

#### Get Alert Details
  
This action is used to displays information about workbench alerts that match the specified criteria in a paginated list

**API key role permissions required:**

**Workbench**

- View, filter, and search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|ID of the Alert to get the details of|None|WB-20837-20221111-0000|None|None|
  
Example input:

```
{
  "alert_id": "WB-20837-20221111-0000"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert_details|alert|True|The details of the alert|{"alert":"<<referenced:bigdata>>"}|
|etag|string|True|An identifier for a specific version of a Workbench alert resource|33a64df551425fcc55e4d42a148795d9f25f89d4|
  
Example output:

```
{
  "alert_details": {
    "alert": "<<referenced:bigdata>>"
  },
  "etag": "33a64df551425fcc55e4d42a148795d9f25f89d4"
}
```

#### Get Alert List
  
This action is used to displays information about workbench alerts that match the specified criteria in a paginated list

**API key role permissions required:**

**Workbench**

- View, filter, and search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_date_time|string|None|True|Datetime in ISO 8601 format (yyyy-MM-ddThh:mm:ssZ in UTC) that indicates the end of the data retrieval time range. Ensure that "endDateTime" is not earlier than "startDateTime"|None|2020-06-15 12:00:00+00:00|None|None|
|start_date_time|string|None|True|Datetime in ISO 8601 format (yyyy-MM-ddThh:mm:ssZ in UTC) that indicates the start of the data retrieval time range. The available oldest value is "1970-01-01T00:00:00Z"|None|2020-06-15 10:00:00+00:00|None|None|
  
Example input:

```
{
  "end_date_time": "2020-06-15 12:00:00+00:00",
  "start_date_time": "2020-06-15 10:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]alert|True|Array of any alerts (awb-workbenchAlertV3)|["<<referenced:bigdata>>"]|
|total_count|integer|True|Number of Workbench alerts retrieved|5|
  
Example output:

```
{
  "alerts": [
    "<<referenced:bigdata>>"
  ],
  "total_count": 5
}
```

#### Get API Key
  
This action is used to displays information of the specified API key

**API key role permissions required:**

**API Keys**

- View

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The unique identifier of the API key|None|2ee04177-53d7-4fc7-a9d7-39285d80f58a|None|None|
  
Example input:

```
{
  "id": "2ee04177-53d7-4fc7-a9d7-39285d80f58a"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|description|string|False|A brief note about the API key|this is a test apikey|
|etag|string|False|Unique alphanumeric string that identifies the version of a resource|d41d8cd98f00b204e9800998ecf8427e|
|expired_date_time|string|True|Timestamp in ISO 8601 format indicating the expiration date of the API key|2025-02-06 10:00:00+00:00|
|id|string|True|The unique identifier of the API key|d367abdd-7739-4129-a36a-862c4ec018b4|
|last_used_date_time|string|True|Timestamp in ISO 8601 format indicating the last time the API key was used|2023-02-06 10:00:00+00:00|
|name|string|True|The unique name of the API key|test|
|role|string|True|The user role assigned to the API key|Master Administrator|
|status|string|True|The status of an API key|enabled|
  
Example output:

```
{
  "description": "this is a test apikey",
  "etag": "d41d8cd98f00b204e9800998ecf8427e",
  "expired_date_time": "2025-02-06 10:00:00+00:00",
  "id": "d367abdd-7739-4129-a36a-862c4ec018b4",
  "last_used_date_time": "2023-02-06 10:00:00+00:00",
  "name": "test",
  "role": "Master Administrator",
  "status": "enabled"
}
```

#### Get Custom Script List

This action is used to retrieves information about the available custom scripts and displays the information in a 
paginated list

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- View, filter and search (Custom Scripts tab)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|object|None|True|JSON object of fields to query by fileName or fileType|None|{"fileName":"test.ps1","fileType":"powershell"}|None|None|
|query_op|string|or|True|Logical operator to employ in the query. (AND/OR)|["or", "and"]|or|None|None|
  
Example input:

```
{
  "fields": {
    "fileName": "test.ps1",
    "fileType": "powershell"
  },
  "query_op": "or"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|custom_scripts_list_resp|[]custom_scripts_list_resp|True|Custom Scripts List Response Array|[{"description":"Terminates processes in user devices","file_name":"trendmicro-security-playbook-terminate-proc.ps1","file_type":"powershell","id":"71c7ae1f-bf14-4e6f-b3eb-30a45d13e6f2"}]|
  
Example output:

```
{
  "custom_scripts_list_resp": [
    {
      "description": "Terminates processes in user devices",
      "file_name": "trendmicro-security-playbook-terminate-proc.ps1",
      "file_type": "powershell",
      "id": "71c7ae1f-bf14-4e6f-b3eb-30a45d13e6f2"
    }
  ]
}
```

#### Get Email Activity Data
  
This action is used to displays search results from the Email Activity Data source in a paginated list

**API key role permissions required:**

**Search**

- View, filter, and search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_date_time|string|None|False|Timestamp in ISO 8601 format that indicates the end of the data retrieval time range. If no value is specified, 'endDateTime' defaults to the time the request is made|None|2020-06-15 12:00:00+00:00|None|None|
|fields|object|None|True|JSON object of fields to query. (uuid, tags, pname, msgUuid, ...)|None|{"mailSenderIp":"192.169.1.1","mailMsgSubject":"spam"}|None|None|
|query_op|string|or|True|Logical operator to employ in the query. (AND/OR)|["or", "and"]|or|None|None|
|select|[]string|None|False|List of fields to include in the search results. If no fields are specified, the query returns all supported fields|None|["mailMsgSubject"]|None|None|
|start_date_time|string|None|False|Timestamp in ISO 8601 format that indicates the start of the data retrieval range. If no value is specified, 'startDateTime' defaults to 24 hours before the request is made|None|2020-06-15 10:00:00+00:00|None|None|
|top|integer|None|True|Number of records displayed on a page|[50, 100, 500, 1000, 5000]|500|None|None|
  
Example input:

```
{
  "end_date_time": "2020-06-15 12:00:00+00:00",
  "fields": {
    "mailMsgSubject": "spam",
    "mailSenderIp": "192.169.1.1"
  },
  "query_op": "or",
  "select": [
    "mailMsgSubject"
  ],
  "start_date_time": "2020-06-15 10:00:00+00:00",
  "top": 500
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|email_activity_data_resp|[]email_activity_data_resp|True|Email Activity Data Response Array|[{"mail_msg_subject":"test sample","mail_msg_id":"<user@example.com>","msg_uuid":"ihbjkhabkjHBJKHBKJHbkjHBKJhbjkhbJKHBJKHBKJhbjHBJhbj","mailbox":"user@example.com","mail_sender_ip":"xx.yy.zz.ww","mail_from_addresses":["user@example.com"],"mail_whole_header":["user@example.com>"],"mail_to_addresses":["user@example.com"],"mail_source_domain":"example.com","search_d_l":"CAS","scan_type":"exchange","event_time":1601249307000,"org_id":"8d23a000-9a4c-11ea-80f5-1de879102030","mail_urls_visible_link":["http://xxxxxx.com"],"mail_urls_real_link":["http://xxxxxx.com"]}]|
  
Example output:

```
{
  "email_activity_data_resp": [
    {
      "event_time": 1601249307000,
      "mail_from_addresses": [
        "user@example.com"
      ],
      "mail_msg_id": "<user@example.com>",
      "mail_msg_subject": "test sample",
      "mail_sender_ip": "xx.yy.zz.ww",
      "mail_source_domain": "example.com",
      "mail_to_addresses": [
        "user@example.com"
      ],
      "mail_urls_real_link": [
        "http://xxxxxx.com"
      ],
      "mail_urls_visible_link": [
        "http://xxxxxx.com"
      ],
      "mail_whole_header": [
        "user@example.com>"
      ],
      "mailbox": "user@example.com",
      "msg_uuid": "ihbjkhabkjHBJKHBKJHbkjHBKJhbjkhbJKHBJKHBKJhbjHBJhbj",
      "org_id": "8d23a000-9a4c-11ea-80f5-1de879102030",
      "scan_type": "exchange",
      "search_d_l": "CAS"
    }
  ]
}
```

#### Get Email Activity Data Count
  
This action is used to displays count of search results from the Email Activity Data source in a paginated list

**API key role permissions required:**

**Search**

- View, filter, and search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_date_time|string|None|False|Timestamp in ISO 8601 format that indicates the end of the data retrieval time range. If no value is specified, 'endDateTime' defaults to the time the request is made|None|2020-06-15 12:00:00+00:00|None|None|
|fields|object|None|True|JSON object of fields to query. (uuid, tags, pname, msgUuid, ...)|None|{"mailSenderIp":"192.169.1.1","mailMsgSubject":"spam"}|None|None|
|query_op|string|or|True|Logical operator to employ in the query. (AND/OR)|["or", "and"]|or|None|None|
|select|[]string|None|False|List of fields to include in the search results. If no fields are specified, the query returns all supported fields|None|["mailMsgSubject"]|None|None|
|start_date_time|string|None|False|Timestamp in ISO 8601 format that indicates the start of the data retrieval range. If no value is specified, 'startDateTime' defaults to 24 hours before the request is made|None|2020-06-15 10:00:00+00:00|None|None|
|top|integer|None|True|Number of records displayed on a page|[50, 100, 500, 1000, 5000]|500|None|None|
  
Example input:

```
{
  "end_date_time": "2020-06-15 12:00:00+00:00",
  "fields": {
    "mailMsgSubject": "spam",
    "mailSenderIp": "192.169.1.1"
  },
  "query_op": "or",
  "select": [
    "mailMsgSubject"
  ],
  "start_date_time": "2020-06-15 10:00:00+00:00",
  "top": 500
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|total_count|integer|True|Number of records returned by a query|5|
  
Example output:

```
{
  "total_count": 5
}
```

#### Get Endpoint Activity Data
  
This action is used to displays results from the Endpoint Activity Data source in a paginated list

**API key role permissions required:**

**Search**

- View, filter, and search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_date_time|string|None|False|Timestamp in ISO 8601 format that indicates the end of the data retrieval time range. If no value is specified, 'endDateTime' defaults to the time the request is made|None|2020-06-15 12:00:00+00:00|None|None|
|fields|object|None|True|JSON object of fields to query. (uuid, tags, pname, msgUuid, ...)|None|{"endpointHostName":"client1","dpt":443}|None|None|
|query_op|string|or|True|Logical operator to employ in the query. (AND/OR)|["or", "and"]|or|None|None|
|select|[]string|None|False|List of fields to include in the search results. If no fields are specified, the query returns all supported fields|None|["endpointHostName"]|None|None|
|start_date_time|string|None|False|Timestamp in ISO 8601 format that indicates the start of the data retrieval range. If no value is specified, 'startDateTime' defaults to 24 hours before the request is made|None|2020-06-15 10:00:00+00:00|None|None|
|top|integer|None|True|Number of records displayed on a page|[50, 100, 500, 1000, 5000]|500|None|None|
  
Example input:

```
{
  "end_date_time": "2020-06-15 12:00:00+00:00",
  "fields": {
    "dpt": 443,
    "endpointHostName": "client1"
  },
  "query_op": "or",
  "select": [
    "endpointHostName"
  ],
  "start_date_time": "2020-06-15 10:00:00+00:00",
  "top": 500
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpoint_activity_data_resp|[]endpoint_activity_data_resp|True|Endpoint Activity Data Response Array|[{"dpt":443,"dst":"","endpoint_guid":"72436165-b5a5-471a-9389-0bdc3647bc33","endpoint_host_name":"xxx-docker","endpoint_ip":["192.0.2.0"],"event_id":"1","event_sub_id":0,"object_integrity_level":0,"object_true_type":0,"object_sub_true_type":0,"win_event_id":3,"event_time":1633124154241,"event_time_d_t":"2021-10-01T21:35:54.241000+00:00","host_name":"xxx-docker","logon_user":["string"],"object_cmd":"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe --type=utility --lang=en-US --no-sandbox","object_file_hash_sha1":"98A9A1C8F69373B211E5F1E303BA8762F44BC898","object_file_path":"C:\\\\Program Files (x86)\\\\temp\\\\Application\\\\test.exe","object_host_name":"string","object_ip":"string","object_ips":["string"],"object_port":0,"object_registry_data":"wscript \\","object_registry_key_handle":"hklm\\\\software\\\\wow6432node\\\\microsoft\\\\windows\\\\currentversion\\\\run","object_registry_value":"its_ie_settings","object_signer":["Microsoft Windows"],"object_signer_valid":[true],"object_user":"SYSTEM","os":"Linux","parent_cmd":"string","parent_file_hash_sha1":"string","parent_file_path":"string","process_cmd":"C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe --type=utility --lang=en-US --no-sandbox","process_file_hash_sha1":"string","process_file_path":"C:\\\\Program Files (x86)\\\\temp\\\\Application\\\\test.exe","request":"https://www.example.com","search_d_l":"SDL","spt":8080,"src":"192.169.1.1","src_file_hash_sha1":"string","src_file_path":"string","tags":["MITRE.T1210"],"uuid":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}]|
  
Example output:

```
{
  "endpoint_activity_data_resp": [
    {
      "dpt": 443,
      "dst": "",
      "endpoint_guid": "72436165-b5a5-471a-9389-0bdc3647bc33",
      "endpoint_host_name": "xxx-docker",
      "endpoint_ip": [
        "192.0.2.0"
      ],
      "event_id": "1",
      "event_sub_id": 0,
      "event_time": 1633124154241,
      "event_time_d_t": "2021-10-01T21:35:54.241000+00:00",
      "host_name": "xxx-docker",
      "logon_user": [
        "string"
      ],
      "object_cmd": "C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe --type=utility --lang=en-US --no-sandbox",
      "object_file_hash_sha1": "98A9A1C8F69373B211E5F1E303BA8762F44BC898",
      "object_file_path": "C:\\\\Program Files (x86)\\\\temp\\\\Application\\\\test.exe",
      "object_host_name": "string",
      "object_integrity_level": 0,
      "object_ip": "string",
      "object_ips": [
        "string"
      ],
      "object_port": 0,
      "object_registry_data": "wscript \\",
      "object_registry_key_handle": "hklm\\\\software\\\\wow6432node\\\\microsoft\\\\windows\\\\currentversion\\\\run",
      "object_registry_value": "its_ie_settings",
      "object_signer": [
        "Microsoft Windows"
      ],
      "object_signer_valid": [
        true
      ],
      "object_sub_true_type": 0,
      "object_true_type": 0,
      "object_user": "SYSTEM",
      "os": "Linux",
      "parent_cmd": "string",
      "parent_file_hash_sha1": "string",
      "parent_file_path": "string",
      "process_cmd": "C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe --type=utility --lang=en-US --no-sandbox",
      "process_file_hash_sha1": "string",
      "process_file_path": "C:\\\\Program Files (x86)\\\\temp\\\\Application\\\\test.exe",
      "request": "https://www.example.com",
      "search_d_l": "SDL",
      "spt": 8080,
      "src": "192.169.1.1",
      "src_file_hash_sha1": "string",
      "src_file_path": "string",
      "tags": [
        "MITRE.T1210"
      ],
      "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "win_event_id": 3
    }
  ]
}
```

#### Get Endpoint Activity Data Count
  
This action is used to displays count of search results from the Endpoint Activity Data source in a paginated list

**API key role permissions required:**

**Search**

- View, filter, and search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_date_time|string|None|False|Timestamp in ISO 8601 format that indicates the end of the data retrieval time range. If no value is specified, 'endDateTime' defaults to the time the request is made|None|2020-06-15 12:00:00+00:00|None|None|
|fields|object|None|True|JSON object of fields to query. (uuid, tags, pname, msgUuid, ...)|None|{"endpointHostName":"client1","dpt":443}|None|None|
|query_op|string|or|True|Logical operator to employ in the query. (AND/OR)|["or", "and"]|or|None|None|
|select|[]string|None|False|List of fields to include in the search results. If no fields are specified, the query returns all supported fields|None|["endpointHostName"]|None|None|
|start_date_time|string|None|False|Timestamp in ISO 8601 format that indicates the start of the data retrieval range. If no value is specified, 'startDateTime' defaults to 24 hours before the request is made|None|2020-06-15 10:00:00+00:00|None|None|
|top|integer|None|True|Number of records displayed on a page|[50, 100, 500, 1000, 5000]|500|None|None|
  
Example input:

```
{
  "end_date_time": "2020-06-15 12:00:00+00:00",
  "fields": {
    "dpt": 443,
    "endpointHostName": "client1"
  },
  "query_op": "or",
  "select": [
    "endpointHostName"
  ],
  "start_date_time": "2020-06-15 10:00:00+00:00",
  "top": 500
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|total_count|integer|True|Number of records returned by a query|5|
  
Example output:

```
{
  "total_count": 5
}
```

#### Get Endpoint Data
  
This action is used to retrieves information about a specific endpoint

**API key role permissions required:**

**Endpoint Inventory**

- View

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|object|None|True|JSON object of endpoint identifiers to query by their hostname, macAddress, agentGuid or IP|None|{"ip":"127.127.127.127","endpointName":"client1"}|None|None|
|query_op|string|or|True|Logical operator to employ in the query. (AND/OR)|["or", "and"]|or|None|None|
  
Example input:

```
{
  "fields": {
    "endpointName": "client1",
    "ip": "127.127.127.127"
  },
  "query_op": "or"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpoint_data|[]endpoint_data|True|Array of Endpoint Data Objects, consisting of agent guid, login account, endpoint name, MAC address, IP, os name, or version, os description, product code and installed product code|[{"agent_guid":"35fa11da-a24e-40cf-8b56-baf8828cc151","login_account":{"updated_date_time":"2024-02-05T20:58:22Z","value":["MSEDGEWIN10\\\\IEUser"]},"endpoint_name":{"updated_date_time":"2024-02-05T20:58:22Z","value":"MSEDGEWIN10"},"mac_address":{"updated_date_time":"2024-02-05T20:58:22Z","value":["00:1c:42:be:22:5f"]},"ip":{"updated_date_time":"2024-02-05T20:58:22Z","value":["10.211.55.36"]},"os_name":"Linux","os_version":"10.0.17763","os_description":"Windows 10 Enterprise Evaluation (64 bit) build 17763","product_code":"sao","installed_product_codes":["xes"]}]|
  
Example output:

```
{
  "endpoint_data": [
    {
      "agent_guid": "35fa11da-a24e-40cf-8b56-baf8828cc151",
      "endpoint_name": {
        "updated_date_time": "2024-02-05T20:58:22Z",
        "value": "MSEDGEWIN10"
      },
      "installed_product_codes": [
        "xes"
      ],
      "ip": {
        "updated_date_time": "2024-02-05T20:58:22Z",
        "value": [
          "10.211.55.36"
        ]
      },
      "login_account": {
        "updated_date_time": "2024-02-05T20:58:22Z",
        "value": [
          "MSEDGEWIN10\\\\IEUser"
        ]
      },
      "mac_address": {
        "updated_date_time": "2024-02-05T20:58:22Z",
        "value": [
          "00:1c:42:be:22:5f"
        ]
      },
      "os_description": "Windows 10 Enterprise Evaluation (64 bit) build 17763",
      "os_name": "Linux",
      "os_version": "10.0.17763",
      "product_code": "sao"
    }
  ]
}
```

#### Get Exception List
  
This action is used to retrieves information about domains, file SHA-1, file SHA-256, IP addresses, sender addresses, or
 URLs in the Exception List and displays it in a paginated list

**API key role permissions required:**

**Suspicious Object Management**

- View, filter, and search

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|exception_objects|[]exception_objects|True|Array of any Exception Objects|[{"description":"ip exception","last_modified_date_time":"2023-04-14T06:53:59Z","type":"ip","value":"1.6.6.3"}]|
  
Example output:

```
{
  "exception_objects": [
    {
      "description": "ip exception",
      "last_modified_date_time": "2023-04-14T06:53:59Z",
      "type": "ip",
      "value": "1.6.6.3"
    }
  ]
}
```

#### Get OAT List

This action is used to gets information about Observed Attack Techniques (OATs) events that match the specified 
criteria in a list

**API key role permissions required:**

**Observed Attack Techniques**

- View, filter, and search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|detected_end_date_time|string|None|True|The end of the event detection data retrieval time range in ISO 8601 format|None|2021-04-06 08:22:37+00:00|None|None|
|detected_start_date_time|string|None|True|The start of the event detection data retrieval time range in ISO 8601 format|None|2021-04-05 08:22:37+00:00|None|None|
|fields|object|None|True|JSON object of OAT identifiers to query|None|{"uuid":123,"endpointName":"client1"}|None|None|
|ingested_end_date_time|string|None|True|The end of the data ingestion time range in ISO 8601 format|None|2021-04-07 08:22:37+00:00|None|None|
|ingested_start_date_time|string|None|True|The beginning of the data ingestion time range in ISO 8601 format|None|2021-04-06 08:22:37+00:00|None|None|
|query_op|string|or|True|Logical operator to employ in the query. (AND/OR)|["or", "and"]|or|None|None|
  
Example input:

```
{
  "detected_end_date_time": "2021-04-06 08:22:37+00:00",
  "detected_start_date_time": "2021-04-05 08:22:37+00:00",
  "fields": {
    "endpointName": "client1",
    "uuid": 123
  },
  "ingested_end_date_time": "2021-04-07 08:22:37+00:00",
  "ingested_start_date_time": "2021-04-06 08:22:37+00:00",
  "query_op": "or"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|oats|[]oat|True|Array of Observed Attack Techniques events|["<<referenced:bigdata>>"]|
|total_count|integer|True|Number of Observed Attack Techniques events retrieved|5|
  
Example output:

```
{
  "oats": [
    "<<referenced:bigdata>>"
  ],
  "total_count": 5
}
```

#### Get Sandbox Analysis Result

This action is used to retrieves the sandbox analysis results

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|poll|boolean|True|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|None|None|
|poll_time_sec|float|30|False|Maximum time to wait for the result to be available|None|15.5|None|None|
|report_id|string|None|True|Report_id of the sandbox submission retrieved from the trendmicro-visionone-get-file-analysis-status command|None|02384|None|None|
  
Example input:

```
{
  "poll": true,
  "poll_time_sec": 30,
  "report_id": "02384"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis_completion_date_time|string|True|Timestamp in ISO 8601 format that indicates when the analysis was completed|2022-02-14 16:30:45+00:00|
|arguments|string|False|Command line arguments encoded in Base64 of the submitted file|QWxhZGRpbjpvcGVuIHNlc2FtZQ==|
|detection_names|[]string|False|The name of the threat as detected by the sandbox|["VAN_DROPPER.UMXX"]|
|digest|object|False|The hash values of the analyzed file|{"md5":"65a8e27d8879283831b664bd8b7f0ad4","sha1":"0a0a9f2a6772942557ab5355d76af442f8f65e01","sha256":"dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"}|
|id|string|True|Unique alphanumeric string that identifies the analysis results of a submitted object|908324jf9384|
|risk_level|string|True|The risk level assigned to the object by the sandbox|low|
|threat_types|[]string|False|The threat type as detected by the sandbox|["Dropper"]|
|true_file_type|string|False|File Type of the Object|.exe|
|type|string|True|Object Type|url|
  
Example output:

```
{
  "analysis_completion_date_time": "2022-02-14 16:30:45+00:00",
  "arguments": "QWxhZGRpbjpvcGVuIHNlc2FtZQ==",
  "detection_names": [
    "VAN_DROPPER.UMXX"
  ],
  "digest": {
    "md5": "65a8e27d8879283831b664bd8b7f0ad4",
    "sha1": "0a0a9f2a6772942557ab5355d76af442f8f65e01",
    "sha256": "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"
  },
  "id": "908324jf9384",
  "risk_level": "low",
  "threat_types": [
    "Dropper"
  ],
  "true_file_type": ".exe",
  "type": "url"
}
```

#### Get Sandbox Submission Status
  
This action is used to retrieves the status of a sandbox analysis submission

**API key role permissions required:**

**Sandbox Analysis**

- View, filter, and search
- Submit objects

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|task_id|string|None|True|Task_id from the trendmicro-visionone-submit-file-to-sandbox command output|None|02384|None|None|
  
Example input:

```
{
  "task_id": "02384"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|action|string|True|Action applied to a submitted object|analyzeFile|
|arguments|string|False|Arguments for the file submitted|-y -d|
|created_date_time|string|True|Timestamp in ISO 8601 that indicates the object was submitted to the sandbox|2022-02-14 16:30:45+00:00|
|digest|object|False|The hash values for the file analyzed|{"md5":"65a8e27d8879283831b664bd8b7f0ad4","sha1":"0a0a9f2a6772942557ab5355d76af442f8f65e01","sha256":"dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"}|
|error|object|False|Error code and message for the submission|{"error":{"code":"NotFound","message":"Not Found"}}|
|id|string|True|Unique alphanumeric string that identifies a submission|0so47fy9|
|is_cached|boolean|False|Parameter that indicates if an object has been analyzed before by the Sandbox Analysis App. Submissions marked as cached do not count toward the daily reserve|False|
|last_action_date_time|string|True|Timestamp in ISO 8601 format that indicates when the information about a submission was last updated|2022-02-14 16:30:45+00:00|
|resource_location|string|False|Location of the submitted file|temp/downloaded/virus.exe|
|status|string|True|Response code for the action call|running|
  
Example output:

```
{
  "action": "analyzeFile",
  "arguments": "-y -d",
  "created_date_time": "2022-02-14 16:30:45+00:00",
  "digest": {
    "md5": "65a8e27d8879283831b664bd8b7f0ad4",
    "sha1": "0a0a9f2a6772942557ab5355d76af442f8f65e01",
    "sha256": "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"
  },
  "error": {
    "error": {
      "code": "NotFound",
      "message": "Not Found"
    }
  },
  "id": "0so47fy9",
  "is_cached": false,
  "last_action_date_time": "2022-02-14 16:30:45+00:00",
  "resource_location": "temp/downloaded/virus.exe",
  "status": "running"
}
```

#### Get Sandbox Suspicious List
  
This action is used to downloads the suspicious object list associated to the specified object. Note ~ Suspicious Object
 Lists are only available for objects with a high risk level

**API key role permissions required:**

**Sandbox Analysis**

- View, filter, and search
- Submit objects

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Unique alphanumeric string that identifies the analysis results of a submission|None|6345645|None|None|
|poll|boolean|True|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|None|None|
|poll_time_sec|float|30|False|Maximum time to wait for the result to be available|None|15.5|None|None|
  
Example input:

```
{
  "id": 6345645,
  "poll": true,
  "poll_time_sec": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|sandbox_suspicious_list_resp|[]sandbox_suspicious_list_resp|True|Sandbox Suspicious Object List Response|[{"analysis_completion_date_time":"2023-01-11T22:40:52Z","expired_date_time":"2023-02-10T22:40:52Z","risk_level":"high","root_sha1":"ccc8c28226224755091a3462ff7704e350f2114b","type":"fileSha1","value":"0d8b8f0baf22e65a80148bcebaef082ef08932d2"}]|
  
Example output:

```
{
  "sandbox_suspicious_list_resp": [
    {
      "analysis_completion_date_time": "2023-01-11T22:40:52Z",
      "expired_date_time": "2023-02-10T22:40:52Z",
      "risk_level": "high",
      "root_sha1": "ccc8c28226224755091a3462ff7704e350f2114b",
      "type": "fileSha1",
      "value": "0d8b8f0baf22e65a80148bcebaef082ef08932d2"
    }
  ]
}
```

#### Get Suspicious List
  
This action is used to retrieves information about domains, file SHA-1, file SHA-256, IP addresses, email addresses, or 
URLs in the Suspicious Object List and displays the information in a paginated list

**API key role permissions required:**

**Suspicious Object Management**

- View, filter, and search

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|suspicious_objects|[]suspicious_objects|True|Array of any Suspicious Objects|[{"description":"","expired_date_time":"2023-05-14T06:55:29Z","in_exception_list":false,"last_modified_date_time":"2023-04-14T06:55:29Z","risk_level":"high","scan_action":"log","type":"ip","value":"6.6.6.3"}]|
  
Example output:

```
{
  "suspicious_objects": [
    {
      "description": "",
      "expired_date_time": "2023-05-14T06:55:29Z",
      "in_exception_list": false,
      "last_modified_date_time": "2023-04-14T06:55:29Z",
      "risk_level": "high",
      "scan_action": "log",
      "type": "ip",
      "value": "6.6.6.3"
    }
  ]
}
```

#### Get Task Result
  
This action is used to retrieves an object containing the results of a response task in JSON format

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Download task result

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|poll|boolean|True|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|None|None|
|poll_time_sec|float|30|False|Maximum time to wait for the result to be available|None|15.5|None|None|
|task_id|string|None|True|TaskId output from the collect command used to collect the file|None|3456346|None|None|
  
Example input:

```
{
  "poll": true,
  "poll_time_sec": 30,
  "task_id": 3456346
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|account|string|False|User that triggered the response|user1|
|action|string|True|Command sent to the target|isolate|
|agent_guid|string|False|Unique alphanumeric string that identifies an installed agent|2839eu2983e23e|
|created_date_time|string|True|Timestamp in ISO 8601 format|2022-02-14 16:30:45+00:00|
|description|string|False|Task Description|example desc|
|endpoint_name|string|False|Endpoint name of the target endpoint|endpoint1|
|expired_date_time|string|False|The expiration date and time of the file|2022-02-14 16:30:45+00:00|
|file_path|string|False|File path for the file that was collected|temp/downloads/virus.exe|
|file_sha1|string|False|The fileSHA1 of the collected file|3395856ce81f2b7382dee72602f798b642f14140|
|file_sha256|string|False|The fileSHA256 of the collected file|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|file_size|integer|False|The file size of the file collected|256|
|filename|string|False|File name of a response task target (<= 255)|virus.exe|
|id|string|False|Unique numeric string that identifies a response task|j9wq384fj9|
|image_path|string|False|File path of a process image|temp/images/image.png|
|last_action_date_time|string|True|Timestamp in ISO 8601 format|2022-02-14 16:30:45+00:00|
|password|string|False|The password of the file collected|1234!|
|pid|integer|False|Unique numeric string that identifies an active process|20374284|
|resource_location|string|False|URL location of the file collected that can be used to download|www.resourcelocation.ert|
|sandbox_task_id|string|False|Unique alphanumeric string that identifies a task generated by the Sandbox Analysis App|283j928j3d2|
|status|string|True|The status of the command sent to the managing server|queued|
|tasks|[]object|False|Currently, it is only possible to apply tasks to one message in a mailbox or one message in several mailboxes|[{"status":"running","lastActionDateTime":"2021-04-06T08:22:37Z","error":{"code":"TaskError","number":4009999,"message":"An internal error has occurred."},"agentGuid":"cb9c8412-1f64-4fa0-a36b-76bf41a07ede","endpointName":"trend-host-1"}]|
|url|string|False|Universal Resource Locator|www.url.url|
  
Example output:

```
{
  "account": "user1",
  "action": "isolate",
  "agent_guid": "2839eu2983e23e",
  "created_date_time": "2022-02-14 16:30:45+00:00",
  "description": "example desc",
  "endpoint_name": "endpoint1",
  "expired_date_time": "2022-02-14 16:30:45+00:00",
  "file_path": "temp/downloads/virus.exe",
  "file_sha1": "3395856ce81f2b7382dee72602f798b642f14140",
  "file_sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "file_size": 256,
  "filename": "virus.exe",
  "id": "j9wq384fj9",
  "image_path": "temp/images/image.png",
  "last_action_date_time": "2022-02-14 16:30:45+00:00",
  "password": "1234!",
  "pid": 20374284,
  "resource_location": "www.resourcelocation.ert",
  "sandbox_task_id": "283j928j3d2",
  "status": "queued",
  "tasks": [
    {
      "agentGuid": "cb9c8412-1f64-4fa0-a36b-76bf41a07ede",
      "endpointName": "trend-host-1",
      "error": {
        "code": "TaskError",
        "message": "An internal error has occurred.",
        "number": 4009999
      },
      "lastActionDateTime": "2021-04-06T08:22:37Z",
      "status": "running"
    }
  ],
  "url": "www.url.url"
}
```

#### Isolate Endpoint
  
This action is used to disconnects an endpoint from the network (but allows communication with the managing Trend Micro 
product)

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Isolate endpoint

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint_identifiers|[]endpoint_identifiers|None|True|Endpoint Identifiers consisting of endpoint(hostname or agentGuid) and description|None|[{"description":"TEST isolate endpoint","endpoint_name":"client1","agent_guid":"cb9c8412-1f64-4fa0-a36b-76bf41a07ede"}]|None|None|
  
Example input:

```
{
  "endpoint_identifiers": [
    {
      "agent_guid": "cb9c8412-1f64-4fa0-a36b-76bf41a07ede",
      "description": "TEST isolate endpoint",
      "endpoint_name": "client1"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Isolate Endpoint Response Array|[{"status":202,"task_id":"00002126"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002126"
    }
  ]
}
```

#### List API Keys
  
This action is used to displays a list of all your API keys in a list

**API key role permissions required:**

**API Keys**

- View

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|object|None|True|JSON object of fields to query by fileName or fileType|None|{"role":"Master Administrator"}|None|None|
|query_op|string|or|True|Logical operator to employ in the query. (AND/OR)|["or", "and"]|or|None|None|
|top|integer|None|False|Number of records displayed on a page|[50, 100, 200]|50|None|None|
  
Example input:

```
{
  "fields": {
    "role": "Master Administrator"
  },
  "query_op": "or",
  "top": 50
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]api_keys_list_resp|True|List of API key object responses|[{"id":"d367abdd-7739-4129-a36a-862c4ec018b4","name":"test","status":"enabled","role":"Master Administrator","description":"this is a test","expiredDateTime":"2025-02-06T10:00:00Z","lastUsedDateTime":"2023-02-06T10:00:00Z"}]|
|total_count|integer|True|The number of retrieved API keys|5|
  
Example output:

```
{
  "items": [
    {
      "description": "this is a test",
      "expiredDateTime": "2025-02-06T10:00:00Z",
      "id": "d367abdd-7739-4129-a36a-862c4ec018b4",
      "lastUsedDateTime": "2023-02-06T10:00:00Z",
      "name": "test",
      "role": "Master Administrator",
      "status": "enabled"
    }
  ],
  "total_count": 5
}
```

#### Quarantine Email Message
  
This action is used to moves a message from a mailbox to the quarantine folder

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Quarantine/Restore messages

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email_identifiers|[]email_identifiers|None|True|Email Identifiers consisting of message id, mailbox and description|None|[{"description":"quarantine email message r7","mailbox":"user@example.com","message_id":"AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AAhCCNvg5sEua0nNjgfLS2AABNpgTSQAA"}]|None|None|
  
Example input:

```
{
  "email_identifiers": [
    {
      "description": "quarantine email message r7",
      "mailbox": "user@example.com",
      "message_id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AAhCCNvg5sEua0nNjgfLS2AABNpgTSQAA"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Quarantine Email Message Response Array|[{"status":202,"task_id":"00002153"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002153"
    }
  ]
}
```

#### Remove from Block List
  
This action is used to removes an email address, file SHA-1, domain, IP address, or URL that was added to the Suspicious
 Object List using the Add to block list action

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Add to block list

**Suspicious Object Management**

- View, filter, and search
- Manage lists and configure settings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|block_objects|[]block_objects|None|True|Objects made up of type, value and description|None|[{"description":"block","object_type":"ip","object_value":"6.6.6.3"}]|None|None|
  
Example input:

```
{
  "block_objects": [
    {
      "description": "block",
      "object_type": "ip",
      "object_value": "6.6.6.3"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Remove From Block List Response Array|[{"status":202,"task_id":"00002141"},{"status":202,"task_id":"00002142"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002141"
    },
    {
      "status": 202,
      "task_id": "00002142"
    }
  ]
}
```

#### Remove from Exception List
  
This action is used to removes domains, file SHA-1 values, IP addresses, or URLs from the Exception List

**API key role permissions required:**

**Suspicious Object Management**

- View, filter, and search
- Manage lists and configure settings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|block_objects|[]block_objects|None|True|Objects made up of type, value and description|None|[{"object_type":"ip","object_value":"1.6.6.3"}]|None|None|
  
Example input:

```
{
  "block_objects": [
    {
      "object_type": "ip",
      "object_value": "1.6.6.3"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Remove From Exception List Response Array|[{"status":204,"task_id":"None"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 204,
      "task_id": "None"
    }
  ]
}
```

#### Remove from Suspicious List
  
This action is used to removes domains, file SHA-1 values, IP addresses, or URLs from the Suspicious Object List

**API key role permissions required:**

**Suspicious Object Management**

- View, filter, and search
- Manage lists and configure settings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|block_objects|[]block_objects|None|True|Objects made up of type, value and description|None|[{"object_type":"ip","object_value":"6.6.6.4"}]|None|None|
  
Example input:

```
{
  "block_objects": [
    {
      "object_type": "ip",
      "object_value": "6.6.6.4"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Add To Exception List Response Array|[{"status":204,"task_id":"None"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 204,
      "task_id": "None"
    }
  ]
}
```

#### Reset Password Account
  
This action is used to signs the user out of all active application and browser sessions, and forces the user to create 
a new password during the next sign-in attempt. Supported IAM systems - Azure AD and Active Directory (on-premises)

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Enable/Disable user account, force sign out, force password reset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_identifiers|[]account_identifiers|None|True|User Account Identifiers containing account name and description|None|[{"account_name":"user@example.com","description":"reset password account r7 "}]|None|None|
  
Example input:

```
{
  "account_identifiers": [
    {
      "account_name": "user@example.com",
      "description": "reset password account r7 "
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Reset Password Account Response Array|[{"status":202,"task_id":"00002131"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002131"
    }
  ]
}
```

#### Restore Email Message
  
This action is used to restores a quarantined email message

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Quarantine/Restore messages

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email_identifiers|[]email_identifiers|None|True|Email Identifiers consisting of message id, mailbox and description|None|[{"description":"restore email message r7","mailbox":"user@example.com","message_id":"AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AAhCCNvg5sEua0nNjgfLS2AABNpgTSQAA"}]|None|None|
  
Example input:

```
{
  "email_identifiers": [
    {
      "description": "restore email message r7",
      "mailbox": "user@example.com",
      "message_id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AAhCCNvg5sEua0nNjgfLS2AABNpgTSQAA"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Delete Email Message Response Array|[{"status":202,"task_id":"00002154"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002154"
    }
  ]
}
```

#### Restore Endpoint
  
This action is used to restores network connectivity to an endpoint that applied the isolate endpoint action

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Isolate endpoint

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint_identifiers|[]endpoint_identifiers|None|True|Endpoint Identifiers consisting of endpoint(hostname or agentGuid) and description|None|[{"description":"restore endpoint r7","endpoint_name":"client1","agent_guid":"cb9c8412-1f64-4fa0-a36b-76bf41a07ede"}]|None|None|
  
Example input:

```
{
  "endpoint_identifiers": [
    {
      "agent_guid": "cb9c8412-1f64-4fa0-a36b-76bf41a07ede",
      "description": "restore endpoint r7",
      "endpoint_name": "client1"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Restore Endpoint Response Array|[{"status":202,"task_id":"00002132"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002132"
    }
  ]
}
```

#### Run Custom Script
  
This action is used to run custom script

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- View, filter and search (Custom Scripts tab)
- Run custom scripts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent_guid|string|None|False|Unique alphanumeric string that identifies an installed agent|None|2839eu2983e23e|None|None|
|description|string|None|False|Task Description|None|example desc|None|None|
|endpoint_name|string|None|False|Endpoint name of the target endpoint|None|endpoint1|None|None|
|file_name|string|test.ps1|False|File name of custom script|None|test.ps1|None|None|
|parameter|string|None|False|Options passed to the script during execution|None|-y --verbose|None|None|
  
Example input:

```
{
  "agent_guid": "2839eu2983e23e",
  "description": "example desc",
  "endpoint_name": "endpoint1",
  "file_name": "test.ps1",
  "parameter": "-y --verbose"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Add To Block List Response Array|[{"status":202,"task_id":"00002133"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002133"
    }
  ]
}
```

#### Sign out Account
  
This action is used to signs the user out of all active application and browser sessions. Supported IAM systems - Azure 
AD

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Enable/Disable user account, force sign out, force password reset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_identifiers|[]account_identifiers|None|True|User Account Identifiers containing account name and description|None|[{"account_name":"user@example.com","description":"sign out account r7 "}]|None|None|
  
Example input:

```
{
  "account_identifiers": [
    {
      "account_name": "user@example.com",
      "description": "sign out account r7 "
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Sign out Account Response Array|[{"status":202,"task_id":"00002130"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002130"
    }
  ]
}
```

#### Submit File to Sandbox
  
This action is used to submits a file to the sandbox for analysis (Note. For more information about the supported file 
types, see the Trend Micro Vision One Online Help. Submissions require credits. Does not require credits in regions 
where Sandbox Analysis has not been officially released.)

**API key role permissions required:**

**Sandbox Analysis**

- View, filter, and search
- Submit objects

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|archive_password|string|None|False|Password encoded in Base64 used to decrypt the submitted archive. The maximum password length (without encoding) is 128 bytes|None|1234|None|None|
|arguments|string|None|False|Parameter that allows you to specify Base64-encoded command line arguments to run the submitted file. The maximum argument length before encoding is 1024 bytes. Arguments are only available for Portable Executable (PE) files and script files|None|IFMlYztbQA==|None|None|
|document_password|string|None|False|Password encoded in Base64 used to decrypt the submitted file sample. The maximum password length (without encoding) is 128 bytes|None|1234|None|None|
|file|file|None|False|File submitted to the sandbox (dict of {filename(string) & content(base64(bytes))})|None|{"content":"dGVzdA==","filename":"r7-test11.bat"}|None|None|
  
Example input:

```
{
  "archive_password": 1234,
  "arguments": "IFMlYztbQA==",
  "document_password": 1234,
  "file": {
    "content": "dGVzdA==",
    "filename": "r7-test11.bat"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|arguments|string|False|Command line arguments encoded in Base64 of the submitted file|QWxhZGRpbjpvcGVuIHNlc2FtZQ==|
|digest|object|True|The hash value of the file|{"md5":"65a8e27d8879283831b664bd8b7f0ad4","sha1":"0a0a9f2a6772942557ab5355d76af442f8f65e01","sha256":"dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"}|
|id|string|True|Unique alphanumeric string that identifies a submission|0so47fy9|
  
Example output:

```
{
  "arguments": "QWxhZGRpbjpvcGVuIHNlc2FtZQ==",
  "digest": {
    "md5": "65a8e27d8879283831b664bd8b7f0ad4",
    "sha1": "0a0a9f2a6772942557ab5355d76af442f8f65e01",
    "sha256": "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"
  },
  "id": "0so47fy9"
}
```

#### Submit URLs to Sandbox
  
This action is used to submits URLs to the sandbox for analysis. You can submit a maximum of 10 URLs per request

**API key role permissions required:**

**Sandbox Analysis**

- View, filter, and search
- Submit objects

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|urls|[]string|None|True|URL(s) to be submitted, formated as bracket array separated by comma|None|["www.urlurl.com","www.zurlzurl.com"]|None|None|
  
Example input:

```
{
  "urls": [
    "www.urlurl.com",
    "www.zurlzurl.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submit_urls_resp|[]submit_urls_resp|True|Submit URLSs response Array|[{"digest":{"md5":"f3a2e1227de8d5ae7296665c1f34b28d","sha1":"d79bff55069994b1c11f7856f9f029de36adfd8f","sha256":"619a273ee4d25fb4aeb97e89c554fcfbdbc82e22d840cfdb364a8f1932f48160"},"id":"d28e22cb-c6af-4291-bf25-22f33ce7aa15","status":202,"task_id":"d28e22cb-c6af-4291-bf25-22f33ce7aa15","url":"https://example.com"}]|
  
Example output:

```
{
  "submit_urls_resp": [
    {
      "digest": {
        "md5": "f3a2e1227de8d5ae7296665c1f34b28d",
        "sha1": "d79bff55069994b1c11f7856f9f029de36adfd8f",
        "sha256": "619a273ee4d25fb4aeb97e89c554fcfbdbc82e22d840cfdb364a8f1932f48160"
      },
      "id": "d28e22cb-c6af-4291-bf25-22f33ce7aa15",
      "status": 202,
      "task_id": "d28e22cb-c6af-4291-bf25-22f33ce7aa15",
      "url": "https://example.com"
    }
  ]
}
```

#### Terminate Process
  
This action is used to terminates a process that is running on an endpoint

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- Terminate process

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|process_identifiers|[]process_identifiers|None|True|Process Identifiers consisting of endpoint(hostname or agentGuid), filesha1, filename(optional) and description(optional)|None|[{"endpoint_name":"client1","agent_guid":"cb9c8412-1f64-4fa0-a36b-76bf41a07ede","file_sha1":"984afc7aaa2718984e15e3b5ab095b519a081321"}]|None|None|
  
Example input:

```
{
  "process_identifiers": [
    {
      "agent_guid": "cb9c8412-1f64-4fa0-a36b-76bf41a07ede",
      "endpoint_name": "client1",
      "file_sha1": "984afc7aaa2718984e15e3b5ab095b519a081321"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|multi_response|[]multi_response|True|Terminate Process Response Array|[{"status":202,"task_id":"00002133"}]|
  
Example output:

```
{
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002133"
    }
  ]
}
```

#### Update API Key
  
This action is used to updates the specified API key

**API key role permissions required:**

**API Keys**

- View
- Configure Settings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|A brief note about the API key|None|this is a test apikey|None|None|
|id|string|None|True|The unique identifier of the API key|None|2ee04177-53d7-4fc7-a9d7-39285d80f58a|None|None|
|if_match|string|None|False|The ETag of the resource you want to update. The resource is updated only if the provided value matches the ETag of the resource|None|d41d8cd98f00b204e9800998ecf8427e|None|None|
|name|string|None|True|The unique name of the API key|None|test|None|None|
|role|string|None|True|The user role assigned to the API key|None|Master Administrator|None|None|
|status|string|None|True|The status of an API key|["enabled", "disabled"]|enabled|None|None|
  
Example input:

```
{
  "description": "this is a test apikey",
  "id": "2ee04177-53d7-4fc7-a9d7-39285d80f58a",
  "if_match": "d41d8cd98f00b204e9800998ecf8427e",
  "name": "test",
  "role": "Master Administrator",
  "status": "enabled"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|True|The Status Code of the API key update|204|
  
Example output:

```
{
  "status": 204
}
```

#### Update Custom Script

This action is used to updates a custom script. Supported file extensions are .ps1, .sh; Custom scripts must use UTF-8 
encoding

**API key role permissions required:**

**Response Management**

- View, filter, and search (Task List tab)
- View, filter and search (Custom Scripts tab)
- Manage custom scripts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Task Description|None|example desc|None|None|
|file|file|None|False|Custom Script (dict of {filename(string) & content(base64(bytes))})|None|{"content":"dGVzdA==","filename":"r7-test11.sh"}|None|None|
|file_type|string|bash|True|File type of custom script|["powershell", "bash"]|bash|None|None|
|script_id|string|None|True|Unique alphanumeric string that identifies a script file|None|44c99cb0-8c5f-4182-af55-62135dbe32f1|None|None|
  
Example input:

```
{
  "description": "example desc",
  "file": {
    "content": "dGVzdA==",
    "filename": "r7-test11.sh"
  },
  "file_type": "bash",
  "script_id": "44c99cb0-8c5f-4182-af55-62135dbe32f1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result_code|string|True|Result Code of the update request|SUCCESS|
  
Example output:

```
{
  "result_code": "SUCCESS"
}
```
### Triggers


#### Poll Alert List
  
This trigger is used to polls information about workbench alerts that match the specified criteria in a paginated list

**API key role permissions required:**

**Workbench**

- View, filter, and search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|1800|True|Interval (in seconds) in which the polling script should run again|None|1800|None|None|
|start_date_time|string|None|True|Datetime in ISO 8601 format (yyyy-MM-ddThh:mm:ssZ in UTC) that indicates the start of the data retrieval time range. The available oldest value is "1970-01-01T00:00:00Z"|None|2020-06-15 10:00:00+00:00|None|None|
  
Example input:

```
{
  "interval": 1800,
  "start_date_time": "2020-06-15 10:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]alert|True|Array of any alerts (awb-workbenchAlertV3)|["<<referenced:bigdata>>"]|
|total_count|integer|True|Number of Workbench alerts retrieved|5|
  
Example output:

```
{
  "alerts": [
    "<<referenced:bigdata>>"
  ],
  "total_count": 5
}
```

#### Poll OAT List

This trigger is used to polls information about Observed Attack Techniques (OATs) events that match the specified 
criteria in a list

**API key role permissions required:**

**Observed Attack Techniques**

- View, filter, and search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|detected_start_date_time|string|None|True|The start of the event detection data retrieval time range in ISO 8601 format|None|2021-04-05 08:22:37+00:00|None|None|
|fields|object|None|True|JSON object of OAT identifiers to query|None|{"uuid":123,"endpointName":"client1"}|None|None|
|ingested_start_date_time|string|None|True|The beginning of the data ingestion time range in ISO 8601 format|None|2021-04-06 08:22:37+00:00|None|None|
|interval|integer|1800|True|Interval (in seconds) in which the polling script should run again|None|1800|None|None|
|query_op|string|or|True|Logical operator to employ in the query. (AND/OR)|["or", "and"]|or|None|None|
  
Example input:

```
{
  "detected_start_date_time": "2021-04-05 08:22:37+00:00",
  "fields": {
    "endpointName": "client1",
    "uuid": 123
  },
  "ingested_start_date_time": "2021-04-06 08:22:37+00:00",
  "interval": 1800,
  "query_op": "or"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|oats|[]oat|True|Array of Observed Attack Techniques events|["<<referenced:bigdata>>"]|
|total_count|integer|True|Number of Observed Attack Techniques events retrieved|5|
  
Example output:

```
{
  "oats": [
    "<<referenced:bigdata>>"
  ],
  "total_count": 5
}
```

#### Poll Sandbox Suspicious List

This trigger is used to polls the suspicious object list associated to the specified object. Note ~ Suspicious Object 
Lists are only available for objects with a high risk level

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Unique alphanumeric string that identifies the analysis results of a submission|None|6345645|None|None|
|interval|integer|1800|True|Interval (in seconds) in which the polling script should run again|None|1800|None|None|
|poll|boolean|True|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|None|None|
|poll_time_sec|float|30|False|Maximum time to wait for the result to be available|None|15.5|None|None|
  
Example input:

```
{
  "id": 6345645,
  "interval": 1800,
  "poll": true,
  "poll_time_sec": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|sandbox_suspicious_list_resp|[]sandbox_suspicious_list_resp|True|Sandbox Suspicious Object List Response|[{"analysis_completion_date_time":"2023-01-11T22:40:52Z","expired_date_time":"2023-02-10T22:40:52Z","risk_level":"high","root_sha1":"ccc8c28226224755091a3462ff7704e350f2114b","type":"fileSha1","value":"0d8b8f0baf22e65a80148bcebaef082ef08932d2"}]|
  
Example output:

```
{
  "sandbox_suspicious_list_resp": [
    {
      "analysis_completion_date_time": "2023-01-11T22:40:52Z",
      "expired_date_time": "2023-02-10T22:40:52Z",
      "risk_level": "high",
      "root_sha1": "ccc8c28226224755091a3462ff7704e350f2114b",
      "type": "fileSha1",
      "value": "0d8b8f0baf22e65a80148bcebaef082ef08932d2"
    }
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**multi_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Status|integer|None|True|Status Code of response|None|
|Task ID|string|None|False|Task ID in Trend Vision One of the executed action|None|
  
**suspicious_objects**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description|None|
|Domain|string|None|False|Support leading wildcard|None|
|Expired Date Time|string|None|None|Timestamp in ISO 8601 format that indicates when the suspicious object expires|2023-04-14 06:55:29+00:00|
|File SHA1|string|None|False|Support only full match (40 characters)|None|
|File SHA256|string|None|False|Support only full match (64 characters)|None|
|In Exception List|boolean|None|True|Value that indicates if a suspicious object is in the exception list|None|
|IP|string|None|False|Support only full match|200.102.35.1|
|Last Modified Date Time|string|None|True|Timestamp in ISO 8601 format that indicates the last time the information about a suspicious object was modified|2023-04-14 06:55:29+00:00|
|Risk Level|string|None|True|Risk level of a suspicious object|None|
|Scan Action|string|None|True|Action that connected products apply after detecting a suspicious object|None|
|Sender Mail Address|string|None|False|Support fully qualified email address|None|
|Type|string|None|True|The type of suspicious object|None|
|URL|string|None|False|Support leading and tailing wildcards|None|
  
**exception_objects**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description|None|
|Domain|string|None|False|Support leading wildcard|None|
|File SHA1|string|None|False|Support only full match (40 characters)|None|
|File SHA256|string|None|False|Support only full match (64 characters)|None|
|IP|string|None|False|Support only full match|200.102.35.1|
|Last Modified Date Time|string|None|True|The time the object was created.|2023-04-14 06:55:29+00:00|
|Sender Mail Address|string|None|False|Support fully qualified email address|None|
|Type|string|None|True|The type of exception object|None|
|URL|string|None|False|Support leading and tailing wildcards|None|
  
**endpoint_data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent GUID|string|None|True|Unique alphanumeric string that identifies an endpoint agent on the Trend Vision One platform|None|
|Endpoint Name|object|None|True|Hostname of an endpoint with timestamp|None|
|Installed Product Codes|[]string|None|True|A 3-character code that identifies the installed Trend Micro products on an endpoint|None|
|IP|object|None|True|IPs of an endpoint with timestamp|None|
|Login Account|object|None|True|User accounts of an endpoint with timestamp|None|
|MAC Address|object|None|True|MAC Address of an endpoint with timestamp|None|
|OS Description|string|None|True|Description of the operating system installed on an endpoint|None|
|OS Name|string|None|True|Operating system installed on an endpoint|None|
|OS Version|string|None|True|Version of the operating system installed on an endpoint|None|
|Product Code|string|None|True|A 3-character code that identifies Trend Micro products|None|
  
**submit_urls_resp**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Digest|object|None|False|Object containing the hashes of the URL submitted|None|
|ID|string|None|False|Unique alphanumeric string that identifies a submission|0so47fy9|
|Status|integer|None|False|The Status Code of the submitted URL task|None|
|Task ID|string|None|False|The Task ID of the submitted URL|None|
|URL|string|None|True|This is the URL you submitted|None|
  
**sandbox_suspicious_list_resp**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Analysis Completion Date Time|string|None|True|Analyze time of suspicious object|2023-04-14 06:55:29+00:00|
|Expired Date Time|string|None|True|Expire time of suspicious object|2023-04-14 06:55:29+00:00|
|Risk Level|string|None|True|Risk Level of suspicious object|None|
|Root SHA1|string|None|True|Sample SHA1 generate this suspicious object|None|
|Type|string|None|True|Type of suspicious object|None|
|Value|string|None|True|Value of suspicious object|None|
  
**process_identifiers**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent GUID|string|None|False|Agent GUID of the endpoint to collect file from|cb9c8412-1f64-4fa0-a36b-76bf41a07ede|
|Description|string|None|False|Optional Description|Terminate Process|
|Endpoint|string|None|False|Hostname or macaddr of the endpoint to collect file from|clientPC|
|File SHA1|string|None|True|SHA1 hash of the process to terminate|c88878f98c7c2b5d9c551a0e99496d0dc7d0367c|
|Filename|string|None|False|Optional file name list for log|v1rus.exe|
  
**endpoint_identifiers**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent GUID|string|None|False|Agent GUID of the endpoint to collect file from|cb9c8412-1f64-4fa0-a36b-76bf41a07ede|
|Description|string|None|False|Optional Description|Isolate Endpoint|
|Endpoint|string|None|False|Hostname or macaddr of the endpoint to collect file from|clientPC|
  
**account_identifiers**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account Name|string|None|True|The User account that needs to be acted upon|account1|
|Description|string|None|False|Description of a response task|This is a regular user account|
  
**email_identifiers**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Optional description for reference|Quarantine e-mail message|
|Mailbox|string|None|False|Email address|user@example.com|
|Message ID|string|None|True|Unique string that identifies an email message (<mailMsgId> or msgUuid)|AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AAhCCNvg5sEua0nNjgfLS2AABNpgLcwAA|
  
**collect_files**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent GUID|string|None|False|Agent GUID of the endpoint to collect file from|cb9c8412-1f64-4fa0-a36b-76bf41a07ede|
|Description|string|None|False|Optional Description of the file|this file got on my computer from www.shadyfiles.com|
|Endpoint|string|None|False|Hostname or macaddr of the endpoint to collect file from|clientPC|
|File Path|string|None|True|Path to the file to collect. (<= 1024 characters)|C://v1rus.exe|
  
**block_objects**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Optional description for reference|Add to exception list|
|Object Type|string|None|True|Object type- domain, IP, fileSha1, fileSha256, senderMailAddress or URL|ip|
|Value|string|None|True|The object value. Full and partial matches supported|127.127.127.127|
  
**suspicious_block_objects**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Days to Expiration|integer|None|False|Indicates the number of days before the object expires. If daysToExpiration is -1, the object does not have an expiration date|None|
|Object Type|string|None|True|Object type- domain, IP, fileSha1, fileSha256, senderMailAddress or URL|ip|
|Value|string|None|True|The object value. Full and partial matches supported|127.127.127.127|
|Risk Level|string|None|False|Risk level of a suspicious object|None|
|Scan Action|string|None|False|Action that connected products apply after detecting a suspicious object|None|
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert Provider|string|None|False|Alert Provider|None|
|Campaign|string|None|False|An object-ref to a campaign object|None|
|Created By|string|None|False|Created By|None|
|Created Date Time|string|None|False|Datetime in ISO 8601 format (yyyy-MM-ddThh:mm:ssZ in UTC) that indicates the created date time of the alert|2023-04-14 06:55:29+00:00|
|Description|string|None|False|Description of the detection model that triggered the alert|None|
|ID|string|None|False|Workbench ID|None|
|Impact Scope|object|None|False|Affected entities information|None|
|Indicators|[]object|None|False|The indicators refer to those objects which are found by RCA or sweeping|None|
|Industry|string|None|False|Industry|None|
|Investigation Status|string|None|False|Workbench alert status|None|
|Matched Indicator Count|integer|None|False|Matched indicator pattern count|None|
|Matched Indicator Patters|[]object|None|False|The matched indicator patterns|None|
|Matched Rules|[]object|None|False|The rules are triggered|None|
|Model|string|None|False|Name of the detection model that triggered the alert|None|
|Region and Country|string|None|False|Region/Country (The region field would follow the STIX2.1 standard. The country field would follow the Alpha-2 standard. If only region or country is provided, the slash would be removed.)|None|
|Report Link|string|None|False|A refrerence URL which links to the report details analysis. For TrendMico research report, the link would link to trend blog|None|
|Schema Version|string|None|False|The version of the JSON schema, not the version of alert trigger content|None|
|Score|integer|None|False|Overall severity assigned to the alert based on the severity of the matched detection model and the impact scope|None|
|Severity|string|None|False|Workbench alert severity|None|
|Total Indicator Count|integer|None|False|Total indicator pattern count|None|
|Updated Date Time|string|None|False|Datetime in ISO 8601 format (yyyy-MM-ddThh:mm:ssZ in UTC) that indicates the last updated date time of the alert|2023-04-14 06:55:29+00:00|
|Workbench Link|string|None|False|Workbench URL|None|
  
**custom_scripts_list_resp**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Task Description|None|
|File Name|string|None|True|File name of a custom script|None|
|File Type|string|None|True|File type of a custom script|None|
|ID|string|None|True|Unique alphanumeric string that identifies a script file|None|
  
**email_activity_data_resp**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Event Time|integer|None|False|Date and time UTC|None|
|Mail From Addresses|[]string|None|False|Sender email address of the email message|None|
|Mail Message ID|string|None|False|Internet message ID of the email message|None|
|Mail Message Subject|string|None|False|Subject of the email message|None|
|Mail Sender IP|string|None|False|Source IP address of the email message|None|
|Mail Source Domain|string|None|False|Source domain of the email message|None|
|Mail To Addresses|[]string|None|False|A list of recipient email addresses of the email message|None|
|Mail URLs Real Link|[]string|None|False|Real link in email message|None|
|Mail URLs Visible Link|[]string|None|False|Visible link in email message|None|
|Mail Whole Header|[]string|None|False|Information about the header of the email message|None|
|Mailbox|string|None|False|Mailbox where the email message is|None|
|Message UUID|string|None|False|Unique ID of the email message|None|
|Organization ID|string|None|False|Unique ID used to identify an organization|None|
|Scan Type|string|None|False|Scan type|None|
|Search Data Lake|string|None|False|Search data lake|None|
  
**endpoint_activity_data_resp**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|DPT|integer|None|False|Destination port|None|
|DST|string|None|False|Destination IP address|None|
|Endpoint GUID|string|None|False|endpoint GUID for identity|None|
|Endpoint Host Name|string|None|False|Hostname of the endpoint on which the event was generated|None|
|Endpoint IP|[]string|None|False|Endpoint IP address list|None|
|Event ID|string|None|False|Event ID|None|
|Event Sub ID|integer|None|False|Event Sub ID|None|
|Event Time|integer|None|False|Log collect time UTC format|None|
|Event Time D T|string|None|False|Log collect time|None|
|Host Name|string|None|False|Hostname of the endpoint on which the event was generated|None|
|Logon User|[]string|None|False|Logon user name|None|
|Object Cmd|string|None|False|Command line entry of target process|None|
|Object File Hash SHA1|string|None|False|The SHA1 hash of target process image or target file|None|
|Object File Path|string|None|False|File path location of target process image or target file|None|
|Object Host Name|string|None|False|Server name where Internet event was detected|None|
|Object Integrity Level|integer|None|False|Object Integrity Level|None|
|Object IP|string|None|False|IP address of internet event|None|
|Object Ips|[]string|None|False|IP address list of internet event|None|
|Object Port|integer|None|False|The port number used by internet event|None|
|Object Registry Data|string|None|False|The registry value data|None|
|Object Registry Key Handle|string|None|False|The registry key|None|
|Object Registry Value|string|None|False|Registry value name|None|
|Object Signer|[]string|None|False|Certificate signer of object process or file|None|
|Object Signer Valid|[]boolean|None|False|Validity of certificate signer|None|
|Object Sub True Type|integer|None|False|Object Sub True Type|None|
|Object True Type|integer|None|False|Object True Type|None|
|Object User|string|None|False|The owner name of target process / The logon user name|None|
|OS|string|None|False|SYSTEM|None|
|Parent Cmd|string|None|False|The command line that parent process|None|
|Parent File Hash SHA1|string|None|False|The SHA1 hash of parent process|None|
|Parent File Path|string|None|False|The file path location of parent process|None|
|Process Cmd|string|None|False|The command line used to launch this process|None|
|Process File Hash SHA1|string|None|False|The process file SHA1|None|
|The process file path|string|None|False|Process File Path|None|
|Request|string|None|False|Request URL normally detected by Web Reputation Services|None|
|Search Data Lake|string|None|False|Search data lake|None|
|SPT|integer|None|False|Source port|None|
|SRC|string|None|False|Source IP address|None|
|Src File Hash SHA1|string|None|False|Source file SHA1|None|
|Src File Path|string|None|False|Src File Path|None|
|Tags|[]string|None|False|Detected by Security Analytics Engine filters|None|
|UUID|string|None|False|Log unique identity|None|
|Win Event ID|integer|None|False|Win Event ID|None|
  
**api_keys_objects**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|A brief note about the API key|None|
|Months to Expiration|string|None|False|The duration of validity for the API key (in months, 0 for no expiration)|None|
|Name|string|None|True|The unique name of an API key|None|
|Role|string|None|True|The user role assigned to the API key|None|
|Status|string|None|False|The status of an API key|None|
  
**api_keys_resp**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Expired Date Time|string|None|True|Timestamp in ISO 8601 format indicating the expiration date of the API key|None|
|ID|string|None|True|The unique identifier of the API key|None|
|Status|integer|None|True|The Status Code of the submitted API keys task|None|
|Value|string|None|True|The API key|None|
  
**api_keys_list_resp**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|A brief note about the API key|None|
|Expired Date Time|string|None|True|Timestamp in ISO 8601 format indicating the expiration date of the API key|None|
|ID|string|None|True|The unique identifier of the API key|None|
|Last Used Date Time|string|None|True|The last time the API key was used in ISO 8601 format|None|
|Name|string|None|True|The unique name of an API key|None|
|Role|string|None|True|The user role assigned to the API key|None|
|Status|string|None|False|The status of an API key|None|
  
**oat**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Detail|object|None|True|Object that contains detailed information about an Observed Attack Technique event|None|
|Detected Date Time|string|None|True|The date and time the OAT event was detected in ISO 8601 format|2021-04-05 08:22:37+00:00|
|Endpoint|object|None|False|Object that contains information about an endpoint|None|
|Entity Type|string|None|True|Name associated with an entity|None|
|Filters|[]object|None|True|The filters associated with the OAT|None|
|Ingested Date Time|string|None|False|The date and time the data related to the OAT event was ingested in ISO 8601 format|2021-04-06 08:22:37+00:00|
|Source|string|None|True|The data sources associated with log types|None|
|UUID|string|None|True|The unique identifier of an Observed Attack Techniques event|None|


## Troubleshooting

For additional info about actions see https://automation.trendmicro.com/xdr/api-v3#

# Version History

* 5.0.0 - Removed app name from connection
* 4.1.0 - Added OAT list action and trigger, limit query size
* 4.0.0 - Added API Keys related actions
* 3.0.0 - Refactored pytmv1 usage | Added Custom Scripts and Activity related actions
* 2.0.1 - Version bump of pytmv1 library
* 2.0.0 - Enabled multiple inputs for Get Endpoint Data, reduced API call frequency & General Refactoring
* 1.0.1 - Alert Details Output Fix (Minor Fix)
* 1.0.0 - Initial plugin

# Links

* [TrendMicro](https://www.trendmicro.com/en_us/business.html)

## References

* [Trend Vision One](https://docs.trendmicro.com/en-us/enterprise/trend-micro-xdr-help/home)