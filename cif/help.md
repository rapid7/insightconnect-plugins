# Description

This plugin is used to manage an instance of Collective Intelligence Framework service.

# Key Features

* Query observables

# Requirements

* Requires self hosted CIF service
* Requires an API Key from the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|CIF URL e.g. https\://cif.example.com|None|
|ssl_verify|boolean|True|True|SSL certificate verification|None|
|api_key|credential_secret_key|None|True|CIF API key|None|

## Technical Details

### Actions

#### Query

This action is used to query for observables.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|observable|string|None|False|The observable to query for|None|
|confidence|integer|65|True|Minimum confidence level to return e.g. 65|None|
|protocol|string|None|False|Layer 4 protocol (icmp, tcp, udp)|['all', 'icmp', 'tcp', 'udp']|
|tags|string|None|False|The tag(s) to filter on e.g. tags=botnet,zeus|None|
|cc|string|None|False|The country code to filter on e.g. us|None|
|portlist|string|None|False|List of ports (ex\: 1,2,445-557)|None|
|nolog|boolean|None|True|Whether CIF should log the query|None|
|otype|string|None|True|Type of observable|['all', 'ipv4', 'ipv6', 'fqdn', 'url', 'email']|
|limit|integer|10|True|Limit number of results|None|
|provider|string|None|False|The provider(s) to filter on e.g. dragonresearchgroup.com|None|
|q|string|None|False|The observable to query for|None|
|itypes|string||False|Itypes|['ipv4', 'ipv6', 'fqdn', 'url', 'email', 'md5', 'sha1', 'sha256']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|query|[]result|False|None|

#### Ping

This action is used to ping the router.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timestamp|[]integer|True|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Update to new credential types
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Added support for itypes
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Collective Intelligence Framework](http://csirtgadgets.org/collective-intelligence-framework)
* [CIF API](https://github.com/csirtgadgets/massive-octo-spice/wiki/API)

