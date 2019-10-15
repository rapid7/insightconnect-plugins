
# Palo Alto Wildfire

## About

[Palo Alto Wildfire](https://www.paloaltonetworks.com/products/secure-the-network/subscriptions/wildfire) is a  cloud-based threat analysis service is the industry's most advanced analysis and prevention engine for highly evasive zero-day exploits and malware.
This plugin utilizes the [Pyldfire library](https://pypi.python.org/pypi/pyldfire/7.1.3).

## Actions

### Submit File from URL

This action is used to submit a file for analysis via a URL.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to submit. The URL must contain the file name, for example http\://paloaltonetworks.com/folder1/my-file.pdf|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submission|filedata|True|None|

### Get Malware Test File

This action is used to get a unique, benign malware test file that will trigger.

#### Input

This action does not contain any inputs.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|Benign malware test file|

### Get PCAP

This action is used to query for a PCAP.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|platform|string|None|True|Target analysis environment|['Windows XP, Adobe Reader 9.3.3, Office 2003', 'Windows XP, Adobe Reader 9.4.0, Flash 10, Office 2007', 'Windows XP, Adobe Reader 11, Flash 11, Office 2010', u'Windows 7 32\u2010bit, Adobe Reader 11, Flash 11, Office 2010', 'Windows 7 64bit, Adobe Reader 11, Flash 11, Office 2010', 'Android 2.3, API 10, avd2.3.1', 'Mac OS X Mountain Lion']|
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|None|

### Get Sample

This action is used to query for a sample file.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|None|

### Submit URL

This action is used to submit a URL for analysis.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to submit|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submission|urldata|True|None|

### Get Report

This action is used to query for an XML or PDF report for a particular sample.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|
|format|string|None|True|Report format\: PDF or XML|['pdf', 'xml']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|bytes|True|None|

### Submit File

This action is used to submit a file for analysis.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|bytes|None|True|File to submit. Supported types are Email-link, Flash, APK, PDF, JAR, PE, MS-Office|None|
|filename|string|None|False|Optional file name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submission|filedata|True|None|

### Get Verdict

This action is used to query for a file's classification.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|verdict|string|True|One of the following verdicts\: 'Benign', 'Malware', 'Greyware', 'Pending', 'Error', or 'Not found`|

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|verify|boolean|True|True|Verify the certificate|None|
|host|string|wildfire.paloaltonetworks.com|True|Palo Alto Wildfire host in cloud or on-premise, e.g. wildfire.paloaltonetworks.com or 10.3.4.50|None|
|api_key|password|None|True|Wildfire API Key, available at https\://wildfire.paloaltonetworks.com/wildfire/account or on your appliance|None|
|proxy|object|None|False|An optional dictionary containing proxy data, with HTTPS as the key, and the proxy path as the value|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Threat intelligence
* Malware analysis

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types | Rename "Submit a File" action to "Submit File" | Rename "Submit File From URL" action to "Submit File from URL" | Rename "Submit a URL" action to "Submit URL"
* 1.0.1 - Fix plugin description
* 1.0.2 - Fixed issue where connection was not passing the API key properly
* 1.1.0 - Fixed issue where unsupported file types failed | Update to add `supported_file` to filedata type

## References

* [Palo Alto Wildfire](https://www.paloaltonetworks.com/products/secure-the-network/subscriptions/wildfire)
* [Wildfire Documentation](https://www.paloaltonetworks.com/documentation/80/wildfire)
* [pyldfire](https://pypi.python.org/pypi/pyldfire/7.1.3)

## Custom Output Types

### filedata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filename|string|False|None|
|filetype|string|False|None|
|md5|string|True|MD5 hash of file|
|sha256|string|True|SHA256 hash of file|
|size|string|True|File size|
|supported_file_type|boolean|True|Boolean indicating whether the filetype of the sample is supported|
|url|string|False|None|

### urldata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|md5|string|True|MD5 hash of file|
|sha256|string|True|SHA256 hash of file|
|url|string|True|None|
