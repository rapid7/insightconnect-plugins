# Description

Protect your Microsoft Office 365 and G-Suite environments with next-generation email security that uses the most advanced AI detection techniques to stop targeted phishing attacks

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
* abnormal-security API abx v1.4.2

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|URL|string|https://api.abnormalplatform.com|True|Abnormal Security URL|None|https://api.abnormalplatform.com|
|api_key|credential_secret_key|None|True|Abnormal Security API Key|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "URL": "https://api.abnormalplatform.com",
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions


#### Get Case Details
  
This action is used to get details of a case identified by Abnormal Security

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|case_id|string|None|True|A string representing the case|None|19377|
  
Example input:

```
{
  "case_id": 19377
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|case_details|case_details|True|Details of the requested case identified by Abnormal Security|{'caseId': '19377', 'severity': 'Potential Account Takeover', 'affectedEmployee': 'FirstName LastName', 'firstObserved': '2020-06-09T17:42:59Z'}|
  
Example output:

```
{
  "case_details": {
    "affectedEmployee": "FirstName LastName",
    "caseId": "19377",
    "firstObserved": "2020-06-09T17:42:59Z",
    "severity": "Potential Account Takeover"
  }
}
```

#### Get Cases
  
This action is used to get a list of up to 100 cases identified by Abnormal Security, if no input filter dates are 
provided, it will return up to 100 latest results

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter_key|string|lastModifiedTime|False|This input enables you to select what timestamp to filter on, default is lastModifiedTime|['lastModifiedTime', 'createdTime', 'customerVisableTime', '']|lastModifiedTime|
|from_date|string|None|False|This input enables you to filter your results from a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-01 21:11:38+00:00|
|to_date|string|None|False|This input enables you to filter your results to a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-11 21:11:38+00:00|
  
Example input:

```
{
  "filter_key": "lastModifiedTime",
  "from_date": "2021-03-01 21:11:38+00:00",
  "to_date": "2021-03-11 21:11:38+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|cases|[]case|True|A list of the top 100 cases identified in Abnormal Cases|[{"caseId": "19377", "severity": "Potential Account Takeover"}]|
  
Example output:

```
{
  "cases": {
    "caseId": "19377",
    "severity": "Potential Account Takeover"
  }
}
```

#### Get Threat Details
  
This action is used to get details of a threat identified by Abnormal Security

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|threat_id|string|None|True|A UUID representing the threat|None|184712ab-6d8b-47b3-89d3-a314efef79e2|
  
Example input:

```
{
  "threat_id": "184712ab-6d8b-47b3-89d3-a314efef79e2"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|threat_details|threat_details|True|Details of the requested threat identified by Abnormal Security|{'threatId': '184712ab-6d8b-47b3-89d3-a314efef79e2', 'messages': [{'threatId': '184712ab-6d8b-47b3-89d3-a314efef79e2', 'autoRemediated': True, 'postRemediated': False, 'attackType': 'Spam', 'attackStrategy': 'Unknown Sender', 'returnPath': 'user@example.com', 'senderIpAddress': '192.168.50.1', 'impersonatedParty': 'none / Others', 'attackVector': 'Link', 'summaryInsights': ['Abnormal Email Body HTML', 'Suspicious Link', 'Unusual Sender Domain', 'Abnormal Email SignOff', 'Unusual Sender'], 'remediationTimestamp': '2021-02-02T21:09:41Z', 'isRead': False, 'attackedParty': 'Other', 'abxMessageId': 1111111111111111113, 'abxPortalUrl': 'https://portal.abnormalsecurity.com/home/threat-center/remediation-history/1111111111111111113', 'subject': '[LIKELY PHISHING] Testing Myths', 'fromAddress': 'user@example.com', 'fromName': 'Test Example', 'toAddresses': 'user@example.com', 'receivedTime': '2021-02-02T21:09:37Z', 'sentTime': '2021-02-02T21:06:49Z', 'internetMessageId': '<user@example.com>', 'urls': ['https://example.com']}, {'threatId': '184712ab-6d8b-47b3-89d3-a314efef79e2', 'autoRemediated': False, 'postRemediated': True, 'attackType': 'Spam', 'attackStrategy': 'Name Impersonation', 'returnPath': 'user@example.com', 'senderIpAddress': '192.168.50.1', 'impersonatedParty': 'none / Others', 'attackVector': 'Link', 'summaryInsights': ['Abnormal Email Body HTML', 'Unusual Sender', 'Suspicious Link', 'Unusual Sender Domain'], 'remediationTimestamp': '2020-05-17T21:09:55Z', 'isRead': False, 'attackedParty': 'Employee (other)', 'abxMessageId': -1111111111111111112, 'abxPortalUrl': 'https://portal.abnormalsecurity.com/home/threat-center/remediation-history/-1111111111111111112', 'subject': '[LIKELY PHISHING] Testing Myths', 'fromAddress': 'user@example.com', 'fromName': 'Test Example', 'toAddresses': 'user@example.com', 'recipientAddress': 'user@example.com', 'receivedTime': '2020-05-17T21:09:51Z', 'sentTime': '2020-05-17T21:09:46Z', 'internetMessageId': '<user@example.com>', 'urls': ['https://example.com', 'https://example.com']}, {'threatId': '184712ab-6d8b-47b3-89d3-a314efef79e2', 'autoRemediated': False, 'postRemediated': False, 'attackType': 'Spam', 'attackStrategy': 'Name Impersonation', 'returnPath': 'user@example.com', 'senderIpAddress': '192.168.50.1', 'impersonatedParty': 'none / Others', 'attackVector': 'Link', 'summaryInsights': ['Abnormal Email Body HTML', 'Suspicious Link', 'Unusual Sender Domain', 'Unusual Sender'], 'attackedParty': 'Employee (other)', 'abxMessageId': -1111111111111111114, 'abxPortalUrl': 'https://portal.abnormalsecurity.com/home/threat-center/remediation-history/-1111111111111111114', 'subject': 'The Truth About 7 Myths', 'fromAddress': 'user@example.com', 'fromName': 'Test Example', 'toAddresses': 'user@example.com', 'recipientAddress': 'user@example.com', 'receivedTime': '2020-05-10T21:05:08Z', 'sentTime': '2020-05-10T21:05:03Z', 'internetMessageId': '<user@example.com>'}]}|
  
Example output:

```
{
  "threat_details": {
    "messages": [
      {
        "abxMessageId": 1111111111111111113,
        "abxPortalUrl": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/1111111111111111113",
        "attackStrategy": "Unknown Sender",
        "attackType": "Spam",
        "attackVector": "Link",
        "attackedParty": "Other",
        "autoRemediated": true,
        "fromAddress": "user@example.com",
        "fromName": "Test Example",
        "impersonatedParty": "none / Others",
        "internetMessageId": "<user@example.com>",
        "isRead": false,
        "postRemediated": false,
        "receivedTime": "2021-02-02T21:09:37Z",
        "remediationTimestamp": "2021-02-02T21:09:41Z",
        "returnPath": "user@example.com",
        "senderIpAddress": "192.168.50.1",
        "sentTime": "2021-02-02T21:06:49Z",
        "subject": "[LIKELY PHISHING] Testing Myths",
        "summaryInsights": [
          "Abnormal Email Body HTML",
          "Suspicious Link",
          "Unusual Sender Domain",
          "Abnormal Email SignOff",
          "Unusual Sender"
        ],
        "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2",
        "toAddresses": "user@example.com",
        "urls": [
          "https://example.com"
        ]
      },
      {
        "abxMessageId": -1111111111111111112,
        "abxPortalUrl": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/-1111111111111111112",
        "attackStrategy": "Name Impersonation",
        "attackType": "Spam",
        "attackVector": "Link",
        "attackedParty": "Employee (other)",
        "autoRemediated": false,
        "fromAddress": "user@example.com",
        "fromName": "Test Example",
        "impersonatedParty": "none / Others",
        "internetMessageId": "<user@example.com>",
        "isRead": false,
        "postRemediated": true,
        "receivedTime": "2020-05-17T21:09:51Z",
        "recipientAddress": "user@example.com",
        "remediationTimestamp": "2020-05-17T21:09:55Z",
        "returnPath": "user@example.com",
        "senderIpAddress": "192.168.50.1",
        "sentTime": "2020-05-17T21:09:46Z",
        "subject": "[LIKELY PHISHING] Testing Myths",
        "summaryInsights": [
          "Abnormal Email Body HTML",
          "Unusual Sender",
          "Suspicious Link",
          "Unusual Sender Domain"
        ],
        "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2",
        "toAddresses": "user@example.com",
        "urls": [
          "https://example.com",
          "https://example.com"
        ]
      },
      {
        "abxMessageId": -1111111111111111114,
        "abxPortalUrl": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/-1111111111111111114",
        "attackStrategy": "Name Impersonation",
        "attackType": "Spam",
        "attackVector": "Link",
        "attackedParty": "Employee (other)",
        "autoRemediated": false,
        "fromAddress": "user@example.com",
        "fromName": "Test Example",
        "impersonatedParty": "none / Others",
        "internetMessageId": "<user@example.com>",
        "postRemediated": false,
        "receivedTime": "2020-05-10T21:05:08Z",
        "recipientAddress": "user@example.com",
        "returnPath": "user@example.com",
        "senderIpAddress": "192.168.50.1",
        "sentTime": "2020-05-10T21:05:03Z",
        "subject": "The Truth About 7 Myths",
        "summaryInsights": [
          "Abnormal Email Body HTML",
          "Suspicious Link",
          "Unusual Sender Domain",
          "Unusual Sender"
        ],
        "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2",
        "toAddresses": "user@example.com"
      }
    ],
    "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2"
  }
}
```

#### Get Threats
  
This action is used to get a list of up to 100 threats identified in the Abnormal Security Threat Log, if no input 
filter dates are provided, it will return up to 100 latest results

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|from_date|string|None|False|This input enables you to filter your results from a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-01 21:11:38+00:00|
|to_date|string|None|False|This input enables you to filter your results to a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-11 21:11:38+00:00|
  
Example input:

```
{
  "from_date": "2021-03-01 21:11:38+00:00",
  "to_date": "2021-03-11 21:11:38+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|threats|[]threat|True|A list of the top 100 threats identified in Threat Log|[{"threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2"}]|
  
Example output:

```
{
  "threats": {
    "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2"
  }
}
```

#### Manage Case
  
This action is used to manage an Abnormal Case

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|True|Acknowledge or take another remediation action on a case|['Action Required', 'Acknowledge in Progress', 'Acknowledge Resolved', 'Acknowledge not an Attack']|Action Required|
|case_id|string|None|True|An ID representing the case|None|12345|
  
Example input:

```
{
  "action": "Action Required",
  "case_id": 12345
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|manage_case_response|True|Response containing the action ID and status URL|{'response': {'actionId': '61e76395-40d3-4d78-b6a8-8b17634d0f5b', 'statusUrl': 'https://api.abnormalplatform.com/v1/cases/19377...'}}|
  
Example output:

```
{
  "response": {
    "response": {
      "actionId": "61e76395-40d3-4d78-b6a8-8b17634d0f5b",
      "statusUrl": "https://api.abnormalplatform.com/v1/cases/19377..."
    }
  }
}
```

#### Manage Threat
  
This action is used to manage a Threat identified by Abnormal Security

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|True|Remediate or unremediate a threat|['remediate', 'unremediate']|remediate|
|threat_id|string|None|True|A UUID representing the threat|None|184712ab-6d8b-47b3-89d3-a314efef79e2|
  
Example input:

```
{
  "action": "remediate",
  "threat_id": "184712ab-6d8b-47b3-89d3-a314efef79e2"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|manage_threat_response|True|Response containing the action ID and status URL|{'response': {'actionId': 'a33a212a-89ff-461f-be34-ea52aff44a73', 'statusUrl': 'https://api.abnormalplatform.com/v1/threats/184712...'}}|
  
Example output:

```
{
  "response": {
    "response": {
      "actionId": "a33a212a-89ff-461f-be34-ea52aff44a73",
      "statusUrl": "https://api.abnormalplatform.com/v1/threats/184712..."
    }
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**threat**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Threat ID|string|None|False|Threat ID|None|
  
**message**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ABX Message ID|integer|None|False|ABX Message ID|None|
|ABX Portal URL ID|string|None|False|ABX portal URL ID|None|
|Attachment Names|[]string|None|False|Attachment names|None|
|Attack Strategy|string|None|False|Attack strategy|None|
|Attack Type|string|None|False|Attack type|None|
|Attack Vector|string|None|False|Attack vector|None|
|Attacked Party|string|None|False|Attacked party|None|
|Auto Remediated|boolean|None|False|Auto remediated|None|
|CC Emails|[]string|None|False|CC emails|None|
|From Address|string|None|False|From address|None|
|From Name|string|None|False|From name|None|
|Impersonated Party|string|None|False|Impersonated party|None|
|Internet Message ID|string|None|False|Internet message ID|None|
|Is Read|boolean|None|False|Is Read|None|
|Post Remediated|boolean|None|False|Post remediated|None|
|Received Time|string|None|False|Received time|None|
|Recipient Address|string|None|False|Recipient address|None|
|Remediation Timestamp|string|None|False|Remediation timestamp|None|
|Reply to Emails|[]string|None|False|Reply to emails|None|
|Return Path|string|None|False|Return path|None|
|Sender IP Address|string|None|False|Sender IP address|None|
|Sent Time|string|None|False|Sent time|None|
|Subject|string|None|False|Subject|None|
|Summary Insights|[]string|None|False|Summary insights|None|
|Threat ID|string|None|False|Threat ID|None|
|To Address|string|None|False|To address|None|
|URLs|[]string|None|False|URLs|None|
  
**threat_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Messages|[]message|None|False|List of messages|None|
|Threat ID|string|None|False|Threat ID|None|
  
**case**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Case ID|string|None|False|Case ID|None|
|Severity|string|None|False|Severity|None|
  
**case_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Affected Employee|string|None|False|Affected employee|None|
|Case ID|string|None|False|Case ID|None|
|First Observed|string|None|False|First observed|None|
|Severity|string|None|False|Severity|None|
  
**manage_threat_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action ID|string|None|False|Action ID|None|
|Status URL|string|None|False|Status URL|None|
  
**manage_case_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action ID|string|None|False|Action ID|None|
|Status URL|string|None|False|Status URL|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 2.0.1 - To remove formatting of the fromTime or toTome values used in the `get_cases` and `get_threats` actions  
* 2.0.0 - Add support to select the time filter filed in `get_cases` action | bump SDK version  
* 1.3.0 - New logo and requirements update  
* 1.2.0 - New actions Manage Case and Manage Threat  
* 1.1.0 - New actions Get Cases and Get Case Details  
* 1.0.0 - Initial plugin

# Links

* [Abnormal Security](https://abnormalsecurity.com/)

## References

* [Abnormal Security](https://abnormalsecurity.com/)