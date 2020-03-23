# Description

[Microsoft Office 365 ATP Safe Links](https://docs.microsoft.com/en-us/office365/securitycompliance/atp-safe-links) is a part of Microsoft's Advance Threat Protection (ATP) that provides time-of-click verification of web addresses (URLs) in email messages and Office documents. This plugin uses the [Office 365 API](https://docs.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema) to decode an encoded Microsoft ATP Safe Link.

# Key Features

* Decode an encoded Microsoft ATP Safe Link in order to blacklist the URL, search logs for other visits to the URL, and use the URL in incident response procedures.

# Requirements

* Encoded Microsoft ATP Safe Link

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Decode Safe Links

This action decodes a Microsoft Safe Link.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Safe Link to be decoded|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decoded|boolean|True|Whether or not we were able to decode the URL|
|result|string|True|Result of the decoded Safe Link|

Example output:

```
{
  "result": "https://aomediacodec.github.io/av1-spec/av1-spec.pdf"
}
```

#### Decode Safe Links

This action is used to decode a Microsoft Safe Link.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Safe Link to be decoded|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.3 - Fixed issue where embedded URLs returned blank string
* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Fixed issue where non-safelinks returned a blank string
* 1.0.0 - Initial plugin

# Links

## References

* [Microsoft ATP Safe Links](https://docs.microsoft.com/en-us/office365/securitycompliance/atp-safe-links)

