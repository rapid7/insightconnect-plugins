# Description

[Networktotal](https://www.networktotal.com/) is a free service that analyzes PCAP files and facilitates the quick detection of viruses, worms, trojans, and all kinds of malware detected by Intrusion Detection Engines and their rulesets.
The Networktotal plugin allows you to submit files and perform searches against on the public service.

# Key Features

* Send PCAP for analysis

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Search

This action is used to search PCAPs by a MD5 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|md5|string|None|False|MD5 hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|signatures|[]string|False|Signatures found|

#### Upload

This action is used to upload a PCAP file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pcap|bytes|None|False|Base64-encoded PCAP file|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|signatures|[]string|False|Signatures found|
|md5|string|False|MD5 hash of PCAP file|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0. - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [NetworkTotal](https://www.networktotal.com/)

