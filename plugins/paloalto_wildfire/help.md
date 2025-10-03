# Description

Perform malware analysis with Palo Alto Wildfire

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

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Wildfire API Key, available at https://wildfire.paloaltonetworks.com/wildfire/account or on your appliance|None|5df698b6778e586b704460731b921e52|None|None|
|host|string|wildfire.paloaltonetworks.com|True|Palo Alto Wildfire host in cloud or on-premise, e.g. wildfire.paloaltonetworks.com or 10.3.4.50|None|wildfire.paloaltonetworks.com|None|None|
|proxy|object|None|False|An optional dictionary containing proxy data, with HTTPS as the key, and the proxy path as the value|None|{ "https": "https://proxy.example.com" }|None|None|
|verify|boolean|True|True|Verify the certificate|None|True|None|None|

Example input:

```
{
  "api_key": "5df698b6778e586b704460731b921e52",
  "host": "wildfire.paloaltonetworks.com",
  "proxy": {
    "https": "https://proxy.example.com"
  },
  "verify": true
}
```

## Technical Details

### Actions


#### Get Malware Test File

This action is used to gets a unique, benign malware test file that will trigger

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file|bytes|True|Benign malware test file|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|
  
Example output:

```
{
  "file": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA..."
}
```

#### Get PCAP

This action is used to query for a PCAP

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|platform|string|None|True|Target analysis environment|["Windows XP, Adobe Reader 9.3.3, Office 2003", "Windows XP, Adobe Reader 9.4.0, Flash 10, Office 2007", "Windows XP, Adobe Reader 11, Flash 11, Office 2010", "Windows 7 32-bit, Adobe Reader 11, Flash 11, Office 2010", "Windows 7 64bit, Adobe Reader 11, Flash 11, Office 2010", "Android 2.3, API 10, avd2.3.1", "Mac OS X Mountain Lion"]|Windows XP, Adobe Reader 11, Flash 11, Office 2010|None|None|
  
Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0",
  "platform": "Windows XP, Adobe Reader 11, Flash 11, Office 2010"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file|bytes|True|File|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|
  
Example output:

```
{
  "file": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA..."
}
```

#### Get Report

This action is used to query for an XML or PDF report for a particular sample

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|format|string|None|True|Report format: PDF or XML|["pdf", "xml"]|pdf|None|None|
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "format": "pdf",
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|report|bytes|True|Report|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|
  
Example output:

```
{
  "report": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA..."
}
```

#### Get Sample

This action is used to query for a sample file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file|bytes|True|File|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|
  
Example output:

```
{
  "file": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA..."
}
```

#### Get Verdict

This action is used to query for a files classification

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hash|string|None|True|The MD5 or SHA-256 hash value of the sample|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|verdict|string|True|One of the following verdicts: Benign, Malware, Greyware, Pending, Error, or Not found|Malware|
  
Example output:

```
{
  "verdict": "Malware"
}
```

#### Submit File

This action is used to submit a file for analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file|bytes|None|True|File to submit. Supported types are Email-link, Flash, APK, PDF, JAR, PE, MS-Office|None|TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAA...|None|None|
|filename|string|None|True|File name of submitted file|None|ImportantCompanyFinancialReport.pdf|None|None|
  
Example input:

```
{
  "file": "TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAA...",
  "filename": "ImportantCompanyFinancialReport.pdf"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submission|filedata|False|Submission|{"filename": "setup.exe","filetype": "exe","md5": "602a171cd840cb0e05cbf2a263aeb708","sha256": "d0fc660de9dbc33c56e2f8cd5a79290290851cded319f953cf78b469dbd6da6d","url": "http://art-archiv.ru/images/animated-number/docum-arhiv.exe"}|
|verdict|string|False|One of the following verdicts: Benign, Malware, Greyware, Pending, Error, or Not found|Malware|
  
Example output:

```
{
  "submission": {
    "filename": "setup.exe",
    "filetype": "exe",
    "md5": "602a171cd840cb0e05cbf2a263aeb708",
    "sha256": "d0fc660de9dbc33c56e2f8cd5a79290290851cded319f953cf78b469dbd6da6d",
    "url": "http://art-archiv.ru/images/animated-number/docum-arhiv.exe"
  },
  "verdict": "Malware"
}
```

#### Submit File from URL

This action is used to submit a file for analysis via a URL

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|url|string|None|True|URL to submit. The URL must contain the file name, for example http://paloaltonetworks.com/folder1/my-file.pdf|None|http://paloaltonetworks.com/folder1/my-file.pdf|None|None|
  
Example input:

```
{
  "url": "http://paloaltonetworks.com/folder1/my-file.pdf"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submission|filedata|False|Submission|{"filename": "setup.exe","filetype": "exe","md5": "602a171cd840cb0e05cbf2a263aeb708","sha256": "d0fc660de9dbc33c56e2f8cd5a79290290851cded319f953cf78b469dbd6da6d","url": "http://art-archiv.ru/images/animated-number/docum-arhiv.exe"}|
|verdict|string|False|One of the following verdicts: Benign, Malware, Greyware, Pending, Error, or Not found|Malware|
  
Example output:

```
{
  "submission": {
    "filename": "setup.exe",
    "filetype": "exe",
    "md5": "602a171cd840cb0e05cbf2a263aeb708",
    "sha256": "d0fc660de9dbc33c56e2f8cd5a79290290851cded319f953cf78b469dbd6da6d",
    "url": "http://art-archiv.ru/images/animated-number/docum-arhiv.exe"
  },
  "verdict": "Malware"
}
```

#### Submit URL

This action is used to submit a URL for analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|url|string|None|True|URL to submit|None|https://example.com|None|None|
  
Example input:

```
{
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submission|urldata|True|Submission|{"md5": "602a171cd840cb0e05cbf2a263aeb708","sha256": "d0fc660de9dbc33c56e2f8cd5a79290290851cded319f953cf78b469dbd6da6d","url": "http://art-archiv.ru/images/animated-number/docum-arhiv.exe"}|
  
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
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**filedata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|filename|string|None|False|None|None|
|File Type|string|None|False|None|None|
|MD5|string|None|False|MD5 hash of file|None|
|SHA256|string|None|False|SHA256 hash of file|None|
|size|string|None|False|File size|None|
|Supported File|boolean|None|False|Boolean indicating whether the filetype of the sample is supported|None|
|URL|string|None|False|None|None|
  
**urldata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|MD5|string|None|False|MD5 hash of file|None|
|SHA256|string|None|False|SHA256 hash of file|None|
|URL|string|None|False|None|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.1 - Addressed snyk vulnerability | Updated SDK to the latest version (6.3.10)
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

* [Palo Alto Wildfire](https://www.paloaltonetworks.com/products/secure-the-network/wildfire)

## References

* [Palo Alto Wildfire](https://www.paloaltonetworks.com/products/secure-the-network/wildfire)
* [Wildfire Documentation](https://www.paloaltonetworks.com/documentation/80/wildfire)
* [pyldfire](https://pypi.python.org/pypi/pyldfire/7.1.3)