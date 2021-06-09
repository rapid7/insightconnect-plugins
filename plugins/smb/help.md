# Description

[SMB](https://en.wikipedia.org/wiki/Server_Message_Block) is a protocol used for interacting with files on an SMB
server. Using this plugin, users can interact with shares and delete files automatically within Rapid7 InsightConnect
workflows.

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

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username": "user@example.com", "password": "mypassword"}|
|domain|string|None|False|The network domain|None|example.com|
|host|string|None|True|Address or hostname of the SMB server|None|198.51.100.1|
|netbios_name|string|None|True|The NetBIOS machine name of the remote server|None|example.com|
|port|integer|445|False|Port of the SMB server|None|445|
|timeout|integer|60|True|Connection timeout|None|30|
|use_ntlmv2|boolean|True|True|Defines use of NTLMv2 for authentication; will use NTLMv1 if set to false|None|True|

Example input:

```
{
  "credentials": "{\"username\": \"user@example.com\", \"password\": \"mypassword\"}",
  "domain": "example.com",
  "host": "198.51.100.1",
  "netbios_name": "example.com",
  "port": 445,
  "timeout": 30,
  "use_ntlmv2": true
}
```

## Technical Details

### Actions

#### Create File

This action is used to create a file in a given share.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_content|string|None|True|File content|None|V2hhdCdzIHVwIGd1eXMh|
|file_path|string|None|True|Path relative to share to create a file|None|test.csv|
|overwrite_existing|boolean|False|True|Overwrite existing file if set to True|None|True|
|share_name|string|None|True|Name of the SMB share|None|data|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|

Example input:

```
{
  "file_content": "V2hhdCdzIHVwIGd1eXMh",
  "file_path": "test.csv",
  "overwrite_existing": true,
  "share_name": "data",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|created|boolean|False|Creation success|

Example output:

```
{
  "created": true
}
```

#### Download File

This action is used to download file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_path|string|None|True|Path relative to share of the file to download|None|test.csv|
|share_name|string|None|True|Name of the SMB share|None|data|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|

Example input:

```
{
  "file_path": "test.csv",
  "share_name": "data",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|file|False|Downloaded file|

Example output:

```
{
  "file": {
    "content": "hello world",
    "filename": "test.csv"
  }
}
```

#### Get Attributes

This action is used to get attributes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_path|string|None|True|Path relative to share to get file attributes|None|test.csv|
|share_name|string|None|True|Name of the SMB share|None|data|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|
|timezone|string|UTC|False|Timezone to be applied to datetime fields (eg. UTC, US/Eastern, US/Pacific, Europe/London). Reference https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid timezone names|None|UTC|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attributes|file|True|File attributes|

Example output:

```
{
  "attributes": {
    "create_time": "2021-06-09T17:20:37+00:00",
    "file_size": 15,
    "is_directory": false,
    "last_access_time": "2021-06-09T17:20:37+00:00",
    "last_write_time": "2021-06-09T17:20:37+00:00",
    "name": "test.csv",
    "short_name": "test.csv"
  }
}
```

#### Echo

This action is used to send a message to a remote server and receive the same message as a reply if successful.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|message|string|None|True|Message to send to the remote server|None|Hello world|

Example input:

```
{
  "message": "Hello world"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|string|True|Server response|

Example output:

```
{
  "response": "Hello world"
}
```

#### List Shares

This action is used to list shares on a remote server.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|

Example input:

```
{
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|shares|[]share|True|List of shares|

Example output:

```
{
  "shares": [
    {
      "name": "ADMIN$",
      "comments": "Remote Admin"
    },
    {
      "name": "AdminUIContentPayload",
      "comments": "AdminUIContentPayload share for AdminUIContent Packages"
    }
  ]
}
```

#### List Share Files

This action is used to list files on a remote server share.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|path|string|/|True|Path relative to share to return files|None|test.csv|
|pattern|string|*|False|Pattern used to filter results|None|*|
|share_name|string|None|True|Name of the SMB share|None|data|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|
|timezone|string|UTC|True|Timezone to be applied to datetime fields (eg. UTC, US/Eastern, US/Pacific, Europe/London). Reference https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid timezone names|None|UTC|

Example input:

```
{
  "path": "test.csv",
  "pattern": "*",
  "share_name": "data",
  "timeout": 30,
  "timezone": "UTC"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|[]file|True|List of Files|

Example output:

```
{
  "files": [
    {
      "name": "test.csv",
      "short_name": "test.csv",
      "is_directory": false,
      "create_time": "2019-03-05T02:27:48.953173",
      "last_access_time": "2019-03-05T02:27:48.953173",
      "last_write_time": "2019-02-26T23:54:31",
      "file_size": 0
    }
  ]
}
```

#### Delete File

This action is used to delete a file from a share.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_path|string|None|True|Path of the file to delete|None|test.csv|
|share_name|string|None|True|Name of the SMB share|None|data|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|

Example input:

```
{
  "file_path": "test.csv",
  "share_name": "data",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deleted|boolean|True|Deletion success|

Example output:

```
{
  "deleted": true
}
```

#### Delete Files

This action is used to delete file(s) from a share; allows wildcards. Important: this action requires the use of SMBv1.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_path|string|None|True|Path of file(s) to delete, accepts wildcard patterns|None|test*.csv|
|share_name|string|None|True|Name of the SMB share|None|data|
|timeout|integer|30|False|Request timeout of operation in seconds|None|30|

Example input:

```
{
  "file_path": "test*.csv",
  "share_name": "data",
  "timeout": 30
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deleted|boolean|True|Deletion success|

Example output:

```
{
  "deleted": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Add actions Create File, Download File, Get Attributes | Update Echo action output
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [pysmb](https://pysmb.readthedocs.io/en/latest/)
* [SMB](https://en.wikipedia.org/wiki/Server_Message_Block)
* [Timezone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

