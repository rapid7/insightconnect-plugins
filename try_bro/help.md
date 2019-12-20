# Description

With the [Try Bro](http://try.bro.org/) plugin for Rapid7 InsightConnect, users can use a free instance of the
Bro Network Security Monitor in the cloud. Users can upload PCAP files for analysis and get Bro logs.

# Key Features

* PCAP analysis
* Get Bro logs

# Requirements

* Try Bro server URL

# Documentation

## Setup

This plugin requires a Try Bro URL. By default, the public service is used.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|server|string|http://try.bro.org|True|Try Bro URL|None|

## Technical Details

### Actions

#### Get Bro Logs

This action is used to retrieve Bro logs from an analysis by its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|job|string|None|False|Job Number|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|files|False|Bro Log Files|

#### Upload PCAP

This action is used to upload a user supplied PCAP and optional Bro scripts for analysis by Bro.
The analysis URL and ID is returned.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pcap|bytes|None|True|Base64 encoded PCAP file|None|
|scripts|[]bytes|None|False|Base64 encoded Bro Scripts|None|
|version|string|master|False|Bro Version|['master', '1.5', '2.1', '2.2', '2.3.1', '2.3.2', '2.4', '2.4.1', '2.5', '2.5.1']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|Job ID|
|url|string|False|URL|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Fix issue where run action was excluded from plugin on build
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Try Bro](http://try.bro.org/)
* [Try Bro Code](https://github.com/bro/try-bro)

