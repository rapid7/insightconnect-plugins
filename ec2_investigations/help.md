# Description

The EC2 Investigation plugin runs security tools on AWS instances.
In many cases, actions require the security tool to be installed on the EC2 host.

Using the EC2 Investigations plugin for Rapid7 InsightConnect will allow users to mount drives and scan
directories with ClamAV.

# Key Features

* Mount drives
* Scan directories with ClamAV

# Requirements

* Access key
* Secret key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access_key|credential_secret_key|None|True|Access Key ID|None|None|
|secret_key|credential_secret_key|None|True|Secret access key|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Mount Drive

This action is used to mount a drive for analysis

#### Clam AV

This action is used to scan a directory with ClamAV. This action requires the host to have clamAV installed.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device|string|None|True|Device|None|None|
|directory|string|None|True|Directory|None|None|
|instance_id|string|None|True|Instance ID|None|None|
|private_key|string|None|True|Private key|None|None|
|region|string|None|True|Region|None|None|
|user|string|None|True|User name|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|directory|string|False|Directory|
|status|string|False|Status|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

In many cases, actions require the security tool to be installed on the EC2 host.
For example, the ClamAV action requires ClamAV to be installed on the destination EC2 host.

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

[Boto](http://boto.cloudhackers.com/en/latest/ref/manage.html)
[ClamAV](https://www.clamav.net/)

