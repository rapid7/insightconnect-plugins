
# URL Extractor

## About

The URL Extractor plugin extracts URls from a body of text using regular expressions.

## Actions

### Parse URLs

This action is used to parse URLs from given text.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|text|string|None|False|Text to parse|None|
|scheme|string|[a-zA-Z][a-zA-Z.\-+]*://|False|Regular expression to match URL scheme|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|urls|[]string|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 0.1.0 - Initial plugin
* 0.2.0 - Provides an optional "scheme" field for more specific URL extraction
* 1.0.0 - Update to v2 architecture | Support web server mode | Semver compliance
* 1.0.1 - Updating to Go SDK 2.6.4
* 1.0.2 - Regenerate with latest Go SDK to solve bug with triggers

## Workflows

Examples:

* [Security Mailbox Triage](https://market.komand.com/workflows/komand/security-mailbox-triage/1.0.0)
* Phishing investigation
* Data extraction

## References

* [Komand](https://www.komand.com/)
