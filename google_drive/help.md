# Description

This plugin allows you to upload and retrieve files from google drive.

This plugin utilizes the [Google Drive API](https://developers.google.com/drive/v3/web/about-sdk).

# Key Features

* Get file contents
* upload files

# Requirements

* A JWT With Google Drive Permissions
* The Google Drive API must be enabled

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|private_key|password|None|True|Private Key from service credentials|None|
|admin_user|string|None|True|Admin user to impersonate, e.g. admin@domain.com|None|
|private_key_id|password|None|True|Private Key ID from service credentials|None|
|token_uri|string|https\://accounts.google.com/o/oauth2/token|True|OAUTH2 Token URI|None|
|auth_provider_x509_cert_url|string|https\://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|
|auth_uri|string|https\://accounts.google.com/o/oauth2/auth|True|None|None|
|client_email|string|None|True|Client email from service credentials|None|
|client_id|string|None|True|Client ID|None|
|project_id|string|None|True|Project ID from service credentials|None|
|client_x509_cert_url|string|None|True|x509 cert URL from service credentials|None|

## Technical Details

### Actions

#### Find File by Name

This action is used to find a file ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|parent_id|string|None|False|The ID of the parent folder|None|
|filename_operator|string|None|True|How the filename search will be performed. =,!=, or contains|['=', '!=', 'contains']|
|filename|string|None|True|The name of the file to search for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files_found|[]file_info|False|Returns a list of file names and their IDs|

Example output:

```

{
  "files_found": [
    {
      "file_name": "test.txt",
      "file_id": "1t4HfdfndRpYHRw4uRtqnu83XC7Oc3nBGqEHyaiPIDy0"
    }
    {
      "file_name": "test_new2.txt",
      "file_id":"13Cxn1BPUnvQGcRVcnCBSF4ZbS0MbVxaxNJe2iuj_NTA"
    }
  ]
}

```

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|content|bytes|None|True|The new data that will overwrite the old file|None|
|new_mime_type|string|None|False|Select a new MIME type for the file|['Docs', 'Sheets', 'Slides', "Don't update"]|
|new_file_name|string|None|False|Select a new file name. e.g. testfile.csv|None|
|file_id|string|None|True|The file ID for the file that will be overwritten|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_id|string|False|Return the ID of the file created on Google Drive|

Example output:

```

{
  "file_id": "1WaKb1NPiFj9Mpgkn0CYA-zmJZLpPi38P-PJih5Aa7DA"
}

```

#### Upload File

This action is used to upload a file to Google Drive.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|google_file_type|string|None|True||['Docs', 'Sheets', 'Slides']|
|folder_id|string|None|False|Folder to put the file in|None|
|file|file|None|True|The File to upload|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_link|string|False|A direct link to the created file|
|file_id|string|False|Return the ID of the file created on Google Drive|

Example output:

```

{
  "file_id": "1vGnLfWUInJ5OhuTXQO1-UpVfPfsXVlmaFnvqY_uhT0M",
  "file_link": "https://docs.google.com/document/d/1vGnLfWUInJ5OhuTXQO1-UpVfPfsXVlmaFnvqY_uhT0M"
}

```

#### Overwrite File

This action is used to overwrites a file with new data.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|content|bytes|None|True|The new data that will overwrite the old file|None|
|new_mime_type|string|None|True|Select a new MIME type for the file|['Docs', 'Sheets', 'Slides']|
|new_file_name|string|None|False|Select a new file name. e.g. testfile.csv|None|
|file_id|string|None|True|The file ID for the file that will be overwritten|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_id|string|False|Return the ID of the file created on Google Drive|

Example output:

```
```

#### Get File Contents

This action is used to get the contents of a file on Google Drive.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_id|string|None|True|The file ID for the file that will be returned|None|
|mime_type|string|None|True|The MIME Type to export the file as e.g. */* , text/plain|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|False|The file in bytes|

Example output:

```
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

* It is very important to use the full filename including the file extension e.g. example.docx. Google Drive uses the file extension to determine how to format the file. Not using a file extension will result in a error and using the wrong file extension may result in file corruption
* When using file overwrite, Google can not change formats. I.E. If the orignal file is a Google sheets file, then the new file will also be a Google sheets file.
* When using file overwrite, the MIME Type should be set to the correct type to avoid data formatting issues.

# Version History

* 2.1.1 - Fix typo in plugin spec
* 2.1.0 - Add Download File action
* 2.0.0 - Update to use new credential types
* 1.2.1 - Fixed a bug that caused an error if Folder ID was left blank
* 1.2.0 - Add the ablity to rename and force a MIME type on the overwrite action
* 1.1.0 - Add overwrite file action and search file action
* 1.0.0 - Initial plugin

# Links

## References

* [oauth2client](https://github.com/google/oauth2client)
* [httplib2](https://github.com/httplib2/httplib2)
* [google-api-python-client](https://github.com/google/google-api-python-client)

