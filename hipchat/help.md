# Description

[HipChat](https://www.hipchat.com) is a web service for internal private online chat
and instant messaging. As well as one-on-one and group/topic chat, it also features
cloud-based file storage, video calling, searchable message-history and inline-image viewing.
This plugin accesses the [HipChat API](https://www.hipchat.com/docs/apiv2/)
The output of this plugin is the JSON data returned by HipChat.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin requires network access to a HipChat API server, as well as authentication data: API Token.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|https\://hipchat.com/|True|HipChat API Server|None|
|version|string|v2|True|API Version|None|
|user|string|None|False|User Account|None|
|token|string|None|False|API Token|None|
|pass|password|None|False|Password|None|

## Technical Details

### Actions

#### Post Message

This action is used to send a message to a room.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|True|The message post to room. Valid length range\: 1 - 1000|None|
|room_id_or_name|string|None|True|The id or url encoded name of the room|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamp|string|False|The utc timestamp representing when the message was processed|
|id|string|False|The unique identifier of the sent message|

#### Delete User

This action is used to delete a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id_or_email|string|None|True|The id, email address, or mention name (beginning with an '@') of the user to update|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|Http status code|

#### Create User

This action is used to create a new user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|User's full name. Valid length range\: 1 - 50|None|
|roles|[]string|None|False|The list of roles for the user|None|
|title|string|None|False|Title of user|None|
|mention_name|string|None|False|User's @mention name|None|
|is_group_admin|boolean|False|False|The user is group admin|None|
|timezone|string|UTC|False|User's timezone|None|
|password|string|None|False|If not provided, a randomly generated password will be returned|None|
|email|string|None|True|The email address|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|The new created user id|
|links|object|False|None|
|entity|object|False|None|

#### Update User

This action an be used to update a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|User's full name. Valid length range\: 1 - 50|None|
|roles|[]string|None|False|The list of roles for the user|None|
|id_or_email|string|None|True|The id, email address, or mention name (beginning with an '@') of the user to update|None|
|presence|object|None|False|Presence information for the user include fields (status, show) with data type is string|None|
|mention_name|string|None|True|User's @mention name|None|
|is_group_admin|boolean|None|False|The user is group admin|None|
|timezone|string|UTC|False|User's timezone|None|
|title|string|None|False|Title of User|None|
|password|string|None|False|If not provided, the existing password is kept|None|
|email|string|None|True|Email of user|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status_code|integer|False|Http status code|

### Triggers

#### Latest Message

This trigger is used to monitor for latest chat message.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|max-results|integer|75|False|The maximum number of messages to return. Valid length range\: 0 - 1000|None|
|timezone|string|UTC|False|Your timezone. Must be a supported timezone name|None|
|include_deleted|boolean|True|False|Include records about deleted messages into results (body of a message isn't returned). Set to 'true'|None|
|room_id_or_name|string|None|True|Room id or name|None|
|not-before|string|None|False|The id of the message that is oldest in the set of messages to be returned. The server will not return any messages that chronologically precede this message|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|items|[]object|False|An array of items|
|startIndex|integer|False|The start index for this set of results|
|maxResults|integer|False|The maximum number of results returned|
|links|object|False|Links|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Error values use the standard HTTP codes (200 OK, 404 Not Found, etc)

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [HipChat](https://hipchat.com/)
* [HipChat API](https://www.hipchat.com/docs/apiv2/)

