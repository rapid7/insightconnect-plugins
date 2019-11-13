# Description

[Microsoft ATP Safe Links](https://docs.microsoft.com/en-us/office365/securitycompliance/atp-safe-links) is a service that helps protect your organization by providing time-of-click verification of web addresses (URLs) in email messages and Office documents.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Decode Safe Links

This action is used to decode a Microsoft Safe Link.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Safe Link to be decoded|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|True|Result of the decoded Safe Link|

Example output:

```
{
  "result":"https://aomediacodec.github.io/av1-spec/av1-spec.pdf"
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - Fixed issue where non-safelinks returned a blank string
* 1.0.0 - Initial plugin

# Links

## References

* [Microsoft ATP Safe Links](https://docs.microsoft.com/en-us/office365/securitycompliance/atp-safe-links)

