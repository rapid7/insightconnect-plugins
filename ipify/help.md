# Description

[Ipify](https://www.ipify.org/) is a free IP address lookup service.

# Key Features

* IP Lookup of a Domain

# Requirements

_This plugin does not contain any requirements_

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Address Lookup

This action is used to lookup the public IP address of an Insight Orchestrator host.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address|string|False|Public IP address of Insight Orchestrator host|

Example output:

```

{
  "address": "208.118.227.1"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.2 - Change docker image from `komand/python-2-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Move test from actions to connection | Use output constants
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [IPify](https://www.ipify.org/)

