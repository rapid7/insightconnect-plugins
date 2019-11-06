# Description

[Networktotal](https://www.networktotal.com/) is a free service that analyzes pcap files and facilitates the quick detection of viruses, worms, trojans, and all kinds of malware detected by Intrusion Detection Engines and their rulesets.
The Networktotal plugin allows you to submit files and perform searches against on the public service.

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

* 1.0.0. - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [NetworkTotal](https://www.networktotal.com/)

