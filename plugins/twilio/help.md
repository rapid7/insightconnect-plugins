# Description

[Twilio](https://www.twilio.com/) is a cloud communications platform for building SMS, voice, and messaging applications
on an API built for global scale. Users can send SMS using the Twilio plugin for Rapid7 for notification or other purposes

# Key Features

* Send SMS

# Requirements

* Twilio phone number
* Authentication token
* Account ID

# Supported Product Versions

* Twilio Client 9.4.2

# Documentation

## Setup

This plugin requires an [account SID, authentication token](https://www.twilio.com/docs/sms/api#sms-api-authentication), and a Twilio phone number.
The account SID and Auth Token are viewable in your [console](https://www.twilio.com/console).

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username should be your account ID, and your password should be your auth token|None|{"username": "ExampleUsername", "password": "ExamplePassword"}|None|None|
|twilio_phone_number|string|None|True|The phone number of a Twilio user from which the SMS will be sent|None|+00000111222|None|None|

Example input:

```
{
  "credentials": {
    "password": "ExamplePassword",
    "username": "ExampleUsername"
  },
  "twilio_phone_number": "+00000111222"
}
```

## Technical Details

### Actions


#### Send SMS

This action is used to send an SMS message to a phone number

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|message|string|None|True|Message to send|None|ExampleMessage|None|None|
|to_number|string|None|True|Phone number to send SMS message|None|+00000111222|None|None|
  
Example input:

```
{
  "message": "ExampleMessage",
  "to_number": "+00000111222"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message_sid|string|False|Message SID|ExampleMessageSID|
  
Example output:

```
{
  "message_sid": "ExampleMessageSID"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* Before sending the SMS make sure that the country you're sending the message to is enabled [here](https://www.twilio.com/console/sms/settings/geo-permissions).

# Version History

* 1.0.3 - Updated dependencies | Updated SDK to the latest version
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Update Twilio dependency to 6.19.1
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Twilio](https://www.twilio.com/)
* [SMS Geo-permissions](https://www.twilio.com/console/sms/settings/geo-permissions)

## References

* [Twilio](https://www.twilio.com/)
* [Twilio Python Library](https://www.twilio.com/docs/libraries/python)