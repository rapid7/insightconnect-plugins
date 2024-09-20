# Description

The Get URL plugin allows you to download files from a URL. Supported protocols are HTTP, HTTPS, and FTP. This plugin's cache is enabled across workflows to store previously downloaded files to reduce future web requests. To reduce the number of subsequent requests the Etag and If-Modified-Since fields are also checked

# Key Features

* Get the contents of a web page
* Check a web page for changes

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* _There are no supported product versions listed._

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Get URL

This action is used to download the contents of a URL

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|checksum|string|None|False|Checksum verification (MD5, SHA1, SHA256)|None|0800fc577294c34e0b28ad2839435945|None|None|
|is_verify|boolean|True|True|Validate certificate|None|True|None|None|
|timeout|integer|60|False|Timeout in seconds|None|60|None|None|
|url|string|None|True|URL to Download|None|https://example.com|None|None|
|user_agent|string|Mozilla/5.0|False|Send requests with user agent|None|Mozilla/5.0|None|None|
  
Example input:

```
{
  "checksum": "0800fc577294c34e0b28ad2839435945",
  "is_verify": true,
  "timeout": 60,
  "url": "https://example.com",
  "user_agent": "Mozilla/5.0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|bytes|bytes|False|Bytes|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
|status_code|integer|False|Status code|200|
  
Example output:

```
{
  "bytes": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "status_code": 200
}
```
### Triggers


#### Poll URL

This trigger is used to monitor the contents of a URL for changes. The contents are returned when a change has been 
detected

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|is_verify|boolean|True|True|Validate certificate|None|True|None|None|
|poll|integer|60|False|Poll in seconds|None|60|None|None|
|url|string|None|True|URL to Download|None|https://example.com|None|None|
|user_agent|string|Mozilla/5.0|False|Send requests with user agent|None|Mozilla/5.0|None|None|
  
Example input:

```
{
  "is_verify": true,
  "poll": 60,
  "url": "https://example.com",
  "user_agent": "Mozilla/5.0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|bytes|bytes|False|Bytes|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
|status_code|integer|False|Status code|200|
  
Example output:

```
{
  "bytes": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "status_code": 200
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.1.0 - Fix issue with getting the same URL multiple times | Refresh with latest SDK (6.1.2)
* 2.0.1 - Fix file decoding error after file download | Update SDK to version 4 | Update unit tests after changing SDK version
* 2.0.0 - Use input and output constants | Add example inputs | Changed `Exception` to `PluginException` | Added 'f' strings | Move test from actions to connection | Change in return `file` key to `bytes` | Add new input User Agent to Get File action and Poll URL trigger
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Get URL](https://github.com/rapid7/insightconnect-plugins/tree/master/plugins/get_url)

## References
  
*This plugin does not contain any references.*