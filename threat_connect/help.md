
# ThreatConnect

## About

[ThreatConnect](https://threatconnect.com) is a Threat Intelligence Platform (TIP) that empowers large organizations to aggregate, analyze and act on their threat intelligence.

[ThreatConnect Python SDK](https://docs.threatconnect.com/en/latest/python/python_sdk.html)

## Actions

### Delete Adversary

This action is used to delete an adversary in the ThreatConnect platform.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|owner|string|None|True|Owner/Organization|None|
|id|integer|None|True|Adversary To Delete|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

### Create Task

This action is used to create a task resource in the ThreatConnect platform.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|False|Task status|['In Progress', 'Completed', 'Waiting on Someone', 'Deferred']|
|due_date|date|None|False|Task due date|None|
|name|string|None|True|Task Name|None|
|tags|string|None|False|Task tags comma delimited|None|
|reminder_date|date|None|False|Task reminder date|None|
|reminded|boolean|None|False|Use task Reminder|None|
|escalatee|string|None|False|Task escalatee|None|
|escalated|boolean|None|False|Use task escalation|None|
|security_label|string|None|False|Task security label|None|
|assignee|string|None|False|Task Assignee|None|
|escalation_date|date|None|False|Task escalation date|None|
|attributes|[]object|None|False|Task Attributes|None|
|overdue|boolean|None|False|Is task overdue|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|None|

### Victims Retrieve

This action is used to retrieve ThreatConnect victims.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|filter|None|False|ThreatConnect filters|None|
|owner|string|None|True|Owner/Organization|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|victims|[]victim_output|False|None|

### Threats Retrieve

This action is used to retrieve ThreatConnect threats.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|filter|None|False|ThreatConnect filters|None|
|owner|string|None|True|Owner/Organization|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threats|[]signatures_output|False|None|

### Create Adversary

This action is used to create a ThreatConnect adversary.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|owner|string|None|True|Owner/Organization|None|
|attributes|[]object|None|False|Adversary Attributes|None|
|tags|string|None|False|Adversary Tags|None|
|name|string|None|True|Adversary Name|None|
|security_label|string|None|False|Adversary Security Label|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|None|

### Bulk Indicator Download

This action is used to retrieve ThreatConnect bulk indicator download.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|rating|string|None|False|Indicator rating|None|
|confidence|integer|None|False|Confidence value|None|
|threat_assess_confidence|integer|None|False|Threat Assess Confidence filter|None|
|attribute|string|None|False|Attribute type|None|
|tag|string|None|False|Single tag filter|None|
|last_modified|date|None|False|Last modified date|None|
|owner|string|None|True|Owner/Organization|None|
|date_added|date|None|False|Date indicator added|None|
|type|string|None|False|Indicator type|None|
|threat_assess_rating|string|None|False|Threat Assess Rating filter|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bulk_indicators|[]bulk_indicator_output|False|None|

### Incidents Retrieve

This action is used to retrieve ThreatConnect incidents.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|filter|None|False|ThreatConnect filters|None|
|owner|string|None|True|Owner/Organization|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incidents|[]incidents_output|False|None|

### Email Retrieve

This action is used to retrieve ThreatConnect e-mails.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|incident_id|integer|None|False|Filter Groups on associated Incident ID|None|
|indicator|string|None|False|Filter Groups on associated Indicator|None|
|threat_id|integer|None|False|Filter Groups on associated Threat ID|None|
|email_id|integer|None|False|Filter Groups on associated Email ID.|None|
|security_label|string|None|False|Filter Groups on associated Security Label|None|
|tag|string|None|False|Filter Groups on applied Tag|None|
|owner|string|None|True|Owner/Organization|None|
|signature_id|integer|None|False|Filter Groups on applied Security Label|None|
|id|integer|None|False|Filter Groups on associated ID|None|
|document_id|integer|None|False|Filter Groups on associated Document ID|None|
|adversary_id|integer|None|False|Filter Groups on associated Adversary ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|emails|[]email_output|False|None|

### Signatures Retrieve

This action is used to retrieve ThreatConnect signatures.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|filter|None|False|ThreatConnect filters|None|
|owner|string|None|True|Owner/Organization|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|signatures|[]signatures_output|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:
|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_default_org|string|None|False|Enter API Default Org|None|
|api_access_id|string|None|False|Enter API Access ID|None|
|api_secret_key|string|None|False|Enter API Secret Key|None|
|api_base_url|string|None|False|Enter API Base URL|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Threat Intelligence
* Enrichment

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to Python v2 architecture | Support web server mode | Use new credential types | Rename "Threat Connect" plugin title to "ThreatConnect" | Rename "Email's Retrieve" to "Email Retrieve"

## References

* [ThreatConnect](https://threatconnect.com)
* [ThreatConnect Python SDK](https://docs.threatconnect.com/en/latest/python/python_sdk.html)
