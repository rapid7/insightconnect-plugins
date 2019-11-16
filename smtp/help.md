# Description

[Simple Mail Transfer Protocol](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) (SMTP) is an 
Internet standard for electronic mail (email) transmission. Users of this plugin will be able to craft and automatically 
send email through their Rapid7 InsightConnect workflows.

This plugin can aid in automated notifications, alerting, employee onboarding/offboarding, and more.

# Key Features

* Send email

# Requirements

* SMTP server credentials (optional depending on SMTP server configuration)
* SMTP server hostname
* SMTP server port

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|False|None|None|
|use_ssl|boolean|True|False|None|None|
|host|string|None|False|Host of SMTP server to connect to|None|
|password|password|None|False|None|None|
|port|integer|25|False|None|None|

NOTE: If username and password are left blank, the plugin will not try to authenticate.

## Technical Details

### Actions

#### Send Email

This action is used to send an email.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email_to|string|None|True|Email to send TO|None|
|attachment|file|None|False|Attachment|None|
|cc|[]string|None|False|CC emails|None|
|message|string|None|True|Message to send on the email|None|
|subject|string|None|True|Subject of the email|None|
|email_from|string|None|True|Email to use as FROM|None|
|bcc|[]string|None|False|BCC email|None|

Example output:

```

{
  "result": "ok"
}

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

If you are passing a variable into the Attachment 'Content' field, you must make sure it is base64-encoded.

## Version History

* 2.0.4 - New spec and help.md format for the Hub
* 2.0.3 - Fix issue with reliability in regards to previous Send action empty attachment fix
* 2.0.2 - Fix issue where Send action doesn't handle empty attachments correctly
* 2.0.1 - Fix issue where credentials were required
* 2.0.0 - Update to new credential types | Rename "SMTP" plugin title to "SMTP Mailer" | Rename "Send an email" action to "Send Email"
* 1.0.1 - Support web server mode | Support for SMTP relays
* 1.0.0 - Add support for carbon copy field in email
* 0.3.0 - Added HTML body support | Updated to v2 architecture
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Add attachment support
* 0.1.0 - Initial plugin

# Links

## References

* [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)