# Description

[Proofpoint Targeted Attack Protection](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection)
(TAP) helps you stay ahead of attackers with an innovative approach that detects, analyzes and blocks advanced 
threats before they reach your inbox. This plugin enables users to parse TAP alerts.

# Key Features

* Parse and trigger a workflow on a new alert

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Parse Alert

This action is used to parse a TAP alert.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tap_alert|string|None|True|A Proofpoint TAP alert|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|tap_results|False|Proofpoint TAP results|

Example output:

```
"results": {
  "threat": {
    "attachment_sha256": "f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2",
    "category": "Malware",
    "condemnation_time": "2019-01-10T12:34:05Z",
    "threat_details_url": "https://threatinsight.proofpoint.com/d7924670-a2ec-a214-9b2a-acd68a33dba2/threat/email/6789c46ac78950da6c243c52dc9312cab77877c6b0e1dbd5d66f9870e96d30bf?linkOrigin=notif"
  },
  "message": {
    "time_delivered": "2019-01-10T12:10:21Z",
    "recipients": "user@example.com",
    "subject": "January Invoice",
    "sender": "user@example.com",
    "header_from": "Bob",
    "header_replyto": "user@example.com",
    "message_id": "user@example.com",
    "sender_ip": "1.2.3.4",
    "message_size": "152 KB"
  },
  "browser": {
     "time": "",
     "source_ip": "",
     "user_agent": ""
   }
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.5 - Parsing out the View Threat Details link from emails to its own value
* 1.0.4 - New spec and help.md format for the Extension Library
* 1.0.3 - Fixed issue where headers were occasionally parsed improperly
* 1.0.2 - Sanitize example output in Parse Alert action documentation
* 1.0.1 - Fixed issue where TAP alerts with attachments are not parsed correctly
* 1.0.0 - Initial plugin

# Links

## References

* [Proofpoint TAP](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection)

