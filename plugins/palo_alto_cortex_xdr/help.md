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
  
* 2022-08-09 Palo Alto Cortex XDR API v1

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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


#### Allow File
  
Add a file to the allow list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
  
Add a file to the block list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|File blocked by InsightConnect|True|String that represents additional information regarding the action|None|File blocked by InsightConnect|
|file_hash|string|None|True|A SHA256 file hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|incident_id|string|None|False|If this is related to an incident, the ID should be entered here|None|5|
  
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
  
Get information about an endpoint

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint|string|None|True|The endpoint to get information about. This can be an IPv4 address, hostname, or endpoint ID|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
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
  
Get quarantine status for a file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
  
Start an XQL query and retrieve the query results

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_time|integer|None|False|Integer in timestamp epoch milliseconds for end of the time range, Cortex XDR calls by default the last 24 hours if both 'Start Time' and 'End Time' values are not present|None|1598907600000|
|limit|integer|20|False|Integer representing the maximum number of results to return, defaults to 20, max value 1000|None|100|
|query|string|None|True|String of the XQL query|None|dataset=xdr_data I fields event_id, event_type, event_sub_type I limit 3|
|start_time|integer|None|False|Integer in timestamp epoch milliseconds for start of the time range, Cortex XDR calls by default the last 24 hours if both 'Start Time' and 'End Time' values are not present|None|1599080399000|
|tenants|[]string|None|True|List of strings used when querying tenants managed by Managed Security Services Providers (MSSP)|None|["tenantID", "tenantID"]|

Example input:

```
{
  "end_time": 1598907600000,
  "limit": 20,
  "query": "dataset=xdr_data I fields event_id, event_type, event_sub_type I limit 3",
  "start_time": 1599080399000,
  "tenants": "tenantID"
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
  
Isolate or unisolate an endpoint

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint|string|None|True|Endpoint to isolate or unisolate. This can be an IPv4 address, hostname, or endpoint ID|None|9de5069c5afe602b2ea0a04b66beb2c0|
|isolation_state|string|Isolate|True|Isolation state to set|['Isolate', 'Unisolate']|Unisolate|
|whitelist|[]string|[]|False|This list contains a set of devices that should not be blocked. This can be a combination of IPv4 addresses, hostnames, or endpoint IDs|None|["198.51.100.100", "hostname123", "225494730938493804"]|

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
  
Get alerts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|5|False|Poll frequency in seconds|None|5|
  
Example input:

```
{
  "frequency": 5
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert|False|Alert|{ "Action": "", "Action Pretty": {}, "Agent Data Collection Status": "true", "Agent Device Domain": {}, "Agent FQDN": {}, "Agent OS Sub Type": {}, "Agent OS Type": {}, "Agent Version": {}, "Alert ID": {}, "Attempt Counter": {}, "BIOC Category Enum Key": {}, "BIOC Indicator": {}, "Category": {}, "Deduplicate Tokens": {}, "Description": {}, "Detection Timestamp": 0, "End Match Attempt TS": {}, "Endpoint ID": {}, "Events": [ { "Action Country": {}, "Action External Hostname": {}, "Action File MD5": {}, "Action File Macro SHA256": {}, "Action File Name": {}, "Action File Path": {}, "Action File SHA256": {}, "Action Local IP": {}, "Action Local Port": {}, "Action Process Causality ID": {}, "Action Process Image Command Line": {}, "Action Process Image Name": {}, "Action Process Image SHA256": {}, "Action Process Instance ID": {}, "Action Process Signature Status": {}, "Action Process Signature Vendor": {}, "Action Registry Data": {}, "Action Registry Full Key": {}, "Action Registry Key Name": {}, "Action Registry Value Name": {}, "Action Remote IP": {}, "Action Remote Port": {}, "Actor Causality ID": {}, "Actor Process Causality ID": {}, "Actor Process Command Line": {}, "Actor Process Image MD5": {}, "Actor Process Image Name": {}, "Actor Process Image Path": {}, "Actor Process Image SHA256": {}, "Actor Process Instance ID": {}, "Actor Process OS PID": {}, "Actor Process Signature Status": {}, "Actor Process Signature Vendor": {}, "Actor Thread Thread ID": {}, "Agent Host Boot Time": {}, "Agent Install Type": {}, "Association Strength": {}, "Causality Actor Causality ID": {}, "Causality Actor Process Command Line": {}, "Causality Actor Process Execution Time": {}, "Causality Actor Process Image MD5": {}, "Causality Actor Process Image Name": {}, "Causality Actor Process Image Path": {}, "Causality Actor Process Image SHA256": {}, "Causality Actor Process Signature Status": {}, "Causality Actor Process Signature Vendor": {}, "Cluster Name": {}, "Container ID": {}, "Contains Featured Host": {}, "Contains Featured IP": {}, "Contains Featured User": {}, "DNS Query Name": {}, "DST Action Country": {}, "DST Action External Hostname": {}, "DST Action External Port": {}, "DST Agent ID": {}, "DST Association Strength": {}, "DST Causality Actor Process Execution Time": {}, "Event ID": {}, "Event Sub Type": {}, "Event Timestamp": {}, "Event Type": {}, "FW App Category": {}, "FW App ID": {}, "FW App Subcategory": {}, "FW App Technology": {}, "FW Device Name": {}, "FW Email Recipient": {}, "FW Email Sender": {}, "FW Email Subject": {}, "FW Interface From": {}, "FW Interface To": {}, "FW Is Phishing": {}, "FW Misc": {}, "FW Rule": {}, "FW Rule ID": {}, "FW Serial Number": {}, "FW URL Domain": {}, "FW VSYS": {}, "FW XFF": {}, "Image Name": {}, "Module ID": {}, "OS Actor Causality ID": {}, "OS Actor Effective Username": {}, "OS Actor Process Causality ID": {}, "OS Actor Process Command Line": {}, "OS Actor Process Image Name": {}, "OS Actor Process Image Path": {}, "OS Actor Process Image SHA256": {}, "OS Actor Process Instance ID": {}, "OS Actor Process OS PID": {}, "OS Actor Process Signature Status": {}, "OS Actor Process Signature Vendor": {}, "OS Actor Thread Thread ID": {}, "Story ID": {}, "User Name": {} } ], "External ID": {}, "Filter Rule ID": {}, "Host IP": [ {} ], "Host Name": {}, "Is Whitelisted": {}, "Local Insert TS": {}, "MAC": {}, "MAC Addresses": {}, "MITRE Tactic ID And Name": {}, "MITRE Technique ID And Name": {}, "Matching Service Rule ID": {}, "Matching Status": {}, "Name": {}, "Severity": {}, "Source": {}, "Starred": {} }|
  
Example output:

```
{
  "alert": {
    "Action": "",
    "Action Pretty": {},
    "Agent Data Collection Status": "true",
    "Agent Device Domain": {},
    "Agent FQDN": {},
    "Agent OS Sub Type": {},
    "Agent OS Type": {},
    "Agent Version": {},
    "Alert ID": {},
    "Attempt Counter": {},
    "BIOC Category Enum Key": {},
    "BIOC Indicator": {},
    "Category": {},
    "Deduplicate Tokens": {},
    "Description": {},
    "Detection Timestamp": 0,
    "End Match Attempt TS": {},
    "Endpoint ID": {},
    "Events": [
      {
        "Action Country": {},
        "Action External Hostname": {},
        "Action File MD5": {},
        "Action File Macro SHA256": {},
        "Action File Name": {},
        "Action File Path": {},
        "Action File SHA256": {},
        "Action Local IP": {},
        "Action Local Port": {},
        "Action Process Causality ID": {},
        "Action Process Image Command Line": {},
        "Action Process Image Name": {},
        "Action Process Image SHA256": {},
        "Action Process Instance ID": {},
        "Action Process Signature Status": {},
        "Action Process Signature Vendor": {},
        "Action Registry Data": {},
        "Action Registry Full Key": {},
        "Action Registry Key Name": {},
        "Action Registry Value Name": {},
        "Action Remote IP": {},
        "Action Remote Port": {},
        "Actor Causality ID": {},
        "Actor Process Causality ID": {},
        "Actor Process Command Line": {},
        "Actor Process Image MD5": {},
        "Actor Process Image Name": {},
        "Actor Process Image Path": {},
        "Actor Process Image SHA256": {},
        "Actor Process Instance ID": {},
        "Actor Process OS PID": {},
        "Actor Process Signature Status": {},
        "Actor Process Signature Vendor": {},
        "Actor Thread Thread ID": {},
        "Agent Host Boot Time": {},
        "Agent Install Type": {},
        "Association Strength": {},
        "Causality Actor Causality ID": {},
        "Causality Actor Process Command Line": {},
        "Causality Actor Process Execution Time": {},
        "Causality Actor Process Image MD5": {},
        "Causality Actor Process Image Name": {},
        "Causality Actor Process Image Path": {},
        "Causality Actor Process Image SHA256": {},
        "Causality Actor Process Signature Status": {},
        "Causality Actor Process Signature Vendor": {},
        "Cluster Name": {},
        "Container ID": {},
        "Contains Featured Host": {},
        "Contains Featured IP": {},
        "Contains Featured User": {},
        "DNS Query Name": {},
        "DST Action Country": {},
        "DST Action External Hostname": {},
        "DST Action External Port": {},
        "DST Agent ID": {},
        "DST Association Strength": {},
        "DST Causality Actor Process Execution Time": {},
        "Event ID": {},
        "Event Sub Type": {},
        "Event Timestamp": {},
        "Event Type": {},
        "FW App Category": {},
        "FW App ID": {},
        "FW App Subcategory": {},
        "FW App Technology": {},
        "FW Device Name": {},
        "FW Email Recipient": {},
        "FW Email Sender": {},
        "FW Email Subject": {},
        "FW Interface From": {},
        "FW Interface To": {},
        "FW Is Phishing": {},
        "FW Misc": {},
        "FW Rule": {},
        "FW Rule ID": {},
        "FW Serial Number": {},
        "FW URL Domain": {},
        "FW VSYS": {},
        "FW XFF": {},
        "Image Name": {},
        "Module ID": {},
        "OS Actor Causality ID": {},
        "OS Actor Effective Username": {},
        "OS Actor Process Causality ID": {},
        "OS Actor Process Command Line": {},
        "OS Actor Process Image Name": {},
        "OS Actor Process Image Path": {},
        "OS Actor Process Image SHA256": {},
        "OS Actor Process Instance ID": {},
        "OS Actor Process OS PID": {},
        "OS Actor Process Signature Status": {},
        "OS Actor Process Signature Vendor": {},
        "OS Actor Thread Thread ID": {},
        "Story ID": {},
        "User Name": {}
      }
    ],
    "External ID": {},
    "Filter Rule ID": {},
    "Host IP": [
      {}
    ],
    "Host Name": {},
    "Is Whitelisted": {},
    "Local Insert TS": {},
    "MAC": {},
    "MAC Addresses": {},
    "MITRE Tactic ID And Name": {},
    "MITRE Technique ID And Name": {},
    "Matching Service Rule ID": {},
    "Matching Status": {},
    "Name": {},
    "Severity": {},
    "Source": {},
    "Starred": {}
  }
}
```

#### Get Incidents
  
Get incidents

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|5|False|Poll frequency in seconds|None|5|
  
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
  
Runs the XQL and returns the output data results

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|5|True|Poll frequency in seconds|None|5|
|limit|integer|20|False|Integer representing the maximum number of results to return, defaults to 20, max value 1000|None|100|
|query|string|None|True|String of the XQL query|None|dataset=xdr_data I fields event_id, event_type, event_sub_type I limit 3|
|tenants|[]string|None|True|List of strings used when querying tenants managed by Managed Security Services Providers (MSSP)|None|["tenantID", "tenantID"]|

Example input:

```
{
  "frequency": 5,
  "limit": 20,
  "query": "dataset=xdr_data I fields event_id, event_type, event_sub_type I limit 3",
  "tenants": "tenantID"
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


#### Monitor Incident Events
  
Monitor incident events

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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
  "incident_id_list": 5,
  "status": "new",
  "time_sorting_field": "modification_time"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]incident|False|Incident events|[ { "Alert Count": 0, "Assigned User Mail": "", "Assigned User Pretty Name": {}, "Creation Time": {}, "Description": {}, "Detection Time": {}, "High Severity Alert Count": {}, "Host Count": {}, "Hosts": [ {} ], "Incident ID": {}, "Incident Name": {}, "Incident Sources": {}, "Low Severity Alert Count": {}, "Manual Description": {}, "Manual Score": {}, "Manual Severity": {}, "Med Severity Alert Count": {}, "Modification Time": {}, "Notes": {}, "Resolve Comment": {}, "Rule Based Score": {}, "Severity": {}, "Starred": "true", "Status": {}, "User Count": {}, "Users": {}, "XDR URL": {} } ]|
  
Example output:

```
{
  "events": [
    {
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
  ]
}
```

### Custom Output Types
  
**event**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action Country|string|None|False|Action country|None|
|Action External Hostname|string|None|False|Action external hostname|None|
|Action File Macro SHA256|string|None|False|Action file macro SHA256|None|
|Action File MD5|string|None|False|Action file MD5|None|
|Action File Name|string|None|False|Action file name|None|
|Action File Path|string|None|False|Action file path|None|
|Action File SHA256|string|None|False|Action file SHA256|None|
|Action Local IP|string|None|False|Action local IP|None|
|Action Local Port|string|None|False|Action local port|None|
|Action Process Causality ID|string|None|False|Action process causality ID|None|
|Action Process Image Command Line|string|None|False|Action process image command line|None|
|Action Process Image Name|string|None|False|Action process image name|None|
|Action Process Image SHA256|string|None|False|Action process image SHA256|None|
|Action Process Instance ID|string|None|False|Action process instance ID|None|
|Action Process Signature Status|string|None|False|Action process signature status|None|
|Action Process Signature Vendor|string|None|False|Action process signature vendor|None|
|Action Registry Data|string|None|False|Action registry data|None|
|Action Registry Full Key|string|None|False|Action registry full key|None|
|Action Registry Key Name|string|None|False|Action registry key name|None|
|Action Registry Value Name|string|None|False|Action registry value name|None|
|Action Remote IP|string|None|False|Action remote IP|None|
|Action Remote Port|string|None|False|Action remote port|None|
|Actor Causality ID|string|None|False|Actor causality ID|None|
|Actor Process Causality ID|string|None|False|Actor process causality ID|None|
|Actor Process Command Line|string|None|False|Actor process command line|None|
|Actor Process Image MD5|string|None|False|Actor process image MD5|None|
|Actor Process Image Name|string|None|False|Actor process image name|None|
|Actor Process Image Path|string|None|False|Actor process image path|None|
|Actor Process Image SHA256|string|None|False|Actor process image SHA256|None|
|Actor Process Instance ID|string|None|False|Actor process instance ID|None|
|Actor Process OS PID|integer|None|False|Actor process OS PID|None|
|Actor Process Signature Status|string|None|False|Actor process signature status|None|
|Actor Process Signature Vendor|string|None|False|Actor process signature vendor|None|
|Actor Thread Thread ID|string|None|False|Actor thread thread ID|None|
|Agent Host Boot Time|string|None|False|Agent host boot time|None|
|Agent Install Type|string|None|False|Agent install type|None|
|Association Strength|string|None|False|Association strength|None|
|Causality Actor Causality ID|string|None|False|Causality actor causality ID|None|
|Causality Actor Process Command Line|string|None|False|Causality actor process command line|None|
|Causality Actor Process Execution Time|string|None|False|Causality actor process execution time|None|
|Causality Actor Process Image MD5|string|None|False|Causality actor process image MD5|None|
|Causality Actor Process Image Name|string|None|False|Causality actor process image name|None|
|Causality Actor Process Image Path|string|None|False|Causality actor process image path|None|
|Causality Actor Process Image SHA256|string|None|False|Causality actor process image SHA256|None|
|Causality Actor Process Signature Status|string|None|False|Causality actor process signature status|None|
|Causality Actor Process Signature Vendor|string|None|False|Causality actor process signature vendor|None|
|Cluster Name|string|None|False|Cluster name|None|
|Container ID|string|None|False|Container ID|None|
|Contains Featured Host|string|None|False|Contains featured host|None|
|Contains Featured IP|string|None|False|Contains featured IP|None|
|Contains Featured User|string|None|False|Contains featured user|None|
|DNS Query Name|string|None|False|DNS query name|None|
|DST Action Country|string|None|False|DST action country|None|
|DST Action External Hostname|string|None|False|DST action external hostname|None|
|DST Action External Port|string|None|False|DST action external port|None|
|DST Agent ID|string|None|False|DST agent ID|None|
|DST Association Strength|string|None|False|DST association strength|None|
|DST Causality Actor Process Execution Time|string|None|False|DST causality actor process execution time|None|
|Event ID|string|None|False|Event ID|None|
|Event Sub Type|string|None|False|Event sub type|None|
|Event Timestamp|integer|None|False|Event timestamp|None|
|Event Type|string|None|False|Event type|None|
|FW App Category|string|None|False|FW app category|None|
|FW App ID|string|None|False|FW app ID|None|
|FW App Subcategory|string|None|False|FW app subcategory|None|
|FW App Technology|string|None|False|FW app technology|None|
|FW Device Name|string|None|False|FW device name|None|
|FW Email Recipient|string|None|False|FW email recipient|None|
|FW Email Sender|string|None|False|FW email sender|None|
|FW Email Subject|string|None|False|FW email subject|None|
|FW Interface From|string|None|False|FW interface from|None|
|FW Interface To|string|None|False|FW interface to|None|
|FW Is Phishing|string|None|False|FW is phishing|None|
|FW Misc|string|None|False|FW misc|None|
|FW Rule|string|None|False|FW rule|None|
|FW Rule ID|string|None|False|FW rule ID|None|
|FW Serial Number|string|None|False|FW serial number|None|
|FW URL Domain|string|None|False|FW URL domain|None|
|FW VSYS|string|None|False|FW VSYS|None|
|FW XFF|string|None|False|FW XFF|None|
|Image Name|string|None|False|Image name|None|
|Module ID|string|None|False|Module ID|None|
|OS Actor Causality ID|string|None|False|OS actor causality ID|None|
|OS Actor Effective Username|string|None|False|OS actor effective username|None|
|OS Actor Process Causality ID|string|None|False|OS actor process causality ID|None|
|OS Actor Process Command Line|string|None|False|OS actor process command line|None|
|OS Actor Process Image Name|string|None|False|OS actor process image name|None|
|OS Actor Process Image Path|string|None|False|OS actor process image path|None|
|OS Actor Process Image SHA256|string|None|False|OS actor process image SHA256|None|
|OS Actor Process Instance ID|string|None|False|OS actor process instance ID|None|
|OS Actor Process OS PID|string|None|False|OS actor process OS PID|None|
|OS Actor Process Signature Status|string|None|False|OS actor process signature status|None|
|OS Actor Process Signature Vendor|string|None|False|OS actor process signature vendor|None|
|OS Actor Thread Thread ID|string|None|False|OS actor thread thread ID|None|
|Story ID|string|None|False|Story ID|None|
|User Name|string|None|False|User name|None|
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|Action|None|
|Action Pretty|string|None|False|Action pretty|None|
|Agent Data Collection Status|boolean|None|False|Agent data collection status|None|
|Agent Device Domain|string|None|False|Agent device domain|None|
|Agent FQDN|string|None|False|Agent FQDN|None|
|Agent OS Sub Type|string|None|False|Agent OS sub type|None|
|Agent OS Type|string|None|False|Agent OS type|None|
|Agent Version|string|None|False|Agent version|None|
|Alert ID|string|None|False|Alert ID|None|
|Attempt Counter|string|None|False|Attempt counter|None|
|BIOC Category Enum Key|string|None|False|BIOC category enum key|None|
|BIOC Indicator|string|None|False|BIOC indicator|None|
|Category|string|None|False|Category|None|
|Deduplicate Tokens|string|None|False|Deduplicate tokens|None|
|Description|string|None|False|Description|None|
|Detection Timestamp|integer|None|False|Detection timestamp|None|
|End Match Attempt TS|string|None|False|End match attempt TS|None|
|Endpoint ID|string|None|False|Endpoint ID|None|
|Events|[]event|None|False|Events|None|
|External ID|string|None|False|External ID|None|
|Filter Rule ID|string|None|False|Filter rule ID|None|
|Host IP|[]string|None|False|Host IP|None|
|Host Name|string|None|False|Host name|None|
|Is Whitelisted|boolean|None|False|Is whitelisted|None|
|Local Insert TS|integer|None|False|Local insert TS|None|
|MAC|string|None|False|MAC|None|
|MAC Addresses|[]string|None|False|MAC addresses|None|
|Matching Service Rule ID|string|None|False|Matching service rule ID|None|
|Matching Status|string|None|False|Matching status|None|
|MITRE Tactic ID And Name|[]string|None|False|MITRE tactic ID and name|None|
|MITRE Technique ID And Name|[]string|None|False|MITRE technique ID and name|None|
|Name|string|None|False|Name|None|
|Severity|string|None|False|Severity|None|
|Source|string|None|False|Source|None|
|Starred|boolean|None|False|Starred|None|
  
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

* Isolate Endpoint fails with 500 error - This will happen if an isolation action (Isolate or Unisolate) is in progress on the selected endpoint. Wait a few minutes and try again. 

# Version History

* 3.0.0 - Updated `hosts` output of `Get Incident` trigger and `Monitor Incident Events` task to separate host values
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
