# Description

[Cortex](https://github.com/CERT-BDF/Cortex) is an observable analysis and active response engine.
With the Cortex plugin for Rapid7 InsightConnect, users can manage analyzers, jobs, and run file analyzers.

Use Cortex within an automation workflow to analyze files using hundreds of analyzers to help determine if they are
malicious or safe.

Note: This plugin utilizes the older unauthenticated [Cortex v1 API](https://github.com/CERT-BDF/CortexDocs/tree/master/api) via [cortex4py](https://pypi.python.org/pypi/cortex4py/1.0.0) and [requests](http://www.python-requests.org/).
For users of Cortex 3.1.0+ please use the newer plugin, Cortex v2, which supports authentication.

# Key Features

* Manage analyzers
* Manage jobs
* Run file analyzers

# Requirements

* Cortex hostname

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|verify|boolean|True|True|Verify the certificate|None|
|host|string|None|True|Cortex host e.g. cortex.company.com or 10.3.4.50|None|
|protocol|string|None|True|HTTP protocol|['http', 'https']|
|port|string|9999|True|Cortex API port e.g. 9999|None|
|proxy|object|None|False|An optional dictionary containing proxy data, with http or https as the key, and the proxy url as the value|None|

## Technical Details

### Actions

#### Run Analyzer

This action is used to run an analyzer on an observable.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|observable|string|None|True|The observable's value e.g. badguy.com|None|
|analyzer_id|string|None|True|Analyzer ID e.g. Hipposcore_1_0|None|
|attributes|attributes|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|The job's status\: Success, InProgress or Failure|
|date|integer|True|A timestamp which represents the job's start date|
|id|string|True|The job's ID|
|artifact|artifact|True|The observable details|
|analyzerId|string|True|The analyzer's ID|

Example output:

```

{
  "analyzerId": "MISP_2_0",
  "status": "InProgress",
  "date": 1509997335557,
  "id": "oMuGYSCKibtxG6SJ",
  "artifact": {
    "data": "1.2.3.4",
    "attributes": {
      "dataType": "ip",
      "tlp": 2
    }
  }
}

```

#### Get Job Details

This action is used to list the details of a given job, identified by its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|job_id|string|None|True|Job ID e.g. c9uZDbHBf32DdIVJ|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|The job's status\: Success, InProgress or Failure|
|date|integer|True|A timestamp which represents the job's start date|
|id|string|True|The job's ID|
|artifact|artifact|True|The observable details|
|analyzerId|string|True|The analyzer's ID|

Example output:

```

{
  "date": 1509934093525,
  "status": "Success",
  "id": "lsqxdgngBF3rdAFe",
  "artifact": {
    "attributes": {
      "tlp": 2,
      "dataType": "ip"
    },
    "data": "1.2.3.4"
  },
  "report": {
    "artifacts": [
      {
        "attributes": {
          "dataType": "url"
        },
        "data": "http://misp-2-4.company.com/"
      }
    ],
    "full": {
      "results": [
        {
          "name": "misp_server_1",
          "result": [],
          "url": "http://misp-2-4.company.com/"
        }
      ]
    },
    "summary": {
      "taxonomies": [
        {
          "predicate": "Search",
          "level": "info",
          "namespace": "MISP",
          "value": "\"0 event\""
        }
      ]
    },
    "success": true
  },
  "analyzerId": "MISP_2_0"
}

```

#### Get Analyzer by Type

This action is used to list analyzers that can act upon a given datatype.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|type|string|None|True|Data type, e.g. IP address, hash, domain|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|[]analyzers|True|None|

Example output:

```

{
  "list": [
    {
      "author": "Nils Kuhnert, CERT-Bund",
      "version": "2.0",
      "name": "MISP",
      "url": "https://github.com/BSI-CERT-Bund/cortex-analyzers",
      "description": "Query multiple MISP instances for events containing an observable.",
      "dataTypeList": [
        "domain",
        "ip",
        "url",
        "fqdn",
        "uri_path",
        "user-agent",
        "hash",
        "email",
        "mail",
        "mail_subject",
        "registry",
        "regexp",
        "other",
        "filename"
      ],
      "license": "AGPL-V3",
      "id": "MISP_2_0"
    },
    {
      "author": "Nils Kuhnert, CERT-Bund",
      "version": "2.0",
      "name": "CERTatPassiveDNS",
      "url": "https://github.com/BSI-CERT-Bund/cortex-analyzers",
      "description": "Checks CERT.at Passive DNS for a given domain, API Key via cert.at.",
      "dataTypeList": [
        "domain",
        "fqdn"
      ],
      "license": "AGPL-V3",
      "id": "CERTatPassiveDNS_2_0"
    }
  ]
}

```

#### Get Job Report

This action is used to list the report of a given job, identified by its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|job_id|string|None|True|Job ID e.g. c9uZDbHBf32DdIVJ|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|object|True|None|

Example output:

```

{
  "id": "P08wjJY04AAz95jc",
  "report": {
    "summary": {
      "taxonomies": [
        {
          "namespace": "MISP",
          "predicate": "Search",
          "level": "info",
          "value": "\"0 event\""
        }
      ]
    },
    "full": {
      "results": [
        {
          "name": "misp_server_1",
          "url": "http://misp-2-4.company.com/",
          "result": []
        }
      ]
    },
    "artifacts": [
      {
        "data": "http://misp-2-4.company.com/",
        "attributes": {
          "dataType": "url"
        }
      }
    ],
    "success": true
  },
  "status": "Success",
  "analyzerId": "MISP_2_0",
  "artifact": {
    "data": "1.2.3.4",
    "attributes": {
      "tlp": 2,
      "dataType": "ip"
    }
  },
  "date": 1509934167175

```

#### Get Analyzers

This action is used to list enabled analyzers within Cortex.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|analyzer_id|string|None|False|Analyzer ID e.g. VirusTotal_Scan_3_0. If empty, all enabled analyzers will be returned|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|[]analyzers|True|None|

Example output:

```

 {
  "list": [
    {
      "name": "Fortiguard_URLCategory",
      "url": "https://github.com/CERT-BDF/Cortex-Analyzers",
      "id": "Fortiguard_URLCategory_2_0",
      "dataTypeList": [
        "domain",
        "url"
      ],
      "author": "Eric Capuano",
      "license": "AGPL-V3",
      "description": "Check the Fortiguard category of a URL or a domain",
      "version": "2.0"
    },
    {
      "name": "MISP",
      "url": "https://github.com/BSI-CERT-Bund/cortex-analyzers",
      "id": "MISP_2_0",
      "dataTypeList": [
        "domain",
        "ip",
        "url",
        "fqdn",
        "uri_path",
        "user-agent",
        "hash",
        "email",
        "mail",
        "mail_subject",
        "registry",
        "regexp",
        "other",
        "filename"
      ],
      "author": "Nils Kuhnert, CERT-Bund",
      "license": "AGPL-V3",
      "description": "Query multiple MISP instances for events containing an observable.",
      "version": "2.0"
    },
    {
      "name": "CERTatPassiveDNS",
      "url": "https://github.com/BSI-CERT-Bund/cortex-analyzers",
      "id": "CERTatPassiveDNS_2_0",
      "dataTypeList": [
        "domain",
        "fqdn"
      ],
      "author": "Nils Kuhnert, CERT-Bund",
      "license": "AGPL-V3",
      "description": "Checks CERT.at Passive DNS for a given domain, API Key via cert.at.",
      "version": "2.0"
    }
  ]
}

```

#### Get Jobs

This action is used to list analysis jobs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|dataTypeFilter|string|None|False|Data type filter e.g. ip, domain, hash, etc.|None|
|start|integer|0|False|A number representing the index of the page start|None|
|analyzerFilter|string|None|False|Analyzer's ID|None|
|dataFilter|string|None|False|A string representing a part of an observable value. Could be an IP or part of an IP, a domain, url and so on|None|
|limit|integer|10|False|A number representing a page size|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|[]job|True|List of jobs|

Example output:

```

{
    "list": [
    {
      "id": "oMuGYSCKibtxG6SJ",
      "analyzerId": "MISP_2_0",
      "report": {
        "full": {
          "results": [
            {
              "name": "misp_server_1",
              "result": [],
              "url": "http://misp-2-4.company.com/"
            }
          ]
        },
        "summary": {
          "taxonomies": [
            {
              "value": "\"0 event\"",
              "namespace": "MISP",
              "level": "info",
              "predicate": "Search"
            }
          ]
        },
        "artifacts": [
          {
            "data": "http://misp-2-4.company.com/",
            "attributes": {
              "dataType": "url"
            }
          }
        ],
        "success": true
      },
      "date": 1509997335557,
      "status": "Success",
      "artifact": {
        "data": "1.2.3.4",
        "attributes": {
          "dataType": "ip",
          "tlp": 2
        }
      }
    },
    ...
  ]
}

```

#### Delete Job

This action is used to delete an existing job, identified by its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|job_id|string|None|True|Job ID e.g. c9uZDbHBf32DdIVJ|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|None|

Example output:

```

{
  "status": true
}

```

#### Run a File Analyzer

This action is used to run analyzers on a file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|attributes|input_file_attributes|None|True|Attributes|None|
|analyzer_id|string|None|True|Analyzer ID e.g. File_Info_2_0|None|
|file|bytes|None|True|A file to analyze|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|The job's status\: Success, InProgress or Failure|
|date|integer|True|A timestamp which represents the job's start date|
|id|string|True|The job's ID|
|artifact|file_artifact|True|The observable details|
|analyzerId|string|True|The analyzer's ID|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Pin library version to 1.0.0
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Add File Analyzer action
* 0.1.0 - Initial plugin

# Links

## References

* [Cortex](https://github.com/CERT-BDF/Cortex)
* [Cortex API](https://github.com/CERT-BDF/CortexDocs/tree/master/api)
* 1.0.1 - New spec and help.md format for the Hub
* [cortex4py](https://pypi.python.org/pypi/cortex4py/1.0.0)

