# Description

[Trend Micro Deep Security](https://www.trendmicro.com/en_us/business/products/hybrid-cloud/deep-security.html) is an endpoint protection software with multiple modules such as Anti-Virus, Intrusion Prevention (Virtual Patching), Integrity Monitoring and more.

# Key Features

* Utilize the Deep Security IPS engine to protect against vulnerabilities without installing a patch (virtual patching)

# Requirements

* Trend Micro Deep Security

# Supported Product Versions

* 2024-11-1

# Documentation

## Setup

* [Create an API key for Deep Security](https://help.deepsecurity.trendmicro.com/api-key.html)
* Create a new connection and enter the Deep Security Manager URL and API key

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|dsm_api_key|credential_secret_key|None|True|API key of the Deep Security Manager|None|12345678-ABCD-1234-ABCD-123456789012:ABCDEFGH-1234-ABCD-1234-ABCDEFGHIJKL:12345678901234567890123456789012345678901234|None|None|
|dsm_url|string|https://app.deepsecurity.trendmicro.com|True|URL of the Deep Security Manager|None|https://192.51.100.100:4119|None|None|
|dsm_verify_ssl|boolean|True|True|Check the certificate of the Deep Security Manager|None|True|None|None|

Example input:

```
{
  "dsm_api_key": "12345678-ABCD-1234-ABCD-123456789012:ABCDEFGH-1234-ABCD-1234-ABCDEFGHIJKL:12345678901234567890123456789012345678901234",
  "dsm_url": "https://192.51.100.100:4119",
  "dsm_verify_ssl": true
}
```

## Technical Details

### Actions


#### Deploy

This action is used to deploy IPS rules

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|computer_or_policy|string|None|True|Target for rule assignment|["computer", "policy"]|policy|None|None|
|id|integer|None|True|ID of the target computer or policy|None|23|None|None|
|rules|[]integer|None|True|IPS rules to assign|None|[108, 6745, 2874, 2875, 2876, 3317, 3318]|None|None|
  
Example input:

```
{
  "computer_or_policy": "policy",
  "id": 23,
  "rules": [
    108,
    6745,
    2874,
    2875,
    2876,
    3317,
    3318
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|rules_assigned|[]integer|False|All IPS rules currently assigned|None|
|rules_not_assigned|[]integer|False|Unassigned IPS rules|None|
  
Example output:

```
{
  "rules_assigned": [
    108,
    2874,
    2875,
    2876,
    3118,
    3124,
    3125,
    3126,
    3317,
    3318,
    4593,
    5177,
    5892,
    6348,
    6745
  ],
  "rules_not_assigned": []
}
```

#### Get Details

This action is used to get detailed information of an IPS rule

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|IPS rule|None|2874|None|None|
  
Example input:

```
{
  "id": 2874
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|cves|[]string|False|List of related CVEs|None|
|cvss_score|string|False|CVSS score|5.0|
|description|string|False|Description of the rule|The TLS and DTLS implementations in OpenSSL do not properly handle Heartbeat Extension packets, which allow remote attackers to obtain sensitive information from process memory via crafted packets. This is a heuristic based rule to identify such suspicious Heartbeat requests.|
|name|string|False|Name of the rule|Identified Suspicious OpenSSL TLS/DTLS Heartbeat Request (ATT\u0026CK T1032)|
|response_json|object|False|Full response in JSON format|None|
|severity|string|False|Severity level of the IPS rule|medium|
|type|string|False|Rule type|smart|
  
Example output:

```
{
  "cves": [
    "CVE-2014-0160"
  ],
  "cvss_score": "5.00",
  "description": "The TLS and DTLS implementations in OpenSSL do not properly handle Heartbeat Extension packets, which allow remote attackers to obtain sensitive information from process memory via crafted packets. This is a heuristic based rule to identify such suspicious Heartbeat requests.",
  "name": "Identified Suspicious OpenSSL TLS/DTLS Heartbeat Request (ATT\u0026CK T1032)",
  "response_json": {
    "CVE": [
      "CVE-2014-0160"
    ],
    "CVSSScore": "5.00",
    "ID": 2874,
    "alertEnabled": false,
    "alwaysIncludePacketData": false,
    "applicationTypeID": 282,
    "canBeAssignedAlone": true,
    "debugModeEnabled": false,
    "description": "The TLS and DTLS implementations in OpenSSL do not properly handle Heartbeat Extension packets, which allow remote attackers to obtain sensitive information from process memory via crafted packets. This is a heuristic based rule to identify such suspicious Heartbeat requests.",
    "detectOnly": false,
    "eventLoggingDisabled": false,
    "generateEventOnPacketDrop": true,
    "identifier": "1006012",
    "lastUpdated": 1569346920000,
    "name": "Identified Suspicious OpenSSL TLS/DTLS Heartbeat Request (ATT\u0026CK T1032)",
    "originalIssue": 1396962540000,
    "priority": "normal",
    "severity": "medium",
    "type": "smart"
  },
  "severity": "medium",
  "type": "smart"
}
```

#### List

This action is used to list IPS rules

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the computer or policy|None|23|None|None|
|scope|string|None|True|Set the scope|["computer", "policy"]|policy|None|None|
  
Example input:

```
{
  "id": 23,
  "scope": "policy"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|covered_cves|[]string|False|CVEs covered by the assigned rules|None|
|response_json|object|False|Full response in JSON format|None|
|rules_assigned|[]integer|False|All IPS rules currently assigned|None|
  
Example output:

```
{
  "rules_assigned": [
    108,
    2874,
    2875,
    2876,
    3317,
    3318,
    6348
  ],
  "rules_not_recommended": [],
  "rules_recommended": []
}
```

#### Search Computers

This action is used to search computers

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|field_name|string|hostName|False|Name of the field to be tested|None|hostName|None|None|
|information|string|none|True|Determines the computer information to include in the response|["none", "all", "computerStatus", "tasks", "securityUpdates", "computerSettings", "allSecurityModules", "antiMalware", "webReputation", "activityMonitoring", "firewall", "intrusionPrevention", "integrityMonitoring", "logInspection", "applicationControl", "SAP", "interfaces", "ESXSummary", "allVirtualMachineSummaries", "azureARMVirtualMachineSummary", "azureVMVirtualMachineSummary", "ec2VirtualMachineSummary", "noConnectorVirtualMachineSummary", "vmwareVMVirtualMachineSummary", "vcloudVMVirtualMachineSummary", "workspaceVirtualMachineSummary", "gcpVirtualMachineSummary"]|none|None|None|
|max_items|integer|5000|True|Limits the number of objects returned|None|5000|None|None|
|number_value|integer|0|False|Number to search for|None|42|None|None|
|search_type|string|string|False|Select the search type|["string", "integer"]|string|None|None|
|string_value|string||False|String to search for|None|MS-AD-SRV-%|None|None|
  
Example input:

```
{
  "field_name": "hostName",
  "information": "none",
  "max_items": 5000,
  "number_value": "42",
  "search_type": "string",
  "string_value": "MS-AD-SRV-%"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|computer_ids|[]integer|False|IDs of matching computers|None|
|response_json|object|False|Full response in JSON format|None|
  
Example output:

```
{
  "computer_ids": [
    34
  ],
  "response_json": {
    "computers": [
      {
        "agentVersion": "11.3.0.292",
        "displayName": "",
        "hostName": "MS-AD-SRV-01",
        "policyID": 45,
        "agentFingerPrint": "14:F3:B3:76:1F:8A:2F:8B:D6:D9:DC:A4:3D:A0:F1:D4:A4...",
        "groupID": 0,
        "hostGUID": "14483D21-D921-32E0-19D7-FA36D91BC46E",
        "relayListID": 0,
        "biosUUID": "175bd693-216e-1e42-a489-2b56f1saf392",
        "description": "",
        "lastIPUsed": "192.0.2.10",
        "platform": "",
        "ID": 34,
        "lastAgentCommunication": 1585228384309
      }
    ]
  }
}
```

#### Search

Search for matching IPS rules in Deep Security by CVE ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|vulnerabilities|[]string|None|True|CVEs to protect against|None|["CVE-2005-0045", "CVE-2014-0160", "CVE-2017-0144", "CVE-1337-1337"]|None|None|
  
Example input:

```
{
  "vulnerabilities": [
    "CVE-2005-0045",
    "CVE-2014-0160",
    "CVE-2017-0144",
    "CVE-1337-1337"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ips_rules|[]integer|False|IPS rules matching the given CVEs|None|
|matched_cves|[]string|False|CVEs with at least one matching IPS rule|None|
|missed_cves|[]string|False|CVEs without matching IPS rules|None|
  
Example output:

```
{
  "ips_rules": [
    108,
    6348,
    3317,
    3318,
    2874,
    2875,
    2876
  ],
  "matched_cves": [
    "CVE-2005-0045",
    "CVE-2017-0144",
    "CVE-2014-0160"
  ],
  "missed_cves": [
    "CVE-1337-1337"
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.2.3 - Bumping requirements.txt | SDK bump to 6.1.4
* 2.2.2 - Fixed memory leak
* 2.2.1 - Improve the search for IPS rules
* 2.2.0 - Add new action Search Computers to receive a list and details of computers matching the search criteria
* 2.1.0 - Add new actions Get Details and List to receive assigned IPS rules from computers and policies
* 2.0.0 - Add an option to toggle DSM certificate verification in the connection
* 1.0.0 - Initial plugin

# Links

* [Trend Micro Deep Security](https://www.trendmicro.com/en_gb/business/products/hybrid-cloud/deep-security.html)

## References

* [Trend Micro Deep Security](https://help.deepsecurity.trendmicro.com/10/0/rest-api.html)