# Description

[Proofpoint Targeted Attack Protection](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection) (TAP) helps you stay ahead of attackers with an innovative approach that detects, analyzes and blocks advanced threats before they reach your inbox. This plugin enables users to parse TAP alerts

# Key Features

* Fetch Forensics
* URL Decode
* Get Top Clickers
* Get Permitted Clicks
* Get Delivered Threats
* Get Blocked Messages
* Get All Threats
* Get Blocked Clicks
* Parse Alert

# Requirements

* Proofpoint TAP [service principal and secret](https://ptr-docs.proofpoint.com/ptr-guides/integrations-files/ptr-tap/#generate-tap-service-credentials)

# Supported Product Versions

* Proofpoint TAP API v2
* Tested on 2024-06-04

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|secret|credential_secret_key|None|True|The TAP secret for basic authentication API interaction|None|30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050|None|None|
|servicePrincipal|credential_secret_key|None|True|The TAP service principal for basic authentication API interaction|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|

Example input:

```
{
  "secret": "30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050",
  "servicePrincipal": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

## Technical Details

### Actions


#### Fetch Forensics

This action is used to pull detailed forensic evidence about individual threats or campaigns. Either 'threatId' or 
'campaignId' should be specified

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|campaignId|string|None|False|Campaign identifier|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
|includeCampaignForensics|boolean|None|False|Include campaign forensics in threats. This parameter works only with Threat ID|None|False|None|None|
|threatId|string|None|False|Threat identifier|None|30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050|None|None|
  
Example input:

```
{
  "campaignId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
  "includeCampaignForensics": false,
  "threatId": "30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|generated|string|True|ISO8601-formatted datetime corresponding to the time this report was generated|2021-06-27 19:58:04.283000+00:00|
|reports|[]report|True|Reported threats|[{"scope": "CAMPAIGN", "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "name": "Emotet", "forensics": [{"type": "behavior", "display": "Test", "engine": "iee", "malicious": False, "note": "Test2", "time": 0, "what": {"rule": "behavior_123456789"}, "platforms": [{"name": "Win10", "os": "win", "version": "win10"}]}]}]|
  
Example output:

```
{
  "generated": "2021-06-27 19:58:04.283000+00:00",
  "reports": [
    {
      "forensics": [
        {
          "display": "Test",
          "engine": "iee",
          "malicious": false,
          "note": "Test2",
          "platforms": [
            {
              "name": "Win10",
              "os": "win",
              "version": "win10"
            }
          ],
          "time": 0,
          "type": "behavior",
          "what": {
            "rule": "behavior_123456789"
          }
        }
      ],
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "name": "Emotet",
      "scope": "CAMPAIGN"
    }
  ]
}
```

#### Get All Threats

This action is used to fetch events for all clicks and messages relating to known threats within the specified time 
period

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|threatStatus|string|all|True|The threat statuses which will be returned in the data|["active", "cleared", "falsePositive", "all"]|active|None|None|
|threatType|string|all|True|The threat type which will be returned in the data|["url", "attachment", "messageText", "all"]|url|None|None|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|None|None|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|None|None|
  
Example input:

```
{
  "threatStatus": "all",
  "threatType": "all",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|allThreats|True|The results containing all threats|{'clicksBlocked': [], 'clicksPermitted': [], 'messagesBlocked': [{'cluster': 'proofpointdemo_cloudadminuidemo_hosted', 'impostorScore': 0, 'threatsInfoMap': [{'threat': 'klongkru.ac.th/', 'threatID': 'd22be456cbc0a0e5d900696c36c92c547bea13cc76d32b63ed...', 'threatStatus': 'active', 'threatTime': '2021-02-09T15:59:49.000Z', 'threatType': 'url', 'threatUrl': 'https://example.com', 'classification': 'phish'}], 'QID': '3823t51rm5-1', 'messageTime': '2021-04-21T11:15:26.000Z', 'spamScore': 100, 'toAddresses': ['user@example.com'], 'GUID': 'gk6qK0AUnJMM-0iF10DbYBA3lZgxMALt', 'completelyRewritten': False, 'modulesRun': ['av', 'spf'], 'messageParts': [{'contentType': 'message/delivery-status', 'disposition': 'attached', 'filename': 'message-delivery-status', 'md5': '9de5069c5afe602b2ea0a04b66beb2c0', 'oContentType': 'message/delivery-status', 'sha256': '067fc64bf84042ce48f4761097aec5c5d6cf62bb80dc66c45e...'}, {'oContentType': 'text/plain', 'sha256': 'f95b2809b1ecd4dd6de4e2318340388f8007c7ac76778532c4...', 'contentType': 'text/plain', 'disposition': 'inline', 'filename': 'text.txt', 'md5': '9de5069c5afe602b2ea0a04b66beb2c0'}], 'messageSize': 9982, 'subject': 'Mail delivery failed: returning message to sender', 'fromAddress': ['user@example.com'], 'headerFrom': 'Mail Delivery System <user@example.com>', 'quarantineFolder': 'Phish', 'recipient': ['user@example.com'], 'malwareScore': 0, 'policyRoutes': ['default_inbound', 'allow_relay'], 'messageID': '<user@example.com>', 'phishScore': 100, 'quarantineRule': 'phish', 'senderIP': '198.51.100.1', 'id': '9de5069c-5afe-602b-2ea0-a04b66beb2c0'}], 'messagesDelivered': [], 'queryEndTime': '2021-04-21T12:00:00Z'}|
  
Example output:

```
{
  "results": {
    "clicksBlocked": [],
    "clicksPermitted": [],
    "messagesBlocked": [
      {
        "GUID": "gk6qK0AUnJMM-0iF10DbYBA3lZgxMALt",
        "QID": "3823t51rm5-1",
        "cluster": "proofpointdemo_cloudadminuidemo_hosted",
        "completelyRewritten": false,
        "fromAddress": [
          "user@example.com"
        ],
        "headerFrom": "Mail Delivery System <user@example.com>",
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "impostorScore": 0,
        "malwareScore": 0,
        "messageID": "<user@example.com>",
        "messageParts": [
          {
            "contentType": "message/delivery-status",
            "disposition": "attached",
            "filename": "message-delivery-status",
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
            "oContentType": "message/delivery-status",
            "sha256": "067fc64bf84042ce48f4761097aec5c5d6cf62bb80dc66c45e..."
          },
          {
            "contentType": "text/plain",
            "disposition": "inline",
            "filename": "text.txt",
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
            "oContentType": "text/plain",
            "sha256": "f95b2809b1ecd4dd6de4e2318340388f8007c7ac76778532c4..."
          }
        ],
        "messageSize": 9982,
        "messageTime": "2021-04-21T11:15:26.000Z",
        "modulesRun": [
          "av",
          "spf"
        ],
        "phishScore": 100,
        "policyRoutes": [
          "default_inbound",
          "allow_relay"
        ],
        "quarantineFolder": "Phish",
        "quarantineRule": "phish",
        "recipient": [
          "user@example.com"
        ],
        "senderIP": "198.51.100.1",
        "spamScore": 100,
        "subject": "Mail delivery failed: returning message to sender",
        "threatsInfoMap": [
          {
            "classification": "phish",
            "threat": "klongkru.ac.th/",
            "threatID": "d22be456cbc0a0e5d900696c36c92c547bea13cc76d32b63ed...",
            "threatStatus": "active",
            "threatTime": "2021-02-09T15:59:49.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com"
          }
        ],
        "toAddresses": [
          "user@example.com"
        ]
      }
    ],
    "messagesDelivered": [],
    "queryEndTime": "2021-04-21T12:00:00Z"
  }
}
```

#### Get Blocked Clicks

This action is used to fetch events for clicks to malicious URLs blocked in the specified time period

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|threatStatus|string|all|True|The threat statuses which will be returned in the data|["active", "cleared", "falsePositive", "all"]|active|None|None|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|None|None|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|None|None|
|url|string|None|False|The URL for which the results will be returned. Returns all results if left empty|None|https://example.com|None|None|
  
Example input:

```
{
  "threatStatus": "all",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00",
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|blockedClicks|True|The results containing blocked clicks|{'clicksBlocked': [{'GUID': 'X7sh5TwRxBZOAXb-d8ESyugsIdtfv3u', 'classification': 'malware', 'clickIP': '198.51.100.1', 'clickTime': '2021-04-20T21:08:13.000Z', 'id': '9de5069c-5afe-602b-2ea0-a04b66beb2c0', 'messageID': '<user@example.com>', 'recipient': 'user@example.com', 'sender': 'user@example.com', 'senderIP': '198.51.100.1', 'threatID': 'f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...', 'threatStatus': 'active', 'threatTime': '2021-04-20T21:08:38.000Z', 'threatURL': 'https://example.com', 'url': 'https://example.com', 'userAgent': 'Mozilla/5.0 (Macintosh; Intel MAC OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}], 'queryEndTime': '2021-04-21T13:00:00Z'}|
  
Example output:

```
{
  "results": {
    "clicksBlocked": [
      {
        "GUID": "X7sh5TwRxBZOAXb-d8ESyugsIdtfv3u",
        "classification": "malware",
        "clickIP": "198.51.100.1",
        "clickTime": "2021-04-20T21:08:13.000Z",
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "messageID": "<user@example.com>",
        "recipient": "user@example.com",
        "sender": "user@example.com",
        "senderIP": "198.51.100.1",
        "threatID": "f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...",
        "threatStatus": "active",
        "threatTime": "2021-04-20T21:08:38.000Z",
        "threatURL": "https://example.com",
        "url": "https://example.com",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel MAC OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
      }
    ],
    "queryEndTime": "2021-04-21T13:00:00Z"
  }
}
```

#### Get Blocked Messages

This action is used to fetch events for messages blocked in the specified time period which contained a known threat

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|subject|string|None|False|The subject of the email for which the results will be returned (performs a full-match lookup). Returns all results if left empty|None|A phishy email|None|None|
|threatStatus|string|all|True|The threat statuses which will be returned in the data|["active", "cleared", "falsePositive", "all"]|active|None|None|
|threatType|string|all|True|The threat type which will be returned in the data|["url", "attachment", "messageText", "all"]|url|None|None|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|None|None|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|None|None|
  
Example input:

```
{
  "subject": "A phishy email",
  "threatStatus": "all",
  "threatType": "all",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|blockedMessages|True|The results containing blocked messages|{'messagesBlocked': [{'headerFrom': '"amazon" <user@example.com>', 'impostorScore': 0, 'sender': 'user@example.com', 'QID': '381f1q3k77-1', 'completelyRewritten': False, 'malwareScore': 0, 'modulesRun': ['av', 'spf'], 'phishScore': 100, 'policyRoutes': ['default_inbound', 'allow_relay'], 'senderIP': '198.51.100.1', 'fromAddress': ['user@example.com'], 'messageParts': [{'md5': '9de5069c5afe602b2ea0a04b66beb2c0', 'oContentType': 'text/html', 'sha256': '7e38804bf4e90803cc6ef24b6c5e79dd9b9d84b48b23f04ea5...', 'contentType': 'text/html', 'disposition': 'inline', 'filename': 'text.html'}, {'sha256': 'b31b0a1f2b61146af3377833db02811d9af26596e9b5e81457...', 'contentType': 'text/plain', 'disposition': 'inline', 'filename': 'text.txt', 'md5': '9de5069c5afe602b2ea0a04b66beb2c0', 'oContentType': 'text/plain'}], 'toAddresses': ['user@example.com'], 'cluster': 'proofpointdemo_cloudadminuidemo_hosted', 'recipient': ['user@example.com'], 'xmailer': 'Fenokohthk 9', 'spamScore': 100, 'GUID': 'fA8S1YIRh2taWGdoS02QyNccz985vY2D', 'messageID': '<user@example.com>', 'messageSize': 26539, 'messageTime': '2021-04-21T12:27:35.000Z', 'id': '9de5069c-5afe-602b-2ea0-a04b66beb2c0', 'quarantineFolder': 'Phish', 'quarantineRule': 'phish', 'subject': 'A phishy email', 'threatsInfoMap': [{'threatStatus': 'active', 'threatTime': '2021-04-20T09:31:34.000Z', 'threatType': 'url', 'threatUrl': 'https://example.com', 'classification': 'phish', 'threat': '198.51.100.1/ap/signin', 'threatID': '0e10e285491d55c6dba3016e31243af7dabf5842433a3c4735...'}, {'threat': 'https://example.com', 'threatID': '378a3a7731552a2f06349d066f2853f833fa6094ed660d8789...', 'threatStatus': 'active', 'threatTime': '2021-04-20T09:29:43.000Z', 'threatType': 'url', 'threatUrl': 'https://example.com', 'classification': 'phish'}]}], 'queryEndTime': '2021-04-21T13:00:00Z'}|
  
Example output:

```
{
  "results": {
    "messagesBlocked": [
      {
        "GUID": "fA8S1YIRh2taWGdoS02QyNccz985vY2D",
        "QID": "381f1q3k77-1",
        "cluster": "proofpointdemo_cloudadminuidemo_hosted",
        "completelyRewritten": false,
        "fromAddress": [
          "user@example.com"
        ],
        "headerFrom": "\"amazon\" <user@example.com>",
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "impostorScore": 0,
        "malwareScore": 0,
        "messageID": "<user@example.com>",
        "messageParts": [
          {
            "contentType": "text/html",
            "disposition": "inline",
            "filename": "text.html",
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
            "oContentType": "text/html",
            "sha256": "7e38804bf4e90803cc6ef24b6c5e79dd9b9d84b48b23f04ea5..."
          },
          {
            "contentType": "text/plain",
            "disposition": "inline",
            "filename": "text.txt",
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
            "oContentType": "text/plain",
            "sha256": "b31b0a1f2b61146af3377833db02811d9af26596e9b5e81457..."
          }
        ],
        "messageSize": 26539,
        "messageTime": "2021-04-21T12:27:35.000Z",
        "modulesRun": [
          "av",
          "spf"
        ],
        "phishScore": 100,
        "policyRoutes": [
          "default_inbound",
          "allow_relay"
        ],
        "quarantineFolder": "Phish",
        "quarantineRule": "phish",
        "recipient": [
          "user@example.com"
        ],
        "sender": "user@example.com",
        "senderIP": "198.51.100.1",
        "spamScore": 100,
        "subject": "A phishy email",
        "threatsInfoMap": [
          {
            "classification": "phish",
            "threat": "198.51.100.1/ap/signin",
            "threatID": "0e10e285491d55c6dba3016e31243af7dabf5842433a3c4735...",
            "threatStatus": "active",
            "threatTime": "2021-04-20T09:31:34.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com"
          },
          {
            "classification": "phish",
            "threat": "https://example.com",
            "threatID": "378a3a7731552a2f06349d066f2853f833fa6094ed660d8789...",
            "threatStatus": "active",
            "threatTime": "2021-04-20T09:29:43.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com"
          }
        ],
        "toAddresses": [
          "user@example.com"
        ],
        "xmailer": "Fenokohthk 9"
      }
    ],
    "queryEndTime": "2021-04-21T13:00:00Z"
  }
}
```

#### Get Delivered Threats

This action is used to fetch events for messages delivered in the specified time period which contained a known threat

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|subject|string|None|False|The subject of the email for which the results will be returned (performs a full-match lookup). Returns all results if left empty|None|A phishy email|None|None|
|threatStatus|string|all|True|The threat statuses which will be returned in the data|["active", "cleared", "falsePositive", "all"]|active|None|None|
|threatType|string|all|True|The threat type which will be returned in the data|["url", "attachment", "messageText", "all"]|url|None|None|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|None|None|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|None|None|
  
Example input:

```
{
  "subject": "A phishy email",
  "threatStatus": "all",
  "threatType": "all",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|deliveredThreats|True|The results containing delivered threats|{'messagesDelivered': [{'messageParts': [{'disposition': 'inline', 'filename': 'text-rfc822-headers', 'md5': '9de5069c5afe602b2ea0a04b66beb2c0', 'oContentType': 'text/plain', 'sha256': '12aea580d129035f1e424484a818bec62455db3f5632cf5bac...', 'contentType': 'text/plain'}, {'contentType': 'message/delivery-status', 'disposition': 'attached', 'filename': 'message-delivery-status', 'md5': '9de5069c5afe602b2ea0a04b66beb2c0', 'oContentType': 'message/delivery-status', 'sha256': '15ec858c84dd6d44ae94cfed9b9edbab8bb1341d75cea30b48...'}], 'messageSize': 16026, 'threatsInfoMap': [{'threatID': '22a340fea5cb89908a7576b5e387ce6b296a61a8ac35aac574...', 'threatStatus': 'active', 'threatTime': '2021-04-13T14:45:53.000Z', 'threatType': 'url', 'threatUrl': 'https://example.com', 'classification': 'phish', 'threat': 'starbrandb2bedm.xyz/emm/'}, {'threat': 'starbrandb2bedm.xyz/emm/index.php', 'threatID': 'bcef1812236a940d5e7bb743439e2dc883d3e666124896c339...', 'threatStatus': 'active', 'threatTime': '2021-04-13T08:51:37.000Z', 'threatType': 'url', 'threatUrl': 'https://example.com', 'classification': 'phish'}], 'malwareScore': 0, 'messageID': '<user@example.com>', 'policyRoutes': ['allow_relay', 'firewallsafe'], 'subject': 'A phishy email', 'senderIP': '198.51.100.1', 'spamScore': 0, 'completelyRewritten': False, 'modulesRun': ['access'], 'id': '9de5069c-5afe-602b-2ea0-a04b66beb2c0', 'messageTime': '2021-04-21T17:26:30.000Z', 'toAddresses': ['info-cheri=user@example.com'], 'headerFrom': 'Mail Delivery Subsystem <user@example.com>', 'impostorScore': 0, 'recipient': ['info-cheri=user@example.com'], 'GUID': 'sVfuaRyZ59_UnD2m8RX9i7uGsW4pHcUX', 'phishScore': 0, 'fromAddress': ['user@example.com'], 'QID': '13LHPoqE012261', 'cluster': 'proofpointdemo_cloudadminuidemo_hosted'}], 'queryEndTime': '2021-04-21T18:00:00Z'}|
  
Example output:

```
{
  "results": {
    "messagesDelivered": [
      {
        "GUID": "sVfuaRyZ59_UnD2m8RX9i7uGsW4pHcUX",
        "QID": "13LHPoqE012261",
        "cluster": "proofpointdemo_cloudadminuidemo_hosted",
        "completelyRewritten": false,
        "fromAddress": [
          "user@example.com"
        ],
        "headerFrom": "Mail Delivery Subsystem <user@example.com>",
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "impostorScore": 0,
        "malwareScore": 0,
        "messageID": "<user@example.com>",
        "messageParts": [
          {
            "contentType": "text/plain",
            "disposition": "inline",
            "filename": "text-rfc822-headers",
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
            "oContentType": "text/plain",
            "sha256": "12aea580d129035f1e424484a818bec62455db3f5632cf5bac..."
          },
          {
            "contentType": "message/delivery-status",
            "disposition": "attached",
            "filename": "message-delivery-status",
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
            "oContentType": "message/delivery-status",
            "sha256": "15ec858c84dd6d44ae94cfed9b9edbab8bb1341d75cea30b48..."
          }
        ],
        "messageSize": 16026,
        "messageTime": "2021-04-21T17:26:30.000Z",
        "modulesRun": [
          "access"
        ],
        "phishScore": 0,
        "policyRoutes": [
          "allow_relay",
          "firewallsafe"
        ],
        "recipient": [
          "info-cheri=user@example.com"
        ],
        "senderIP": "198.51.100.1",
        "spamScore": 0,
        "subject": "A phishy email",
        "threatsInfoMap": [
          {
            "classification": "phish",
            "threat": "starbrandb2bedm.xyz/emm/",
            "threatID": "22a340fea5cb89908a7576b5e387ce6b296a61a8ac35aac574...",
            "threatStatus": "active",
            "threatTime": "2021-04-13T14:45:53.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com"
          },
          {
            "classification": "phish",
            "threat": "starbrandb2bedm.xyz/emm/index.php",
            "threatID": "bcef1812236a940d5e7bb743439e2dc883d3e666124896c339...",
            "threatStatus": "active",
            "threatTime": "2021-04-13T08:51:37.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com"
          }
        ],
        "toAddresses": [
          "info-cheri=user@example.com"
        ]
      }
    ],
    "queryEndTime": "2021-04-21T18:00:00Z"
  }
}
```

#### Get Permitted Clicks

This action is used to fetch events for clicks to malicious URLs permitted in the specified time period

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|threatStatus|string|all|True|The threat statuses which will be returned in the data|["active", "cleared", "falsePositive", "all"]|active|None|None|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|None|None|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|None|None|
|url|string|None|False|The URL for which the results will be returned. Returns all results if left empty|None|https://example.com|None|None|
  
Example input:

```
{
  "threatStatus": "all",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00",
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|permittedClicks|True|The results containing permitted clicks|{'clicksPermitted': [{'GUID': 'X7sh5TwRxBZOAXb-d8ESyugsIdtfv3u', 'classification': 'malware', 'clickIP': '198.51.100.1', 'clickTime': '2021-04-20T21:08:13.000Z', 'id': '9de5069c-5afe-602b-2ea0-a04b66beb2c0', 'messageID': '<user@example.com>', 'recipient': 'user@example.com', 'sender': 'user@example.com', 'senderIP': '198.51.100.1', 'threatID': 'f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...', 'threatStatus': 'active', 'threatTime': '2021-04-20T21:08:38.000Z', 'threatURL': 'https://example.com', 'url': 'https://example.com', 'userAgent': 'Mozilla/5.0 (Macintosh; Intel MAC OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}], 'queryEndTime': '2021-04-21T13:00:00Z'}|
  
Example output:

```
{
  "results": {
    "clicksPermitted": [
      {
        "GUID": "X7sh5TwRxBZOAXb-d8ESyugsIdtfv3u",
        "classification": "malware",
        "clickIP": "198.51.100.1",
        "clickTime": "2021-04-20T21:08:13.000Z",
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "messageID": "<user@example.com>",
        "recipient": "user@example.com",
        "sender": "user@example.com",
        "senderIP": "198.51.100.1",
        "threatID": "f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...",
        "threatStatus": "active",
        "threatTime": "2021-04-20T21:08:38.000Z",
        "threatURL": "https://example.com",
        "url": "https://example.com",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel MAC OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
      }
    ],
    "queryEndTime": "2021-04-21T13:00:00Z"
  }
}
```

#### Get Top Clickers

This action is used to fetch the identities and attack index of the top clickers within your organization for a given 
period

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|window|integer|None|True|An integer indicating how many days the data should be retrieved for|[14, 30, 90]|14|None|None|
  
Example input:

```
{
  "window": 14
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|interval|string|False|An ISO8601-formatted interval showing what time the response was calculated for|2023-03-07T06:01:00Z/2023-06-05T06:01:00Z|
|totalTopClickers|integer|False|An integer describing the total number of top clickers in the time interval|2|
|users|[]user|False|An array of user objects that contain information about the user's identity and statistics of the clicking behavior|[{"clickStatistics": {"families": [{"clicks": 28, "name": "Malware"}], "clickCount": 28}, "identity": {"emails": ["user@example.com"], "guid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "vip": False}}, {"clickStatistics": {"clickCount": 8, "families": [{"clicks": 6, "name": "MalSpam"}, {"clicks": 8, "name": "Malware"}]}, "identity": {"emails": ["user@example.com"], "guid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "vip": False}}]|
  
Example output:

```
{
  "interval": "2023-03-07T06:01:00Z/2023-06-05T06:01:00Z",
  "totalTopClickers": 2,
  "users": [
    {
      "clickStatistics": {
        "clickCount": 28,
        "families": [
          {
            "clicks": 28,
            "name": "Malware"
          }
        ]
      },
      "identity": {
        "emails": [
          "user@example.com"
        ],
        "guid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "vip": false
      }
    },
    {
      "clickStatistics": {
        "clickCount": 8,
        "families": [
          {
            "clicks": 6,
            "name": "MalSpam"
          },
          {
            "clicks": 8,
            "name": "Malware"
          }
        ]
      },
      "identity": {
        "emails": [
          "user@example.com"
        ],
        "guid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "vip": false
      }
    }
  ]
}
```

#### Parse Alert

This action is used to parse a TAP alert

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|tapAlert|string|None|True|A Proofpoint TAP alert|None|`proofpoint      URL DefenseAn end user has clicked on a link in their email which Proofpoint now recog=nizes as malicious. Details about the threat, the permitted click, and the =message containing the link are below:ThreatURL      hxxp://ec2-12-23-34-123[.]compute-1[.]amazonaws[.]com/[.]0[.]/ja=ke[.]user@example[.]comCategory         phishCondemnation Time        2020-04-27T12:22:54ZMessageTime Delivered   2020-04-27T09:54:49ZRecipient        user@example.comSubject  =97Sender   =97Header From      =97Header ReplyTo   =97Message-ID       =97Message-GUID     -JsyOYf--Yt7cR-ctdIo7RuUiK9kSECEThreat-ID        6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3da6f4e=798a39Sender IP        =97Message Size     =97ClickTime     2020-04-27T09:54:49ZSource IP        192.168.50.100User Agent       Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0)= like GeckoView Threat Details<https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789=-ef71-f3998c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a75=9e7db48f3da6f4e798a39?linkOrigin=3Dnotif>You are receiving this message because you are subscribed to alerts from th=e Threat Insight Dashboard. Update your subscription preferences<https://th=reatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f3998c3e92e3/settings/pr=ivileges?linkOrigin=3Dnotif> to stop receiving these notifications.Proofpoint Targeted Attack Protectionproofpoint--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_Content-Type: text/html; charset="Windows-1252"Content-ID: <user@example.com>Content-Transfer-Encoding: quoted-printable<html><head><meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3DWindows-1=252"></head><body style=3D"margin:0px"><div style=3D"background:#f1f2f2;font-family:Arial;font-size:13px;color:#66=6666"><div style=3D"background:white"><div style=3D"max-width:720px;margin:auto;padding:0"><table style=3D"width:100%;height:60px;font-family:inherit;font-size:inheri=t;color:inherit"><tbody><tr><td><b style=3D"font-size:22px;color:black">proofpoint</b> </td><td align=3D"right">URL Defense</td></tr><tr></tr></tbody></table></div></div><div style=3D"max-width:720px;margin:auto;padding:20px 0">An end user has c=licked on a link in their email which Proofpoint now recognizes as maliciou=s. Details about the threat, the permitted click, and the message containin=g the link are below:<p><b>Threat</b></p><p><table border=3D"1" style=3D"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit" cellspa=cing=3D"0" cellpadding=3D"8"><col width=3D"150"><col><tbody><tr valign=3D"top"><td><b>URL</b></td><td style=3D"background:white">hxxp://ec2-12-34-56-123[.]compute-1[.]amazo=naws[.]com/[.]0[.]/user@example[.]com</td></tr><tr valign=3D"top"><td><b>Category</b></td><td style=3D"background:white">phish</td></tr><tr valign=3D"top"><td><b>Condemnation Time</b></td><td style=3D"background:white">2020-04-27T12:22:54Z</td></tr></tbody></table></p><p><b>Message</b></p><p><table border=3D"1" style=3D"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit" cellspa=cing=3D"0" cellpadding=3D"8"><col width=3D"150"><col><tbody><tr valign=3D"top"><td><b>Time Delivered</b></td><td style=3D"background:white">2020-04-27T09:54:49Z</td></tr><tr valign=3D"top"><td><b>Recipient</b></td><td style=3D"background:white">user@example.com</td></tr><tr valign=3D"top"><td><b>Subject</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Sender</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Header From</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Header ReplyTo</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Message-ID</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Message-GUID</b></td><td style=3D"background:white">-JsyOYf--Yt7cR-ctdIo7RuUiK9kSECE</td></tr><tr valign=3D"top"><td><b>Threat-ID</b></td><td style=3D"background:white">6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759=e7db48f3da6f4e798a39</td></tr><tr valign=3D"top"><td><b>Sender IP</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Message Size</b></td><td style=3D"background:white">=97</td></tr></tbody></table></p><p><b>Click</b></p><p><table border=3D"1" style=3D"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit" cellspa=cing=3D"0" cellpadding=3D"8"><col width=3D"150"><col><tbody><tr valign=3D"top"><td><b>Time</b></td><td style=3D"background:white">2020-04-27T09:54:49Z</td></tr><tr valign=3D"top"><td><b>Source IP</b></td><td style=3D"background:white">192.168.50.100</td></tr><tr valign=3D"top"><td><b>User Agent</b></td><td style=3D"background:white">Mozilla/5.0 (Windows NT 10.0; WOW64; Trident=/7.0; rv:11.0) like Gecko</td></tr></tbody></table></p><p></p><div style=3D"width:120px;margin:40px auto;padding:8px 32px;background:#06a=2d5;text-align:center"><a href=3D"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3=da6f4e798a39?linkOrigin=3Dnotif" style=3D"color:white;text-decoration:none"=>View Threat Details</a></div><div style=3D"font-size:11px;border-bottom:solid 1px #d1d3d4;padding-bottom=:8px;">You are receiving this message because you are subscribed to alerts =from the Threat Insight Dashboard.<a href=3D"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/settings/privileges?linkOrigin=3Dnotif">Update your subscription preferences</a> to stop receiving these notificati=ons. </div><p></p><div style=3D"font-size:11px;text-align:center;padding-bottom:30px">Proofpo=int Targeted Attack Protection<p><b>proofpoint</b> </p></div></div></div></body></html>--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_--`|None|None|
  
Example input:

```
{
  "tapAlert": "`proofpoint      URL DefenseAn end user has clicked on a link in their email which Proofpoint now recog=nizes as malicious. Details about the threat, the permitted click, and the =message containing the link are below:ThreatURL      hxxp://ec2-12-23-34-123[.]compute-1[.]amazonaws[.]com/[.]0[.]/ja=ke[.]user@example[.]comCategory         phishCondemnation Time        2020-04-27T12:22:54ZMessageTime Delivered   2020-04-27T09:54:49ZRecipient        user@example.comSubject  =97Sender   =97Header From      =97Header ReplyTo   =97Message-ID       =97Message-GUID     -JsyOYf--Yt7cR-ctdIo7RuUiK9kSECEThreat-ID        6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3da6f4e=798a39Sender IP        =97Message Size     =97ClickTime     2020-04-27T09:54:49ZSource IP        192.168.50.100User Agent       Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0)= like GeckoView Threat Details<https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789=-ef71-f3998c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a75=9e7db48f3da6f4e798a39?linkOrigin=3Dnotif>You are receiving this message because you are subscribed to alerts from th=e Threat Insight Dashboard. Update your subscription preferences<https://th=reatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f3998c3e92e3/settings/pr=ivileges?linkOrigin=3Dnotif> to stop receiving these notifications.Proofpoint Targeted Attack Protectionproofpoint--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_Content-Type: text/html; charset=\"Windows-1252\"Content-ID: <user@example.com>Content-Transfer-Encoding: quoted-printable<html><head><meta http-equiv=3D\"Content-Type\" content=3D\"text/html; charset=3DWindows-1=252\"></head><body style=3D\"margin:0px\"><div style=3D\"background:#f1f2f2;font-family:Arial;font-size:13px;color:#66=6666\"><div style=3D\"background:white\"><div style=3D\"max-width:720px;margin:auto;padding:0\"><table style=3D\"width:100%;height:60px;font-family:inherit;font-size:inheri=t;color:inherit\"><tbody><tr><td><b style=3D\"font-size:22px;color:black\">proofpoint</b> </td><td align=3D\"right\">URL Defense</td></tr><tr></tr></tbody></table></div></div><div style=3D\"max-width:720px;margin:auto;padding:20px 0\">An end user has c=licked on a link in their email which Proofpoint now recognizes as maliciou=s. Details about the threat, the permitted click, and the message containin=g the link are below:<p><b>Threat</b></p><p><table border=3D\"1\" style=3D\"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit\" cellspa=cing=3D\"0\" cellpadding=3D\"8\"><col width=3D\"150\"><col><tbody><tr valign=3D\"top\"><td><b>URL</b></td><td style=3D\"background:white\">hxxp://ec2-12-34-56-123[.]compute-1[.]amazo=naws[.]com/[.]0[.]/user@example[.]com</td></tr><tr valign=3D\"top\"><td><b>Category</b></td><td style=3D\"background:white\">phish</td></tr><tr valign=3D\"top\"><td><b>Condemnation Time</b></td><td style=3D\"background:white\">2020-04-27T12:22:54Z</td></tr></tbody></table></p><p><b>Message</b></p><p><table border=3D\"1\" style=3D\"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit\" cellspa=cing=3D\"0\" cellpadding=3D\"8\"><col width=3D\"150\"><col><tbody><tr valign=3D\"top\"><td><b>Time Delivered</b></td><td style=3D\"background:white\">2020-04-27T09:54:49Z</td></tr><tr valign=3D\"top\"><td><b>Recipient</b></td><td style=3D\"background:white\">user@example.com</td></tr><tr valign=3D\"top\"><td><b>Subject</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Sender</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Header From</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Header ReplyTo</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Message-ID</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Message-GUID</b></td><td style=3D\"background:white\">-JsyOYf--Yt7cR-ctdIo7RuUiK9kSECE</td></tr><tr valign=3D\"top\"><td><b>Threat-ID</b></td><td style=3D\"background:white\">6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759=e7db48f3da6f4e798a39</td></tr><tr valign=3D\"top\"><td><b>Sender IP</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Message Size</b></td><td style=3D\"background:white\">=97</td></tr></tbody></table></p><p><b>Click</b></p><p><table border=3D\"1\" style=3D\"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit\" cellspa=cing=3D\"0\" cellpadding=3D\"8\"><col width=3D\"150\"><col><tbody><tr valign=3D\"top\"><td><b>Time</b></td><td style=3D\"background:white\">2020-04-27T09:54:49Z</td></tr><tr valign=3D\"top\"><td><b>Source IP</b></td><td style=3D\"background:white\">192.168.50.100</td></tr><tr valign=3D\"top\"><td><b>User Agent</b></td><td style=3D\"background:white\">Mozilla/5.0 (Windows NT 10.0; WOW64; Trident=/7.0; rv:11.0) like Gecko</td></tr></tbody></table></p><p></p><div style=3D\"width:120px;margin:40px auto;padding:8px 32px;background:#06a=2d5;text-align:center\"><a href=3D\"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3=da6f4e798a39?linkOrigin=3Dnotif\" style=3D\"color:white;text-decoration:none\"=>View Threat Details</a></div><div style=3D\"font-size:11px;border-bottom:solid 1px #d1d3d4;padding-bottom=:8px;\">You are receiving this message because you are subscribed to alerts =from the Threat Insight Dashboard.<a href=3D\"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/settings/privileges?linkOrigin=3Dnotif\">Update your subscription preferences</a> to stop receiving these notificati=ons. </div><p></p><div style=3D\"font-size:11px;text-align:center;padding-bottom:30px\">Proofpo=int Targeted Attack Protection<p><b>proofpoint</b> </p></div></div></div></body></html>--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_--`"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|tapResults|False|Proofpoint TAP results|{'threat': {'attachmentSha256': '275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f', 'category': 'Malware', 'condemnationTime': '2019-01-10T12:34:05Z', 'threatDetailsUrl': 'https://example.com/9de5069c5afe602b2ea0a04b66beb2c0/threat/email/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f?linkOrigin=notif'}, 'message': {'timeDelivered': '2019-01-10T12:10:21Z', 'recipients': 'user@example.com', 'subject': 'January Invoice', 'sender': 'user@example.com', 'headerFrom': 'Bob', 'headerReplyto': 'user@example.com', 'messageId': 'user@example.com', 'senderIp': '198.51.100.1', 'messageSize': '152 KB', 'messageGuid': '9de5069c5afe602b2ea0a04b66beb2c0', 'threatId': '9de5069c5afe602b2ea0a04b66beb2c0'}, 'browser': {'time': '2020-05-11T11:01:13Z', 'sourceIp': '198.51.100.1', 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}}|
  
Example output:

```
{
  "results": {
    "browser": {
      "sourceIp": "198.51.100.1",
      "time": "2020-05-11T11:01:13Z",
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    },
    "message": {
      "headerFrom": "Bob",
      "headerReplyto": "user@example.com",
      "messageGuid": "9de5069c5afe602b2ea0a04b66beb2c0",
      "messageId": "user@example.com",
      "messageSize": "152 KB",
      "recipients": "user@example.com",
      "sender": "user@example.com",
      "senderIp": "198.51.100.1",
      "subject": "January Invoice",
      "threatId": "9de5069c5afe602b2ea0a04b66beb2c0",
      "timeDelivered": "2019-01-10T12:10:21Z"
    },
    "threat": {
      "attachmentSha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "category": "Malware",
      "condemnationTime": "2019-01-10T12:34:05Z",
      "threatDetailsUrl": "https://example.com/9de5069c5afe602b2ea0a04b66beb2c0/threat/email/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f?linkOrigin=notif"
    }
  }
}
```

#### URL Decode

This action is used to decode URLs which have been rewritten by TAP to their original, target URL

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|urls|[]string|None|True|List of URLs to decode|None|["https://example.com", "https://example2.com"]|None|None|
  
Example input:

```
{
  "urls": [
    "https://example.com",
    "https://example2.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|urls|[]urls|False|Decoded URLs|[{"encodedUrl": "https://urldefense.proofpoint.com/v1/url?u=http://www.example.com/&amp;k=oIvRg1%2BdGAgOoM1BIlLLqw%3D%3D%0A&amp;r=IKM5u8%2B%2F%2Fi8EBhWOS%2BqGbTqCC%2BrMqWI%2FVfEAEsQO%2F0Y%3D%0A&amp;m=Ww6iaHO73mDQpPQwOwfLfN8WMapqHyvtu8jM8SjqmVQ%3D%0A&amp;s=d3583cfa53dade97025bc6274c6c8951dc29fe0f38830cf8e5a447723b9f1c9a\"", "decodedUrl": "http://www.example.com/", "success": true}]|
  
Example output:

```
{
  "urls": [
    {
      "decodedUrl": "http://www.example.com/",
      "encodedUrl": "https://urldefense.proofpoint.com/v1/url?u=http://www.example.com/&amp;k=oIvRg1%2BdGAgOoM1BIlLLqw%3D%3D%0A&amp;r=IKM5u8%2B%2F%2Fi8EBhWOS%2BqGbTqCC%2BrMqWI%2FVfEAEsQO%2F0Y%3D%0A&amp;m=Ww6iaHO73mDQpPQwOwfLfN8WMapqHyvtu8jM8SjqmVQ%3D%0A&amp;s=d3583cfa53dade97025bc6274c6c8951dc29fe0f38830cf8e5a447723b9f1c9a\"",
      "success": true
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks


#### Monitor Events

This task is used to monitor events for all clicks and messages relating to known threats

##### Input
  
*This task does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]event|True|List of all events|[{"eventType": "messageBlocked", "ccAddresses": ["user@example.com"], "clusterId": "example_hosted", "completelyRewritten": true, "fromAddress": ["user@example.com"], "GUID": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "headerFrom": "\"example\" <user@example.com> ", "headerReplyTo": "user@example.com", "impostorScore": 0, "malwareScore": 0, "messageID": "<user@example.com>", "messageParts": [{"disposition": "inline", "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f", "md5": "9de5069c5afe602b2ea0a04b66beb2c0", "filename": "text.txt", "oContentType": "text/plain", "contentType": "text/plain"}], "messageSize": 0, "messageTime": "2023-06-01T23:57:22.000Z", "modulesRun": ["spam"], "phishScore": 0, "policyRoutes": ["default_inbound"], "QID": "9de5069c5afe602b2ea0a04b66beb2c0", "quarantineFolder": "Impostor", "quarantineRule": "impostor", "recipient": ["user@example.com"], "replyToAddress": ["user@example.com"], "sender": "user@example.com", "senderIP": "198.51.100.1", "spamScore": 100, "subject": "Transfer and Balance Request", "threatsInfoMap": [{"threat": "example.ab.cd/", "threatID": "9de5069c5afe602b2ea0a04b66beb2c0", "threatStatus": "active", "threatTime": "2021-02-09T15:59:49.000Z", "threatType": "url", "threatUrl": "https://example.com", "classification": "phish"}], "toAddresses": ["user@example.com"]}, {"eventType": "clickBlocked", "campaignId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "classification": "malware", "clickIP": "198.51.100.1", "clickTime": "2021-04-20T21:08:13.000Z", "GUID": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "recipient": "user@example.com", "sender": "user@example.com", "senderIP": "198.51.100.1", "threatID": "9de5069c5afe602b2ea0a04b66beb2c0", "threatTime": "2016-06-24T19:17:46.000Z", "threatURL": "https://example.com", "threatStatus": "active", "url": "https://example.com", "userAgent": "Mozilla/5.0(WindowsNT6.1;WOW64;rv:27.0)Gecko/20100101Firefox/27.0"}]|
  
Example output:

```
{
  "events": [
    {
      "GUID": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "QID": "9de5069c5afe602b2ea0a04b66beb2c0",
      "ccAddresses": [
        "user@example.com"
      ],
      "clusterId": "example_hosted",
      "completelyRewritten": true,
      "eventType": "messageBlocked",
      "fromAddress": [
        "user@example.com"
      ],
      "headerFrom": "\"example\" <user@example.com> ",
      "headerReplyTo": "user@example.com",
      "impostorScore": 0,
      "malwareScore": 0,
      "messageID": "<user@example.com>",
      "messageParts": [
        {
          "contentType": "text/plain",
          "disposition": "inline",
          "filename": "text.txt",
          "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
          "oContentType": "text/plain",
          "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
        }
      ],
      "messageSize": 0,
      "messageTime": "2023-06-01T23:57:22.000Z",
      "modulesRun": [
        "spam"
      ],
      "phishScore": 0,
      "policyRoutes": [
        "default_inbound"
      ],
      "quarantineFolder": "Impostor",
      "quarantineRule": "impostor",
      "recipient": [
        "user@example.com"
      ],
      "replyToAddress": [
        "user@example.com"
      ],
      "sender": "user@example.com",
      "senderIP": "198.51.100.1",
      "spamScore": 100,
      "subject": "Transfer and Balance Request",
      "threatsInfoMap": [
        {
          "classification": "phish",
          "threat": "example.ab.cd/",
          "threatID": "9de5069c5afe602b2ea0a04b66beb2c0",
          "threatStatus": "active",
          "threatTime": "2021-02-09T15:59:49.000Z",
          "threatType": "url",
          "threatUrl": "https://example.com"
        }
      ],
      "toAddresses": [
        "user@example.com"
      ]
    },
    {
      "GUID": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "campaignId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "classification": "malware",
      "clickIP": "198.51.100.1",
      "clickTime": "2021-04-20T21:08:13.000Z",
      "eventType": "clickBlocked",
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "recipient": "user@example.com",
      "sender": "user@example.com",
      "senderIP": "198.51.100.1",
      "threatID": "9de5069c5afe602b2ea0a04b66beb2c0",
      "threatStatus": "active",
      "threatTime": "2016-06-24T19:17:46.000Z",
      "threatURL": "https://example.com",
      "url": "https://example.com",
      "userAgent": "Mozilla/5.0(WindowsNT6.1;WOW64;rv:27.0)Gecko/20100101Firefox/27.0"
    }
  ]
}
```

### Custom Types
  
**threat**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attachment SHA256 Hash|string|None|False|Attachment SHA256 hash|f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...|
|Category|string|None|False|Category|Malware|
|Condemnation Time|string|None|False|Condemnation time|2023-06-09 09:54:49+00:00|
|Threat Details URL|string|None|False|URL to the details of the threat|https://example.com|
|URL|string|None|False|URL|https://example.com|
  
**message**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Header From|string|None|False|Header from|user@example.com|
|Header Reply To|string|None|False|Header reply to|user@example.com|
|Message GUID|string|None|False|Message GUID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Message ID|string|None|False|Message ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Message Size|string|None|False|Message size|1234|
|Recipients|string|None|False|Recipients|user@example.com|
|Sender|string|None|False|Sender|user@example.com|
|Sender IP|string|None|False|Sender IP|198.51.100.1|
|Subject|string|None|False|Subject|Example subject|
|Threat ID|string|None|False|Unique identifier for this threat|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Time Delivered|string|None|False|Time delivered|2023-06-09 09:54:49+00:00|
  
**browser**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Source IP|string|None|False|Source IP|198.51.100.1|
|Time|string|None|False|Time|2023-06-09 09:54:49+00:00|
|User Agent|string|None|False|User agent string|Mozilla/5.0|
  
**tapResults**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Browser|browser|None|False|Browser information|{}|
|Message|message|None|False|TAP alert meta data|{}|
|Threat|threat|None|False|Threat information|{}|
  
**messageParts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content Type|string|None|False|The true, detected Content-Type of the messagePart|text/html|
|Disposition|string|None|False|If the value is 'inline', the messagePart is a message body. If the value is 'attached', the messagePart is an attachment|inline|
|Filename|string|None|False|The filename of the messagePart|text.html|
|MD5|string|None|False|The MD5 hash of the messagePart contents|9de5069c5afe602b2ea0a04b66beb2c0|
|Declared Content Type|string|None|False|The declared Content-Type of the messagePart|text/html|
|Sandbox Status|string|None|False|The verdict returned by the sandbox during the scanning process|threat|
|SHA256|string|None|False|The SHA256 hash of the messagePart contents|f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...|
  
**threatsInfoMap**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Campaign ID|string|None|False|An identifier for the campaign of which the threat is a member|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Classification|string|None|False|The category of threat found in the message|phish|
|Threat|string|None|False|The artifact which was condemned by Proofpoint. The malicious URL, hash of the attachment threat, or email address of the impostor sender|badsite.zz|
|Threat ID|string|None|False|The unique identifier associated with this threat|f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...|
|Threat Status|string|None|False|The current state of the threat|active|
|Threat Time|string|None|False|Proofpoint assigned the threatStatus at this time|2021-04-20 09:31:34+00:00|
|Threat Type|string|None|False|Whether the threat was an attachment, URL, or message type|url|
|Threat URL|string|None|False|A link to the entry about the threat on the TAP Dashboard|https://example.com|
  
**messages**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|GUID|string|None|False|The ID of the message within PPS|ExaMpleGUidrtMqpWpyaBcD123456789|
|QID|string|None|False|The queue ID of the message within PPS|381f1q3k77-1|
|CC Addresses|[]string|None|False|A list of email addresses contained within the CC|["user@example.com"]|
|Cluster|string|None|False|The name of the PPS cluster which processed the message|example_hosted|
|Completely Rewritten|boolean|None|False|The rewrite status of the message|True|
|From Address|[]string|None|False|The email address contained in the From|["user@example.com"]|
|Header From|string|None|False|The full content of the From|Example Sender <user@example.com>|
|Header Reply To|string|None|False|If present, the full content of the Reply-To|Example Sender <user@example.com>|
|Impostor Score|integer|None|False|The impostor score of the message. Higher scores indicate higher certainty|0|
|Malware Score|integer|None|False|The malware score of the message. Higher scores indicate higher certainty|0|
|Message ID|string|None|False|Message-ID extracted from the headers of the email message|<user@example.com>|
|Message Parts|[]messageParts|None|False|Details about parts of the message, including both message bodies and attachments|[]|
|Message Size|integer|None|False|The size in bytes of the message, including headers and attachments|2347|
|Message Time|string|None|False|When the message was delivered to the user or quarantined by PPS|2021-04-21 12:27:35+00:00|
|Modules Run|[]string|None|False|The list of PPS modules which processed the message|["spam", "pdr"]|
|Phish Score|integer|None|False|The phish score of the message. Higher scores indicate higher certainty|0|
|Policy Routes|[]string|None|False|The policy routes that the message matched during processing by PPS|["default_inbound"]|
|Quarantine Folder|string|None|False|The name of the folder which contains the quarantined message|Phish|
|Quarantine Rule|string|None|False|The name of the rule which quarantined the message|phish|
|Recipient|[]string|None|False|An array containing the email addresses of the SMTP (envelope) recipients|["user@example.com"]|
|Reply To Address|[]string|None|False|The email address contained in the Reply-To|["user@example.com"]|
|Sender|string|None|False|The email address of the SMTP (envelope) sender. The user-part is hashed. The domain-part is cleartext|user@example.com|
|Sender IP|string|None|False|The IP address of the sender|198.51.100.1|
|Spam Score|integer|None|False|The spam score of the message. Higher scores indicate higher certainty|0|
|Subject|string|None|False|The subject line of the message, if available|A phishy email|
|Threats Info Map|[]threatsInfoMap|None|False|Details about detected threats within the message|[]|
|To Address|[]string|None|False|A list of email addresses contained within the To|["user@example.com"]|
|X-Mailer|string|None|False|The content of the X-Mailer|Fenokohthk 9|
  
**clicks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|GUID|string|None|False|The ID of the message within PPS|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Campaign ID|string|None|False|An identifier for the campaign of which the threat is a member|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Classification|string|None|False|The threat category of the malicious URL|malware|
|Click IP|string|None|False|The external IP address of the user who clicked on the link|198.51.100.1|
|Click Time|string|None|False|The time the user clicked on the URL|2021-04-20 21:08:13+00:00|
|ID|string|None|False|The unique ID of the click|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Recipient|string|None|False|The email address of the recipient|user@example.com|
|Sender|string|None|False|The email address of the sender. The user-part is hashed. The domain-part is cleartext|user@example.com|
|Sender IP|string|None|False|The IP address of the sender|198.51.100.1|
|Threat ID|string|None|False|The unique identifier associated with this threat|f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...|
|Threat Status|string|None|False|The current state of the threat|active|
|Threat Time|string|None|False|Proofpoint identified the URL as a threat at this time|2021-04-20 21:08:38+00:00|
|Threat URL|string|None|False|A link to the entry on the TAP Dashboard for the particular threat|https://example.com|
|URL|string|None|False|The malicious URL which was clicked|https://example.com|
|User Agent|string|None|False|The User-Agent header from the clicker's HTTP request|Mozilla/5.0 (Macintosh; Intel MAC OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36|
  
**blockedMessages**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Messages Blocked|[]messages|None|False|An array containing all messages with threats which were quarantined by PPS|[]|
|Query End Time|string|None|False|The time at which the period queried for data ended|2023-06-09 10:48:00+00:00|
  
**deliveredThreats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Messages Delivered|[]messages|None|False|An array containing all messages with threats which were delivered by PPS|[]|
|Query End Time|string|None|False|The time at which the period queried for data ended|2023-06-09 10:48:00+00:00|
  
**blockedClicks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Clicks Blocked|[]clicks|None|False|An array containing all clicks to URL threats which were blocked|[]|
|Query End Time|string|None|False|The time at which the period queried for data ended|2023-06-09 10:48:00+00:00|
  
**permittedClicks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Clicks Permitted|[]clicks|None|False|An array containing all clicks to URL threats which were permitted|[]|
|Query End Time|string|None|False|The time at which the period queried for data ended|2023-06-09 10:48:00+00:00|
  
**allThreats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Clicks Blocked|[]clicks|None|False|An array containing all clicks to URL threats which were blocked|[]|
|Clicks Permitted|[]clicks|None|False|An array containing all clicks to URL threats which were permitted|[]|
|Messages Blocked|[]messages|None|False|An array containing all messages with threats which were quarantined by PPS|[]|
|Messages Delivered|[]messages|None|False|An array containing all messages with threats which were delivered by PPS|[]|
|Query End Time|string|None|False|The time at which the period queried for data ended|2021-04-21 12:00:00+00:00|
  
**families**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Clicks|integer|None|False|Total number of clicks on threats belong to this threat family|3|
|Name|string|None|False|Name of the threat family|phishing|
  
**clickStatistics**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Click Count|integer|None|False|Total number of clicks from this user in the time interval|4|
|Families|[]families|None|False|List of threat families|[]|
  
**identity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Customer User ID|string|None|False|Identifier associated with the user which was provided by the customer|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Department|string|None|False|Department of the user|Example department|
|Emails|[]string|None|False|List of email addresses associated with the user|["user@example.com"]|
|GUID|string|None|False|Unique identifier within Proofpoint's system|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Location|string|None|False|Location of the user|Example location|
|Name|string|None|False|Name of the user|Example User|
|Title|string|None|False|Title of the user|Example title|
|VIP|boolean|None|False|Whether the user has been identified as a VIP|False|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Click Statistics|clickStatistics|None|False|Click statistics|{}|
|Identity|identity|None|False|Identity|{}|
  
**urls**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Cluster Name|string|None|False|Cluster name|Example name|
|Decoded URL|string|None|False|Decoded URL|https://example.com|
|Encoded URL|string|None|False|Encoded URL|https://urldefense.proofpoint.com/v1/url?u=https://example.com|
|Error|string|None|False|Error details if any error occurs|Invalid URL - encoded URL is not a URL Defense URL|
|Message GUID|string|None|False|Message GUID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Recipient Email|string|None|False|Recipient email|user@example.com|
|Success|boolean|None|False|Success|True|
  
**platform**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name of platform|Win10|
|OS|string|None|False|Operating system|win|
|Version|string|None|False|Version of operating system|win10|
  
**evidenceType**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|Action performed|create|
|Blacklisted|boolean|None|False|Optional, whether the file or URL was blacklisted|False|
|Canonical Names|[]string|None|False|Optional, an array of CNAMEs which were associated with the hostname|["example.com"]|
|Domain|string|None|False|Which domain set the cookie|example.com|
|Host|string|None|False|The hostname being resolved|example.com|
|HTTP Status|integer|None|False|Optional, the HTTP status code which was produced when our sandbox visited the URL|200|
|Remote IP Address|string|None|False|The remote IP address being contacted|198.51.100.1|
|Resolved IP Addresses|[]string|None|False|Optional, an array of IP addresses which were resolved to the hostname|["198.51.100.1"]|
|Key|string|None|False|The location of the registry key being modified or the name of the cookie being set or deleted|Example|
|MD5|string|None|False|Optional, the MD5 sum of the item's content|9de5069c5afe602b2ea0a04b66beb2c0|
|Name|string|None|False|The name of the related item|Example name|
|Nameservers|[]string|None|False|Optional, the nameservers responsible for the hostname's domain|["example.nameserver.net"]|
|Nameservers List|[]string|None|False|Optional, the nameservers responsible for the hostname's domain|["example.nameserver.net"]|
|Offset|integer|None|False|Optional, the offset in bytes where the malicious content or URL was found|0|
|Path|string|None|False|Path to the file|b64.js|
|Port|integer|None|False|The remote IP port being contacted|25|
|Rule|string|None|False|Optional, the name of the static rule inside the sandbox which identified the related item|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|SHA256|string|None|False|The SHA256 hash of the item's content|f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...|
|Signature ID|integer|None|False|The identifier of the IDs rule which observed the malicious traffic|123456789|
|Size|integer|None|False|Optional, the size in bytes of the file content|4691|
|Type|string|None|False|The protocol being used - TCP or UDP|TCP|
|URL|string|None|False|URL|example.com|
|Value|string|None|False|The content of the cookie or registry key being set|Example|
  
**evidence**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Display|string|None|False|Friendly display string|File b64.js created|
|Malicious|boolean|None|False|Whether the evidence was used to reach a malicious verdict|False|
|Platforms|[]platform|None|False|Array of Platform objects|[]|
|Type|string|None|False|The evidence type|file|
|What|evidenceType|None|False|Map of values associated with the specific evidence type|{}|
  
**report**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Forensics|[]evidence|None|False|Array of Evidence objects|[]|
|ID|string|None|False|The identifier associated with the campaign or individual threat|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Name|string|None|False|The malicious URL, SHA256 hash of the malicious attachment, or campaign name|Emotet|
|Scope|string|None|False|Whether the report scope covers a campaign or an individual threat|CAMPAIGN|
|Type|string|None|False|The threat type|attachment|
  
**event**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|GUID|string|None|False|The ID of the message within PPS|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|QID|string|None|False|The queue ID of the message within PPS|381f1q3k77-1|
|Campaign ID|string|None|False|An identifier for the campaign of which the threat is a member|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|CC Addresses|[]string|None|False|A list of email addresses contained within the CC|["user@example.com"]|
|Classification|string|None|False|The threat category of the malicious URL|malware|
|Click IP|string|None|False|The external IP address of the user who clicked on the link|198.51.100.1|
|Click Time|string|None|False|The time the user clicked on the URL|2021-04-20 21:08:13+00:00|
|Cluster|string|None|False|The name of the PPS cluster which processed the message|example_hosted|
|Completely Rewritten|boolean|None|False|The rewrite status of the message|True|
|Event Type|string|None|False|The type of event logged|messageBlocked|
|From Address|[]string|None|False|The email address contained in the From|["user@example.com"]|
|Header From|string|None|False|The full content of the From|Example Sender <user@example.com>|
|Header Reply To|string|None|False|If present, the full content of the Reply-To|Example Sender <user@example.com>|
|ID|string|None|False|The unique id of the click|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Impostor Score|integer|None|False|The impostor score of the message. Higher scores indicate higher certainty|0|
|Malware Score|integer|None|False|The malware score of the message. Higher scores indicate higher certainty|0|
|Message ID|string|None|False|Message-ID extracted from the headers of the email message|<user@example.com>|
|Message Parts|[]messageParts|None|False|Details about parts of the message, including both message bodies and attachments|[]|
|Message Size|integer|None|False|The size in bytes of the message, including headers and attachments|2347|
|Message Time|string|None|False|When the message was delivered to the user or quarantined by PPS|2021-04-21 12:27:35+00:00|
|Modules Run|[]string|None|False|The list of PPS modules which processed the message|["spam", "pdr"]|
|Phish Score|integer|None|False|The phish score of the message. Higher scores indicate higher certainty|0|
|Policy Routes|[]string|None|False|The policy routes that the message matched during processing by PPS|["default_inbound"]|
|Quarantine Folder|string|None|False|The name of the folder which contains the quarantined message|Phish|
|Quarantine Rule|string|None|False|The name of the rule which quarantined the message|phish|
|Recipient|[]string|None|False|An array containing the email addresses of the SMTP (envelope) recipients|["user@example.com"]|
|Reply To Address|[]string|None|False|The email address contained in the Reply-To|["user@example.com"]|
|Sender|string|None|False|The email address of the SMTP (envelope) sender. The user-part is hashed. The domain-part is cleartext|user@example.com|
|Sender IP|string|None|False|The IP address of the sender|198.51.100.1|
|Spam Score|integer|None|False|The spam score of the message. Higher scores indicate higher certainty|0|
|Subject|string|None|False|The subject line of the message, if available|A phishy email|
|Threat ID|string|None|False|The unique identifier associated with this threat|f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...|
|Threat Status|string|None|False|The current state of the threat|active|
|Threat Time|string|None|False|Proofpoint identified the URL as a threat at this time|2021-04-20 21:08:38+00:00|
|Threat URL|string|None|False|A link to the entry on the TAP Dashboard for the particular threat|https://example.com|
|Threats Info Map|[]threatsInfoMap|None|False|Details about detected threats within the message|[]|
|To Address|[]string|None|False|A list of email addresses contained within the To|["user@example.com"]|
|URL|string|None|False|The malicious URL which was clicked|https://example.com|
|User Agent|string|None|False|The User-Agent header from the clicker's HTTP request|Mozilla/5.0 (Macintosh; Intel MAC OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36|
|X-Mailer|string|None|False|The content of the X-Mailer|Fenokohthk 9|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 4.1.12 - `Monitor Events`: Updated end_time property | Updated SDK to latest version (6.2.6)
* 4.1.11 - SDK Bump to 6.2.3 | `Monitor Events` task updated to handle requests outside of Proofpoint TAP API limits
* 4.1.10 - SDK Bump to 6.1.0 | Task Connection test added Update `Parse Tap Alert` to utilise BeautifulSoup resolving vulnerabilities
* 4.1.9 - Update connection fields to be required.
* 4.1.8 - Include SDK 5.4.9 | Task - Use cutoff of 7 days for first query, use cutoff of 1 hours for subsequent queries
* 4.1.7 - Include SDK 5.4.5 | Task - enforce query cutoff based on Proofpoint API max lookback | Task - toggle pagination when backfilling | Task - only store previous page of hashes.
* 4.1.6 - Include SDK 5.4.4 which prevents any potential memory leaks | first task lookup should only be 1 hour unless override supplied.
* 4.1.5 - Include SDK 5.4 which adds new task custom_config parameter.
* 4.1.4 - Remove hard coded env var from Dockerfile.
* 4.1.3 - Allow task `monitor_events` to poll from a set date in env var. | Fix issue where an MD5 value of None from Proofpoint was breaking the sorting of the list in the `monitor_events` task
* 4.1.2 - Update to latest plugin SDK to get task and exception logging
* 4.1.1 - Monitor Events Task: Update max lookback time, remove log cleaning, add debugging
* 4.1.0 - Update to latest plugin SDK
* 4.0.0 - Add Monitor Events task | Code refactor | Update plugin to be cloud enabled
* 3.1.2 - Fix invalid type for `blacklisted` in `evidence_type` custom output | Add a conversion to a boolean for `blacklisted` returned as an integer in Fetch Forensics action
* 3.1.1 - Fix decoding URLs with quotable encoding in URL Decode action
* 3.1.0 - Add new action Fetch Forensics
* 3.0.0 - Add `all` value to Threat Type and Threat Status inputs in Get Blocked Clicks, Get Permitted Clicks, Get Blocked Messages, Get Delivered Threats, Get All Threats actions
* 2.0.0 - Add new actions Get Blocked Clicks, Get Permitted Clicks, Get Blocked Messages, Get Delivered Threats, Get All Threats, Get Top Clickers, URL Decode
* 1.0.8 - Fix finding e-mail in `header_from` for e-mails addresses with `[.]`
* 1.0.7 - Update to use the `insightconnect-python-3-38-slim-plugin:4` Docker image | Update plugin.spec.yaml to include `cloud_ready`
* 1.0.6 - Parsing out GUID of the message into the output type
* 1.0.5 - Parsing out the View Threat Details link from emails to its own value
* 1.0.4 - New spec and help.md format for the Extension Library
* 1.0.3 - Fixed issue where headers were occasionally parsed improperly
* 1.0.2 - Sanitize example output in Parse Alert action documentation
* 1.0.1 - Fixed issue where TAP alerts with attachments are not parsed correctly
* 1.0.0 - Initial plugin

# Links

* [Proofpoint TAP](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection)

## References

* [Proofpoint TAP](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection)