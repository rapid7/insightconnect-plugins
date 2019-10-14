
# SMTP Mailer

## About

[Simple Mail Transfer Protocol](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) (SMTP) is an Internet standard for electronic mail (email) transmission.
This plugin allows you to craft and send an email to an SMTP server.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|False|None|None|
|use_ssl|boolean|True|False|None|None|
|host|string|None|False|Host of SMTP server to connect to|None|
|password|password|None|False|None|None|
|port|integer|25|False|None|None|

NOTE: If username and password are left blank, the plugin will not try to authenticate.

## Actions

### Send Email

This action is used to send an email.

#### Input

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

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|False|None|

## Triggers

This plugin does not contain any triggers.

## Troubleshooting

If you are passing a variable into the Attachment 'Content' field, you must make sure it is base64-encoded.

## Workflows

Examples:

* [Security Mailbox Triage](https://market.komand.com/workflows/komand/security-mailbox-triage/1.0.0)
* Notification
* Send logs from artifacts

## Versions

* 0.1.0 - Initial plugin
* 0.2.0 - Add attachment support
* 0.2.1 - SSL bug fix in SDK
* 0.3.0 - Added HTML body support | Updated to v2 architecture
* 1.0.0 - Add support for carbon copy field in email
* 1.0.1 - Support web server mode | Support for SMTP relays
* 2.0.0 - Update to new credential types | Rename "SMTP" plugin title to "SMTP Mailer" | Rename "Send an email" action to "Send Email"
* 2.0.1 - Fix issue where credentials were required
* 2.0.2 - Fix issue where Send action doesn't handle empty attachments correctly
* 2.0.3 - Fix issue with reliability in regards to previous Send action empty attachment fix

## References

* [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
