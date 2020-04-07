# Description

The Black Hole Router plugin is use to assist with managing networks blocked within Black Hole Router site.

# Key Features

* Identify suspicious network activity
* Network segment isolation
* Block network traffic

# Requirements

* Requires the URL of an accessible instance of the Black Hole Router and an API token.

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ssl_no_verify|boolean|None|True|SSL No Verify|None|
|token|credential_token|None|True|API Token and URL to BHR Host E.g. http://bhr.company.com:8000|None|

## Technical Details

### Actions

#### Unblock Address

This action is used to send an unblock request for an IP address or CIDR block.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cidr|string|None|True|IP Address or CIDR network to block|None|
|why|string|None|True|The reason for the unblock|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|False|None|

#### Block Stats

This action is used to retrieve the current block statistics.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|current|integer|False|None|
|expected|integer|False|None|
|block_pending|integer|False|None|
|unblock_pending|integer|False|None|

#### Mblock

This action is used to send a batch of IP addresses as an `array` of block request `objects`.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|batch|[]object|None|True|A list of block objects E.g. [ { "cidr": "1.1.1.1", ..}, { "cidr": "1.2.3.4",..} ]|None|

The following parameters can be used in each `object`:

* CIDR - IP address or CIDR network to block
* Source - Name of source for the block i.e., where the intel came from
* Why - The reason for the block e.g., SSH scanning
* Duration - The duration of the block expressed in seconds, or with available suffixes are `y`, `mo`, `d`, `h`, `m`, `s`, e.g. 1d for one day
* Autoscale - Autoscale the duration based on server side block history
* Skip Whitelist - Bypass the server side whitelist

For example, 3 block requests would be specified like the following:

```

[
  { "cidr": "1.1.1.1", "duration": 30, "source": "ssh", "why": "scanning" },
  { "cidr": "1.1.1.2", "duration": 30, "source": "ssh", "why": "scanning" },
  { "cidr": "1.1.1.3", "duration": 30, "source": "ssh", "why": "scanning" },
]

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]object|False|None|

#### Query Block History

This action is used to query the block history for an IP address or CIDR block.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cidr|string|None|True|IP Address or CIDR network to block|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|is_blocked|boolean|False|None|
|result|[]object|False|None|

#### Block Address

This action is used to send a block request for an IP address or CIDR block.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|Source for this block i.e., where the intel came from|None|
|autoscale|boolean|None|False|Autoscale the duration based on server side block history|None|
|skip_whitelist|boolean|None|False|Bypass the server side whitelist|None|
|duration|string|300|False|Duration of block in seconds. Accepted suffixes are y, mo, d, h, m, s, e.g. 1d|None|
|cidr|string|None|True|IP Address or CIDR network to block|None|
|why|string|None|True|The reason for the block|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|object|False|None|

#### List Blocks

This action is used to retrieve a list of current blocks.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|string|False|None|

#### Batch Address Block

This action is used to send a batch block request.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|batch|[]object|None|True|A list of block objects E.g. [ { "cidr": "1.1.1.1", ..}, { "cidr": "1.2.3.4",..} ]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]object|False|Block Information|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin currently doesn't support the ident parameter which would allow blocks across multiple backend systems.

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Black Hole Router Site](https://github.com/ncsa/bhr-site)
* [BHR Client](https://github.com/ncsa/bhr-client)
* [BHR Client Docs](https://bhr-client.readthedocs.io)

