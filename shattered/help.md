# Description

[SHAtterred](http://shattered.io) is a free service for checking SHA-1 hash collisions. Using the SHAttered plugin for
Rapid7 InsightConnect, users can quickly determine if a file is part of a collision attack. SHAttered can assist
with forensics, phishing analysis, and other needs.

# Key Features

* SHA-1 collision checking

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Check Collision

This action is used to check for a SHA-1 hash collision for a submitted file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|True|File to check for a collision|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|has_collision|boolean|False|Has collision|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.2 - Fix issue in spec description
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [SHAttered](http://shattered.io/)

