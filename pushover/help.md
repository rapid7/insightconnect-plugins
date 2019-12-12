# Description

[Pushover](https://pushover.net) is a simple push notification service that integrates easily into web apps 
like IFTTT, network monitors like Nagios, shell scripts, servers, and anything else that needs to send alerts 
to your Android, iPhone, iPad, and Desktop. The Pushover plugin allows you to send Pushover notifications.

# Key Features

* Send a notification to a device

# Requirements

* Pushover API token

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|token|credential_secret_key|None|True|App Token|None|

The connection represents an 'app' in Pushover.  The key determines which 'source' it will be coming from.

## Technical Details

### Actions

#### Send pushover notification

This action sends a message to a user or group

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|Target of push notification|None|
|message|string|None|True|Message Body to send|None|
|title|string|None|False|Title for message - app name used otherwise|None|
|url|string|None|False|Supplemental URL to include|None|
|url_title|string|None|False|Title for URL|None|
|priority|integer|0|False|Priority of the message from very low to emergency|None|
|retry|integer|30|False|For Emergency messages, time to acknowledge before retry|None|
|expire|integer|None|False|When to give up on Emergency messages|None|
|sound|string|None|False|Sound to play - names at https://pushover.net/api#sounds|None|
|timestamp|date|None|False|Override default timestamp on message|None|

##### output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|True|Indicator of message acceptance for delivery|
|request|string|True|Identifier of the request in the pushover system|
|receipt|string|False|For emergency messages, the receipt ID to lookup if has been acknowledged|

### Triggers

_This plugin does not contain any triggers_

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [Pushover.net](https://pushover.net)

