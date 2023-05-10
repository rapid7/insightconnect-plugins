# Description

[Networktotal](https://www.networktotal.com/) is a free service that analyzes PCAP files and facilitates the quick
detection of viruses, worms, trojans, and all kinds of malware detected by Intrusion Detection Engines and their
rulesets. The Networktotal plugin submits files and perform searches against on the public service.

# Key Features

* Send PCAP for analysis

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions

* NGINX 2023-05-10

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Search

This action is used to search PCAPs by a MD5 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|md5|string|None|False|MD5 hash|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "md5": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|signatures|[]string|False|Signatures found|[]|

Example output:

```
[
  "signature 1",
  "signature 2"
]
```

#### Upload

This action is used to upload a PCAP file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|pcap|bytes|None|False|Base64-encoded PCAP file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|

Example input:

```
{
  "pcap": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|md5|string|False|MD5 hash of PCAP file|9de5069c5afe602b2ea0a04b66beb2c0|
|signatures|[]string|False|Signatures found|[]|

Example output:

```
{
  "md5":"9de5069c5afe602b2ea0a04b66beb2c0",
  "signatures":[
    "signature 1",
    "signature 2"
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

* 1.0.2 - Updated requests to version 2.20.0
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [NetworkTotal Docs](http://nginx.org/en/docs/)

## References

* [NetworkTotal](https://www.networktotal.com/)

