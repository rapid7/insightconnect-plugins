# Description

This plugin utilizes Cisco Firepower to add scan results from a CSV file

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Documentation
## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|key|bytes|None|False|SSH key from firepower in base64|None|None|
|server|string|None|False|Enter the address for the server|None|None|
|username_password|credential_username_password|None|False|Username and password used to ssh into the Firepower server|None|None|

Example input:

```
```
## Technical Details

### Actions

#### Import CSV

This action is used to import a base64 encoded csv of vulnerabilities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|csv|bytes|None|True|CSV of vulnerabilities|None|ABCDE1234ASDF1234ASDF1234ASDF1234ASDF1234ASDF1234|

Example input:

```
{
  "csv": "ABCDE1234ASDF1234ASDF1234ASDF1234ASDF1234ASDF1234"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|False|Results from the import utility on the Firepower server|
|success|boolean|True|Was import successful|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._
## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Firepower](LINK TO PRODUCT/VENDOR WEBSITE)
