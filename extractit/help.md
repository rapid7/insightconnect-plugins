
# ExtractIt

## About

The ExtractIt plugin is a collection of data extractors.

## Actions

### MAC Extractor

This action is used to extracts all mac addresses from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|mac_addrs|[]string|False|List of extracted MAC Addresses|

### MD5 Hash Extractor

This action is used to extracts all md5 hashes from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|md5|[]string|False|List of extracted MD5 Hashes|

### IOC Extractor

This action is used to extracts all indicators of compromise from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|iocs|[]string|False|List of extracted Indicators of Compromise|

### Domain Extractor

This action is used to extracts all domain names from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|
|subdomain|bool|None|True|Include subdomain in result|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|[]string|False|List of extracted Domain names|

### SHA1 Hash Extractor

This action is used to extracts all sha1 hashes from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha1|[]string|False|List of extracted SHA1 Hashes|

### File Path Extractor

This action is used to extracts all file paths from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filepaths|[]string|False|List of extracted file paths|

### SHA512 Hash Extractor

This action is used to extracts all sha512 hashes from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha512|[]string|False|List of extracted SHA512 Hashes|

### SHA256 Hash Extractor

This action is used to extracts all sha256 hashes from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sha256|[]string|False|List of extracted SHA256 Hashes|

### Date Extractor

This action is used to extracts all dates from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dates|[]date|False|List of extracted Dates|

### Email Extractor

This action is used to extracts all email addresses from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|emails|[]string|False|List of extracted Email Addresses|

### IP Extractor

This action is used to extracts all ipv4 and ipv6 addresses from a string or file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip_addrs|[]string|False|List of extracted IP Addresses|

### URL Extractor

This action is used to extract URL's from a string or file.

If you need more advanced regular expression support to match URL schemes, use the URL Extractor plugin.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|str|string|None|False|Input string|None|
|file|bytes|None|False|Input file as bytes|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|urls|[]string|False|List of extracted URLs|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Extract URLs for analysis

## Versions

* 0.1.0 - Initial plugin
* 1.0.0 - Domain Extractor bugfix
* 1.0.1 - Bugfix Email Extractor
* 1.1.0 - Port to V2 architecture | Support web server mode | MD5 matching bugfix
* 1.1.1 - Fix issue where test method for Domain Extractor was not properly testing the action
* 1.1.2 - Updating to Go SDK 2.6.4
* 1.1.3 - Regenerate with latest Go SDK to solve bug with triggers
* 1.1.4 - Fix issue where URL Extractor would return IPs
* 1.1.5 - Fix issue where URL Extractor parsing was missing URLs
* 1.1.6 - Fix issue where IP Extractor would return inaccurate IPs

## References

* None
