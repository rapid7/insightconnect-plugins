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
|tap_alert|string|None|True|A Proofpoint TAP alert|None|proofpoint      URL DefenseAn end user has clicked on a link in their email which Proofpoint now recog=nizes as malicious. Details about the threat, the permitted click, and the =message containing the link are below:ThreatURL      hxxp://ec2-12-23-34-123[.]compute-1[.]amazonaws[.]com/[.]0[.]/ja=ke[.]user@example[.]comCategory         phishCondemnation Time        2020-04-27T12:22:54ZMessageTime Delivered   2020-04-27T09:54:49ZRecipient        user@example.comSubject  =97Sender   =97Header From      =97Header ReplyTo   =97Message-ID       =97Message-GUID     -JsyOYf--Yt7cR-ctdIo7RuUiK9kSECEThreat-ID        6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3da6f4e=798a39Sender IP        =97Message Size     =97ClickTime     2020-04-27T09:54:49ZSource IP        192.168.50.100User Agent       Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0)= like GeckoView Threat Details<https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789=-ef71-f3998c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a75=9e7db48f3da6f4e798a39?linkOrigin=3Dnotif>You are receiving this message because you are subscribed to alerts from th=e Threat Insight Dashboard. Update your subscription preferences<https://th=reatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f3998c3e92e3/settings/pr=ivileges?linkOrigin=3Dnotif> to stop receiving these notifications.Proofpoint Targeted Attack Protectionproofpoint--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_Content-Type: text/html; charset="Windows-1252"Content-ID: <725AAFECC53B504DBB925D82C035329A@example.prod.outlook.com>Content-Transfer-Encoding: quoted-printable<html><head><meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3DWindows-1=252"></head><body style=3D"margin:0px"><div style=3D"background:#f1f2f2;font-family:Arial;font-size:13px;color:#66=6666"><div style=3D"background:white"><div style=3D"max-width:720px;margin:auto;padding:0"><table style=3D"width:100%;height:60px;font-family:inherit;font-size:inheri=t;color:inherit"><tbody><tr><td><b style=3D"font-size:22px;color:black">proofpoint</b> </td><td align=3D"right">URL Defense</td></tr><tr></tr></tbody></table></div></div><div style=3D"max-width:720px;margin:auto;padding:20px 0">An end user has c=licked on a link in their email which Proofpoint now recognizes as maliciou=s. Details about the threat, the permitted click, and the message containin=g the link are below:<p><b>Threat</b></p><p><table border=3D"1" style=3D"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit" cellspa=cing=3D"0" cellpadding=3D"8"><col width=3D"150"><col><tbody><tr valign=3D"top"><td><b>URL</b></td><td style=3D"background:white">hxxp://ec2-12-34-56-123[.]compute-1[.]amazo=naws[.]com/[.]0[.]/user@example[.]com</td></tr><tr valign=3D"top"><td><b>Category</b></td><td style=3D"background:white">phish</td></tr><tr valign=3D"top"><td><b>Condemnation Time</b></td><td style=3D"background:white">2020-04-27T12:22:54Z</td></tr></tbody></table></p><p><b>Message</b></p><p><table border=3D"1" style=3D"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit" cellspa=cing=3D"0" cellpadding=3D"8"><col width=3D"150"><col><tbody><tr valign=3D"top"><td><b>Time Delivered</b></td><td style=3D"background:white">2020-04-27T09:54:49Z</td></tr><tr valign=3D"top"><td><b>Recipient</b></td><td style=3D"background:white">user@example.com</td></tr><tr valign=3D"top"><td><b>Subject</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Sender</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Header From</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Header ReplyTo</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Message-ID</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Message-GUID</b></td><td style=3D"background:white">-JsyOYf--Yt7cR-ctdIo7RuUiK9kSECE</td></tr><tr valign=3D"top"><td><b>Threat-ID</b></td><td style=3D"background:white">6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759=e7db48f3da6f4e798a39</td></tr><tr valign=3D"top"><td><b>Sender IP</b></td><td style=3D"background:white">=97</td></tr><tr valign=3D"top"><td><b>Message Size</b></td><td style=3D"background:white">=97</td></tr></tbody></table></p><p><b>Click</b></p><p><table border=3D"1" style=3D"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit" cellspa=cing=3D"0" cellpadding=3D"8"><col width=3D"150"><col><tbody><tr valign=3D"top"><td><b>Time</b></td><td style=3D"background:white">2020-04-27T09:54:49Z</td></tr><tr valign=3D"top"><td><b>Source IP</b></td><td style=3D"background:white">192.168.50.100</td></tr><tr valign=3D"top"><td><b>User Agent</b></td><td style=3D"background:white">Mozilla/5.0 (Windows NT 10.0; WOW64; Trident=/7.0; rv:11.0) like Gecko</td></tr></tbody></table></p><p></p><div style=3D"width:120px;margin:40px auto;padding:8px 32px;background:#06a=2d5;text-align:center"><a href=3D"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3=da6f4e798a39?linkOrigin=3Dnotif" style=3D"color:white;text-decoration:none"=>View Threat Details</a></div><div style=3D"font-size:11px;border-bottom:solid 1px #d1d3d4;padding-bottom=:8px;">You are receiving this message because you are subscribed to alerts =from the Threat Insight Dashboard.<a href=3D"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/settings/privileges?linkOrigin=3Dnotif">Update your subscription preferences</a> to stop receiving these notificati=ons. </div><p></p><div style=3D"font-size:11px;text-align:center;padding-bottom:30px">Proofpo=int Targeted Attack Protection<p><b>proofpoint</b> </p></div></div></div></body></html>--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_--|

Example input:

```
{
  "tap_alert": "proofpoint      URL DefenseAn end user has clicked on a link in their email which Proofpoint now recog=nizes as malicious. Details about the threat, the permitted click, and the =message containing the link are below:ThreatURL      hxxp://ec2-12-23-34-123[.]compute-1[.]amazonaws[.]com/[.]0[.]/ja=ke[.]user@example[.]comCategory         phishCondemnation Time        2020-04-27T12:22:54ZMessageTime Delivered   2020-04-27T09:54:49ZRecipient        user@example.comSubject  =97Sender   =97Header From      =97Header ReplyTo   =97Message-ID       =97Message-GUID     -JsyOYf--Yt7cR-ctdIo7RuUiK9kSECEThreat-ID        6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3da6f4e=798a39Sender IP        =97Message Size     =97ClickTime     2020-04-27T09:54:49ZSource IP        192.168.50.100User Agent       Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0)= like GeckoView Threat Details\u003chttps://threatinsight.proofpoint.com/5d1ce8c6-1234-6789=-ef71-f3998c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a75=9e7db48f3da6f4e798a39?linkOrigin=3Dnotif\u003eYou are receiving this message because you are subscribed to alerts from th=e Threat Insight Dashboard. Update your subscription preferences\u003chttps://th=reatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f3998c3e92e3/settings/pr=ivileges?linkOrigin=3Dnotif\u003e to stop receiving these notifications.Proofpoint Targeted Attack Protectionproofpoint--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_Content-Type: text/html; charset=\"Windows-1252\"Content-ID: \u003c725AAFECC53B504DBB925D82C035329A@example.prod.outlook.com\u003eContent-Transfer-Encoding: quoted-printable\u003chtml\u003e\u003chead\u003e\u003cmeta http-equiv=3D\"Content-Type\" content=3D\"text/html; charset=3DWindows-1=252\"\u003e\u003c/head\u003e\u003cbody style=3D\"margin:0px\"\u003e\u003cdiv style=3D\"background:#f1f2f2;font-family:Arial;font-size:13px;color:#66=6666\"\u003e\u003cdiv style=3D\"background:white\"\u003e\u003cdiv style=3D\"max-width:720px;margin:auto;padding:0\"\u003e\u003ctable style=3D\"width:100%;height:60px;font-family:inherit;font-size:inheri=t;color:inherit\"\u003e\u003ctbody\u003e\u003ctr\u003e\u003ctd\u003e\u003cb style=3D\"font-size:22px;color:black\"\u003eproofpoint\u003c/b\u003e \u003c/td\u003e\u003ctd align=3D\"right\"\u003eURL Defense\u003c/td\u003e\u003c/tr\u003e\u003ctr\u003e\u003c/tr\u003e\u003c/tbody\u003e\u003c/table\u003e\u003c/div\u003e\u003c/div\u003e\u003cdiv style=3D\"max-width:720px;margin:auto;padding:20px 0\"\u003eAn end user has c=licked on a link in their email which Proofpoint now recognizes as maliciou=s. Details about the threat, the permitted click, and the message containin=g the link are below:\u003cp\u003e\u003cb\u003eThreat\u003c/b\u003e\u003c/p\u003e\u003cp\u003e\u003ctable border=3D\"1\" style=3D\"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit\" cellspa=cing=3D\"0\" cellpadding=3D\"8\"\u003e\u003ccol width=3D\"150\"\u003e\u003ccol\u003e\u003ctbody\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eURL\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003ehxxp://ec2-12-34-56-123[.]compute-1[.]amazo=naws[.]com/[.]0[.]/user@example[.]com\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eCategory\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003ephish\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eCondemnation Time\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e2020-04-27T12:22:54Z\u003c/td\u003e\u003c/tr\u003e\u003c/tbody\u003e\u003c/table\u003e\u003c/p\u003e\u003cp\u003e\u003cb\u003eMessage\u003c/b\u003e\u003c/p\u003e\u003cp\u003e\u003ctable border=3D\"1\" style=3D\"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit\" cellspa=cing=3D\"0\" cellpadding=3D\"8\"\u003e\u003ccol width=3D\"150\"\u003e\u003ccol\u003e\u003ctbody\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eTime Delivered\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e2020-04-27T09:54:49Z\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eRecipient\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003euser@example.com\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eSubject\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e=97\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eSender\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e=97\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eHeader From\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e=97\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eHeader ReplyTo\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e=97\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eMessage-ID\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e=97\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eMessage-GUID\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e-JsyOYf--Yt7cR-ctdIo7RuUiK9kSECE\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eThreat-ID\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759=e7db48f3da6f4e798a39\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eSender IP\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e=97\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eMessage Size\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e=97\u003c/td\u003e\u003c/tr\u003e\u003c/tbody\u003e\u003c/table\u003e\u003c/p\u003e\u003cp\u003e\u003cb\u003eClick\u003c/b\u003e\u003c/p\u003e\u003cp\u003e\u003ctable border=3D\"1\" style=3D\"width:100%;border-collapse:collapse;border:sol=id 1px #d1d3d4;font-family:inherit;font-size:inherit;color:inherit\" cellspa=cing=3D\"0\" cellpadding=3D\"8\"\u003e\u003ccol width=3D\"150\"\u003e\u003ccol\u003e\u003ctbody\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eTime\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e2020-04-27T09:54:49Z\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eSource IP\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003e192.168.50.100\u003c/td\u003e\u003c/tr\u003e\u003ctr valign=3D\"top\"\u003e\u003ctd\u003e\u003cb\u003eUser Agent\u003c/b\u003e\u003c/td\u003e\u003ctd style=3D\"background:white\"\u003eMozilla/5.0 (Windows NT 10.0; WOW64; Trident=/7.0; rv:11.0) like Gecko\u003c/td\u003e\u003c/tr\u003e\u003c/tbody\u003e\u003c/table\u003e\u003c/p\u003e\u003cp\u003e\u003c/p\u003e\u003cdiv style=3D\"width:120px;margin:40px auto;padding:8px 32px;background:#06a=2d5;text-align:center\"\u003e\u003ca href=3D\"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/threat/email/6b5ebcb1a7fb7e19bad6d8e02a2a5e169320b1f8a759e7db48f3=da6f4e798a39?linkOrigin=3Dnotif\" style=3D\"color:white;text-decoration:none\"=\u003eView Threat Details\u003c/a\u003e\u003c/div\u003e\u003cdiv style=3D\"font-size:11px;border-bottom:solid 1px #d1d3d4;padding-bottom=:8px;\"\u003eYou are receiving this message because you are subscribed to alerts =from the Threat Insight Dashboard.\u003ca href=3D\"https://threatinsight.proofpoint.com/5d1ce8c6-1234-6789-ef71-f39=98c3e92e3/settings/privileges?linkOrigin=3Dnotif\"\u003eUpdate your subscription preferences\u003c/a\u003e to stop receiving these notificati=ons. \u003c/div\u003e\u003cp\u003e\u003c/p\u003e\u003cdiv style=3D\"font-size:11px;text-align:center;padding-bottom:30px\"\u003eProofpo=int Targeted Attack Protection\u003cp\u003e\u003cb\u003eproofpoint\u003c/b\u003e \u003c/p\u003e\u003c/div\u003e\u003c/div\u003e\u003c/div\u003e\u003c/body\u003e\u003c/html\u003e--_000_01000171bb978ba8b63e1565672b4239b8d917020071a120000000e_--"
}
```

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

* 1.0.7 - Update to use the `insightconnect-python-3-38-slim-plugin:4` Docker image | Update plugin.spec.yaml to include `cloud_ready`
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

