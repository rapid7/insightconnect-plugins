# Description

Stop modern attacks with the industry's first extended detection and response platform that spans your endpoints, network and cloud data

# Key Features

* Get Endpoint Information
* Isolate or Unisolate an endpoint
* Add files to the block or allow lists

# Requirements

* A Palo Alto Cortex XDR API key
* A Palo Alto Cortex XDR API key ID
* The URL to your Palo Alto Cortex XDR API instance

# Supported Product Versions

* 2024-07-15 Palo Alto Cortex XDR API

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|The Cortex XDR API Key that is generated when creating a new key|None|1234123412341234asdfasdfasdfasdfasdf1234123412341234123412341234asdfasdfasdfasdfasdf123412341234123412341234asdfasdfasdfasdfasdf|None|None|
|api_key_id|integer|None|True|The API Key ID shown in the Cortex XDR API Keys table in settings. e.g. 1, 2, 3|None|1|None|None|
|security_level|string|Standard|True|The Security Level of the key provided. This can be found in the API Key settings table in the Cortex XDR settings|["Advanced", "Standard"]|Standard|None|None|
|url|string|None|True|Cortex XDR API URL|None|https://api-example.xdr.us.paloaltonetworks.com/|None|None|

Example input:

```
{
  "api_key": "1234123412341234asdfasdfasdfasdfasdf1234123412341234123412341234asdfasdfasdfasdfasdf123412341234123412341234asdfasdfasdfasdfasdf",
  "api_key_id": 1,
  "security_level": "Standard",
  "url": "https://api-example.xdr.us.paloaltonetworks.com/"
}
```

## Technical Details

### Actions


#### Allow File

This action is used to add a file to the allow list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|File allowed by InsightConnect|True|String that represents additional information regarding the action|None|File allowed by InsightConnect|None|None|
|file_hash|string|None|True|A SHA256 file hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|None|None|
|incident_id|string|None|False|If this is related to an incident, the ID should be entered here|None|5|None|None|
  
Example input:

```
{
  "comment": "File allowed by InsightConnect",
  "file_hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "incident_id": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was the operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Block File

This action is used to add a file to the block list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|File blocked by InsightConnect|True|String that represents additional information regarding the action|None|File blocked by InsightConnect|None|None|
|file_hash|string|None|True|A SHA256 file hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|None|None|
|incident_id|string|None|False|If this is related to an incident, the ID should be entered here|None|5|None|None|
  
Example input:

```
{
  "comment": "File blocked by InsightConnect",
  "file_hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "incident_id": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was the operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Endpoint Details

This action is used to get information about an endpoint

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint|string|None|True|The endpoint to get information about. This can be an IPv4 address, hostname, or endpoint ID|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "endpoint": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpoints|[]endpoint|True|Any endpoints that match the given endpoint information|[ { "Alias": "", "Content Version": {}, "Domain": {}, "Endpoint ID": {}, "Endpoint Name": {}, "Endpoint Status": {}, "Endpoint Type": {}, "Endpoint Version": {}, "First Seen": 0, "IP": [ {} ], "Install Date": {}, "Installation Package": {}, "Is Isolated": {}, "Last Seen": {}, "OS Type": {}, "Operational Status": {}, "Operational Status Description": {}, "Scan Status": {}, "Users": {} } ]|
|total_count|integer|True|Number of results found (max 100)|100|
  
Example output:

```
{
  "endpoints": [
    {
      "Alias": "",
      "Content Version": {},
      "Domain": {},
      "Endpoint ID": {},
      "Endpoint Name": {},
      "Endpoint Status": {},
      "Endpoint Type": {},
      "Endpoint Version": {},
      "First Seen": 0,
      "IP": [
        {}
      ],
      "Install Date": {},
      "Installation Package": {},
      "Is Isolated": {},
      "Last Seen": {},
      "OS Type": {},
      "Operational Status": {},
      "Operational Status Description": {},
      "Scan Status": {},
      "Users": {}
    }
  ],
  "total_count": 100
}
```

#### Get File Quarantine Status

This action is used to get quarantine status for a file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint_id|string|None|True|Endpoint ID|None|example_ID|None|None|
|file_hash|string|None|True|File Hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|None|None|
|file_path|string|None|True|File path|None|powershell.exe|None|None|
  
Example input:

```
{
  "endpoint_id": "example_ID",
  "file_hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "file_path": "powershell.exe"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file_is_quarantined|boolean|True|Check if the provided file is quarantined|True|
  
Example output:

```
{
  "file_is_quarantined": true
}
```

#### Get XQL Query Results

This action is used to start an XQL query and retrieve the query results

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_time|integer|None|False|Integer in timestamp epoch milliseconds for end of the time range, Cortex XDR calls by default the last 24 hours if both 'Start Time' and 'End Time' values are not present|None|1598907600000|None|None|
|limit|integer|20|False|Integer representing the maximum number of results to return, defaults to 20, max value 1000|None|100|None|None|
|query|string|None|True|String of the XQL query|None|dataset=xdr_data I fields event_id, event_type, event_sub_type I limit 3|None|None|
|start_time|integer|None|False|Integer in timestamp epoch milliseconds for start of the time range, Cortex XDR calls by default the last 24 hours if both 'Start Time' and 'End Time' values are not present|None|1599080399000|None|None|
|tenants|[]string|None|True|List of strings used when querying tenants managed by Managed Security Services Providers (MSSP)|None|["tenantID", "tenantID"]|None|None|
  
Example input:

```
{
  "end_time": 1598907600000,
  "limit": 20,
  "query": "dataset=xdr_data I fields event_id, event_type, event_sub_type I limit 3",
  "start_time": 1599080399000,
  "tenants": [
    "tenantID",
    "tenantID"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|reply|False|Object containing the query data results|{"Number of Results": 0, "Query Cost": {}, "Remaining Quota": 0.0, "Results": { "Data": [ {} ], "Event Subtype": {} }, "Status": "" }|
  
Example output:

```
{
  "reply": {
    "Number of Results": 0,
    "Query Cost": {},
    "Remaining Quota": 0.0,
    "Results": {
      "Data": [
        {}
      ],
      "Event Subtype": {}
    },
    "Status": ""
  }
}
```

#### Isolate Endpoint

This action is used to isolate or unisolate an endpoint

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint|string|None|True|Endpoint to isolate or unisolate. This can be an IPv4 address, hostname, or endpoint ID|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|isolation_state|string|Isolate|True|Isolation state to set|["Isolate", "Unisolate"]|Unisolate|None|None|
|whitelist|[]string|[]|False|This list contains a set of devices that should not be blocked. This can be a combination of IPv4 addresses, hostnames, or endpoint IDs|None|["198.51.100.100", "hostname123", "225494730938493804"]|None|None|
  
Example input:

```
{
  "endpoint": "9de5069c5afe602b2ea0a04b66beb2c0",
  "isolation_state": "Isolate",
  "whitelist": []
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|isolation_result|True|The result of the isolation request|{ "Action ID": 0, "Endpoints Count": {}, "Status": "" }|
  
Example output:

```
{
  "result": {
    "Action ID": 0,
    "Endpoints Count": {},
    "Status": ""
  }
}
```
### Triggers


#### Get Alerts

This trigger is used to get alerts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|5|False|Poll frequency in seconds|None|5|None|None|
  
Example input:

```
{
  "frequency": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|object|False|Alert|{"external_id":"12345","severity":"high","matching_status":"UNMATCHABLE","local_insert_ts":1721031230123,"attempt_counter":0,"case_id":1,"is_whitelisted":false,"starred":false,"mitre_technique_id_and_name":["T000.000 - Example Technique: Name"],"mitre_tactic_id_and_name":["ExampleTacticIDName"],"agent_version":"7.5.0.36150","agent_device_domain":"ExampleDomain","agent_fqdn":"ExampleFQDN","agent_os_type":"Windows","agent_os_sub_type":"6","agent_data_collection_status":false,"agent_is_vdi":false,"agent_install_type":"STANDARD","module_id":["Behavioral Threat Protection"],"association_strength":[50],"event_type":["Process Execution"],"event_timestamp":[1721031230123],"actor_process_instance_id":["ExampleID"],"actor_process_image_path":["C:\\Windows\\System32\\cmd.exe"],"actor_process_image_name":["cmd.exe"],"actor_process_command_line":["\"C:\\Windows\\System32\\cmd.exe\" "],"actor_process_signature_status":["N/A"],"actor_process_signature_vendor":["Microsoft Windows","Microsoft Corporation"],"actor_process_image_sha256":["275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"],"actor_process_os_pid":[123],"causality_actor_process_signature_status":["N/A"],"action_country":["UNKNOWN"],"action_process_signature_status":["N/A"],"os_actor_process_signature_status":["N/A"],"fw_is_phishing":["N/A"],"is_pcap":false,"contains_featured_host":["NO"],"contains_featured_user":["NO"],"contains_featured_ip":["NO"],"alert_type":"Unclassified","resolution_status":"STATUS_010_NEW","tags":["XDR Agent"],"alert_id":"8","detection_timestamp":1721031230123,"name":"Behavioral Threat","category":"Malware","endpoint_id":"13629dd5c7284859a2954c19c275285f","description":"Example Description","host_ip":["198.51.100.1"],"host_name":"ExampleHostName","action":"BLOCKED","source":"XDR Agent","original_tags":["XDR Agent"],"user_name":["ExampleUsername"],"mac_addresses":["00:00:00:00:00:00"],"action_pretty":"Prevented (Blocked)"}|
  
Example output:

```
{
  "alert": {
    "action": "BLOCKED",
    "action_country": [
      "UNKNOWN"
    ],
    "action_pretty": "Prevented (Blocked)",
    "action_process_signature_status": [
      "N/A"
    ],
    "actor_process_command_line": [
      "\"C:\\Windows\\System32\\cmd.exe\" "
    ],
    "actor_process_image_name": [
      "cmd.exe"
    ],
    "actor_process_image_path": [
      "C:\\Windows\\System32\\cmd.exe"
    ],
    "actor_process_image_sha256": [
      "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
    ],
    "actor_process_instance_id": [
      "ExampleID"
    ],
    "actor_process_os_pid": [
      123
    ],
    "actor_process_signature_status": [
      "N/A"
    ],
    "actor_process_signature_vendor": [
      "Microsoft Windows",
      "Microsoft Corporation"
    ],
    "agent_data_collection_status": false,
    "agent_device_domain": "ExampleDomain",
    "agent_fqdn": "ExampleFQDN",
    "agent_install_type": "STANDARD",
    "agent_is_vdi": false,
    "agent_os_sub_type": "6",
    "agent_os_type": "Windows",
    "agent_version": "7.5.0.36150",
    "alert_id": "8",
    "alert_type": "Unclassified",
    "association_strength": [
      50
    ],
    "attempt_counter": 0,
    "case_id": 1,
    "category": "Malware",
    "causality_actor_process_signature_status": [
      "N/A"
    ],
    "contains_featured_host": [
      "NO"
    ],
    "contains_featured_ip": [
      "NO"
    ],
    "contains_featured_user": [
      "NO"
    ],
    "description": "Example Description",
    "detection_timestamp": 1721031230123,
    "endpoint_id": "13629dd5c7284859a2954c19c275285f",
    "event_timestamp": [
      1721031230123
    ],
    "event_type": [
      "Process Execution"
    ],
    "external_id": "12345",
    "fw_is_phishing": [
      "N/A"
    ],
    "host_ip": [
      "198.51.100.1"
    ],
    "host_name": "ExampleHostName",
    "is_pcap": false,
    "is_whitelisted": false,
    "local_insert_ts": 1721031230123,
    "mac_addresses": [
      "00:00:00:00:00:00"
    ],
    "matching_status": "UNMATCHABLE",
    "mitre_tactic_id_and_name": [
      "ExampleTacticIDName"
    ],
    "mitre_technique_id_and_name": [
      "T000.000 - Example Technique: Name"
    ],
    "module_id": [
      "Behavioral Threat Protection"
    ],
    "name": "Behavioral Threat",
    "original_tags": [
      "XDR Agent"
    ],
    "os_actor_process_signature_status": [
      "N/A"
    ],
    "resolution_status": "STATUS_010_NEW",
    "severity": "high",
    "source": "XDR Agent",
    "starred": false,
    "tags": [
      "XDR Agent"
    ],
    "user_name": [
      "ExampleUsername"
    ]
  }
}
```

#### Get Incidents

This trigger is used to get incidents

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|5|False|Poll frequency in seconds|None|5|None|None|
  
Example input:

```
{
  "frequency": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident|incident|False|Incident|{ "Alert Count": 0, "Assigned User Mail": "", "Assigned User Pretty Name": {}, "Creation Time": {}, "Description": {}, "Detection Time": {}, "High Severity Alert Count": {}, "Host Count": {}, "Hosts": [ {} ], "Incident ID": {}, "Incident Name": {}, "Incident Sources": {}, "Low Severity Alert Count": {}, "Manual Description": {}, "Manual Score": {}, "Manual Severity": {}, "Med Severity Alert Count": {}, "Modification Time": {}, "Notes": {}, "Resolve Comment": {}, "Rule Based Score": {}, "Severity": {}, "Starred": "true", "Status": {}, "User Count": {}, "Users": {}, "XDR URL": {} }|
  
Example output:

```
{
  "incident": {
    "Alert Count": 0,
    "Assigned User Mail": "",
    "Assigned User Pretty Name": {},
    "Creation Time": {},
    "Description": {},
    "Detection Time": {},
    "High Severity Alert Count": {},
    "Host Count": {},
    "Hosts": [
      {}
    ],
    "Incident ID": {},
    "Incident Name": {},
    "Incident Sources": {},
    "Low Severity Alert Count": {},
    "Manual Description": {},
    "Manual Score": {},
    "Manual Severity": {},
    "Med Severity Alert Count": {},
    "Modification Time": {},
    "Notes": {},
    "Resolve Comment": {},
    "Rule Based Score": {},
    "Severity": {},
    "Starred": "true",
    "Status": {},
    "User Count": {},
    "Users": {},
    "XDR URL": {}
  }
}
```

#### Get Query Results

This trigger is used to runs the XQL and returns the output data results

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|5|True|Poll frequency in seconds|None|5|None|None|
|limit|integer|20|False|Integer representing the maximum number of results to return, defaults to 20, max value 1000|None|100|None|None|
|query|string|None|True|String of the XQL query|None|dataset=xdr_data I fields event_id, event_type, event_sub_type I limit 3|None|None|
|tenants|[]string|None|True|List of strings used when querying tenants managed by Managed Security Services Providers (MSSP)|None|["tenantID", "tenantID"]|None|None|
  
Example input:

```
{
  "frequency": 5,
  "limit": 20,
  "query": "dataset=xdr_data I fields event_id, event_type, event_sub_type I limit 3",
  "tenants": [
    "tenantID",
    "tenantID"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reply|reply|True|Object containing the query data results|{ "Number of Results": 0, "Query Cost": {}, "Remaining Quota": 0.0, "Results": { "Data": [ {} ], "Event Subtype": {} }, "Status": "" }|
  
Example output:

```
{
  "reply": {
    "Number of Results": 0,
    "Query Cost": {},
    "Remaining Quota": 0.0,
    "Results": {
      "Data": [
        {}
      ],
      "Event Subtype": {}
    },
    "Status": ""
  }
}
```
### Tasks


#### Monitor Alerts

This task is used to monitor alerts

##### Input
  
*This task does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]object|False|Alerts|[ { "action": "BLOCKED", "action_country": "UNKNOWN", "action_external_hostname": null, "action_file_macro_sha256": null, "action_file_md5": null, "action_file_name": null, "action_file_path": null, "action_file_sha256": null, "action_local_ip": null, "action_local_ip_v6": null, "action_local_port": null, "action_pretty": "Prevented (Blocked)", "action_process_causality_id": null, "action_process_image_command_line": null, "action_process_image_name": null, "action_process_image_sha256": null, "action_process_instance_id": null, "action_process_signature_status": "N/A", "action_process_signature_vendor": null, "action_registry_data": null, "action_registry_full_key": null, "action_registry_key_name": null, "action_registry_value_name": null, "action_remote_ip": null, "action_remote_ip_v6": null, "action_remote_port": null, "actor_causality_id": null, "actor_process_causality_id": null, "actor_process_command_line": "\"C:\\Users\\Administrator\\Downloads\\filename3.exe\" ", "actor_process_image_md5": null, "actor_process_image_name": "filename3.exe", "actor_process_image_path": "C:\\Users\\Administrator\\Downloads\\filename3.exe", "actor_process_image_sha256": "347874EEE7A8DA0E9277D1F601DA1326480E37D09766142BBD050D536090043F", "actor_process_instance_id": "Adr1YUm6dfgAAAnkAAAAAA==", "actor_process_os_pid": 2532, "actor_process_signature_status": "N/A", "actor_process_signature_vendor": null, "actor_thread_thread_id": null, "agent_data_collection_status": false, "agent_device_domain": "WORKGROUP", "agent_fqdn": "cortex-xdr-w12.WORKGROUP", "agent_host_boot_time": null, "agent_install_type": "STANDARD", "agent_ip_addresses_v6": null, "agent_is_vdi": false, "agent_os_sub_type": "6.2.9200", "agent_os_type": "Windows", "agent_version": "7.5.0.36150", "alert_id": "18", "alert_type": "Unclassified", "association_strength": 50, "attempt_counter": 0, "bioc_category_enum_key": null, "bioc_indicator": null, "case_id": 8, "category": "Malware", "causality_actor_causality_id": null, "causality_actor_process_command_line": null, "causality_actor_process_execution_time": null, "causality_actor_process_image_md5": null, "causality_actor_process_image_name": null, "causality_actor_process_image_path": null, "causality_actor_process_image_sha256": null, "causality_actor_process_signature_status": "N/A", "causality_actor_process_signature_vendor": null, "cloud_provider": null, "cluster_name": null, "container_id": null, "container_name": null, "contains_featured_host": "NO", "contains_featured_ip": "NO", "contains_featured_user": "NO", "deduplicate_tokens": "72515d0bdf934b9e82338cd1f32d6413", "description": "Suspicious executable detected", "detection_timestamp": 1724420114000, "dns_query_name": null, "dst_action_country": null, "dst_action_external_hostname": null, "dst_action_external_port": null, "dst_agent_id": null, "dst_association_strength": null, "dst_causality_actor_process_execution_time": null, "dynamic_fields": null, "end_match_attempt_ts": null, "endpoint_id": "13629dd5c7284859a2954c19c275285f", "event_id": null, "event_sub_type": null, "event_timestamp": 1724420114000, "event_type": "Process Execution", "events_length": 1, "external_id": "82ad0920baaf4a4fbc08990958217808", "filter_rule_id": null, "fw_app_category": null, "fw_app_id": null, "fw_app_subcategory": null, "fw_app_technology": null, "fw_device_name": null, "fw_email_recipient": null, "fw_email_sender": null, "fw_email_subject": null, "fw_interface_from": null, "fw_interface_to": null, "fw_is_phishing": "N/A", "fw_misc": null, "fw_rule": null, "fw_rule_id": null, "fw_serial_number": null, "fw_url_domain": null, "fw_vsys": null, "fw_xff": null, "host_ip": "10.4.92.53", "host_name": "cortex-xdr-w12", "identity_sub_type": null, "identity_type": null, "image_id": null, "image_name": null, "is_pcap": false, "is_whitelisted": false, "last_modified_ts": null, "local_insert_ts": 1724420117968, "mac": "00:50:56:94:42:04", "malicious_urls": null, "matching_service_rule_id": null, "matching_status": "UNMATCHABLE", "mitre_tactic_id_and_name": null, "mitre_technique_id_and_name": null, "module_id": "Local Analysis", "name": "Local Analysis Malware", "namespace": null, "operation_name": null, "original_tags": "DS:PANW/XDR Agent", "os_actor_causality_id": null, "os_actor_effective_username": null, "os_actor_process_causality_id": null, "os_actor_process_command_line": null, "os_actor_process_image_name": null, "os_actor_process_image_path": null, "os_actor_process_image_sha256": null, "os_actor_process_instance_id": null, "os_actor_process_os_pid": null, "os_actor_process_signature_status": "N/A", "os_actor_process_signature_vendor": null, "os_actor_thread_thread_id": null, "project": null, "referenced_resource": null, "resolution_comment": null, "resolution_status": "STATUS_010_NEW", "resource_sub_type": null, "resource_type": null, "severity": "medium", "source": "XDR Agent", "starred": false, "story_id": null, "tags": "DS:PANW/XDR Agent", "user_agent": null, "user_name": "Administrator" }]|
  
Example output:

```
{
  "alerts": [
    {
      "action": "BLOCKED",
      "action_country": "UNKNOWN",
      "action_external_hostname": null,
      "action_file_macro_sha256": null,
      "action_file_md5": null,
      "action_file_name": null,
      "action_file_path": null,
      "action_file_sha256": null,
      "action_local_ip": null,
      "action_local_ip_v6": null,
      "action_local_port": null,
      "action_pretty": "Prevented (Blocked)",
      "action_process_causality_id": null,
      "action_process_image_command_line": null,
      "action_process_image_name": null,
      "action_process_image_sha256": null,
      "action_process_instance_id": null,
      "action_process_signature_status": "N/A",
      "action_process_signature_vendor": null,
      "action_registry_data": null,
      "action_registry_full_key": null,
      "action_registry_key_name": null,
      "action_registry_value_name": null,
      "action_remote_ip": null,
      "action_remote_ip_v6": null,
      "action_remote_port": null,
      "actor_causality_id": null,
      "actor_process_causality_id": null,
      "actor_process_command_line": "\"C:\\Users\\Administrator\\Downloads\\filename3.exe\" ",
      "actor_process_image_md5": null,
      "actor_process_image_name": "filename3.exe",
      "actor_process_image_path": "C:\\Users\\Administrator\\Downloads\\filename3.exe",
      "actor_process_image_sha256": "347874EEE7A8DA0E9277D1F601DA1326480E37D09766142BBD050D536090043F",
      "actor_process_instance_id": "Adr1YUm6dfgAAAnkAAAAAA==",
      "actor_process_os_pid": 2532,
      "actor_process_signature_status": "N/A",
      "actor_process_signature_vendor": null,
      "actor_thread_thread_id": null,
      "agent_data_collection_status": false,
      "agent_device_domain": "WORKGROUP",
      "agent_fqdn": "cortex-xdr-w12.WORKGROUP",
      "agent_host_boot_time": null,
      "agent_install_type": "STANDARD",
      "agent_ip_addresses_v6": null,
      "agent_is_vdi": false,
      "agent_os_sub_type": "6.2.9200",
      "agent_os_type": "Windows",
      "agent_version": "7.5.0.36150",
      "alert_id": "18",
      "alert_type": "Unclassified",
      "association_strength": 50,
      "attempt_counter": 0,
      "bioc_category_enum_key": null,
      "bioc_indicator": null,
      "case_id": 8,
      "category": "Malware",
      "causality_actor_causality_id": null,
      "causality_actor_process_command_line": null,
      "causality_actor_process_execution_time": null,
      "causality_actor_process_image_md5": null,
      "causality_actor_process_image_name": null,
      "causality_actor_process_image_path": null,
      "causality_actor_process_image_sha256": null,
      "causality_actor_process_signature_status": "N/A",
      "causality_actor_process_signature_vendor": null,
      "cloud_provider": null,
      "cluster_name": null,
      "container_id": null,
      "container_name": null,
      "contains_featured_host": "NO",
      "contains_featured_ip": "NO",
      "contains_featured_user": "NO",
      "deduplicate_tokens": "72515d0bdf934b9e82338cd1f32d6413",
      "description": "Suspicious executable detected",
      "detection_timestamp": 1724420114000,
      "dns_query_name": null,
      "dst_action_country": null,
      "dst_action_external_hostname": null,
      "dst_action_external_port": null,
      "dst_agent_id": null,
      "dst_association_strength": null,
      "dst_causality_actor_process_execution_time": null,
      "dynamic_fields": null,
      "end_match_attempt_ts": null,
      "endpoint_id": "13629dd5c7284859a2954c19c275285f",
      "event_id": null,
      "event_sub_type": null,
      "event_timestamp": 1724420114000,
      "event_type": "Process Execution",
      "events_length": 1,
      "external_id": "82ad0920baaf4a4fbc08990958217808",
      "filter_rule_id": null,
      "fw_app_category": null,
      "fw_app_id": null,
      "fw_app_subcategory": null,
      "fw_app_technology": null,
      "fw_device_name": null,
      "fw_email_recipient": null,
      "fw_email_sender": null,
      "fw_email_subject": null,
      "fw_interface_from": null,
      "fw_interface_to": null,
      "fw_is_phishing": "N/A",
      "fw_misc": null,
      "fw_rule": null,
      "fw_rule_id": null,
      "fw_serial_number": null,
      "fw_url_domain": null,
      "fw_vsys": null,
      "fw_xff": null,
      "host_ip": "10.4.92.53",
      "host_name": "cortex-xdr-w12",
      "identity_sub_type": null,
      "identity_type": null,
      "image_id": null,
      "image_name": null,
      "is_pcap": false,
      "is_whitelisted": false,
      "last_modified_ts": null,
      "local_insert_ts": 1724420117968,
      "mac": "00:50:56:94:42:04",
      "malicious_urls": null,
      "matching_service_rule_id": null,
      "matching_status": "UNMATCHABLE",
      "mitre_tactic_id_and_name": null,
      "mitre_technique_id_and_name": null,
      "module_id": "Local Analysis",
      "name": "Local Analysis Malware",
      "namespace": null,
      "operation_name": null,
      "original_tags": "DS:PANW/XDR Agent",
      "os_actor_causality_id": null,
      "os_actor_effective_username": null,
      "os_actor_process_causality_id": null,
      "os_actor_process_command_line": null,
      "os_actor_process_image_name": null,
      "os_actor_process_image_path": null,
      "os_actor_process_image_sha256": null,
      "os_actor_process_instance_id": null,
      "os_actor_process_os_pid": null,
      "os_actor_process_signature_status": "N/A",
      "os_actor_process_signature_vendor": null,
      "os_actor_thread_thread_id": null,
      "project": null,
      "referenced_resource": null,
      "resolution_comment": null,
      "resolution_status": "STATUS_010_NEW",
      "resource_sub_type": null,
      "resource_type": null,
      "severity": "medium",
      "source": "XDR Agent",
      "starred": false,
      "story_id": null,
      "tags": "DS:PANW/XDR Agent",
      "user_agent": null,
      "user_name": "Administrator"
    }
  ]
}
```

### Custom Types
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|The action taken.|None|
|Action Country|[]string|None|False|The country where the action took place.|None|
|Action File Macro SHA256|string|None|False|The SHA256 hash of the macro file involved in the action.|None|
|Action File MD5|string|None|False|The MD5 hash of the file involved in the action.|None|
|Action File Name|string|None|False|The name of the file involved in the action.|None|
|Action File Path|string|None|False|The path to the file involved in the action.|None|
|Action File SHA256|string|None|False|The SHA256 hash of the file involved in the action.|None|
|Action Pretty|string|None|False|A pretty-printed representation of the action.|None|
|Action Process Signature Status|[]string|None|False|The status of the signature associated with the action process.|None|
|Actor Process Command Line|[]string|None|False|The command line arguments of the actor process.|None|
|Actor Process Image MD5|[]string|None|False|The MD5 hash of the actor process image.|None|
|Actor Process Image Name|[]string|None|False|The name of the actor process image.|None|
|Actor Process Image Path|[]string|None|False|The path to the actor process image.|None|
|Actor Process Image SHA256|[]string|None|False|The SHA256 hash of the actor process image.|None|
|Actor Process Instance ID|[]string|None|False|The instance ID of the actor process.|None|
|Actor Process Operating System PID|[]integer|None|False|The process ID of the actor process on the operating system.|None|
|Actor Process Signature Status|[]string|None|False|The status of the signature associated with the actor process.|None|
|Actor Process Signature Vendor|[]string|None|False|The vendor of the signature associated with the actor process.|None|
|Actor Thread Thread ID|[]integer|None|False|The thread ID of the actor thread.|None|
|Agent Data Collection Status|boolean|None|False|The status of data collection by the agent.|None|
|Agent Fully Qualified Domain Name|string|None|False|The fully qualified domain name of the agent.|None|
|Agent Host Boot Time|[]integer|None|False|The boot time of the host.|None|
|Agent Install Type|string|None|False|The install type of the agent.|None|
|Agent Is VDI|boolean|None|False|Indicates if the agent is running on a VDI.|None|
|Agent OS Sub Type|string|None|False|The subtype of the operating system running on the agent.|None|
|Agent Operating System Type|string|None|False|The type of the operating system running on the agent.|None|
|Agent Version|string|None|False|The version of the agent.|None|
|Alert ID|string|None|False|The unique ID of the alert.|None|
|Alert Type|string|None|False|The type of the alert.|None|
|Association Strength|[]integer|None|False|The strength of association between entities.|None|
|Attempt Counter|integer|None|False|The counter for attempts made.|None|
|Case ID|integer|None|False|The case ID associated with the alert.|None|
|Category|string|None|False|The general category of the event.|None|
|Causality Actor Causality ID|[]string|None|False|The causality ID of the causality actor.|None|
|Causality Actor Process Command Line|[]string|None|False|The command line arguments of the causality actor process.|None|
|Causality Actor Process Execution Time|[]integer|None|False|The execution time of the causality actor process.|None|
|Causality Actor Process Image MD5|[]string|None|False|The MD5 hash of the causality actor process image.|None|
|Causality Actor Process Image Name|[]string|None|False|The name of the causality actor process image.|None|
|Causality Actor Process Image Path|[]string|None|False|The path to the causality actor process image.|None|
|Causality Actor Process Image SHA256|[]string|None|False|The SHA256 hash of the causality actor process image.|None|
|Causality Actor Process Signature Status|[]string|None|False|The status of the signature associated with the causality actor process.|None|
|Causality Actor Process Signature Vendor|[]string|None|False|The vendor of the signature associated with the causality actor process.|None|
|Contains Featured Host|[]string|None|False|Indicates if the event contains a featured host.|None|
|Contains Featured IP|[]string|None|False|Indicates if the event contains a featured IP address.|None|
|Contains Featured User|[]string|None|False|Indicates if the event contains a featured user.|None|
|Description|string|None|False|A textual description of the event.|None|
|Detection Timestamp|integer|None|False|The timestamp when the detection occurred.|None|
|Endpoint ID|string|None|False|The ID of the endpoint.|None|
|Event Sub Type|[]integer|None|False|The subtype of the event.|None|
|Event Timestamp|[]integer|None|False|The timestamp of the event.|None|
|Event Type|[]string|None|False|The type of the event.|None|
|External ID|string|None|False|An external identifier for the alert.|None|
|Firewall Device Name|string|None|False|The name of the firewall device.|None|
|Firewall Is Phishing|[]string|None|False|Indicates if the event is related to phishing.|None|
|Host IP|[]string|None|False|The IP address of the host.|None|
|Host Name|string|None|False|The name of the host.|None|
|Image Name|string|None|False|The name of the image.|None|
|Is PCAP|boolean|None|False|Indicates if the alert involves PCAP data.|None|
|Is Whitelisted|boolean|None|False|Indicates if the event is whitelisted.|None|
|Local Insert Timestamp|integer|None|False|The timestamp when the alert was inserted locally.|None|
|MAC Addresses|[]string|None|False|The MAC addresses associated with the alert.|None|
|Matching Service Rule ID|string|None|False|The ID of the service rule matched.|None|
|Matching Status|string|None|False|The status of the matching process.|None|
|MITRE Tactic ID and Name|[]string|None|False|The ID and name of the MITRE tactic.|None|
|MITRE Technique ID and Name|[]string|None|False|The ID and name of the MITRE technique.|None|
|Module ID|[]string|None|False|The ID of the module.|None|
|Name|string|None|False|The name of the alert.|None|
|Original Tags|[]string|None|False|The original tags associated with the alert.|None|
|OS Actor Process Command Line|[]string|None|False|The command line arguments of the OS actor process.|None|
|OS Actor Process Image Name|[]string|None|False|The name of the OS actor process image.|None|
|OS Actor Process Image Path|[]string|None|False|The path to the OS actor process image.|None|
|OS Actor Process Image SHA256|[]string|None|False|The SHA256 hash of the OS actor process image.|None|
|OS Actor Process Operating System PID|[]integer|None|False|The process ID of the OS actor process on the operating system.|None|
|OS Actor Process Signature Status|[]string|None|False|The status of the signature associated with the OS actor process.|None|
|OS Actor Process Signature Vendor|[]string|None|False|The vendor of the signature associated with the OS actor process.|None|
|OS Actor Thread Thread ID|[]integer|None|False|The thread ID of the OS actor thread.|None|
|Resolution Status|string|None|False|The resolution status of the alert.|None|
|Severity|string|None|False|The severity level of the alert.|None|
|Source|string|None|False|The source of the alert.|None|
|Starred|boolean|None|False|Indicates if the alert is starred.|None|
|Tags|[]string|None|False|Tags associated with the alert.|None|
|User Name|[]string|None|False|The name of the user.|None|
  
**incident**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert Count|integer|None|False|Alert count|None|
|Assigned User Mail|string|None|False|Assigned user mail|None|
|Assigned User Pretty Name|string|None|False|Assigned user pretty name|None|
|Creation Time|integer|None|False|Creation time|None|
|Description|string|None|False|Description|None|
|Detection Time|string|None|False|Detection time|None|
|High Severity Alert Count|integer|None|False|High severity alert count|None|
|Host Count|integer|None|False|Host count|None|
|Hosts|[]string|None|False|Hosts|None|
|Incident ID|string|None|False|Incident ID|None|
|Incident Name|string|None|False|Incident name|None|
|Incident Sources|[]string|None|False|Incident sources|None|
|Low Severity Alert Count|integer|None|False|Low severity alert count|None|
|Manual Description|string|None|False|Manual description|None|
|Manual Score|string|None|False|Manual score|None|
|Manual Severity|string|None|False|Manual severity|None|
|Med Severity Alert Count|integer|None|False|Med severity alert count|None|
|Modification Time|integer|None|False|Modification time|None|
|Notes|string|None|False|Notes|None|
|Resolve Comment|string|None|False|Resolve comment|None|
|Rule Based Score|string|None|False|Rule based score|None|
|Severity|string|None|False|Severity|None|
|Starred|boolean|None|False|Starred|None|
|Status|string|None|False|Status|None|
|User Count|integer|None|False|User count|None|
|Users|[]string|None|False|Users|None|
|XDR URL|string|None|False|XDR URL|None|
  
**isolation_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action ID|integer|None|False|Action ID|None|
|Endpoints Count|integer|None|False|Endpoints count|None|
|Status|string|None|False|Status|None|
  
**endpoint**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alias|string|None|False|Alias|None|
|Content Version|string|None|False|Content version|None|
|Domain|string|None|False|Domain|None|
|Endpoint ID|string|None|False|Endpoint ID|None|
|Endpoint Name|string|None|False|Endpoint name|None|
|Endpoint Status|string|None|False|Endpoint status|None|
|Endpoint Type|string|None|False|Endpoint type|None|
|Endpoint Version|string|None|False|Endpoint version|None|
|First Seen|integer|None|False|First seen|None|
|Install Date|integer|None|False|Install date|None|
|Installation Package|string|None|False|Installation package|None|
|IP|[]string|None|False|IP|None|
|Is Isolated|string|None|False|Is isolated|None|
|Last Seen|integer|None|False|Last seen|None|
|Operational Status|string|None|False|Operational status|None|
|Operational Status Description|string|None|False|Operational status description|None|
|OS Type|string|None|False|OS type|None|
|Scan Status|string|None|False|Scan status|None|
|Users|[]string|None|False|Users|None|
  
**xql_query_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Data|[]object|None|False|List of obtained data results|None|
|Event Subtype|string|None|False|String representing a unique ID of more than 1000 number of results|None|
  
**reply**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Number of Results|integer|None|False|Integer representing the number of results returned|None|
|Query Cost|object|None|False|Float representing the number of query units collected for this API|None|
|Remaining Quota|float|None|False|Float representing the number of query units available for you to use|None|
|Results|xql_query_result|None|False|API results according to defined format field|None|
|Status|string|None|False|API call status: 'SUCCESS', 'FAIL', 'PENDING', 'PARTIAL_SUCCESS'|None|


## Troubleshooting

Isolate Endpoint fails with 500 error - This will happen if an isolation action (Isolate or Unisolate) is in progress on the selected endpoint. Wait a few minutes and try again.

# Version History

* 4.0.6 - Update `MonitorAlerts` to resume alert monitoring from the last task run time | Update error handling to log additional data | Update SDK to 6.2.4
* 4.0.5 - Update `MonitorAlerts` task pagination decision handling | update SDK to 6.2.2
* 4.0.4 - Raise authentication errors if provided invalid credentials
* 4.0.3 - `Monitor Incidents` - Add custom config exception handling
* 4.0.2 - SDK bump to 6.1.4
* 4.0.1 - SDK Bump to 6.1.3
* 4.0.0 - `Get Alerts`: Fixed issue where trigger was failing due to empty and different typed output fields - updated to generic object | Added Monitor_alert tasks | SDK Bump to 6.1.2
* 3.0.0 - Updated `hosts` output of `Get Incident` trigger and `Monitor Incident Events` task to separate host values | Update `insightconnect-plugin-runtime` to version 5
* 2.3.0 - Add types `xql_query_result` to `Get XQL Query Results` action's response | Add new trigger `Get Query Results`
* 2.2.1 - Fix issue in Get Incidents trigger where fields with null values were causing trigger to fail
* 2.2.0 - New action Get XQL Query Results | Update SDK to insightconnect-python-3-38-slim-plugin:4
* 2.1.1 - Fix issue in Monitor Incident Events task where fields with null values aren't removed from incidents leading to validation errors
* 2.1.0 - New task Monitor Incident Events
* 2.0.0 - New action Get File Quarantine Status | New trigger Get Alerts
* 1.0.0 - Initial plugin

# Links

* [Palo Alto Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr)

## References

* This plugin was tested using Viewer, Security Admin, and Instance Administrator Roles using both Standard and Advanced Security Levels. Please ensure your selected Role has adequate permissions to perform the desired actions.