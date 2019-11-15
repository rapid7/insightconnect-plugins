# Description

[SMB](https://en.wikipedia.org/wiki/Server_Message_Block) is a protocol used for interacting with files on an SMB 
server. Using this plugin, users can interact with shares and delete files automatically within Rapid7 InsightConnect
workflows. 

# Key Features

* List shares and files
* Delete files

# Requirements

* SMB server hostname
* SMB server credentials
* SMB server NetBios name

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|Address or hostname of SMB server|None|
|port|integer|445|False|Port of SMB server|None|
|credentials|credential_username_password|None|True|Username and password|None|
|domain|string|None|False|The network domain|None|
|netbios_name|string|None|True|The NetBios machine name of the remote server|None|
|use_ntlmv2|boolean|True|True|Defines use of NTLMv2 for authentication; will use NTLMv1 if set to False|None|
|timeout|integer|60|True|Connection Timeout|None|

## Technical Details

### Actions

#### Echo

This action is used to send a message to a remote server and receive the same message as a reply if successful.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|True|Message to send to remote server|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|string|True|Response|

Example output:

```
{
  "response": "hello world"
}
```

#### List Shares

This action is used to list shares on a remote server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|timeout|integer|30|False|Request timeout of operation in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|shares|[]share|True|List of Shares|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|share_name|string|None|True|Name of the SMB share|None|
|path|string|/|True|Path relative to share to return files|None|
|pattern|string|*|False|Pattern used to filter results|None|
|timeout|integer|30|False|Request timeout of operation in seconds|None|
|timezone|string|UTC|True|Timezone to be applied to datetime fields (eg. UTC, US/Eastern, US/Pacific, Europe/London). Reference https\://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid timezone names|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|[]file|True|List of Files|

Example output:

```
{
  "files": [
    {
      "name": ".",
      "short_name": "\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000",
      "is_directory": true,
      "create_time": "2019-02-15T20:54:54.803277",
      "last_access_time": "2019-03-05T02:27:48.968801",
      "last_write_time": "2019-03-05T02:27:48.968801",
      "file_size": 0
    },
    {
      "name": "..",
      "short_name": "\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000",
      "is_directory": true,
      "create_time": "2019-02-15T20:54:54.803277",
      "last_access_time": "2019-03-05T02:27:48.968801",
      "last_write_time": "2019-03-05T02:27:48.968801",
      "file_size": 0
    },
    {
      "name": "test1",
      "short_name": "\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000",
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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|share_name|string|None|True|Name of the SMB share|None|
|file_path|string|None|True|Path of the file to delete|None|
|timeout|integer|30|False|Request timeout of operation in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deleted|boolean|True|Deleted Success|

Example output:

```
{
  "deleted": true
}
```

#### Delete Files

This action is used to delete file(s) from a share; allows wildcards. Important: this action requires the use of SMBv1.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|share_name|string|None|True|Name of the SMB share|None|
|file_path|string|None|True|Path of file(s) to delete, accepts wildcard patterns (e.g. /test*.csv)|None|
|timeout|integer|30|False|Request timeout of operation in seconds|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deleted|boolean|True|Deleted Success|

Example output:

```
{
  "deleted": true
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [pysmb](https://pysmb.readthedocs.io/en/latest/)
* [SMB](https://en.wikipedia.org/wiki/Server_Message_Block)
* [Timezone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

