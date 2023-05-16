# Description
  
The Symantec Business Critical Services plugin allows you to submit a file to Symantec Security Response
# Key Features

* Submit a malicious file or hash

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions
  
* 2023-05-16
# Documentation

## Setup
  
*This plugin does not contain a connection.*
## Technical Details

### Actions

#### Submit
Submit a malicious file or hash
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cname|string|None|True|Company name|None|Example Organization|
|comments|string|None|True|Additional information|None|Example Comment|
|critical|boolean|False|True|High severity|None|True|
|data|bytes|None|True|URL to file, hash (MD5 or SHA256), or base64 file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
|email|string|None|True|Email address|None|user@example.com|
|filename|string|None|False|Optional filename if submission type is upfile|None|malicious-file|
|fname|string|None|True|First name|None|John|
|lname|string|None|True|Last name|None|Smith|
|pin|string|None|True|Support ID number|None|1|
|stype|string|None|True|Submission type|['upfile', 'url', 'hash']|upfile|
  
Example input:

```
{
  "cname": "Example Organization",
  "comments": "Example Comment",
  "critical": false,
  "data": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "email": "user@example.com",
  "filename": "malicious-file",
  "fname": "John",
  "lname": "Smith",
  "pin": 1,
  "stype": "upfile"
}
```
##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|response|string|None|True|HTML response|None|"<!DOCTYPE html> <html> <body> <h1>Example Response</h1> </body> </html>"|
  
Example output:

```
{
  "response": "<!DOCTYPE html> <html> <body> <h1>Example Response</h1> </body> </html>"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*
### Custom Types
  
*This plugin does not contain any custom output types.*
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
