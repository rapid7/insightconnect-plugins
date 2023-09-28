# Description

The Windows Defender Advanced Threat Protection plugin allows Rapid7 InsightConnect users to quickly take remediation actions across their organization. This plugin can isolate machines, run virus scans, and quarantine files

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
* 2022-05-20

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|application_id|string|None|True|Application (client) ID|None|a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d|
|application_secret|credential_secret_key|None|True|Application secret|None|kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=|
|directory_id|string|None|True|Directory (tenant) ID|None|3a522933-ae5e-2b63-96ab-3c004b4f7f10|
  
Example input:

```
{
  "application_id": "a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d",
  "application_secret": "kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=",
  "directory_id": "3a522933-ae5e-2b63-96ab-3c004b4f7f10"
}
```

## Technical Details

### Actions


#### Blacklist
  
Submit or update new indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|AlertAndBlock|False|The action that will be taken if the indicator will be discovered in the organization|['Alert', 'AlertAndBlock', 'Allowed']|AlertAndBlock|
|application|string|None|False|The application associated with the indicator|None|demo-test|
|description|string|Indicator Blacklisted from InsightConnect|False|Description of the indicator|None|Indicator Blacklisted from InsightConnect|
|expiration_time|string|None|False|The expiration time of the indicator, default value is one year from now|None|2020-12-12T00:00:00Z|
|indicator|string|None|True|A supported indicator to blacklist or unblacklist. Supported indicators are IP addresses, URLs, domains, and SHA1 and SHA256 hashes|None|220e7d15b011d7fac48f2bd61114db1022197f7f|
|indicator_state|boolean|False|False|True to add indicator, false to remove it from the list|None|True|
|rbac_group_names|[]string|None|False|List of RBAC group names the indicator would be applied to|None|["group1","group2"]|
|recommended_actions|string|None|False|TI indicator alert recommended actions|None|nothing|
|severity|string|High|False|The severity of the indicator|['Informational', 'Low', 'Medium', 'High']|High|
|title|string|None|False|Indicator alert title|None|test|
  
Example input:

```
{
  "action": "AlertAndBlock",
  "application": "demo-test",
  "description": "Indicator Blacklisted from InsightConnect",
  "expiration_time": "2020-12-12T00:00:00Z",
  "indicator": "220e7d15b011d7fac48f2bd61114db1022197f7f",
  "indicator_state": false,
  "rbac_group_names": [
    "group1",
    "group2"
  ],
  "recommended_actions": "nothing",
  "severity": "High",
  "title": "test"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|indicator_action_response|indicator_action|False|A response that includes the result of the action, and supplemental information about the action taken|None|
  
Example output:

```
{
  "indicator_action_response": {
    "@Odata.Context": "",
    "Action": {},
    "Application": {},
    "Created By": {},
    "Created By Display Name": {},
    "Created By Source": {},
    "Creation Time": {},
    "Description": {},
    "Expiration Time": {},
    "Generate Alert": "true",
    "Historical Detection": {},
    "Indicator ID": {},
    "Indicator Type": {},
    "Indicator Value": {},
    "Last Update Time": {},
    "Last Updated By": {},
    "MITRE Techniques": [
      {}
    ],
    "RBAC Group IDs": {},
    "RBAC Group Names": {},
    "Recommended Actions": {},
    "Severity": {},
    "Source": {},
    "Source Type": {},
    "Title": {}
  }
}
```

#### Collect Investigation Package
  
Collects investigation package from a machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|Investigation package collected via InsightConnect|False|Comment to associate with the action|None|Investigation package collected via InsightConnect|
|machine|string|None|True|Machine IP address, hostname, or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
  
Example input:

```
{
  "comment": "Investigation package collected via InsightConnect",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|collect_investigation_package_response|machine_action|True|A response that includes information about the action taken|None|
  
Example output:

```
{
  "collect_investigation_package_response": {
    "Creation Date Time UTC": "",
    "Error HResult": 0,
    "ID": {},
    "Last Update Date Time UTC": {},
    "Machine ID": {},
    "Requestor": {},
    "Requestor Comment": {},
    "Status": {}
  }
}
```

#### Find Machines with Installed Software
  
Retrieve a list of device references that have specific software installed

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|software|string|None|True|Name of the software to be searched|None|microsoft-_-edge|
  
Example input:

```
{
  "software": "microsoft-_-edge"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machines|[]machine_software|True|List of machines with provided software|None|
  
Example output:

```
{
  "machines": [
    {
      "Computer DNS Name": {},
      "ID": "",
      "OS Platform": {},
      "RBAC Group ID": 0,
      "RBAC Group Name": {}
    }
  ]
}
```

#### Get Files from Alert
  
Retrieve a list of file information objects related to an alert

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|Alert ID to get files from|None|da637293198146839977_2089064327|
  
Example input:

```
{
  "alert_id": "da637293198146839977_2089064327"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file_list|[]file_type|True|The file ID related to the given alert ID|None|
  
Example output:

```
{
  "file_list": [
    {
      "Determination Type": {},
      "Determination Value": {},
      "File Product Name": {},
      "File Publisher": {},
      "File Type": {},
      "Global First Observed": {},
      "Global Last Observed": {},
      "Global Prevalence": 0,
      "Is PE File": "true",
      "Is Valid Certificate": {},
      "Issuer": {},
      "MD5": {},
      "SHA1": "",
      "SHA256": {},
      "Signer": {},
      "Signer Hash": {},
      "Size": {}
    }
  ]
}
```

#### Get Installed Software
  
Retrieves a collection of installed software related to a given machine IP address, hostname, or machine ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname, or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|software|[]software|True|List of installed software on the machine|None|
  
Example output:

```
{
  "software": [
    {
      "Active Alert": "true",
      "Exposed Machines": 0,
      "ID": "",
      "Impact Score": 0.0,
      "Name": {},
      "Public Exploit": {},
      "Vendor": {},
      "Weaknesses": {}
    }
  ]
}
```

#### Get Machine Action
  
Retrieve details about an action taken on a machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action_id|string|None|True|Action ID|None|ffd1f0cb-68ad-44ea-bf90-d01061b965ec|
  
Example input:

```
{
  "action_id": "ffd1f0cb-68ad-44ea-bf90-d01061b965ec"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine_action_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|None|
  
Example output:

```
{
  "machine_action_response": {
    "Creation Date Time UTC": "",
    "Error HResult": 0,
    "ID": {},
    "Last Update Date Time UTC": {},
    "Machine ID": {},
    "Requestor": {},
    "Requestor Comment": {},
    "Status": {}
  }
}
```

#### Get Machine Information
  
Get details about a machine with its ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine|machine|True|Machine information|None|
  
Example output:

```
{
  "machine": {
    "Agent Version": "",
    "Computer DNS Name": {},
    "Exposure Level": {},
    "First Seen": {},
    "Health Status": {},
    "ID": {},
    "Last External IP Address": {},
    "Last IP Address": {},
    "Last Seen": {},
    "Machine Tags": [
      {}
    ],
    "OS Build": 0,
    "OS Platform": {},
    "OS Processor": {},
    "RBAC Group ID": {},
    "Risk Score": {},
    "Version": {}
  }
}
```

#### Get Machine Vulnerabilities
  
Retrieves a collection of discovered vulnerabilities related to a given device

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname or machine ID|None|9de5069c5afe602b2ea0a04b66beb2c0cef77fdf|
  
Example input:

```
{
  "machine": "9de5069c5afe602b2ea0a04b66beb2c0cef77fdf"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerabilities|[]vulnerability|True|List of vulnerabilities of the machine|None|
  
Example output:

```
{
  "vulnerabilities": [
    {
      "CVSS V3": 0.0,
      "Description": "",
      "Exploit In Kit": "true",
      "Exploit Types": [
        {}
      ],
      "Exploit URIs": {},
      "Exploit Verified": {},
      "Exposed Machines": 0,
      "ID": {},
      "Name": {},
      "Public Exploit": {},
      "Published On": {},
      "Severity": {},
      "Updated On": {}
    }
  ]
}
```

#### Get Missing Software Updates
  
Retrieve a list of software updates

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|updates|[]update|True|List of updates|None|
  
Example output:

```
{
  "updates": [
    {
      "CVE Addressed": {},
      "ID": "",
      "Machine Missed On": {},
      "Name": {},
      "OS Build": 0,
      "Products Names": [
        {}
      ],
      "URL": {}
    }
  ]
}
```

#### Get Related Machines
  
Get machines related to an file hash(SHA1), domain or username indicator

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|indicator|string|None|True|File hash(SHA1), domain or username indicator|None|example.com|
  
Example input:

```
{
  "indicator": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machines|[]machine|True|Machines related to an file hash(SHA1), domain or username indicator|None|
  
Example output:

```
{
  "machines": [
    {
      "Agent Version": "",
      "Computer DNS Name": {},
      "Exposure Level": {},
      "First Seen": {},
      "Health Status": {},
      "ID": {},
      "Last External IP Address": {},
      "Last IP Address": {},
      "Last Seen": {},
      "Machine Tags": [
        {}
      ],
      "OS Build": 0,
      "OS Platform": {},
      "OS Processor": {},
      "RBAC Group ID": {},
      "Risk Score": {},
      "Version": {}
    }
  ]
}
```

#### Get Security Recommendations
  
Retrieve a list of security recommendations

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|recommendations|[]recommendation|True|List of security recommendations|None|
  
Example output:

```
{
  "recommendations": [
    {
      "Active Alert": "true",
      "Associated Threats": [
        ""
      ],
      "Config Score Impact": 0.0,
      "Exposed Machines Count": 0,
      "Exposure Impact": {},
      "ID": {},
      "Non Productivity Impacted Assets": {},
      "Product Name": {},
      "Public Exploit": {},
      "Recommendation Category": {},
      "Recommendation Name": {},
      "Related Component": {},
      "Remediation Type": {},
      "Severity Score": {},
      "Status": {},
      "Total Machine Count": {},
      "Vendor": {},
      "Weaknesses": {}
    }
  ]
}
```

#### Isolate Machine
  
Isolate a machine from the network

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment to associate with the isolation action|None|Isolated by InsightConnect|
|isolation_type|string|None|True|Type of isolation to perform on target machine|['Full', 'Selective']|Full|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
  
Example input:

```
{
  "comment": "Isolated by InsightConnect",
  "isolation_type": "Full",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine_isolation_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|None|
  
Example output:

```
{
  "machine_isolation_response": {
    "Creation Date Time UTC": "",
    "Error HResult": 0,
    "ID": {},
    "Last Update Date Time UTC": {},
    "Machine ID": {},
    "Requestor": {},
    "Requestor Comment": {},
    "Status": {}
  }
}
```

#### Manage Tags
  
Add or remove machine tags

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|machine|string|None|True|Machine IP address, hostname, or machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
|tag|string|None|True|The tag value|None|example tag|
|type|boolean|True|True|True to add tag, false to remove it|None|True|
  
Example input:

```
{
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
  "tag": "example tag",
  "type": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|manage_tags_response|manage_tags_response|True|A response that includes updated tags and supplemental information about the machine|None|
  
Example output:

```
{
  "manage_tags_response": {
    "@Odata.Context": "",
    "Agent Version": {},
    "Computer DNS Name": {},
    "Device Value": {},
    "Exposure Level": {},
    "First Seen": {},
    "Health Status": {},
    "ID": {},
    "Is AAD Joined": "true",
    "Last External IP Address": {},
    "Last IP Address": {},
    "Last Seen": {},
    "Machine Tags": [
      {}
    ],
    "OS Build": 0,
    "OS Platform": {},
    "OS Processor": {},
    "RBAC Group ID": {},
    "Risk Score": {},
    "Version": {}
  }
}
```

#### Run Antivirus Scan
  
Initiate a Windows Defender Antivirus scan on a machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment to associate with the antivirus scan action|None|InsightConnect has started an antivirus scan.|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
|scan_type|string|None|True|The type of antivirus scan to run|['Full', 'Quick']|Full|
  
Example input:

```
{
  "comment": "InsightConnect has started an antivirus scan.",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
  "scan_type": "Full"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine_action_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|None|
  
Example output:

```
{
  "machine_action_response": {
    "Creation Date Time UTC": "",
    "Error HResult": 0,
    "ID": {},
    "Last Update Date Time UTC": {},
    "Machine ID": {},
    "Requestor": {},
    "Requestor Comment": {},
    "Status": {}
  }
}
```

#### Stop and Quarantine File
  
Stop the execution of a file on a machine and delete it

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment to associate with the stop and quarantine action|None|InsightConnect has stopped a file.|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
|sha1|string|None|True|SHA1 hash of the file to stop and quarantine on the machine|None|ad0c0f2fa80411788e81a4567d1d8758b83cd76e|
  
Example input:

```
{
  "comment": "InsightConnect has stopped a file.",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73",
  "sha1": "ad0c0f2fa80411788e81a4567d1d8758b83cd76e"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|stop_and_quarantine_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|None|
  
Example output:

```
{
  "stop_and_quarantine_response": {
    "Creation Date Time UTC": "",
    "Error HResult": 0,
    "ID": {},
    "Last Update Date Time UTC": {},
    "Machine ID": {},
    "Requestor": {},
    "Requestor Comment": {},
    "Status": {}
  }
}
```

#### Unisolate Machine
  
Restore network connectivity to a machine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment to associate with the unisolate action|None|Unisolated by InsightConnect|
|machine|string|None|True|Machine IP address, hostname and machine ID|None|2df36d707c1ee5084cef77f3dbfc95db65bc4a73|
  
Example input:

```
{
  "comment": "Unisolated by InsightConnect",
  "machine": "2df36d707c1ee5084cef77f3dbfc95db65bc4a73"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|machine_isolation_response|machine_action|True|A response that includes the result of the action, and supplemental information about the action taken|None|
  
Example output:

```
{
  "machine_isolation_response": {
    "Creation Date Time UTC": "",
    "Error HResult": 0,
    "ID": {},
    "Last Update Date Time UTC": {},
    "Machine ID": {},
    "Requestor": {},
    "Requestor Comment": {},
    "Status": {}
  }
}
```
### Triggers


#### Get Alerts Matching Key
  
Get alerts that match a given key to its value

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|10|False|Poll frequency in seconds|None|10|
|key|string|None|True|The key to look for in the alert. This key must match the case shown in the example output section in help|None|assignedTo|
|value|string|None|True|The value to look for in the alert. The value must match the case of the value returned|None|user@example.com|
  
Example input:

```
{
  "frequency": 10,
  "key": "assignedTo",
  "value": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert|True|An alert that contains the given key and matching value|None|
  
Example output:

```
{
  "alert": {
    "AAD Tenant ID": {},
    "Alert Creation Time": {},
    "Assigned To": {},
    "Category": {},
    "Classification": {},
    "Computer DNS Name": {},
    "Description": {},
    "Detection Source": {},
    "Determination": {},
    "Evidence": [
      {
        "AAD User ID": {},
        "Account Name": {},
        "Detection Status": {},
        "Domain Name": {},
        "Entity Type": {},
        "Evidence Creation Time": {},
        "File Name": {},
        "File Path": {},
        "IP Address": {},
        "Parent Process Creation Time": {},
        "Parent Process File Name": {},
        "Parent Process File Path": {},
        "Parent Process ID": {},
        "Process Command Line": {},
        "Process Creation Time": {},
        "Process ID": {},
        "Registry Hive": {},
        "Registry Key": {},
        "Registry Value": {},
        "Registry Value Type": {},
        "SHA1": {},
        "SHA256": {},
        "URL": {},
        "User Principal Name": {},
        "User SID": {}
      }
    ],
    "First Event Time": {},
    "ID": "",
    "Incident ID": 0,
    "Investigation ID": {},
    "Investigation State": {},
    "Last Event Time": {},
    "Last Update Time": {},
    "Machine ID": {},
    "RBAC Group Name": {},
    "Related User": {
      "Domain Name": {},
      "User Name": {}
    },
    "Resolved Time": {},
    "Severity": {},
    "Status": {},
    "Threat Family Name": {},
    "Title": {}
  }
}
```

#### Get Alerts
  
Return all new alerts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|10|False|Poll frequency in seconds|None|10|
  
Example input:

```
{
  "frequency": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert|True|Alert|None|
  
Example output:

```
{
  "alert": {
    "AAD Tenant ID": {},
    "Alert Creation Time": {},
    "Assigned To": {},
    "Category": {},
    "Classification": {},
    "Computer DNS Name": {},
    "Description": {},
    "Detection Source": {},
    "Determination": {},
    "Evidence": [
      {
        "AAD User ID": {},
        "Account Name": {},
        "Detection Status": {},
        "Domain Name": {},
        "Entity Type": {},
        "Evidence Creation Time": {},
        "File Name": {},
        "File Path": {},
        "IP Address": {},
        "Parent Process Creation Time": {},
        "Parent Process File Name": {},
        "Parent Process File Path": {},
        "Parent Process ID": {},
        "Process Command Line": {},
        "Process Creation Time": {},
        "Process ID": {},
        "Registry Hive": {},
        "Registry Key": {},
        "Registry Value": {},
        "Registry Value Type": {},
        "SHA1": {},
        "SHA256": {},
        "URL": {},
        "User Principal Name": {},
        "User SID": {}
      }
    ],
    "First Event Time": {},
    "ID": "",
    "Incident ID": 0,
    "Investigation ID": {},
    "Investigation State": {},
    "Last Event Time": {},
    "Last Update Time": {},
    "Machine ID": {},
    "RBAC Group Name": {},
    "Related User": {
      "Domain Name": {},
      "User Name": {}
    },
    "Resolved Time": {},
    "Severity": {},
    "Status": {},
    "Threat Family Name": {},
    "Title": {}
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**manage_tags_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|@Odata.Context|string|None|False|@odata.context|None|
|Agent Version|string|None|False|Agent version|None|
|Computer DNS Name|string|None|False|Computer DNS name|None|
|Device Value|string|None|False|Device value|None|
|Exposure Level|string|None|False|Exposure level|None|
|First Seen|string|None|False|First seen|None|
|Health Status|string|None|False|Health status|None|
|ID|string|None|False|ID|None|
|Is AAD Joined|boolean|None|False|Is AAD joined|None|
|Last External IP Address|string|None|False|Last external IP address|None|
|Last IP Address|string|None|False|Last IP address|None|
|Last Seen|string|None|False|Last seen|None|
|Machine Tags|[]string|None|False|Machine tags|None|
|OS Build|integer|None|False|OS build|None|
|OS Platform|string|None|False|OS platform|None|
|OS Processor|string|None|False|OS Processor|None|
|RBAC Group ID|integer|None|False|RBAC group ID|None|
|Risk Score|string|None|False|Risk score|None|
|Version|string|None|False|Version|None|
  
**software**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active Alert|boolean|None|False|Active alert|None|
|Exposed Machines|integer|None|False|Exposed machines|None|
|ID|string|None|False|ID|None|
|Impact Score|float|None|False|Impact score|None|
|Name|string|None|False|Name|None|
|Public Exploit|boolean|None|False|Public exploit|None|
|Vendor|string|None|False|Vendor|None|
|Weaknesses|integer|None|False|Weaknesses|None|
  
**related_user_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Domain Name|string|None|False|Domain name|None|
|User Name|string|None|False|User name|None|
  
**evidence**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AAD User ID|string|None|False|Azure Active Directory User ID|None|
|Account Name|string|None|False|Account Name|None|
|Detection Status|string|None|False|Detection Status|None|
|Domain Name|string|None|False|Domain Name|None|
|Entity Type|string|None|False|Type of evidence|None|
|Evidence Creation Time|string|None|False|Creation time of evidence in ISO 8601 format|None|
|File Name|string|None|False|File Name|None|
|File Path|string|None|False|File Path|None|
|IP Address|string|None|False|IP Address|None|
|Parent Process Creation Time|string|None|False|Parent Process Creation Time in ISO 8601 format|None|
|Parent Process File Name|string|None|False|Parent Process File Name|None|
|Parent Process File Path|string|None|False|Parent Process File Path|None|
|Parent Process ID|integer|None|False|Parent process ID|None|
|Process Command Line|string|None|False|Process Command Line|None|
|Process Creation Time|string|None|False|Process Creation Time in ISO 8601 format|None|
|Process ID|integer|None|False|Process ID|None|
|Registry Hive|string|None|False|Registry Hive|None|
|Registry Key|string|None|False|A key-level node in the Windows registry|None|
|Registry Value|string|None|False|Registry Value|None|
|Registry Value Type|string|None|False|Registry Value Type|None|
|SHA1|string|None|False|SHA1 hash|None|
|SHA256|string|None|False|SHA256 hash|None|
|URL|string|None|False|URL|None|
|User Principal Name|string|None|False|User Principal Name|None|
|User SID|string|None|False|User Secrurity ID|None|
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AAD Tenant ID|string|None|False|AAD tenant ID|None|
|Alert Creation Time|string|None|False|Alert creation time|None|
|Assigned To|string|None|False|Assigned To|None|
|Category|string|None|False|Category|None|
|Classification|string|None|False|Classification|None|
|Computer DNS Name|string|None|False|Computer DNS name|None|
|Description|string|None|False|Description|None|
|Detection Source|string|None|False|Detection source|None|
|Determination|string|None|False|Determination|None|
|Evidence|[]evidence|None|False|List of related alert evidence|None|
|First Event Time|string|None|False|First event time|None|
|ID|string|None|False|ID|None|
|Incident ID|integer|None|False|Incident ID|None|
|Investigation ID|integer|None|False|Investigation ID|None|
|Investigation State|string|None|False|Investigation state|None|
|Last Event Time|string|None|False|Last event time|None|
|Last Update Time|string|None|False|Last update time|None|
|Machine ID|string|None|False|Machine ID|None|
|RBAC Group Name|string|None|False|RBAC group name|None|
|Related User|related_user_object|None|False|Related user|None|
|Resolved Time|string|None|False|Resolved time|None|
|Severity|string|None|False|Severity|None|
|Status|string|None|False|Status|None|
|Threat Family Name|string|None|False|Threat family name|None|
|Title|string|None|False|Title|None|
  
**file_type**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Determination Type|string|None|False|Determination type|None|
|Determination Value|string|None|False|Determination value|None|
|File Product Name|string|None|False|File product name|None|
|File Publisher|string|None|False|File publisher|None|
|File Type|string|None|False|File type|None|
|Global First Observed|string|None|False|Global first observed|None|
|Global Last Observed|string|None|False|Global last observed|None|
|Global Prevalence|integer|None|False|Global prevalence|None|
|Is PE File|boolean|None|False|Is PE File|None|
|Is Valid Certificate|boolean|None|False|Is valid certificate|None|
|Issuer|string|None|False|Issuer|None|
|MD5|string|None|False|MD5|None|
|SHA1|string|None|False|SHA1|None|
|SHA256|string|None|False|SHA256|None|
|Signer|string|None|False|Signer|None|
|Signer Hash|string|None|False|Signer hash|None|
|Size|integer|None|False|Size|None|
  
**machine_software**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Computer DNS Name|string|None|False|Computer DNS name|None|
|ID|string|None|False|ID|None|
|OS Platform|string|None|False|OS platform|None|
|RBAC Group ID|number|None|False|RBAC group ID|None|
|RBAC Group Name|string|None|False|RBAC group name|None|
  
**machine**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Version|string|None|False|Agent version|None|
|Computer DNS Name|string|None|False|Computer DNS name|None|
|Exposure Level|string|None|False|Exposure level|None|
|First Seen|string|None|False|First seen|None|
|Health Status|string|None|False|Health status|None|
|ID|string|None|False|ID|None|
|Last External IP Address|string|None|False|Last external IP address|None|
|Last IP Address|string|None|False|Last IP address|None|
|Last Seen|string|None|False|Last seen|None|
|Machine Tags|[]string|None|False|Machine Tags|None|
|OS Build|integer|None|False|OS build|None|
|OS Platform|string|None|False|OS platform|None|
|OS Processor|string|None|False|OS processor|None|
|RBAC Group ID|integer|None|False|RBAC group ID|None|
|Risk Score|string|None|False|Risk score|None|
|Version|string|None|False|Version|None|
  
**machine_action**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Creation Date Time UTC|string|None|False|Creation date time UTC|None|
|Error HResult|integer|None|False|Error HResult|None|
|ID|string|None|False|ID|None|
|Last Update Date Time UTC|string|None|False|Last update date time UTC|None|
|Machine ID|string|None|False|Machine ID|None|
|Requestor|string|None|False|Requestor|None|
|Requestor Comment|string|None|False|Requestor comment|None|
|Status|string|None|False|Status|None|
  
**indicator_action**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|@Odata.Context|string|None|False|@odata.context|None|
|Action|string|None|False|The action that will be taken if the indicator will be discovered in the organization|AlertAndBlock|
|Application|string|None|False|The application associated with the indicator|demo-test|
|Created By|string|None|False|Unique identity of the user/application that submitted the indicator|test|
|Created By Display Name|string|None|False|Created by display name|None|
|Created By Source|string|None|False|Created by source|None|
|Creation Time|string|None|False|The date and time when the indicator was created|None|
|Description|string|None|False|Description of the indicator|None|
|Expiration Time|string|None|False|The expiration time of the indicator|None|
|Generate Alert|boolean|None|False|Generate alert|None|
|Historical Detection|boolean|None|False|Historical detection|None|
|Indicator ID|string|None|False|Identity of the indicator entity|None|
|Indicator Type|string|None|False|Type of the indicator|Url|
|Indicator Value|string|None|False|The potentially malicious indicator of one of the following types: IP addresses, URLs, domains, and SHA1 and SHA256 hashes|None|
|Last Update Time|string|None|False|The last time the indicator was updated|None|
|Last Updated By|string|None|False|Identity of the user/application that last updated the indicator|None|
|MITRE Techniques|[]string|None|False|MITRE techniques|None|
|RBAC Group IDs|[]string|None|False|RBAC group IDs|None|
|RBAC Group Names|[]string|None|False|RBAC device group names where the indicator is exposed and active. Empty list in case it exposed to all devices|None|
|Recommended Actions|string|None|False|Recommended actions for the indicator|None|
|Severity|string|None|False|The severity of the indicator|None|
|Source|string|None|False|The name of the user/application that submitted the indicator|test|
|Source Type|string|None|False|User in case the Indicator created by a user (e.g. from the portal), AadApp in case it submitted using automated application via the API.|AadApp|
|Title|string|None|False|Indicator alert title|None|
  
**vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVSS V3|float|None|False|CVSS v3|None|
|Description|string|None|False|Description|None|
|Exploit In Kit|boolean|None|False|Exploit in kit|None|
|Exploit Types|[]string|None|False|Exploit types|None|
|Exploit URIs|[]string|None|False|Exploit URIs|None|
|Exploit Verified|boolean|None|False|Exploit verified|None|
|Exposed Machines|integer|None|False|Exposed machines|None|
|ID|string|None|False|ID|None|
|Name|string|None|False|Name|None|
|Public Exploit|boolean|None|False|Public exploit|None|
|Published On|string|None|False|Published on|None|
|Severity|string|None|False|Severity|None|
|Updated On|string|None|False|Updated on|None|
  
**recommendation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active Alert|boolean|None|False|Active alert|None|
|Associated Threats|[]string|None|False|Associated threats|None|
|Config Score Impact|float|None|False|Config score impact|None|
|Exposed Machines Count|integer|None|False|Exposed machines count|None|
|Exposure Impact|float|None|False|Exposure impact|None|
|ID|string|None|False|ID|None|
|Non Productivity Impacted Assets|integer|None|False|Non productivity impacted assets|None|
|Product Name|string|None|False|Product name|None|
|Public Exploit|boolean|None|False|Public exploit|None|
|Recommendation Category|string|None|False|Recommendation category|None|
|Recommendation Name|string|None|False|Recommendation name|None|
|Related Component|string|None|False|Related component|None|
|Remediation Type|string|None|False|Remediation type|None|
|Severity Score|float|None|False|Severity score|None|
|Status|string|None|False|Status|None|
|Total Machine Count|integer|None|False|Total machine count|None|
|Vendor|string|None|False|Vendor|None|
|Weaknesses|integer|None|False|Weaknesses|None|
  
**update**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVE Addressed|integer|None|False|Update CVE addressed|None|
|ID|string|None|False|Update ID|None|
|Machine Missed On|integer|None|False|Update machine missed on|None|
|Name|string|None|False|Update name|None|
|OS Build|integer|None|False|Update OS build|None|
|Products Names|[]string|None|False|Update products names|None|
|URL|string|None|False|Update URL|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 5.0.0 - Updated the SDK version | Cloud enabled | fixed bug when machine_id is used for find_first_machine
* 4.8.1 - Fixed a problem where some actions could not find the machine
* 4.8.0 - Add Evidence output for Get Alerts trigger and Get Alert Matching Key trigger
* 4.7.1 - Fix bug in Get Alerts trigger which caused trigger to crash
* 4.7.0 - Add new action Collect Investigation Package
* 4.6.0 - Add new actions Get Installed Software, Get Related Machines and Manage Tags
* 4.5.1 - Add `docs_url` to plugin spec with link to [plugin setup guide](https://docs.rapid7.com/insightconnect/microsoft-defender-ATP)
* 4.5.0 - Add new action Get Missing Software Updates
* 4.4.1 - Add validation MD5 hash in Blacklist action | Set default value for Title, Expiration Time and Description input in action Blacklist
* 4.4.0 - Add new action Get Security Recommendations
* 4.3.0 - Add new action Get Machine Vulnerabilities
* 4.2.0 - Add new action Blacklist
* 4.1.0 - Add new action Find Machines with Installed Software
* 4.0.0 - Add custom type to output in action Get Machine Information
* 3.0.0 - Move connection functions to their own util class | Changed `Exception` to `PluginException` | Added error handling around "Action already in progress" state in Isolate Machine, Unisolate Machine, Stop and Quarantine File, and Run Antivirus Scan actions | Rename `machine_id` to `machine` in machine-related actions to support hostnames and IP addresses in addition to machine IDs.
* 2.0.0 - Update to refactor connection and actions
* 1.5.1 - New spec and help.md format for the Extension Library
* 1.5.0 - Fix issue where triggers always returned a blank payload
* 1.4.0 - New trigger Get Alerts | New action Get Machine Action
* 1.3.0 - New actions Stop and Quarantine File and Run Antivirus Scan
* 1.2.0 - New action Get File IDs from Alert
* 1.1.0 - New actions Get Machine ID from Alert, Isolate Machine, and Unisolate Machine
* 1.0.0 - Initial plugin

# Links

* [Windows Defender ATP](https://www.microsoft.com/en-us/windowsforbusiness/windows-atp)
* [Windows Defender ATP API Start Page](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-atp/use-apis)
* [Windows Defender ATP API Endpoints](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-atp/exposed-apis-list)

## References

* [Windows Defender ATP](https://www.microsoft.com/en-us/windowsforbusiness/windows-atp)
* [Windows Defender ATP API Start Page](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-atp/use-apis)
* [Windows Defender ATP API Endpoints](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-atp/exposed-apis-list)
