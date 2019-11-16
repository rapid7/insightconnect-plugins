# Description

[Request Tracker](https://bestpractical.com/request-tracker) is the open-source enterprise grade issue and ticket tracking system.
It allows organizations to keep track of what needs to get done, who is working on which tasks, what's already been done, and when tasks were (or weren't) completed.
The Request Tracker plugin allows you to create and manage tickets. 

# Key Features

* Create Tickets
* Get Ticket information

# Requirements

* Request tracker credentials

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|False|Username|None|
|pass|string|None|True|Password|None|
|host|string|None|True|Server hosting Request Tracker|None|

## Technical Details

### Actions

#### Ticket Properties

This action is used to get the data for a single ticket, not including the history and comments.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ticket_id|integer|None|True|Ticket ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Queue|string|False|None|
|Owner|string|False|None|
|Creator|string|False|None|
|Subject|string|False|None|
|Status|string|False|None|
|Priority|string|False|None|
|InitialPriority|string|False|None|
|FinalPriority|string|False|None|
|Requestors|[]string|False|None|
|CC|string|False|None|
|AdminCc|string|False|None|
|Created|string|False|None|
|Due|string|False|None|
|Resolved|string|False|None|
|Told|string|False|None|
|TimeEstimated|string|False|None|
|TimeWorked|string|False|None|
|TimeLeft|string|False|None|

#### Ticket Links

This action is used to get the ticket links for a single ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ticket_id|integer|None|True|Ticket ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HasMember|string|False|None|
|ReferredToBy|string|False|None|
|DependedOnBy|[]string|False|None|
|MemberOf|string|False|None|
|RefersTo|string|False|None|
|DependsTo|[]string|False|None|

#### Ticket Attachments

This action is used to get a list of all attachments related to the ticket.

##### Output

Returns a list of attachments each structured as shown below:

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|None|
|Name|string|False|None|
|Size|string|False|None|
|ContentType|string|False|None|

#### Ticket Attachment

This action is used to get the metadata and content of a specific attachment.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ticket_id|integer|None|True|Ticket ID|None|
|attachment_id|integer|None|True|Attachment ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|None|
|Subject|string|False|None|
|Creator|integer|False|None|
|Created|integer|False|None|
|Transaction|integer|False|None|
|Parent|integer|False|None|
|MessageId|integer|False|None|
|Filename|string|False|None|
|ContentType|string|False|None|
|ContentEncoding|string|False|None|
|Headers|string|False|None|
|Content|string|False|None|

#### Ticket Attachment Content

This action is used to get the attachment data content without additional metadata or whitespace characters.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ticket_id|integer|None|True|Ticket ID|None|
|attachment_id|integer|None|True|Attachment ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|content|string|False|string containing the original content|

#### Ticket History

This action is used to get a list of all the history items for a given ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ticket_id|integer|None|True|Ticket ID|None|

##### Output

Returns a list of Ticket History objects

#### Ticket History Entry

This action is used to get the history information for a single history item. Note that the history item must actually correspond to the ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ticket_id|integer|None|True|Ticket ID|None|
|history_id|integer|None|True|Ticket ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|History ID|
|Ticket|integer|False|Ticket ID|
|TimeTaken|string|False|None|
|Type|string|False|None|
|Field|string|False|None|
|OldValue|string|False|None|
|NewValue|string|False|None|
|Data|string|False|None|
|Description|string|False|None|
|Content|string|False|None|
|Creator|string|False|None|
|Created|date|False|None|
|Attachments|[]object|False|None|

#### Ticket Search

This action is used to get the ticket links for a single ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|raw_query|string|None|False|You can use any query generated by the query builder - or feel free to write your own|None|
|order|string|None|False|By this parameter you can change the sort field and order of the search result. To sort a list ascending just put a + before the fieldname|None|
|queue|string|None|False|Queue where to search|None|
|keywords|object|None|False|Other arguments possible to set if not passing raw_query|None|

###### Keywords Input

Other arguments possible to set if not passing raw_query

Requestors, Subject, Cc, AdminCc, Owner, Status,
Priority, InitialPriority, FinalPriority,
TimeEstimated, Starts, Due, Text,... (according to RT
fields)

Custom fields CF.{<CustomFieldName>} could be set
with keywords CF_CustomFieldName.

To alter lookup operators you can append one of the
following endings to each keyword

__exact    for operator = (default)
__notexact for operator !=
__gt       for operator >
__lt       for operator <
__like     for operator LIKE
__notlike  for operator NOT LIKE

Setting values to keywords constrain search
result to the tickets satisfying all of them.

##### Output

Returns a list of matching tickets. Each ticket is the same dictionary as in the Ticket type.

#### Ticket Create

This action is used to get a new ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|queue|string|None|False|Queue where to search|None|
|keywords|object|None|False|Key-Value pairs map of ticket properties|None|

##### Output

Returns ID of new ticket or ``-1``, if creating failed.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Request Tracker](https://bestpractical.com/request-tracker)
* [REST API documentation](https://rt-wiki.bestpractical.com/wiki/REST#Ticket_Create)

