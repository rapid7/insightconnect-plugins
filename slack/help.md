
# Slack

## About

[Slack](https://slack.com/) brings all your communication together in one place. It's real-time messaging, archiving and search for modern teams.
This plugin utilizes the [Slack API](https://api.slack.com/).

## Actions

### Search messages

This action is used to search the message archive by pattern.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|count|integer|100|False|None|None|
|sort|string|score|False|None|None|
|highlight|boolean|None|False|None|None|
|query|string|None|True|None|None|
|page|integer|1|False|None|None|
|sort_dir|string|desc|False|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|matches|[]object|False|None|
|count|int|False|None|
|total|int|False|None|
|page|int|False|None|
|pages|int|False|None|

### Enable User

This action is used to (Slack plus only) enable user with specific email address.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|None|

### Post Message

This action is used to post a message to the Slack channel.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|False|Username to post to. Username, channel, or channel id must be specified|None|
|channel_id|string|None|False|Channel ID to post to (will ignore username/channel if specified)|None|
|attachments|[]object|None|False|(Advanced) JSON array of attachments - see https\://api.slack.com/docs/message-attachments|None|
|icon_emoji|string|None|False|Icon to use when posting|None|
|message|string|None|False|Message to send|None|
|channel|string|None|False|Channel name to post to (e.g. #dev)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamp|string|False|Timestamp of sucessful message|
|message_id|string|False|MessageID of successful message|

### Upload File

This action is used to upload a file to Slack.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|content|bytes|None|False|File content (base64 encoded)|None|
|channels|string|None|False|Channels which the file should be shared to (comma-separated)|None|
|title|string|None|False|Title of Attachment|None|
|filename|string|None|False|File name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|file_reference|False|None|

### Disable User

This action is used to (Slack plus only) disable user with specific email address.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|None|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|None|

### Upload Snippet

This action is used to upload a snippet to Slack.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|content|string|None|True|Snippet text|None|
|channels|string|None|False|Channels which the file should be shared to (comma-separated)|None|
|filetype|string|None|False|File type|None|
|title|string|None|False|Title of Snippet|None|
|filename|string|None|False|File name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|file_reference|False|None|

## Triggers

### New Message With File

This trigger is used to monitor for messages with file attachments.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|match_text|string|None|False|Regexp match on message text|None|
|match_filename|string|None|False|Regexp match on a specific filename|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamp|string|False|Timestamp|
|message|object|False|Message|
|type|string|False|Message type|
|file|file|False|File|

### New Message

This trigger is used to monitor for messages of a given pattern.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|match_text|string|None|False|Regex match on message content e.g. hi or .*hi.* matches `john says hi` in the message text.|None|
|match_channel|string|None|False|Regex match on channel. Otherwise\: listen on any channel.|None|
|type|string|any|True|Trigger on direct messages, group chats, or any|['any', 'direct', 'group']|
|match_user|string|None|False|Regex match on username sending the message. Otherwise\: listen for any private message.|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamp|string|False|Timestamp|
|message|message|False|Message|
|type|string|False|Message Type|

### Slack Event

This trigger is used to monitor for Slack events.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|subtype|string|None|True|Event subtype to monitor|['bot_message', 'channel_archive', 'channel_join', 'channel_leave', 'channel_name', 'channel_purpose', 'channel_topic', 'channel_unarchive', 'file_comment', 'file_mention', 'file_share', 'group_archive', 'group_join', 'group_leave', 'group_name', 'group_purpose', 'group_topic', 'group_unarchive', 'me_message', 'message_changed', 'message_deleted', 'pinned_item', 'unpinned_item']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamp|string|False|Timestamp|
|event|object|False|Event|

## Connection

This plugin requires a Slack API token to authenticate.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|token|string|None|False|Authentication token|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Notification

## Versions

* 0.1.0 - Initial plugin
* 1.0.0 - Update plugin to v2 Go architecture | Support web server mode
* 2.0.1 - Updating to Go SDK 2.6.4

## References

* [Slack](https://slack.com/)
* [Slack API](https://api.slack.com/)
* [Chatops Example: Investigating URLs](https://komand.zendesk.com/hc/en-us/articles/115000954607-Use-Case-Chatops-Example-Investigating-URLs)
