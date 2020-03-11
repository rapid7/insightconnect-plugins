# Description

[Joe Sandbox](https://www.joesecurity.org) executes files and URLs fully automated in a controlled environment and monitors the behavior of applications and the operating system for suspicious activities.

This plugin supports Joe Sandbox Cloud and Joe Sandbox (on-premise) instances and utilizes the [Joe Sandbox API](https://github.com/joesecurity/jbxapi).

# Key Features

* Submit samples and URLs for sandbox analysis
* Search, list, get, download, and delete analyses
* Get, list, and manage server and user info

# Requirements

* API Key
* Sandbox server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|https://jbxcloud.joesecurity.org/api|False|API URL of the Joe Sandbox instance. Default is for Joe Sandbox Cloud. On-premise installations use the following URL format http://example.com/joesandbox/index.php/api|None|
|api_key|credential_secret_key|None|True|API key generated for Joe Sandbox user|None|

The default setting is to use Joe Sandbox Cloud URL at `https://jbxcloud.joesecurity.org/api`. If you have a Sandbox at a different location such as hosting an on-premise instance, set the `url` field to your instance with the following URL format of `http://example.com/joesandbox/index.php/api`.

## Technical Details

### Actions

#### List Countries

This action is used to retrieve a list of localized internet anonymization countries.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|countries|[]country|True|List of localized internet anonymization countries|

Example output:

```
{
  "countries": [
    {
      "name": "Japan"
    },
    {
      "name": "Lithuania"
    },
    {
      "name": "Netherlands"
    },
    {
      "name": "Norway"
    }
  ]
}
```

#### Search Analysis

This action is used to list the web IDs of the analyses that match the given query. Searches in MD5, SHA1, SHA256, filename, cookbook name, comment, URL and report ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|String to search for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analyses|[]webid|True|A list of matching analyses IDs|

Example output:

```
{
  "analyses": [
    {
      "webid": "792650"
    },
    {
      "webid": "792649"
    }
  ]
}
```

#### Get Server Info

This action is used to query information about the server.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|queuesize|integer|True|Queue size|

Example output:

```
{
  "queuesize": 7
}
```

#### Check Server Status

This action is used to check if Joe Sandbox is online or in maintenance mode.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|online|boolean|True|Is the server online|

Example output:

```
{
  "online": true
}
```

#### Submit Sample URL

This action is used to submit a sample at a given URL for analysis and return the associated web IDs for the sample.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sample_url|string|None|True|The URL of a sample to submit|None|
|additional_parameters|object|None|False|Additional parameters for Joe Sandbox Cloud, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. Parameter `accept-tac` will always be set to 1|None|
|parameters|object|None|False|Custom sandbox parameters, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|webids|[]string|True|Web IDs associated with the sample|

Example output:

```
{
  "webids": [
    "793128"
  ]
}
```

#### List Analyses

This action is used to fetch a list of all analyses.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analyses|[]webid|True|A list of all analyses IDs|

Example output:

```
{
  "analyses": [
    {
      "webid": "792654"
    },
    {
      "webid": "792653"
    },
    {
      "webid": "792652"
    },
    {
      "webid": "792651"
    }
  ]
}
```

#### List Keyboard Layouts

This action is used to retrieve a list of available keyboard layouts for Windows analyzers.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|keyboard_layouts|[]keyboard_layout|True|List of available keyboard layouts|

Example output:

```
{
  "keyboard_layouts": [
    {
      "name": "Norwegian - Norway (Nynorsk)"
    },
    {
      "name": "Polish - Poland"
    },
    {
      "name": "Portuguese - Brazil"
    },
    {
      "name": "Spanish - Bolivarian Republic of Venezuela"
    }
  ]
}
```

#### Submit URL

This action is used to submit a website for analysis and return the associated web IDs for the sample.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|The URL of a website to submit|None|
|additional_parameters|object|None|False|Additional parameters for Joe Sandbox Cloud, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. Parameter `accept-tac` will always be set to 1|None|
|parameters|object|None|False|Custom sandbox parameters, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|webids|[]string|True|Web IDs associated with the sample|

Example output:

```
{
  "webids": [
    "793102"
  ]
}
```

#### Download Analysis

This action is used to download a resource for an analysis. This can be a full report, binaries, screenshots. The full list of resources can be found in the API documentation.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|run|integer|None|False|The number of the run. If not specified, Joe Sandbox will choose one automatically|None|
|type|string|html|False|The report type, e.g. 'html', 'bins'|['bins', 'binstrings', 'classhtml', 'classxml', 'clusterxml', 'cookbook', 'executive', 'graphreports', 'html', 'ida', 'irjson', 'irjsonfixed', 'irxml', 'ishots', 'json', 'jsonfixed', 'lighthtml', 'lightjson', 'lightjsonfixed', 'lightxml', 'maec', 'memdumps', 'memstrings', 'misp', 'openioc', 'pcap', 'pcapslim', 'pdf', 'sample', 'shoots', 'unpack', 'unpackpe', 'xml', 'yara']|
|webid|string|None|True|The web ID of the analysis|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|resource_content|bytes|True|Content of the resource associated with the analysis in base64|
|resource_name|string|True|Name of the resource associated with the analysis|

Example output:

```
{
  "resource_name": "report-784504.html",
  "resource_content": "jwvaHRtbD4="
}
```

#### Submit Sample

This action is used to submit a sample for analysis and return the associated web IDs for the sample.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sample|bytes|None|True|The sample to submit|None|
|cookbook|bytes|None|False|Cookbook to be uploaded together with the sample|None|
|parameters|object|None|False|Custom sandbox parameters, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. In case the `cookbook` option is used, most other options are silently ignored since they can be specified inside the cookbook|None|
|additional_parameters|object|None|False|Additional parameters for Joe Sandbox Cloud, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. Parameter `accept-tac` will always be set to 1|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|webids|[]string|True|Web IDs associated with the sample|

Example output:

```
{
  "webids": [
    "793101"
  ]
}
```

#### List Systems

This action is used to retrieve a list of systems on the server.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|systems|[]system|True|List of systems on the server|

Example output:

```
{
  "systems": [
    {
      "name": "w7x64_lang_packs",
      "description": "Windows 7 x64 with <b>additional language packs (German, French, Swedish)</b>, Java 1.8.0_40, Flash 16.0.0.305, Acrobat Reader 11.0.08, Internet Explorer 11, Chrome 41, Firefox 36",
      "arch": "WINDOWS",
      "count": 1
    },
    {
      "name": "w7x64",
      "description": "Windows 7 x64 (Office 2003 SP3, Java 1.8.0_40, Flash 16.0.0.305, Acrobat Reader 11.0.08, Internet Explorer 11, Chrome 41, Firefox 36)",
      "arch": "WINDOWS",
      "count": 3
    },
    {
      "name": "w7_1",
      "description": "Windows 7 (<b>Office 2010 SP2</b>, Java 1.8.0_40 1.8.0_191, Flash 16.0.0.305, Acrobat Reader 11.0.08, Internet Explorer 11, Chrome 55, Firefox 43)",
      "arch": "WINDOWS",
      "count": 4
    }
  ]
}
```

#### Get Account Info

This action is used to query information about Joe Sandbox user account.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|type|string|True|Type of the account|
|quota|full_quota|True|Account quota|

Example output:

```
{
  "type": "ultimate",
  "quota": {
    "daily": {
      "current": 1,
      "limit": 20,
      "remaining": 19
    },
    "monthly": {
      "current": 11,
      "limit": 50,
      "remaining": 39
    }
  }
}
```

#### Submit Cookbook

This action is used to submit a cookbook for analysis and return the associated web IDs for the cookbook.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cookbook|bytes|None|True|Cookbook to be uploaded together with the sample|None|
|parameters|object|None|False|Custom sandbox parameters, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0|None|
|additional_parameters|object|None|False|Additional parameters for Joe Sandbox Cloud, described in more detail in the API documentation. All boolean parameters should be set to 1 or 0. Parameter `accept-tac` will always be set to 1|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|webids|[]string|True|Web IDs associated with the cookbook|

Example output:

```
{
  "webids": [
    "793118"
  ]
}
```

#### Get Analysis Info

This action is used to show the status and most important attributes of an analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|webid|string|None|True|The web ID of the analysis|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|analysis|analysis|True|Analysis details|

Example output:

```
{
  "analysis": {
    "webid": "792649",
    "time": "2019-02-10T20:31:04+01:00",
    "runs": [
      {
        "detection": "clean",
        "system": "w7_1",
        "yara": false
      }
    ],
    "tags": [],
    "analysisid": "784504",
    "duration": 157,
    "filename": "https://raw.githubusercontent.com/kennethreitz/requests/master/README.md",
    "scriptname": "urldownload.jbs",
    "status": "finished"
  }
}
```

#### Delete Analysis

This action is used to delete an analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|webid|string|None|True|The web ID of the analysis|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deleted|boolean|True|Was the analysis deleted|

Example output:

```
{
  "deleted": true
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - Fix misspelling in error message | Remove generic "automation" keyword
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [Joe Sandbox](https://www.joesecurity.org)
* [Joe Sandbox API](https://jbxcloud.joesecurity.org/userguide?sphinxurl=usage%2Fwebapi.html)
* [Joe Sandbox API wrapper](https://github.com/joesecurity/jbxapi)
* [Report formats](https://jbxcloud.joesecurity.org/userguide?sphinxurl=usage/reportformats.html)

