# Description

Joe Sandbox Cloud executes files and URLs fully automated in a controlled environment and monitors the behavior of applications and the operating system for suspicious activities

# Key Features
  
* Sandbox  
* Analysis  
* Malware

# Requirements
  
* API Key  
* Sandbox server (if not using cloud)

# Supported Product Versions
  
* Joe Sandbox API v2

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|API key generated for Joe Sandbox user|None|8e8786182c66e8bc2abdab9198f1385691987bfe2a4917be1268e915e457dbc5|
|url|string|https://jbxcloud.joesecurity.org/api|False|API URL of the Joe Sandbox instance. Default is for Joe Sandbox Cloud. On-premise installations use the following URL format http://example.com/joesandbox/index.php/api|None|http://example.com/joesandbox/index.php/api|
  
Example input:

```
{
  "api_key": "8e8786182c66e8bc2abdab9198f1385691987bfe2a4917be1268e915e457dbc5",
  "url": "https://jbxcloud.joesecurity.org/api"
}
```

## Technical Details

### Actions


#### Check Server Status
  
This action is used to check if Joe Sandbox is online or in maintenance mode

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|online|boolean|True|Is the server online|True|
  
Example output:

```
{
  "online": true
}
```

#### Delete Analysis
  
This action is used to delete an analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|webid|string|None|True|The web ID of the analysis|None|10001|
  
Example input:

```
{
  "webid": 10001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|deleted|boolean|True|Was the analysis deleted|True|
  
Example output:

```
{
  "deleted": true
}
```

#### Download Analysis
  
This action is used to download a resource for an analysis. This can be a full report, binaries, screenshots, etc

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|run|integer|None|False|The number of the run. If not specified, Joe Sandbox will choose one automatically|None|1|
|type|string|html|False|The report type|["bins", "binstrings", "classhtml", "classxml", "clusterxml", "cookbook", "executive", "graphreports", "html", "ida", "irjson", "irjsonfixed", "irxml", "ishots", "json", "jsonfixed", "lighthtml", "lightjson", "lightjsonfixed", "lightxml", "maec", "memdumps", "memstrings", "misp", "openioc", "pcap", "pcapslim", "pdf", "sample", "shoots", "unpack", "unpackpe", "xml", "yara"]|pdf|
|webid|string|None|True|The web ID of the analysis|None|10001|
  
Example input:

```
{
  "run": 1,
  "type": "html",
  "webid": 10001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|resource_content|bytes|True|Content of the resource associated with the analysis in base64|01001001|
|resource_name|string|True|Name of the resource associated with the analysis|Resource Name|
  
Example output:

```
{
  "resource_content": "01001001",
  "resource_name": "Resource Name"
}
```

#### Get Account Info
  
This action is used to query information about Joe Sandbox user account

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|quota|full_quota|True|Account quota|tbd|
|type|string|True|Type of the account|tbd|
  
Example output:

```
{
  "quota": "tbd",
  "type": "tbd"
}
```

#### Get Analysis Info
  
This action is used to show the status and most important attributes of an analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|webid|string|None|True|The web ID of the analysis|None|10001|
  
Example input:

```
{
  "webid": 10001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis|analysis|True|Analysis details|None|
  
Example output:

```
{
  "analysis": {
    "AnalysisID": {},
    "Comments": {},
    "Duration": 397,
    "Filename": {},
    "MD5": {},
    "Runs": [
      {
        "Detection": {},
        "Error": {},
        "System": {},
        "Yara": false
      }
    ],
    "SHA1": {},
    "SHA256": {},
    "Scriptname": {},
    "Status": {},
    "Tags": [
      "malicious",
      "suspicious"
    ],
    "Time": "2024-02-29 12:50:03+01:00",
    "WebID": 1234567
  }
}
```

#### Get Server Info
  
This action is used to query information about the server

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|queuesize|integer|True|Queue size|5|
  
Example output:

```
{
  "queuesize": 5
}
```

#### Get Submitted Info
  
This action is used to show the status and info of submission

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|submission_id|string|None|True|Submission ID from analysis|None|1001|
  
Example input:

```
{
  "submission_id": 1001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submission_info|submission_info|True|Submission Info|1001|
  
Example output:

```
{
  "submission_info": 1001
}
```

#### List Analyses
  
This action is used to fetch a list of all analyses

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analyses|[]webid|True|A list of all analyses IDs|["10001", "10002", "10003"]|
  
Example output:

```
{
  "analyses": [
    "10001",
    "10002",
    "10003"
  ]
}
```

#### List Countries
  
This action is used to retrieve a list of localized internet anonymization countries

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|countries|[]country|True|List of localized internet anonymization countries|None|
  
Example output:

```
{
  "countries": [
    {
      "Name": "America"
    }
  ]
}
```

#### List Languages And Locales
  
This action is used to retrieve a list of available keyboard layouts for Windows analyzers

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|keyboard_layouts|[]keyboard_layout|True|List of available keyboard layouts|[{"name": "English - United States"}, {"name": "English - Great Britain"}]|
  
Example output:

```
{
  "keyboard_layouts": [
    {
      "name": "English - United States"
    },
    {
      "name": "English - Great Britain"
    }
  ]
}
```

#### List Systems
  
This action is used to retrieve a list of systems on the server

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|systems|[]system|True|List of systems on the server|None|
  
Example output:

```
{
  "systems": [
    {
      "Arch": {},
      "Count": 8,
      "Description": {},
      "Name": "w10x64_office"
    }
  ]
}
```

#### Search Analysis
  
This action is used to lists the web IDs of the analyses that match the given query. Searches in MD5, SHA1, SHA256, 
filename, cookbook name, comment, URL and report ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|String to search for|None|44d88612fea8a8f36de82e1278abb02f|
  
Example input:

```
{
  "query": "44d88612fea8a8f36de82e1278abb02f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analyses|[]webid|True|A list of matching analyses IDs|None|
  
Example output:

```
{
  "analyses": [
    {
      "WebID": 1234567
    }
  ]
}
```

#### Submit Cookbook
  
This action is used to submit a cookbook for analysis and return the associated web IDs for the cookbook

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_parameters|object|None|False|Additional parameters for Joe Sandbox Cloud, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. Parameter `accept-tac` will always be set to 1|None|{ "accept-tac": 1, "url-reputation": 0, "export-to-jbxview": 1, "delete-after-days": 30 }|
|cookbook|bytes|None|True|Cookbook to be uploaded together with the sample|None|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|
|parameters|object|None|False|Custom sandbox parameters, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0|None|{ "comments": "Enabled hybrid code analysis for sample", "hybrid-code-analysis": 1 }|
  
Example input:

```
{
  "additional_parameters": {
    "accept-tac": 1,
    "delete-after-days": 30,
    "export-to-jbxview": 1,
    "url-reputation": 0
  },
  "cookbook": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA...",
  "parameters": {
    "comments": "Enabled hybrid code analysis for sample",
    "hybrid-code-analysis": 1
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submission_id|string|True|Submission ID for submitted analysis|1234567|
  
Example output:

```
{
  "submission_id": 1234567
}
```

#### Submit Sample
  
This action is used to submit a sample for analysis and return the associated web IDs for the sample

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_parameters|object|None|False|Additional parameters for Joe Sandbox Cloud, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. Parameter `accept-tac` will always be set to 1|None|{ "accept-tac": 1, "url-reputation": 0, "export-to-jbxview": 1, "delete-after-days": 30 }|
|cookbook|bytes|None|False|Cookbook to be uploaded together with the sample|None|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|
|filename|string|None|False|Used to give Joe Sandbox a hint at what file type is being uploaded. File extension (eg .txt, .zip) required|None|example.jpg|
|parameters|object|None|False|Custom sandbox parameters, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. In case the `cookbook` option is used, most other options are silently ignored since they can be specified inside the cookbook|None|{ "comments": "Enabled hybrid code analysis for sample", "hybrid-code-analysis": 1 }|
|sample|bytes|None|True|The sample to submit|None|TVqQAAMAAAAEAAAA//8AALgAAAAAAA...|
  
Example input:

```
{
  "additional_parameters": {
    "accept-tac": 1,
    "delete-after-days": 30,
    "export-to-jbxview": 1,
    "url-reputation": 0
  },
  "cookbook": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA...",
  "filename": "example.jpg",
  "parameters": {
    "comments": "Enabled hybrid code analysis for sample",
    "hybrid-code-analysis": 1
  },
  "sample": "TVqQAAMAAAAEAAAA//8AALgAAAAAAA..."
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|webids|[]string|True|Web IDs associated with the sample|None|
  
Example output:

```
{
  "webids": [
    ""
  ]
}
```

#### Submit Sample URL
  
This action is used to submit a sample at a given URL for analysis and return the associated web IDs for the sample

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_parameters|object|None|False|Additional parameters for Joe Sandbox Cloud, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. Parameter `accept-tac` will always be set to 1|None|{ "accept-tac": 1, "url-reputation": 0, "export-to-jbxview": 1, "delete-after-days": 30 }|
|parameters|object|None|False|Custom sandbox parameters, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0|None|{ "comments": "Enabled hybrid code analysis for sample", "hybrid-code-analysis": 1 }|
|sample_url|string|None|True|The URL of a sample to submit|None|https://example.com|
  
Example input:

```
{
  "additional_parameters": {
    "accept-tac": 1,
    "delete-after-days": 30,
    "export-to-jbxview": 1,
    "url-reputation": 0
  },
  "parameters": {
    "comments": "Enabled hybrid code analysis for sample",
    "hybrid-code-analysis": 1
  },
  "sample_url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submission_id|string|True|Submission ID associated with the sample|1234567|
  
Example output:

```
{
  "submission_id": 1234567
}
```

#### Submit URL
  
This action is used to submit a website for analysis and return the associated web IDs for the sample

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_parameters|object|None|False|Additional parameters for Joe Sandbox Cloud, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. Parameter `accept-tac` will always be set to 1|None|{ "accept-tac": 1, "url-reputation": 0, "export-to-jbxview": 1, "delete-after-days": 30 }|
|parameters|object|None|False|Custom sandbox parameters, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0|None|{ "comments": "Enabled hybrid code analysis for sample", "hybrid-code-analysis": 1 }|
|url|string|None|True|The URL of a website to submit|None|https://example.com|
  
Example input:

```
{
  "additional_parameters": {
    "accept-tac": 1,
    "delete-after-days": 30,
    "export-to-jbxview": 1,
    "url-reputation": 0
  },
  "parameters": {
    "comments": "Enabled hybrid code analysis for sample",
    "hybrid-code-analysis": 1
  },
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submission_id|string|True|Submission ID associated with the sample|1001|
  
Example output:

```
{
  "submission_id": 1001
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**system**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Arch|string|None|None|Architecture (one of WINDOWS, MAC, LINUX, IOS, ANDROID)|WINDOWS|
|Count|integer|None|None|How many systems of given type exist|8|
|Description|string|None|None|Description|Windows 10 64 bit (version 1803) with <b>Office 2016</b> Adobe Reader DC 19, Chrome 104, Firefox 63, Java 8.171, Flash 30.0.0.113|
|Name|string|None|None|Name|w10x64_office|
  
**keyboard_layout**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|None|Name of the keyboard layout language|English - Great Britain|
  
**country**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|None|Name of the country|America|
  
**single_quota**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Current|integer|None|None|Current quota|20|
|Limit|integer|None|None|Limit of quota|30|
|Remaining|integer|None|None|Remaining quota|30|
  
**full_quota**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Daily|single_quota|None|None|Daily quota|None|
|Monthly|single_quota|None|None|Monthly quota|None|
  
**webid**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|WebID|string|None|None|Web ID|1234567|
  
**run**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Detection|string|None|None|Detection, one of: unknown, clean, suspicious, malicious|clean|
|Error|string|None|None|Error description, will not be present if no error was detected|None|
|System|string|None|None|System|w10x64_office|
|Yara|boolean|None|None|Yara|False|
  
**submission_info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|analyses|[]object|None|None|Analysis details|[{}]|
|Most Relevant Analysis|object|None|None|Webid, detection & score|{}|
|name|string|None|None|name|w10x64_office|
|Status|string|None|None|Status of the analysis e.g. submitted, running, finished|submitted|
|Submission ID|string|None|None|submission ID|1234567|
|time|string|None|None|time|2012-10-03:10-00|
  
**analysis**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AnalysisID|string|None|None|Analysis ID. Will not be returned if the analysis is not finished|1234567|
|Comments|string|None|None|Comments|Suspicious URL here|
|Duration|integer|None|None|Duration of the analysis in seconds (only for finished analyses)|397|
|Filename|string|None|None|File name|testfile.txt|
|MD5|string|None|None|MD5|0f0c95e3facb5859ea37e7e033390b1a|
|Runs|[]run|None|None|Runs|None|
|Scriptname|string|None|None|Script name|browseurl.jbs|
|SHA1|string|None|None|SHA1|0f0c95e3facb5859ea37e7e033390b1a|
|SHA256|string|None|None|SHA256|0f0c95e3facb5859ea37e7e033390b1a|
|Status|string|None|None|Status of the analysis, one of: submitted, running, finished|submitted|
|Tags|[]string|None|None|Tags|["malicious", "suspicious"]|
|Time|date|None|None|Time|2024-02-29 12:50:03+01:00|
|WebID|string|None|None|Web ID|1234567|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History
  
*This plugin does not contain a version history.*

# Links


## References
  
*This plugin does not contain any references.*