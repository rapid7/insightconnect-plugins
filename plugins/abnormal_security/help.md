# Description

Protect your Microsoft Office 365 and G-Suite environments with next-generation email security from Abnormal Security, that uses the most advanced AI detection techniques to stop targeted phishing attacks.

# Key Features

* Retrieve a list of threats and cases from Abnormal Threat Log
* Get details about existing threats and cases

# Requirements

* An Abnormal Security API Key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

#### Manage Threat

This action is used to manage a Threat identified by Abnormal Security.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|manage_threat_response|True|Response containing the action ID and status URL|

Example output:

```
{
  "response": {
    "actionId": "a33a212a-89ff-461f-be34-ea52aff44a73",
    "statusUrl": "https://api.abnormalplatform.com/v1/threats/184712..."
  }
}
```

#### Manage Case

This action is used to manage an Abnormal Case.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|manage_case_response|True|Response containing the action ID and status URL|

Example output:

```
{
  "response": {
    "actionId": "61e76395-40d3-4d78-b6a8-8b17634d0f5b",
    "statusUrl": "https://api.abnormalplatform.com/v1/cases/19377..."
  }
}
```

#### Get Cases

This action is used to get a list of up to 100 cases identified by Abnormal Security, if no input filter dates are provided, it will return up to 100 latest results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|from_date|string|None|False|This input enables you to filter your results from a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|22021-03-01T21:11:38Z|
|to_date|string|None|False|This input enables you to filter your results to a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-01T21:11:38Z|

Example input:

```
{
  "from_date": "2021-03-01T21:11:38Z",
  "to_date": "2021-03-11T21:11:38Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cases|[]case|True|A list of the top 100 cases identified in Abnormal Cases|

Example output:

```
{
  "cases": [
    {
      "caseId": "19377",
      "severity": "Potential Account Takeover"
    }
  ]
}
```

#### Get Case Details

This action is used to get details of a case identified by Abnormal Security.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|case_id|string|None|True|A string representing the case|None|19377|

Example input:

```
{
  "case_id": "19377"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|case_details|case_details|True|Details of the requested case identified by Abnormal Security|

Example output:

```
{
  "case_details": {
    "caseId": "19377",
    "severity": "Potential Account Takeover",
    "affectedEmployee": "FirstName LastName",
    "firstObserved": "2020-06-09T17:42:59Z"
  }
}
```

#### Get Threat Details

This action is used to get details of a threat identified by Abnormal Security.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|threat_id|string|None|True|A UUID representing the threat|None|184712ab-6d8b-47b3-89d3-a314efef79e2|

Example input:

```
{
  "threat_id": "184712ab-6d8b-47b3-89d3-a314efef79e2"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threat_details|threat_details|True|Details of the requested threat identified by Abnormal Security|

Example output:

```
{
  "threat_details": {
    "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2",
    "messages": [
      {
        "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2",
        "autoRemediated": true,
        "postRemediated": false,
        "attackType": "Spam",
        "attackStrategy": "Unknown Sender",
        "returnPath": "user@example.com",
        "senderIpAddress": "192.168.50.1",
        "impersonatedParty": "none / Others",
        "attackVector": "Link",
        "summaryInsights": [
          "Abnormal Email Body HTML",
          "Suspicious Link",
          "Unusual Sender Domain",
          "Abnormal Email SignOff",
          "Unusual Sender"
        ],
        "remediationTimestamp": "2021-02-02T21:09:41Z",
        "isRead": false,
        "attackedParty": "Other",
        "abxMessageId": 1111111111111111113,
        "abxPortalUrl": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/1111111111111111113",
        "subject": "[LIKELY PHISHING] Testing Myths",
        "fromAddress": "user@example.com",
        "fromName": "Test Example",
        "toAddresses": "user@example.com",
        "receivedTime": "2021-02-02T21:09:37Z",
        "sentTime": "2021-02-02T21:06:49Z",
        "internetMessageId": "<user@example.com>",
        "urls": [
          "https://example.com"
        ]
      },
      {
        "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2",
        "autoRemediated": false,
        "postRemediated": true,
        "attackType": "Spam",
        "attackStrategy": "Name Impersonation",
        "returnPath": "user@example.com",
        "senderIpAddress": "192.168.50.1",
        "impersonatedParty": "none / Others",
        "attackVector": "Link",
        "summaryInsights": [
          "Abnormal Email Body HTML",
          "Unusual Sender",
          "Suspicious Link",
          "Unusual Sender Domain"
        ],
        "remediationTimestamp": "2020-05-17T21:09:55Z",
        "isRead": false,
        "attackedParty": "Employee (other)",
        "abxMessageId": -1111111111111111112,
        "abxPortalUrl": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/-1111111111111111112",
        "subject": "[LIKELY PHISHING] Testing Myths",
        "fromAddress": "user@example.com",
        "fromName": "Test Example",
        "toAddresses": "user@example.com",
        "recipientAddress": "user@example.com",
        "receivedTime": "2020-05-17T21:09:51Z",
        "sentTime": "2020-05-17T21:09:46Z",
        "internetMessageId": "<user@example.com>",
        "urls": [
          "https://example.com",
          "https://example.com"
        ]
      },
      {
        "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2",
        "autoRemediated": false,
        "postRemediated": false,
        "attackType": "Spam",
        "attackStrategy": "Name Impersonation",
        "returnPath": "user@example.com",
        "senderIpAddress": "192.168.50.1",
        "impersonatedParty": "none / Others",
        "attackVector": "Link",
        "summaryInsights": [
          "Abnormal Email Body HTML",
          "Suspicious Link",
          "Unusual Sender Domain",
          "Unusual Sender"
        ],
        "attackedParty": "Employee (other)",
        "abxMessageId": -1111111111111111114,
        "abxPortalUrl": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/-1111111111111111114",
        "subject": "The Truth About 7 Myths",
        "fromAddress": "user@example.com",
        "fromName": "Test Example",
        "toAddresses": "user@example.com",
        "recipientAddress": "user@example.com",
        "receivedTime": "2020-05-10T21:05:08Z",
        "sentTime": "2020-05-10T21:05:03Z",
        "internetMessageId": "<user@example.com>"
      }
    ]
  }
}
```

#### Get Threats

This action is used to get a list of up to 100 threats identified in the Abnormal Security Threat Log.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|from_date|string|None|False|This input enables you to filter your results from a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-01T21:11:38Z|
|to_date|string|None|False|This input enables you to filter your results to a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-01T21:11:38Z|

Example input:

```
{
  "from_date": "2021-03-01T21:11:38Z",
  "to_date": "2021-03-11T21:11:38Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threats|[]threat|True|A list of the top 100 threats identified in Threat Log|

Example output:

```
{
  "threats": [
    {
      "threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2"
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### case

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Case ID|string|False|Case ID|
|Severity|string|False|Severity|

#### case_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Affected Employee|string|False|Affected employee|
|Case ID|string|False|Case ID|
|First Observed|string|False|First observed|
|Severity|string|False|Severity|

#### manage_case_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action ID|string|False|Action ID|
|Status URL|string|False|Status URL|

#### manage_threat_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action ID|string|False|Action ID|
|Status URL|string|False|Status URL|

#### message

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ABX Message ID|integer|False|ABX Message ID|
|ABX Portal URL ID|string|False|ABX portal URL ID|
|Attachment Names|[]string|False|Attachment names|
|Attack Strategy|string|False|Attack strategy|
|Attack Type|string|False|Attack type|
|Attack Vector|string|False|Attack vector|
|Attacked Party|string|False|Attacked party|
|Auto Remediated|boolean|False|Auto remediated|
|CC Emails|[]string|False|CC emails|
|From Address|string|False|From address|
|From Name|string|False|From name|
|Impersonated Party|string|False|Impersonated party|
|Internet Message ID|string|False|Internet message ID|
|Is Read|boolean|False|Is Read|
|Post Remediated|boolean|False|Post remediated|
|Received Time|string|False|Received time|
|Recipient Address|string|False|Recipient address|
|Remediation Timestamp|string|False|Remediation timestamp|
|Reply to Emails|[]string|False|Reply to emails|
|Return Path|string|False|Return path|
|Sender IP Address|string|False|Sender IP address|
|Sent Time|string|False|Sent time|
|Subject|string|False|Subject|
|Summary Insights|[]string|False|Summary insights|
|Threat ID|string|False|Threat ID|
|To Address|string|False|To address|
|URLs|[]string|False|URLs|

#### threat

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Threat ID|string|False|Threat ID|

#### threat_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Messages|[]message|False|List of messages|
|Threat ID|string|False|Threat ID|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.0 - New actions Manage Case and Manage Threat
* 1.1.0 - New actions Get Cases and Get Case Details
* 1.0.0 - Initial plugin

# Links

## References

* [Abnormal Security](https://abnormalsecurity.com/)

