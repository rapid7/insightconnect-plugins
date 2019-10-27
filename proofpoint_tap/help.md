
# Proofpoint TAP Parser

## About

Proofpoint TAP is a plugin for [Proofpoint Targeted Attack Protection](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection) (TAP) alerts.

## Actions

### Parse Alert

This action is used to parse a TAP alert.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tap_alert|string|None|True|A Proofpoint TAP alert|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|tap_results|False|Proofpoint TAP results|

Example output:

```
"results": {
  "threat": {
    "attachment_sha256": "f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2",
    "category": "Malware",
    "condemnation_time": "2019-01-10T12:34:05Z"
  },
  "message": {
    "time_delivered": "2019-01-10T12:10:21Z",
    "recipients": "alice@example.com",
    "subject": "January Invoice",
    "sender": "bob@example.com",
    "header_from": "Bob",
    "header_replyto": "bob@example.com",
    "message_id": " 1111111111.22222222.3333333333333@mail.yahoo.com",
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

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Fixed issue where TAP alerts with attachments are not parsed correctly
* 1.0.2 - Sanitize example output in Parse Alert action documentation
* 1.0.3 - Fixed issue where headers were occasionally parsed improperly

## Workflows

Examples:

* Look up SHA256 hash and enrich data

## References

* [Proofpoint TAP](https://www.proofpoint.com/us/products/ransomware-and-targeted-attack-protection)
