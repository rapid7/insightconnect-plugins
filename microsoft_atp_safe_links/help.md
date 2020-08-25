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

This action is used to decode a Microsoft Safe Link.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|Safe Link to be decoded|None|https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Faomediacodec.github.io%2Fav1-spec%2Fav1-spec.pdf&data=04%7C01%7Cgfrost%40microsoft.com%7Cc01143f4353e426231d508d590e3a9c1%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C1%7C636574229902920663%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwifQ%3D%3D%7C-1&sdata=lLQibtMygoLH30UNXZcUZGAA1i%2FqNE%2Ff6fgotaX3uhI%3D&reserved=0|

Example input:

```
{
  "url": "https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Faomediacodec.github.io%2Fav1-spec%2Fav1-spec.pdf&data=04%7C01%7Cgfrost%40microsoft.com%7Cc01143f4353e426231d508d590e3a9c1%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C1%7C636574229902920663%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwifQ%3D%3D%7C-1&sdata=lLQibtMygoLH30UNXZcUZGAA1i%2FqNE%2Ff6fgotaX3uhI%3D&reserved=0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decoded|boolean|True|Whether or not we were able to decode the URL|
|result|string|True|Result of the decoded Safe Link|

Example output:

```
{
  "decoded": true,
  "result": "https://aomediacodec.github.io/av1-spec/av1-spec.pdf"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.1.2 - Update to use the `insightconnect-python-3-38-slim-plugin:4` Docker image | Update plugin.spec.yaml to include `cloud_ready`
* 1.1.1 - Fix issue where `decoded` output wasn't returned
* 1.1.0 - Fixed issue where embedded URLs returned blank string
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Fixed issue where non-safelinks returned a blank string
* 1.0.0 - Initial plugin

# Links

## References

* [Microsoft ATP Safe Links](https://docs.microsoft.com/en-us/office365/securitycompliance/atp-safe-links)
