# Description

Utilizing the power of Rapid7's Insight platform and the heritage of our award-winning Nexpose product, InsightVM - our vulnerability management solution - provides a fully available, scalable, and efficient way to collect your vulnerability data, turn it into answers, and minimize your risk in modern networks.

This plugin utilizes the [InsightVM API 3](https://help.rapid7.com/insightvm/en-us/api/index.html).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to your InsightVM console, without trailing slashes, e.g. https\://insightvm.example.com\:3780|None|
|credentials|credential_username_password|None|True|Username and password|None|

## Technical Details

### Actions

#### Get Asset

This action gets an asset by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Get an asset by ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asset|asset|True|Asset details|

Example output:

```
{
  "asset": {
    "addresses": [
      {
        "ip": "10.0.0.1",
        "mac": "00:50:56:8A:3D:8C"
      }
    ],
    "assessedForPolicies": False,
    "assessedForVulnerabilities": True,
    "history": [
      {
        "date": "2018-08-28T11:06:47.738Z",
        "scanId": 189170,
        "type": "SCAN",
        "version": 1
      }
    ],
    "id": 74708,
    "ip": "10.0.0.1",
    "links": [
      {
        "href": "https://insightvm:3780/api/3/assets/74708",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/assets/74708/software",
        "rel": "Software"
      },
      {
        "href": "https://insightvm:3780/api/3/assets/74708/files",
        "rel": "Files"
      },
      {
        "href": "https://insightvm:3780/api/3/assets/74708/users",
        "rel": "Users"
      },
      {
        "href": "https://insightvm:3780/api/3/assets/74708/user_groups",
        "rel": "User Groups"
      },
      {
        "href": "https://insightvm:3780/api/3/assets/74708/databases",
        "rel": "Databases"
      },
      {
        "href": "https://insightvm:3780/api/3/assets/74708/services",
        "rel": "Services"
      },
      {
        "href": "https://insightvm:3780/api/3/assets/74708/tags",
        "rel": "Tags"
      }
    ],
    "mac": "00:50:56:8A:3D:8C",
    "os": "Microsoft Windows Server 2012",
    "osFingerprint": {
      "cpe": {
        "part": "o",
        "product": "windows_server_2012",
        "update": "gold",
        "v2.2": "cpe:/o:microsoft:windows_server_2012:-:gold",
        "v2.3": "cpe:2.3:o:microsoft:windows_server_2012:-:gold:*:*:*:*:*:*",
        "vendor": "microsoft",
        "version": "-"
      },
      "description": "Microsoft Windows Server 2012",
      "family": "Windows",
      "id": 720,
      "product": "Windows Server 2012",
      "systemName": "Microsoft Windows",
      "type": "General",
      "vendor": "Microsoft"
    },
    "rawRiskScore": 4787.376953125,
    "riskScore": 4787.376953125,
    "services": [
      {
        "configurations": [
          {
            "name": "ssl",
            "value": "true"
          },
          {
            "name": "ssl.cert.chainerror",
            "value": "[Path does not chain with any of the trust anchors]"
          }
        ],
        "links": [
          {
            "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389",
            "rel": "self"
          },
          {
            "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/configurations",
            "rel": "Configurations"
          },
          {
            "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/databases",
            "rel": "Databases"
          },
          {
            "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/users",
            "rel": "Users"
          },
          {
            "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/user_groups",
            "rel": "User Groups"
          },
          {
            "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/web_applications",
            "rel": "Web Applications"
          }
        ],
        "port": 3389,
        "protocol": "tcp"
      }
    ],
    "vulnerabilities": {
      "critical": 0,
      "exploits": 1,
      "malwareKits": 0,
      "moderate": 7,
      "severe": 7,
      "total": 14
    }
  }
}
```

#### Get Asset Tags

This action is used to get a listing of all tags for an asset.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|asset_id|integer|None|True|Identifier of asset|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tags|[]tag|True|List of tags|

Example output:

```
{
  "tags": [
    {
      "color": "default",
      "created": "2019-02-06T15:07:07.517Z",
      "id": 83,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/tags/83",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/83/assets",
          "rel": "Tag Assets"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/83/asset_groups",
          "rel": "Tag Asset Groups"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/83/sites",
          "rel": "Tag Sites"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/83/search_criteria",
          "rel": "Tag Search Criteria"
        },
        {
          "href": "https://insightvm:3780/api/3/users/2",
          "rel": "Tag Creator"
        }
      ],
      "name": "windows",
      "source": "custom",
      "sources": [
        {
          "id": 9,
          "links": [
            {
              "id": 9,
              "href": "https://insightvm:3780/api/3/asset_groups/9",
              "rel": "Asset Group"
            }
          ],
          "source": "asset-group"
        }
      ],
      "type": "custom"
    },
    {
      "color": "default",
      "created": "2019-04-24T17:06:29.296Z",
      "id": 168,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/tags/168",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/168/assets",
          "rel": "Tag Assets"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/168/asset_groups",
          "rel": "Tag Asset Groups"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/168/sites",
          "rel": "Tag Sites"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/168/search_criteria",
          "rel": "Tag Search Criteria"
        },
        {
          "href": "https://insightvm:3780/api/3/users/1",
          "rel": "Tag Creator"
        }
      ],
      "name": "Windows Servers",
      "source": "custom",
      "sources": [
        {
          "id": 12,
          "links": [
            {
              "id": 12,
              "href": "https://insightvm:3780/api/3/asset_groups/12",
              "rel": "Asset Group"
            }
          ],
          "source": "asset-group"
        }
      ],
      "type": "custom"
    }
  ]
}
```

#### Get Asset Vulnerabilities

This action is used to get vulnerabilities found on an asset. Can only be used if the asset has first been scanned (via Komand or other means).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|asset_id|string|None|True|ID of the asset for which to find vulnerabilities|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|vulnerabilities|[]asset_vulnerability|False|Vulnerabilities found on the asset|

Example output:

```

{
  "vulnerabilities": [{
    "id": "tlsv1_1-enabled",
    "instances": 2,
    "links": [{
        "href": "",
        "rel": "self"
      },
      {
        "id": "tlsv1_1-enabled",
        "href": "",
        "rel": "Vulnerability"
      },
      {
        "id": "tlsv1_1-enabled",
        "href": "",
        "rel": "Vulnerability Validations"
      },
      {
        "id": "tlsv1_1-enabled",
        "href": "",
        "rel": "Vulnerability Solutions"
      }
    ],
    "results": [{
        "port": 995,
        "proof": "<p><p>Successfully connected to 10.4.22.249:995 over TLSv1.1</p></p>",
        "protocol": "tcp",
        "since": "2016-02-23T18:20:33.811Z",
        "status": "vulnerable"
      },
      {
        "port": 110,
        "proof": "<p><p>Successfully connected to 10.4.22.249:110 over TLSv1.1</p></p>",
        "protocol": "tcp",
        "since": "2016-02-23T18:20:33.811Z",
        "status": "vulnerable"
      }
    ],
    "since": "2016-02-23T18:20:33.811Z",
    "status": "vulnerable"
  }]
}

```

#### Get Asset Software

This action is used to get software found on an asset. Can only be used if the asset has first been scanned.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|asset_id|string|None|True|ID of the asset for which to find software|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|software|[]software|False|Software found on the asset|

Example output:

```
{
  "software": [
    {
      "description": "Apache Struts 1.3.10",
      "family": "Struts",
      "id": 3910,
      "product": "Struts",
      "type": "Middleware",
      "vendor": "Apache",
      "version": "1.3.10"
    }
  }
}
```

#### Get Scan

This action is used to get the status of a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_id|string|None|True|ID of the scan to obtain|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Scan status (aborted, unknown, running, finished, stopped, error, paused, dispatched or integrating)|
|scanType|string|False|Scan type (manual, automated, scheduled)|
|assets|integer|False|Number of assets within the scan|
|links|[]link|False|Links|
|vulnerabilities|vulnerabilities_count|False|Counts of vulnerabilities found within the scan|
|startTime|string|False|Start time of the scan in ISO8601 format|
|duration|string|False|Duration of the scan in ISO8601 format|
|engineName|string|False|Name of the engine used for the scan|
|endTime|string|False|End time of the scan in ISO8601 format|
|id|integer|False|ID of the scan|
|scanName|string|False|User-driven scan name for the scan|

Example output:

```

{
  "result": {
    "assets": 0,
    "engineName": "Local scan engine",
    "id": 188934,
    "links": [
      {
        "href": "https://insightvm:3780/api/3/scans/188934",
        "rel": "self"
      }
    ],
    "scanName": "API Scan - 2018-04-23T04:21:05Z",
    "scanType": "Manual",
    "startTime": "2018-04-23T04:21:05.500Z",
    "status": "running",
    "vulnerabilities": {
      "critical": 0,
      "moderate": 0,
      "severe": 0,
      "total": 0
    }
  }
}
```

#### Get Site Assets

This action is used to get assets for a site.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|site_id|string|None|True|ID of the site to get assets for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|[]asset|False|Assets|

Example output:

```

{
  "assets": [{
    "addresses": [{
      "ip": ""
    }],
    "assessedForPolicies": true,
    "assessedForVulnerabilities": true,
    "history": [{
      "date": "2015-04-08T20:12:24.353Z",
      "type": "SCAN",
      "version": 1
    }],
    "hostName": "",
    "hostNames": [{
          "name": "42:878126666232_i-2377d629",
          "source": "epsec"
      },
      {
          "name": "",
          "source": "dns"
      }
    ],
    "id": 18086,
    "ip": "",
    "links": [{
      "href": "",
      "rel": "self"
    }],
    "os": "Asus embedded",
    "osFingerprint": {
      "description": "Asus embedded",
      "family": "embedded",
      "id": 13792,
      "product": "embedded",
      "systemName": "Asus embedded",
      "type": "WAP",
      "vendor": "Asus"
    },
    "rawRiskScore": 0,
    "riskScore": 0,
    "vulnerabilities": {
      "critical": 0,
      "exploits": 0,
      "malwareKits": 0,
      "moderate": 0,
      "severe": 0,
      "total": 0
    }
  }]
}

```

#### Scan

This action is used to start a scan on a site.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|site_id|string|None|True|ID of the site to scan|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|Scan ID|
|links|[]link|False|Hypermedia links to corresponding or related resources|

Example output:

```

{
  "result": {
    "links": [
      {
        "href": "https://insightvm:3780/api/3/sites/44/scans",
        "rel": "self"
      },
      {
        "id": 188935,
        "href": "https://insightvm:3780/api/3/scans/188935",
        "rel": "Scan"
      }
    ],
    "id": 188935
  }
}

```

#### Generate AdHoc SQL Report

This action is used to create, generate, download, and cleanup a SQL report based on the provided query.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filters|string|{}|False|Filters in JSON format to be applied to the contents of the report; review InsightVM API documentation for filter options|None|
|query|string|None|True|Reporting Data Model SQL query|None|
|scope|string|none|True|Scope context for generated report; if set, remediations will be scoped by each in scope ID, e.g Site ID, Tag ID, Asset Group ID; scan scope only supports single scan ID as input|['none', 'assets', 'assetGroups', 'sites', 'tags', 'scan']|
|scope_ids|[]integer|[]|False|Scope IDs for which tickets should be generated, by default all are included|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|file|True|Base64 encoded file making up the report|

Example output:

```
{
  "report": {
    "content": "YXNzZXRfaWQsbWFjX2FkZHJlc3MsaXBfYWRkcmVzcyxob3N0X25hbWUsb3BlcmF0aW5nX3N5c3RlbV9pZCxob3N0X3R5cGVfaWQsbWF0Y2hfdmFsdWUsc2l0ZXMsbGFzdF9hc3Nlc3NlZF9mb3JfdnVsbmVyYWJpbGl0aWVzCjE0OCwsMy4xNy4yMTQuNjgsZWMyLTMtMTctMjE0LTY4LnVzLWVhc3QtMi5jb21wdXRlLmFtYXpvbmF3cy5jb20sNjEsLTEsMC4zMjQ5OTk5ODgsVGVzdC1FQzIsMjAxOS0wNC0xNiAyMDoyNzo0Mi4yNTUKMTQ5LCwzLjE5LjEyNC4yNCxlYzItMy0xOS0xMjQtMjQudXMtZWFzdC0yLmNvbXB1dGUuYW1hem9uYXdzLmNvbSwtMSwtMSwwLjMyNDk5OTk4OCxUZXN0LUVDMiwyMDE5LTA0LTE2IDIwOjI3OjU3LjM4OQo=",
    "filename": "adhoc_sql_report.csv"
  }
}
```

#### Download Report

This action is used to return the contents of a generated report.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|instance|string|None|True|The identifier of the report instance, 'latest' or ID e.g. 100|None|
|id|integer|None|True|Identifier of the report to download e.g. 265|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|bytes|False|Base64 encoded report|

Example output:

```

{
  "report": "<base64 encoded report>"
}

```

#### List Reports

This action is used to list reports and return their identifiers.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sort|string|None|True|Sort order, ascending or descending|['Ascending', 'Descending']|
|name|string|None|False|Name of report, otherwise all reports by criteria|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|Whether optional user supplied report name was found|
|list|[]report_id|False|List of report identifiers|

Example output:

```

{
  "found": false,
  "list": [
    {
      "name": "Host Inventory",
      "id": 111
    },
    {
      "name": "PCI Host Details - Critical Assets",
      "id": 112
    },
  ]
}

```

#### Get Vulnerability Affected Assets

This action is used to get the assets affected by the vulnerability.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|vulnerability_id|string|None|True|The identifier of the vulnerability e.g. jre-vuln-cve-2013-2471|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|resources|[]integer|False|The identifiers of the associated resources|

Example output:

```

{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/vulnerabilities/jre-vuln-cve-2013-2471/assets",
      "rel": "self"
    },
    {
      "href": "https://insightvm:3780/api/3/assets/259",
      "rel": "Asset"
    },
    {
      "href": "https://insightvm:3780/api/3/assets/22754",
      "rel": "Asset"
    }
  ],
  "resources": [
    259,
    22754
  ]
}

```

#### Create Tag

This action is used to create a new tag.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Tag name|None|
|type|string|None|True|Tag type|['owner', 'location', 'custom']|
|color|string|default|False|Tag color (only available for custom tags)|['default', 'blue', 'green', 'orange', 'purple', 'red']|
|searchCriteria|object|None|False|Tag search Criteria - options documentation https\://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the created tag|

Example output:

```
{
  "id": 665
}
```

#### Delete Tag

This action is used to delete an existing tag.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Tag ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/tags/20",
      "rel": "self"
    }
  ]
}
```

#### Get Tags

This action is used to get a listing of all tags and return their details.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|type|string||False|Type of tag by which to filter, all types are returned if none is specified|['owner', 'location', 'custom', 'criticality', '']|
|name|string||False|Tag name regular expression by which to filter|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tags|[]tag|True|List of tags|

Example output:

```
{
  "tags": [
    {
      "color": "default",
      "created": "2017-11-23T16:11:16.641Z",
      "id": 2,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/tags/2",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/2/assets",
          "rel": "Tag Assets"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/2/asset_groups",
          "rel": "Tag Asset Groups"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/2/sites",
          "rel": "Tag Sites"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/2/search_criteria",
          "rel": "Tag Search Criteria"
        },
        {
          "href": "https://insightvm:3780/api/3/users/0",
          "rel": "Tag Creator"
        }
      ],
      "name": "High",
      "riskModifier": "1.5",
      "source": "built-in",
      "type": "criticality"
    },
    {
      "color": "default",
      "created": "2017-11-23T16:11:16.641Z",
      "id": 4,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/tags/4",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/4/assets",
          "rel": "Tag Assets"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/4/asset_groups",
          "rel": "Tag Asset Groups"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/4/sites",
          "rel": "Tag Sites"
        },
        {
          "href": "https://insightvm:3780/api/3/tags/4/search_criteria",
          "rel": "Tag Search Criteria"
        },
        {
          "href": "https://insightvm:3780/api/3/users/0",
          "rel": "Tag Creator"
        }
      ],
      "name": "Low",
      "riskModifier": "0.75",
      "source": "built-in",
      "type": "criticality"
    }
  ]
}
```

#### Get Tag

This action is used to get tag details by tag ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Tag ID, e.g. 1|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tag|tag|True|Tag Details|

Example output:

```
{
  "tag": {
    "color": "default",
    "created": "2014-03-21T01:45:04.584Z",
    "id": 1,
    "links": [
      {
        "href": "https://insightvm:3780/api/3/tags/1",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/tags/1/assets",
        "rel": "Tag Assets"
      },
      {
        "href": "https://insightvm:3780/api/3/tags/1/asset_groups",
        "rel": "Tag Asset Groups"
      },
      {
        "href": "https://insightvm:3780/api/3/tags/1/sites",
        "rel": "Tag Sites"
      },
      {
        "href": "https://insightvm:3780/api/3/tags/1/search_criteria",
        "rel": "Tag Search Criteria"
      },
      {
        "href": "https://insightvm:3780/api/3/users/0",
        "rel": "Tag Creator"
      }
    ],
    "name": "Very High",
    "riskModifier": "2",
    "searchCriteria": {
      "match": "all",
      "filters": [
        {
          "field": "operating-system",
          "operator": "contains",
          "value": "windows"
        },
        {
          "field": "site-id",
          "operator": "in",
          "values": [
            "1"
          ]
        }
      ]
    },
    "source": "built-in",
    "type": "criticality"
  }
}
```

#### Get Tag Sites

This action is used to get site IDs associated with a tag.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tag_id|integer|None|True|Tag ID for which to retrieve site associations|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|site_ids|[]integer|True|Site IDs associated with the tag|

Example output:

```
{
  "site_ids": [
    42
  ]
}
```

#### Get Tag Assets

This action is used to tag ID for which to retrieve asset associations.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tag_id|integer|None|True|Tag ID to add to site|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|[]tag_asset|True|Asset IDs and tag association sources for the tag|

Example output:

```
{
  "assets": [
    {
      "id": 3,
      "sources": [
        "asset-group",
        "criteria"
      ]
    },
    {
      "id": 18,
      "sources": [
        "site"
      ]
    }
  ]
}
```

#### Get Tag Asset Groups

This action is used to get asset groups associated with a tag.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tag_id|integer|None|True|Tag ID for which to retrieve asset group associations|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asset_group_ids|[]integer|True|Asset group IDs associated with the tag|

Example output:

```
{
  "asset_group_ids": [
    15,
    42
  ]
}
```

#### Remove Asset Tag

This action is used to remove a tag from an asset.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|asset_id|integer|None|True|Asset ID from which to remove the tag|None|
|tag_id|integer|None|True|Tag ID to remove from the asset|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/assets/21150/tags/69",
      "rel": "self"
    }
  ]
}
```

#### Remove Asset Group Tags

This action is used to remove all tags from an asset group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Asset group ID from which to remove all tags|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/asset_groups/20/tags",
      "rel": "self"
    }
  ]
}
```

#### Remove Tag Asset Groups

This action is used to remove all asset group associations from a tag.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Tag ID from which to remove all asset group associations|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/tags/69/asset_groups",
      "rel": "self"
    }
  ]
}
```

#### Remove Tag Sites

This action is used to remove all site associations from a tag.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Tag ID from which to remove all site associations|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/tags/69/sites",
      "rel": "self"
    }
  ]
}
```

#### Remove Tag Search Criteria

This action is used to remove all search criteria from a tag.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Tag ID from which to remove all search criteria|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/tags/69/search_criteria",
      "rel": "self"
    }
  ]
}
```

#### Tag Asset

This action is used to add a tag to an asset.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|asset_id|integer|None|True|Asset ID to tag|None|
|tag_id|integer|None|True|Tag ID to add to site|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/assets/21150/tags/4",
      "rel": "self"
    }
  ]
}
```

#### Tag Asset Group

This action is used to add a tag to an asset group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|asset_group_id|integer|None|True|Asset group ID to tag|None|
|tag_id|integer|None|True|Tag ID to add to site|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/asset_groups/20/tags/69",
      "rel": "self"
    }
  ]
}
```

#### Tag Site

This action is used to add a tag to a site.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|site_id|integer|None|True|Site ID to tag|None|
|tag_id|integer|None|True|Tag ID to add to site|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/sites/42/tags/69",
      "rel": "self"
    }
  ]
}
```

#### Update Tag Search Criteria

This action is used to update the search criteria for an existing tag.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Tag ID|None|
|searchCriteria|object|None|True|Tag search criteria - options documentation\: https\://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/tags/69/search_criteria",
      "rel": "self"
    }
  ]
}
```

#### Asset Search

This action is used to search for assets using a filtered asset search.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|searchCriteria|object|None|True|Tag search criteria - options documentation\: https\://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|[]asset|True|List of asset details returned by the search|

Example output:

```
{
  "assets": [
      {
          "addresses": [
              {
                  "ip": "10.0.0.1",
                  "mac": "00:50:56:8A:3D:8C"
              }
          ],
          "assessedForPolicies": False,
          "assessedForVulnerabilities": True,
          "history": [
              {
                  "date": "2018-08-28T11:06:47.738Z",
                  "scanId": 189170,
                  "type": "SCAN",
                  "version": 1
              }
          ],
          "id": 74708,
          "ip": "10.0.0.1",
          "links": [
              {
                  "href": "https://insightvm:3780/api/3/assets/74708",
                  "rel": "self"
              },
              {
                  "href": "https://insightvm:3780/api/3/assets/74708/software",
                  "rel": "Software"
              },
              {
                  "href": "https://insightvm:3780/api/3/assets/74708/files",
                  "rel": "Files"
              },
              {
                  "href": "https://insightvm:3780/api/3/assets/74708/users",
                  "rel": "Users"
              },
              {
                  "href": "https://insightvm:3780/api/3/assets/74708/user_groups",
                  "rel": "User Groups"
              },
              {
                  "href": "https://insightvm:3780/api/3/assets/74708/databases",
                  "rel": "Databases"
              },
              {
                  "href": "https://insightvm:3780/api/3/assets/74708/services",
                  "rel": "Services"
              },
              {
                  "href": "https://insightvm:3780/api/3/assets/74708/tags",
                  "rel": "Tags"
              }
          ],
          "mac": "00:50:56:8A:3D:8C",
          "os": "Microsoft Windows Server 2012",
          "osFingerprint": {
              "cpe": {
                  "part": "o",
                  "product": "windows_server_2012",
                  "update": "gold",
                  "v2.2": "cpe:/o:microsoft:windows_server_2012:-:gold",
                  "v2.3": "cpe:2.3:o:microsoft:windows_server_2012:-:gold:*:*:*:*:*:*",
                  "vendor": "microsoft",
                  "version": "-"
              },
              "description": "Microsoft Windows Server 2012",
              "family": "Windows",
              "id": 720,
              "product": "Windows Server 2012",
              "systemName": "Microsoft Windows",
              "type": "General",
              "vendor": "Microsoft"
          },
          "rawRiskScore": 4787.376953125,
          "riskScore": 4787.376953125,
          "services": [
              {
                  "configurations": [
                      {
                          "name": "ssl",
                          "value": "true"
                      },
                      {
                          "name": "ssl.cert.chainerror",
                          "value": "[Path does not chain with any of the trust anchors]"
                      }
                  ],
                  "links": [
                      {
                          "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389",
                          "rel": "self"
                      },
                      {
                          "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/configurations",
                          "rel": "Configurations"
                      },
                      {
                          "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/databases",
                          "rel": "Databases"
                      },
                      {
                          "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/users",
                          "rel": "Users"
                      },
                      {
                          "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/user_groups",
                          "rel": "User Groups"
                      },
                      {
                          "href": "https://insightvm:3780/api/3/assets/74708/services/tcp/3389/web_applications",
                          "rel": "Web Applications"
                      }
                  ],
                  "port": 3389,
                  "protocol": "tcp"
              }
          ],
          "vulnerabilities": {
              "critical": 0,
              "exploits": 1,
              "malwareKits": 0,
              "moderate": 7,
              "severe": 7,
              "total": 14
          }
      }
  ]
}
```

#### Create Asset Group

This action is used to create an asset group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|description|string|None|False|Asset group description|None|
|type|string|None|True|Asset group type|['dynamic', 'static']|
|name|string|None|True|Asset group name|None|
|searchCriteria|object|None|False|Asset group search criteria - options documentation\: https\://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|ID of the created tag|

Example output:

```
{
  "id": 20
}
```

#### Create Site

This action is used to create a new site.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|The site name. Name must be unique|None|
|description|string|None|False|The site's description|None|
|engine_id|integer|None|False|The identifier of a scan engine. Default scan engine is selected when not specified|None|
|importance|string|normal|False|The site importance|['very_low', 'low', 'normal', 'high', 'very_high']|
|scan_template_id|string|None|False|The identifier of a scan template|None|
|included_addresses|[]string|[]|False|List of addresses to include in scan scope|None|
|excluded_addresses|[]string|[]|False|List of addresses to exclude in scan scope|None|
|included_asset_groups|[]integer|[]|False|Assets associated with these asset group IDs will be included in the site|None|
|excluded_asset_groups|[]integer|[]|False|Assets associated with these asset group IDs will be excluded in the site|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|The identifier of the created site|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/sites",
      "rel": "self"
    },
    {
      "id": 15,
      "href": "https://insightvm:3780/api/3/sites/15",
      "rel": "Site"
    }
  ],
  "id": 15
}
```

#### Update Site

This action is used to update an existing site.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|The identifier of the site|None|
|name|string|None|True|The site name. Name must be unique|None|
|description|string|None|True|The site's description|None|
|engine_id|integer|None|True|The identifier of a scan engine. Default scan engine is selected when not specified|None|
|importance|string|normal|True|The site importance|['very_low', 'low', 'normal', 'high', 'very_high']|
|scan_template_id|string|None|True|The identifier of a scan template|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|The identifier of the updated site|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "id": 332,
  "links": [
    {
      "href": "https://insightvm:3780/api/3/sites/332",
      "rel": "self"
    }
  ]
}
```

#### Update Site Included Targets

This action is used to update an existing site scope of included IP address and hostname targets.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|The identifier of the site|None|
|included_targets|[]string|None|False|List of addresses that represent either a hostname, IPv4 address, IPv4 address range, IPv6 address, or CIDR notation|None|
|overwrite|boolean|True|True|Whether to overwrite the included targets to the current site or append to the previous list of included targets|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|The identifier of the updated site|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "id": 332,
  "links": [
    {
      "href": "https://insightvm:3780/api/3/sites/332/included_targets",
      "rel": "self"
    }
  ]
}
```

#### Update Site Excluded Targets

This action is used to update an existing site scope of excluded IP address and hostname targets.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|The identifier of the site|None|
|excluded_targets|[]string|None|False|List of addresses that represent either a hostname, IPv4 address, IPv4 address range, IPv6 address, or CIDR notation|None|
|overwrite|boolean|True|True|Whether to overwrite the excluded targets to the current site or append to the previous list of excluded targets|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|The identifier of the updated site|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "id": 332,
  "links": [
    {
      "href": "https://insightvm:3780/api/3/sites/332/excluded_targets",
      "rel": "self"
    }
  ]
}
```

#### Update Site Included Asset Groups

This action is used to update an existing site scope of included asset groups.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|The identifier of the site|None|
|included_asset_groups|[]integer|None|False|Assets associated with these asset group IDs will be included in the site|None|
|overwrite|boolean|True|True|Whether to overwrite the included asset group IDs to the current site or append to the previous list of asset group IDs|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|The identifier of the updated site|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "id": 332,
  "links": [
    {
      "href": "https://insightvm:3780/api/3/sites/332/included_asset_groups",
      "rel": "self"
    }
  ]
}
```

#### Update Site Excluded Asset Groups

This action is used to update an existing site scope of excluded asset groups.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|The identifier of the site|None|
|excluded_asset_groups|[]integer|None|False|Assets associated with these asset group IDs will be excluded from the site|None|
|overwrite|boolean|True|True|Whether to overwrite the excluded asset group IDs to the current site or append to the previous list of asset group IDs|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|The identifier of the updated site|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "id": 332,
  "links": [
    {
      "href": "https://insightvm:3780/api/3/sites/332/excluded_asset_groups",
      "rel": "self"
    }
  ]
}
```

#### Delete Site

This action is used to delete an existing site.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Site ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/sites/322",
      "rel": "self"
    }
  ]
}
```

#### Get Asset Groups

This action is used to get a list of asset groups.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string||False|Asset group name regular expression by which to filter|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asset_groups|[]asset_group|True|List of asset groups|

Example output:

```
{
  "asset_groups": [
    {
      "assets": 5,
      "description": "This is a test",
      "id": 53,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/asset_groups/53",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/asset_groups/53/tags",
          "rel": "Asset Group Tags"
        },
        {
          "href": "https://insightvm:3780/api/3/asset_groups/53/assets",
          "rel": "Asset Group Assets"
        },
        {
          "href": "https://insightvm:3780/api/3/asset_groups/53/users",
          "rel": "Asset Group Users"
        }
      ],
      "name": "Test Asset Group",
      "riskScore": 1305499,
      "searchCriteria": {
        "match": "all",
        "filters": [
          {
            "field": "host-name",
            "operator": "contains",
            "value": "meta"
          }
        ]
      },
      "type": "dynamic",
      "vulnerabilities": {
        "critical": 449,
        "moderate": 150,
        "severe": 1101,
        "total": 1700
      }
    }
  ]
}
```

#### Get Asset Group

This action is used to get an asset group by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Asset group ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asset_group|asset_group|True|Asset group|

Example output:

```
{
  "asset_group": {
    "assets": 5,
    "description": "This is a test",
    "id": 53,
    "links": [
      {
        "href": "https://insightvm:3780/api/3/asset_groups/53",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/asset_groups/53/tags",
        "rel": "Asset Group Tags"
      },
      {
        "href": "https://insightvm:3780/api/3/asset_groups/53/assets",
        "rel": "Asset Group Assets"
      },
      {
        "href": "https://insightvm:3780/api/3/asset_groups/53/users",
        "rel": "Asset Group Users"
      }
    ],
    "name": "Test Asset Group",
    "riskScore": 1305499,
    "searchCriteria": {
      "match": "all",
      "filters": [
        {
          "field": "host-name",
          "operator": "contains",
          "value": "meta"
        }
      ]
    },
    "type": "dynamic",
    "vulnerabilities": {
      "critical": 449,
      "moderate": 150,
      "severe": 1101,
      "total": 1700
    }
  }
}
```

#### Delete Asset Group

This action is used to delete an existing asset group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Asset group ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/asset_groups/20",
      "rel": "self"
    }
  ]
}
```

#### Update Asset Group Search Criteria

This action is used to update the search criteria for an existing asset group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Asset group ID|None|
|searchCriteria|object|None|True|Asset group search criteria - options documentation\: https\://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/tags/69/search_criteria",
      "rel": "self"
    }
  ]
}
```

#### Get Sites

This action is used to get a list of sites.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string||False|Site name regular expression by which to filter|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sites|[]site|True|List of sites|

Example output:

```
{
  "sites": [
    {
      "assets": 13,
      "id": 37,
      "importance": "normal",
      "lastScanTime": "2016-03-26T19:17:30.806Z",
      "links": [
        {
          "href": "https://insightvm:3780/api/3/sites/37",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/alerts",
          "rel": "Alerts"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/scan_engine",
          "rel": "Scan Engine"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/scan_schedules",
          "rel": "Schedules"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/organization",
          "rel": "Organization"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/tags",
          "rel": "Tags"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/users",
          "rel": "Users"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/scan_template",
          "rel": "Template"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/site_credentials",
          "rel": "Site Credentials"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/shared_credentials",
          "rel": "Assigned Shared Credentials"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/web_authentication/html_forms",
          "rel": "Web HTML Forms Authentication"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/web_authentication/http_headers",
          "rel": "Web HTTP Headers Authentication"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/assets",
          "rel": "Assets"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/included_targets",
          "rel": "Included Targets"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/excluded_targets",
          "rel": "Excluded Targets"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/included_asset_groups",
          "rel": "Included Asset Groups"
        },
        {
          "href": "https://insightvm:3780/api/3/sites/37/excluded_asset_groups",
          "rel": "Excluded Asset Groups"
        }
      ],
      "name": "Toronto - Discovery",
      "riskScore": 0,
      "scanEngine": 2,
      "scanTemplate": "aggressive-discovery",
      "type": "static",
      "vulnerabilities": {
        "critical": 0,
        "moderate": 0,
        "severe": 0,
        "total": 0
      }
    }
  ]
}
```

#### Get Site

This action is used to get a site by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Site ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|site|site|True|Site details|

Example output:

```
{
  "site": {
    "assets": 10,
    "id": 39,
    "importance": "normal",
    "links": [
      {
        "href": "https://insightvm:3780/api/3/sites/39",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/alerts",
        "rel": "Alerts"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/scan_engine",
        "rel": "Scan Engine"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/scan_schedules",
        "rel": "Schedules"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/organization",
        "rel": "Organization"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/tags",
        "rel": "Tags"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/users",
        "rel": "Users"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/scan_template",
        "rel": "Template"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/site_credentials",
        "rel": "Site Credentials"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/shared_credentials",
        "rel": "Assigned Shared Credentials"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/web_authentication/html_forms",
        "rel": "Web HTML Forms Authentication"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/web_authentication/http_headers",
        "rel": "Web HTTP Headers Authentication"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/assets",
        "rel": "Assets"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/included_targets",
        "rel": "Included Targets"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/excluded_targets",
        "rel": "Excluded Targets"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/included_asset_groups",
        "rel": "Included Asset Groups"
      },
      {
        "href": "https://insightvm:3780/api/3/sites/39/excluded_asset_groups",
        "rel": "Excluded Asset Groups"
      }
    ],
    "name": "Toronto - Discovery",
    "riskScore": 0,
    "scanEngine": 2,
    "scanTemplate": "aggressive-discovery",
    "type": "static",
    "vulnerabilities": {
      "critical": 0,
      "moderate": 0,
      "severe": 0,
      "total": 0
    }
  }
}
```

#### Get Vulnerabilities by CVE

This action is used to get vulnerability details associated with a CVE.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cve_id|string|None|True|Common Vulnerabilities and Exposures ID, e.g CVE-2018-12345|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|vulnerabilities|[]vulnerability|True|Vulnerability details|

Example output:

```
{
  "vulnerabilities": [
    {
      "added": "2008-10-23",
      "categories": [
        "IAVM",
        "Microsoft",
        "Microsoft Patch",
        "Microsoft Windows",
        "RPC",
        "Remote Execution"
      ],
      "cves": [
        "CVE-2008-4250"
      ],
      "cvss": {
        "links": [
          {
            "href": "https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator?vector=(AV:N/AC:L/Au:N/C:C/I:C/A:C)",
            "rel": "CVSS v2 Calculator"
          }
        ],
        "v2": {
          "accessComplexity": "L",
          "accessVector": "N",
          "authentication": "N",
          "availabilityImpact": "C",
          "confidentialityImpact": "C",
          "exploitScore": 9.9968,
          "impactScore": 10.0008,
          "integrityImpact": "C",
          "score": 10,
          "vector": "AV:N/AC:L/Au:N/C:C/I:C/A:C"
        }
      },
      "denialOfService": false,
      "description": {
        "html": "<p>This security update resolves a privately reported vulnerability in the Server service. The vulnerability could allow remote code execution if an affected system received a specially crafted RPC request. It is possible that an attacker could exploit this vulnerability without authentication to run arbitrary code. It is possible that this vulnerability could be used in the crafting of a wormable exploit. Firewall best practices and standard default firewall configurations can help protect network resources from attacks that originate outside the enterprise perimeter.</p>",
        "text": "This security update resolves a privately reported vulnerability in the Server service. The vulnerability could allow remote code execution if an affected system received a specially crafted RPC request. It is possible that an attacker could exploit this vulnerability without authentication to run arbitrary code. It is possible that this vulnerability could be used in the crafting of a wormable exploit. Firewall best practices and standard default firewall configurations can help protect network resources from attacks that originate outside the enterprise perimeter."
      },
      "exploits": 6,
      "id": "windows-hotfix-ms08-067",
      "links": [
        {
          "href": "https://insightvm:3780/api/3/vulnerabilities/windows-hotfix-ms08-067",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/vulnerabilities/windows-hotfix-ms08-067/checks",
          "rel": "Vulnerability Checks"
        },
        {
          "href": "https://insightvm:3780/api/3/vulnerabilities/windows-hotfix-ms08-067/references",
          "rel": "Vulnerability References"
        },
        {
          "href": "https://insightvm:3780/api/3/vulnerabilities/windows-hotfix-ms08-067/malware_kits",
          "rel": "Vulnerability Malware Kits"
        },
        {
          "href": "https://insightvm:3780/api/3/vulnerabilities/windows-hotfix-ms08-067/exploits",
          "rel": "Vulnerability Exploits"
        },
        {
          "href": "https://insightvm:3780/api/3/vulnerabilities/windows-hotfix-ms08-067/solutions",
          "rel": "Vulnerability Solutions"
        }
      ],
      "malwareKits": 0,
      "modified": "2018-03-21",
      "pci": {
        "adjustedCVSSScore": 10,
        "adjustedSeverityScore": 5,
        "fail": true,
        "status": "Fail"
      },
      "published": "2008-10-23",
      "riskScore": 902.24,
      "severity": "Critical",
      "severityScore": 10,
      "title": "MS08-067: Vulnerability in Server Service Could Allow Remote Code Execution (958644)"
    }
  ]
}
```

#### Get Scan Assets

This action gets assets for a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_id|integer|None|True|ID of the scan to get assets for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|[]asset|False|Assets|

Example output:

```
{
  "assets": [
    {
      "addresses": [
        {
          "ip": "10.0.0.1"
        }
      ],
      "assessedForPolicies": false,
      "assessedForVulnerabilities": true,
      "history": [
        {
          "date": "2019-04-17T00:27:42.255Z",
          "scanId": 1235,
          "type": "SCAN",
          "version": 1
        },
        {
          "date": "2019-06-17T17:05:26.236Z",
          "scanId": 2160,
          "type": "SCAN",
          "version": 2
        },
        {
          "date": "2019-06-17T18:23:42.565Z",
          "scanId": 2161,
          "type": "SCAN",
          "version": 3
        },
        {
          "date": "2019-06-17T18:31:13.270Z",
          "scanId": 2162,
          "type": "SCAN",
          "version": 4
        }
      ],
      "hostName": "hostname.us-east-2.compute.amazonaws.com",
      "hostNames": [
        {
          "name": "hostname.us-east-2.compute.amazonaws.com",
          "source": "dns"
        }
      ],
      "id": 148,
      "ip": "10.0.0.1",
      "links": [
        {
          "href": "https://insightvm:3780/api/3/assets/148",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/assets/148/software",
          "rel": "Software"
        },
        {
          "href": "https://insightvm:3780/api/3/assets/148/files",
          "rel": "Files"
        },
        {
          "href": "https://insightvm:3780/api/3/assets/148/users",
          "rel": "Users"
        },
        {
          "href": "https://insightvm:3780/api/3/assets/148/user_groups",
          "rel": "User Groups"
        },
        {
          "href": "https://insightvm:3780/api/3/assets/148/databases",
          "rel": "Databases"
        },
        {
          "href": "https://insightvm:3780/api/3/assets/148/services",
          "rel": "Services"
        },
        {
          "href": "https://insightvm:3780/api/3/assets/148/tags",
          "rel": "Tags"
        }
      ],
      "rawRiskScore": 0,
      "riskScore": 0,
      "vulnerabilities": {
        "critical": 0,
        "exploits": 0,
        "malwareKits": 0,
        "moderate": 0,
        "severe": 0,
        "total": 0
      }
    }
  ]
}
```

#### Get Scans

This action is used to get scans with optional site filter.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|False|Site ID|None|
|active|boolean|False|False|Return running scans or past scans|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scans|[]scan|True|List of scan details|

Example output:

```
{
  "scans": [
    {
      "assets": 2,
      "duration": "PT2M24.049S",
      "endTime": "2018-10-28T16:03:24.173Z",
      "engineId": 2,
      "engineName": "Local scan engine",
      "id": 189739,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/scans/189739",
          "rel": "self"
        },
        {
          "id": 2,
          "href": "https://insightvm:3780/api/3/scan_engines/2",
          "rel": "Scan Engine"
        }
      ],
      "scanName": "Sun 28 Oct 2018 09:01 AM",
      "scanType": "Scheduled",
      "startTime": "2018-10-28T16:01:00.124Z",
      "status": "finished",
      "vulnerabilities": {
        "critical": 0,
        "moderate": 0,
        "severe": 0,
        "total": 0
      },
      "siteId": 41,
      "siteName": "AWS"
    }
  ]
}
```

#### Update Scan Status

This action is used to update the status of a scan (pause, resume, stop).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Scan ID|None|
|status|string|stop|True|Status to which the scan should be set|['stop', 'resume', 'pause']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/scans/1026/stop",
      "rel": "self"
    }
  ]
}
```

#### Generate Shared Secret

This action is used to generate a shared secret for use with pairing a scan engine using the engine -> console communication direction.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|time_to_live|integer|3600|True|Time to live in seconds for the shared secret|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|shared_secret|string|True|Scan engine pairing shared secret|

Example output:

```
{
  "shared_secret": "99DB-B9F0-CD8B-5997-06BF-607B-BA21-0A81"
}
```

#### Get Scan Engines

This action is used to list scan engines paired with the security console.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|False|Optional engine name by which to filter, accepts regular expression patterns|None|
|address|string|None|False|Optional address (IP/hostname) by which to filter, accepts regular expression patterns|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_engines|[]scan_engine|True|List of scan engines details|

Example output:

```
{
  "scan_engines": [
    {
      "address": "10.0.0.24",
      "contentVersion": "1327036290 (2018-10-24)",
      "id": 4,
      "lastRefreshedDate": "2018-10-29T14:43:31.201Z",
      "lastUpdatedDate": "2018-10-24T15:10:10.291Z",
      "links": [
        {
          "href": "https://insightvm:3780/api/3/scan_engines/4",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/4/sites",
          "rel": "Sites"
        },
        {
          "id": 4,
          "href": "https://insightvm:3780/api/3/scan_engines/4/scan_engine_pools",
          "rel": "Associated Engine Pools"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/4/scans",
          "rel": "Scans"
        }
      ],
      "name": "AWS",
      "port": 40814,
      "productVersion": "2445745114 (2018-10-22)",
      "sites": [
        193,
        194,
        195,
        196,
        197,
        198,
        199
      ],
      "enginePools": [
        6
      ]
    },
    {
      "address": "10.0.0.23",
      "contentVersion": "1327036290 (2018-10-24)",
      "id": 5,
      "lastRefreshedDate": "2018-10-29T14:43:33.036Z",
      "lastUpdatedDate": "2018-10-24T15:10:10.291Z",
      "links": [
        {
          "href": "https://insightvm:3780/api/3/scan_engines/5",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/5/sites",
          "rel": "Sites"
        },
        {
          "id": 5,
          "href": "https://insightvm:3780/api/3/scan_engines/5/scan_engine_pools",
          "rel": "Associated Engine Pools"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/5/scans",
          "rel": "Scans"
        }
      ],
      "name": "Azure",
      "port": 40814,
      "productVersion": "2445745114 (2018-10-22)",
      "sites": [
        207
      ],
      "enginePools": [
        6
      ]
    },
    {
      "address": "test",
      "id": 6,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/scan_engines/6",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/6/sites",
          "rel": "Sites"
        },
        {
          "id": 6,
          "href": "https://insightvm:3780/api/3/scan_engines/6/scan_engine_pools",
          "rel": "Associated Engine Pools"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/6/scans",
          "rel": "Scans"
        }
      ],
      "name": "test",
      "port": -1,
      "enginePools": []
    },
    {
      "address": "nse.extranet.rapid7.com",
      "id": 1,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/scan_engines/1",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/1/sites",
          "rel": "Sites"
        },
        {
          "id": 1,
          "href": "https://insightvm:3780/api/3/scan_engines/1/scan_engine_pools",
          "rel": "Associated Engine Pools"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/1/scans",
          "rel": "Scans"
        }
      ],
      "name": "Rapid7 Hosted Scan Engine",
      "port": 40814,
      "sites": [
        5
      ],
      "enginePools": []
    },
    {
      "address": "127.0.0.1",
      "contentVersion": "801603722 (2018-07-11)",
      "id": 3,
      "lastUpdatedDate": "2018-07-11T09:13:04.639Z",
      "links": [
        {
          "href": "https://insightvm:3780/api/3/scan_engines/3",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/3/sites",
          "rel": "Sites"
        },
        {
          "id": 3,
          "href": "https://insightvm:3780/api/3/scan_engines/3/scan_engine_pools",
          "rel": "Associated Engine Pools"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/3/scans",
          "rel": "Scans"
        }
      ],
      "name": "Local scan engine",
      "port": 40814,
      "productVersion": "1267385905 (2018-07-11)",
      "sites": [
        256,
        1,
        257,
        258,
        259,
        260
      ],
      "enginePools": []
    }
  ]
}
```

#### Get Scan Engine

This action is used to get a scan engine by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Scan engine identifier|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_engine|scan_engine|True|Scan engine details|

Example output:

```
{
  "scan_engine": {
    "address": "10.0.0.26",
    "contentVersion": "1327036290 (2018-10-24)",
    "id": 4,
    "lastRefreshedDate": "2018-10-29T14:05:15.268Z",
    "lastUpdatedDate": "2018-10-24T15:10:10.291Z",
    "links": [
      {
        "href": "https://insightvm:3780/api/3/scan_engines/4",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/scan_engines/4/sites",
        "rel": "Sites"
      },
      {
        "id": 4,
        "href": "https://insightvm:3780/api/3/scan_engines/4/scan_engine_pools",
        "rel": "Associated Engine Pools"
      },
      {
        "href": "https://insightvm:3780/api/3/scan_engines/4/scans",
        "rel": "Scans"
      }
    ],
    "name": "master-vm-engine-1",
    "port": 40814,
    "productVersion": "2445745114 (2018-10-21)",
    "sites": [
      1,
      2
    ],
    "enginePools": [
      5
    ]
  }
}
```

#### Create Scan Engine

This action is used to create a new scan engine with console -> engine connectivity.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|Scan engine address (IP/hostname)|None|
|port|integer|40814|True|Scan engine connectivity port|None|
|name|string|None|True|Scan engine name|None|
|sites|[]integer|[]|False|List of site IDs with which to associate the engine|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|Scan engine ID|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/scan_engines",
      "rel": "self"
    },
    {
      "id": 12,
      "href": "https://insightvm:3780/api/3/scan_engines/12",
      "rel": "Scan Engine"
    }
  ],
  "id": 12
}
```

#### Delete Scan Engine

This action is used to delete an existing scan engine from the security console.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Scan engine identifier|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/scan_engines/12",
      "rel": "self"
    }
  ]
}
```

#### Get Scan Engine Pools

This action is used to retrieve a list of configured scan engine pools.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|False|Scan engine pool name by which to filter, accepts regular expression patterns|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_engine_pools|[]scan_engine_pool|True|List of scan engine pool details|

Example output:

```
{
  "scan_engine_pools": [
    {
      "engines": [
        5,
        4
      ],
      "id": 6,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/scan_engines/6",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/6/sites",
          "rel": "Sites"
        },
        {
          "id": 6,
          "href": "https://insightvm:3780/api/3/scan_engine_pools/6/engines",
          "rel": "Engine Pool Engines"
        }
      ],
      "name": "test"
    },
    {
      "id": 2,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/scan_engines/2",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/scan_engines/2/sites",
          "rel": "Sites"
        },
        {
          "id": 2,
          "href": "https://insightvm:3780/api/3/scan_engine_pools/2/engines",
          "rel": "Engine Pool Engines"
        }
      ],
      "name": "Default Engine Pool",
      "engines": []
    }
  ]
}
```

#### Get Scan Engine Pool

This action is used to retrieve scan engine pool details by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Scan engine pool identifier|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_engine_pool|scan_engine_pool|True|Scan engine pool details|

Example output:

```
{
  "scan_engine_pool": {
    "engines": [
      5,
      4
    ],
    "id": 6,
    "links": [
      {
        "href": "https://insightvm:3780/api/3/scan_engines/6",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/scan_engines/6/sites",
        "rel": "Sites"
      },
      {
        "id": 6,
        "href": "https://insightvm:3780/api/3/scan_engine_pools/6/engines",
        "rel": "Engine Pool Engines"
      }
    ],
    "name": "test"
  }
}
```

#### Create Scan Engine Pool

This action is used to create a new scan engine pool. NOTE: If you are using output from a prior step to configure
the engines assigned to the pool and that output is NOT an array, you will need to use a separate plugin
(e.g Python script) to convert the data to an array.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Scan engine pool name|None|
|engines|[]integer|None|False|List of scan engine IDs to associate with the scan engine pool|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|Scan engine pool ID|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/scan_engine_pools",
      "rel": "self"
    },
    {
      "id": 13,
      "href": "https://insightvm:3780/api/3/scan_engine_pools/13",
      "rel": "Scan Engine Pool"
    }
  ],
  "id": 13
}
```

#### Add Scan Engine Pool Engine

This action is used to add a scan engine to a scan engine pool (AWS pre-authorized engine AMI engines cannot be pooled).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pool_id|integer|None|True|Scan engine pool ID|None|
|engine_id|integer|None|True|Scan engine ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/scan_engine_pools/6/engines/5",
      "rel": "self"
    }
  ]
}
```

#### Remove Scan Engine Pool Engine

This action is used to remove a scan engine from a scan engine pool.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pool_id|integer|None|True|Scan engine pool ID|None|
|engine_id|integer|None|True|Scan engine ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/scan_engine_pools/6/engines/5",
      "rel": "self"
    }
  ]
}
```

#### Delete Scan Engine Pool

This action is used to delete an existing scan engine pool from the security console.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Scan engine pool identifier|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/scan_engine_pools/13",
      "rel": "self"
    }
  ]
}
```

#### Update Site Scan Engine

This action is used to update the scan engine/scan engine pool associated with a site.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|site_id|integer|None|True|Identifier of the site to update|None|
|engine_id|integer|None|True|Identifier of the scan engine/scan engine pool to associate with the site|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/sites/272/scan_engine",
      "rel": "self"
    }
  ]
}
```

#### Create Vulnerability Exception Submission

This action is used to create a vulnerability exception submission.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|Exception created with InsightConnect|True|Comment to include in the vulnerability exception submission|None|
|expiration|date|None|False|The date the vulnerability exception expires|None|
|key|string|None|False|The key to identify a specific instance if the type is Instance|None|
|port|integer|None|False|The port the vulnerability appears on if the type is Instance|None|
|reason|string|None|True|Reason for the exception|['False Positive', 'Compensating Control', 'Acceptable Use', 'Acceptable Risk', 'Other']|
|scope|integer|None|False|The ID of the scope the vulnerability exception applies to.  May be empty if type is Global|None|
|type|string|None|True|The type of vulnerability exception to create|['Global', 'Site', 'Asset', 'Asset Group', 'Instance']|
|vulnerability|string|None|True|The vulnerability this exception applies to|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|The vulnerability exception that was created|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "id": 35,
  "links": [
    {
      "href": "https://insightvm:3780/api/3/vulnerability_exceptions",
      "rel": "self"
    },
    {
      "href": "https://insightvm:3780/api/3/vulnerability_exceptions/35",
      "id": 35,
      "rel": "Vulenrability Exception"
    }
  ]
}
```

#### Delete Vulnerability Exception

This action is used to delete an existing vulnerability exception.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|exception_id|integer|None|True|Vulnerability Exception ID to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/vulnerability_exceptions/32",
      "rel": "self"
    }
  ]
}
```

#### Get Vulnerability Details

This action is used to get the details of a specific vulnerability by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|The identifier of the vulnerability to retrieve from InsightVM|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|vulnerability|vulnerability|True|The details of the vulnerability requested|

Example output:

```
{
  "vulnerability": {
    "added": "2012-02-06",
    "categories": [
      "Apple",
      "Apple iTunes",
      "Obsolete Software"
    ],
    "cvss": {
      "links": [
        {
          "href": "https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator?vector=(AV:N/AC:L/Au:N/C:C/I:C/A:C)",
          "rel": "CVSS v2 Calculator"
        }
      ],
      "v2": {
        "accessComplexity": "L",
        "accessVector": "N",
        "authentication": "N",
        "availabilityImpact": "C",
        "confidentialityImpact": "C",
        "exploitScore": 9.9968,
        "impactScore": 10.0008,
        "integrityImpact": "C",
        "score": 10,
        "vector": "AV:N/AC:L/Au:N/C:C/I:C/A:C"
      }
    },
    "denialOfService": false,
    "description": {
      "html": "\u003cp\u003e\n        Apple only maintains one major version of iTunes.  Versions prior to\n        this are not supported. Unsupported versions of iTunes may contain\n        unpatched security flaws. It is recommended to upgrade to the latest\n        version.\n     \u003c/p\u003e",
      "text": "Apple only maintains one major version of iTunes. Versions prior to this are not supported. Unsupported versions of iTunes may contain unpatched security flaws. It is recommended to upgrade to the latest version."
    },
    "exploits": 0,
    "id": "apple-itunes-obsolete",
    "links": [
      {
        "href": "https://insightvm:3780/api/3/vulnerabilities/apple-itunes-obsolete",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/vulnerabilities/apple-itunes-obsolete/checks",
        "rel": "Vulnerability Checks"
      },
      {
        "href": "https://insightvm:3780/api/3/vulnerabilities/apple-itunes-obsolete/references",
        "rel": "Vulnerability References"
      },
      {
        "href": "https://insightvm:3780/api/3/vulnerabilities/apple-itunes-obsolete/malware_kits",
        "rel": "Vulnerability Malware Kits"
      },
      {
        "href": "https://insightvm:3780/api/3/vulnerabilities/apple-itunes-obsolete/exploits",
        "rel": "Vulnerability Exploits"
      },
      {
        "href": "https://insightvm:3780/api/3/vulnerabilities/apple-itunes-obsolete/solutions",
        "rel": "Vulnerability Solutions"
      }
    ],
    "malwareKits": 0,
    "modified": "2013-05-03",
    "pci": {
      "adjustedCVSSScore": 10,
      "adjustedSeverityScore": 5,
      "fail": true,
      "status": "Fail"
    },
    "published": "2001-01-09",
    "riskScore": 911.25,
    "severity": "Critical",
    "severityScore": 10,
    "title": "Obsolete version of Apple iTunes"
  }
}
```

#### Review Vulnerability Exception

This action is used to approve or reject a vulnerability exception.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|Comment to include in the review|None|
|exception|integer|None|True|The Vulnerability Exception ID to Approve or Reject|None|
|review|string|None|True|Approval or Rejection of the exception|['Approved', 'Rejected']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/vulnerability_exceptions/35/approve",
      "rel": "self"
    }
  ]
}
```

#### Get Authentication Sources

This action is used to list authentication sources available for InsightVM users.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|False|Authentication source name by which to filter, accepts regular expression patterns|None|
|type|string||False|Authentication source type by which to filter|['', 'admin', 'kerberos', 'ldap', 'normal', 'saml']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|authentication_sources|[]authentication_source|True|List of authentication sources|

Example output:

```
{
  "authentication_sources": [
    {
      "external": true,
      "id": 5,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/authentication_sources/5",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/authentication_sources/5/users",
          "rel": "Authentication Source Users"
        }
      ],
      "name": "OpenLDAP",
      "type": "ldap"
    }
  ]
}
```

#### Get Authentication Source

This action is used to get the details for an authentication source.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|Authentication source ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|authentication_source|authentication_source|True|User authentication source|

Example output:

```
{
  "authentication_source": {
    "external": false,
    "id": 1,
    "links": [
      {
        "href": "https://insightvm:3780/api/3/authentication_sources/1",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/authentication_sources/1/users",
        "rel": "Authentication Source Users"
      }
    ],
    "name": "Builtin Administrators",
    "type": "admin"
  }
}
```

#### Get Roles

This action is used to list role details.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|False|Role name by which to filter, accepts regular expression patterns|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|roles|[]role|True|List of roles|

Example output:

```
{
  "roles": [
    {
      "description": "Custom defined role.",
      "id": "custom",
      "links": [
        {
          "href": "https://insightvm:3780/api/3/roles/custom",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/roles/custom/users",
          "rel": "Users"
        }
      ],
      "name": "Custom",
      "privileges": []
    },
    {
      "description": "site-admin-custom",
      "id": "Site Admin Custom",
      "links": [
        {
          "href": "https://insightvm:3780/api/3/roles/Site%20Admin%20Custom",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/roles/Site%20Admin%20Custom/users",
          "rel": "Users"
        }
      ],
      "name": "Site Admin Custom",
      "privileges": [
        "approve-vulnerability-exceptions",
        "assign-scan-engine",
        "assign-scan-template",
        "assign-ticket-assignee",
        "close-tickets",
        "configure-global-settings",
        "create-reports",
        "create-tickets",
        "delete-vulnerability-exceptions",
        "manage-asset-group-access",
        "manage-asset-group-assets",
        "manage-dynamic-asset-groups",
        "manage-policies",
        "manage-report-access",
        "manage-report-templates",
        "manage-scan-alerts",
        "manage-scan-engines",
        "manage-scan-templates",
        "manage-site-access",
        "manage-site-credentials",
        "manage-sites",
        "manage-static-asset-groups",
        "manage-tags",
        "purge-site-asset-data",
        "schedule-automatic-scans",
        "specify-scan-targets",
        "specify-site-metadata",
        "start-unscheduled-scans",
        "submit-vulnerability-exceptions",
        "use-restricted-report-sections",
        "view-asset-group-asset-data",
        "view-site-asset-data"
      ]
    }
  ]
}
```

#### Get Role

This action is used to get role details by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|Role ID, e.g 'global-admin'|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|role|role|True|Role details|

Example output:

```
{
  "role": {
    "description": "Manage configuration, maintenance, and diagnostic operations for the Security Console. Manage site, scan, and report operations, manage shared scan credentials, create tickets, and view asset data in accessible sites and asset groups. Manage vConnections.",
    "id": "global-admin",
    "links": [
      {
        "href": "https://insightvm:3780/api/3/roles/global-admin",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/roles/global-admin/users",
        "rel": "Users"
      }
    ],
    "name": "Global Administrator",
    "privileges": [
      "all-permissions",
      "approve-vulnerability-exceptions",
      "assign-scan-engine",
      "assign-scan-template",
      "assign-ticket-assignee",
      "close-tickets",
      "configure-global-settings",
      "create-reports",
      "create-tickets",
      "delete-vulnerability-exceptions",
      "manage-asset-group-access",
      "manage-asset-group-assets",
      "manage-dynamic-asset-groups",
      "manage-policies",
      "manage-report-access",
      "manage-report-templates",
      "manage-scan-alerts",
      "manage-scan-engines",
      "manage-scan-templates",
      "manage-site-access",
      "manage-site-credentials",
      "manage-sites",
      "manage-static-asset-groups",
      "manage-tags",
      "purge-site-asset-data",
      "schedule-automatic-scans",
      "specify-scan-targets",
      "specify-site-metadata",
      "start-unscheduled-scans",
      "submit-vulnerability-exceptions",
      "use-restricted-report-sections",
      "view-asset-group-asset-data",
      "view-site-asset-data"
    ]
  }
}
```

#### Get Users

This action is used to list user accounts.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|False|User account name by which to filter, accepts regular expression patterns|None|
|login|string|None|False|User account login name by which to filter, accepts regular expression patterns|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]user_account|True|List of user account details|

Example output:

```
{
  "users": [
    {
      "authentication": {
        "external": false,
        "id": 1,
        "links": [
          {
            "href": "https://insightvm:3780/api/3/authentication_sources/1",
            "rel": "self"
          },
          {
            "href": "https://insightvm:3780/api/3/authentication_sources/1/users",
            "rel": "Authentication Source Users"
          }
        ],
        "name": "Builtin Administrators",
        "type": "admin"
      },
      "email": "blaah@example.com",
      "enabled": true,
      "id": 1,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/users/1",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/authentication_sources/1",
          "rel": "Authentication Source"
        },
        {
          "href": "https://insightvm:3780/api/3/users/1/asset_groups",
          "rel": "Asset Groups"
        },
        {
          "href": "https://insightvm:3780/api/3/users/1/sites",
          "rel": "Sites"
        },
        {
          "href": "https://insightvm:3780/api/3/users/1/privileges",
          "rel": "Privileges"
        },
        {
          "href": "https://insightvm:3780/api/3/roles/global-admin",
          "rel": "Role"
        }
      ],
      "locale": {
        "default": "en-US",
        "reports": "en-US"
      },
      "locked": false,
      "login": "blaah",
      "name": "blaah",
      "role": {
        "allAssetGroups": true,
        "allSites": true,
        "id": "global-admin",
        "name": "Global Administrator",
        "privileges": [
          "all-permissions",
          "approve-vulnerability-exceptions",
          "assign-scan-engine",
          "assign-scan-template",
          "assign-ticket-assignee",
          "close-tickets",
          "configure-global-settings",
          "create-reports",
          "create-tickets",
          "delete-vulnerability-exceptions",
          "manage-asset-group-access",
          "manage-asset-group-assets",
          "manage-dynamic-asset-groups",
          "manage-policies",
          "manage-report-access",
          "manage-report-templates",
          "manage-scan-alerts",
          "manage-scan-engines",
          "manage-scan-templates",
          "manage-site-access",
          "manage-site-credentials",
          "manage-sites",
          "manage-static-asset-groups",
          "manage-tags",
          "purge-site-asset-data",
          "schedule-automatic-scans",
          "specify-scan-targets",
          "specify-site-metadata",
          "start-unscheduled-scans",
          "submit-vulnerability-exceptions",
          "use-restricted-report-sections",
          "view-asset-group-asset-data",
          "view-site-asset-data"
        ],
        "superuser": true
      }
    }
  ]
}
```

#### Get User

This action is used to get user account details by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|User account ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|user_account|True|User account details|

Example output:

```
{
  "user": {
    "authentication": {
      "external": false,
      "id": 1,
      "links": [
        {
          "href": "https://insightvm:3780/api/3/authentication_sources/1",
          "rel": "self"
        },
        {
          "href": "https://insightvm:3780/api/3/authentication_sources/1/users",
          "rel": "Authentication Source Users"
        }
      ],
      "name": "Builtin Administrators",
      "type": "admin"
    },
    "email": "blaah@example.com",
    "enabled": true,
    "id": 1,
    "links": [
      {
        "href": "https://insightvm:3780/api/3/users/1",
        "rel": "self"
      },
      {
        "href": "https://insightvm:3780/api/3/authentication_sources/1",
        "rel": "Authentication Source"
      },
      {
        "href": "https://insightvm:3780/api/3/users/1/asset_groups",
        "rel": "Asset Groups"
      },
      {
        "href": "https://insightvm:3780/api/3/users/1/sites",
        "rel": "Sites"
      },
      {
        "href": "https://insightvm:3780/api/3/users/1/privileges",
        "rel": "Privileges"
      },
      {
        "href": "https://insightvm:3780/api/3/roles/global-admin",
        "rel": "Role"
      }
    ],
    "locale": {
      "default": "en-US",
      "reports": "en-US"
    },
    "locked": false,
    "login": "blaah",
    "name": "blaah",
    "role": {
      "allAssetGroups": true,
      "allSites": true,
      "id": "global-admin",
      "name": "Global Administrator",
      "privileges": [
        "all-permissions",
        "approve-vulnerability-exceptions",
        "assign-scan-engine",
        "assign-scan-template",
        "assign-ticket-assignee",
        "close-tickets",
        "configure-global-settings",
        "create-reports",
        "create-tickets",
        "delete-vulnerability-exceptions",
        "manage-asset-group-access",
        "manage-asset-group-assets",
        "manage-dynamic-asset-groups",
        "manage-policies",
        "manage-report-access",
        "manage-report-templates",
        "manage-scan-alerts",
        "manage-scan-engines",
        "manage-scan-templates",
        "manage-site-access",
        "manage-site-credentials",
        "manage-sites",
        "manage-static-asset-groups",
        "manage-tags",
        "purge-site-asset-data",
        "schedule-automatic-scans",
        "specify-scan-targets",
        "specify-site-metadata",
        "start-unscheduled-scans",
        "submit-vulnerability-exceptions",
        "use-restricted-report-sections",
        "view-asset-group-asset-data",
        "view-site-asset-data"
      ],
      "superuser": true
    }
  }
}
```

#### Create User

This action is used to create a new user account (limited to external authentication sources).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|authentication_id|integer|None|False|The identifier of the authentication source to use to authenticate the user. The source with the specified identifier must be of the type specified by Authentication Type. If Authentication ID is omitted, then one source of the specified Authentication Type is selected|None|
|authentication_type|string|ldap|True|The type of the authentication source to use to authenticate the user|['kerberos', 'ldap', 'saml']|
|email|string|None|True|The email address of the user|None|
|enabled|boolean|True|True|Whether the user account is enabled|None|
|login|string|None|True|The login name of the user|None|
|name|string|None|True|The full name of the user|None|
|access_all_asset_groups|boolean|False|True|Whether to grant the user access to all asset groups|None|
|access_all_sites|boolean|False|True|Whether to grant the user access to all sites|None|
|role_id|string|None|True|The identifier of the role to which the user should be assigned, e.g 'global-admin'|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|
|id|integer|True|The identifier of the created user account|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users",
      "rel": "self"
    },
    {
      "href": "https://insightvm:3780/api/3/users/83",
      "rel": "self"
    }
  ],
  "id": 83
}
```

#### Update User

This action is used to update the configuration of an existing user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|The identifier of the user|None|
|authentication_id|integer|None|False|The identifier of the authentication source to use to authenticate the user. The source with the specified identifier must be of the type specified by Authentication Type. If Authentication ID is omitted, then one source of the specified Authentication Type is selected|None|
|authentication_type|string|ldap|True|The type of the authentication source to use to authenticate the user|['normal', 'admin', 'kerberos', 'ldap', 'saml']|
|email|string|None|True|The email address of the user|None|
|enabled|boolean|True|True|Whether the user account is enabled|None|
|login|string|None|True|The login name of the user|None|
|name|string|None|True|The full name of the user|None|
|access_all_asset_groups|boolean|False|True|Whether to grant the user access to all asset groups|None|
|access_all_sites|boolean|False|True|Whether to grant the user access to all sites|None|
|role_id|string|None|True|The identifier of the role to which the user should be assigned, e.g 'global-admin'|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83",
      "rel": "self"
    }
  ]
}
```

#### Delete User

This action is used to delete an user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|The identifier of the user account|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83",
      "rel": "self"
    }
  ]
}
```

#### Disable User

This action is used to disable an user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|The identifier of the user account|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83",
      "rel": "self"
    }
  ]
}
```

#### Enable User

This action is used to enable an user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|integer|None|True|The identifier of the user account|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83",
      "rel": "self"
    }
  ]
}
```

#### Update User Role

This action is used to update the role associated with an user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|integer|None|True|The identifier of the user account|None|
|access_all_asset_groups|boolean|False|True|Whether to grant the user access to all asset groups|None|
|access_all_sites|boolean|False|True|Whether to grant the user access to all sites|None|
|role_id|string|None|True|The identifier of the role to which the user should be assigned, e.g 'global-admin'|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83",
      "rel": "self"
    }
  ]
}
```

#### Update User Asset Group Access

This action is used to update the asset groups to which a user has access in bulk. It can be used to remove asset group access as well.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|integer|None|True|The identifier of the user account|None|
|asset_group_ids|[]integer|None|True|The identifiers of the asset groups to which the user account should be granted access, ignored if the user has access to all asset groups|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83/sites",
      "rel": "User Asset Groups"
    }
  ]
}
```

#### Add User Asset Group Access

This action is used to grant an user account access to an asset group by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|integer|None|True|The identifier of the user account|None|
|asset_group_id|integer|None|True|The identifier of the asset group|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83/sites",
      "rel": "User Asset Groups"
    }
  ]
}
```

#### Remove User Asset Group Access

This action is used to remove asset group access from an user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|integer|None|True|The identifier of the user account|None|
|asset_group_id|integer|None|True|The identifier of the asset group|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83/sites",
      "rel": "User Asset Groups"
    }
  ]
}
```

#### Update User Site Access

This action is used to update the sites to which a user has access in bulk. It can be used to remove sites as well.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|integer|None|True|The identifier of the user account|None|
|site_ids|[]integer|None|True|The identifiers of the sites to which the user account should be granted access, ignored if the user has access to all sites|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83/sites",
      "rel": "User Sites"
    }
  ]
}
```

#### Add User Site Access

This action is used to grant an user account access to a site by id.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|integer|None|True|The identifier of the user account|None|
|site_id|integer|None|True|The identifier of the site|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83/sites",
      "rel": "User Sites"
    }
  ]
}
```

#### Remove User Site Access

This action is used to remove site access from an user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|integer|None|True|The identifier of the user account|None|
|site_id|integer|None|True|The identifier of the site|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|True|Hypermedia links to corresponding or related resources|

Example output:

```
{
  "links": [
    {
      "href": "https://insightvm:3780/api/3/users/83/sites",
      "rel": "User Sites"
    }
  ]
}
```

#### Top Remediations

This action is used to generate results for the top remediations based on a defined scope.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|asset_limit|integer|None|False|The amount of assets to be returned with each top remediation; this can be used to reduce message size and processing time|None|
|limit|integer|25|True|Number of remediations for which tickets should be generated|[10, 25, 50, 100]|
|scope|string|none|True|Scope context for generated report; if set remediations will be scoped by each in scope ID, e.g Site ID, Tag ID, Asset Group ID|['none', 'assets', 'assetGroups', 'sites', 'tags', 'scan']|
|scope_ids|[]integer|[]|False|Scope IDs for which tickets should be generated, by default all are included|None|
|vulnerability_limit|integer|None|False|The amount of vulnerabilities to be returned with each top remediation; this can be used to reduce message size and processing time|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|remediations|[]remediation|True|List of top remediations|

Example output:

```
{
  "remediations": [
    {
      "solutionId": 50460,
      "nexposeId": "mozilla-firefox-upgrade-latest",
      "summary": "Upgrade to the latest version of Mozilla Firefox",
      "fix": "Install the latest version of Mozilla Firefox from the Mozilla Products (http://www.mozilla.org/products/firefox/) page.",
      "assetCount": 1,
      "vulnerabilityCount": 689,
      "riskScore": 595588,
      "assets": [
        {
          "id": 44,
          "hostName": "hostname",
          "ip": "10.0.0.1",
          "mac": "00:00:00:00:00:00",
          "os": "Windows Server 2012 R2 Standard Edition",
          "riskScore": 2116158,
          "criticalityTag": "Very High"
        }
      ],
      "vulnerabilities": [
        {
          "id": 73213,
          "title": "Obsolete Version of Mozilla Firefox",
          "description": "\n    \n<p>\n      Versions of Mozilla Firefox prior to 57.0.x are no longer supported. Unsupported\n      versions of Firefox may contain unpatched security flaws. It is recommended to \n      upgrade to the latest version.\n    </p>\n  ",
          "cvssScore": "10",
          "severity": 10,
          "riskScore": 871
        }
      ]
    }
  ]
}
```

### Triggers

#### New Vulnerability Exception Activity

This trigger is used to check for new InsightVM vulnerability exception activity.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|frequency|integer|5|True|How often the trigger should check for new vulnerability exception requests|None|
|status_filter|[]string|['Under Review']|False|List of vulnerabiliti statuses to match for trigger; options include: Under Review, Approved, Rejected, Expired, Deleted|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|exception|vulnerability_exception|False|InsightVM Vulnerability Exception|

Example output:

```
{
  "expires": "2019-10-31T00:00:00Z",
  "id": 31,
  "links": [
    {
      "href": "https://insightvm:3780/api/3/vulnerability_exceptions/31",
      "rel": "self"
    }
  ],
  "scope": {
    "id": 80,
    "links": [
      {
        "id": "apple-itunes-obsolete",
        "href": "https://insightvm:3780/api/3/vulnerabilities/apple-itunes-obsolete",
        "rel": "Vulnerability"
      },
      {
        "id": 80,
        "href": "https://insightvm:3780/api/3/assets/80",
        "rel": "Asset"
      }
    ],
    "type": "asset",
    "vulnerability": "apple-itunes-obsolete"
  },
  "state": "under review",
  "submit": {
    "comment": "ICON Test Exception",
    "date": "2019-10-27T14:59:31.449114Z",
    "links": [
      {
        "id": 5,
        "href": "https://insightvm:3780/api/3/users/5",
        "rel": "Submitter"
      }
    ],
    "name": "blaah",
    "reason": "acceptable use",
    "user": 5
  }
}
```

#### New Scans

This trigger is used to check for new InsightVM scans by site and scan status.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|frequency|integer|5|True|How often the trigger should check for new scans in minutes|None|
|most_recent_scan|boolean|True|True|Only process the most recent scan for a site since the last time the trigger was run|None|
|site_name_filter|string|.*|True|Regular expression to match sites where new scans should be triggered|None|
|status_filter|[]string|['Successful']|False|List of scan statuses to match for trigger; options include: Aborted, Successful, Running, Stopped, Failed, Paused, Unknown|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan|scan|False|InsightVM Scan|

Example output:

```
{
  "scan": {
    "assets": 2,
    "duration": "PT1M30.77S",
    "endTime": "2019-06-17T19:23:50.927Z",
    "engineName": "Local scan engine",
    "id": 2163,
    "links": [
      {
        "href": "https://insightvm:3780/api/3/scans/2163",
        "rel": "self"
      }
    ],
    "scanName": "Mon 17 Jun 2019 03:22 PM",
    "scanType": "Manual",
    "startTime": "2019-06-17T19:22:20.157Z",
    "status": "finished",
    "vulnerabilities": {
      "critical": 0,
      "moderate": 0,
      "severe": 0,
      "total": 0
    },
    "siteId": 31,
    "siteName": "Test-Site"
  }
}
```

### Custom Output Types

#### report_id

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|Identifer|
|name|string|False|Name of report|

#### link

|Name|Type|Required|Description|
|----|----|--------|-----------|
|href|string|False|A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)|
|rel|string|False|Link relation type following RFC 5988|

#### address

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip|string|False|IPv4 or IPv6 address|
|mac|string|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|

#### configuration

|Name|Type|Required|Description|
|----|----|--------|-----------|
|name|string|False|Name of the configuration value|
|value|string|False|Configuration value|

#### database

|Name|Type|Required|Description|
|----|----|--------|-----------|
|description|string|False|Description of the database instance|
|id|integer|False|Identifier of the database|
|name|string|False|Name of the database instance|

#### file

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attributes|[]configuration|False|Attributes detected on the file|
|name|string|False|Name of the file|
|size|integer|False|Size of the regular file (in bytes). If the file is a directory, no value is returned|
|type|string|False|Type of the file, e.g. file or directory|

#### history

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|string|False|Date the asset information was collected or changed|
|description|string|False|Additional information describing the change|
|scanId|integer|False|If a scan-oriented change, the identifier of the corresponding scan the asset was scanned in|
|type|string|False|Type, for additional information see the help section of this plugin|
|user|string|False|User|
|version|integer|False|Version|
|vulnerabilityExceptionId|integer|False|Vulnerability exception ID|

#### hostName

|Name|Type|Required|Description|
|----|----|--------|-----------|
|name|string|False|Name|
|source|string|False|Source|

#### id

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|ID|
|source|string|False|Source|

#### cpe

|Name|Type|Required|Description|
|----|----|--------|-----------|
|edition|string|False|Edition-related terms applied by the vendor to the product|
|language|string|False|Defines the language supported in the user interface of the product being described. The format of the language tag adheres to RFC 5646|
|other|string|False|Captures any other general descriptive or identifying information which is vendor- or product-specific and which does not logically fit in any other attribute value|
|part|string|False|A single letter code that designates the particular platform part that is being identified|
|product|string|False|Most common and recognizable title or name of the product|
|swEdition|string|False|Characterizes how the product is tailored to a particular market or class of end users|
|targetHW|string|False|Characterize the instruction set architecture on which the product operates|
|targetSW|string|False|Characterizes the software computing environment within which the product operates|
|update|string|False|Vendor-specific alphanumeric strings characterizing the particular update, service pack, or point release of the product|
|v2.2|string|False|The full CPE string in the CPE 2.2 format|
|v2.3|string|False|The full CPE string in the CPE 2.3 format|
|vendor|string|False|The person or organization that manufactured or created the product|
|version|string|False|Vendor-specific alphanumeric strings characterizing the particular release version of the product|

#### osFingerprint

|Name|Type|Required|Description|
|----|----|--------|-----------|
|architecture|string|False|The architecture of the operating system|
|configurations|[]configuration|False|Configuration key-values pairs enumerated on the operating system|
|cpe|cpe|False|Common Platform Enumeration|
|description|string|False|The description of the operating system (containing vendor, family, product, version and architecture in a single string)|
|family|string|False|Family of the operating system|
|id|integer|False|Identifier of the operating system|
|product|string|False|Name of the operating system|
|systemName|string|False|A combination of vendor and family (with redundancies removed), suitable for grouping|
|type|string|False|Type of operating system|
|vendor|string|False|Vendor of the operating system|
|version|string|False|Version of the operating system|

#### userGroup

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|Identifier of the user group|
|name|string|False|Name of the user group|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|fullName|string|False|Full name of the user account|
|id|integer|False|Identifier of the user account|
|name|string|False|Name of the user account|

#### page

|Name|Type|Required|Description|
|----|----|--------|-----------|
|linkType|string|False|Type of link used to traverse or detect the page|
|path|string|False|Path to the page (URI)|
|response|integer|False|HTTP response code observed with retrieving the page|

#### webApplication

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|Identifier of the web application|
|pages|[]page|False|Pages|
|root|string|False|Web root of the web application|
|virtualHost|string|False|Virtual host of the web application|

#### service

|Name|Type|Required|Description|
|----|----|--------|-----------|
|configurations|[]configuration|False|Configuration key-values pairs enumerated on the service|
|databases|[]database|False|Databases enumerated on the service|
|family|string|False|Family of the service|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|name|string|False|Name of the service|
|port|integer|False|Port of the service|
|product|string|False|Product running the service|
|protocol|string|False|Protocol of the service|
|userGroups|[]userGroup|False|User groups|
|users|[]user|False|Users|
|vendor|string|False|Vendor of the service|
|version|string|False|Version of the service|
|webApplications|[]webApplication|False|Web applications found on the service|

#### software

|Name|Type|Required|Description|
|----|----|--------|-----------|
|configurations|[]configuration|False|Configurations|
|cpe|cpe|False|CPE|
|description|string|False|Description of the software|
|family|string|False|Family of the software|
|id|integer|False|ID|
|product|string|False|Product of the software|
|type|string|False|Type of the software|
|vendor|string|False|Vendor of the software|
|version|string|False|Version of the software|

#### vulnerabilities

|Name|Type|Required|Description|
|----|----|--------|-----------|
|critical|integer|False|Number of critical vulnerabilities|
|exploits|integer|False|Number of distinct exploits that can exploit any of the vulnerabilities on the asset|
|malwareKits|integer|False|Number of distinct malware kits that vulnerabilities on the asset are susceptible to|
|moderate|integer|False|Number of moderate vulnerabilities|
|severe|integer|False|Number of severe vulnerabilities|
|total|integer|False|Total number of vulnerabilities|

#### vulnerabilities_count

|Name|Type|Required|Description|
|----|----|--------|-----------|
|critical|integer|False|Number of critical vulnerabilities|
|moderate|integer|False|Number of moderate vulnerabilities|
|severe|integer|False|Number of severe vulnerabilities|
|total|integer|False|Total|

#### vulnerability_exception

|Name|Type|Required|Description|
|----|----|--------|-----------|
|expires|date|False|The date and time the vulnerability exception is set to expire|
|id|integer|True|The ID uniquely identifying the vulnerability exception|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|review|object|False|Details of the exception review|
|scope|object|True|Details of the scope of the exception|
|state|string|True|The state of the vulnerability exception|
|submit|object|True|Details of the exception submission|

#### exception_review

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comment|string|False|The comment from the reviewer detailing the review|
|date|date|False|The date and time the review took place|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|name|string|False|The login name of the user that reviewed the vulnerability exception|
|user|integer|False|The identifier of the user that reviewed the vulnerability exception|

#### exception_submit

|Name|Type|Required|Description|
|----|----|--------|-----------|
|comment|string|False|The comment from the submit detailing the exception|
|date|date|False|The date and time the exception request took place|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|name|string|False|The login name of the user that submitted the vulnerability exception|
|user|integer|False|The identifier of the user that submitted the vulnerability exception|

#### exception_scope

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|The identifer of the scope (asset, group, site) the vulnerability exception applies to|
|key|string|False|Optional key to discriminate the instance when the scope type is Instance|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|port|integer|False|If the scope type is Instance, the port the exception applies to|
|type|string|True|The type of vulnerability exception - Global, Site, Asset, Asset Group, Instance|
|vulnerability|string|True|The vulnerability the exception applies to|

#### asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|addresses|[]address|False|All addresses discovered on the asset|
|assessedForPolicies|boolean|False|Whether the asset has been assessed for policies at least once|
|assessedForVulnerabilities|boolean|False|Whether the asset has been assessed for vulnerabilities at least once|
|configurations|[]configuration|False|Configuration key-values pairs enumerated on the asset|
|databases|[]database|False|Databases enumerated on the asset|
|files|[]file|False|Files discovered with searching on the asset|
|history|[]history|False|History of changes to the asset over time|
|hostName|string|False|Primary host name (local or FQDN) of the asset|
|hostNames|[]hostName|False|All hostnames or aliases discovered on the asset|
|id|integer|False|Identifier of the asset|
|ids|[]id|False|Unique identifiers found on the asset, such as hardware or operating system identifiers|
|ip|string|False|Primary IPv4 or IPv6 address of the asset|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|mac|string|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|
|os|string|False|Full description of the operating system of the asset|
|osFingerprint|osFingerprint|False|Details of the operating system of the asset|
|rawRiskScore|float|False|Base risk score of the asset|
|riskScore|float|False|Risk score (with criticality adjustments) of the asset|
|services|[]service|False|Services discovered on the asset|
|software|[]software|False|Software discovered on the asset|
|type|string|False|Type of asset e.g. unknown, guest, hypervisor, physical, mobile|
|userGroups|[]userGroup|False|User group accounts enumerated on the asset|
|users|[]user|False|User accounts enumerated on the asset|
|vulnerabilities|vulnerabilities|False| Summary information for vulnerabilities on the asset|

#### asset_vulnerability_result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|checkId|string|False|Check ID, ie. ssh-openssh-x11uselocalhost-x11-forwarding-session-hijack|
|exceptions|[]integer|False|If the result is vulnerable with exceptions applied, the identifier(s) of the exceptions actively applied to the result|
|key|string|False|An additional discriminating key used to uniquely identify between multiple instances of results on the same finding|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|port|integer|False|Port of the service the result was discovered on e.g. 22|
|proof|string|False|Proof of the vulnerability, ie. <p><p>OpenBSD OpenSSH 4.3 on Linux</p></p>|
|protocol|string|False|Protocol of the service the result was discovered on, ie. TCP|
|status|string|False|Status of the vulnerability check result, ie. vulnerable-version|

#### asset_vulnerability

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|Vulnerability ID, ie. ssh-openssh-x11uselocalhost-x11-forwarding-session-hijack|
|instances|integer|False|Identifier of the report instance|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|results|[]asset_vulnerability_result|False|The vulnerability check results for the finding. Multiple instances may be present if one or more checks fired, or a check has multiple independent results|
|status|string|False|Status, ie. vulnerable|

#### site

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|integer|True|Site asset count|
|connectionType|string|False|Site discovery connection type (if applicable)|
|description|string|False|Site description|
|id|integer|True|Identifier of the site|
|importance|string|True|Site importance, used with the 'weighted' risk scoring strategy|
|lastScanTime|date|False|Site last scan time|
|links|[]link|True|Hypermedia links to corresponding or related resources|
|name|string|True|Site name|
|riskScore|float|True|Site risk score|
|scanEngine|integer|True|Site default scan engine ID|
|scanTemplate|string|True|Site default scan template|
|type|string|True|Site type|
|vulnerabilities|vulnerabilities_count|True|Site vulnerability counts|

#### asset_group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|integer|True|Site asset count|
|description|string|False|Asset group description|
|id|integer|True|Site ID|
|links|[]link|True|Hypermedia links to corresponding or related resources|
|name|string|True|Asset group name|
|riskScore|float|True|Site risk score|
|searchCriteria|object|False|Asset group search criteria|
|type|string|True|Asset group type|
|vulnerabilities|vulnerabilities_count|True|Asset group vulnerability counts|

#### vulnerability_description

|Name|Type|Required|Description|
|----|----|--------|-----------|
|html|string|False|Vulnerability description HTML|
|text|string|False|Vulnerability description raw text|

#### pci

|Name|Type|Required|Description|
|----|----|--------|-----------|
|adjustedCVSSScore|integer|False|PCI adjusted CVSS score|
|adjustedSeverityScore|integer|False|PCI adjusted severity score|
|fail|boolean|False|Whether this vulnerability results in a PCI assessment failure|
|specialNotes|string|False|PCI special notes|
|status|string|False|PCI status|

#### cvss_v2

|Name|Type|Required|Description|
|----|----|--------|-----------|
|accessComplexity|string|False|CVSSv2 access complexity metric|
|accessVector|string|False|CVSSv2 access vector metric|
|authentication|string|False|CVSSv2 authentication metric|
|availabilityImpact|string|False|CVSSv2 availability impact metric|
|confidentialityImpact|string|False|CVSSv2 confidentiality impact metric|
|exploitScore|float|False|CVSSv2 combined exploit metric score (Access Complexity/Access Vector/Authentication)|
|impactScore|float|False|CVSSv2 combined impact metric score (Confidentiality/Integrity/Availability)|
|integrityImpact|string|False|CVSSv2 integrity impact metric|
|score|float|False|CVSSv2 score|
|vector|string|False|CVSSv2 combined vector string|

#### cvss_v3

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attackComplexity|string|False|CVSSv3 attack complexity metric|
|attackVector|string|False|CVSSv3 attack vector metric|
|availabilityImpact|string|False|CVSSv3 availability impact metric|
|confidentialityImpact|string|False|CVSSv3 confidentiality impact metric|
|exploitScore|float|False|CVSSv3 combined exploit metric score (Attack Complexity/Attack Vector/Privilege Required/Scope/User Interaction)|
|impactScore|float|False|CVSSv3 combined impact metric score (Confidentiality/Integrity/Availability)|
|integrityImpact|string|False|CVSSv3 integrity impact metric|
|privilegeRequired|string|False|CVSSv3 privilege required metric|
|scope|string|False|CVSSv3 scope metric|
|score|float|False|CVSSv3 score|
|userInteraction|string|False|CVSSv3 user interaction metric|
|vector|string|False|CVSSv3 combined vector string|

#### cvss

|Name|Type|Required|Description|
|----|----|--------|-----------|
|links|[]link|False|List of hypermedia links to corresponding resources|
|v2|cvss_v2|False|CVSSv2 details|
|v3|cvss_v3|False|CVSSv3 details|

#### vulnerability

|Name|Type|Required|Description|
|----|----|--------|-----------|
|added|date|False|Date that the vulnerability was added to InsightVM|
|categories|[]string|False|List of vulnerabilities categories with which this vulnerability is affiliated|
|cves|[]string|False|List of CVE identifiers associated with this vulnerability|
|cvss|cvss|False|Vulnerability CVSS details|
|denialOfService|boolean|False|Whether the vulnerability is a denial of service vulnerability|
|description|vulnerability_description|False|Vulnerability description|
|exploits|integer|False|Exploit count|
|id|string|False|Vulnerability ID|
|links|[]link|False|List of hypermedia links to corresponding resources|
|malwareKits|integer|False|Malware kit count|
|modified|date|False|Date the vulnerability was last modified in InsightVM|
|pci|pci|False|Vulnerability PCI details|
|published|date|False|Date the vulnerability was published|
|riskScore|float|False|Vulnerability risk score using the configured risk scoring strategy (RealRisk by default)|
|severity|string|False|Vulnerability severity string (Moderate/Severe/Critical)|
|severityScore|integer|False|Vulnerability severity score|
|title|string|False|Vulnerability title|

#### tag

|Name|Type|Required|Description|
|----|----|--------|-----------|
|color|string|False|Tag color|
|created|date|False|Tag creation date|
|id|integer|True|Tag ID|
|links|[]link|False|Hypermedia links to corresponding or related resources|
|name|string|True|Tag name|
|riskModifier|string|False|Tag risk score modifier|
|searchCriteria|object|False|Tag search criteria|
|source|string|False|Tag source|
|type|string|True|Tag type|

#### tag_asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|True|Asset ID|
|sources|[]string|True|Tag association sources|

#### scan

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|integer|False|Count of assets identified during the scan|
|duration|date|False|Duration of the scan|
|endTime|date|False|End time of the scan|
|engineId|integer|False|ID for the scan engine/scan engine pool used for the scan|
|engineName|string|False|Name of the scan engine/scan engine pool used for the scan|
|id|integer|False|ID of the scan|
|links|[]link|False|List of hypermedia links to corresponding resources|
|message|string|False|Scan status message|
|scanName|string|False|Name of the scan|
|scanType|string|False|Type of scan (automated, manual, scheduled)|
|siteId|integer|False|ID of the site scanned|
|siteName|string|False|Name of the site scanned|
|startTime|date|False|Start time for the scan|
|startedBy|string|False|User that started the scan|
|status|string|False|Scan status (aborted, unknown, running, finished, stopped, error, paused, dispatched, integrating)|
|vulnerabilities|vulnerabilities_count|False|Counts of vulnerabilities identified during the scan|

#### scan_engine

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address|string|True|Scan engine address (IP/hostname)|
|contentVersion|string|False|Scan engine content version|
|enginePools|[]integer|True|Engine pool IDs with which the scan engine is associated|
|id|integer|True|Scan engine identifier|
|lastRefreshedDate|date|False|Date and time when the engine last communicated with the console|
|lastUpdatedDate|date|False|Date and time when the engine was last updated|
|links|[]link|True|List of hypermedia links to corresponding resources|
|name|string|True|Scan engine name|
|port|integer|True|Scan engine communication port|
|productVersion|string|False|Scan engine product version|
|sites|[]integer|False|Sites with which the scan engine is associated|

#### scan_engine_pool

|Name|Type|Required|Description|
|----|----|--------|-----------|
|engines|[]integer|True|List of scan engine IDs associated with the scan engine pool|
|id|integer|True|Scan engine pool identifier|
|links|[]link|True|List of hypermedia links to corresponding resources|
|name|string|True|Scan engine pool name|

#### authentication_source

|Name|Type|Required|Description|
|----|----|--------|-----------|
|external|boolean|True|Whether the authentication source is external (true) or internal (false)|
|id|integer|True|Authentication source identifier|
|links|[]link|True|List of hypermedia links to corresponding or related resources|
|name|string|True|Authentication source name|
|type|string|True|Authentication source type|

#### role

|Name|Type|Required|Description|
|----|----|--------|-----------|
|description|string|True|The description of the role|
|id|string|True|ID of the role, e.g 'global-admin'|
|links|[]link|True|List of hypermedia links to corresponding or related resources|
|name|string|True|Name of the role|
|privileges|[]string|True|List of privileges assigned to the role|

#### user_account_role

|Name|Type|Required|Description|
|----|----|--------|-----------|
|allAssetGroups|boolean|False|Whether the user has access to all asset groups|
|allSites|boolean|False|Whether the user has access to all sites|
|id|string|False|The identifier of the role the user is assigned to|
|privileges|[]string|False|None|
|superuser|boolean|False|Whether the user is a superuser|

#### user_account_locale

|Name|Type|Required|Description|
|----|----|--------|-----------|
|default|string|True|Default locale|
|reports|string|True|Reports locale|

#### user_account

|Name|Type|Required|Description|
|----|----|--------|-----------|
|authentication|authentication_source|False|The authentication source used to authenticate the user|
|email|string|False|The email address of the user|
|enabled|boolean|False|Whether the user account is enabled|
|id|integer|False|The identifier of the user|
|links|[]link|False|List of hypermedia links to corresponding or related resources|
|locale|user_account_locale|False|The locale and language preferences for the user|
|locked|boolean|True|Whether the user account is locked (exceeded maximum password retry attempts)|
|login|string|True|The login name of the user|
|name|string|True|The full name of the user|
|role|user_account_role|False|The privileges and role the user is assigned|

#### remediation_asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|criticalityTag|string|False|The criticality tag assigned to the asset|
|hostName|string|False|Primary host name (local or FQDN) of the asset|
|id|integer|True|Identifier of the asset|
|ip|string|True|Primary IPv4 or IPv6 address of the asset|
|mac|string|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|
|os|string|False|Full description of the operating system of the asset|
|riskScore|float|False|Risk score (with criticality adjustments) of the asset|

#### remediation_vulnerability

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cvssScore|string|True|The CVSS score of the vulnerability|
|description|string|True|The description of the vulnerability|
|id|integer|True|Identifier of the vulnerability|
|riskScore|integer|True|The risk score of the vulnerability|
|severity|integer|True|The severity of the vulnerability|
|title|string|True|The title of the vulnerability|

#### remediation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assetCount|integer|True|The number of assets that require the solution to be applied|
|assets|[]remediation_asset|True|The assets that require the solution to be applied|
|fix|string|False|The steps that are part of the fix this solution prescribes|
|nexposeId|string|True|The identifier of the solution within InsightVM/Nexpose|
|riskScore|integer|True|The risk score that is reduced by performing the solution|
|solutionId|integer|True|The identifier of the solution|
|summary|string|True|Remediation summary|
|vulnerabilities|[]remediation_vulnerability|True|The vulnerabilities that would be remediated|
|vulnerabilityCount|integer|True|The number of vulnerabilities that would be remediated|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 3.5.0 - New Actions Get Vulnerability Details, Create Vulnerability Exception Submission,  Delete Vulnerability Exception, Review Vulnerability Exception  | New Trigger New Vulnerability Exception Activity | Misc. Cleanup
* 3.4.0 - New Action Get Asset Software | Fix issue with New Scan trigger not properly caching new scan IDs
* 3.3.1 - Fix issue in Top Remediations action that causes assets without criticality tags to not be returned in asset list
* 3.3.0 - New Actions Get Asset, Get Asset Tags, Get Scan Assets, Generate AdHoc SQL Report, Top Remediations | New trigger New Scans
* 3.2.0 - New Actions Create Site, Update Site, Delete Site, Update Site Included Targets, Update Site Excluded Targets, Update Site Included Asset Groups, and Update Site Excluded Asset Groups
* 3.1.0 - New Actions Get Authentication Sources, Get Authentication Source, Get Roles, Get Role, Get Users, Get User, Create User, Update User, Update User Asset Group Access, Add User Asset Group Access, Remove User Asset Group Access, Update User Site Access, Add User Site Access, Remove User Site Access, Disable User, Enable User, Delete User, Update User Role
* 3.0.1 - Update descriptions
* 3.0.0 - Rename Action Get Vulnerabilities to Get Asset Vulnerabilities | Correct output of Scan action | New Actions Get Vulnerabilities by CVE, Get Scans, Update Scan Status, Generate Shared Secret, Get Scan Engines, Get Scan Engine, Create Scan Engine, Delete Scan Engine, Get Scan Engine Pools, Get Scan Engine Pool, Create Scan Engine Pool, Add Scan Engine Pool Engine, Remove Scan Engine Pool Engine, Delete Scan Engine Pool, Update Site Scan Engine
* 2.3.0 - New Actions Create Tag, Delete Tag, Get Tag, Get Tag Sites, Get Tag Assets, Get Tag Asset Groups, Get Tags, Remove Asset Tag, Remove Asset Group Tags, Remove Tag Asset Groups, Remove Tag Sites, Remove Tag Search Criteria, Tag Site, Tag Asset, Tag Asset Group, Update Tag Search Criteria, Asset Search, Get Sites, Get Site, Get Asset Groups, Get Asset Group, Create Asset Group, Delete Asset Group, and Update Asset Group Search Criteria
* 2.2.1 - Correct output of the Get Scan action
* 2.2.0 - New Action Get Vulnerability Affected Assets
* 2.1.0 - Add Download Report and List Reports action
* 2.0.0 - Support web server mode
* 1.0.0 - Initial plugin release

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [InsightVM](https://www.rapid7.com/products/insightvm/)
* [InsightVM API 3](https://help.rapid7.com/insightvm/en-us/api/index.html)

