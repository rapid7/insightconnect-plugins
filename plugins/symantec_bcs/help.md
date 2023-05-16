# Description

The Symantec BCS plugin allows you to submit a file to Symantec Security Response.

[Symantec BCS](https://submit.symantec.com/websubmit/bcs.cgi) is a suspected infected file or hash submission form that sends data to Symantec Security Response.

# Key Features

* Submit a malicious file or hash

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Submit

This action is used to submit a malicious file or hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|pin|string|None|True|Support ID number|None|1|
|comments|string|None|True|Additional information|None|Example Comment|
|lname|string|None|True|Last name|None|Smith|
|cname|string|None|True|Company name|None|Example Organization|
|critical|boolean|False|True|None|None|True|
|fname|string|None|True|First name|None|John|
|data|bytes|None|True|URL to file, hash (MD5 or SHA256), or base64 file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
|email|string|None|True|Email address|None|user@example.com|
|stype|string|None|True|Submission type|['upfile', 'url', 'hash']|upfile|
|filename|string|None|False|Optional filename if submission type is upfile|None|malicious-file|

Example input:

```
{
  "pin": "1",
  "comments": "Example Comment",
  "lname": "Smith",
  "cname": "Example Organization",
  "critical": True,
  "fname": "John",
  "data": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "email": "user@example.com",
  "stype": "upfile",
  "filename": "malicious-file"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|string|True|HTML response|<!DOCTYPE html> <html> <body> <h1>Example Response</h1> </body> </html>|

Example output:

```
{
  "response": "<!DOCTYPE html> <html> <body> <h1>Example Response</h1> </body> </html>"
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - Update requests to 2.20.0 | Update to insightconnect-plugin-runtime | Fix Error handling
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

*[Broadcom](https://www.broadcom.com/)

## References

* [Symantec BCS](https://submit.symantec.com/websubmit/bcs.cgi)
