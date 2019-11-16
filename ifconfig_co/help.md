# Description

[ifconfig.co](https://ifconfig.co/) is a free IP address lookup API.

# Key Features

* Network Address Translation
* IP details

# Requirements

_This plugin does not contain any requirements_

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Check Ports

This action is used to check for a given TCP port on your public facing IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|port|integer|None|True|TCP Port to Check|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|False|None|
|port|integer|False|None|
|address|string|False|None|

Example output:

```

{
  "reachable": false,
  "port": 8080,
  "address": "208.118.227.1"
}

```

#### Lookup IP Address

This action is used to retrieve your public facing IP address.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|city|string|False|None|
|address_decimal|integer|False|None|
|hostname|string|False|None|
|address|string|False|None|
|country|string|False|None|

Example output:

```

{
  "city": "Brighton",
  "country_iso": "US",
  "ip_decimal": 3497452289,
  "country": "United States",
  "hostname": "208.118.227.1.rapid7.com",
  "address": "208.118.227.1"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Convert to Python 3
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Rename "Lookup Your IP Address" action to "Lookup IP Address" | Rename "Check Your Ports" action to "Check Ports"
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [ifconfig.co](https://ifconfig.co/)

