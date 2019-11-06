# Description

The File Transfer Protocol (FTP) is a standard network protocol used to transfer computer files
between a client and server on a computer network. This plugin provides FTP functionality using
[ftplib](https://docs.python.org/3/library/ftplib.html) and [ftputil](http://ftputil.sschwarzer.net/trac/wiki/Documentation)
and supports SSL/TLS transactions.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|False|FTP username and password|None|
|passive|boolean|False|False|Passive connection for FTP server|None|
|host|string|None|True|Address of FTP server|None|
|secure|boolean|False|False|Whether TLS encryption should be used|None|

## Technical Details

### Actions

#### Download File

This action can be used to download a file from an FTP server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|path|string|None|True|Path of file to download|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|download|bytes|False|None|
|downloaded|boolean|False|None|

#### Upload File

This action can be used to upload a file to an FTP server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_content|bytes|None|True|Contents of file to upload|None|
|remote_path|string|None|True|Path of file (with filename) on remote server E.g. /home/user/upload.txt|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|uploaded|boolean|False|None|

#### Delete File

This action can be used to delete a file from an FTP server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|path|string|None|True|Path of file to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deleted|boolean|False|None|

### Triggers

#### Monitor

This trigger is used to poll for file or directory changes at an FTP server path.

It can monitor timestamps, file mode, and/or file size to check for modifications.
The poll interval frequency can be set by the user but its default value is 5 minutes.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|monitor_mode|boolean|False|False|Monitor file mode|None|
|path|string|None|True|Path to file or directory|None|
|monitor_time|boolean|True|False|Monitor file timestamp|None|
|interval|integer|300|False|Poll interval in seconds|None|
|monitor_size|boolean|False|False|Monitor file size|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|time|string|False|None|
|changed|bytes|False|None|
|mode|integer|False|None|
|size|integer|False|None|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The FTP user must have permission to execute the respective tasks.

# Version History

* 2.0.0 - Rename "Upload file" action to "Upload File" | Rename "Download file" action to "Download File" | Rename "Delete file" action to "Delete File"
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocolkj)
* [ftplib](https://docs.python.org/3/library/ftplib.html)
* [ftputil](http://ftputil.sschwarzer.net/trac/wiki/Documentation).

