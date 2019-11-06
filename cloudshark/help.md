# Description

[Cloudshark](https://www.cloudshark.org/) is a cloud packet analysis and sharing product based on tshark.
This plugin implements most of the CloudShark API calls.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

A CloudShark API token is required to authenticate to the API. The default domain is `https://www.cloudshark.org`.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API Key|None|

## Technical Details

### Actions

#### Info

This action is used to obtain metadata from a capture file by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cid|string|None|True|Cloud Shark ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file_source|string|False|None|
|num_packets|integer|False|None|
|viewcount|integer|False|None|
|truncated|string|False|None|
|cap_file_id|integer|False|None|
|start_time|string|False|None|
|last_accessed|date|False|None|
|data_bit_rate|string|False|None|
|user|string|False|None|
|file|string|False|None|
|duration|string|False|None|
|encapsulation|string|False|None|
|group_write|boolean|False|None|
|id|string|False|None|
|avg_packet_size|string|False|None|
|size|integer|False|None|
|group|string|False|None|
|avg_packet_rate|string|False|None|
|created_at|date|False|None|
|comments|string|False|None|
|filename|string|False|None|
|file_type|string|False|None|
|data_size|integer|False|None|
|data_byte_rate|string|False|None|
|tag_list|string|False|None|
|public|boolean|False|None|
|end_time|date|False|None|

#### Merge

This action is used merge multiple captures files by id into one larger capture file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|duplicates|string|None|False|Duplicate packets|['remove', 'keep']|
|cids|string|None|True|Comma-separated list of Cloud Shark IDs|None|
|tags|string|None|False|Comma-separated list of tags|None|
|filename|string|None|False|Resulting filename|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|None|
|filename|string|False|None|

#### Download

This action is used to download a capture file by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cid|string|None|True|Cloud Shark ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|None|
|capture_file|bytes|False|None|

#### Upload URL

This action is used upload a capture file by URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Url|None|
|tags|string|None|False|Comma-separated list of tags|None|
|comments|string|None|False|File comments|None|
|filename|string|None|False|Resulting filename|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|HTTP Status|
|exceptions|[]string|False|Exceptions|
|id|string|False|Cloud Shark ID|
|filename|string|False|Filename|

#### Upload

This action is used to upload capture file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tags|string|None|False|Comma-separated list of tags|None|
|file|bytes|None|True|Base64 encoded capture file|None|
|comments|string|None|False|File comments|None|
|filename|string|None|False|Resulting filename|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|HTTP Status|
|exceptions|[]string|False|Exceptions|
|id|string|False|Cloud Shark ID|
|filename|string|False|Filename|

#### Delete

This action is used to delete capture file by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cid|string|None|True|Cloud Shark ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|None|
|message|string|False|None|
|id|string|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The API token provided in the CloudShark free trial doesn't contain sufficient privileges to utilize this plugin.
For uploads, make sure that a supported [capture file format](https://wiki.wireshark.org/FileFormatReference) is passed as input.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [CloudShark](https://www.cloudshark.org/)
* [CloudShark API](https://support.cloudshark.org/api/)
* [Capture File Formats](https://wiki.wireshark.org/FileFormatReference)

