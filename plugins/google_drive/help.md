# Description

[Google Drive](https://www.google.com/drive/) is an online file storage and management system. This plugin allows you to upload and retrieve files from Google drive.

This plugin utilizes the [Google Drive API](https://developers.google.com/drive/v3/web/about-sdk).

# Key Features
  
* Get file contents  
* Upload files  
* Create files  
* Move files to a different folder  
* Find files by name  
* Copy files to a folder

# Requirements
  
* A JWT With Google Drive Permissions  
* The Google Drive API must be enabled

# Supported Product Versions
  
* Google Drive API v3 2021-09-27

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|admin_user|string|None|True|Admin user to impersonate, e.g. user@example.com|None|user@example.com|
|auth_provider_x509_cert_url|string|https://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|https://www.googleapis.com/oauth2/v1/certs|
|auth_uri|string|https://accounts.google.com/o/oauth2/auth|True|OAUTH2 Auth URI|None|https://accounts.google.com/o/oauth2/auth|
|client_email|string|None|True|Client email from service credentials|None|user@example.com|
|client_id|string|None|True|Client ID|None|102790495738029996994|
|client_x509_cert_url|string|None|True|X509 cert URL from service credentials|None|https://www.googleapis.com/robot/v1/metadata/x509/user@example.com|
|private_key|credential_asymmetric_key|None|True|Private Key from service credentials|None|-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAjGnoUtfPHqvX3PIU6N9FKmwQ3Zl+NoaWb4yMLhudkdEBJ3Au...8/dqUH5yjRKs2qxkBWG4HmT3Nx6A8sYIrUYxyqVLBpG8yKngbnaYPV4=
-----END RSA PRIVATE KEY-----|
|private_key_id|string|None|True|Private Key ID from service credentials|None|02699626f388ed830012e5b787640e71c56d42d8|
|project_id|string|None|True|Project ID from service credentials|None|example-12345|
|token_uri|string|https://accounts.google.com/o/oauth2/token|True|OAUTH2 Token URI|None|https://accounts.google.com/o/oauth2/token|
  
Example input:

```
{
  "admin_user": "user@example.com",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "client_email": "user@example.com",
  "client_id": 102790495738029996994,
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/user@example.com",
  "private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpQIBAAKCAQEAjGnoUtfPHqvX3PIU6N9FKmwQ3Zl+NoaWb4yMLhudkdEBJ3Au...8/dqUH5yjRKs2qxkBWG4HmT3Nx6A8sYIrUYxyqVLBpG8yKngbnaYPV4=\n-----END RSA PRIVATE KEY-----",
  "private_key_id": "02699626f388ed830012e5b787640e71c56d42d8",
  "project_id": "example-12345",
  "token_uri": "https://accounts.google.com/o/oauth2/token"
}
```

## Technical Details

### Actions


#### Copy File
  
This action is used to copy a file to a folder

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_id|string|None|True|The ID of the file that will be copied to another folder|None|1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR|
|folder_id|string|None|True|ID of the folder where the file will be copied|None|0BwwA4oUTeiV1TGRPeTVjaWRDY1E|
|new_file_name|string|None|False|Select a new file name. e.g. testfile.csv|None|test.txt|
  
Example input:

```
{
  "file_id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR",
  "folder_id": "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
  "new_file_name": "test.txt"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|copy_file_result|True|The result containing the ID of the file and ID of the folder to which the file was copied|{"id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR", "parents": ["0BwwA4oUTeiV1TGRPeTVjaWRDY1E"]}|
  
Example output:

```
{
  "result": {
    "id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR",
    "parents": [
      "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"
    ]
  }
}
```

#### Create File in Folder
  
This action is used to create a file in a folder

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file|file|None|True|The file to create|None|{'filename': 'test.txt', 'content': 'UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=='}|
|folder_id|string|None|True|The ID of the folder where the file will be created|None|0BwwA4oUTeiV1TGRPeTVjaWRDY1E|
  
Example input:

```
{
  "file": {
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
    "filename": "test.txt"
  },
  "folder_id": "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file_id|string|True|Return the ID of the file created on Google Drive|1bKpnBMV1TQ5iU6sM7d0sfovqWwdVJSet|
  
Example output:

```
{
  "file_id": "1bKpnBMV1TQ5iU6sM7d0sfovqWwdVJSet"
}
```

#### Create Folder
  
This action is used to create a folder

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|folder_name|string|None|True|The name for the new folder|None|New Folder|
|parent_folder_id|string|None|False|The ID of the folder in which the new folder will be created|None|0BwwA4oUTeiV1TGRPeTVjaWRDY1E|
  
Example input:

```
{
  "folder_name": "New Folder",
  "parent_folder_id": "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|folder_id|string|True|Return the ID of the folder created on Google Drive|1eYy68j4cIucDRE1pAkar5bOgyLxCM_Rj|
  
Example output:

```
{
  "folder_id": "1eYy68j4cIucDRE1pAkar5bOgyLxCM_Rj"
}
```

#### Find File by Name
  
This action is used to find a file ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filename|string|None|True|The name of the file to search for|None|test|
|filename_operator|string|None|True|How the filename search will be performed. =,!=, or contains|["=", "!=", "contains"]|contains|
|parent_id|string|None|False|The ID of the parent folder|None|0BwwA4oUTeiV1TGRPeTVjaWRDY1E|
  
Example input:

```
{
  "filename": "test",
  "filename_operator": "contains",
  "parent_id": "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|files_found|[]file_info|False|Returns a list of file names and their IDs|[{"file_name":"test.txt","file_id":"1t4HfdfndRpYHRw4uRtqnu83XC7Oc3nBGqEHyaiPIDy0"},{"file_name":"test_new2.txt","file_id":"13Cxn1BPUnvQGcRVcnCBSF4ZbS0MbVxaxNJe2iuj_NTA"}]|
  
Example output:

```
{
  "files_found": [
    {
      "file_id": "1t4HfdfndRpYHRw4uRtqnu83XC7Oc3nBGqEHyaiPIDy0",
      "file_name": "test.txt"
    },
    {
      "file_id": "13Cxn1BPUnvQGcRVcnCBSF4ZbS0MbVxaxNJe2iuj_NTA",
      "file_name": "test_new2.txt"
    }
  ]
}
```

#### Get File Contents
  
This action is used to get the contents of a file on Google Drive

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_id|string|None|True|The file ID for the file that will be returned|None|1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ|
|mime_type|string|None|True|The MIME Type to export the file as e.g. */* , text/plain|None|text/plain|
  
Example input:

```
{
  "file_id": "1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ",
  "mime_type": "text/plain"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file|bytes|False|The file in bytes|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "file": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

#### Move File
  
This action is used to move a file to a different folder

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_id|string|None|True|The ID of the file that will be moved to another folder|None|1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR|
|folder_id|string|None|True|ID of the folder where the file will be moved|None|0BwwA4oUTeiV1TGRPeTVjaWRDY1E|
  
Example input:

```
{
  "file_id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR",
  "folder_id": "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|move_file_result|True|The result containing the ID of the file and ID of the folder to which the file was moved|{"id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR", "parents": ["0BwwA4oUTeiV1TGRPeTVjaWRDY1E"]}|
  
Example output:

```
{
  "result": {
    "id": "1pAT5CqVKi6XtyaD4betZvDQqOt8ZcuUR",
    "parents": [
      "0BwwA4oUTeiV1TGRPeTVjaWRDY1E"
    ]
  }
}
```

#### Overwrite File
  
This action is used to overwrites a file with new data

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|content|bytes|None|True|The new data that will overwrite the old file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
|file_id|string|None|True|The file ID for the file that will be overwritten|None|1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ|
|new_file_name|string|None|False|Select a new file name. e.g. testfile.csv|None|test.txt|
|new_mime_type|string|None|True|Select a new MIME type for the file|["Docs", "Sheets", "Slides"]|Docs|
  
Example input:

```
{
  "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "file_id": "1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLPNQ",
  "new_file_name": "test.txt",
  "new_mime_type": "Docs"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file_id|string|False|Return the ID of the file created on Google Drive|1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLREW|
  
Example output:

```
{
  "file_id": "1sTWaJ_j7PkjzaBWtNc3IzovK5hQf21FbOw9yLeeLREW"
}
```

#### Upload File
  
This action is used to upload a file to Google Drive

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file|file|None|True|The file to upload|None|{'filename': 'test.txt', 'content': 'UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=='}|
|folder_id|string|None|False|Folder to put the file in|None|0BwwA4oUTeiV1TGRPeTVjaWRDY1E|
|google_file_type|string|None|True|The file type that Google will convert the file to|["Docs", "Sheets", "Slides"]|Docs|
  
Example input:

```
{
  "file": {
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
    "filename": "test.txt"
  },
  "folder_id": "0BwwA4oUTeiV1TGRPeTVjaWRDY1E",
  "google_file_type": "Docs"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file_id|string|False|Return the ID of the file created on Google Drive|1vGnLfWUInJ5OhuTXQO1-UpVfPfsXVlmaFnvqY_uhT0M|
|file_link|string|False|A direct link to the created file|https://docs.google.com/document/d/1vGnLfWUInJ5OhuTXQO1-UpVfPfsXVlmaFnvqY_uhT0M|
  
Example output:

```
{
  "file_id": "1vGnLfWUInJ5OhuTXQO1-UpVfPfsXVlmaFnvqY_uhT0M",
  "file_link": "https://docs.google.com/document/d/1vGnLfWUInJ5OhuTXQO1-UpVfPfsXVlmaFnvqY_uhT0M"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**file_info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|File ID|string|None|None|None|None|
|File Name|string|None|None|None|None|
  
**move_file_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|File ID|string|None|None|File ID|None|
|Folder ID|[]string|None|None|Folder ID|None|
  
**copy_file_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|File ID|string|None|None|File ID|None|
|Folder ID|[]string|None|None|Folder ID|None|


## Troubleshooting
  
* It is very important to use the full filename including the file extension e.g. example.docx. Google Drive uses the file extension to determine how to format the file. Not using a file extension will result in a error and using the wrong file extension may result in file corruption
* When using file overwrite, Google can not change formats. I.E. If the original file is a Google sheets file, then the new file will also be a Google sheets file.
* When using file overwrite, the MIME Type should be set to the correct type to avoid data formatting issues.

# Version History

* 3.0.0 - Implement shared drive support | Add Copy file action | Code refactor  
* 2.2.0 - Add Create Folder, Create File in Folder and Move File actions | Add missing input and output examples | Code refactor  
* 2.1.3 - Correct spelling in help.md  
* 2.1.2 - New spec and help.md format for the Extension Library  
* 2.1.1 - Fix typo in plugin spec  
* 2.1.0 - Add Download File action  
* 2.0.0 - Update to use new credential types  
* 1.2.1 - Fixed a bug that caused an error if Folder ID was left blank  
* 1.2.0 - Add the ability to rename and force a MIME type on the overwrite action  
* 1.1.0 - Add overwrite file action and search file action  
* 1.0.0 - Initial plugin

# Links

* https://developers.google.com/drive/api/guides/about-sdk

## References
  
* oauth2client - https://github.com/google/oauth2client  
* httplib2 - https://github.com/httplib2/httplib2  
* google-api-python-client - https://github.com/google/google-api-python-client  
* Google Drive API - https://developers.google.com/drive/api/guides/about-sdk