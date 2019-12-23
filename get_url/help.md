# Description

The Get URL plugin allows you to download files from a URL. Supported protocols are HTTP, HTTPS, and FTP.

This plugin's cache is enabled across workflows to store previously downloaded files to reduce future web requests.
To reduce the number of subsequent requests the Etag and If-Modified-Since fields are also checked.

# Key Features

* Get the contents of a web page
* Check a web page for changes

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Get URL

This action is used to download the contents of a URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to Download|None|
|checksum|string|None|False|Checksum verification (MD5, SHA1, SHA256)|None|
|is_verify|boolean|True|True|Validate certificate|None|
|timeout|integer|60|False|Timeout in seconds|None|

##### Output

This action returns the contents of the URL and an HTTP status code.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bytes|bytes|False|Bytes|
|status_code|integer|False|Status code|

### Triggers

#### Poll URL

This trigger is used to monitor the contents of a URL for changes. The contents are returned when a change has been detected.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to Download|None|
|poll|integer|60|False|Poll in seconds|None|
|is_verify|boolean|True|True|Validate certificate|None|

##### Output

This action returns the contents of the URL and an HTTP status code.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bytes|bytes|False|Bytes|
|status_code|integer|False|Status code|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Some web servers do not support cache control mechanisms, or do not use them properly.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

_This plugin does not contain any references._
