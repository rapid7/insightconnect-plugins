# Description

[Falcon Sandbox](https://www.crowdstrike.com/endpoint-security-products/falcon-sandbox-malware-analysis/) is an innovative and fully automated malware analysis system
that includes the unique Hybrid Analysis technology. Our plugin connects to your VxStream instance. In addition, it supports the free and public [Hybrid Analysis](https://www.hybrid-analysis.com/) API.

# Key Features

* Search by file hash
* Submit file for analysis
* Get file analysis report details

# Requirements

* Falcon Sandbox API Key
* Falcon Sandbox API Secret
* Falcon Sandbox server address

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key|None|
|api_secret|credential_secret_key|None|True|API secret|None|
|server|string|https://www.falcon-sandbox.com/api|True|Falcon Sandbox API Server URL|None|

## Technical Details

### Actions

#### Search Database

This action is used to search the database using the [query syntax](https://www.hybrid-analysis.com/faq).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|False|Search parameters; syntax available at https://www.hybrid-analysis.com/faq|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Number of results returned|
|query|string|False|Query|
|response_code|integer|True|Response code|
|results|[]result|False|List of results|

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
|hash|string|None|True|MD5/SHA1/SHA256 hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Number of reports returned|
|reports|[]report|False|Reports|
|response_code|integer|True|Response code|

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
|customcmdline|string|None|False|Custom Command Line, e.g. /VX:promptfill mypassword|None|
|env_id|integer|100|False|Environment ID|None|
|experimentalantievasion|boolean|True|False|Enable experimental anti-evasion features. This feature can have an impact application execution, but at the same time can improve performance for very evasive malware|None|
|file|bytes|None|True|File to be analyzed. See https://www.falcon-sandbox.com/faq for supported filetypes|None|
|filename|string|None|False|Optional filename of the malware|None|
|hybridanalysis|boolean|True|False|Enable a unique process memory inspection. This feature may slow down the overall analysis, but improves behavior analysis through instruction level inspection regardless of execution|None|
|promptfill_password|string|None|False|Optional malware password to pass in to the analysis (shortcut for /VX:promptfill)|None|
|scriptlogging|boolean|True|False|Enable the script logging feature. This feature can give deeper insights into the functionality of Javascripts, VBA macros and similar script languages (see 'Script calls' in the per process details)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|hash|string|False|SHA256 Hash|
|response_code|integer|True|Response code|
|submission_url|string|False|Submission URL|

##### Output

|submission_url|string|False|Submission URL|
|response_code|integer|True|Response code|
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
|analysis|analysis|False|Analysis|
|found|boolean|False|True if found|
|response_code|integer|False|Response code|
|state|string|False|State|

Example output:

```

{
  "found": false,
  "response_code": 0,
  "state": "IN_QUEUE"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### analysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Final|final|False|None|
|General|general|False|None|
|Hybrid Analysis|hybridanalysis|False|None|
|Runtime|runtime|False|None|

#### apicalls

|Name|Type|Required|Description|
|----|----|--------|-----------|
|API DB|apidb|False|None|
|Chronology|chronology|False|None|
|Parameter DB|parameterdb|False|None|

#### apidb

|Name|Type|Required|Description|
|----|----|--------|-----------|
|APICall List|[]apidb_apicall|False|None|

#### apidb_apicall

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Module|string|False|None|
|Name|string|False|None|
|SysNum|string|False|None|
|UID|string|False|None|
|VA|string|False|None|

#### app

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|None|
|Product|string|False|None|
|Version|string|False|None|

#### appinfos

|Name|Type|Required|Description|
|----|----|--------|-----------|
|App List|[]app|False|None|

#### appserver

|Name|Type|Required|Description|
|----|----|--------|-----------|
|External IP|string|False|None|

#### banner

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Architecture|string|False|None|
|Author Name|string|False|None|
|Author Version|string|False|None|
|HA Enabled|boolean|False|None|
|Tiny Tags|boolean|False|None|

#### category

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Count|string|False|None|
|Description|string|False|None|
|Order|string|False|None|
|Signature List|[]signature|False|None|

#### characteristics

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Carved Files|string|False|None|
|Runtime TargetNum|string|False|None|

#### chronology

|Name|Type|Required|Description|
|----|----|--------|-----------|
|APICall List|[]chronology_apicall|False|None|

#### chronology_apicall

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Parameters|parameters|False|None|
|Ref ID|string|False|None|
|Tick|string|False|None|
|UID|string|False|None|

#### chronology_parameter

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|None|
|Meaning|string|False|None|
|Number|string|False|None|

#### confidence

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Overall Confidence|string|False|None|
|Max Impact|string|False|None|
|ThreatSig Impact|string|False|None|

#### controller

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Architecture|string|False|None|
|Client Address|string|False|None|
|Client Architecture|string|False|None|
|Client Description|string|False|None|
|Client ID|string|False|None|
|Client Name|string|False|None|
|Client Path|string|False|None|
|Client Type|string|False|None|
|Crashfile|boolean|False|None|
|End Time|date|False|None|
|Environment ID|integer|False|None|
|Exec Options|exec_options|False|None|
|Missing KernelMode|boolean|False|None|
|Network Enabled|boolean|False|None|
|Original Name|string|False|None|
|Sniffer Enabled|boolean|False|None|
|Start Time|date|False|None|
|Total Time|integer|False|None|

#### custom_string

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Database|string|False|None|
|Delta|string|False|None|
|File Name|string|False|None|
|Origin|string|False|None|
|Signature Match|string|False|None|
|Source ID|string|False|None|
|Type|string|False|None|

#### dates

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Date (Unix)|string|False|None|
|Date (UTC)|string|False|None|
|Date (Year)|integer|False|None|
|DOS Date(Unix)|string|False|None|
|DOS Date(UTC)|string|False|None|
|DOS Date(Year)|string|False|None|

#### digests

|Name|Type|Required|Description|
|----|----|--------|-----------|
|MD5|string|False|None|
|SHA1|string|False|None|
|SHA256|string|False|None|
|SHA512|string|False|None|

#### engine

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|None|
|Total Detected|string|False|None|
|Total Scans|string|False|None|

#### engines

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Engine|engine|False|None|

#### exec_options

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Dependencies|string|False|None|
|Duration|integer|False|None|
|Allow SampleTampering|boolean|False|None|
|Experimental AntiEvasion|boolean|False|None|
|Folder Analysis|boolean|False|None|
|Script Logging|boolean|False|None|
|Static Analysis|boolean|False|None|
|Tor-Enabled Analysis|boolean|False|None|
|Mode|string|False|None|
|Netsim|integer|False|None|
|No HashLookup|boolean|False|None|
|Script|string|False|None|
|Script Description|string|False|None|
|Shared Analysis|boolean|False|None|

#### fileaccesses

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Real Total|string|False|None|

#### final

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Business Threats|string|False|None|
|Characteristics|characteristics|False|None|
|Confidence|confidence|False|None|
|Image Processing|imageprocessing|False|None|
|MultiScan|multiscan|False|None|
|Signatures|signatures|False|None|
|Signatures Chronology|string|False|None|
|Signatures Triplets|string|False|None|
|Strings|strings|False|None|
|Verdict|verdict|False|None|
|Warnings|object|False|None|
|YARA Scanner|string|False|None|

#### general

|Name|Type|Required|Description|
|----|----|--------|-----------|
|App Infos|appinfos|False|None|
|App Server|appserver|False|None|
|Banner|banner|False|None|
|Controller|controller|False|None|
|Digests|digests|False|None|
|Extra Static|string|False|None|
|Icon|bytes|False|None|
|Delayed AVScan|boolean|False|None|
|Is URLAnalysis|boolean|False|None|
|Sample|string|False|None|
|Static|static|False|None|
|TRID|trid|False|None|
|VirusTotal|virustotal|False|None|
|Windows Bitness|integer|False|None|
|Windows Edition|string|False|None|
|Windows VersionName|string|False|None|
|ServicePack Number|string|False|None|
|Spoofed Username|string|False|None|
|Windows Username|string|False|None|
|Windows Version|string|False|None|

#### handle

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Database|string|False|None|
|ID|string|False|None|
|Tick|string|False|None|
|Type|string|False|None|
|UID|string|False|None|

#### handles

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Handle List|[]handle|False|None|

#### hybrid_target

|Name|Type|Required|Description|
|----|----|--------|-----------|
|POIS|integer|False|None|
|Shellcodes|string|False|None|
|Streams|string|False|None|
|UID|string|False|None|

#### hybrid_targets

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Target|hybrid_target|False|None|

#### hybridanalysis

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Banner|banner|False|None|
|Sample|sample|False|None|
|Targets|hybrid_targets|False|None|

#### image

|Name|Type|Required|Description|
|----|----|--------|-----------|
|File Name|string|False|None|

#### imageprocessing

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Image List|[]image|False|None|

#### import

|Name|Type|Required|Description|
|----|----|--------|-----------|
|APIs|string|False|None|
|Module|string|False|None|

#### imports

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Import List|[]import|False|None|

#### module

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Base|string|False|None|
|Name|string|False|None|
|Path|string|False|None|
|Tick|string|False|None|
|UID|string|False|None|

#### modules

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Module List|[]module|False|None|

#### multiscan

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DetectRate PCNT|integer|False|None|
|Engines|engines|False|None|

#### network

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Domains|string|False|None|
|FTP Connections|string|False|None|
|Hosts|string|False|None|
|HTTP Requests|string|False|None|
|Port Info|string|False|None|
|Suricata Alerts|string|False|None|

#### parameterdb

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Parameter List|[]parameterdb_parameter|False|None|

#### parameterdb_parameter

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Database|string|False|None|
|ID|string|False|None|

#### parameters

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Parameter List|[]chronology_parameter|False|None|

#### registry

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access List|[]registry_access|False|None|

#### registry_access

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Path|string|False|None|
|Tick|string|False|None|
|Type|string|False|None|
|UID|string|False|None|

#### report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analysis StartTime|date|False|None|
|Avdetect|string|False|AV MultiScan Detection Percentage|
|Classification Tags|[]string|False|None|
|Domains|[]string|False|None|
|Environment Description|string|False|None|
|Environment ID|string|False|None|
|Hosts|[]string|False|None|
|Interesting|boolean|False|None|
|URL Analysis|boolean|False|None|
|MD5 Hash|string|False|None|
|SHA1 Hash|string|False|None|
|SHA256 Hash|string|False|None|
|Filesize (Bytes)|integer|False|None|
|Filename|string|False|File name|
|Targeturl|string|False|None|
|Threatlevel|integer|False|Threat Level|
|Threatscore|integer|False|Confidence value of VxStream Sandbox in the verdict; lies between 0 and 100|
|Total Network Connections|integer|False|None|
|Total Processes|integer|False|None|
|Total Signatures|integer|False|None|
|Type|string|False|File type|
|Verdict|string|False|File verdict e.g. malicious|
|Vxfamily|string|False|VxFamily e.g. Trojan.Generic|

#### result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Avdetect|integer|False|AV MultiScan Detection Percentage|
|Environment Description|string|False|None|
|Environment ID|string|False|None|
|SHA256 Hash|string|False|None|
|Filesize (Bytes)|integer|False|None|
|Analysis StartTime|date|False|None|
|Filename|string|False|File name|
|Threatscore|integer|False|Confidence value of VxStream Sandbox in the verdict; lies between 0 and 100|
|File Extension|string|False|File type e.g. exe|
|Verdict|string|False|File verdict e.g. malicious|
|Vxfamily|string|False|VxFamily e.g. Trojan.Generic|

#### runtime

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Network|network|False|None|
|Targets|runtime_targets|False|None|

#### runtime_target

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Additional Context|string|False|None|
|API Calls|apicalls|False|None|
|Commandline|string|False|None|
|CPU Tick|integer|False|None|
|Created Files|object|False|None|
|Date|date|False|None|
|File Accesses|fileaccesses|False|None|
|Handles|handles|False|None|
|Hooks|object|False|None|
|Inject|string|False|None|
|Is Injected|boolean|False|None|
|Modules|modules|False|None|
|Monitored|boolean|False|None|
|Mutants|object|False|None|
|Name|string|False|None|
|Network|string|False|None|
|Normalized Path|string|False|None|
|OS Path|string|False|None|
|Parent PID|integer|False|None|
|Parent UID|integer|False|None|
|PID|integer|False|None|
|Registry|registry|False|None|
|UID|string|False|None|
|VBE Events|string|False|None|

#### runtime_targets

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Runtime Target|runtime_target|False|None|

#### sample

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Streams|string|False|None|
|UID|string|False|None|

#### section

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Entropy|float|False|None|
|MD5|string|False|None|
|Name|string|False|None|
|Rsize|string|False|None|
|VA|string|False|None|
|Vsize|string|False|None|

#### sections

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Section List|[]section|False|None|

#### signature

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Database|string|False|None|
|Identifier|string|False|None|
|Name|string|False|None|
|Relevance|string|False|None|
|Sources|string|False|None|
|Threat Level|string|False|None|
|Type|string|False|None|

#### signatures

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Category List|[]category|False|None|

#### static

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Architecture|string|False|None|
|Authenticated Hash|string|False|None|
|Actual CRC|integer|False|None|
|Claimed CRC|integer|False|None|
|Dates|dates|False|None|
|Entrypoint Section|string|False|None|
|Entrypoint VA|string|False|None|
|Exports|string|False|None|
|Import Hash|string|False|None|
|Imports|imports|False|None|
|Language|string|False|None|
|Packers|string|False|None|
|Parser|string|False|None|
|PDB Path|string|False|None|
|Resources|string|False|None|
|Sections|sections|False|None|
|Size|integer|False|None|
|Ssdeep Output|string|False|None|
|TLS Callbacks|string|False|None|
|Type|string|False|None|
|Version Info|string|False|None|
|YARA Hits|string|False|None|

#### strings

|Name|Type|Required|Description|
|----|----|--------|-----------|
|String List|[]custom_string|False|None|

#### trid

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Classification List|object|False|None|

#### verdict

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Is Reliable|string|False|None|
|Threat Level|string|False|None|
|Threat Score|string|False|None|

#### virustotal

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DetectRate PCNT|string|False|None|
|Family Name|string|False|None|
|Result List|[]virustotal_result|False|None|
|SHA256|string|False|None|

#### virustotal_result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AV Name|string|False|None|
|Date|date|False|None|
|Database|string|False|None|
|Is Virus|string|False|None|
|Version|string|False|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 4.0.0 - Updated to reflect Crowdstrike acquisition and rebrand to Falcon Sandbox
* 3.0.0 - Updated variable titles, spelling mistakes
* 2.0.1 - New spec and help.md format for the Hub
* 2.0.0 - Support web server mode | Update to new credential types | Rename "Lookup By Hash" to "Lookup by Hash"
* 1.0.1 - Update to v2 Python plugin architecture, edit to input parsing for lookup, report, and query actions
* 1.0.0 - Invalid key in types section of plugin specification, and style updates
* 0.2.3 - SSL bug fix in SDK
* 0.2.1 - Schema fixes for Search Database and Lookup by Hash actions to allow use in UI by name
* 0.2.0 - Update schema types for Lookup by Hash and Submit actions
* 0.1.0 - Initial plugin

# Links

## References

* [Falcon Sandbox](https://www.crowdstrike.com/endpoint-security-products/falcon-sandbox-malware-analysis/)
* [Hybrid Analysis](https://www.hybrid-analysis.com/)
* [Hybrid Analysis Query Syntax](https://www.hybrid-analysis.com/faq)

