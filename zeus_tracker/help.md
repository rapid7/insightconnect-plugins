# Description

This plugin uses the API of the [Abuse.ch ZeuS Tracker](https://zeustracker.abuse.ch/)
which tracks ZeuS Command & Control servers (hosts) around the world.

# Key Features

* Obtain and look up ZeuS indicators

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|server|string|https://zeustracker.abuse.ch|True|ZeuS Tracker API Server|None|

## Technical Details

### Actions

#### Host Feed

This action is used to look up ZeuS hosts by hostname.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|False|Host to search for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|
|last_updated|date|False|None|
|binary_urls|[]binary_url|False|ZeuS binary URLs on this C&C|
|ip|string|False|None|
|uptime|string|False|None|
|host|string|False|None|
|last_checked|date|False|None|
|date_added|date|False|None|
|sbl|string|False|Spamhaus Block List number|
|malware|string|False|None|
|level|integer|False|None|
|nameservers|[]string|False|None|
|country|string|False|None|
|drop_urls|[]drop_url|False|ZeuS drop URLs on this C&C|
|fake_urls|[]fake_url|False|ZeuS fake URLs on this C&C|
|registrar|string|False|None|
|domain_history|[]domain_history|False|None|
|found|boolean|False|None|
|config_urls|[]config_url|False|ZeuS config URLs on this C&C|
|as_name|string|False|Autonomous system name|
|as_num|string|False|Autonomous system number|

#### Dropzones Feed

This action is used to get information on ZeuS dropzone URLs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|limit|integer|None|False|Limit number of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]default|False|None|

#### Country Feed

This action is used to look up ZeuS hosts in a specific country.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|country|string|None|False|Two character country code (see ISO column of https://countrycode.org)|None|
|limit|integer|None|False|Limit number of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]detailed|False|None|

#### Configs Feed

This action is used to get information on ZeuS config URLs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|limit|integer|None|False|Limit number of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]default|False|None|

#### Binaries Feed

This action is used to get information on ZeuS binary URLs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|limit|integer|None|False|Limit number of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]default|False|None|

#### IP Address

This action is used to look up ZeuS hosts by IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip|string|None|False|IP address to search for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip|string|False|None|
|num_hosts|integer|False|Number of ZeuS hosts|
|host|string|False|None|
|sbl|string|False|Spamhaus Block List number|
|zeus_hosts|[]hosts|False|List of hosts on this IP address|
|found|boolean|True|None|
|country|string|False|None|
|as_name|string|False|Autonomous system name|
|active_files|integer|False|Number of active files|
|as_num|string|False|Autonomous system number|

#### ASN Feed

This action is used to look up ZeuS hosts in a specific Autonomous System (AS).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|as|string|None|False|Autonomous System Number|None|
|limit|integer|None|False|Limit number of results|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]detailed|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Rename "Host" action to "Host Feed"
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Abuse.ch ZeuS Tracker](https://zeustracker.abuse.ch/)

