
# Proofpoint URL Defense

## About

[Proofpoint URL Defense](https://www.proofpoint.com/us) is a service designed to handle emails that contain malicious URLs.
This plugin decodes URLs that are encoded by Proofpoints URL Defense service using ppdecode.

## Actions

### URL Decode

This action is used to take a proofpoint url and decodes to the original url.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|proofpoint_url|string|None|True|Proofpoint encoded URL|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decoded_url|string|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Decode Proofpoint encoded URLs

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Bug fix with decode parsing

## References

* [Proofpoint URL Defense](https://www.proofpoint.com/us/products/targeted-attack-protection)
* [ppdecode Library](https://github.com/warquel/ppdecode)
