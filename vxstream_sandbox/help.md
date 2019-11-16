# Description

[VxStream Sandbox](https://www.payload-security.com/products/vxstream-sandbox) is an innovative and fully automated malware analysis system
that includes the unique Hybrid Analysis technology. Our plugin connects to your VxStream instance. In addition, it supports the free and public [Hybrid Analysis](https://www.hybrid-analysis.com/) API.

# Key Features

* Search by file Hash
* Submit file for analysis
* Get file analysis report details

# Requirements

* VxStream API Key
* VxStream API Secret
* VxStream server address

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_secret|credential_secret_key|None|True|API secret|None|
|api_key|credential_secret_key|None|True|API key|None|
|server|string|https\://www.hybrid-analysis.com/api|True|VxStream Sandbox API Server URL|None|

## Technical Details

### Actions

#### Search Database

This action is used to search the database using the [query syntax](https://www.hybrid-analysis.com/faq).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|False|Search parameters; syntax available at https\://www.hybrid-analysis.com/faq|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Number of results returned|
|query|string|False|None|
|response_code|integer|True|None|
|results|[]result|False|None|

Example output:

```

{
  "count": 1,
  "query": "filetype:exe",
  "response_code": 0,
  "results": [
    {
      "threatscore": 99,
      "avdetect": 63,
      "environmentId": "100",
      "vxfamily": "Trojan.Generic",
      "submitname": "file",
      "sha256": "93b9b7b85c8cd0de0710fe0331b1939d6bdebba206cc49cccda40ce40ddaec33",
      "start_time": "2017-12-20T20:44:47+01:00",
      "size": 285696,
      "verdict": "Unknown",
      "type_short": "exe",
      "environmentDescription": "Windows 7 32 bit"
    }
  ]
}

```

#### Lookup by Hash

This action is used to get summary information for a given hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|False|MD5/SHA1/SHA256 hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Number of reports returned|
|response_code|integer|True|None|
|reports|[]report|False|None|

Example output:

```

{
  "count": 1,
  "response_code": 0,
  "reports": [
    {
      "threatlevel": 2,
      "environmentDescription": "Windows 7 32 bit",
      "size": 285696,
      "classification_tags": [],
      "isinteresting": false,
      "hosts": [],
      "environmentId": "100",
      "total_signatures": 14,
      "vxfamily": "Trojan.Generic",
      "domains": [],
      "avdetect": "63",
      "md5": "65da6f5b6ae29b3485b4bdabd01d1cf9",
      "total_processes": 1,
      "isurlanalysis": false,
      "sha1": "a67f7c65c8ac1788a41be05f39d083ff532811a5",
      "targeturl": "",
      "analysis_start_time": "2017-12-20T20:44:47+01:00",
      "type": "PE32 executable (GUI) Intel 80386, for MS Windows",
      "submitname": "file",
      "threatscore": 99,
      "sha256": "93b9b7b85c8cd0de0710fe0331b1939d6bdebba206cc49cccda40ce40ddaec33",
      "verdict": "Unknown",
      "total_network_connections": 0
    }
  ]
}

```

#### Submit File

This action is used to submit file for analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|customcmdline|string|None|False|Custom Command Line, e.g. /VX\:promptfill mypassword|None|
|scriptlogging|boolean|True|False|Enable the script logging feature. This feature can give deeper insights into the functionality of Javascripts, VBA macros and similar script languages (see 'Script calls' in the per process details)|None|
|filename|string|None|False|Optional filename of the malware|None|
|promptfill_password|string|None|False|Optional malware password to pass in to the analysis (shortcut for /VX\:promptfill)|None|
|file|bytes|None|True|File to be analyzed. See https\://vxstream-sandbox.com/faq for supported filetypes|None|
|env_id|integer|100|False|Environment ID|None|
|hybridanalysis|boolean|True|False|Enable a unique process memory inspection. This feature may slow down the overall analysis, but improves behavior analysis through instruction level inspection regardless of execution|None|
|experimentalantievasion|boolean|True|False|Enable experimental anti-evasion features. This feature can have an impact application execution, but at the same time can improve performance for very evasive malware|None|

##### Output

|submission_url|string|False|None|
|response_code|integer|True|None|
|hash|string|False|SHA256 Hash|

Example output:

```

{
  "hash": "93b9b7b85c8cd0de0710fe0331b1939d6bdebba206cc49cccda40ce40ddaec33",
  "submission_url": "https://demo15.vxstream-sandbox.com/sample/93b9b7b85c8cd0de0710fe0331b1939d6bdebba206cc49cccda40ce40ddaec33",
  "response_code": 0
}

```

#### Retrieve Report

This action is used to retrieve report by providing SHA256 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|env_id|string|None|False|Environment ID|None|
|hash|string|None|False|SHA256 Hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|response_code|integer|False|None|
|state|string|False|None|
|analysis|analysis|False|None|

Example output:

```

{
  "found": false,
  "response_code": 0,
  "state": "IN_QUEUE"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Support web server mode | Update to new credential types | Rename "Lookup By Hash" to "Lookup by Hash"
* 1.0.1 - Update to v2 Python plugin architecture, edit to input parsing for lookup, report, and query actions
* 1.0.0 - Invalid key in types section of plugin specification, and style updates
* 0.2.3 - SSL bug fix in SDK
* 0.2.1 - Schema fixes for Search Database and Lookup by Hash actions to allow use in UI by name
* 0.2.0 - Update schema types for Lookup by Hash and Submit actions
* 0.1.0 - Initial plugin

# Links

## References

* [VxStream Sandbox](https://www.payload-security.com/products/vxstream-sandbox)
* [Hybrid Analysis](https://www.hybrid-analysis.com/)
* [Hybrid Analysis Query Syntax](https://www.hybrid-analysis.com/faq)

