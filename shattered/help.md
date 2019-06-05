
# SHAttered

## About

[SHAterred](http://shattered.io) is an SHA-1 collision checking service and attack knowledge website.
The SHAttered plugin submits a file to SHAttered.io for analysis.

## Actions

### Check Collision

This action is used to check for a SHA-1 hash collision for a submitted file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|False|File to check for a collision|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|has_collision|boolean|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Hash collision detection

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode

## References

* [SHAttered](http://shattered.io/)
