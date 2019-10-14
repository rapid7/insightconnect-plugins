
# IDNA

## About

IDNA handles converting between ASCII (punycode) and unicode domain names.

## Actions

### To ASCII

This action is used to convert a unicode domain name to ASCII (punycode).

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Unicode domain name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain|string|True|ASCII (punycode) domain name|

### To Unicode

This action is used to convert an ASCII (punycode) domain to unicode.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|ASCII (punycode) domain name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain|string|True|Unicode domain name|

## Triggers

There are no triggers associated with this plugin.

## Connection

There is no connection associated with this plugin.

## Workflows

Examples:

*  Punycode transformation

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - Support web server mode
* 1.1.2 - Regenerate with latest Go SDK to solve bug with triggers

## Troubleshooting

This plugin does not contain any troubleshooting information.

## References

* [Unicode IDN Utility](http://unicode.org/cldr/utility/idna.jsp)
* [Go IDNA Package](https://godoc.org/golang.org/x/net/idna)
