
# UUID

## About

[UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) standards for Universally Unique Identifier (ID).
It's a way to generate a value which is gauranteed to be unique.

It's also referred to as a GUID (Global Unique Identifier), however strictly speaking a GUID is
the name for the Microsoft implementation of the UUID spec. That said, they are both identical in
nature and purpose.

## Actions

### UUIDv4

This action is used to a generate 1 UUID Version 4.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|uuid|string|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This action requires no inputs, and the UUID is generated per the V4 specification.
Please contact komand to report any issues with the plugin.

## Workflows

Examples:

* Data format

## Versions

* 0.1.0 - Initial plugin
* 1.0.0 - Update to v2 architecture | Support web server mode | Semver compliance
* 1.0.1 - Updating to Go SDK 2.6.4
* 1.0.2 - Regenerate with latest Go SDK to solve bug with triggers
* 1.0.3 - Add `utilities` plugin tag for Marketplace searchability

## References

* [UUID Spec](https://www.ietf.org/rfc/rfc4122.txt)
