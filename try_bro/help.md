
# Try Bro

## About

[Try Bro](http://try.bro.org/) is a free service that runs the Bro Network Security Monitor in the cloud.

## Actions

### Get Bro Logs

This action is used to retrieve Bro logs from an analysis by its ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|job|string|None|False|Job Number|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|files|False|None|

### Upload PCAP

This action is used to upload a user supplied PCAP and optional Bro scripts for analysis by Bro.
The analysis URL and ID is returned.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|version|string|None|False|None|['master', '1.5', '2.1', '2.2', '2.3.1', '2.3.2', '2.4', '2.4.1']|
|pcap|bytes|None|True|Base64 encoded PCAP file|None|
|scripts|[]bytes|None|False|Base64 encoded Bro Scripts|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|
|id|string|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin requires a Try Bro URL. By default, the public service is used.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|server|string|http\://try.bro.org|True|Try Bro URL|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Packet analysis

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.1 - Fix issue where run action was excluded from plugin on build

## References

* [Try Bro](http://try.bro.org/)
* [Try Bro Code](https://github.com/bro/try-bro)
