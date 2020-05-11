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
|skip_address_ips|[]string|None|False|Skip address IPs on isolate and uninstall actions|None|["198.51.100.100", "198.51.100.101"]|
|skip_entity_ids|[]string|None|False|Skip entity ids on isolate and uninstall actions|None|["2EBEC86D-3FEB-4666-9CA6-B80AB1E193E6"]|
|skip_host_names|[]string|None|False|Skip host names on isolate and uninstall actions|None|["CU-PRO1-7814-2"]|
|skip_mac_addresses|[]string|None|False|Skip MAC addresses on isolate and uninstall actions|None|["08:00:27:8d:c0:4d"]|
|url|string|None|True|URL with port number of the Apex Security Manager.|None|https://host.example.com:443|

Example input:

```
{
  "api_key": {
      "secretKey": "CU1874A2-G782-47X1-B6J3-1014A92624BC"
  },
  "application_id": {
      "secretKey": "909D88H7-3458-42RN-92FF-012V3CU3D294"
  },
  "url": "https://host.example.com:443"
}
```

## Technical Details

### Actions

#### Get Investigation

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

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result_code|integer|False|The Apex Central Automation API result code|
|result_content|[]result_content|False|The Apex Central Automation API result content|
|result_description|string|False|The Apex Central Automation API result description|

Example output:

```
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
```

#### Delete OpenIOC File

This action deletes existing OpenIOC files from the Apex Central server.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_hash_id_list|[]string|None|True|The list of file SHA-1 values|None|["695cad3121a1f496cff0e35d51ba25e33cf266650626b4c1d035a72d2f801343"]|

Example input:

```
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
```

#### Download OpenIOC File

This action is used to download OpenIOC files to the Apex Central server.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_hash_id|string|None|True|The file hash ID of the file to download|None|769fcc7550bf98d96bccb7e22a5557301c403455|

Example input:

```
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
```

#### Upload OpenIOC File

This action uploads OpenIOC files to the Apex Central server.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|files|[]file|None|True|Files to upload|None|[{"filename": "file.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}]|

Example input:

```
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
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|api_response|api_response|False|Contains data returned|

Example output:

```
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
|task_type|string|CMEF|False|Type of API request. For Endpoint Sensor, the value is always 4|['UNKNOWN', 'INTERNAL', 'CM', 'CMEF', 'OSF_COMMAND', 'OSF_QUERY', 'OSF_NOTIFY', 'OSF_LOG', 'MDR_ATTACK_DISCOVERY', 'OSF_SYS_CALL']|CMEF|
|termination_info_list|[]termination_info|None|True|Container for terminationInfoList objects|None|[{"name": 101, "value": "2FF40C5ED6E5A3BBC68A10F2966F347463E326AD"}]|

Example input:

```
{
  "agent_guid": {
    "C22E1795-BF95-45BB-BC82-486B0F5161BE": [
      "626dcf14-b0c3-4b00-bc76-71cf5713ab2e"
    ]
  },
  "server_guid": [
    "C22E1795-BF95-45BB-BC82-486B0F5161BE"
  ],
  "suspicious_object_name": "BalabolkaPortable_2.15.0.741.paf.exe",
  "termination_info_list": [
    {
      "name": 101,
      "value": "6646ED5128898E4B3ECB9691CEECD62CA4E078EC"
    }
  ]
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

#### List Security Agents

This action retrieves a list of all Security Agents with the Endpoint Sensor feature enabled.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|[]filter|None|False|Filter|None|[{"type": 1, "value": "a"}]|
|pagination|meta_page|None|False|Pagination|None|{"offset": 0, "limit": 50}|
|task_type|string|CMEF|True|Type of API request. For Endpoint Sensor, the value is always 4|['UNKNOWN', 'INTERNAL', 'CM', 'CMEF', 'OSF_COMMAND', 'OSF_QUERY', 'OSF_NOTIFY', 'OSF_LOG', 'MDR_ATTACK_DISCOVERY', 'OSF_SYS_CALL']|CMEF|

Example input:

```
{
  "task_type": "INTERNAL"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|api_data|False|Contains the data returned by the specific API|
|FeatureCtrl|FeatureCtrl|False|The Apex Central deployment model|
|Meta|Meta|False|Indicates the response status, including the result, error code, and error message|
|PermissionCtrl|PermissionCtrl|False|Indicates the permissions assigned to the logged-on user account for accessing Apex Central menu items and features|
|SystemCtrl|SystemCtrl|False|Indicates the suspicious object distribution role of the Apex Central server|

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
            "agentEntity": [
              {
                "agentGuid": "626dcf14-b0c3-4b00-bc76-71cf5713ab2e",
                "ip": "10.0.2.15",
                "isEnable": true,
                "isImportant": false,
                "isOnline": true,
                "isolateStatus": 1,
                "machineGuid": "3E4EC062-A620-4DE6-9DA9-395DD98EC1D8",
                "machineName": "TREND-MICRO-TES",
                "machineOS": "Windows 10",
                "machineType": "Desktop",
                "productType": 15,
                "serverGuid": "C22E1795-BF95-45BB-BC82-486B0F5161BE",
                "userGuid": "6AC1B3DCF-CE52-8279-EE9E-E101FD504E3",
                "userName": "TREND-MICRO-TES\\vagrant"
              }
            ],
            "agentQueryStatus": {
              "hasFullAgents": true,
              "hasFullRbac": true
            },
            "pagination": {
              "limit": 50,
              "offset": 0,
              "total": 1
            }
          },
          "message": "Success",
          "statusCode": 0
        }
      ],
      "hasMore": false
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
  "content": "1.2.3.4"
  "scan_action": "BLOCK",
  "data_type": "IP",
  "expiry_date": 44,
  "notes": "block sesame streets IP address"
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
  "file": {
    "filename": "file.txt",
    "content": "c2xpamJvb20="
  },
  "scan_action": "BLOCK",
  "notes": "This is the most suspicious file I have ever seen"
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

* 1.1.0 - Add actions agent_list, openioc_files_list, download_rca_csv_file, upload_openioc_file, delete_openioc_file, download_openioc_file, get_rca_object, terminate_process, performs_action
* 1.0.0 - Initial plugin

# Links

## References

* [Trend Micro Apex](https://www.trendmicro.com/en_ca/business/products/user-protection/sps/endpoint.html)
* [Apex API](https://beta-community-trendmicro.cs23.force.com/automationcenter/apex-central/api)
