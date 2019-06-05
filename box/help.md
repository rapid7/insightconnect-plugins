
# Box

## About

[Box](https://www.box.com/) is a popular cloud storage solutions for consumers and businesses of any size.

This plugin utilizes the [Box SDK](https://box-python-sdk.readthedocs.io/en/latest/) Python library.

## Actions

### Lock File

This action is used to lock a file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|string|None|True|Specific file to lock|None|
|download_prevented|boolean|None|False|File cannot be downloaded while locked|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

### Delete File

This action is used to delete a file by ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|File ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

### Create User

This action is used to create a user account in Box enterprise.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|login|string|None|True|Login email|None|
|name|string|None|True|Username|None|
|role|string|User|False|Enterprise role e.g. coadmin, user|['Coadmin', 'User']|
|sync|boolean|None|False|Whether or not this user can use Box Sync|None|
|job_title|string|None|False|User's job title|None|
|phone|string|None|False|User's phone number|None|
|address|string|None|False|User's street address|None|
|space_amount|integer|None|False|User's total available space amount in bytes|None|
|timezone|string|None|False|User's timezone|None|
|two_factor|boolean|None|False|Exempt two-factor authentication|None|
|exempt_device|boolean|None|False|Exempt this user from Enterprise device limits|None|

#### Output

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

### Get Folder

This action is used to fetch a folder by name to obtain ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|folder_name|string|None|True|Folder Name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|None|

### Delete Folder

This action is used to delete a folder by ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Folder ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

### Delete User Account

This action is used to delete specific user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|User ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

### Get User Info

This action is used to retrieve user information.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|User's ID|None|

#### Output

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

### Download File

This action is used to download file by ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|string|None|True|Specific file ID to download|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|
|url|string|False|None|
|file|bytes|False|None|

### Unlock File

This action is used to unlock a file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|string|None|True|Specific file to unlock|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

### Get File

This action is used to retrieve a specific file ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_name|string|None|True|File Name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|None|

### Upload File

This action is used to upload a file. Input "0" for root folder. Include extention in filename.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|File name, max. 225 char, no special characters accepted|None|
|file|string|None|True|File to upload|None|
|folder_id|string|None|True|Parent folder ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

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

## Troubleshooting

The RSA token private key, JWT, client ID and secret must be provided to the plugin, and the public key must be submitted to your Box account.

## Workflows

Examples:

* Enterprise file management

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 2.0.0 - Update formatting of connection credentials
* 2.0.1 - Improper escaping of `\n` could cause connection error bug fix
* 2.0.2 - Fix issue with credentials in InsightConnect
* 2.0.3 - Fix issue where size was sometimes reported as a float

## References

* [Box](https://www.box.com/)
* [BOX Developers](https://docs.box.com/docs/)
* [BOX](https://app.box.com/login/)
* [boxsdk](https://box-python-sdk.readthedocs.io/en/latest/)
