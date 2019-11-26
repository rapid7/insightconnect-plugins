# Description

[mxtoolbox_dns](https://www.mxtoolbox.com) is a Interface with MxToolBox DNS lookup API
This plugin utilizes the [mxtoolbox_dns API](https//api.mxtoolbox.com).

# Key Features

* Blacklist checking for domains

# Requirements

* API Key
* MxToolBox server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|https\://api.mxtoolbox.com/api/v1/|True|MxToolBox DNS Lookup|None|
|api_key|credential_secret_key|None|False|API access key|None|

## Technical Details

### Actions

#### A

This action is used to check DNS A records for the provided host name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|A_Output|True|None|

#### SOA

This action is used to get start of authority records for a domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|SOA_Output|True|None|

#### MX

This action is used to check DNS MX records for a domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|MX_Output|True|None|

#### Blacklist

This action is used to check for a host's presence on a list of known bad actors.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|BLACKLIST_Output|True|None|

#### DNS

This action is used to run a standard DNS query.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|DNS_Output|True|None|

#### Usage

This action is used to check your usage of the mxtoolbox api.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|USAGE_Output|True|None|

#### TXT

This action is used to check txt records on a domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|TXT_Output|True|None|

#### PTR

This action is used to check DNS ptr records for an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip_address|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|PTR_Output|True|None|

#### SPF

This action is used to check spf records on a domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hostname|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|SPF_Output|True|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

If MxToolBox returns a key with a `null` value e.g. `"DnsServiceProvider": null`, the key will removed by the plugin and not returned to the user.
The [templating](https://docs.komand.com/docs/input-templating) and [query language](https://docs.komand.com/docs/query-language) can be used to
test for the existence of a value if it's needed later in the workflow.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Example](https://example.com)
* [Example API](http://docs.example.com)

