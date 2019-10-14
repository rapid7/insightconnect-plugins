
# Cacador

## About

[Cacador](https://github.com/sroberts/cacador) (Portuguese for hunter) is tool for extracting common indicators
of compromise from a block of text.

## Actions

### Extract

This action will allow you to extract potential IOCs from some text.
These include items like hashes, network domains, emails, files, etc.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|text|string|None|False|Text to extract IOCs|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|files|files|False|File IOCS|
|hashes|hashes|False|None|
|time|string|False|Time of extraction|
|utilities|utilities|False|Other IOCs|
|networks|networks|False|Network IOCS|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* [IOC Extraction](https://market.komand.com/snippets/komand/ioc-extraction/0.1.0)

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - Support web server mode | Port to Go SDK 2
* 1.1.1 - Updating to Go SDK 2.6.4
* 1.1.2 - Regenerate with latest Go SDK to solve bug with triggers

## References

* [Cacador](https://github.com/sroberts/cacador)
