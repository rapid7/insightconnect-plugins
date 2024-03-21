# Description

[Snort Labs List](http://talosintel.com/feeds/ip-filter.blf) is an IP blacklist provided by Snort.
Users of this plugin can query it with an IP address to check the status, assisting with alert enrichment and
other threat intelligence needs.

# Key Features

* IP address blacklist query

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
* 2021-17-08

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### IP Lookup
  
This action is used to look up a given IP address in the intel feed and return whether is was found.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IPv4 Address|None|198.51.100.0|
  
Example input:

```
{
  "address": "198.51.100.0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address|string|False|IP address that was found|198.51.100.0|
|found|boolean|False|Found status|True|
|status|string|False|Error message|No Error|
|url|string|False|URL of reputation list|www.example.com|
  
Example output:

```
{
  "address": "198.51.100.0",
  "found": true,
  "status": "No Error",
  "url": "www.example.com"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 1.0.3 - Updated SDK to the latest version | Added unittests
* 1.0.2 - Update requests to version 2.20.0
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - Feed URL [http://www.talosintelligence.com/feeds/ip-filter.blf](http://www.talosintelligence.com/feeds/ip-filter.blf) moved to S3, redirect required
* 0.1.0 - Initial plugin

# Links

* [Snort](https://www.snort.org/)

## References

* [Snort Labs IP Reputation](http://blog.snort.org/2015/09/ip-blacklist-feed-has-moved-locations.html)

