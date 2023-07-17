# Description

[Proofpoint Targeted Attack Protection](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection)
(TAP) helps you stay ahead of attackers with an innovative approach that detects, analyzes and blocks advanced
threats before they reach your inbox. This plugin enables users to parse TAP alerts.

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

* Proofpoint TAP [service principal and secret](https://ptr-docs.proofpoint.com/ptr-guides/integrations-files/ptr-tap/#generate-tap-service-credentials) is required for all actions except Parse Alert

# Supported Product Versions

* Proofpoint TAP API v2
* Tested on 2023-06-22

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|secret|credential_secret_key|None|False|The TAP secret for basic authentication API interaction|None|30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050|
|servicePrincipal|credential_secret_key|None|False|The TAP service principal for basic authentication API interaction|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|

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

This action is used to fetch forensic evidence about individual threats or campaigns. Either 'threatId' or 'campaignId' should be specified.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|campaignId|string|None|False|Campaign identifier|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|includeCampaignForensics|boolean|None|False|Include campaign forensics in threats. This parameter works only with Threat ID|None|False|
|threatId|string|None|False|Threat identifier|None|30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050|

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
|----|----|--------|-----------|-------|
|generated|string|True|ISO8601-formatted datetime corresponding to the time this report was generated|2021-06-27 19:58:04.283000+00:00|
|reports|[]report|True|Reported threats|[]|

Example output:

```
{
  "generated": "2021-06-27T19:58:04.283Z",
  "reports": [
    {
      "scope": "CAMPAIGN",
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "name": "Emotet",
      "forensics": [
        {
          "type": "behavior",
          "display": "Test",
          "engine": "iee",
          "malicious": false,
          "note": "Test2",
          "time": 0,
          "what": {
            "rule": "behavior_123456789"
          },
          "platforms": [
            {
              "name": "Win10",
              "os": "win",
              "version": "win10"
            }
          ]
        }
      ]
    }
  ]
}
```

#### URL Decode

This action is used to decode URLs which have been rewritten by TAP to their original, target URL.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|urls|[]string|None|True|List of URLs to decode|None|["https://example.com", "https://example2.com"]|

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
|----|----|--------|-----------|-------|
|urls|[]urls|False|Decoded URLs|[]|

Example output:

```
{
  "urls": [
    {
      "encodedUrl": "https://urldefense.proofpoint.com/v1/url?u=http://www.example.com/&amp;k=oIvRg1%2BdGAgOoM1BIlLLqw%3D%3D%0A&amp;r=IKM5u8%2B%2F%2Fi8EBhWOS%2BqGbTqCC%2BrMqWI%2FVfEAEsQO%2F0Y%3D%0A&amp;m=Ww6iaHO73mDQpPQwOwfLfN8WMapqHyvtu8jM8SjqmVQ%3D%0A&amp;s=d3583cfa53dade97025bc6274c6c8951dc29fe0f38830cf8e5a447723b9f1c9a\"",
      "decodedUrl": "http://www.example.com/",
      "success": true
    }
  ]
}
```

#### Get Top Clickers

This action is used to fetch the identities and attack index of the top clickers within your organization for a given period.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|window|integer|None|True|An integer indicating how many days the data should be retrieved for|[14, 30, 90]|14|

Example input:

```
{
  "window": 14
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|interval|string|False|An ISO8601-formatted interval showing what time the response was calculated for|2023-03-07T06:01:00Z/2023-06-05T06:01:00Z|
|totalTopClickers|integer|False|An integer describing the total number of top clickers in the time interval|2|
|users|[]user|False|An array of user objects that contain information about the user's identity and statistics of the clicking behavior|[]|

Example output:

```
{
  "interval": "2023-03-07T06:01:00Z/2023-06-05T06:01:00Z",
  "totalTopClickers": 2,
  "users": [
    {
      "clickStatistics": {
        "families": [
          {
            "clicks": 28,
            "name": "Malware"
          }
        ],
        "clickCount": 28
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

#### Get Permitted Clicks

This action is used to fetch events for clicks to malicious URLs permitted in the specified time period.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|threatStatus|string|all|True|The threat statuses which will be returned in the data|['active', 'cleared', 'falsePositive', 'all']|active|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|
|url|string|None|False|The URL for which the results will be returned. Returns all results if left empty|None|https://example.com|

Example input:

```
{
  "threatStatus": "active",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00",
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|permittedClicks|True|The results containing permitted clicks|{}|

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
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
      }
    ],
    "queryEndTime": "2021-04-21T13:00:00Z"
  }
}
```

#### Get Delivered Threats

This action is used to fetch events for messages delivered in the specified time period which contained a known threat.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|subject|string|None|False|The subject of the email for which the results will be returned (performs a full-match lookup). Returns all results if left empty|None|A phishy email|
|threatStatus|string|all|True|The threat statuses which will be returned in the data|['active', 'cleared', 'falsePositive', 'all']|active|
|threatType|string|all|True|The threat type which will be returned in the data|['url', 'attachment', 'messageText', 'all']|url|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|

Example input:

```
{
  "subject": "A phishy email",
  "threatStatus": "active",
  "threatType": "url",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|deliveredThreats|True|The results containing delivered threats|{}|

Example output:

```
{
  "results": {
    "messagesDelivered": [
      {
        "messageParts": [
          {
            "disposition": "inline",
            "filename": "text-rfc822-headers",
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
            "oContentType": "text/plain",
            "sha256": "12aea580d129035f1e424484a818bec62455db3f5632cf5bac...",
            "contentType": "text/plain"
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
        "threatsInfoMap": [
          {
            "threatID": "22a340fea5cb89908a7576b5e387ce6b296a61a8ac35aac574...",
            "threatStatus": "active",
            "threatTime": "2021-04-13T14:45:53.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com",
            "classification": "phish",
            "threat": "starbrandb2bedm.xyz/emm/"
          },
          {
            "threat": "starbrandb2bedm.xyz/emm/index.php",
            "threatID": "bcef1812236a940d5e7bb743439e2dc883d3e666124896c339...",
            "threatStatus": "active",
            "threatTime": "2021-04-13T08:51:37.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com",
            "classification": "phish"
          }
        ],
        "malwareScore": 0,
        "messageID": "<user@example.com>",
        "policyRoutes": [
          "allow_relay",
          "firewallsafe"
        ],
        "subject": "A phishy email",
        "senderIP": "198.51.100.1",
        "spamScore": 0,
        "completelyRewritten": false,
        "modulesRun": [
          "access"
        ],
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "messageTime": "2021-04-21T17:26:30.000Z",
        "toAddresses": [
          "info-cheri=user@example.com"
        ],
        "headerFrom": "Mail Delivery Subsystem <user@example.com>",
        "impostorScore": 0,
        "recipient": [
          "info-cheri=user@example.com"
        ],
        "GUID": "sVfuaRyZ59_UnD2m8RX9i7uGsW4pHcUX",
        "phishScore": 0,
        "fromAddress": [
          "user@example.com"
        ],
        "QID": "13LHPoqE012261",
        "cluster": "proofpointdemo_cloudadminuidemo_hosted"
      }
    ],
    "queryEndTime": "2021-04-21T18:00:00Z"
  }
}
```

#### Get Blocked Messages

This action is used to fetch events for messages blocked in the specified time period which contained a known threat.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|subject|string|None|False|The subject of the email for which the results will be returned (performs a full-match lookup). Returns all results if left empty|None|A phishy email|
|threatStatus|string|all|True|The threat statuses which will be returned in the data|['active', 'cleared', 'falsePositive', 'all']|active|
|threatType|string|all|True|The threat type which will be returned in the data|['url', 'attachment', 'messageText', 'all']|url|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|

Example input:

```
{
  "subject": "A phishy email",
  "threatStatus": "active",
  "threatType": "url",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|blockedMessages|True|The results containing blocked messages|{}|

Example output:

```
{
  "results": {
    "messagesBlocked": [
      {
        "headerFrom": "\"amazon\" <user@example.com>",
        "impostorScore": 0,
        "sender": "user@example.com",
        "QID": "381f1q3k77-1",
        "completelyRewritten": false,
        "malwareScore": 0,
        "modulesRun": [
          "av",
          "spf"
        ],
        "phishScore": 100,
        "policyRoutes": [
          "default_inbound",
          "allow_relay"
        ],
        "senderIP": "198.51.100.1",
        "fromAddress": [
          "user@example.com"
        ],
        "messageParts": [
          {
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
            "oContentType": "text/html",
            "sha256": "7e38804bf4e90803cc6ef24b6c5e79dd9b9d84b48b23f04ea5...",
            "contentType": "text/html",
            "disposition": "inline",
            "filename": "text.html"
          },
          {
            "sha256": "b31b0a1f2b61146af3377833db02811d9af26596e9b5e81457...",
            "contentType": "text/plain",
            "disposition": "inline",
            "filename": "text.txt",
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
            "oContentType": "text/plain"
          }
        ],
        "toAddresses": [
          "user@example.com"
        ],
        "cluster": "proofpointdemo_cloudadminuidemo_hosted",
        "recipient": [
          "user@example.com"
        ],
        "xmailer": "Fenokohthk 9",
        "spamScore": 100,
        "GUID": "fA8S1YIRh2taWGdoS02QyNccz985vY2D",
        "messageID": "<user@example.com>",
        "messageSize": 26539,
        "messageTime": "2021-04-21T12:27:35.000Z",
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "quarantineFolder": "Phish",
        "quarantineRule": "phish",
        "subject": "A phishy email",
        "threatsInfoMap": [
          {
            "threatStatus": "active",
            "threatTime": "2021-04-20T09:31:34.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com",
            "classification": "phish",
            "threat": "198.51.100.1/ap/signin",
            "threatID": "0e10e285491d55c6dba3016e31243af7dabf5842433a3c4735..."
          },
          {
            "threat": "https://example.com",
            "threatID": "378a3a7731552a2f06349d066f2853f833fa6094ed660d8789...",
            "threatStatus": "active",
            "threatTime": "2021-04-20T09:29:43.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com",
            "classification": "phish"
          }
        ]
      }
    ],
    "queryEndTime": "2021-04-21T13:00:00Z"
  }
}
```

#### Get All Threats

This action is used to fetch events for all clicks and messages relating to known threats within the specified time period.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|threatStatus|string|all|True|The threat statuses which will be returned in the data|['active', 'cleared', 'falsePositive', 'all']|active|
|threatType|string|all|True|The threat type which will be returned in the data|['url', 'attachment', 'messageText', 'all']|url|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|

Example input:

```
{
  "threatStatus": "active",
  "threatType": "url",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|allThreats|True|The results containing all threats|{}|

Example output:

```
{
  "results": {
    "clicksBlocked": [],
    "clicksPermitted": [],
    "messagesBlocked": [
      {
        "cluster": "proofpointdemo_cloudadminuidemo_hosted",
        "impostorScore": 0,
        "threatsInfoMap": [
          {
            "threat": "klongkru.ac.th/",
            "threatID": "d22be456cbc0a0e5d900696c36c92c547bea13cc76d32b63ed...",
            "threatStatus": "active",
            "threatTime": "2021-02-09T15:59:49.000Z",
            "threatType": "url",
            "threatUrl": "https://example.com",
            "classification": "phish"
          }
        ],
        "QID": "3823t51rm5-1",
        "messageTime": "2021-04-21T11:15:26.000Z",
        "spamScore": 100,
        "toAddresses": [
          "user@example.com"
        ],
        "GUID": "gk6qK0AUnJMM-0iF10DbYBA3lZgxMALt",
        "completelyRewritten": false,
        "modulesRun": [
          "av",
          "spf"
        ],
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
            "oContentType": "text/plain",
            "sha256": "f95b2809b1ecd4dd6de4e2318340388f8007c7ac76778532c4...",
            "contentType": "text/plain",
            "disposition": "inline",
            "filename": "text.txt",
            "md5": "9de5069c5afe602b2ea0a04b66beb2c0"
          }
        ],
        "messageSize": 9982,
        "subject": "Mail delivery failed: returning message to sender",
        "fromAddress": [
          "user@example.com"
        ],
        "headerFrom": "Mail Delivery System <user@example.com>",
        "quarantineFolder": "Phish",
        "recipient": [
          "user@example.com"
        ],
        "malwareScore": 0,
        "policyRoutes": [
          "default_inbound",
          "allow_relay"
        ],
        "messageID": "<user@example.com>",
        "phishScore": 100,
        "quarantineRule": "phish",
        "senderIP": "198.51.100.1",
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
      }
    ],
    "messagesDelivered": [],
    "queryEndTime": "2021-04-21T12:00:00Z"
  }
}
```

#### Get Blocked Clicks

This action is used to fetch events for clicks to malicious URLs blocked in the specified time period.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|threatStatus|string|all|True|The threat statuses which will be returned in the data|['active', 'cleared', 'falsePositive', 'all']|active|
|timeEnd|date|None|False|The end of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T22:00:00Z. If left empty, it will be calculated from the 'time_start' parameter. If the 'time_start' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T22:00:00+00:00|
|timeStart|date|None|False|The start of the data retrieval period as ISO8601-formatted date e.g 2021-04-20T21:00:00Z. If left empty, it will be calculated from the 'time_end' parameter. If the 'time_end' parameter is empty, data from one hour before the current API server time will be returned. The minimum time range is thirty seconds. The maximum time range is one hour|None|2021-04-20T21:00:00+00:00|
|url|string|None|False|The URL for which the results will be returned. Returns all results if left empty|None|https://example.com|

Example input:

```
{
  "threatStatus": "active",
  "timeEnd": "2021-04-20T22:00:00+00:00",
  "timeStart": "2021-04-20T21:00:00+00:00",
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|blockedClicks|True|The results containing blocked clicks|{}|

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
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
      }
    ],
    "queryEndTime": "2021-04-21T13:00:00Z"
  }
}
```

#### Parse Alert

This action is used to parse a TAP alert. It is often used to parse the indicators from a forwarded e-mail containing a TAP alert. Note that this action does not require the connection to be configured.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|tapAlert|string|None|True|A Proofpoint TAP alert|None|`proofpoint      URL DefenseAn end user has clicked on a link in their email which Proofpoint now recog=nizes as malicious. Details about the threat, the permitted click, and the =message containing the link are below:ThreatURL      hxxp://ec2-12-23-34-123[.]compute-1[.]amazonaws[.]com/[.]0[.]/ja=ke[.]user@example[.]comCategory         phishCondemnation Time        2020-04-27T12:22:54ZMessageTime Delivered   2020-04-27T09:54:49ZRecipient        user@example.comSubject  =97Sender   =97Header From      =97Header ReplyTo   =97Message-ID       =97Message-GUID     -JsyOYf--Yt7cR-ctdIo7RuUiK9kSECEThreat-ID        6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3da6f4e=798a39Sender IP        =97Message Size     =97ClickTime     2020-04-27T09:54:49ZSource IP        192.168.50.100User Agent       Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0)= like GeckoView Threat Details<https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789=-ef71-f3998c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a75=9e7db48f3da6f4e798a39?linkOrigin=3Dnotif>You are receiving this message because you are subscribed to alerts from th=e Threat Insight Dashboard. Update your subscription preferences<https://th=reatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f3998c3e92e3/settings/pr=ivileges?linkOrigin=3Dnotif> to stop receiving these notifications.Proofpoint Targeted Attack Protectionproofpoint--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_Content-Type: text/html; charset="Windows-1252"Content-ID: <user@example.com>Content-Transfer-Encoding: quoted-printable<html><head><meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3DWindows-1=252"></head><body style=3D"margin:0px"><div style=3D"background:#f1f2f2;font-family:Arial;font-size:13px;color:#66=6666"><div style=3D"background:white"><div style=3D"max-width:720px;margin:auto;padding:0"><table style=3D"width:100%;height:60px;font-family:inherit;font-size:inheri=t;color:inherit"><tbody><tr><td><b style=3D"font-size:22px;color:black">proofpoint</b> </td><td align=3D"right">URL Defense</td></tr><tr></tr></tbody></table></div></div><div style=3D"max-width:720px;margin:auto;padding:20px 0">An end user has c=licked on a link in their email which Proofpoint now recognizes as maliciou=s. Details about the threat, the permitted click, and the message containin=g the link are below:<p><b>Threat</b></p><p><table border=3D"1" style=3D"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit" cellspa=cing=3D"0" cellpadding=3D"8"><col width=3D"150"><col><tbody><tr valign=3D"top"><td><b>URL</b></td><td style=3D"background:white">hxxp://ec2-12-34-56-123[.]compute-1[.]amazo=naws[.]com/[.]0[.]/user@example[.]com</td></tr><tr valign=3D"top"><td><b>Category</b></td><td style=3D"background:white">phish</td></tr><tr valign=3D"top"><td><b>Condemnation Time</b></td><td style=3D"background:white">2020-04-27T12:22:54Z</td></tr></tbody></table></p><p><b>Message</b></p><p><table border=3D"1" style=3D"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit" cellspa=cing=3D"0" cellpadding=3D"8"><col width=3D"150"><col><tbody><tr valign=3D"top"><td><b>Time Delivered</b></td><td style=3D"background:white">2020-04-27T09:54:49Z</td></tr><tr valign=3D"top"><td><b>Recipient</b></td><td style=3D"background:white">user@example.com</td></tr><tr valign=3D"top"><td><b>Subject</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Sender</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Header From</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Header ReplyTo</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Message-ID</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Message-GUID</b></td><td style=3D"background:white">-JsyOYf--Yt7cR-ctdIo7RuUiK9kSECE</td></tr><tr valign=3D"top"><td><b>Threat-ID</b></td><td style=3D"background:white">6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759=e7db48f3da6f4e798a39</td></tr><tr valign=3D"top"><td><b>Sender IP</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Message Size</b></td><td style=3D"background:white">=97</td></tr></tbody></table></p><p><b>Click</b></p><p><table border=3D"1" style=3D"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit" cellspa=cing=3D"0" cellpadding=3D"8"><col width=3D"150"><col><tbody><tr valign=3D"top"><td><b>Time</b></td><td style=3D"background:white">2020-04-27T09:54:49Z</td></tr><tr valign=3D"top"><td><b>Source IP</b></td><td style=3D"background:white">192.168.50.100</td></tr><tr valign=3D"top"><td><b>User Agent</b></td><td style=3D"background:white">Mozilla/5.0 (Windows NT 10.0; WOW64; Trident=/7.0; rv:11.0) like Gecko</td></tr></tbody></table></p><p></p><div style=3D"width:120px;margin:40px auto;padding:8px 32px;background:#06a=2d5;text-align:center"><a href=3D"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3=da6f4e798a39?linkOrigin=3Dnotif" style=3D"color:white;text-decoration:none"=>View Threat Details</a></div><div style=3D"font-size:11px;border-bottom:solid 1px #d1d3d4;padding-bottom=:8px;">You are receiving this message because you are subscribed to alerts =from the Threat Insight Dashboard.<a href=3D"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/settings/privileges?linkOrigin=3Dnotif">Update your subscription preferences</a> to stop receiving these notificati=ons. </div><p></p><div style=3D"font-size:11px;text-align:center;padding-bottom:30px">Proofpo=int Targeted Attack Protection<p><b>proofpoint</b> </p></div></div></div></body></html>--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_--`|

Example input:

```
{
  "tapAlert": "proofpoint      URL DefenseAn end user has clicked on a link in their email which Proofpoint now recog=nizes as malicious. Details about the threat, the permitted click, and the =message containing the link are below:ThreatURL      hxxp://ec2-12-23-34-123[.]compute-1[.]amazonaws[.]com/[.]0[.]/ja=ke[.]user@example[.]comCategory         phishCondemnation Time        2020-04-27T12:22:54ZMessageTime Delivered   2020-04-27T09:54:49ZRecipient        user@example.comSubject  =97Sender   =97Header From      =97Header ReplyTo   =97Message-ID       =97Message-GUID     -JsyOYf--Yt7cR-ctdIo7RuUiK9kSECEThreat-ID        6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3da6f4e=798a39Sender IP        =97Message Size     =97ClickTime     2020-04-27T09:54:49ZSource IP        192.168.50.100User Agent       Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0)= like GeckoView Threat Details<https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789=-ef71-f3998c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a75=9e7db48f3da6f4e798a39?linkOrigin=3Dnotif>You are receiving this message because you are subscribed to alerts from th=e Threat Insight Dashboard. Update your subscription preferences<https://th=reatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f3998c3e92e3/settings/pr=ivileges?linkOrigin=3Dnotif> to stop receiving these notifications.Proofpoint Targeted Attack Protectionproofpoint--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_Content-Type: text/html; charset=\"Windows-1252\"Content-ID: <user@example.com>Content-Transfer-Encoding: quoted-printable<html><head><meta http-equiv=3D\"Content-Type\" content=3D\"text/html; charset=3DWindows-1=252\"></head><body style=3D\"margin:0px\"><div style=3D\"background:#f1f2f2;font-family:Arial;font-size:13px;color:#66=6666\"><div style=3D\"background:white\"><div style=3D\"max-width:720px;margin:auto;padding:0\"><table style=3D\"width:100%;height:60px;font-family:inherit;font-size:inheri=t;color:inherit\"><tbody><tr><td><b style=3D\"font-size:22px;color:black\">proofpoint</b> </td><td align=3D\"right\">URL Defense</td></tr><tr></tr></tbody></table></div></div><div style=3D\"max-width:720px;margin:auto;padding:20px 0\">An end user has c=licked on a link in their email which Proofpoint now recognizes as maliciou=s. Details about the threat, the permitted click, and the message containin=g the link are below:<p><b>Threat</b></p><p><table border=3D\"1\" style=3D\"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit\" cellspa=cing=3D\"0\" cellpadding=3D\"8\"><col width=3D\"150\"><col><tbody><tr valign=3D\"top\"><td><b>URL</b></td><td style=3D\"background:white\">hxxp://ec2-12-34-56-123[.]compute-1[.]amazo=naws[.]com/[.]0[.]/user@example[.]com</td></tr><tr valign=3D\"top\"><td><b>Category</b></td><td style=3D\"background:white\">phish</td></tr><tr valign=3D\"top\"><td><b>Condemnation Time</b></td><td style=3D\"background:white\">2020-04-27T12:22:54Z</td></tr></tbody></table></p><p><b>Message</b></p><p><table border=3D\"1\" style=3D\"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit\" cellspa=cing=3D\"0\" cellpadding=3D\"8\"><col width=3D\"150\"><col><tbody><tr valign=3D\"top\"><td><b>Time Delivered</b></td><td style=3D\"background:white\">2020-04-27T09:54:49Z</td></tr><tr valign=3D\"top\"><td><b>Recipient</b></td><td style=3D\"background:white\">user@example.com</td></tr><tr valign=3D\"top\"><td><b>Subject</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Sender</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Header From</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Header ReplyTo</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Message-ID</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Message-GUID</b></td><td style=3D\"background:white\">-JsyOYf--Yt7cR-ctdIo7RuUiK9kSECE</td></tr><tr valign=3D\"top\"><td><b>Threat-ID</b></td><td style=3D\"background:white\">6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759=e7db48f3da6f4e798a39</td></tr><tr valign=3D\"top\"><td><b>Sender IP</b></td><td style=3D\"background:white\">=97</td></tr><tr valign=3D\"top\"><td><b>Message Size</b></td><td style=3D\"background:white\">=97</td></tr></tbody></table></p><p><b>Click</b></p><p><table border=3D\"1\" style=3D\"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit\" cellspa=cing=3D\"0\" cellpadding=3D\"8\"><col width=3D\"150\"><col><tbody><tr valign=3D\"top\"><td><b>Time</b></td><td style=3D\"background:white\">2020-04-27T09:54:49Z</td></tr><tr valign=3D\"top\"><td><b>Source IP</b></td><td style=3D\"background:white\">192.168.50.100</td></tr><tr valign=3D\"top\"><td><b>User Agent</b></td><td style=3D\"background:white\">Mozilla/5.0 (Windows NT 10.0; WOW64; Trident=/7.0; rv:11.0) like Gecko</td></tr></tbody></table></p><p></p><div style=3D\"width:120px;margin:40px auto;padding:8px 32px;background:#06a=2d5;text-align:center\"><a href=3D\"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3=da6f4e798a39?linkOrigin=3Dnotif\" style=3D\"color:white;text-decoration:none\"=>View Threat Details</a></div><div style=3D\"font-size:11px;border-bottom:solid 1px #d1d3d4;padding-bottom=:8px;\">You are receiving this message because you are subscribed to alerts =from the Threat Insight Dashboard.<a href=3D\"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/settings/privileges?linkOrigin=3Dnotif\">Update your subscription preferences</a> to stop receiving these notificati=ons. </div><p></p><div style=3D\"font-size:11px;text-align:center;padding-bottom:30px\">Proofpo=int Targeted Attack Protection<p><b>proofpoint</b> </p></div></div></div></body></html>--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_--"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|tapResults|False|Proofpoint TAP results|{}|

Example output:

```
{
  "results": {
    "threat": {
      "attachmentSha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
      "category": "Malware",
      "condemnationTime": "2019-01-10T12:34:05Z",
      "threatDetailsUrl": "https://example.com/9de5069c5afe602b2ea0a04b66beb2c0/threat/email/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f?linkOrigin=notif"
    },
    "message": {
      "timeDelivered": "2019-01-10T12:10:21Z",
      "recipients": "user@example.com",
      "subject": "January Invoice",
      "sender": "user@example.com",
      "headerFrom": "Bob",
      "headerReplyto": "user@example.com",
      "messageId": "user@example.com",
      "senderIp": "198.51.100.1",
      "messageSize": "152 KB",
      "messageGuid": "9de5069c5afe602b2ea0a04b66beb2c0",
      "threatId": "9de5069c5afe602b2ea0a04b66beb2c0"
    },
    "browser": {
      "time": "2020-05-11T11:01:13Z",
      "sourceIp": "198.51.100.1",
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Tasks

#### Monitor Events

This task will monitor events for all clicks and messages relating to known threats.

##### Input

_This task does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|events|[]event|True|List of all events|[]|

Example output:
```
[
  {
    "eventType": "messageBlocked",
    "ccAddresses": [
      "user@example.com"
    ],
    "clusterId": "example_hosted",
    "completelyRewritten": true,
    "fromAddress": [
      "user@example.com"
    ],
    "GUID": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "headerFrom": "\"example\" <user@example.com> ",
    "headerReplyTo": "user@example.com",
    "impostorScore": 0,
    "malwareScore": 0,
    "messageID": "<user@example.com>",
    "messageParts": [
      {
        "disposition": "inline",
        "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
        "md5": "9de5069c5afe602b2ea0a04b66beb2c0",
        "filename": "text.txt",
        "oContentType": "text/plain",
        "contentType": "text/plain"
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
    "QID": "9de5069c5afe602b2ea0a04b66beb2c0",
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
        "threat": "example.ab.cd/",
        "threatID": "9de5069c5afe602b2ea0a04b66beb2c0",
        "threatStatus": "active",
        "threatTime": "2021-02-09T15:59:49.000Z",
        "threatType": "url",
        "threatUrl": "https://example.com",
        "classification": "phish"
      }
    ],
    "toAddresses": [
      "user@example.com"
    ]
  },
  {
    "eventType": "clickBlocked",
    "campaignId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "classification": "malware",
    "clickIP": "198.51.100.1",
    "clickTime": "2021-04-20T21:08:13.000Z",
    "GUID": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "recipient": "user@example.com",
    "sender": "user@example.com",
    "senderIP": "198.51.100.1",
    "threatID": "9de5069c5afe602b2ea0a04b66beb2c0",
    "threatTime": "2016-06-24T19:17:46.000Z",
    "threatURL": "https://example.com",
    "threatStatus": "active",
    "url": "https://example.com",
    "userAgent": "Mozilla/5.0(WindowsNT6.1;WOW64;rv:27.0)Gecko/20100101Firefox/27.0"
  }
]
```

### Custom Output Types

#### allThreats

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Clicks Blocked|[]clicks|False|An array containing all clicks to URL threats which were blocked|
|Clicks Permitted|[]clicks|False|An array containing all clicks to URL threats which were permitted|
|Messages Blocked|[]messages|False|An array containing all messages with threats which were quarantined by PPS|
|Messages Delivered|[]messages|False|An array containing all messages with threats which were delivered by PPS|
|Query End Time|string|False|The time at which the period queried for data ended|

#### blockedClicks

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Clicks Blocked|[]clicks|False|An array containing all clicks to URL threats which were blocked|
|Query End Time|string|False|The time at which the period queried for data ended|

#### blockedMessages

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Messages Blocked|[]messages|False|An array containing all messages with threats which were quarantined by PPS|
|Query End Time|string|False|The time at which the period queried for data ended|

#### browser

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Source IP|string|False|Source IP|
|Time|string|False|Time|
|User Agent|string|False|User agent string|

#### clickStatistics

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Click Count|integer|False|Total number of clicks from this user in the time interval|
|Families|[]families|False|List of threat families|

#### clicks

|Name|Type|Required|Description|
|----|----|--------|-----------|
|GUID|string|False|The ID of the message within PPS|
|Campaign ID|string|False|An identifier for the campaign of which the threat is a member|
|Classification|string|False|The threat category of the malicious URL|
|Click IP|string|False|The external IP address of the user who clicked on the link|
|Click Time|string|False|The time the user clicked on the URL|
|ID|string|False|The unique ID of the click|
|Recipient|string|False|The email address of the recipient|
|Sender|string|False|The email address of the sender. The user-part is hashed. The domain-part is cleartext|
|Sender IP|string|False|The IP address of the sender|
|Threat ID|string|False|The unique identifier associated with this threat|
|Threat Status|string|False|The current state of the threat|
|Threat Time|string|False|Proofpoint identified the URL as a threat at this time|
|Threat URL|string|False|A link to the entry on the TAP Dashboard for the particular threat|
|URL|string|False|The malicious URL which was clicked|
|User Agent|string|False|The User-Agent header from the clicker's HTTP request|

#### deliveredThreats

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Messages Delivered|[]messages|False|An array containing all messages with threats which were delivered by PPS|
|Query End Time|string|False|The time at which the period queried for data ended|

#### event

|Name|Type|Required|Description|
|----|----|--------|-----------|
|GUID|string|False|The ID of the message within PPS|
|QID|string|False|The queue ID of the message within PPS|
|Campaign ID|string|False|An identifier for the campaign of which the threat is a member|
|CC Addresses|[]string|False|A list of email addresses contained within the CC|
|Classification|string|False|The threat category of the malicious URL|
|Click IP|string|False|The external IP address of the user who clicked on the link|
|Click Time|string|False|The time the user clicked on the URL|
|Cluster|string|False|The name of the PPS cluster which processed the message|
|Completely Rewritten|boolean|False|The rewrite status of the message|
|Event Type|string|False|The type of event logged|
|From Address|[]string|False|The email address contained in the From|
|Header From|string|False|The full content of the From|
|Header Reply To|string|False|If present, the full content of the Reply-To|
|ID|string|False|The unique id of the click|
|Impostor Score|integer|False|The impostor score of the message. Higher scores indicate higher certainty|
|Malware Score|integer|False|The malware score of the message. Higher scores indicate higher certainty|
|Message ID|string|False|Message-ID extracted from the headers of the email message|
|Message Parts|[]messageParts|False|Details about parts of the message, including both message bodies and attachments|
|Message Size|integer|False|The size in bytes of the message, including headers and attachments|
|Message Time|string|False|When the message was delivered to the user or quarantined by PPS|
|Modules Run|[]string|False|The list of PPS modules which processed the message|
|Phish Score|integer|False|The phish score of the message. Higher scores indicate higher certainty|
|Policy Routes|[]string|False|The policy routes that the message matched during processing by PPS|
|Quarantine Folder|string|False|The name of the folder which contains the quarantined message|
|Quarantine Rule|string|False|The name of the rule which quarantined the message|
|Recipient|[]string|False|An array containing the email addresses of the SMTP (envelope) recipients|
|Reply To Address|[]string|False|The email address contained in the Reply-To|
|Sender|string|False|The email address of the SMTP (envelope) sender. The user-part is hashed. The domain-part is cleartext|
|Sender IP|string|False|The IP address of the sender|
|Spam Score|integer|False|The spam score of the message. Higher scores indicate higher certainty|
|Subject|string|False|The subject line of the message, if available|
|Threat ID|string|False|The unique identifier associated with this threat|
|Threat Status|string|False|The current state of the threat|
|Threat Time|string|False|Proofpoint identified the URL as a threat at this time|
|Threat URL|string|False|A link to the entry on the TAP Dashboard for the particular threat|
|Threats Info Map|[]threatsInfoMap|False|Details about detected threats within the message|
|To Address|[]string|False|A list of email addresses contained within the To|
|URL|string|False|The malicious URL which was clicked|
|User Agent|string|False|The User-Agent header from the clicker's HTTP request|
|X-Mailer|string|False|The content of the X-Mailer|

#### evidence

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Display|string|False|Friendly display string|
|Malicious|boolean|False|Whether the evidence was used to reach a malicious verdict|
|Platforms|[]platform|False|Array of Platform objects|
|Type|string|False|The evidence type|
|What|evidenceType|False|Map of values associated with the specific evidence type|

#### evidenceType

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action|string|False|Action performed|
|Blacklisted|boolean|False|Optional, whether the file or URL was blacklisted|
|Canonical Names|[]string|False|Optional, an array of CNAMEs which were associated with the hostname|
|Domain|string|False|Which domain set the cookie|
|Host|string|False|The hostname being resolved|
|HTTP Status|integer|False|Optional, the HTTP status code which was produced when our sandbox visited the URL|
|Remote IP Address|string|False|The remote IP address being contacted|
|Resolved IP Addresses|[]string|False|Optional, an array of IP addresses which were resolved to the hostname|
|Key|string|False|The location of the registry key being modified or the name of the cookie being set or deleted|
|MD5|string|False|Optional, the MD5 sum of the item's content|
|Name|string|False|The name of the related item|
|Nameservers|[]string|False|Optional, the nameservers responsible for the hostname's domain|
|Nameservers List|[]string|False|Optional, the nameservers responsible for the hostname's domain|
|Offset|integer|False|Optional, the offset in bytes where the malicious content or URL was found|
|Path|string|False|Path to the file|
|Port|integer|False|The remote IP port being contacted|
|Rule|string|False|Optional, the name of the static rule inside the sandbox which identified the related item|
|SHA256|string|False|The SHA256 hash of the item's content|
|Signature ID|integer|False|The identifier of the IDs rule which observed the malicious traffic|
|Size|integer|False|Optional, the size in bytes of the file content|
|Type|string|False|The protocol being used - TCP or UDP|
|URL|string|False|URL|
|Value|string|False|The content of the cookie or registry key being set|

#### families

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Clicks|integer|False|Total number of clicks on threats belong to this threat family|
|Name|string|False|Name of the threat family|

#### identity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Customer User ID|string|False|Identifier associated with the user which was provided by the customer|
|Department|string|False|Department of the user|
|Emails|[]string|False|List of email addresses associated with the user|
|GUID|string|False|Unique identifier within Proofpoint's system|
|Location|string|False|Location of the user|
|Name|string|False|Name of the user|
|Title|string|False|Title of the user|
|VIP|boolean|False|Whether the user has been identified as a VIP|

#### message

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Header From|string|False|Header from|
|Header Reply To|string|False|Header reply to|
|Message GUID|string|False|Message GUID|
|Message ID|string|False|Message ID|
|Message Size|string|False|Message size|
|Recipients|string|False|Recipients|
|Sender|string|False|Sender|
|Sender IP|string|False|Sender IP|
|Subject|string|False|Subject|
|Threat ID|string|False|Unique identifier for this threat|
|Time Delivered|string|False|Time delivered|

#### messageParts

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Content Type|string|False|The true, detected Content-Type of the messagePart|
|Disposition|string|False|If the value is 'inline', the messagePart is a message body. If the value is 'attached', the messagePart is an attachment|
|Filename|string|False|The filename of the messagePart|
|MD5|string|False|The MD5 hash of the messagePart contents|
|Declared Content Type|string|False|The declared Content-Type of the messagePart|
|Sandbox Status|string|False|The verdict returned by the sandbox during the scanning process|
|SHA256|string|False|The SHA256 hash of the messagePart contents|

#### messages

|Name|Type|Required|Description|
|----|----|--------|-----------|
|GUID|string|False|The ID of the message within PPS|
|QID|string|False|The queue ID of the message within PPS|
|CC Addresses|[]string|False|A list of email addresses contained within the CC|
|Cluster|string|False|The name of the PPS cluster which processed the message|
|Completely Rewritten|boolean|False|The rewrite status of the message|
|From Address|[]string|False|The email address contained in the From|
|Header From|string|False|The full content of the From|
|Header Reply To|string|False|If present, the full content of the Reply-To|
|Impostor Score|integer|False|The impostor score of the message. Higher scores indicate higher certainty|
|Malware Score|integer|False|The malware score of the message. Higher scores indicate higher certainty|
|Message ID|string|False|Message-ID extracted from the headers of the email message|
|Message Parts|[]messageParts|False|Details about parts of the message, including both message bodies and attachments|
|Message Size|integer|False|The size in bytes of the message, including headers and attachments|
|Message Time|string|False|When the message was delivered to the user or quarantined by PPS|
|Modules Run|[]string|False|The list of PPS modules which processed the message|
|Phish Score|integer|False|The phish score of the message. Higher scores indicate higher certainty|
|Policy Routes|[]string|False|The policy routes that the message matched during processing by PPS|
|Quarantine Folder|string|False|The name of the folder which contains the quarantined message|
|Quarantine Rule|string|False|The name of the rule which quarantined the message|
|Recipient|[]string|False|An array containing the email addresses of the SMTP (envelope) recipients|
|Reply To Address|[]string|False|The email address contained in the Reply-To|
|Sender|string|False|The email address of the SMTP (envelope) sender. The user-part is hashed. The domain-part is cleartext|
|Sender IP|string|False|The IP address of the sender|
|Spam Score|integer|False|The spam score of the message. Higher scores indicate higher certainty|
|Subject|string|False|The subject line of the message, if available|
|Threats Info Map|[]threatsInfoMap|False|Details about detected threats within the message|
|To Address|[]string|False|A list of email addresses contained within the To|
|X-Mailer|string|False|The content of the X-Mailer|

#### permittedClicks

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Clicks Permitted|[]clicks|False|An array containing all clicks to URL threats which were permitted|
|Query End Time|string|False|The time at which the period queried for data ended|

#### platform

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Name of platform|
|OS|string|False|Operating system|
|Version|string|False|Version of operating system|

#### report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Forensics|[]evidence|False|Array of Evidence objects|
|ID|string|False|The identifier associated with the campaign or individual threat|
|Name|string|False|The malicious URL, SHA256 hash of the malicious attachment, or campaign name|
|Scope|string|False|Whether the report scope covers a campaign or an individual threat|
|Type|string|False|The threat type|

#### tapResults

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Browser|browser|False|Browser information|
|Message|message|False|TAP alert meta data|
|Threat|threat|False|Threat information|

#### threat

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attachment SHA256 Hash|string|False|Attachment SHA256 hash|
|Category|string|False|Category|
|Condemnation Time|string|False|Condemnation time|
|Threat Details URL|string|False|URL to the details of the threat|
|URL|string|False|URL|

#### threatsInfoMap

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Campaign ID|string|False|An identifier for the campaign of which the threat is a member|
|Classification|string|False|The category of threat found in the message|
|Threat|string|False|The artifact which was condemned by Proofpoint. The malicious URL, hash of the attachment threat, or email address of the impostor sender|
|Threat ID|string|False|The unique identifier associated with this threat|
|Threat Status|string|False|The current state of the threat|
|Threat Time|string|False|Proofpoint assigned the threatStatus at this time|
|Threat Type|string|False|Whether the threat was an attachment, URL, or message type|
|Threat URL|string|False|A link to the entry about the threat on the TAP Dashboard|

#### urls

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Cluster Name|string|False|Cluster name|
|Decoded URL|string|False|Decoded URL|
|Encoded URL|string|False|Encoded URL|
|Error|string|False|Error details if any error occurs|
|Message GUID|string|False|Message GUID|
|Recipient Email|string|False|Recipient email|
|Success|boolean|False|Success|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Click Statistics|clickStatistics|False|Click statistics|
|Identity|identity|False|Identity|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

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
