# Description

Protect your Microsoft Office 365 and G-Suite environments with next-generation email security that uses the most advanced AI detection techniques to stop targeted phishing attacks

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
|api_key|credential_secret_key|None|True|Abnormal Security API Key|None|Vud5CDO9ULIV3SJOcp|
|hostname|string|https://api.abnormalplatform.com|True|Abnormal Security host url|None|https://api.abnormalplatform.com|

Example input:

```
```

## Technical Details

### Actions

#### Get Threats

This action is used to get a list of up to 100 threats identified in the Abnormal Security Threat Log.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|from_date|string|None|False|This input enables you to filter your results from a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-01T21:11:38Z|
|to_date|string|None|False|This input enables you to filter your results to a certain date, the date has to be in ISO 8601 format - YYYY-MM-DDTHH:MM:SSZ|None|2021-03-11T21:11:38Z|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threats|[]threat|True|List of threats found|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### threat

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Threat ID|string|False|Threat ID|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Abnormal Security](LINK TO PRODUCT/VENDOR WEBSITE)
