# Description

The [Threatq](https://www.threatq.com) plugin provides the ability to work with Threat Quotient indicators and events. Using The ThreatQ as a threat intelligence platform equips you with a threat library that automatically scores and prioritizes threat intelligence based on parameters you set. Prioritization is calculated across many separate sources, both external and internal, to deliver a single source of truth using the aggregated context provided.

# Key Features

* Search for indicators
* Manage indicators
* Manage events

# Requirements

* Administrative credentials for Threatq
* The host address of your instance of Threatq
* A client ID
* Proxy information if needed

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|False|ThreatQuotient username (e.g. email) and password|None|
|host|string|None|False|Address of the Threat Quotient host (e.g. https\://localhost\:8443)|None|
|proxy|string|None|False|Address of a proxy if applicable (e.g. https\://localhost\:8443)|None|
|client_id|password|None|False|Threat Quotient OAuth Token|None|

## Technical Details

### Actions

#### Search Indicators

This action is used to search for a specific indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|indicator|indicator|None|False|Parameters of an indicator on which to search|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|total|integer|False|Total number of search results|
|data|[]indicator|False|List of indicators that match query|

#### Search

This action is used to search all data.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|False|Search query|None|
|limit|integer|None|False|Maximum number of records to retrieve|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]search_result|False|Data entries matching query|

#### List Events

This action is used to list all events.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|event|event|None|False|Parameters of an event on which to search|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|total|integer|False|Total number of search results|
|data|[]event|False|List of events that match query|

#### Create Indicator

This action is used to create a new indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|False|Status of the indicator|['Active', 'Expired', 'Indirect', 'Review', 'Whitelisted']|
|source|string|None|False|Source of the indicator|None|
|type|string|None|False|Type of the indicator|['CIDR Block', 'Email Address', 'Eamil Attachment', 'Email Subject', 'File Path', 'Filename', 'FQDN', 'Fuzzy Hash', 'GOST Hash', 'IP Address', 'MD5', 'Mutex', 'Password', 'Registry Key', 'SHA-1', 'SHA-256', 'SHA-384', 'SHA-512', 'String', 'URL', 'URL Path', 'User-agent', 'Username', 'X-Mailer']|
|value|string|None|False|Value of the indicator|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|ID of the created indicator|

#### Create Event

This action is used to create a new event.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|date|date|None|False|None|None|
|source|string|None|False|Source of the event|None|
|type|string|None|False|Type of the event|['Watering Hole', 'SQL Injection Attack', 'DoS Attack', 'Malware', 'Watchlist', 'Command and Control', 'Anonymization', 'Exfiltration', 'Host Characteristics', 'Compromised PKI Certificate', 'Login Compromise', 'Incident']|
|description|string|None|False|Description of the event|None|
|title|string|None|False|Title of the event|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|ID of the created event|

#### Get Indicator

This action is used to retrieve detailed information associated with a given indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|with|[]string|None|False|The classes of items related to the indicator to return. e.g. ['adversaries', 'attachments']|None|
|id|integer|None|False|The ID of the requested indicator|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|object|False|The properties of the indicator|

#### Get Event

This action is used to retrieve detailed information associated with a given event.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|with|[]string|None|False|The classes of items related to the event to return. e.g. ['adversaries', 'attachments']|None|
|id|integer|None|False|The ID of the requested event|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|object|False|The properties of the event|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types | Rename "Get indicator" action to "Get Indicator" | Rename "Get event" action to "Get Event"
* 0.2.3 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Threat Quotient](https://www.threatq.com/)

