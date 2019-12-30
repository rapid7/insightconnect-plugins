# Description

[CloudShark](https://www.cloudshark.org/) is an on-premises platform for packet analysis.
Users can upload and manage capture files using the CloudShark plugin for Rapid7 InsightConnect. Use CloudShark to
assist with alert investigations, internal penetration testing, and more.

# Key Features

* Capture file management
* View capture file metadata

# Requirements

* API Key

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
|avg_packet_rate|string|False|Average packet rate|
|avg_packet_size|string|False|Average packet size|
|cap_file_id|integer|False|Capture file ID|
|comments|string|False|Comments|
|created_at|date|False|Created at|
|data_bit_rate|string|False|Data bit rate|
|data_byte_rate|string|False|Data byte rate|
|data_size|integer|False|Data size|
|duration|string|False|Duration|
|encapsulation|string|False|Encapsulation|
|end_time|date|False|End time|
|file|string|False|File|
|file_source|string|False|File source|
|file_type|string|False|File type|
|filename|string|False|Filename|
|group|string|False|Group|
|group_write|boolean|False|Group write|
|id|string|False|Cloudshark ID|
|last_accessed|date|False|Last accessed|
|num_packets|integer|False|Number of packets|
|public|boolean|False|Public|
|size|integer|False|Size|
|start_time|string|False|Start time|
|tag_list|string|False|Tag list|
|truncated|string|False|Truncated|
|user|string|False|User|
|viewcount|integer|False|View count|

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
|filename|string|False|Filename|
|id|string|False|Cloudshark ID|

#### Download

This action is used to download a capture file by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cid|string|None|True|Cloud Shark ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|capture_file|bytes|False|Capture file|
|status|integer|False|HTTP status|

#### Upload URL

This action is used to upload capture file by URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comments|string|None|False|File comments|None|
|filename|string|None|False|Resulting filename|None|
|tags|string|None|False|Comma-separated list of tags|None|
|url|string|None|True|URL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|exceptions|[]string|False|Exceptions|
|filename|string|False|Filename|
|id|string|False|Cloud Shark ID|
|status|integer|False|HTTP Status|

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cid|string|None|True|Cloud Shark ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|avg_packet_rate|string|False|Average packet rate|
|avg_packet_size|string|False|Average packet size|
|cap_file_id|integer|False|Capture file ID|
|comments|string|False|Comments|
|created_at|date|False|Created at|
|data_bit_rate|string|False|Data bit rate|
|data_byte_rate|string|False|Data byte rate|
|data_size|integer|False|Data size|
|duration|string|False|Duration|
|encapsulation|string|False|Encapsulation|
|end_time|date|False|End time|
|file|string|False|File|
|file_source|string|False|File source|
|file_type|string|False|File type|
|filename|string|False|Filename|
|group|string|False|Group|
|group_write|boolean|False|Group write|
|id|string|False|Cloudshark ID|
|last_accessed|date|False|Last accessed|
|num_packets|integer|False|Number of packets|
|public|boolean|False|Public|
|size|integer|False|Size|
|start_time|string|False|Start time|
|tag_list|string|False|Tag list|
|truncated|string|False|Truncated|
|user|string|False|User|
|viewcount|integer|False|View count|

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
|id|string|False|Cloudshark ID|
|message|string|False|Message|
|status|integer|False|HTTP status|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The API token provided in the CloudShark free trial doesn't contain sufficient privileges to utilize this plugin.
For uploads, make sure that a supported [capture file format](https://wiki.wireshark.org/FileFormatReference) is passed as input.

# Version History

* 2.0.0 - Add missing title values for actions in plugin.spec.yaml
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [CloudShark](https://www.cloudshark.org/)
* [CloudShark API](https://support.cloudshark.org/api/)
* [Capture File Formats](https://wiki.wireshark.org/FileFormatReference)

