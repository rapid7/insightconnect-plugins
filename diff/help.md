
# Diff

## About

The Diff plugin allows you to find the difference between strings.
Results persist across runs of workflows (using the unique label).

## Actions

### Diff

This action is used to `diff` strings.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|compare|string|None|True|New data, for comparison against the old data|None|
|label|string|None|True|Unique label to store the old data|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|diff|string|False|Diff string|
|different|boolean|False|True if different|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Data comparison

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.1 - Update plugin tag `utility` to `utilities` for Marketplace searchability

## References

* None
