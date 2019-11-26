# Description

[Google Sheets](https://www.google.com/sheets/about/) is used to create, edit and collaborate with others on spreadsheets.

This plugin utilizes the [Google Sheets API](https://developers.google.com/sheets/api/) and [Gspread library](https://github.com/burnash/gspread/).

# Key Features

* Update cells

# Requirements

* A JWT with Google Sheets permissions
* The Google Sheets API must be enabled

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|admin_user|string|None|False|Admin user to impersonate, e.g. admin@domain.com|None|
|auth_provider_x509_cert_url|string|https://www.googleapis.com/oauth2/v1/certs|True|OAuth2 auth provider X.509 certificate URL|None|
|auth_uri|string|https://accounts.google.com/o/oauth2/auth|True|OAuth2 auth URI|None|
|client_email|string|None|True|Client email from service credentials|None|
|client_id|string|None|True|Client ID|None|
|client_x509_cert_url|string|None|True|X.509 certificate URL from service credentials|None|
|private_key|credential_asymmetric_key|None|True|Private Key from service credentials|None|
|private_key_id|string|None|True|Private Key ID from service credentials|None|
|project_id|string|None|True|Project ID from service credentials|None|
|token_uri|string|https://accounts.google.com/o/oauth2/token|True|OAuth2 token URI|None|

## Technical Details

### Actions

#### Update Cell

This action is used to update a specified cell in Google Sheets with new data.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sheet_id|string|None|True|The ID of the spreadsheet to update|None|
|cell|string|None|True|The cell to update e.g. A1, B6, C55, etc|None|
|update|string|None|True|The data to update the cell with|None|
|worksheet|string|None|True|The worksheet to update e.g. Sheet1|None|

##### Output

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

#### Spread List to Sheet

This action is used to given a starting cell, this action will take a list of data and push it to either rows or columns in a google sheet.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sheet_id|string|None|True|The ID of the spreadsheet to update|None|
|cell|string|None|True|The target cell to being placing data e.g. A1, B6, C55, etc|None|
|direction|string|None|True|The direction to fill in data e.g. row or column|['row', 'column']|
|update_list|[]string|None|True|The data to update the cell with|None|
|worksheet|string|None|True|The worksheet to update e.g. Sheet1|None|

##### Output

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

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.1.2 - New spec and help.md format for the Hub
* 1.1.1 - Fix typo in plugin spec
* 1.1.0 - New action Spread List to Sheet
* 1.0.1 - Update connection and troubleshooting documentation
* 1.0.0 - Initial plugin

# Links

## References

* [Google Sheets API](https://developers.google.com/sheets/api/)
* [gspread](https://github.com/burnash/gspread)

