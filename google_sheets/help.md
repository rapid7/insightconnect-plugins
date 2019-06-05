# Google Sheets

## About

[Google Sheets](https://www.google.com/sheets/about/) is used to create, edit and collaborate with others on spreadsheets.
This plugin utilizes the [Google Sheets API](https://developers.google.com/sheets/api/) and [Gspread library](https://github.com/burnash/gspread/).

## Actions

### Update Cell

This action is used to update a specified cell in Google Sheets with new data.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sheet_id|string|None|True|The ID of the spreadsheet to update|None|
|cell|string|None|True|The cell to update e.g. A1, B6, C55, etc|None|
|update|string|None|True|The data to update the cell with|None|
|worksheet|string|None|True|The worksheet to update e.g. Sheet1|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|value|string|False|The value of the updated cell|
|update_information|update|False|Information on the update performed|

Example output:

```
{
  "value": "test",
  "update_information": {
    "spreadsheetId": "1B2lGipQRx5whl_2Lebz53SQWQGfHbohYuP-ojSQYi3g",
    "updatedRange": "Sheet1!A1",
    "updatedRows": 1,
    "updatedColumns": 1,
    "updatedCells": 1
  }
}
```

### Spread List to Sheet

This action is used to given a starting cell, this action will take a list of data and push it to either rows or columns in a google sheet.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sheet_id|string|None|True|The ID of the spreadsheet to update|None|
|cell|string|None|True|The target cell to being placing data e.g. A1, B6, C55, etc|None|
|direction|string|None|True|The direction to fill in data e.g. row or column|['row', 'column']|
|update_list|[]string|None|True|The data to update the cell with|None|
|worksheet|string|None|True|The worksheet to update e.g. Sheet1|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|update_information|update|False|Information on the update performed|

Example output:

```
{
   "spreadsheetId": "1rmAH-sHB84Z0mwKMD7GpBok9mSKTW5op-b4ncvoz3H0",
   "updatedRange": "Sheet1!A1:A5",
   "updatedRows": 5,
   "updatedColumns": 1,
   "updatedCells": 5
}
```

## Triggers

This plugin does not contain any triggers.

## Connection

### Grant Google Sheets API access to service account

Once a service account as been created, it will need access to Google Sheets API. This can be done one of two ways. You can enabled it through [Turn on the Google Sheets API](https://developers.google.com/sheets/api/quickstart/python#step_1_turn_on_the) or by assigning permissions via the instructions below.

#### Scope for Google Sheets

|URL|Description|
|---|-----------|
|https://www.googleapis.com/auth/drive|View and manage the files in your Google Drive|
|https://www.googleapis.com/auth/drive.file|View and manage Google Drive files and folders that you have opened or created with this app|
|https://www.googleapis.com/auth/drive.readonly|View the files in your Google Drive|
|https://www.googleapis.com/auth/spreadsheets|View and manage your spreadsheets in Google Drive|
|https://www.googleapis.com/auth/spreadsheets.readonly|View your Google Spreadsheets|

To add the above settings, access the [Admin Home](https://admin.google.com/AdminHome) page and navigate to `Security` > `Advanced Settings` > `Manage API client access`.
You'll need to provide the client ID and the above URL, comma separated.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|admin_user|string|None|False|Admin user to impersonate, e.g. admin@domain.com|None|
|project_id|string|None|True|Project ID from service credentials|None|
|private_key_id|string|None|True|Private Key ID from service credentials|None|
|private_key|credential_asymmetric_key|None|True|Private Key from service credentials|None|
|client_email|string|None|True|Client email from service credentials|None|
|client_id|string|None|True|Client ID|None|
|client_x509_cert_url|string|None|True|X.509 certificate URL from service credentials|None|
|auth_uri|string|https\://accounts.google.com/o/oauth2/auth|True|OAuth2 auth URI|None|
|token_uri|string|https\://accounts.google.com/o/oauth2/token|True|OAuth2 token URI|None|
|auth_provider_x509_cert_url|string|https\://www.googleapis.com/oauth2/v1/certs|True|OAuth2 auth provider X.509 certificate URL|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

### Connection

Please make sure [Google Sheets API](https://console.developers.google.com/apis/library/sheets.googleapis.com) is enabled for the project.
To access a spreadsheet it must first be shared with the `client_email`, or the admin user must have access to the spreadsheet.

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Update connection and troubleshooting documentation
* 1.1.0 - New action Spread List to Sheet
* 1.1.1 - Fix typo in plugin spec

## Workflows

Examples:

* Update a cell in a specified Google Sheet

## References

* [Google Sheets API](https://developers.google.com/sheets/api/)
* [gspread](https://github.com/burnash/gspread)
