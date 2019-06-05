
# Twilio

## About

[Twilio](https://www.twilio.com/) is a cloud communications platform for building SMS, Voice & Messaging applications on an API built for global scale.

## Actions

### Send SMS

This action is used to send an SMS message to a phone number.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|True|Message to send|None|
|to_number|string|None|True|Phone number to send SMS message|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message_sid|string|False|Message SID|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin requires an [account SID, authentication token](https://www.twilio.com/docs/sms/api#sms-api-authentication), and a Twilio phone number.
The account SID and Auth Token are viewable in your [console](https://www.twilio.com/console).

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|twilio_phone_number|string|None|True|Twilio phone number|None|
|auth_token|string|None|True|Twilio Auth Token|None|
|account_id|string|None|True|Twilio Account SID|None|

## Troubleshooting

Before sending the SMS make sure that the country you're sending the message to is enabled [here](https://www.twilio.com/console/sms/settings/geo-permissions).

## Workflows

Examples:

* Notifications

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 1.0.1 - Update Twilio dependency to 6.19.1

## References

* [Twilio](https://www.twilio.com/)
* [Twilio Python Library](https://www.twilio.com/docs/libraries/python)
