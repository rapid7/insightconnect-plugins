# Description

[SMB](https://en.wikipedia.org/wiki/Server_Message_Block) is a protocol used for interacting with files on an SMB server. Using this plugin, users can interact with shares and delete files automatically within Rapid7 InsightConnect workflows

# Key Features

* List shares and files
* Delete files
* Create files
* Download files
* Get file attributes

# Requirements

* SMB server hostname
* SMB server credentials
* SMB server NetBios name

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
|netbios_name|string|None|True|The NetBIOS machine name of the remote server|None|example.com|None|None|
|port|integer|445|False|Port of the SMB server|None|445|None|None|
|timeout|integer|60|True|Connection timeout|None|30|None|None|
|use_ntlmv2|boolean|True|True|Defines use of NTLMv2 for authentication; will use NTLMv1 if set to false|None|True|None|None|

Example input:

```
{
  "credentials": {
    "password": "mypassword",
    "username": "user@example.com"
  },
  "domain": "example.com",
  "host": "198.51.100.1",
  "netbios_name": "example.com",
  "port": 445,
  "timeout": 60,
  "use_ntlmv2": true
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

#### Delete Files

This action is used to delete file(s) from the share; allows wildcards

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_path|string|None|True|Path of file(s) to delete, accepts wildcard patterns|None|test*.csv|None|None|
|share_name|string|None|True|Name of the SMB share|None|data|None|None|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|None|None|
  
Example input:

```
{
  "file_path": "test*.csv",
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
|file_path|string|None|True|Path relative to share of the file to download|None|test.csv|None|None|
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
|file|file|False|Downloaded file|{'content': 'bytes', 'filename': 'string'}|
  
Example output:

```
{
  "file": {
    "content": "bytes",
    "filename": "string"
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

#### Get Attributes

This action is used to get attributes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_path|string|None|True|Path relative to share to get file attributes|None|test.csv|None|None|
|share_name|string|None|True|Name of the SMB share|None|data|None|None|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|None|None|
|timezone|string|UTC|False|Timezone to be applied to datetime fields (eg. UTC, US/Eastern, US/Pacific, Europe/London). Reference https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid timezone names|None|UTC|None|None|
  
Example input:

```
{
  "file_path": "test.csv",
  "share_name": "data",
  "timeout": 30,
  "timezone": "UTC"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attributes|file|True|File attributes|{'content': 'bytes', 'filename': 'string'}|
  
Example output:

```
{
  "attributes": {
    "content": "bytes",
    "filename": "string"
  }
}
```

#### List Share Files

This action is used to list files on the remote server share

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|path|string|/|True|Path relative to share to return files|None|test.csv|None|None|
|pattern|string|*|False|Pattern used to filter results|None|*|None|None|
|share_name|string|None|True|Name of the SMB share|None|data|None|None|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|None|None|
|timezone|string|UTC|True|Timezone to be applied to datetime fields (eg. UTC, US/Eastern, US/Pacific, Europe/London). Reference https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid timezone names|None|UTC|None|None|
  
Example input:

```
{
  "path": "/",
  "pattern": "*",
  "share_name": "data",
  "timeout": 30,
  "timezone": "UTC"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|files|[]file|True|List of Files|None|
  
Example output:

```
{
  "files": [
    {
      "content": "bytes",
      "filename": "string"
    }
  ]
}
```

#### List Shares

This action is used to list shares on the remote server

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|None|None|
  
Example input:

```
{
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|shares|[]share|True|List of shares|None|
  
Example output:

```
{
  "shares": [
    {
      "Share Comments": {},
      "Share Name": ""
    }
  ]
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

* 2.1.0 - Bumping packages | Adding SDK | Added unit tests
* 2.0.0 - New actions Create File, Download File, Get Attributes | Update Echo action output
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [SMB](https://en.wikipedia.org/wiki/Server_Message_Block)

## References

* [pysmb](https://pysmb.readthedocs.io/en/latest/)
* [SMB](https://en.wikipedia.org/wiki/Server_Message_Block)
* [Timezone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)