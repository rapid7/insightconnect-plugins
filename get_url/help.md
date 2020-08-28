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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|URL to Download|None|https://example.com|
|checksum|string|None|False|Checksum verification (MD5, SHA1, SHA256)|None|0800fc577294c34e0b28ad2839435945|
|is_verify|boolean|True|True|Validate certificate|None|True|
|timeout|integer|60|False|Timeout in seconds|None|60|
|user_agent|string|Mozilla/5.0|False|Send requests with user agent|None|Mozilla/5.0|

Example input:

```
{
  "is_verify": false,
  "timeout": 60,
  "url": "https://httpbin.org/base64/a29tYW5kIHRlc3Q%3D"
}
```

##### Output

This action returns the contents of the URL and an HTTP status code.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bytes|bytes|False|Bytes|
|status_code|integer|False|Status code|

Example output:

```
{
  "bytes": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "status_code": 200
}
```

### Triggers

#### Poll URL

This trigger is used to monitor the contents of a URL for changes. The contents are returned when a change has been detected.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|URL to Download|None|https://example.com|
|poll|integer|60|False|Poll in seconds|None|60|
|is_verify|boolean|True|True|Validate certificate|None|True|
|user_agent|string|Mozilla/5.0|False|Send requests with user agent|None|Mozilla/5.0|

Example input:

```
{
  "is_verify": true,
  "poll": 60,
  "url": "https://httpbin.org/base64/a29tYW5kIHRlc3Q%3D"
}
```

##### Output

This action returns the contents of the URL and an HTTP status code.

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bytes|bytes|False|Bytes|
|status_code|integer|False|Status code|

Example output:

```
{
  "bytes": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "status_code": 200
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Some web servers do not support cache control mechanisms, or do not use them properly.

# Version History

* 2.0.0 - Use input and output constants | Add example inputs | Changed `Exception` to `PluginException` | Added "f" strings | Move test from actions to connection | Change in return `file` key to `bytes` | Add new input User Agent to Get File action and Poll URL trigger
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

_This plugin does not contain any references._
