# Description

[Palo Alto Wildfire](https://www.paloaltonetworks.com/products/secure-the-network/wildfire) is a cloud-based malware sandboxing service that integrates with Palo Alto firewalls to identify unknown threats. This plugin utilizes the [Pyldfire library](https://pypi.python.org/pypi/pyldfire/7.1.3) to get vulnerability information and analyze malware samples.

# Key Features

* Submit files and URLs for malware analysis to identify unknown threats
* Get reports, verdicts, and files to assess a given sample
* Query packet capture data for a given hash and platform to search for a sample

# Requirements

* Palo Alto Wildfire host IP address or URL
* Palo Alto Wildefire API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Example|Enum|
|----|----|-------|--------|-----------|-------|----|
|api_key|credential_secret_key|None|True|Wildfire API Key, available at https://wildfire.paloaltonetworks.com/wildfire/account or on your appliance|None|None|
|host|string|wildfire.paloaltonetworks.com|True|Palo Alto Wildfire host in cloud or on-premise, e.g. wildfire.paloaltonetworks.com or 10.3.4.50|None|None|
|proxy|object|None|False|An optional dictionary containing proxy data, with HTTPS as the key, and the proxy path as the value|None|None|
|verify|boolean|True|True|Verify the certificate|None|None|

Example input:

```
{
  "api_key": {
    "secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"
  },
  "host": "wildfire.paloaltonetworks.com",
  "proxy": {},
  "verify": true
}
```

## Technical Details

### Actions

#### Submit File from URL

This action is used to submit a file for analysis via a URL.

##### Input

|Name|Type|Default|Required|Description|Example|Enum|
|----|----|-------|--------|-----------|-------|----|
|url|string|None|True|URL to submit. The URL must contain the file name, for example http://paloaltonetworks.com/folder1/my-file.pdf|None|None|

Example input:

```
{
  "url": "http://paloaltonetworks.com/folder1/my-file.pdf"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submission|filedata|True|Submission|

#### Get Malware Test File

This action is used to get a unique, benign malware test file that will trigger.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|Benign malware test file|

#### Get PCAP

This action is used to query for a PCAP.

##### Input

|Name|Type|Default|Required|Description|Example|Enum|
|----|----|-------|--------|-----------|-------|----|
|hash|string|None|True|The MD5 or SHA‐256 hash value of the sample|None|None|
|platform|string|None|True|Target analysis environment|None|['Windows XP, Adobe Reader 9.3.3, Office 2003', 'Windows XP, Adobe Reader 9.4.0, Flash 10, Office 2007', 'Windows XP, Adobe Reader 11, Flash 11, Office 2010', 'Windows 7 32‐bit, Adobe Reader 11, Flash 11, Office 2010', 'Windows 7 64bit, Adobe Reader 11, Flash 11, Office 2010', 'Android 2.3, API 10, avd2.3.1', 'Mac OS X Mountain Lion']|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0",
  "platform": "Windows XP, Adobe Reader 9.4.0, Flash 10, Office 2007"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|File|

#### Get Sample

This action is used to query for a sample file.

##### Input

|Name|Type|Default|Required|Description|Example|Enum|
|----|----|-------|--------|-----------|-------|----|
|hash|string|None|True|The MD5 or SHA‐256 hash value of the sample|None|None|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|File|

#### Submit URL

This action is used to submit a URL for analysis.

##### Input

|Name|Type|Default|Required|Description|Example|Enum|
|----|----|-------|--------|-----------|-------|----|
|url|string|None|True|URL to submit|None|None|

Example input:

```
{
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submission|urldata|True|Submission|

#### Get Report

This action is used to query for an XML or PDF report for a particular sample.

##### Input

|Name|Type|Default|Required|Description|Example|Enum|
|----|----|-------|--------|-----------|-------|----|
|format|string|None|True|Report format: PDF or XML|None|['pdf', 'xml']|
|hash|string|None|True|The MD5 or SHA‐256 hash value of the sample|None|None|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0",
  "format": "PDF"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|bytes|True|Report|

#### Submit File

This action is used to submit a file for analysis.

##### Input

|Name|Type|Default|Required|Description|Example|Enum|
|----|----|-------|--------|-----------|-------|----|
|file|bytes|None|True|File to submit. Supported types are Email-link, Flash, APK, PDF, JAR, PE, MS-Office|None|None|
|filename|string|None|False|Optional file name|None|None|

Example input:

```
{
  "file": "TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAA...",
  "filename": "ImportantCompanyFinancialReport.pdf"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submission|filedata|True|Submission|

#### Get Verdict

This action is used to query for a file's classification.

##### Input

|Name|Type|Default|Required|Description|Example|Enum|
|----|----|-------|--------|-----------|-------|----|
|hash|string|None|True|The MD5 or SHA‐256 hash value of the sample|None|None|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|verdict|string|True|One of the following verdicts: 'Benign', 'Malware', 'Greyware', 'Pending', 'Error', or 'Not found`|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.2 - Add example inputs
* 1.1.1 - New spec and help.md format for the Hub
* 1.1.0 - Fixed issue where unsupported file types failed | Update to add `supported_file` to filedata type
* 1.0.2 - Fixed issue where connection was not passing the API key properly
* 1.0.1 - Fix plugin description
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types | Rename "Submit a File" action to "Submit File" | Rename "Submit File From URL" action to "Submit File from URL" | Rename "Submit a URL" action to "Submit URL"
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Palo Alto Wildfire](https://www.paloaltonetworks.com/products/secure-the-network/wildfire)
* [Wildfire Documentation](https://www.paloaltonetworks.com/documentation/80/wildfire)
* [pyldfire](https://pypi.python.org/pypi/pyldfire/7.1.3)
