# Description

[Simple Mail Transfer Protocol](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) (SMTP) is an Internet standard for electronic mail (email) transmission. This plugin provides users with the ability to craft and automatically send emails through their Rapid7 InsightConnect workflows. This plugin can aid in automated notifications, alerting, employee onboarding/offboarding, and more

# Key Features

* Send an email with customizable FROM address, TO address, Subject line, and Message
* Send an HTML-enabled email for enhanced viewing quality
* Attach multiple files to a single email with the Attachments input

# Requirements

* SMTP server credentials (optional depending on SMTP server configuration)
* SMTP server hostname
* SMTP server port

# Supported Product Versions

* 2026-10-02

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|False|Username and password|None|{"username":"user@example.com","password":"mypassword"}|None|None|
|host|string|None|True|Host of SMTP server to connect to|None|smtp.example.com|None|None|
|port|integer|25|True|Port of SMTP server|None|25|None|None|
|use_ssl|boolean|True|True|Use SSL|None|True|None|None|

Example input:

```
{
  "credentials": {
    "password": "mypassword",
    "username": "user@example.com"
  },
  "host": "smtp.example.com",
  "port": 25,
  "use_ssl": true
}
```

## Technical Details

### Actions


#### Send Email

This action is used to send an email

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachments|[]file|None|False|List of files to attach to the email|None|[{"filename":"report.txt","content":"UmFwaWQ3IEluc2lnaHRDb25uZWN0"},{"filename":"second report.txt","content":"UmFwaWQ3IEluc2lnaHRDb25uZWN0"}]|None|None|
|bcc|[]string|None|False|BCC email|None|["user@example.com"]|None|None|
|cc|[]string|None|False|CC emails|None|["user@example.com"]|None|None|
|email_from|string|None|True|Email to use as FROM|None|user@example.com|None|None|
|email_to|string|None|True|Email to send TO|None|user@example.com|None|None|
|html|boolean|None|True|Message contains HTML|None|False|None|None|
|message|string|None|True|Message to send on the email|None|Please find the reports attached|None|None|
|subject|string|None|True|Subject of the email|None|Weekly report|None|None|
  
Example input:

```
{
  "attachments": [
    {
      "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0",
      "filename": "report.txt"
    },
    {
      "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0",
      "filename": "second report.txt"
    }
  ],
  "bcc": [
    "user@example.com"
  ],
  "cc": [
    "user@example.com"
  ],
  "email_from": "user@example.com",
  "email_to": "user@example.com",
  "html": false,
  "message": "Please find the reports attached",
  "subject": "Weekly report"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|string|False|Result|ok|
  
Example output:

```
{
  "result": "ok"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* If username and password are left blank, the plugin will not try to authenticate.
* Attachment content must be Base64 encoded. The error message shows which input contains the invalid attachment.
* Attachments with empty content are skipped.
* Attachment filenames longer than 255 characters are shortened and keep their extension.
* If the SMTP server refuses only some of the recipients, the action fails but the email is still delivered to the others.

# Version History

* 3.0.0 - Added support for multiple attachments in `Send Email` action | Replaced `Attachment` input with `Attachments` | Updated SDK to the latest version (6.6.0)
* 2.0.5 - Fix issue sending emails without attachment
* 2.0.4 - New spec and help.md format for the Extension Library
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

* [Simple Mail Transfer Protocol](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)

## References

* [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)