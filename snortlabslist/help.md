
# Snort Labs IP Reputation

## About

The [Snort Labs IP Reputation](http://blog.snort.org/2015/09/ip-blacklist-feed-has-moved-locations.html) list is a IP intelligence list.
This plugin allows you to query the list for an IP address.

## Actions

### IP Lookup

This action is used to look up a given IP address in the intel feed and return whether is was found.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IPv4 Address|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|
|found|boolean|False|None|
|status|string|False|None|
|address|string|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - Feed URL [http://www.talosintelligence.com/feeds/ip-filter.blf](http://www.talosintelligence.com/feeds/ip-filter.blf) moved to S3, redirect required
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode

## Workflows

Examples:

* Intelligence

## References

* [Snort Labs IP Reputation](http://blog.snort.org/2015/09/ip-blacklist-feed-has-moved-locations.html)
