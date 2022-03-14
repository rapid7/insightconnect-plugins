# Description

[Cortex](https://github.com/CERT-BDF/Cortex) is an observable analysis and active response engine.
With the Cortex plugin for Rapid7 InsightConnect, users can manage analyzers, jobs, and run file analyzers.

Use Cortex within an automation workflow to analyze files using hundreds of analyzers to help determine if they are
malicious or safe.

# Key Features

* Manage analyzers
* Manage jobs
* Run file analyzers

# Requirements

* API key
* Cortex hostname

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API key assigned to the user|None|None|
|host|string|None|True|Cortex host e.g. cortex.company.com or 10.3.4.50|None|None|
|port|string|9999|True|Cortex API port e.g. 9999|None|None|
|protocol|string|None|True|HTTP protocol|['HTTP', 'HTTPS']|None|
|proxy|object|None|False|An optional dictionary containing proxy data, with HTTP or HTTPS as the key, and the proxy URL as the value|None|None|
|verify|boolean|True|True|Verify the certificate|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Run Analyzer

This action is used to run an analyzer on an observable.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analyzer_id|string|None|True|Analyzer ID e.g. Hipposcore_1_0|None|None|
|attributes|attributes|None|True|Attributes|None|None|
|observable|string|None|True|A string representing an observable value. This could be an IP address, a domain, URL, or other indicator|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job|job|True|Result of analyzer run|

Example output:

```
{
  "job": {
    "status": "Waiting",
    "date": 1542049729209,
    "id": "AWcJU4q6fI1HpwTkEINU",
    "analyzerId": "0f25f71570887a5eaf34811e410e044f",
    "artifacts": []
  }
}
```

#### Get Job Details

This action is used to list the details of a given job, identified by its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|job_id|string|None|True|Job ID e.g. c9uZDbHBf32DdIVJ|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job|job|True|Matching job|

Example output:

```
{
  "job": {
    "status": "Success",
    "date": 1541969319323,
    "id": "AWcEiJXFX0wPvjeSFsh2",
    "analyzerId": "0f25f71570887a5eaf34811e410e044f",
    "artifacts": []
  }
}
```

#### Get Analyzer by Type

This action is used to list analyzers that can act upon a given datatype.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|type|string|None|True|Data type, e.g. IP address, hash, domain|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|[]analyzers|True|List|

Example output:

```
{
  "list": [
    {
      "id": "d0eb9ca6ed88181843c26bd1cee7a4b6",
      "version": "1.0",
      "dataTypeList": [
        "domain",
        "fqdn",
        "ip",
        "url",
        "other"
      ],
      "name": "CyberCrime-Tracker_1_0",
      "description": "Search cybercrime-tracker.net for C2 servers.",
      "license": "AGPL-V3",
      "author": "ph34tur3",
      "url": "https://github.com/ph34tur3/Cortex-Analyzers"
    },
    {
      "id": "df88142ba58b413e551a8d1e3ecd6eb0",
      "version": "2.1",
      "dataTypeList": [
        "domain",
        "url"
      ],
      "name": "Fortiguard_URLCategory_2_1",
      "description": "Check the Fortiguard category of a URL or a domain. Check the full available list at https://fortiguard.com/webfilter/categories",
      "license": "AGPL-V3",
      "author": "Eric Capuano",
      "url": "https://github.com/TheHive-Project/Cortex-Analyzers"
    },
    {
      "id": "9b0d95706bc617071924152fec31a131",
      "version": "1.0",
      "dataTypeList": [
        "domain"
      ],
      "name": "Crt_sh_Transparency_Logs_1_0",
      "description": "Query domains against the certificate transparency lists available at crt.sh.",
      "license": "AGPL-V3",
      "author": "crackytsi",
      "url": "https://crt.sh"
    },
    {
      "id": "0f25f71570887a5eaf34811e410e044f",
      "version": "2.0",
      "dataTypeList": [
        "ip",
        "domain",
        "url",
        "mail"
      ],
      "name": "Abuse_Finder_2_0",
      "description": "Find abuse contacts associated with domain names, URLs, IPs and email addresses.",
      "license": "AGPL-V3",
      "author": "CERT-BDF",
      "url": "https://github.com/TheHive-Project/Cortex-Analyzers"
    },
    {
      "id": "a4fb69492f817527db0d6778c4ca86d3",
      "version": "2.0",
      "dataTypeList": [
        "domain",
        "fqdn",
        "ip"
      ],
      "name": "CERTatPassiveDNS_2_0",
      "description": "Checks CERT.at Passive DNS for a given domain.",
      "license": "AGPL-V3",
      "author": "Nils Kuhnert, CERT-Bund",
      "url": "https://github.com/BSI-CERT-Bund/cortex-analyzers"
    }
  ]
}
```

#### Get Job Report

This action is used to list the report of a given job, identified by its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|job_id|string|None|True|Job ID e.g. c9uZDbHBf32DdIVJ|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|object|True|Report|

Example output:

```
{
  "report": {
    "workerId": "dd2d532d41e643f3ef09c2660db7d211",
    "organization": "training",
    "workerName": "EmlParser_1_0",
    "pap": 2,
    "dataType": "file",
    "status": "Success",
    "tlp": 1,
    "type": "analyzer",
    "parameters": {},
    "message": "",
    "createdAt": 1542052196785,
    "workerDefinitionId": "EmlParser_1_0",
    "createdBy": "thehive",
    "attachment": {
      "name": "file.txt",
      "hashes": [
        "13d72ff696b7be008a893c3a9de865bbe2f236eb2123c2c8412408894c9306b4",
        "64deb6b10ce96f433af12304eb5f5aaa9f7ab6f0",
        "350508a95660d0b2915f41fe5ab646f4"
      ],
      "size": 28,
      "contentType": "text/plain",
      "id": "13d72ff696b7be008a893c3a9de865bbe2f236eb2123c2c8412408894c9306b4"
    },
    "startDate": 1542052196995,
    "updatedBy": "thehive",
    "updatedAt": 1542052198018,
    "endDate": 1542052198018,
    "id": "AWcJeTG0fI1HpwTkEINk",
    "analyzerId": "dd2d532d41e643f3ef09c2660db7d211",
    "analyzerName": "EmlParser_1_0",
    "analyzerDefinitionId": "EmlParser_1_0",
    "date": 1542052196785,
    "report": {
      "summary": {
        "taxonomies": [
          {
            "level": "info",
            "namespace": "EmlParser",
            "predicate": "Attachments",
            "value": 0
          }
        ]
      },
      "full": {
        "subject": "",
        "date": "",
        "receivers": "",
        "displayFrom": "",
        "sender": "",
        "topic": "",
        "bcc": "",
        "displayto": "",
        "headers": "\nHello World, this is a test\n",
        "body": "Hello World, this is a test\n",
        "attachments": []
      },
      "success": true,
      "artifacts": [],
      "operations": []
    }
  }
}
```

#### Get Analyzers

This action is used to list enabled analyzers within Cortex.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analyzer_id|string|None|False|Analyzer ID e.g. VirusTotal_Scan_3_0. If empty, all enabled analyzers will be returned|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|[]analyzers|True|List|

Example output:

```
{
  "list": [
    {
      "id": "f21d58f9652b1d544d6e43f037d7bd45",
      "version": "3.0",
      "dataTypeList": [
        "ip"
      ],
      "name": "MaxMind_GeoIP_3_0",
      "description": "Use MaxMind to geolocate an IP address.",
      "license": "AGPL-V3",
      "author": "CERT-BDF",
      "url": "https://github.com/TheHive-Project/Cortex-Analyzers"
    },
    {
      "id": "df88142ba58b413e551a8d1e3ecd6eb0",
      "version": "2.1",
      "dataTypeList": [
        "domain",
        "url"
      ],
      "name": "Fortiguard_URLCategory_2_1",
      "description": "Check the Fortiguard category of a URL or a domain. Check the full available list at https://fortiguard.com/webfilter/categories",
      "license": "AGPL-V3",
      "author": "Eric Capuano",
      "url": "https://github.com/TheHive-Project/Cortex-Analyzers"
    },
    {
      "id": "dd2d532d41e643f3ef09c2660db7d211",
      "version": "1.0",
      "dataTypeList": [
        "file"
      ],
      "name": "EmlParser_1_0",
      "description": "Parse Eml message",
      "license": "AGPL-V3",
      "author": "ninsmith",
      "url": "https://github.com/TheHive-Project/Cortex-Analyzers"
    },
    {
      "id": "d0eb9ca6ed88181843c26bd1cee7a4b6",
      "version": "1.0",
      "dataTypeList": [
        "domain",
        "fqdn",
        "ip",
        "url",
        "other"
      ],
      "name": "CyberCrime-Tracker_1_0",
      "description": "Search cybercrime-tracker.net for C2 servers.",
      "license": "AGPL-V3",
      "author": "ph34tur3",
      "url": "https://github.com/ph34tur3/Cortex-Analyzers"
    },
    {
      "id": "a4fb69492f817527db0d6778c4ca86d3",
      "version": "2.0",
      "dataTypeList": [
        "domain",
        "fqdn",
        "ip"
      ],
      "name": "CERTatPassiveDNS_2_0",
      "description": "Checks CERT.at Passive DNS for a given domain.",
      "license": "AGPL-V3",
      "author": "Nils Kuhnert, CERT-Bund",
      "url": "https://github.com/BSI-CERT-Bund/cortex-analyzers"
    },
    {
      "id": "9b0d95706bc617071924152fec31a131",
      "version": "1.0",
      "dataTypeList": [
        "domain"
      ],
      "name": "Crt_sh_Transparency_Logs_1_0",
      "description": "Query domains against the certificate transparency lists available at crt.sh.",
      "license": "AGPL-V3",
      "author": "crackytsi",
      "url": "https://crt.sh"
    },
    {
      "id": "15fb216ff6023e8a0242aa0dea3bbf3e",
      "version": "1.0",
      "dataTypeList": [
        "url"
      ],
      "name": "UnshortenLink_1_0",
      "description": "Use UnshortenLink to reveal the real URL.",
      "license": "AGPL-V3",
      "author": "Remi Pointel, CERT-BDF",
      "url": "https://github.com/TheHive-Project/Cortex-Analyzers"
    },
    {
      "id": "0f25f71570887a5eaf34811e410e044f",
      "version": "2.0",
      "dataTypeList": [
        "ip",
        "domain",
        "url",
        "mail"
      ],
      "name": "Abuse_Finder_2_0",
      "description": "Find abuse contacts associated with domain names, URLs, IPs and email addresses.",
      "license": "AGPL-V3",
      "author": "CERT-BDF",
      "url": "https://github.com/TheHive-Project/Cortex-Analyzers"
    }
  ]
}
```

#### Get Jobs

This action is used to list analysis jobs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analyzerFilter|string|None|False|Analyzer's ID|None|None|
|dataFilter|string|None|False|A string representing a part of an observable value. Could be an IP or part of an IP, a domain, URL and so on|None|None|
|dataTypeFilter|string|None|False|Data type filter e.g. ip, domain, hash, etc|None|None|
|limit|integer|10|False|A number representing a page size|None|None|
|start|integer|0|False|A number representing the index of the page start|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|[]job|True|List of jobs|

Example output:

```
{
  "list": [
    {
      "status": "Success",
      "date": 1542049729209,
      "id": "AWcJU4q6fI1HpwTkEINU",
      "analyzerId": "0f25f71570887a5eaf34811e410e044f",
      "artifacts": []
    },
    {
      "status": "Success",
      "date": 1542046239671,
      "id": "AWcJHku9fI1HpwTkEINP",
      "analyzerId": "dd2d532d41e643f3ef09c2660db7d211",
      "artifacts": []
    },
    {
      "status": "Success",
      "date": 1542046135271,
      "id": "AWcJHLPwfI1HpwTkEINN",
      "analyzerId": "dd2d532d41e643f3ef09c2660db7d211",
      "artifacts": []
    },
    {
      "status": "Success",
      "date": 1542043409332,
      "id": "AWcI8xvNfI1HpwTkEINK",
      "analyzerId": "dd2d532d41e643f3ef09c2660db7d211",
      "artifacts": []
    },
    {
      "status": "Success",
      "date": 1542025636089,
      "id": "AWcH4-j8fI1HpwTkEINH",
      "analyzerId": "0f25f71570887a5eaf34811e410e044f",
      "artifacts": []
    },
    {
      "status": "Success",
      "date": 1542024732484,
      "id": "AWcH1h9yfI1HpwTkEINE",
      "analyzerId": "0f25f71570887a5eaf34811e410e044f",
      "artifacts": []
    },
    {
      "status": "Success",
      "date": 1541969319323,
      "id": "AWcEiJXFX0wPvjeSFsh2",
      "analyzerId": "0f25f71570887a5eaf34811e410e044f",
      "artifacts": []
    },
    {
      "status": "Success",
      "date": 1541969319323,
      "id": "AWcEiJWrX0wPvjeSFsh1",
      "analyzerId": "d0eb9ca6ed88181843c26bd1cee7a4b6",
      "artifacts": []
    }
  ]
}
```

#### Delete Job

This action is used to delete an existing job, identified by its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|job_id|string|None|True|Job ID e.g. c9uZDbHBf32DdIVJ|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|boolean|True|Deletion success|

Example output:

```
{
  "status": true
}
```

#### Run a File Analyzer

This action is used to run analyzers on a file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analyzer_id|string|None|True|Analyzer ID e.g. File_Info_2_0|None|None|
|attributes|input_file_attributes|None|True|Attributes|None|None|
|file|bytes|None|True|A file to analyze|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job|job|True|Result of analyzer run|

Example output:

```
{
  "job": {
    "status": "Waiting",
    "date": 1542050656874,
    "id": "AWcJYbJvfI1HpwTkEINY",
    "analyzerId": "dd2d532d41e643f3ef09c2660db7d211",
    "artifacts": []
  }
}
```

#### Bulk Analyze

This action is used to run all or a collection of analyzers on an observable.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analyze_all|boolean|False|True|Use all available analyzers on observable (ignores list of Analyzer IDs)|None|None|
|analyzer_ids|[]string|None|False|A collection of analyzer IDs e.g ["Hipposcore_1_0", "Robtex"]|None|None|
|attributes|attributes|None|True|Attributes|None|None|
|observable|string|None|True|A string representing an observable value. This could be an IP address, a domain, URL, or other indicator|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|jobs|[]job|True|Collection of results from the analyzers that ran|

Example output:

```
{
  "jobs": [
    {
      "status": "Waiting",
      "date": 1555011546428,
      "id": "AWoN6S09IzgJa3569qEa",
      "analyzerId": "f21d58f9652b1d544d6e43f037d7bd45",
      "artifacts": []
    },
    {
      "status": "Waiting",
      "date": 1555011548130,
      "id": "AWoN6TPjIzgJa3569qEb",
      "analyzerId": "df88142ba58b413e551a8d1e3ecd6eb0",
      "artifacts": []
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.1.1 - New spec and help.md format for the Extension Library
* 1.1.0 - New action Bulk Analyze
* 1.0.0 - Initial plugin

# Links

## References

* [Cortex](https://github.com/TheHive-Project/Cortex)
* [cortex4py](https://github.com/TheHive-Project/Cortex4py/blob/master/Usage.md)

