# Description

Protect your Microsoft Office 365 and G-Suite environments with next-generation email security that uses the most advanced AI detection techniques to stop targeted phishing attacks

# Key Features

* Retrive a list of threats from Abnormal Threat Log
* Get details about existing threats

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Abnormal Security API Key|None|Vud5CDO9ULIV3SJOcp|
|hostname|string|https://api.abnormalplatform.com|True|Abnormal Security host URL|None|https://api.abnormalplatform.com|

Example input:

```
{
  "api_key": "Vud5CDO9ULIV3SJOcp",
  "hostname": "https://api.abnormalplatform.com"
}
```

## Technical Details

### Actions

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
            "remediationTimestamp": "2021-02-02T21: 09: 41Z",
            "isRead": false,
            "attackedParty": "Other",
            "abxMessageId": 1111111111111111113,
            "abxPortalUrl": "https: //portal.abnormalsecurity.com/home/threat-center/remediation-history/1111111111111111113",
            "subject": "[LIKELY PHISHING] Testing Myths",
            "fromAddress": "user@example.com",
            "fromName": "Test Example",
            "toAddresses": "user@example.com",
            "receivedTime": "2021-02-02T21:09:37Z",
            "sentTime": "2021-02-02T21:06:49Z",
            "internetMessageId": "<user@example.com>",
            "urls": [
                "https://do-not-click-me.com/click/example/EW71AW9IBJ7ZQHKRF6JN/"
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
                "https://randomurl.com/docs/DOC-0r2019j",
                "https://suspicious-url.com/click/example/EW71AW9IBJ7ZQHKRF6JN/"
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
            "subject": "The Truth About 7 Masturbation Myths",
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
```

#### Get Threats

This action is used to get a list of up to 100 threats identified in the Abnormal Security Threat Log.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|from_date|string|None|False|This input enables you to filter your results from a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-01 21:11:38|
|to_date|string|None|False|This input enables you to filter your results to a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-11 21:11:38|

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

#### threat

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Threat ID|string|False|Threat ID|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Abnormal Security](LINK TO PRODUCT/VENDOR WEBSITE)
