# Description

[SMB](https://en.wikipedia.org/wiki/Server_Message_Block) is a protocol used for interacting with files on an SMB server. Using this plugin, users can interact with shares and delete files automatically within Rapid7 InsightConnect workflows

# Key Features

* Delete files
* Create files
* Download files

# Requirements

* SMB server hostname
* SMB server credentials
* SMB server Domain

# Supported Product Versions

* SMB1
* SMB2
* SMB3

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username and password|None|{"username": "user@example.com", "password": "mypassword"}|None|None|
|domain|string|None|False|The network domain|None|example.com|None|None|
|host|string|None|True|Address or hostname of the SMB server|None|198.51.100.1|None|None|
|port|integer|445|False|Port of the SMB server|None|445|None|None|
|timeout|integer|60|True|Connection timeout|None|30|None|None|

Example input:

```
{
  "credentials": {
    "password": "mypassword",
    "username": "user@example.com"
  },
  "domain": "example.com",
  "host": "198.51.100.1",
  "port": 445,
  "timeout": 60
}
```

## Technical Details

### Actions


#### Create File

This action is used to create a file in a given share

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_content|string|None|True|File content|None|V2hhdCdzIHVwIGd1eXMh|None|None|
|file_path|string|None|True|Path relative to share to create a file|None|test.csv|None|None|
|overwrite_existing|boolean|False|True|Overwrite existing file if set to True|None|True|None|None|
|share_name|string|None|True|Name of the SMB share|None|data|None|None|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|None|None|
  
Example input:

```
{
  "file_content": "V2hhdCdzIHVwIGd1eXMh",
  "file_path": "test.csv",
  "overwrite_existing": false,
  "share_name": "data",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|created|boolean|False|Creation success|True|
  
Example output:

```
{
  "created": true
}
```

#### Delete File

This action is used to delete a file from the share

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_path|string|None|True|Path of the file to delete|None|test.csv|None|None|
|share_name|string|None|True|Name of the SMB share|None|data|None|None|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|None|None|
  
Example input:

```
{
  "file_path": "test.csv",
  "share_name": "data",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|deleted|boolean|True|Deletion success|True|
  
Example output:

```
{
  "deleted": true
}
```

#### Download File

This action is used to download a file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_path|string|None|True|Path relative to share of the file to download|None|test.txt|None|None|
|share_name|string|None|True|Name of the SMB share|None|smbshare|None|None|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|None|None|
  
Example input:

```
{
  "file_path": "test.txt",
  "share_name": "smbshare",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file|file|False|Downloaded file|{'content': "What's up guys!", 'filename': 'text.txt'}|
  
Example output:

```
{
  "file": {
    "content": "What's up guys!",
    "filename": "text.txt"
  }
}
```

#### Echo

This action is used to send a message to a remote server and receive the same message as a reply if successful

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|message|string|None|True|Message to send to the remote server|None|Hello world|None|None|
  
Example input:

```
{
  "message": "Hello world"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|string|True|Server response|Hello world|
  
Example output:

```
{
  "response": "Hello world"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**share**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Share Comments|string|None|None|Share comments|None|
|Share Name|string|None|None|Share name|None|
  
**file**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Create Time|date|None|None|Datetime the file was created|None|
|File Size|integer|None|None|File size in number of bytes|None|
|Is Directory|boolean|None|None|Is directory|None|
|Last Access Time|date|None|None|Datetime the file was last accessed|None|
|Last Write Time|date|None|None|Datetime the file was last updated|None|
|File Name|string|None|None|File name|string|
|Short Name|string|None|None|Short name|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 3.0.0 - Migrated from `pysmb` to `smbprotocol` (allow for SMB2/3 support) | Added SDK (v6.3.2) | `echo` unit test added
* 2.0.0 - New actions Create File, Download File, Get Attributes | Update Echo action output
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [SMB](https://en.wikipedia.org/wiki/Server_Message_Block)

## References

* [smbprotocol](https://pypi.org/project/smbprotocol/)
* [SMB](https://en.wikipedia.org/wiki/Server_Message_Block)