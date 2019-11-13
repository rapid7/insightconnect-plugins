# Description

The [Snort Labs IP Reputation](http://blog.snort.org/2015/09/ip-blacklist-feed-has-moved-locations.html) list is a IP intelligence list.
This plugin allows you to query the list for an IP address.

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

#### IP Lookup

This action is used to look up a given IP address in the intel feed and return whether is was found.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IPv4 Address|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|
|found|boolean|False|None|
|status|string|False|None|
|address|string|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - Feed URL [http://www.talosintelligence.com/feeds/ip-filter.blf](http://www.talosintelligence.com/feeds/ip-filter.blf) moved to S3, redirect required
* 0.1.0 - Initial plugin

# Links

## References

* [Snort Labs IP Reputation](http://blog.snort.org/2015/09/ip-blacklist-feed-has-moved-locations.html)

