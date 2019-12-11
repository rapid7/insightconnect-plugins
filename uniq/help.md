# Description

The Uniq plugin is an implementation of the classic [uniq](https://linux.die.net/man/1/uniq) unix tool.
It filters out repeated lines or items from supplied input, returning only different values. It's great for
removing duplicate IP addresses, domains, etc. from an array.

# Key Features

* Data deduplication

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Deduplicate Integer Array

This action is used to remove duplicate items from an array of integers.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|data|[]integer|None|True|Array of integers|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|duplicate_count|integer|False|Count of duplicates removed|
|result|[]integer|False|Result without duplicates|
|element_count|object|False|Count of each element|

#### Deduplicate String Array

This action is used to remove duplicate items from an array of strings.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|data|[]string|None|True|Array of strings|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|duplicate_count|integer|False|Count of duplicates removed|
|result|[]string|False|Result without duplicates|
|element_count|object|False|Count of each element|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.3 - Spec description update
* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Update plugin tag from `utility` to `utilities` for Marketplace searchability
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Uniq](https://example.co://linux.die.net/man/1/uniq)

