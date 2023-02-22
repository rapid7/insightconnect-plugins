# Description

[Nmap](https://nmap.org) ("Network Mapper") is an open source tool for network exploration and security auditing.
Determine available hosts, their services, and other details of devices on the network.
The Nmap plugin runs `nmap` directly and returns the results.

# Key Features

* Network Audit
* Network Discovery

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Scan

This action is used to run an Nmap scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|arguments|string|None|False|Arguments to supply to the Nmap command|None|-A|
|hosts|string|None|True|Host(s) to scan in Nmap-allowed formats|None|examplehost|
|ports|string|None|False|Port(s) to scan in Nmap-allowed formats|None|8080|
|sudo|boolean|False|True|Whether or not to use superuser privileges for scan|None|True|

Example input:

```
{
  "arguments": "-A",
  "hosts": "examplehost",
  "ports": "8080",
  "sudo": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]host|False|Scan results|

Example output:

```

{
  "result": [
    {
      "hostnames": [
        {}
      ],
      "addresses": {
        "ipv4": "192.168.1.100"
      },
      "vendor": {},
      "status": {
        "state": "up",
        "reason": "echo-reply"
      },
      "portused": [
        {
          "state": "closed",
          "proto": "tcp",
          "portid": "27"
        }
      ],
      "osmatch": [
        {
          "name": "Apple AirPort Extreme WAP",
          "accuracy": "98",
          "line": "3160",
          "osclass": [
            {
              "type": "WAP",
              "vendor": "Apple",
              "osfamily": "embedded",
              "accuracy": "98",
              "cpe": [
                "cpe:/h:apple:airport_extreme"
              ]
            }
          ]
        }
      ]
    }
  ]
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.4 - Action - Scan: Fix validation error for returned results. Changed array to object
* 1.0.3 - Scan: Fixed issue where `sudo` == True caused an error | Fixed issue where inputting 'nmap_args' as an empty string caused an error
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Support web server mode
* 1.0.0 - Overhaul with additional inputs and typed output
* 0.2.0 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Nmap](https://nmap.org/)

