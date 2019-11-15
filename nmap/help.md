# Description

[Nmap](https://nmap.org) ("Network Mapper") is an open source tool for network exploration and security auditing.
The Nmap plugin runs Nmap directly and returns the results.

# Key Features

* Network Audit
* Network Discovery

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Scan

This action is used to run an Nmap scan.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sudo|boolean|False|True|Whether or not to use superuser privileges for scan|None|
|hosts|string|None|True|Host(s) to scan in Nmap-allowed formats|None|
|ports|string|None|False|Port(s) to scan in Nmap-allowed formats|None|
|arguments|string|None|False|Arguments to supply to the Nmap command, Nmap <arguments>|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]hosts|False|Scan results|

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

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - Support web server mode
* 1.0.0 - Overhaul with additional inputs and typed output
* 0.2.0 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Nmap](https://nmap.org/)

