# Description

Stop modern attacks with the industry’s first extended detection and response platform that spans your endpoint, network and cloud data.

# Key Features

* Get Endpoint Information
* Isolate or Unisolate an endpoint
* Add files to the block or allow lists

# Requirements

* A Palo Alto Cortex XDR API key
* A Palo Alto Cortex XDR API key ID
* The URL to your Palo Alto Cortex XDR API instance

# Supported Product Versions

* 2022-03-28 Palo Alto Cortex XDR API v1

# Documentation

## Setup

The required connection information is available in the Cortex XDR web dashboard. Click the gear icon, click settings, and then click on API Keys on the left.

The API Key will be generated when you create a new API key.

The API Key ID is the value from the ID column.

To get the API URL, right click on your API key and pick generate examples. The generated example is a URL that should look similar to "https://api-yourorg.xdr.us.paloaltonetworks.com/api_keys/validate/".
In our example the API URL is "https://api-yourorg.xdr.us.paloaltonetworks.com" and should be copied.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|The Cortex XDR API Key that is generated when creating a new key|None|1234123412341234asdfasdfasdfasdfasdf1234123412341234123412341234asdfasdfasdfasdfasdf123412341234123412341234asdfasdfasdfasdfasdf|
|api_key_id|int|None|True|The API Key ID shown in the Cortex XDR API Keys table in settings. e.g. 1, 2, 3|None|1|
|security_level|string|Standard|True|The Security Level of the key provided. This can be found in the API Key settings table in the Cortex XDR settings|['Advanced', 'Standard']|Standard|
|url|string|None|True|Cortex XDR API URL|None|https://api-example.xdr.us.paloaltonetworks.com/|

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

#### Get XQL Query Results

This action is used to start an XQL query and retrieve the query results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|start_time|integer|None|False|Integer in timestamp epoch milliseconds for start of the time range, Cortex XDR calls by default the last 24 hours if both 'Start Time' and 'End Time' values are not present|None|1599080399000|
|limit|integer|20|False|Integer representing the maximum number of results to return, defaults to 20, max value 1000|None|100|
|query|string|None|True|String of the XQL query|None|dataset=xdr_data | fields event_id, event_type, event_sub_type | limit 3|
|tenants|[]string|None|True|String that represents additional information regarding the action|None|["tenantID", "tenantID"]|
|end_time|integer|None|False|Integer in timestamp epoch milliseconds for end of the time range, Cortex XDR calls by default the last 24 hours if both 'Start Time' and 'End Time' values are not present|None|1598907600000|

Example input:

```
{
  "start_time": 1599080399000,
  "limit": 100,
  "query": "dataset=xdr_data | fields event_id, event_type, event_sub_type | limit 3",
  "tenants": [
    "tenantID",
    "tenantID"
  ],
  "end_time": 1598907600000
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reply|reply|False|Was the operation successful|

Example output:

```
{
  "reply": {
    "number_of_results": 1,
    "query_cost": {
      "1098781949": 0.0007469444444444444
    },
    "remaining_quota": 4.999253055555555,
    "results": {
      "data": [
        {
          "event_id": "eventID1",
          "_vendor": "PANW",
          "_product": "Fusion",
          "insert_timestamp": 1621541825324,
          "_time": 1621541523000,
          "event_type": "STORY",
          "event_sub_type": "NULL"
        }
      ]
    }
  }
}
```

#### Get File Quarantine Status

This action is used to get quarantine status for a file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|endpoint_id|string|None|True|Endpoint ID|None|example_ID|
|file_hash|string|None|True|File Hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|file_path|string|None|True|File path|None|powershell.exe|

Example input:

```
{
  "endpoint_id": "example_ID",
  "file_hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "file_path": "powershell.exe"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_is_quarantined|boolean|True|Check if the provided file is quarantined|

Example output:

```
{
  "file_is_quarantined": true
}
```

#### Block File

This action is used to add a file to the block list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|File blocked by InsightConnect|True|String that represents additional information regarding the action|None|File blocked by InsightConnect|
|file_hash|string|None|True|A SHA256 file hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|incident_id|string|None|False|If this is related to an incident, the ID should be entered here|None|5|

Example input:

```
{
  "comment": "File blocked by InsightConnect",
  "file_hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "incident_id": "5"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was the operation successful|

Example output:

```
{
  "success": true
}
```

#### Allow File

This action is used to add a file to the allow list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|File allowed by InsightConnect|True|String that represents additional information regarding the action|None|File allowed by InsightConnect|
|file_hash|string|None|True|A SHA256 file hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|incident_id|string|None|False|If this is related to an incident, the ID should be entered here|None|5|

Example input:

```
{
  "comment": "File allowed by InsightConnect",
  "file_hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "incident_id": 5
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was the operation successful|

Example output:

```
{
  "success": true
}
```

#### Isolate Endpoint

This action is used to isolate an endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|endpoint|string|None|True|Endpoint to isolate or unisolate. This can be an IPv4 address, hostname, or endpoint ID|None|9de5069c5afe602b2ea0a04b66beb2c0|
|isolation_state|string|Isolate|True|Isolation state to set|['Isolate', 'Unisolate']|Unisolate|
|whitelist|[]string|[]|False|This list contains a set of devices that should not be blocked. This can be a combination of IPv4 addresses, hostnames, or endpoint IDs|None|["198.51.100.100", "hostname123", "225494730938493804"]|

Example input:

```
{
  "endpoint": "9de5069c5afe602b2ea0a04b66beb2c0",
  "isolation_state": "Unisolate",
  "whitelist": [
    "198.51.100.100",
    "hostname123",
    "225494730938493804"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|isolation_result|True|The result of the isolation request|

Example output:

```
{
  "result": {
    "action_id": 14,
    "endpoints_count": 1
  }
}
```

#### Get Endpoint Details

This action is used to get information about an endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|endpoint|string|None|True|The endpoint to get information about. This can be an IPv4 address, hostname, or endpoint ID|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "endpoint": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|endpoints|[]endpoint|True|Any endpoints that match the given endpoint information|
|total_count|integer|True|Number of results found (max 100)|

Example output:

```
{
  "endpoints": [
    {
      "endpoint_id": "0123456abcdef12345abcde12345abcd",
      "endpoint_name": "EXAMPLEHOST",
      "endpoint_type": "AGENT_TYPE_WORKSTATION",
      "endpoint_status": "CONNECTED",
      "os_type": "AGENT_OS_WINDOWS",
      "ip": [
        "192.168.50.1"
      ],
      "users": [
        "ExampleUser"
      ],
      "domain": "WORKGROUP",
      "first_seen": 1621361378523,
      "last_seen": 1621449040261,
      "content_version": "181-58715",
      "installation_package": "Example-Install-Package",
      "install_date": 1621361378541,
      "endpoint_version": "7.3.2.26319",
      "is_isolated": "AGENT_UNISOLATED",
      "group_name": [],
      "operational_status": "PROTECTED",
      "operational_status_description": "[]",
      "scan_status": "SCAN_STATUS_IN_PROGRESS"
    }
  ],
  "total_count": 1
}
```

### Triggers

#### Get Query Results

This trigger runs the XQL and returns the output data results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|integer|5|True|Poll frequency in seconds|None|5|
|limit|integer|20|False|Integer representing the maximum number of results to return, defaults to 20, max value 1000|None|100|
|query|string|None|True|String of the XQL query|None|dataset=xdr_data | fields event_id, event_type, event_sub_type | limit 3|
|tenants|[]string|None|True|String that represents additional information regarding the action|None|["tenantID", "tenantID"]|

Example input:

```
{
  "frequency": 5,
  "limit": 100,
  "query": "dataset=xdr_data | fields event_id, event_type, event_sub_type | limit 3",
  "tenants": [
    "tenantID",
    "tenantID"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reply|reply|True|Was the operation successful|

Example output:

```
```

#### Get Alerts

This trigger is used to get Alerts.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|integer|5|False|Poll frequency in seconds|None|5|

Example input:

```
{
  "frequency": 5
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert|False|Alert|

Example output:

```
{
  "alert": {
    "external_id": "abcdefghijlkmnopqrstuv123456789",
    "severity": "high",
    "matching_status": "UNMATCHABLE",
    "end_match_attempt_ts": null,
    "local_insert_ts": 1621448835056,
    "bioc_indicator": null,
    "matching_service_rule_id": null,
    "attempt_counter": null,
    "bioc_category_enum_key": null,
    "is_whitelisted": false,
    "starred": false,
    "deduplicate_tokens": null,
    "filter_rule_id": null,
    "mitre_technique_id_and_name": [
      "T1140 - Deobfuscate/Decode Files or Information",
      "T1059.001 - Command and Scripting Interpreter: PowerShell",
      "T1059 - Command and Scripting Interpreter"
    ],
    "mitre_tactic_id_and_name": [
      "TA0005 - Defense Evasion",
      "TA0002 - Execution"
    ],
    "agent_version": "7.3.2.26319",
    "agent_device_domain": "example.com",
    "agent_fqdn": "example-host.example.com",
    "agent_os_type": "Windows",
    "agent_os_sub_type": "10.0.1234",
    "agent_data_collection_status": false,
    "mac": "ab:cd:ef:12:34:56",
    "events": [
      {
        "agent_install_type": "STANDARD",
        "agent_host_boot_time": null,
        "event_sub_type": null,
        "module_id": "Behavioral Threat Protection",
        "association_strength": null,
        "dst_association_strength": null,
        "story_id": null,
        "event_id": null,
        "event_type": "Process Execution",
        "event_timestamp": 1621448822758,
        "actor_process_instance_id": "<some id>",
        "actor_process_image_path": "C:\\Windows\\System32\\executable.exe",
        "actor_process_image_name": "cmd.exe",
        "actor_process_command_line": "C:\\Windows\\system32\\executable.exe /c \"\"C:\\detection_test.bat\" \"",
        "actor_process_signature_status": "N/A",
        "actor_process_signature_vendor": "Microsoft WindowsMicrosoft Corporation",
        "actor_process_image_sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
        "actor_process_image_md5": null,
        "actor_process_causality_id": null,
        "actor_causality_id": null,
        "actor_process_os_pid": 2964,
        "actor_thread_thread_id": null,
        "causality_actor_process_image_name": null,
        "causality_actor_process_command_line": null,
        "causality_actor_process_image_path": null,
        "causality_actor_process_signature_vendor": null,
        "causality_actor_process_signature_status": "N/A",
        "causality_actor_causality_id": null,
        "causality_actor_process_execution_time": null,
        "causality_actor_process_image_md5": null,
        "causality_actor_process_image_sha256": null,
        "action_file_path": null,
        "action_file_name": null,
        "action_file_md5": null,
        "action_file_sha256": null,
        "action_file_macro_sha256": null,
        "action_registry_data": null,
        "action_registry_key_name": null,
        "action_registry_value_name": null,
        "action_registry_full_key": null,
        "action_local_ip": null,
        "action_local_port": null,
        "action_remote_ip": null,
        "action_remote_port": null,
        "action_external_hostname": null,
        "action_country": "UNKNOWN",
        "action_process_instance_id": null,
        "action_process_causality_id": null,
        "action_process_image_name": null,
        "action_process_image_sha256": null,
        "action_process_image_command_line": null,
        "action_process_signature_status": "N/A",
        "action_process_signature_vendor": null,
        "os_actor_effective_username": null,
        "os_actor_process_instance_id": null,
        "os_actor_process_image_path": null,
        "os_actor_process_image_name": null,
        "os_actor_process_command_line": null,
        "os_actor_process_signature_status": "N/A",
        "os_actor_process_signature_vendor": null,
        "os_actor_process_image_sha256": null,
        "os_actor_process_causality_id": null,
        "os_actor_causality_id": null,
        "os_actor_process_os_pid": null,
        "os_actor_thread_thread_id": null,
        "fw_app_id": null,
        "fw_interface_from": null,
        "fw_interface_to": null,
        "fw_rule": null,
        "fw_rule_id": null,
        "fw_device_name": null,
        "fw_serial_number": null,
        "fw_url_domain": null,
        "fw_email_subject": null,
        "fw_email_sender": null,
        "fw_email_recipient": null,
        "fw_app_subcategory": null,
        "fw_app_category": null,
        "fw_app_technology": null,
        "fw_vsys": null,
        "fw_xff": null,
        "fw_misc": null,
        "fw_is_phishing": "N/A",
        "dst_agent_id": null,
        "dst_causality_actor_process_execution_time": null,
        "dns_query_name": null,
        "dst_action_external_hostname": null,
        "dst_action_country": null,
        "dst_action_external_port": null,
        "contains_featured_host": "NO",
        "contains_featured_user": "NO",
        "contains_featured_ip": "NO",
        "image_name": null,
        "container_id": null,
        "cluster_name": null,
        "user_name": "example"
      }
    ],
    "alert_id": "1",
    "detection_timestamp": 1621448822758,
    "name": "Behavioral Threat",
    "category": "Malware",
    "endpoint_id": "abcdefghijlkmnop123654",
    "description": "Behavioral threat detected (rule: heuristic.b.205)",
    "host_ip": [
      "10.0.20.10"
    ],
    "host_name": "example-host",
    "mac_addresses": [
      "ab:cd:ef:12:34:56"
    ],
    "source": "XDR Agent",
    "action": "BLOCKED",
    "action_pretty": "Prevented (Blocked)"
  }
}
```

#### Get Incidents

This trigger is used to get Incidents.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|integer|5|False|Poll frequency in seconds|None|5|

Example input:

```
{
  "frequency": 5
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|incident|False|Incident|

Example output:

```
{
   "incident":{
      "incident_id":"1",
      "incident_name":null,
      "creation_time":1621448873194,
      "modification_time":1621448873194,
      "detection_time":null,
      "status":"new",
      "severity":"high",
      "description":"'Behavioral Threat' generated by XDR Agent detected on host msedgewin10 involving user ieuser",
      "assigned_user_mail":null,
      "assigned_user_pretty_name":null,
      "alert_count":1,
      "low_severity_alert_count":0,
      "med_severity_alert_count":0,
      "high_severity_alert_count":1,
      "user_count":1,
      "host_count":1,
      "notes":null,
      "resolve_comment":null,
      "manual_severity":null,
      "manual_description":null,
      "xdr_url":"https://example.xdr.us.paloaltonetworks.com/incident-view/1",
      "starred":false,
      "hosts":[
         "examplehost:0123456abcdef12345abcde12345abcd"
      ],
      "users":[
         "exampleuser"
      ],
      "incident_sources":[
         "XDR Agent"
      ],
      "rule_based_score":null,
      "manual_score":null
   }
}
```

### Tasks

Plugin Tasks are currently in development! This new plugin capability will collect and deliver events to Insight products for search and use in automation workflows.

#### Monitor Incident Events

This task is used to monitor incident events.

Supported schedule types for this task include:
  - cron
  - minutes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|descriptions|[]string|None|False|Descriptions|None|["Behavioral threat detected (rule: heuristic.b.205)"]|
|incident_id_list|[]string|None|False|Incident ID list|None|["5"]|
|status|string|None|False|Status|['any', 'new', 'under_investigation', 'resolved_threat_handled', 'resolved_known_issue', 'resolved_false_positive', 'resolved_other', 'resolved_auto']|new|
|time_sorting_field|string|None|False|Field to use to sort Incident events|['modification_time', 'creation_time']|modification_time|

Example input:

```
{
  "descriptions": [
    "Behavioral threat detected (rule: heuristic.b.205)"
  ],
  "incident_id_list": [
    "5"
  ],
  "status": "new",
  "time_sorting_field": "modification_time"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]incident|False|Incident events|

Example output:

```
{
   "incident":{
      "incident_id":"1",
      "incident_name":null,
      "creation_time":1621448873194,
      "modification_time":1621448873194,
      "detection_time":null,
      "status":"new",
      "severity":"high",
      "description":"'Behavioral Threat' generated by XDR Agent detected on host msedgewin10 involving user ieuser",
      "assigned_user_mail":null,
      "assigned_user_pretty_name":null,
      "alert_count":1,
      "low_severity_alert_count":0,
      "med_severity_alert_count":0,
      "high_severity_alert_count":1,
      "user_count":1,
      "host_count":1,
      "notes":null,
      "resolve_comment":null,
      "manual_severity":null,
      "manual_description":null,
      "xdr_url":"https://example.xdr.us.paloaltonetworks.com/incident-view/1",
      "starred":false,
      "hosts":[
         "examplehost:0123456abcdef12345abcde12345abcd"
      ],
      "users":[
         "exampleuser"
      ],
      "incident_sources":[
         "XDR Agent"
      ],
      "rule_based_score":null,
      "manual_score":null
   }
}
```

### Custom Output Types

#### alert

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action|string|False|Action|
|Action Pretty|string|False|Action pretty|
|Agent Data Collection Status|boolean|False|Agent data collection status|
|Agent Device Domain|string|False|Agent device domain|
|Agent FQDN|string|False|Agent FQDN|
|Agent OS Sub Type|string|False|Agent OS sub type|
|Agent OS Type|string|False|Agent OS type|
|Agent Version|string|False|Agent version|
|Alert ID|string|False|Alert ID|
|Attempt Counter|string|False|Attempt counter|
|BIOC Category Enum Key|string|False|BIOC category enum key|
|BIOC Indicator|string|False|BIOC indicator|
|Category|string|False|Category|
|Deduplicate Tokens|string|False|Deduplicate tokens|
|Description|string|False|Description|
|Detection Timestamp|integer|False|Detection timestamp|
|End Match Attempt TS|string|False|End match attempt TS|
|Endpoint ID|string|False|Endpoint ID|
|Events|[]event|False|Events|
|External ID|string|False|External ID|
|Filter Rule ID|string|False|Filter rule ID|
|Host IP|[]string|False|Host IP|
|Host Name|string|False|Host name|
|Is Whitelisted|boolean|False|Is whitelisted|
|Local Insert TS|integer|False|Local insert TS|
|MAC|string|False|MAC|
|MAC Addresses|[]string|False|MAC addresses|
|Matching Service Rule ID|string|False|Matching service rule ID|
|Matching Status|string|False|Matching status|
|MITRE Tactic ID And Name|[]string|False|MITRE tactic ID and name|
|MITRE Technique ID And Name|[]string|False|MITRE technique ID and name|
|Name|string|False|Name|
|Severity|string|False|Severity|
|Source|string|False|Source|
|Starred|boolean|False|Starred|

#### endpoint

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alias|string|False|Alias|
|Content Version|string|False|Content version|
|Domain|string|False|Domain|
|Endpoint ID|string|False|Endpoint ID|
|Endpoint Name|string|False|Endpoint name|
|Endpoint Status|string|False|Endpoint status|
|Endpoint Type|string|False|Endpoint type|
|Endpoint Version|string|False|Endpoint version|
|First Seen|integer|False|First seen|
|Install Date|integer|False|Install date|
|Installation Package|string|False|Installation package|
|IP|[]string|False|IP|
|Is Isolated|string|False|Is isolated|
|Last Seen|integer|False|Last seen|
|Operational Status|string|False|Operational status|
|Operational Status Description|string|False|Operational status description|
|OS Type|string|False|OS type|
|Scan Status|string|False|Scan status|
|Users|[]string|False|Users|

#### event

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action Country|string|False|Action country|
|Action External Hostname|string|False|Action external hostname|
|Action File Macro SHA256|string|False|Action file macro SHA256|
|Action File MD5|string|False|Action file MD5|
|Action File Name|string|False|Action file name|
|Action File Path|string|False|Action file path|
|Action File SHA256|string|False|Action file SHA256|
|Action Local IP|string|False|Action local IP|
|Action Local Port|string|False|Action local port|
|Action Process Causality ID|string|False|Action process causality ID|
|Action Process Image Command Line|string|False|Action process image command line|
|Action Process Image Name|string|False|Action process image name|
|Action Process Image SHA256|string|False|Action process image SHA256|
|Action Process Instance ID|string|False|Action process instance ID|
|Action Process Signature Status|string|False|Action process signature status|
|Action Process Signature Vendor|string|False|Action process signature vendor|
|Action Registry Data|string|False|Action registry data|
|Action Registry Full Key|string|False|Action registry full key|
|Action Registry Key Name|string|False|Action registry key name|
|Action Registry Value Name|string|False|Action registry value name|
|Action Remote IP|string|False|Action remote IP|
|Action Remote Port|string|False|Action remote port|
|Actor Causality ID|string|False|Actor causality ID|
|Actor Process Causality ID|string|False|Actor process causality ID|
|Actor Process Command Line|string|False|Actor process command line|
|Actor Process Image MD5|string|False|Actor process image MD5|
|Actor Process Image Name|string|False|Actor process image name|
|Actor Process Image Path|string|False|Actor process image path|
|Actor Process Image SHA256|string|False|Actor process image SHA256|
|Actor Process Instance ID|string|False|Actor process instance ID|
|Actor Process OS PID|integer|False|Actor process OS PID|
|Actor Process Signature Status|string|False|Actor process signature status|
|Actor Process Signature Vendor|string|False|Actor process signature vendor|
|Actor Thread Thread ID|string|False|Actor thread thread ID|
|Agent Host Boot Time|string|False|Agent host boot time|
|Agent Install Type|string|False|Agent install type|
|Association Strength|string|False|Association strength|
|Causality Actor Causality ID|string|False|Causality actor causality ID|
|Causality Actor Process Command Line|string|False|Causality actor process command line|
|Causality Actor Process Execution Time|string|False|Causality actor process execution time|
|Causality Actor Process Image MD5|string|False|Causality actor process image MD5|
|Causality Actor Process Image Name|string|False|Causality actor process image name|
|Causality Actor Process Image Path|string|False|Causality actor process image path|
|Causality Actor Process Image SHA256|string|False|Causality actor process image SHA256|
|Causality Actor Process Signature Status|string|False|Causality actor process signature status|
|Causality Actor Process Signature Vendor|string|False|Causality actor process signature vendor|
|Cluster Name|string|False|Cluster name|
|Container ID|string|False|Container ID|
|Contains Featured Host|string|False|Contains featured host|
|Contains Featured IP|string|False|Contains featured IP|
|Contains Featured User|string|False|Contains featured user|
|DNS Query Name|string|False|DNS query name|
|DST Action Country|string|False|DST action country|
|DST Action External Hostname|string|False|DST action external hostname|
|DST Action External Port|string|False|DST action external port|
|DST Agent ID|string|False|DST agent ID|
|DST Association Strength|string|False|DST association strength|
|DST Causality Actor Process Execution Time|string|False|DST causality actor process execution time|
|Event ID|string|False|Event ID|
|Event Sub Type|string|False|Event sub type|
|Event Timestamp|integer|False|Event timestamp|
|Event Type|string|False|Event type|
|FW App Category|string|False|FW app category|
|FW App ID|string|False|FW app ID|
|FW App Subcategory|string|False|FW app subcategory|
|FW App Technology|string|False|FW app technology|
|FW Device Name|string|False|FW device name|
|FW Email Recipient|string|False|FW email recipient|
|FW Email Sender|string|False|FW email sender|
|FW Email Subject|string|False|FW email subject|
|FW Interface From|string|False|FW interface from|
|FW Interface To|string|False|FW interface to|
|FW Is Phishing|string|False|FW is phishing|
|FW Misc|string|False|FW misc|
|FW Rule|string|False|FW rule|
|FW Rule ID|string|False|FW rule ID|
|FW Serial Number|string|False|FW serial number|
|FW URL Domain|string|False|FW URL domain|
|FW VSYS|string|False|FW VSYS|
|FW XFF|string|False|FW XFF|
|Image Name|string|False|Image name|
|Module ID|string|False|Module ID|
|OS Actor Causality ID|string|False|OS actor causality ID|
|OS Actor Effective Username|string|False|OS actor effective username|
|OS Actor Process Causality ID|string|False|OS actor process causality ID|
|OS Actor Process Command Line|string|False|OS actor process command line|
|OS Actor Process Image Name|string|False|OS actor process image name|
|OS Actor Process Image Path|string|False|OS actor process image path|
|OS Actor Process Image SHA256|string|False|OS actor process image SHA256|
|OS Actor Process Instance ID|string|False|OS actor process instance ID|
|OS Actor Process OS PID|string|False|OS actor process OS PID|
|OS Actor Process Signature Status|string|False|OS actor process signature status|
|OS Actor Process Signature Vendor|string|False|OS actor process signature vendor|
|OS Actor Thread Thread ID|string|False|OS actor thread thread ID|
|Story ID|string|False|Story ID|
|User Name|string|False|User name|

#### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert Count|integer|False|Alert count|
|Assigned User Mail|string|False|Assigned user mail|
|Assigned User Pretty Name|string|False|Assigned user pretty name|
|Creation Time|integer|False|Creation time|
|Description|string|False|Description|
|Detection Time|string|False|Detection time|
|High Severity Alert Count|integer|False|High severity alert count|
|Host Count|integer|False|Host count|
|Hosts|[]string|False|Hosts|
|Incident ID|string|False|Incident ID|
|Incident Name|string|False|Incident name|
|Incident Sources|[]string|False|Incident sources|
|Low Severity Alert Count|integer|False|Low severity alert count|
|Manual Description|string|False|Manual description|
|Manual Score|string|False|Manual score|
|Manual Severity|string|False|Manual severity|
|Med Severity Alert Count|integer|False|Med severity alert count|
|Modification Time|integer|False|Modification time|
|Notes|string|False|Notes|
|Resolve Comment|string|False|Resolve comment|
|Rule Based Score|string|False|Rule based score|
|Severity|string|False|Severity|
|Starred|boolean|False|Starred|
|Status|string|False|Status|
|User Count|integer|False|User count|
|Users|[]string|False|Users|
|XDR URL|string|False|XDR URL|

#### isolation_result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action ID|integer|False|Action ID|
|Endpoints Count|integer|False|Endpoints count|
|Status|string|False|Status|

#### reply

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Number of Results|integer|False|Integer representing the number of results returned|
|Query Cost|object|False|Float representing the number of query units collected for this API|
|Remaining Quota|float|False|Float representing the number of query units available for you to use|
|Results|xql_query_result|False|API results according to defined format field|
|Status|string|False|API call status: 'SUCCESS', 'FAIL', 'PENDING', 'PARTIAL_SUCCESS'|

#### xql_query_result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|[]xql_query_result_data|False|List of obtained data results|
|Event Subtype|string|False|String representing a unique ID of more than 1000 number of results|

#### xql_query_result_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Product|string|False|Name of a product|
|Time|integer|False|Integer representing the event time as epoch in ms|
|Vendor Name|string|False|The name of a vendor|
|Event ID|string|False|String representing the event identifier|
|Event Subtype|string|False|String representing the subtype of an event|
|Event Type|string|False|The type of event|
|Insertion timestamp|integer|False|Integer representing insertion timestamp as epoch in ms|


## Troubleshooting

* Isolate Endpoint fails with 500 error - This will happen if an isolation action (Isolate or Unisolate) is in progress on the selected endpoint. Wait a few minutes and try again. 

# Version History

* 2.3.0 - Add types `xql_query_result`, `xql_query_result_data` to `Get XQL Query Results` action's response | Add new trigger `Get Query Results` 
* 2.2.1 - Fix issue in Get Incidents trigger where fields with null values were causing trigger to fail
* 2.2.0 - New action Get XQL Query Results | Update SDK to insightconnect-python-3-38-slim-plugin:4
* 2.1.1 - Fix issue in Monitor Incident Events task where fields with null values aren't removed from incidents leading to validation errors
* 2.1.0 - New task Monitor Incident Events
* 2.0.0 - New action Get File Quarantine Status | New trigger Get Alerts
* 1.0.0 - Initial plugin

# Links

## References

* [Palo Alto Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr)
* This plugin was tested using Viewer, Security Admin, and Instance Administrator Roles using both Standard and Advanced Security Levels. Please ensure your selected Role has adequate permissions to perform the desired actions.
