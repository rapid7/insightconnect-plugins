# Description

[Palo Alto Wildfire](https://www.paloaltonetworks.com/products/secure-the-network/wildfire) is a cloud-based malware sandboxing service that integrates with Palo Alto firewalls to identify unknown threats. This plugin utilizes the [Pyldfire library](https://pypi.python.org/pypi/pyldfire/7.1.3) to get vulnerability information and analyze malware samples.

# Key Features

* Submit files and URLs for malware analysis to identify unknown threats
* Get reports, verdicts, and files to assess a given sample
* Query packet capture data for a given hash and platform to search for a sample

# Requirements

* Palo Alto Wildfire host IP address or URL
* Palo Alto Wildefire API key

# Supported Product Versions

* WildFire 8.0

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Wildfire API Key, available at https://wildfire.paloaltonetworks.com/wildfire/account or on your appliance|None|5df698b6778e586b704460731b921e52|
|host|string|wildfire.paloaltonetworks.com|True|Palo Alto Wildfire host in cloud or on-premise, e.g. wildfire.paloaltonetworks.com or 10.3.4.50|None|wildfire.paloaltonetworks.com|
|proxy|object|None|False|An optional dictionary containing proxy data, with HTTPS as the key, and the proxy path as the value|None|{ "https": "https://proxy.example.com" }|
|verify|boolean|True|True|Verify the certificate|None|True|

Example input:

```
{
   "api_key":{
      "secretKey": "5df698b6778e586b704460731b921e52"
   },
   "host": "wildfire.paloaltonetworks.com",
   "proxy": {
      "https": "https://proxy.example.com"
   },
   "verify": true
}
```

## Technical Details

### Actions

#### Submit File from URL

This action is used to submit a file for analysis via a URL.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|URL to submit. The URL must contain the file name, for example http://paloaltonetworks.com/folder1/my-file.pdf|None|http://paloaltonetworks.com/folder1/my-file.pdf|

Example input:

```
{
  "url": "http://paloaltonetworks.com/folder1/my-file.pdf"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submission|filedata|False|Submission|
|verdict|string|False|One of the following verdicts: Benign, Malware, Greyware, Pending, Error, or Not found|

Example output:

```
{
  "submission": {
    "filename": "setup.exe",
    "filetype": "exe",
    "md5": "602a171cd840cb0e05cbf2a263aeb708",
    "sha256": "d0fc660de9dbc33c56e2f8cd5a79290290851cded319f953cf78b469dbd6da6d",
    "url": "http://art-archiv.ru/images/animated-number/docum-arhiv.exe"
  }
}
```

#### Get Malware Test File

This action is used to get a unique, benign malware test file that will trigger.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|file|bytes|True|Benign malware test file|

Example output:

```
{
  "file": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA..."
}
```

#### Get PCAP

This action is used to query for a PCAP.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|9de5069c5afe602b2ea0a04b66beb2c0|
|platform|string|None|True|Target analysis environment|['Windows XP, Adobe Reader 9.3.3, Office 2003', 'Windows XP, Adobe Reader 9.4.0, Flash 10, Office 2007', 'Windows XP, Adobe Reader 11, Flash 11, Office 2010', 'Windows 7 32-bit, Adobe Reader 11, Flash 11, Office 2010', 'Windows 7 64bit, Adobe Reader 11, Flash 11, Office 2010', 'Android 2.3, API 10, avd2.3.1', 'Mac OS X Mountain Lion']|Windows XP, Adobe Reader 11, Flash 11, Office 2010|

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

Example output:

```
{
  "file": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA..."
}
```

#### Get Sample

This action is used to query for a sample file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|9de5069c5afe602b2ea0a04b66beb2c0|

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

Example output:

```
{
  "file": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA..."
}
```

#### Submit URL

This action is used to submit a URL for analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|URL to submit|None|https://example.com|

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

Example output:

```
{
  "submission": {
    "md5": "602a171cd840cb0e05cbf2a263aeb708",
    "sha256": "d0fc660de9dbc33c56e2f8cd5a79290290851cded319f953cf78b469dbd6da6d",
    "url": "http://art-archiv.ru/images/animated-number/docum-arhiv.exe"
  }
}
```

#### Get Report

This action is used to query for an XML or PDF report for a particular sample.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|format|string|None|True|Report format: PDF or XML|['pdf', 'xml']|pdf|
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "format": "pdf",
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|bytes|True|Report|

Example output:

```
{
  "report": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA..."
}
```

#### Submit File

This action is used to submit a file for analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|bytes|None|True|File to submit. Supported types are Email-link, Flash, APK, PDF, JAR, PE, MS-Office|None|TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAA...|
|filename|string|None|False|Optional file name|None|ImportantCompanyFinancialReport.pdf|

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
|submission|filedata|False|Submission|
|verdict|string|False|One of the following verdicts: Benign, Malware, Greyware, Pending, Error, or Not found|

Example output:

```
{
  "submission": {
    "filename": "setup.exe",
    "filetype": "PE32 executable",
    "md5": "65da6f5b6ae29b3485b4bdabd01d1cf9",
    "sha256": "93b9b7b85c8cd0de0710fe0331b1939d6bdebba206cc49cccda40ce40ddaec33",
    "size": "285696",
    "supported_file_type": true
  }
}
```

#### Get Verdict

This action is used to query for a file's classification.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|verdict|string|True|One of the following verdicts: Benign, Malware, Greyware, Pending, Error, or Not found|

Example output:

```
{
  "verdict": "Malware"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Moved communication with API to separate class | Add logic for validation if submitted file is already in API DB | Add validation for submitting only supported by API file types | Refactor unit tests for Submit File action | Add unit test for Submit File From URL action
* 1.2.0 - Added connection test
* 1.1.2 - Fix bug where output doesn't match schema in Get Verdict action | Add improved error messaging in Submit URL action | Add example inputs
* 1.1.1 - New spec and help.md format for the Extension Library
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
