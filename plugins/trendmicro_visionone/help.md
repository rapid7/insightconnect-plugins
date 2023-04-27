# Description

Trend Micro Vision One is a purpose-built threat defense platform that provides added value and new benefits beyond XDR solutions, allowing you to see more and respond faster. Providing deep and broad extended detection and response (XDR) capabilities that collect and automatically correlate data across multiple security layers, email, endpoints, servers, cloud workloads, and networks. Trend Micro Vision One prevents the majority of attacks with automated protection.

# Key Features

* Add Alert Note
* Add to Block List
* Add to Exception List
* Add to Suspicious List
* Collect File
* Delete Email Message
* Disable Account
* Download Sandbox Analysis Result
* Download Sandbox Investigation Package
* Edit Alert Status
* Enable Account
* Get Alert Details
* Get Alert List
* Get Endpoint Data
* Get Exception List
* Get Sandbox Analysis Result
* Get Sandbox Submission Status
* Get Sandbox Suspicious List
* Get Suspicious List
* Get Task Result
* Poll Alert List
* Poll Sandbox Suspicious List

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

* Trend Micro Vision One API v3

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|Dummy-API-KEY|True|Vision One API Token|None|12345678-ABCD-1234-ABCD-123456789012:ABCDEFGH-1234-ABCD-1234-ABCDEFGHIJKL:02699626f388ed830012e5b787640e71c56d42d81234|
|api_url|string|https://example.com|True|URL of Trend Micro Vision One|None|https://example.com|
|app_name|string|Rapid7-InsightConnect|True|Name of the App to be Integrated with|None|Rapid7-InsightConnect|
|verify_ssl|boolean|True|True|Verify if connection uses SSL|None|True|

Example input:

```
{
  "api_key": "12345678-ABCD-1234-ABCD-123456789012:ABCDEFGH-1234-ABCD-1234-ABCDEFGHIJKL:12345678901234567890123456789012345678901234",
  "api_url": "https://apimock-dev.trendmicro.com",
  "app_name": "Rapid7-InsightConnect",
  "verify_ssl": true
}
```

## Technical Details

### Actions

#### Restore Email Message

This action restores a quarantined email message.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email_identifiers|[]email_identifiers|None|True|Email Identifiers consisting of message id, mailbox and description|None|List of email identifiers in JSON syntax|

Example input:

```
{
  "email_identifiers": "List of email identifiers in JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Delete Email Message Response Array|

Example output:

```
```

#### Get Alert Details

This action displays information about workbench alerts that match the specified criteria in a paginated list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|ID of the Alert to get the details of|None|WB-20837-20221111-0000|

Example input:

```
{
  "alert_id": "WB-20837-20221111-0000"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert_details|alert|True|The details of the alert|
|etag|string|True|An identifier for a specific version of a Workbench alert resource|

Example output:

```
{
  "alert_details": {
    "alert": "{\"id\": \"WB-20837-20221222-00000\", \"schema_version\"..."
  },
  "etag": "\"0eaa4c39854bd42dcd9f09d5952c4e63c\""
}
```

#### Remove from Block List

This action removes an email address, file SHA-1, domain, IP address, or URL that was added to the Suspicious Object List using the "Add to block list" action.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|block_object|[]block_object|None|True|Object object made up of type, value and description|None|Block object consiting of object_type, object_value, description|

Example input:

```
{
  "block_object": "Block object consiting of object_type, object_value, description"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Remove From Block List Response Array|

Example input:

```
```

##### Output

|Name|Type|Required| Description                           |
|----|----|--------|---------------------------------------|
|multi_response|[]multi_response|True| Remove from Block List Response Array |

Example output:

```
```

#### Submit URLs to Sandbox

This action submits URLs to the sandbox for analysis. You can submit a maximum of 10 URLs per request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|[]string|None|True|URL(s) to be submitted, formated as bracket array separated by comma|None|https://example.com|

Example input:

```
{
  "url": "https://www.trendmicro.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submit_urls_resp|[]submit_urls_resp|True|Submit URLSs response Array|

Example output:

```
```

#### Add to Block List

This action adds an email address, file SHA-1, domain, IP address, or URL to the Suspicious Object List, which blocks the objects on subsequent detections.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|block_object|[]block_object|None|True|Object object made up of type, value and description|None|Block object consiting of object_type, object_value, description|

Example input:

```
{
  "block_object": "Block object consiting of object_type, object_value, description"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Add To Block List Response Array|

Example input:

```
```

##### Output

|Name|Type|Required| Description                      |
|----|----|--------|----------------------------------|
|multi_response|[]multi_response|True| Add to Block List Response Array |

Example output:

```
```

#### Submit File to Sandbox

This action submits a file to the sandbox for analysis (Note. For more information about the supported file types, see the Trend Micro Vision One Online Help. Submissions require credits. Does not require credits in regions where Sandbox Analysis has not been officially released.).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|archive_password|string|None|False|Password encoded in Base64 used to decrypt the submitted archive. The maximum password length (without encoding) is 128 bytes|None|1234|
|arguments|string|None|False|Parameter that allows you to specify Base64-encoded command line arguments to run the submitted file. The maximum argument length before encoding is 1024 bytes. Arguments are only available for Portable Executable (PE) files and script files|None|IFMlYztbQA==|
|document_password|string|None|False|Password encoded in Base64 used to decrypt the submitted file sample. The maximum password length (without encoding) is 128 bytes|None|1234|
|file|file|None|False|File submitted to the sandbox (dict of {filename(string) & content(base64(bytes))})|None|file binary|

Example input:

```
{
  "archive_password": 1234,
  "arguments": "IFMlYztbQA==",
  "document_password": 1234,
  "file": "file binary"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|arguments|string|False|Command line arguments encoded in Base64 of the submitted file|
|digest|object|True|The hash value of the file|
|id|string|True|Unique alphanumeric string that identifies a submission|

Example output:

```
```

#### Sign out Account

This action signs the user out of all active application and browser sessions. Supported IAM systems - Azure AD..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_identifiers|[]account_identifiers|None|True|User Account Identifiers containing account name and description|None|List of account identifier objects in proper JSON syntax|

Example input:

```
{
  "account_identifiers": "List of account identifier objects in proper JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Sign out Account Response Array|

Example output:

```
```

#### Reset Password Account

This action signs the user out of all active application and browser sessions, and forces the user to create a new password during the next sign-in attempt. Supported IAM systems - Azure AD and Active Directory (on-premises)..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_identifiers|[]account_identifiers|None|True|User Account Identifiers containing account name and description|None|List of account identifier objects in proper JSON syntax|

Example input:

```
{
  "account_identifiers": "List of account identifier objects in proper JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Reset Password Account Response Array|

Example output:

```
```

#### Remove from Suspicious List

This action removes domains, file SHA-1 values, IP addresses, or URLs from the Suspicious Object List.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|block_object|[]block_object|None|True|Object object made up of type, value and description|None|Block object consiting of object_type, object_value, description|

Example input:

```
{
  "block_object": "Block object consiting of object_type, object_value, description"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Add To Exception List Response Array|

Example input:

```
```

##### Output

|Name|Type|Required| Description                          |
|----|----|--------|--------------------------------------|
|multi_response|[]multi_response|True| Add to Exception List Response Array |

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

#### Remove from Exception List

This action removes domains, file SHA-1 values, IP addresses, or URLs from the Exception List..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|block_object|[]block_object|None|True|Object object made up of type, value and description|None|Block object consiting of object_type, object_value, description|

Example input:

```
{
  "block_object": "Block object consiting of object_type, object_value, description"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Remove From Exception List Response Array|

Example input:

```
```

##### Output

|Name|Type|Required| Description                               |
|----|----|--------|-------------------------------------------|
|multi_response|[]multi_response|True| Remove from Exception List Response Array |

Example output:

```
```

#### Get Endpoint Data

This action retrieves information about a specific endpoint.

##### Input

|Name|Type|Default|Required| Description                                                    |Enum|Example|
|----|----|-------|--------|----------------------------------------------------------------|----|-------|
|endpoint|string|None|True| hostname, macAddress, agentGuid or IP of the endpoint to query |None|https://example.com|
|query_op|string| or |True| Logical operator to employ in the query. (AND/OR)              |[' or ', ' and ']| or |

Example input:

```
{
  "endpoint": "127.127.127.127",
  "query_op": " or "
}
```

##### Output

|Name|Type|Required| Description                                                                                                                                                                           |
|----|----|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|endpoint_data|[]endpoint_data|True| Array of Endpoint Data Objects, consisting of agent guid, login account, endpoint name, MAC address, IP, os name, or version, os description, product code and installed product code |

Example output:

```
```

#### Enable Account

This action allows the user to sign in to new application and browser sessions. Supported IAM systems - Azure AD and Active Directory (on-premises)..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_identifiers|[]account_identifiers|None|True|User Account Identifiers containing account name and description|None|List of account identifier objects in proper JSON syntax|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|endpoint_data|[]endpoint_data|True|Array of Endpoint Data Objects, consisting of agent guid, login account, endpoint name, MAC address, IP, os name, or version, os description, product code and installed product code|

Example input:

```
{
  "account_identifiers": "List of account identifier objects in proper JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Enable Account Response Array|

Example input:

```
{
  "account_identifiers": [
    {
      "account_name": "jdoe@emailpage.com",
      "description": "enable jdoe account, test"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Enable Account Response Array|

Example output:

```
  "multi_response": [
    {
      "status": 202,
      "task_id": "00002148"
    }
  ]
```

#### Download Sandbox Analysis Result

This action downloads the analysis result for an object submitted to sandbox for analysis based on the submission ID..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Unique alphanumeric string that identifies the analysis results of a submission|None|6345645|
|poll|boolean|None|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|
|poll_time_sec|float|None|False|Maximum time to wait for the result to be available|None|True|

Example input:

```
{
  "id": "6345645",
  "poll": true,
  "poll_time_sec": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|file|True|The response is a .pdf file|

Example output:

```
```

#### Disable Account

This action signs the user out of all active application and browser sessions, and prevents the user from signing in any new session. Supported IAM systems - Azure AD and Active Directory (on-premises)..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_identifiers|[]account_identifiers|None|True|User Account Identifiers containing account name and description|None|List of account identifier objects in proper JSON syntax|

Example input:

```
{
  "account_identifiers": "List of account identifier objects in proper JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Disable Account Response Array|

Example output:

```
```

#### Add to Suspicious List

This action adds domains, file SHA-1/SHA-256 values, IP addresses, senderMailAddress, or URLs to the Suspicious Object List..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|suspicious_block_object|[]suspicious_block_object|None|True|Suspicious Object object made up of type, value and scan_action, risk_level and days_to_expiration|None|An object consisting of object_type, object_value, scan_action, risk_level and days_to_expiration|

Example input:

```
{
  "suspicious_block_object": "An object consisting of object_type, object_value, scan_action, risk_level and days_to_expiration"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Add To Exception List Response Array|

Example input:

```
```

##### Output

|Name|Type|Required| Description                          |
|----|----|--------|--------------------------------------|
|multi_response|[]multi_response|True| Add to Exception List Response Array |

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

#### Add to Exception List

This action adds domains, file SHA-1 values, IP addresses, or URLs to the Exception List and prevents these objects from being added to the Suspicious Object List.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|block_object|[]block_object|None|True|Object object made up of type, value and description|None|Block object consiting of object_type, object_value, description|

Example input:

```
{
  "block_object": "Block object consiting of object_type, object_value, description"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Add To Exception List Response Array|

Example input:

```
```

##### Output

|Name|Type|Required| Description                          |
|----|----|--------|--------------------------------------|
|multi_response|[]multi_response|True| Add to Exception List Response Array |

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

#### Restore Endpoint

This action restores network connectivity to an endpoint that applied the isolate endpoint action..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|endpoint_identifiers|[]endpoint_identifiers|None|True|Endpoint Identifiers consisting of endpoint(hostname or agentGuid) and description|None|List of endpoint identifier objects in proper JSON syntax|

Example input:

```
{
  "endpoint_identifiers": "List of endpoint identifier objects in proper JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Restore Endpoint Response Array|

Example output:

```
```

#### Get Task Result

This action retrieves an object containing the results of a response task in JSON format..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|poll|boolean|None|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|
|poll_time_sec|float|None|False|Maximum time to wait for the result to be available|None|True|
|task_id|string|None|True|TaskId output from the collect command used to collect the file|None|3456346|

Example input:

```
{
  "poll": true,
  "poll_time_sec": true,
  "task_id": 3456346
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|account|string|False|User that triggered the response|
|action|string|True|Command sent to the target|
|agent_guid|string|False|Unique alphanumeric string that identifies an installed agent|
|created_date_time|string|True|Timestamp in ISO 8601 format|
|description|string|False|Task Description|
|endpoint_name|string|False|Endpoint name of the target endpoint|
|expired_date_time|string|False|The expiration date and time of the file|
|file_path|string|False|File path for the file that was collected|
|file_sha1|string|False|The fileSHA1 of the collected file|
|file_sha256|string|False|The fileSHA256 of the collected file|
|file_size|integer|False|The file size of the file collected|
|filename|string|False|File name of a response task target (<= 255)|
|id|string|False|Unique numeric string that identifies a response task|
|image_path|string|False|File path of a process image|
|last_action_date_time|string|True|Timestamp in ISO 8601 format|
|password|string|False|The password of the file collected|
|pid|integer|False|Unique numeric string that identifies an active process|
|resource_location|string|False|URL location of the file collected that can be used to download|
|sandbox_task_id|string|False|Unique alphanumeric string that identifies a task generated by the Sandbox Analysis App|
|status|string|True|The status of the command sent to the managing server. Possible task statuses; queued - The server queued the command due to a high volume of requests or because the Security Agent was offline; running - Trend Micro Vision One sent the command to the managing server and is waiting for a response; succeeded - The managing server successfully received the command; rejected - The server rejected the task. For automated response task only; waitForApproval - The task is pending approval. For automated response task only; failed - An error or time-out occurred when attempting to send the command to the managing server|
|tasks|[]object|False|Currently, it is only possible to apply tasks to one message in a mailbox or one message in several mailboxes|
|url|string|False|Universal Resource Locator|

Example output:

```
```

#### Get Suspicious List

This action retrieves information about domains, file SHA-1, file SHA-256, IP addresses, email addresses, or URLs in the Suspicious Object List and displays the information in a paginated list..

##### Input

_This action does not contain any inputs._

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|suspicious_objects|[]suspicious_objects|True|Array of any Suspicious Objects|

Example output:

```
{
  "suspicious_objects": [
    {
      "type": "url",
      "url": "http://test.com",
      "description": "object description",
      "expired_date_time": "2023-03-29T14:45:38Z",
      "in_exception_list": false,
      "last_modified_date_time": "2023-03-29T14:45:38Z",
      "risk_level": "high",
      "scan_action": "log"
    }
  ]
}
```

#### Get Sandbox Suspicious List

This action downloads the suspicious object list associated to the specified object. Note ~ Suspicious Object Lists are only available for objects with a high risk level..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Unique alphanumeric string that identifies the analysis results of a submission|None|6345645|
|poll|boolean|None|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|
|poll_time_sec|float|None|False|Maximum time to wait for the result to be available|None|True|

Example input:

```
{
  "id": "6345645",
  "poll": true,
  "poll_time_sec": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sandbox_suspicious_list_resp|[]sandbox_suspicious_list_resp|True|Sandbox Suspicious Object List Response|

Example output:

```
{
  "sandbox_suspicious_list_resp": [
    {
      "type": "fileSha1",
      "value": "0d8b8f0baf22e65a80148bcebaef082ef08932d2",
      "analysis_completion_date_time": "2023-01-11T22:40:52Z",
      "expired_date_time": "2023-02-10T22:40:52Z",
      "risk_level": "high",
      "root_sha1": "ccc8c28226224755091a3462ff7704e350f2114b"
    }
  ]
}
```

#### Get Sandbox Submission Status

This action retrieves the status of a sandbox analysis submission.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|task_id|string|None|True|Task_id from the trendmicro-visionone-submit-file-to-sandbox command output|None|02384|

Example input:

```
{
  "task_id": "02384"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|action|string|True|Action applied to a submitted object|
|arguments|string|False|Arguments for the file submitted|
|created_date_time|string|True|Timestamp in ISO 8601 that indicates the object was submitted to the sandbox|
|digest|object|False|The hash values for the file analyzed|
|error|object|False|Error code and message for the submission|
|id|string|True|Unique alphanumeric string that identifies a submission|
|is_cached|boolean|False|Parameter that indicates if an object has been analyzed before by the Sandbox Analysis App. Submissions marked as cached do not count toward the daily reserve|
|last_action_date_time|string|True|Timestamp in ISO 8601 format that indicates when the information about a submission was last updated|
|resource_location|string|False|Location of the submitted file|
|status|string|True|Response code for the action call|

Example output:

```
```

#### Get Sandbox Analysis Result

This action retrieves the sandbox analysis results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|poll|boolean|None|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|
|poll_time_sec|float|None|False|Maximum time to wait for the result to be available|None|True|
|report_id|string|None|True|Report_id of the sandbox submission retrieved from the trendmicro-visionone-get-file-analysis-status command|None|02384|

Example input:

```
{
  "poll": true,
  "poll_time_sec": true,
  "report_id": "02384"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analysis_completion_date_time|string|True|Timestamp in ISO 8601 format that indicates when the analysis was completed|
|arguments|string|False|Command line arguments encoded in Base64 of the submitted file|
|detection_names|[]string|False|The name of the threat as detected by the sandbox|
|digest|object|False|The hash values of the analyzed file|
|id|string|True|Unique alphanumeric string that identifies the analysis results of a submitted object|
|risk_level|string|True|The risk level assigned to the object by the sandbox|
|threat_types|[]string|False|The threat type as detected by the sandbox|
|true_file_type|string|False|File Type of the Object|
|type|string|True|Object Type|

Example output:

```
```

#### Get Exception List

This action retrieves information about domains, file SHA-1, file SHA-256, IP addresses, sender addresses, or URLs in the Exception List and displays it in a paginated list..

##### Input

_This action does not contain any inputs._

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|exception_objects|[]exception_objects|True|Array of any Exception Objects|

Example output:

```
{
  "exception_objects": [
    {
      "description": "object description",
      "last_modified_date_time": "2023-03-29T14:47:44Z",
      "type": "url",
      "url": "https://*.example.com/path1/*"
    }
  ]
}
```

#### Get Alert List

This action displays information about workbench alerts that match the specified criteria in a paginated list..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|end_date_time|string|None|True|Datetime in ISO 8601 format (yyyy-MM-ddThh:mm:ssZ in UTC) that indicates the end of the data retrieval time range. Ensure that "endDateTime" is not earlier than "startDateTime"|None|endDateTime=2020-06-15T12:00:00Z|
|start_date_time|string|None|True|Datetime in ISO 8601 format (yyyy-MM-ddThh:mm:ssZ in UTC) that indicates the start of the data retrieval time range. The available oldest value is "1970-01-01T00:00:00Z"|None|startDateTime=2020-06-15T10:00:00Z|

Example input:

```
{
  "end_date_time": "endDateTime=2020-06-15T12:00:00Z",
  "start_date_time": "startDateTime=2020-06-15T10:00:00Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert|True|Array of any alerts (awb-workbenchAlertV3)|
|total_count|integer|True|Number of Workbench alerts retrieved|

Example output:

```
```

#### Edit Alert Status

This action updates the status of a workbench alert..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Workbench alert ID|None|WB-14-20190709-00003|
|if_match|string|None|False|The target resource will be updated only if it matches ETag of the target one|None|9de5069c5afe602b2ea0a04b66beb2c0|
|status|string|None|True|ID of the workbench you would like to update the status for|['New', 'In Progress', 'True Positive', 'False Positive']|New|

Example input:

```
{
  "id": "WB-14-20190709-00003",
  "if_match": "d41d8cd98f00b204e9800998ecf8427e",
  "status": "New"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result_code|string|True|Result code of response|

Example output:

```
```

#### Download Sandbox Investigation Package

This action downloads the investigation package based on submission ID..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Unique alphanumeric string that identifies the analysis results of a submission|None|6345645|
|poll|boolean|None|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|
|poll_time_sec|float|None|False|Maximum time to wait for the result to be available|None|True|

Example input:

```
{
  "id": "6345645",
  "poll": true,
  "poll_time_sec": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|file|True|The output is a .zip file|

Example output:

```
```

#### Collect File

This action collects a file from one or more endpoints and then sends the files to Trend Micro Vision One in a password-protected archive Note- You can specify either the computer name ("endpointName") or the GUID of the installed agent program ("agentGuid")..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|collect_files|[]collect_files|None|True|Collect file input JSON containing endpoint, file path and description|None|JSON list object containing necessary fields|

Example input:

```
{
  "collect_files": "JSON list object containing necessary fields"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Add To Block List Response Array|

Example input:

```
{
  "collect_files": "JSON list object containing necessary fields"
}
```

##### Output

|Name|Type|Required| Description                      |
|----|----|--------|----------------------------------|
|multi_response|[]multi_response|True| Add to Block List Response Array |

Example output:

```
```

#### Add Alert Note

This action attaches a note to a workbench alert..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Unique alphanumeric string that identifies a Workbench alert|None|WB-14-20190709-00003|
|content|string|None|True|Unique alphanumeric string that identifies a Workbench alert|None|Suspected False Positive, please verify|

Example input:

```
{
  "alert_id": "WB-14-20190709-00003",
  "content": "Suspected False Positive, please verify"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|location|string|True|URL of the created resource|
|note_id|string|True|ID of the note created|
|result_code|string|True|Result message of adding workbench note|

Example output:

```
```

#### Delete Email Message

This action deletes a message from a mailbox..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email_identifiers|[]email_identifiers|None|True|Email Identifiers consisting of message id, mailbox and description|None|List of email identifiers in JSON syntax|

Example input:

```
{
  "email_identifiers": "List of email identifiers in JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Delete Email Message Response Array|

Example output:

```
```

#### Isolate Endpoint

This action disconnects an endpoint from the network (but allows communication with the managing Trend Micro product).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|endpoint_identifiers|[]endpoint_identifiers|None|True|Endpoint Identifiers consisting of endpoint(hostname or agentGuid) and description|None|List of endpoint identifier objects in proper JSON syntax|

Example input:

```
{
  "endpoint_identifiers": "List of endpoint identifier objects in proper JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Isolate Endpoint Response Array|

Example output:

```
```

#### Quarantine Email Message

This action moves a message from a mailbox to the quarantine folder..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email_identifiers|[]email_identifiers|None|True|Email Identifiers consisting of message id, mailbox and description|None|List of email identifiers in JSON syntax|

Example input:

```
{
  "email_identifiers": "List of email identifiers in JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Quarantine Email Message Response Array|

Example output:

```
```

#### Terminate Process

This action terminates a process that is running on an endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|process_identifiers|[]process_identifiers|None|True|Process Identifiers consisting of endpoint(hostname or agentGuid), filesha1, filename(optional) and description(optional)|None|List of process identifier objects in proper JSON syntax|

Example input:

```
{
  "process_identifiers": "List of process identifier objects in proper JSON syntax"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|multi_response|[]multi_response|True|Terminate Process Response Array|

Example output:

```
```

### Triggers

#### Poll Alert List

This trigger polls information about workbench alerts that match the specified criteria in a paginated list..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|end_date_time|string|None|True|Datetime in ISO 8601 format (yyyy-MM-ddThh:mm:ssZ in UTC) that indicates the end of the data retrieval time range. Ensure that "endDateTime" is not earlier than "startDateTime"|None|endDateTime=2023-06-15T12:00:00Z|
|interval|integer|None|True|Interval (in seconds) in which the polling script should run again|None|1800|
|start_date_time|string|None|True|Datetime in ISO 8601 format (yyyy-MM-ddThh:mm:ssZ in UTC) that indicates the start of the data retrieval time range. The available oldest value is "1970-01-01T00:00:00Z"|None|startDateTime=2020-06-15T10:00:00Z|

Example input:

```
{
  "end_date_time": "endDateTime=2023-06-15T12:00:00Z",
  "interval": 1800,
  "start_date_time": "startDateTime=2020-06-15T10:00:00Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert|True|Array of any alerts (awb-workbenchAlertV3)|
|total_count|integer|True|Number of Workbench alerts retrieved|

Example output:

```
```

#### Poll Sandbox Suspicious List

This trigger polls the suspicious object list associated to the specified object. Note ~ Suspicious Object Lists are only available for objects with a high risk level..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Unique alphanumeric string that identifies the analysis results of a submission|None|6345645|
|interval|integer|None|True|Interval (in seconds) in which the polling script should run again|None|1800|
|poll|boolean|None|True|If script should wait until the task is finished before returning the result (enabled by default)|None|True|
|poll_time_sec|float|None|False|Maximum time to wait for the result to be available|None|True|

Example input:

```
{
  "id": "6345645",
  "interval": 1800,
  "poll": true,
  "poll_time_sec": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sandbox_suspicious_list_resp|[]sandbox_suspicious_list_resp|True|Sandbox Suspicious Object List Response|

Example output:

```
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

* [TrendMicro](https://www.trendmicro.com/en_us/business.html)

## References

* [Trend Micro Vision One](LINK TO PRODUCT/VENDOR WEBSITE)

