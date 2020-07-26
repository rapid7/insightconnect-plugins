# Description

[Proofpoint Targeted Attack Protection](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection)
(TAP) helps you stay ahead of attackers with an innovative approach that detects, analyzes and blocks advanced 
threats before they reach your inbox. This plugin enables users to parse TAP alerts.

# Key Features

* Parse indicators from TAP alert e-mails

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Parse Alert

This action is used to parse a TAP alert. This action supports a TAP alert from a forwarded e-mail as well.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|tap_alert|string|None|True|A Proofpoint TAP alert|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|tap_results|False|Proofpoint TAP results|

Example output:

```
"results": {
  "threat": {
    "attachment_sha256": "9c22af77f29f5eb007403455b7896906b479995b6444e421d6093e683f593e4",
    "category": "Malware",
    "condemnation_time": "2019-01-10T12:34:05Z",
    "threat_details_url": "https://threatinsight.proofpoint.com/v7l34e70-a2ec-a214-bc4d-acd68a33dba2/threat/email/9c22af77f29f5eb007403455b7896906b479995b6444e421d6093e683f593e4?linkOrigin=notif"
  },
  "message": {
    "time_delivered": "2019-01-10T12:10:21Z",
    "recipients": "user@example.com",
    "subject": "January Invoice",
    "sender": "user@example.com",
    "header_from": "Bob",
    "header_replyto": "user@example.com",
    "message_id": "user@example.com",
    "sender_ip": "198.51.100.100",
    "message_size": "152 KB",
    "message_guid": "-AsyUBf--Yt7cR-tndAo8RaUbk8kBACE",
    "threat_id": "30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050"

  },
  "browser": {
      "time": "2020-05-11T11:01:13Z",
      "source_ip": "198.51.100.100",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
   }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

### Custom Output Types

#### browser

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Source IP|string|False|Source IP|
|Time|string|False|Time|
|User Agent|string|False|User agent string|

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
|Time Delivered|string|False|Time Delivered|

#### tap_results

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
|Condemnation Time|string|False|Condemnation Time|
|Threat Details URL|string|False|URL for Details of the Threat|
|URL|string|False|URL|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Update to use the `insightconnect-python-3-38-slim-plugin:4` Docker image | Update plugin.spec.yaml to include `cloud_ready`
* 1.0.6 - Parsing out GUID of the message into the output type
* 1.0.5 - Parsing out the View Threat Details link from emails to its own value
* 1.0.4 - New spec and help.md format for the Extension Library
* 1.0.3 - Fixed issue where headers were occasionally parsed improperly
* 1.0.2 - Sanitize example output in Parse Alert action documentation
* 1.0.1 - Fixed issue where TAP alerts with attachments are not parsed correctly
* 1.0.0 - Initial plugin

# Links

## References

* [Proofpoint TAP](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection)

