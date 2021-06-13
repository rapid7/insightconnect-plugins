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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|access_key|credential_secret_key|None|True|Access Key ID|None|
|secret_key|credential_secret_key|None|True|Secret access key|None|

## Technical Details

### Actions

#### Mount Drive

This action is used to mount a drive for analysis

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|directory|string|None|True|Directory|None|
|device|string|None|True|Device|None|
|filesystem_type|string|None|True|Filesystem Type|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|instance_id|string|None|True|Instance ID|None|
|region|string|None|True|Region|None|
|private_key|string|None|True|Private Key|None|
|user|string|None|True|User Name|None|
|directory|string|False|Directory|
|status|string|False|Status|

#### Clam AV

This action is used to scan a directory with ClamAV. This action requires the host to have clamav installed.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|instance_id|string|None|True|Instance ID|None|
|region|string|None|True|Region|None|
|private_key|string|None|True|Private Key|None|
|user|string|None|True|User Name|None|
|directory|string|None|True|Directory|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_name|string|False|File Name|
|file_location|string|False|File Location|
|hash_value|string|False|Hash Value|
|owner|string|False|Owner|
|time_created|string|False|Time Created|

### Triggers

This plugin does not contain any triggers.

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

