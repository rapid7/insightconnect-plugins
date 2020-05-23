# Description

Trend Micro Apex offers modern advanced automated threat detection and response.  Apex agents have more than antivirus
capabilities, they are an extension of the Apex threat management system.  
This plugin works for the on-premise or Apex SaaS configurations.

# Key Features

* Reporting suspicious IP addresses, URLs and other similar content
* Reporting suspicious files and their contents

# Requirements

* API URL for Apex SaaS or Apex on-premise
* API Key
* Application ID

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API key paired with the Application ID e.g. CU1874A2-G782-47X1-B6J3-1014A92624BC|None|CU1874A2-G782-47X1-B6J3-1014A92624BC|
|application_id|credential_secret_key|None|True|Application ID to communicate to the Apex Security Manager e.g. 909D88H7-3458-42RN-92FF-012V3CU3D294|None|909D88H7-3458-42RN-92FF-012V3CU3D294|
|url|string|None|True|URL with port number of the Apex Security Manager.|None|https://host.example.com:443|

Example input:

```
{
  "api_key": "CU1874A2-G782-47X1-B6J3-1014A92624BC",
  "application_id": "909D88H7-3458-42RN-92FF-012V3CU3D294",
  "url": "https://host.example.com:443"
}
```

## Technical Details

### Actions

#### Search Agents

This action is used to retrieve a list of security agents based on the available search terms.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_ids|[]string|None|False|The GUID, IP address, MAC address, hostname of the Security Agent|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_agent_response|[]search_agent_response|False|Search agent response|

Example output:

```
{}
```

#### Get Root Cause Analysis

This action retrieves results of investigations in different formats based on the specified taskId.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|content_id|string|None|False|Indicates the location of the dataset|None|8|
|limit|string|None|True|Retrieves the top n results from the servers|None|1|
|task_id|string|None|True|Task ID from another API call that is used to retrieve a specific task result Specify the taskId values returned by the following APIs|None|9BD2204C-0554-45C8-9C62-799284928AFA|
|task_type|string|CMEF|False|Type of API request. For Endpoint Sensor, the value is always 4|['UNKNOWN', 'INTERNAL', 'CM', 'CMEF', 'OSF_COMMAND', 'OSF_QUERY', 'OSF_NOTIFY', 'OSF_LOG', 'MDR_ATTACK_DISCOVERY', 'OSF_SYS_CALL']|CMEF|

Example input:

```
{
  "content_id": 8,
  "limit": "1",
  "task_id": "9BD2204C-0554-45C8-9C62-799284928AFA",
  "task_type": "CMEF"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|api_data|True|Contains the data returned by the specific API|
|FeatureCtrl|FeatureCtrl|False|The Apex Central deployment model|
|Meta|Meta|False|Indicates the response status, including the result, error code, and error message|
|PermissionCtrl|PermissionCtrl|False|Indicates the permissions assigned to the logged-on user account for accessing Apex Central menu items and features|
|SystemCtrl|SystemCtrl|False|Indicates the suspicious object distribution role of the Apex Central server|

Example output:

```
```

#### Get Agent Status

This action retrieves a list of all Security Agents with the Endpoint Sensor feature enabled.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_guid|string|None|True|GUID of the agent|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agentEntity|agentEntity|False|Agent entity data|
|agentQueryStatus|agentQueryStatus|False|Agent query status data|

Example output:

```
{}
```

#### Execute Agent Action

This action performs actions on the agent.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|Perform action|['Isolate', 'Restore', 'Relocate', 'Uninstall']|Isolate|
|allow_multiple_match|boolean|True|False|True - Allows multiple matches False - Does not allow multiple matches|None|True|
|entity_id|string|None|False|The GUID of the managed product agent. Use to identify the agent(s) on which the action is performed|None|2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6|
|host_name|string|None|False|The endpoint name of the managed product agent. Use to identify the agent(s) on which the action is performed|None|CU-PRO1-7814-2|
|ip_address|string|None|False|The IP address of the managed product agent. Use to identify the agent(s) on which the action is performed|None|198.51.100.100|
|mac_address|string|None|False|The MAC address of the managed product agent. Use to identify the agent(s) on which the action is performed|None|08:00:27:8d:c0:4d|
|product|string|None|False|The Trend Micro product on the server instance. Use to identify the agent(s) on which the action is performed|None|SLF_PRODUCT_OFFICESCAN_CE|
|relocate_to_folder_path|string|None|False|The target directory for the agent|None|\NewDomain\NewFolder|
|relocate_to_server_id|string|None|False|The GUID of the target server for the agent|None|C22E1795-BF95-45BB-BC82-486B0F5161BE|
|skip_ids|[]string|None|False|Skip entity ids on isolate and uninstall actions|None|["2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6"]|

Example input:

```
{
  "action": "Isolate",
  "allow_multiple_match": true,
  "entity_id": "2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6",
  "host_name": "CU-PRO1-7814-2",
  "ip_address": "198.51.100.100",
  "mac_address": "08:00:27:8d:c0:4d",
  "product": "SLF_PRODUCT_OFFICESCAN_CE",
  "relocate_to_folder_path": "\\NewDomain\\NewFolder",
  "relocate_to_server_id": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
  "skip_ids": "[\"2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6\"]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result_code|integer|False|The Apex Central Automation API result code|
|result_content|[]result_content|False|The Apex Central Automation API result content|
|result_description|string|False|The Apex Central Automation API result description|

Example output:

```
{
  "result_code": 1,
  "result_description": "Operation successful",
  "result_content": [
    {
      "entity_id": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
      "product": "SLF_PRODUCT_OFFICESCAN_CE",
      "managing_server_id": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
      "folder_path": "Workgroup",
      "ip_address_list": "10.0.2.15",
      "mac_address_list": "08-00-27-96-86-8E",
      "host_name": "TREND-MICRO-TES",
      "isolation_status": "normal",
      "capabilities": [
        "cmd_restore_isolated_agent",
        "cmd_isolate_agent",
        "cmd_relocate_agent",
        "cmd_uninstall_agent"
      ]
    }
  ]
}
```

#### List OpenIOC Files

This action retrieves a list of OpenIOC files from the Apex Central server.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_hash_id_list|[]string|[]|False|Filters the list for file SHA-1 values|None|["769fcc7550bf98d96bccb7e22a5557301c403455"]|
|fuzzy_match_string|string|None|False|Filters the list for matching strings in the File Name, Title, and Source Context fields|None|Rapid7 InsightConnect|
|page_number|integer|1|False|Filters the list to uploaded files that appear on the specified page number on the Threat Intel > Custom Intelligence > STIX tab|None|1|
|page_size|integer|10|False|Filters the list to the specified number of uploaded files per page|None|10|
|sorting_column|string|FileAddedDatetime|False|Sorts the list by the specified table column|['FileName', 'Title', 'FileAddedDatetime', 'UploadedFrom', 'UploadedBy', 'ExtractingStatus']|FileAddedDatetime|
|sorting_direction|string|Descending|False|Sorts the list in the specified direction|['Ascending', 'Descending']|Descending|

Example input:

```
{
  "file_hash_id_list": "[\"769fcc7550bf98d96bccb7e22a5557301c403455\"]",
  "fuzzy_match_string": "Rapid7 InsightConnect",
  "page_number": 1,
  "page_size": 10,
  "sorting_column": "FileAddedDatetime",
  "sorting_direction": "Descending"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|IOC_Data|False|Contains the data returned by the specific API|
|feature_ctrl|FeatureCtrl|False|The Apex Central deployment model|
|meta|Meta|False|Indicates the response status, including the result, error code, and error message|
|permission_ctrl|PermissionCtrl|False|Indicates the permissions assigned to the logged-on user account for accessing Apex Central menu items and features|
|system_ctrl|SystemCtrl|False|Indicates the suspicious object distribution role of the Apex Central server|

Example output:

```
{
  "Data": {
    "FilingCabinet": [
      {
        "FileHashID": "cd9b739b7c6e488080412e9a831e9260a468564f",
        "FileName": "file.txt",
        "FileAddedDatetime": "05/10/2020 15:58:41",
        "UploadedFrom": 1,
        "UploadedBy": "Integration Lab",
        "ExtractingStatus": 999,
        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)"
      },
      {
        "FileHashID": "2a99370fd6218b6b8e0c3413f11eb504a4a60225",
        "FileName": "openioc1",
        "FileAddedDatetime": "05/10/2020 12:28:18",
        "UploadedFrom": 1,
        "UploadedBy": "Integration Lab",
        "ExtractingStatus": 1,
        "ShortDesc": "SHELLDC.DLL (BACKDOOR)"
      },
      {
        "FileHashID": "fc3f17bd9068c2588c4c475d2d08a0e7f04f434d",
        "FileName": "cryptolocker2.ioc",
        "FileAddedDatetime": "05/10/2020 10:39:17",
        "UploadedFrom": 1,
        "UploadedBy": "Integration Lab",
        "ExtractingStatus": 1,
        "ShortDesc": "Cryptolocker Detection (EXPERIMENTAL)"
      }
    ],
    "TotalIOCCount": 3
  },
  "Meta": {
    "Result": 1,
    "ErrorCode": 0
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}
```

#### Delete OpenIOC File

This action deletes existing OpenIOC files from the Apex Central server.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_hash_id_list|[]string|None|True|The list of file SHA-1 values|None|["695cad3121a1f496cff0e35d51ba25e33cf266650626b4c1d035a72d2f801343"]|

Example input:

```
{
  "file_hash_id_list": "[\"695cad3121a1f496cff0e35d51ba25e33cf266650626b4c1d035a72d2f801343\"]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|[]delete_data|False|Contains the data returned by the specific API|
|FeatureCtrl|FeatureCtrl|False|The Apex Central deployment model|
|Meta|Meta|False|Indicates the response status, including the result, error code, and error message|
|PermissionCtrl|PermissionCtrl|False|Indicates the permissions assigned to the logged-on user account for accessing Apex Central menu items and features|
|SystemCtrl|SystemCtrl|False|Indicates the suspicious object distribution role of the Apex Central server|

Example output:

```
{
  "Data": [
    {
      "DeletedStatus": 1,
      "FileHashID": "769fcc7550bf98d96bccb7e22a5557301c403455"
    }
  ],
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "ErrorCode": 0,
    "Result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}
```

#### Download OpenIOC File

This action is used to download OpenIOC files from the Apex Central server.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_hash_id|string|None|True|The file hash ID of the file to download|None|769fcc7550bf98d96bccb7e22a5557301c403455|

Example input:

```
{
  "file_hash_id": "769fcc7550bf98d96bccb7e22a5557301c403455"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|file|True|OpenIOC file|
|FeatureCtrl|FeatureCtrl|False|The Apex Central deployment model|
|Meta|Meta|False|Indicates the response status, including the result, error code, and error message|
|PermissionCtrl|PermissionCtrl|False|Indicates the permissions assigned to the logged-on user account for accessing Apex Central menu items and features|
|SystemCtrl|SystemCtrl|False|Indicates the suspicious object distribution role of the Apex Central server|

Example output:

```
{
  "Data": {
    "FileName": "file.txt",
    "FileContentBase64": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXMtYXNjaWkiPz4KPGlvYyB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIiB4bWxuczp4c2Q9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hIiBpZD0iYTEzZTI4MmQtNjVlMS00MjYzLTliMzEtNWY5MTI1MTUyODhjIiBsYXN0LW1vZGlmaWVkPSIyMDEzLTEwLTMwVDE5OjA3OjQ2IiB4bWxucz0iaHR0cDovL3NjaGVtYXMubWFuZGlhbnQuY29tLzIwMTAvaW9jIj4KICA8c2hvcnRfZGVzY3JpcHRpb24+Q3J5cHRvbG9ja2VyIERldGVjdGlvbiAoRVhQRVJJTUVOVEFMKTwvc2hvcnRfZGVzY3JpcHRpb24+CiAgPGRlc2NyaXB0aW9uPlRoaXMgSU9DIGRldGVjdHMgcmVnaXN0cnkgZW50cmllcyBjcmVhdGVkIHdoZW4gdGhlIENyeXB0b2xvY2tlciBjcmltZXdhcmUgcnVucy4gUHJlc2VuY2Ugb2Ygb25lIG9mIHRoZXNlIHJlZ2lzdHJ5IGtleSBzaG93cyB0aGF0IGEgYm94IGhhcyBsaWtlbHkgYmVlbiBpbmZlY3RlZCB3aXRoIHRoZSBDcnlwdG9sb2NrZXIgc29mdHdhcmUuPC9kZXNjcmlwdGlvbj4KICA8YXV0aG9yZWRfYnk+TWFuZGlhbnQ8L2F1dGhvcmVkX2J5PgogIDxhdXRob3JlZF9kYXRlPjIwMTMtMTAtMjhUMTQ6Mjc6MTI8L2F1dGhvcmVkX2RhdGU+CiAgPGxpbmtzPgogICAgPGxpbmsgcmVsPSJncmFkZSI+dW50ZXN0ZWQ8L2xpbms+CiAgPC9saW5rcz4KICA8ZGVmaW5pdGlvbj4KICAgIDxJbmRpY2F0b3Igb3BlcmF0b3I9Ik9SIiBpZD0iN2VhNjA1YjctOGFiMS00ZTFjLTkxMjgtOTk5MjY1Y2Q5ZjIxIj4KICAgICAgPEluZGljYXRvckl0ZW0gaWQ9ImE3MWViMGQ3LWFmZTUtNDcwOC04ZGJiLTM3OWJkNDNjYzlkNyIgY29uZGl0aW9uPSJjb250YWlucyI+CiAgICAgICAgPENvbnRleHQgZG9jdW1lbnQ9IlJlZ2lzdHJ5SXRlbSIgc2VhcmNoPSJSZWdpc3RyeUl0ZW0vUGF0aCIgdHlwZT0ibWlyIiAvPgogICAgICAgIDxDb250ZW50IHR5cGU9InN0cmluZyI+U29mdHdhcmVcQ3J5cHRvTG9ja2VyXEZpbGVzPC9Db250ZW50PgogICAgICA8L0luZGljYXRvckl0ZW0+CiAgICAgIDxJbmRpY2F0b3Igb3BlcmF0b3I9IkFORCIgaWQ9ImJmYmVmOGEyLTdmMTktNDAwZC04Yjg5LTg3ZjdjNzYwNzhhZSI+CiAgICAgICAgPEluZGljYXRvckl0ZW0gaWQ9IjQyZTk2OTk4LTcxNjEtNGYyMi1iYjc3LTczNjYwZTI2OWE2YiIgY29uZGl0aW9uPSJjb250YWlucyI+CiAgICAgICAgICA8Q29udGV4dCBkb2N1bWVudD0iUmVnaXN0cnlJdGVtIiBzZWFyY2g9IlJlZ2lzdHJ5SXRlbS9QYXRoIiB0eXBlPSJtaXIiIC8+CiAgICAgICAgICA8Q29udGVudCB0eXBlPSJzdHJpbmciPkN1cnJlbnRWZXJzaW9uXFJ1bjwvQ29udGVudD4KICAgICAgICA8L0luZGljYXRvckl0ZW0+CiAgICAgICAgPEluZGljYXRvckl0ZW0gaWQ9IjVkNWI4Mjk2LTAxYzktNDE0Ni05YTc0LWFiYTUzMWM1NzQ3OSIgY29uZGl0aW9uPSJjb250YWlucyI+CiAgICAgICAgICA8Q29udGV4dCBkb2N1bWVudD0iUmVnaXN0cnlJdGVtIiBzZWFyY2g9IlJlZ2lzdHJ5SXRlbS9QYXRoIiB0eXBlPSJtaXIiIC8+CiAgICAgICAgICA8Q29udGVudCB0eXBlPSJzdHJpbmciPkNyeXB0b2xvY2tlcjwvQ29udGVudD4KICAgICAgICA8L0luZGljYXRvckl0ZW0+CiAgICAgIDwvSW5kaWNhdG9yPgogICAgPC9JbmRpY2F0b3I+CiAgPC9kZWZpbml0aW9uPgo8L2lvYz4="
  },
  "Meta": {
    "Result": 1,
    "ErrorCode": 0
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}
```

#### Upload OpenIOC File

This action uploads OpenIOC files to the Apex Central server.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|files|[]file|None|True|Files to upload|None|[{"filename": "file.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}]|

Example input:

```
{
  "files": "[{\"filename\": \"file.txt\", \"content\": \"UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==\"}]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|FeatureCtrl|FeatureCtrl|False|The Apex Central deployment model|
|Meta|Meta|False|Indicates the response status, including the result, error code, and error message|
|PermissionCtrl|PermissionCtrl|False|Indicates the permissions assigned to the logged-on user account for accessing Apex Central menu items and features|
|SystemCtrl|SystemCtrl|False|Indicates the suspicious object distribution role of the Apex Central server|
|uploaded_info_list|[]uploaded_info_list|False|Uploaded Result Info List|
|uploaded_message_list|[]uploaded_message_list|False|Uploaded Result Message List|

Example output:

```
{
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "ErrorCode": 0,
    "Result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  },
  "uploaded_info_list": [
    {
      "FileHashID": "cd9b739b7c6e488080412e9a831e9260a468564f",
      "FileName": "file.txt",
      "UploadedStatus": 1
    }
  ],
  "uploaded_message_list": [
    {
      "Message": "Uploaded 1 OpenIOC file(s) successfully.",
      "MessageType": 1
    }
  ]
}
```

#### Download the RCA CSV File

This action downloads existing RCA files from the Apex Central server.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_guid|string|None|True|GUID of the target endpoint|None|654B1B52-C3C9-4405-B133-48E2353DA13B|
|host_ip|string|None|True|Host IP address|None|198.51.100.100|
|host_name|string|None|True|Host name|None|CU-PRO1-7814-2|
|scan_summary_guid|string|None|True|GUID of the investigation summary to retrieve|None|58127b3e-1bde-4c6e-8d86-0d0f89ded601|
|server_guid|[]string|None|True|GUID of the target server|None|["2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6"]|
|task_type|string|CMEF|False|Type of API request. For Endpoint Sensor, the value is always 4|['UNKNOWN', 'INTERNAL', 'CM', 'CMEF', 'OSF_COMMAND', 'OSF_QUERY', 'OSF_NOTIFY', 'OSF_LOG', 'MDR_ATTACK_DISCOVERY', 'OSF_SYS_CALL']|CMEF|

Example input:

```
{
  "agent_guid": "654B1B52-C3C9-4405-B133-48E2353DA13B",
  "host_ip": "198.51.100.100",
  "host_name": "CU-PRO1-7814-2",
  "scan_summary_guid": "58127b3e-1bde-4c6e-8d86-0d0f89ded601",
  "server_guid": "[\"2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6\"]",
  "task_type": "CMEF"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|api_response|api_response|False|Contains data returned|

Example output:

```
{
  "api_response": {
    "Data": {
      "Code": 0,
      "CodeType": 1,
      "Message": "OK",
      "Data": {
        "taskId": "21afcb09-05c9-4dfe-9d1e-5751e99e639c",
        "hasMore": false,
        "serverName": "Apex One as a Service",
        "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
        "content": [
          {
            "statusCode": 0,
            "message": "TMSL_S_SUCCESS",
            "content": {
              "csv": "Host Name,TREND-MICRO-TES\nIP Address,10.0.2.15\nChain,Operation Time,Parent,Activity,Object Type,Object Name,Process ID,Command Line,User,Server Name,File Path,SHA1,SHA2,MD5,Signer,Connect To IP,Port,DNS Query,Resolved DNS,Registry Key,Registry Name,Registry Data\n1,05/10/20 1:00:20 -04:00,compattelrunner.exe,creation,process,compattelrunner.exe,11192,C:\\WINDOWS\\system32\\CompatTelRunner.exe -m:appraiser.dll -f:DoScheduledTelemetryRun -cv:lg+7FM07T0yHrx0b.1,SYSTEM,NT AUTHORITY,c:\\windows\\system32\\compattelrunner.exe,9c6a334bac3122876fcfe3e46ce9a08bc60d6c3a,924405fd4df46b0a1d955aa492f441b938f051cc830ab494e88398def701fc1f,1e79615ef9946eb8a28d15584b21db2f,microsoft windows (Invalid),-,-,-,-,-,-,-\n1,05/10/20 1:02:26 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\appxprovider.dll,creation,file,appxprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\appxprovider.dll,caac3efe84f653fbd1e1f27ce6180a5775653f50,b2e72ab88312e701830170ed750becda9d20cd65969f86a1e533ae2074abcb93,302aeac868a4c8045eca8340537a5214,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:25 -04:00,c:\\windows\\system32\\dism\\logprovider.dll,load,file,logprovider.dll,-,-,-,-,c:\\windows\\system32\\dism\\logprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,modify,file,dismcoreps.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,trend-micro-test,query,dns,trend-micro-test,-,-,-,-,-,-,-,-,-,-,-,trend-micro-test,10.0.2.15,-,-,-\n1,05/10/20 1:01:36 -04:00,c:\\windows\\system32\\drivers\\en-us\\kbdhid.sys.mui,access,file,kbdhid.sys.mui,-,-,-,-,c:\\windows\\system32\\drivers\\en-us\\kbdhid.sys.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\folderprovider.dll.mui,delete,file,folderprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\folderprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:17 -04:00,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_pccnt\\common\\pccntmon.exe,access,file,pccntmon.exe,-,-,-,-,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_pccnt\\common\\pccntmon.exe,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:39 -04:00,c:\\windows\\appcompat\\ua\\genericerror.png,creation,file,genericerror.png,-,-,-,-,c:\\windows\\appcompat\\ua\\genericerror.png,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:18 -04:00,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_pccnt\\drv\\x64\\tmwfp.sys,access,file,tmwfp.sys,-,-,-,-,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_pccnt\\drv\\x64\\tmwfp.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:44 -04:00,c:\\windows\\system32\\drivers\\ndfltr.sys,access,file,ndfltr.sys,-,-,-,-,c:\\windows\\system32\\drivers\\ndfltr.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\setupplatformprovider.dll.mui,creation,file,setupplatformprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\setupplatformprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:51 -04:00,c:\\windows\\system32\\drivers\\rasacd.sys,access,file,rasacd.sys,-,-,-,-,c:\\windows\\system32\\drivers\\rasacd.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:25 -04:00,c:\\windows\\system32\\dism\\dismprov.dll,load,file,dismprov.dll,-,-,-,-,c:\\windows\\system32\\dism\\dismprov.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,delete,file,dismcoreps.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:39 -04:00,c:\\windows\\system32\\en-us\\netshell.dll.mui,access,file,netshell.dll.mui,-,-,-,-,c:\\windows\\system32\\en-us\\netshell.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\genericprovider.dll,delete,file,genericprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\genericprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:30 -04:00,c:\\windows\\system32\\devinv.dll,load,file,devinv.dll,-,-,-,-,c:\\windows\\system32\\devinv.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\wimprovider.dll.mui,copy,file,wimprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\wimprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,delete,file,dmiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\unattendprovider.dll.mui,creation,file,unattendprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\unattendprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:06 -04:00,c:\\windows\\system32\\drivers\\urscx01000.sys,access,file,urscx01000.sys,-,-,-,-,c:\\windows\\system32\\drivers\\urscx01000.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:51 -04:00,c:\\windows\\system32\\dismapi.dll,load,file,dismapi.dll,-,-,-,-,c:\\windows\\system32\\dismapi.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\genericprovider.dll.mui,modify,file,genericprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\genericprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismprov.dll,modify,file,dismprov.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismprov.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:30 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\intlprovider.dll,creation,file,intlprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\intlprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:36 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\transmogprovider.dll,delete,file,transmogprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\transmogprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,c:\\windows\\system32\\pnrpnsp.dll,load,file,pnrpnsp.dll,-,-,-,-,c:\\windows\\system32\\pnrpnsp.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:36 -04:00,c:\\windows\\logs\\dism\\dism.log,access,file,dism.log,-,-,-,-,c:\\windows\\logs\\dism\\dism.log,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:41 -04:00,c:\\windows\\system32\\newdev.dll,load,file,newdev.dll,-,-,-,-,c:\\windows\\system32\\newdev.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:36 -04:00,c:\\windows\\logs\\dism\\dism.log,creation,file,dism.log,-,-,-,-,c:\\windows\\logs\\dism\\dism.log,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\offlinesetupprovider.dll.mui,creation,file,offlinesetupprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\offlinesetupprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ffuprovider.dll.mui,copy,file,ffuprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ffuprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\smiprovider.dll.mui,creation,file,smiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\smiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:25 -04:00,c:\\windows\\system32\\dism\\ffuprovider.dll,load,file,ffuprovider.dll,-,-,-,-,c:\\windows\\system32\\dism\\ffuprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:12 -04:00,c:\\windows\\system32\\drivers\\arcsas.sys,access,file,arcsas.sys,-,-,-,-,c:\\windows\\system32\\drivers\\arcsas.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\appxprovider.dll.mui,modify,file,appxprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\appxprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\offlinesetupprovider.dll,delete,file,offlinesetupprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\offlinesetupprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\smiprovider.dll,delete,file,smiprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\smiprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:23 -04:00,c:\\program files (x86)\\trend micro\\iservice\\ivp\\infsys\\vistarelease\\tbimdsa.sys,access,file,tbimdsa.sys,-,-,-,-,c:\\program files (x86)\\trend micro\\iservice\\ivp\\infsys\\vistarelease\\tbimdsa.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:20 -04:00,c:\\program files (x86)\\trend micro\\iservice\\ivp\\ivpagent.exe,access,file,ivpagent.exe,-,-,-,-,c:\\program files (x86)\\trend micro\\iservice\\ivp\\ivpagent.exe,ad5c9d9b85f83bc3ad075b61248367c05eb5774d,6928a1a89db5a0aa5b796c064386b9106cbb318c3c5435d7329f577dcd7caf44,db5ddc230e5cd8d8b032c3c80ee21d54,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:44 -04:00,c:\\windows\\system32\\drivers\\en-us\\nwifi.sys.mui,access,file,nwifi.sys.mui,-,-,-,-,c:\\windows\\system32\\drivers\\en-us\\nwifi.sys.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:03 -04:00,c:\\windows\\system32\\drivers\\ucmtcpcicx.sys,access,file,ucmtcpcicx.sys,-,-,-,-,c:\\windows\\system32\\drivers\\ucmtcpcicx.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,c:\\windows\\system32\\ktmw32.dll,load,file,ktmw32.dll,-,-,-,-,c:\\windows\\system32\\ktmw32.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:21 -04:00,c:\\windows\\system32\\windows.security.authentication.onlineid.dll,load,file,windows.security.authentication.onlineid.dll,-,-,-,-,c:\\windows\\system32\\windows.security.authentication.onlineid.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ibsprovider.dll.mui,delete,file,ibsprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ibsprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,c:\\windows\\system32\\wshbth.dll,load,file,wshbth.dll,-,-,-,-,c:\\windows\\system32\\wshbth.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:33 -04:00,c:\\windows\\system32\\updatepolicy.dll,load,file,updatepolicy.dll,-,-,-,-,c:\\windows\\system32\\updatepolicy.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:31 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\wimprovider.dll,copy,file,wimprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\wimprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:58 -04:00,c:\\program files (x86)\\trend micro\\officescan client\\amsi\\tmamsiprovider64.dll,load,file,tmamsiprovider64.dll,-,-,-,-,c:\\program files (x86)\\trend micro\\officescan client\\amsi\\tmamsiprovider64.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:21 -04:00,c:\\windows\\system32\\dusmapi.dll,load,file,dusmapi.dll,-,-,-,-,c:\\windows\\system32\\dusmapi.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:24 -04:00,c:\\windows\\system32\\dismapi.dll,access,file,dismapi.dll,-,-,-,-,c:\\windows\\system32\\dismapi.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcore.dll,copy,file,dismcore.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcore.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:33 -04:00,settings-win.data.microsoft.com,query,dns,settings-win.data.microsoft.com,-,-,-,-,-,-,-,-,-,-,-,settings-win.data.microsoft.com,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ffuprovider.dll.mui,delete,file,ffuprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ffuprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\intlprovider.dll.mui,copy,file,intlprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\intlprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\logprovider.dll.mui,creation,file,logprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\logprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,copy,file,dismcoreps.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dismcoreps.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\folderprovider.dll.mui,copy,file,folderprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\folderprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\smiprovider.dll.mui,copy,file,smiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\smiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,modify,file,dmiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:57 -04:00,c:\\windows\\system32\\drivers\\smartsamd.sys,access,file,smartsamd.sys,-,-,-,-,c:\\windows\\system32\\drivers\\smartsamd.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\genericprovider.dll,creation,file,genericprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\genericprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:31 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\wimprovider.dll,creation,file,wimprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\wimprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:30 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\intlprovider.dll,copy,file,intlprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\intlprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:27 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,copy,file,dmiprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\dmiprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:27 -04:00,c:\\windows\\system32\\wuapi.dll,load,file,wuapi.dll,-,-,-,-,c:\\windows\\system32\\wuapi.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:42 -04:00,c:\\windows\\system32\\drivers\\mslldp.sys,access,file,mslldp.sys,-,-,-,-,c:\\windows\\system32\\drivers\\mslldp.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:35 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dmiprovider.dll,delete,file,dmiprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\dmiprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:17 -04:00,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_admin\\tmuninst.exe,access,file,tmuninst.exe,-,-,-,-,c:\\program files (x86)\\trend micro\\officescan client\\activeupdate\\officescan\\hotfix_admin\\tmuninst.exe,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\ibsprovider.dll,copy,file,ibsprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\ibsprovider.dll,dbbeb426cedb8ee7d402cff66fb859eedde93182,c88ad6c3919519468b3694cbf2d90a40df7eaaa10210854cf546598a104d2526,280d67aa4d95a9f517129db2173ba5cc,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:28 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ibsprovider.dll.mui,copy,file,ibsprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\ibsprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:29 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\unattendprovider.dll.mui,modify,file,unattendprovider.dll.mui,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\en-us\\unattendprovider.dll.mui,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:21 -04:00,c:\\windows\\winsxs\\amd64_microsoft.windows.gdiplus_6595b64144ccf1df_1.1.18362.778_none_17b1aa466d9fc986\\gdiplus.dll,load,file,gdiplus.dll,-,-,-,-,c:\\windows\\winsxs\\amd64_microsoft.windows.gdiplus_6595b64144ccf1df_1.1.18362.778_none_17b1aa466d9fc986\\gdiplus.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:26 -04:00,c:\\windows\\system32\\generaltel.dll,load,file,generaltel.dll,-,-,-,-,c:\\windows\\system32\\generaltel.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:41 -04:00,c:\\windows\\system32\\drvstore.dll,load,file,drvstore.dll,-,-,-,-,c:\\windows\\system32\\drvstore.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:20 -04:00,c:\\windows\\system32\\appraiser.dll,load,file,appraiser.dll,-,-,-,-,c:\\windows\\system32\\appraiser.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:59 -04:00,c:\\windows\\system32\\drivers\\storufs.sys,access,file,storufs.sys,-,-,-,-,c:\\windows\\system32\\drivers\\storufs.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:22 -04:00,c:\\windows\\system32\\catroot\\{f750e6c3-38ee-11d1-85e5-00c04fc295ee}\\microsoft-windows-client-features-package00~31bf3856ad364e35~amd64~~10.0.18362.1.cat,access,file,microsoft-windows-client-features-package00~31bf3856ad364e35~amd64~~10.0.18362.1.cat,-,-,-,-,c:\\windows\\system32\\catroot\\{f750e6c3-38ee-11d1-85e5-00c04fc295ee}\\microsoft-windows-client-features-package00~31bf3856ad364e35~amd64~~10.0.18362.1.cat,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:41 -04:00,c:\\windows\\system32\\acmigration.dll,load,file,acmigration.dll,-,-,-,-,c:\\windows\\system32\\acmigration.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:18 -04:00,c:\\windows\\system32\\drivers\\bttflt.sys,access,file,bttflt.sys,-,-,-,-,c:\\windows\\system32\\drivers\\bttflt.sys,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:40 -04:00,c:\\windows\\system32\\napinsp.dll,load,file,napinsp.dll,-,-,-,-,c:\\windows\\system32\\napinsp.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:02:31 -04:00,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\transmogprovider.dll,modify,file,transmogprovider.dll,-,-,-,-,c:\\windows\\temp\\91ea94ff-057a-4e9f-889c-1a3739b23f4f\\transmogprovider.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:19 -04:00,svchost.exe,creation,process,compattelrunner.exe,7304,C:\\WINDOWS\\system32\\compattelrunner.exe,SYSTEM,NT AUTHORITY,c:\\windows\\system32\\compattelrunner.exe,9c6a334bac3122876fcfe3e46ce9a08bc60d6c3a,924405fd4df46b0a1d955aa492f441b938f051cc830ab494e88398def701fc1f,1e79615ef9946eb8a28d15584b21db2f,microsoft windows (Invalid),-,-,-,-,-,-,-\n1,05/10/20 1:00:19 -04:00,c:\\windows\\system32\\compattelrunner.exe,load,file,compattelrunner.exe,-,-,-,-,c:\\windows\\system32\\compattelrunner.exe,9c6a334bac3122876fcfe3e46ce9a08bc60d6c3a,924405fd4df46b0a1d955aa492f441b938f051cc830ab494e88398def701fc1f,1e79615ef9946eb8a28d15584b21db2f,-,-,-,-,-,-,-,-\n1,05/10/20 1:03:45 -04:00,c:\\windows\\system32\\compattelrunner.exe,access,file,compattelrunner.exe,-,-,-,-,c:\\windows\\system32\\compattelrunner.exe,9c6a334bac3122876fcfe3e46ce9a08bc60d6c3a,924405fd4df46b0a1d955aa492f441b938f051cc830ab494e88398def701fc1f,1e79615ef9946eb8a28d15584b21db2f,-,-,-,-,-,-,-,-\n1,05/09/20 17:21:32 -04:00,services.exe,creation,process,svchost.exe,1296,C:\\WINDOWS\\system32\\svchost.exe -k netsvcs -p -s Schedule,SYSTEM,NT AUTHORITY,c:\\windows\\system32\\svchost.exe,75c5a97f521f760e32a4a9639a653eed862e9c61,dd191a5b23df92e12a8852291f9fb5ed594b76a28a5a464418442584afd1e048,9520a99e77d6196d0d09833146424113,microsoft windows publisher (Invalid),-,-,-,-,-,-,-\n1,05/09/20 20:51:19 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,creation,file,ac power install,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:04 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,delete,file,ac power install,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:28 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,creation,file,ac power download,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 23:14:36 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\.net framework\\.net framework ngen v4.0.30319 64 critical,creation,file,.net framework ngen v4.0.30319 64 critical,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\.net framework\\.net framework ngen v4.0.30319 64 critical,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 23:13:52 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\.net framework\\.net framework ngen v4.0.30319 critical,creation,file,.net framework ngen v4.0.30319 critical,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\.net framework\\.net framework ngen v4.0.30319 critical,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:28 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\backup scan,creation,file,backup scan,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\backup scan,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:59:14 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\universal orchestrator start,delete,file,universal orchestrator start,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\universal orchestrator start,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:51:19 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,modify,file,ac power install,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power install,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:28 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,modify,file,ac power download,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:29 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,delete,file,ac power download,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\ac power download,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:17 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\softwareprotectionplatform\\svcrestarttask,creation,file,svcrestarttask,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\softwareprotectionplatform\\svcrestarttask,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 22:41:48 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\flighting\\onesettings\\refreshcache,creation,file,refreshcache,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\flighting\\onesettings\\refreshcache,-,-,-,-,-,-,-,-,-,-,-\n1,05/09/20 20:53:06 -04:00,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\schedule scan,creation,file,schedule scan,-,-,-,-,c:\\windows\\system32\\tasks\\microsoft\\windows\\updateorchestrator\\schedule scan,-,-,-,-,-,-,-,-,-,-,-\n1,01/01/70 0:00:00 -05:00,-,creation,process,services.exe,656,-,-,-,c:\\windows\\system32\\services.exe,86662690d627002d7cab3285f7be3e6d87b35cfb,9090e0e44e14709fb09b23b98572e0e61c810189e2de8f7156021bc81c3b1bb6,bccc12eb2ef644e662a63a023fb83f9b,microsoft windows publisher (Invalid),-,-,-,-,-,-,-\n1,05/10/20 2:22:10 -04:00,c:\\windows\\security\\database\\edb.chk,creation,file,edb.chk,-,-,-,-,c:\\windows\\security\\database\\edb.chk,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:00 -04:00,c:\\windows\\inf\\ucmucsiacpiclient.pnf,creation,file,ucmucsiacpiclient.pnf,-,-,-,-,c:\\windows\\inf\\ucmucsiacpiclient.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\iai2c.pnf,creation,file,iai2c.pnf,-,-,-,-,c:\\windows\\inf\\iai2c.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:52 -04:00,c:\\windows\\inf\\bcmfn2.pnf,creation,file,bcmfn2.pnf,-,-,-,-,c:\\windows\\inf\\bcmfn2.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:57 -04:00,c:\\windows\\inf\\msgpiowin32.pnf,creation,file,msgpiowin32.pnf,-,-,-,-,c:\\windows\\inf\\msgpiowin32.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\ialpss2i_i2c_bxt_p.pnf,creation,file,ialpss2i_i2c_bxt_p.pnf,-,-,-,-,c:\\windows\\inf\\ialpss2i_i2c_bxt_p.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\wgencounter.pnf,creation,file,wgencounter.pnf,-,-,-,-,c:\\windows\\inf\\wgencounter.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\ialpss2i_gpio2_bxt_p.pnf,creation,file,ialpss2i_gpio2_bxt_p.pnf,-,-,-,-,c:\\windows\\inf\\ialpss2i_gpio2_bxt_p.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:59 -04:00,c:\\windows\\inf\\sbp2.pnf,creation,file,sbp2.pnf,-,-,-,-,c:\\windows\\inf\\sbp2.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidinterrupt.pnf,creation,file,hidinterrupt.pnf,-,-,-,-,c:\\windows\\inf\\hidinterrupt.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\mdmbtmdm.pnf,creation,file,mdmbtmdm.pnf,-,-,-,-,c:\\windows\\inf\\mdmbtmdm.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\ialpss2i_gpio2_glk.pnf,creation,file,ialpss2i_gpio2_glk.pnf,-,-,-,-,c:\\windows\\inf\\ialpss2i_gpio2_glk.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:00 -04:00,c:\\windows\\inf\\umpass.pnf,creation,file,umpass.pnf,-,-,-,-,c:\\windows\\inf\\umpass.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\microsoft_bluetooth_hfp.pnf,creation,file,microsoft_bluetooth_hfp.pnf,-,-,-,-,c:\\windows\\inf\\microsoft_bluetooth_hfp.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:58 -04:00,c:\\windows\\inf\\mtconfig.pnf,creation,file,mtconfig.pnf,-,-,-,-,c:\\windows\\inf\\mtconfig.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:54 -04:00,c:\\windows\\inf\\circlass.pnf,creation,file,circlass.pnf,-,-,-,-,c:\\windows\\inf\\circlass.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidi2c.pnf,creation,file,hidi2c.pnf,-,-,-,-,c:\\windows\\inf\\hidi2c.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:22:10 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\acdriver\"\", \"\"imagepath\"\", \"\"system32\\\\DRIVERS\\\\AcDriver.sys\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\acdriver,imagepath,system32\\DRIVERS\\AcDriver.sys\n1,05/10/20 2:22:11 -04:00,c:\\windows\\security\\database\\edb.log,creation,file,edb.log,-,-,-,-,c:\\windows\\security\\database\\edb.log,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:00 -04:00,c:\\windows\\inf\\wdma_usb.pnf,creation,file,wdma_usb.pnf,-,-,-,-,c:\\windows\\inf\\wdma_usb.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:57 -04:00,c:\\windows\\inf\\intelpmax.pnf,creation,file,intelpmax.pnf,-,-,-,-,c:\\windows\\inf\\intelpmax.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:02 -04:00,c:\\windows\\inf\\wmiacpi.pnf,creation,file,wmiacpi.pnf,-,-,-,-,c:\\windows\\inf\\wmiacpi.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidbth.pnf,creation,file,hidbth.pnf,-,-,-,-,c:\\windows\\inf\\hidbth.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\ialpss2i_i2c_skl.pnf,creation,file,ialpss2i_i2c_skl.pnf,-,-,-,-,c:\\windows\\inf\\ialpss2i_i2c_skl.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:01 -04:00,c:\\windows\\inf\\usbcir.pnf,creation,file,usbcir.pnf,-,-,-,-,c:\\windows\\inf\\usbcir.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:58 -04:00,c:\\windows\\inf\\ksfilter.pnf,creation,file,ksfilter.pnf,-,-,-,-,c:\\windows\\inf\\ksfilter.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:59 -04:00,c:\\windows\\inf\\tpm.pnf,creation,file,tpm.pnf,-,-,-,-,c:\\windows\\inf\\tpm.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidspi_km.pnf,creation,file,hidspi_km.pnf,-,-,-,-,c:\\windows\\inf\\hidspi_km.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:01 -04:00,c:\\windows\\inf\\hidvhf.pnf,creation,file,hidvhf.pnf,-,-,-,-,c:\\windows\\inf\\hidvhf.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:22:11 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\tmiacagentsvc\"\", \"\"imagepath\"\", \"\"\\\"\"C:\\\\Program Files (x86)\\\\Trend Micro\\\\iService\\\\iAC\\\\ac_bin\\\\TMiACAgentSvc.exe\\\"\" --mode SVC --sc --l DEBUG\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\tmiacagentsvc,imagepath,\"\"C:\\Program Files (x86)\\Trend Micro\\iService\\iAC\\ac_bin\\TMiACAgentSvc.exe\"\" --mode SVC --sc --l DEBUG\n1,05/10/20 1:00:58 -04:00,c:\\windows\\inf\\memory.pnf,creation,file,memory.pnf,-,-,-,-,c:\\windows\\inf\\memory.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:52 -04:00,c:\\windows\\inf\\amdgpio2.pnf,creation,file,amdgpio2.pnf,-,-,-,-,c:\\windows\\inf\\amdgpio2.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:55 -04:00,c:\\windows\\inf\\hidbatt.pnf,creation,file,hidbatt.pnf,-,-,-,-,c:\\windows\\inf\\hidbatt.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\bth.pnf,creation,file,bth.pnf,-,-,-,-,c:\\windows\\inf\\bth.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:01:00 -04:00,c:\\windows\\inf\\urssynopsys.pnf,creation,file,urssynopsys.pnf,-,-,-,-,c:\\windows\\inf\\urssynopsys.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:56 -04:00,c:\\windows\\inf\\iastorv.pnf,creation,file,iastorv.pnf,-,-,-,-,c:\\windows\\inf\\iastorv.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\virtdisk.pnf,creation,file,virtdisk.pnf,-,-,-,-,c:\\windows\\inf\\virtdisk.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:54 -04:00,c:\\windows\\inf\\netevbda.pnf,creation,file,netevbda.pnf,-,-,-,-,c:\\windows\\inf\\netevbda.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:59 -04:00,c:\\windows\\inf\\stornvme.pnf,creation,file,stornvme.pnf,-,-,-,-,c:\\windows\\inf\\stornvme.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\buttonconverter.pnf,creation,file,buttonconverter.pnf,-,-,-,-,c:\\windows\\inf\\buttonconverter.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:22:11 -04:00,c:\\windows\\security\\database\\secedit.sdb,creation,file,secedit.sdb,-,-,-,-,c:\\windows\\security\\database\\secedit.sdb,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 1:00:53 -04:00,c:\\windows\\inf\\chargearbitration.pnf,creation,file,chargearbitration.pnf,-,-,-,-,c:\\windows\\inf\\chargearbitration.pnf,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:22:10 -04:00,c:\\windows\\system32\\esent.dll,load,file,esent.dll,-,-,-,-,c:\\windows\\system32\\esent.dll,-,-,-,-,-,-,-,-,-,-,-\n1,05/10/20 2:21:47 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\dsasvc\"\", \"\"imagepath\"\", \"\"%SystemRoot%\\\\system32\\\\dgagent\\\\DSAGENT.exe\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\dsasvc,imagepath,%SystemRoot%\\system32\\dgagent\\DSAGENT.exe\n1,05/10/20 2:21:47 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\sakfile\"\", \"\"imagepath\"\", \"\"system32\\\\drivers\\\\sakfile.sys\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\sakfile,imagepath,system32\\drivers\\sakfile.sys\n1,05/10/20 2:22:11 -04:00,\"[\"\"hklm\\\\system\\\\currentcontrolset\\\\services\\\\acdriverhelper\"\", \"\"imagepath\"\", \"\"\\\\SystemRoot\\\\system32\\\\DRIVERS\\\\AcDriverHelper.sys\"\", true]\",modify,registry,imagepath,-,-,-,-,-,-,-,-,-,-,-,-,-,hklm\\system\\currentcontrolset\\services\\acdriverhelper,imagepath,\\SystemRoot\\system32\\DRIVERS\\AcDriverHelper.sys"
            }
          }
        ]
      },
      "TimeZone": -4
    },
    "Meta": {
      "result": 1,
      "errorCode": 0,
      "errorMessgae": "Success"
    },
    "PermissionCtrl": {
      "permission": "255"
    },
    "FeatureCtrl": {
      "mode": "0"
    },
    "SystemCtrl": {
      "TmcmSoDist_Role": "none"
    }
  }
}
```

#### Terminate Process

This action terminates the processes specified on Security Agent endpoints.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_guid|object|None|False|The key is the serverGuid, and the value is a list of agentGuid strings of the endpoints managed by the target server|None|{"2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6": ["B7F34FF9-9DEE-45F4-9F24-DC5116C79D52"]}|
|filter|[]filter|None|False|The filter paramter is useful for terminating the amount of agents without specifying the agentGuid|None|[{"type": 1, "value": "a"}]|
|server_guid|[]string|None|False|GUID of servers which manage the endpoints specified in agentGuid|None|["2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6"]|
|suspicious_object_name|string|None|False|File name of the object to terminate|None|file.txt|
|termination_info_list|[]termination_info|None|True|Container for terminationInfoList objects|None|[{"name": 101, "value": "2FF40C5ED6E5A3BBC68A10F2966F347463E326AD"}]|

Example input:

```
{
  "agent_guid": "{\"2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6\": [\"B7F34FF9-9DEE-45F4-9F24-DC5116C79D52\"]}",
  "filter": "[{\"type\": 1, \"value\": \"a\"}]",
  "server_guid": "[\"2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6\"]",
  "suspicious_object_name": "file.txt",
  "termination_info_list": "[{\"name\": 101, \"value\": \"2FF40C5ED6E5A3BBC68A10F2966F347463E326AD\"}]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|termination_api_data|True|Contains the data returned by the specific API|

Example output:

```
{
  "Data": {
    "Code": 0,
    "CodeType": 1,
    "Data": {
      "content": [
        {
          "content": {
            "agentGuid": [
              "626dcf14-b0c3-4b00-bc76-71cf5713ab2e"
            ],
            "processTerminationSummaryGuid": "5f7bef38-6603-4edc-b285-837feb136da5",
            "status": 3
          },
          "message": "TMSL_S_SUCCESS",
          "statusCode": 0
        }
      ],
      "hasMore": false,
      "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
      "serverName": "Apex One as a Service",
      "taskId": "5f7bef38-6603-4edc-b285-837feb136da5"
    },
    "Message": "OK",
    "TimeZone": -4
  },
  "FeatureCtrl": {
    "mode": "0"
  },
  "Meta": {
    "errorCode": 0,
    "errorMessgae": "Success",
    "result": 1
  },
  "PermissionCtrl": {
    "permission": "255"
  },
  "SystemCtrl": {
    "TmcmSoDist_Role": "none"
  }
}
```

#### Add to UDSO List

This action is used to add an IP address, email or similar info to the UDSO list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|content|string|None|True|The item to be filed as suspicious. data_type affects character limit.  URL/DOMAIN are 2046 characters max, SHA is 40 characters max|None|http://www.example.com|
|data_type|string|URL|True|Format of the data, character length of content is affected by this|['IP', 'URL', 'FILE_SHA1', 'DOMAIN']|URL|
|expiry_date|int|30|False|Number of days to allow this rule to be active|None|100|
|notes|string|None|False|Notes about why the file is being quarantined (256 characters max)|None|This URL leads to malware|
|scan_action|string|LOG|True|What action to do with the data sent|['BLOCK', 'LOG']|LOG|

Example input:

```
{
  "content": "http://www.example.com",
  "data_type": "URL",
  "expiry_date": 100,
  "notes": "This URL leads to malware",
  "scan_action": "LOG"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the action was successful|

Example output:

```
{
  "success": true
}
```

#### Add File to UDSO List

This action is used to add a file to the UDSO list of the Apex Security Manager.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|file|None|True|File to be marked as suspicious|None|{"filename": "setup.exe", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}|
|notes|string|None|False|Notes about why the file is being quarantined (256 characters max)|None|This file is malware|
|scan_action|string|LOG|True|What action to do with the data sent|['BLOCK', 'LOG', 'QUARANTINE']|QUARANTINE|

Example input:

```
{
  "file": "{\"filename\": \"setup.exe\", \"content\": \"UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==\"}",
  "notes": "This file is malware",
  "scan_action": "QUARANTINE"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the action was successful|

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

* 1.1.0 - New actions Get Agent Status, Search Agents, List OpenIOC Files, Download the RCA CSV File, Upload OpenIOC File, Delete OpenIOC File, Download OpenIOC File, Get Investigation, Terminate Process, Execute Agent Action
* 1.0.0 - Initial plugin

# Links

## References

* [Trend Micro Apex](https://www.trendmicro.com/en_ca/business/products/user-protection/sps/endpoint.html)
* [Apex API](https://beta-community-trendmicro.cs23.force.com/automationcenter/apex-central/api)
