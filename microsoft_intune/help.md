# Description

Integrate Microsoft Intune into your workflow

# Key Features

* Initiate a Windows Defender Antivirus scan on a machine.

# Requirements

* Azure credentials
* Client ID, Client Secret and Tenant ID

# Documentation
## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|string|None|True|Client ID, also called Application ID|None|aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa|
|client_secret|string|None|True|Client secret key|None|kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=|
|credentials|credential_username_password|None|True|E-mail address and password|None|{"username": "user@example.com", "password": "mypassword"}|
|tenant_id|string|None|True|Tenant ID can be found in Active Directory|None|aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa|
|url|string|None|True|Base URL for the Microsoft endpoint|None|https://example.com|

Example input:

```
{
  "client_id": "aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa",
  "client_secret": "kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=",
  "credentials": {
    "username": "user@example.com",
    "password": "mypassword"
  },
  "tenant_id": "aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa",
  "url": "https://example.com"
}
```
## Technical Details

### Actions

#### Antivirus Scan

This action is used to initiate a Windows Defender Antivirus scan on a machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device|string|None|True|Search devices by either of - device name, user ID, email address, device ID|None|aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa|
|update|boolean|False|False|If true the action with update Antivirus Signatures before scan|None|True|

Example input:

```
{
  "device": "aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa",
  "update": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if scan was initiated successfully|

Example output:

```
{
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin creation, action Antivirus Scan added

# Links

## References

* [Microsoft Intune](https://docs.microsoft.com/en-us/graph/)
