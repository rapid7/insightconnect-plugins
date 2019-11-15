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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pin|string|None|True|Support ID number|None|
|comments|string|None|True|Additional information|None|
|lname|string|None|True|Last name|None|
|cname|string|None|True|Company name|None|
|critical|boolean|False|True|None|None|
|fname|string|None|True|First name|None|
|data|bytes|None|True|URL to file, hash (MD5 or SHA256), or base64 file|None|
|email|string|None|True|Email address|None|
|stype|string|None|True|Submission type|['upfile', 'url', 'hash']|
|filename|string|None|False|Optional filename if submission type is upfile|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|string|True|HTML response|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Symantec BCS](https://submit.symantec.com/websubmit/bcs.cgi)

