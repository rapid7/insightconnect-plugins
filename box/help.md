# Description

[Box](https://www.box.com/) is a popular cloud storage solutions for consumers and businesses of any size. Using the InsightConnect plugin you can manage users and files.

This plugin utilizes the [Box SDK](https://box-python-sdk.readthedocs.io/en/latest/) Python library.

# Key Features

* Add and delete users
* Download and upload files

# Requirements

* Create a RSA token and submit it to Box
* Create a JWT key in Box

# Documentation

## Setup

This plugin requires a Box enterprise account and a self generated and submitted RSA token and (optional) password.
The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|client_id|string|None|True|Box client ID|None|
|client_secret|credential_secret_key|None|True|Box client secret|None|
|enterprise_id|string|None|True|Box enterprise ID|None|
|private_key|credential_secret_key|None|True|User generated private key|None|
|rsa_password|credential_secret_key|None|False|Private key password|None|
|jwt_key_id|string|None|True|Box generated JWT key ID|None|

## Technical Details

### Actions

#### Lock File

This action is used to lock a file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|string|None|True|Specific file to lock|None|
|download_prevented|boolean|None|False|File cannot be downloaded while locked|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Delete File

This action is used to delete a file by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|File ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Create User

This action is used to create a user account in Box enterprise.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|False|User's street address|None|
|exempt_device|boolean|None|False|Exempt this user from Enterprise device limits|None|
|job_title|string|None|False|User's job title|None|
|login|string|None|True|Login email|None|
|name|string|None|True|Username|None|
|phone|string|None|False|User's phone number|None|
|role|string|User|False|Enterprise role e.g. coadmin, user|['Coadmin', 'User']|
|space_amount|float|None|False|User's total available space amount in bytes. -1 will set the user to unlimited|None|
|sync|boolean|None|False|Whether or not this user can use Box Sync|None|
|timezone|string|None|False|User's timezone|None|
|two_factor|boolean|None|False|Exempt two-factor authentication|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|login|string|False|User email|
|id|string|False|User ID|
|name|string|False|Username|
|timezone|string|False|Timezone|
|space_amount|integer|False|Max space amount|
|sync|boolean|False|Sync|
|exempt_device|boolean|False|Device limits exemption|
|two_factor|boolean|False|Login verification exemption|
|job_title|string|False|Job title|
|phone|string|False|User phone number|
|address|string|False|User address|
|avatar_url|string|False|User avatar|

#### Get Folder

This action is used to fetch a folder by name to obtain ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|folder_name|string|None|True|Folder Name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|None|

#### Delete Folder

This action is used to delete a folder by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Folder ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Delete User Account

This action is used to delete specific user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|User ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Get User Info

This action is used to retrieve user information.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|User's ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|name|string|False|None|
|timezone|string|False|None|
|phone|string|False|None|
|avatar_url|string|False|None|
|space_used|integer|False|None|
|address|string|False|None|
|space_amount|integer|False|None|
|login|string|False|None|
|id|string|False|None|
|job_title|string|False|None|

#### Get User Info from Login

This action is used to retrieve user information using their login ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|login|string|None|True|User's login e.g. bob@hotmail.com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address|string|False|User address|
|avatar_url|string|False|User avatar|
|id|string|False|User ID|
|job_title|string|False|Job title|
|login|string|False|User email|
|name|string|False|Username|
|phone|string|False|User phone number|
|space_amount|float|False|Max space amount|
|space_used|float|False|Space used|
|timezone|string|False|Timezone|

Example output:

```
{
  "address": "103 memory lane, apt. 21, 61801",
  "avatar_url": "https://app.box.com/api/avatar/large/8830457340",
  "id": "8830457340",
  "job_title": "guinepig3",
  "login": "randomtestuser@somerandomdomain.com",
  "name": "bob",
  "phone": "5555555555",
  "space_amount": 10737418240,
  "space_used": 0,
  "timezone": "America/Los_Angeles"
}
```

#### Download File

This action is used to download file by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|string|None|True|Specific file ID to download|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|
|url|string|False|None|
|file|bytes|False|None|

#### Unlock File

This action is used to unlock a file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|string|None|True|Specific file to unlock|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Get File

This action is used to retrieve a specific file ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_name|string|None|True|File Name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|None|

#### Upload File

This action is used to upload a file. Input "0" for root folder. Include extention in filename.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|File name, max. 225 char, no special characters accepted|None|
|file|string|None|True|File to upload|None|
|folder_id|string|None|True|Parent folder ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

#### Get Enterprise Groups

This action is used to get all enterprise groups.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group_name|string|None|False|Group name to find|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|groups|[]group|False|Groups|

Example output:

```
{
  "groups": [
    {
      "type": "group",
      "id": "38901557",
      "name": "group1",
      "group_type": "managed_group"
    },
    {
      "type": "group",
      "id": "66186068",
      "name": "group2",
      "group_type": "managed_group"
    }
  ]
}
```

#### Add User to Group

This action is used to add a user to a group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group_id|string|None|True|Group ID|None|
|role|string|None|True|Role|['admin', 'member']|
|user_id|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|group|object|False|Group|

Example output:

```
{
  "group": {
    "user_id": "8830457340",
    "group_id": "66186068",
    "role": "member",
    "type": "group_membership"
  }
}
```

#### Get User Groups

This action is used to get groups for a given user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|False|User ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|groups|[]group|False|Groups|

Example output:

```
{
  "groups": [
    {
      "user_id": "8830457340",
      "group_id": "66186068",
      "role": "member",
      "type": "group_membership",
      "name": "bloop"
    },
    {
      "user_id": "8830457340",
      "group_id": "38901557",
      "role": "member",
      "type": "group_membership",
      "name": "blah"
    }
  ]
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The RSA token private key, JWT, client ID and secret must be provided to the plugin, and the public key must be submitted to your Box account.

# Version History

* 2.2.3 - New spec and help.md format for the Hub
* 2.2.2 - New spec and help.md format for the Hub
* 2.2.1 - Fix issue where a misleading error message could be given in the log
* 2.2.0 - New actions Get User Groups and Get User Info from Login
* 2.1.0 - New actions Get Enterprise Groups and Add User to Group
* 2.0.4 - Update to `Create User` action `Space Amount` input showing input for unlimited size
* 2.0.3 - Fix issue where size was sometimes reported as a float
* 2.0.2 - Fix issue with credentials in InsightConnect
* 2.0.1 - Improper escaping of `\n` could cause connection error bug fix
* 2.0.0 - Update formatting of connection credentials
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Box](https://www.box.com/)
* [BOX Developers](https://docs.box.com/docs/)
* [BOX](https://app.box.com/login/)
* [boxsdk](https://box-python-sdk.readthedocs.io/en/latest/)

