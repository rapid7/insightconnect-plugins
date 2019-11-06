# Description

[Twitter](https://twitter.com) is an online news and social networking service where users post and interact with messages, "tweets,"
restricted to 140 characters. Registered users can post tweets, but those who are unregistered can only read them.

This plugin utilizes the [python-twitter](https://github.com/bear/python-twitter/wiki) Python library.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

Using the plugin will require a valid Twitter OAuth token, by creating an "App" registered to use your Twitter account.
You can find the page to do so at [Twitter Apps](https://apps.twitter.com/)
Note - you must be logged in to access this page properly.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|consumer_credentials|credential_username_password|None|True|Consumer Key and Consumer Secret|None|
|access_token_credentials|credential_username_password|None|True|Access Token and Access Token Secret|None|

## Technical Details

### Actions

#### Destroy Direct Message

This action can be used to destroy a direct message from the Twitter account linked via the connection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message_id|string|None|True|ID of direct message to destroy|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|destroyed|boolean|False|None|

#### Post

This action can be used to issue a tweet from the Twitter account linked via the connection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|msg|string|None|True|Text to tweet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|

#### Block

This action can be used to block a user from the Twitter account linked via the connection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|User to block|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|blocked|boolean|False|None|

### Triggers

All of the below triggers utilize the plugin cache to track a history of the last message received.
This means they will not replay messages that already were pulled via the API.

#### Tweets

The Tweets trigger will fire off a job for every Tweet that matches the supplied pattern you give to the Trigger. For example, you could monitor for "BBQ" to get BBQ related tweets.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pattern|string|None|True|Pattern to Match|None|
|interval|integer|300|False|Poll interval in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|False|None|
|url|string|False|None|
|user|string|False|None|

#### Mentions

The Mentions trigger will off a job for every Mention that matches the supplied pattern, and involves the linked account in the connection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pattern|string|None|False|Pattern to Match|None|
|interval|integer|300|False|Poll interval in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|False|None|
|url|string|False|None|
|user|string|False|None|

#### Messages

This trigger will fire off a job for every direct message received by the linked account in the connection.
Note that to use this trigger "Read, Write and Access direct messages" must be selected in your Twitter App's permissions tab.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pattern|string|None|False|Pattern to Match|None|
|interval|integer|300|False|Poll interval in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sender_lang|string|False|Sender's language|
|sender_name|string|False|Sender's profile name|
|created_at|string|False|None|
|sender_created_at|string|False|Sender account creation date|
|sender_id|integer|False|None|
|sender_description|string|False|Sender profile description|
|id|string|False|None|
|sender_default_profile|boolean|False|Sender uses the default profile|
|recipient_id|integer|False|None|
|sender_location|string|False|Sender's geographic location|
|user|string|False|None|
|sender_followers_count|integer|False|Sender's follower count|
|msg|string|False|None|
|sender_friends_count|integer|False|Sender's friend count|
|sender_default_profile_image|boolean|False|Sender uses the default profile image|

#### User

The user trigger will allow you to follow a given user and receive any tweets from their timeline.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|300|False|Poll interval in seconds|None|
|screen_name|string|None|True|Screen Name (no @)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|False|None|
|url|string|False|None|
|user|string|False|None|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Refer to the Jobs page to inspect any jobs which have failed due to issues with this plugin.
If you suspect the failures are caused by a bug in the plugin, please contact Komand.

# Version History

* 2.0.0 - Support web server mode | Update to new credential types
* 1.0.1 - Fix long integer bug for `message_id` in Destroy action and `id` in Messages trigger
* 1.0.0 - Update to v2 Python plugin architecture
* 0.3.5 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Twitter Apps](https://apps.twitter.com/)
* [python-twitter](https://github.com/bear/python-twitter/wiki)

