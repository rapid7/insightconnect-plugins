# Description

Analyze URLs for malicious indicators using the URLScan website scanner

# Key Features

* Launch a scan on a URL
* Retrieve reports on a URL

# Requirements

* A URLScan API key

# Supported Product Versions

* urlscan.io API v1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|False|urlscan API key. Not required for the search action|None|{"secretKey": "381cd93b-1946-9c73-1946-c916075eb9a3"}|None|None|

Example input:

```
{
  "api_key": {
    "secretKey": "381cd93b-1946-9c73-1946-c916075eb9a3"
  }
}
```

## Technical Details

### Actions


#### Get Scan Results

This action is used to get the results of a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_id|string|None|True|UUID of the scan to retrieve|None|b1f3dab-ad7e-e2790803d6d0-76wFGijr|None|None|
  
Example input:

```
{
  "scan_id": "b1f3dab-ad7e-e2790803d6d0-76wFGijr"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|lists|object|True|Results of the lists|None|
|meta|object|True|Results of the meta|None|
|page|object|True|Results of the page|None|
|scan_results|scan_results|True|Results of the scan report|None|
|stats|object|True|Results of the stats|None|
|task|object|True|Results of the task|None|
|verdicts|object|True|Results of the verdicts|None|
  
Example output:

```
{
  "lists": {},
  "meta": {},
  "page": {},
  "scan_results": {
    "console": {},
    "cookies": {},
    "globals": {},
    "links": {},
    "requests": [
      {}
    ],
    "screenshotURL": "",
    "timing": {}
  },
  "stats": {},
  "task": {},
  "verdicts": {}
}
```

#### Search

This action is used to search urlscan.io

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input_type|string|Custom|True|Type of provided query. Set 'custom' to provide custom query, set 'url' to search information about provided URL, set 'domain' to search information about provided domain|["URL", "Domain", "Custom"]|Domain|None|None|
|q|string|example.com|True|The query term (ElasticSearch simple query string), default is *. If 'Input Type' input is set to URL or domain, provide only the URL or domain|None|example.com|None|None|
|sort|string|_score|True|Sorting, specificied via $sort_field:$sort_order|None|_score|None|None|
  
Example input:

```
{
  "input_type": "Custom",
  "q": "example.com",
  "sort": "_score"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|has_more|boolean|False|Whether or not the source has more entities|True|
|results|[]results|False|UrlScan.io Results|None|
|total|integer|False|Total number of results returned|0|
  
Example output:

```
{
  "has_more": true,
  "results": [
    {
      "_id": "",
      "page": {
        "asn": {},
        "asnname": {},
        "city": {},
        "country": {},
        "domain": {},
        "ip": {},
        "ptr": {},
        "server": {},
        "url": {}
      },
      "result": {},
      "stats": {
        "consoleMsgs": 0,
        "dataLength": {},
        "encodedDataLength": {},
        "requests": {},
        "uniqIPs": {}
      },
      "task": {
        "method": {},
        "options": {},
        "source": {},
        "time": "",
        "url": {},
        "visibility": {}
      },
      "uniq_countries": {}
    }
  ],
  "total": 0
}
```

#### Submit URL for Scan

This action is used to submit a URL to generate a scan report that can be retrieved later

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|public|boolean|False|True|Set to false for a private scan|None|True|None|None|
|url|string|None|True|The URL to scan|None|http://www.example.com|None|None|
  
Example input:

```
{
  "public": false,
  "url": "http://www.example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan_id|string|True|UUID of the scan to query later|557a7923-c597-4a84-982c-665ece8fa6ed|
|was_scan_skipped|boolean|True|If true scan was skipped, false if scan was executed|False|
  
Example output:

```
{
  "scan_id": "557a7923-c597-4a84-982c-665ece8fa6ed",
  "was_scan_skipped": false
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**page**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|asn|string|None|False|Autonomous System Number|None|
|asnname|string|None|False|Autonomous System Name|None|
|city|string|None|False|None|None|
|country|string|None|False|None|None|
|domain|string|None|False|None|None|
|ip|string|None|False|IP address|None|
|ptr|string|None|False|None|None|
|server|string|None|False|Server Software|None|
|url|string|None|False|None|None|
  
**stats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|consoleMsgs|integer|None|False|Console Messages|None|
|dataLength|integer|None|False|Data Length|None|
|encodedDataLength|integer|None|False|Encoded Data Length|None|
|requests|integer|None|False|None|None|
|uniqIPs|integer|None|False|Unique IPs|None|
  
**task**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|method|string|None|False|None|None|
|options|object|None|False|None|None|
|source|string|None|False|None|None|
|time|date|None|False|None|None|
|url|string|None|False|None|None|
|visibility|string|None|False|None|None|
  
**results**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|_id|string|None|False|None|None|
|page|page|None|False|None|None|
|result|string|None|False|None|None|
|stats|stats|None|False|None|None|
|task|task|None|False|None|None|
|uniq_countries|integer|None|False|Unique Countries|None|
  
**scan_results**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|console|[]object|None|False|None|None|
|cookies|[]object|None|False|None|None|
|globals|[]object|None|False|None|None|
|links|[]object|None|False|None|None|
|requests|[]object|None|False|None|None|
|screenshotURL|string|None|False|None|None|
|timing|object|None|False|None|None|
  
**verdicts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|community|object|None|False|None|None|
|engines|object|None|False|None|None|
|overall|object|None|False|None|None|
|urlscan|object|None|False|None|None|
  
**scan_stats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IPv6Percentage|integer|None|False|None|None|
|adBlocked|integer|None|False|None|None|
|domainStats|[]object|None|False|None|None|
|ipStats|[]object|None|False|None|None|
|malicious|integer|None|False|None|None|
|protocolStats|[]object|None|False|None|None|
|regDomainStats|[]object|None|False|None|None|
|resourceStats|[]object|None|False|None|None|
|securePercentage|integer|None|False|None|None|
|secureRequests|integer|None|False|None|None|
|serverStats|[]object|None|False|None|None|
|tlsStats|[]object|None|False|None|None|
|totalLinks|integer|None|False|None|None|
|uniqCountries|integer|None|False|None|None|
  
**meta**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|processors|object|None|False|None|None|
  
**lists**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|asns|[]object|None|False|None|None|
|certificates|[]object|None|False|None|None|
|countries|[]object|None|False|None|None|
|domains|[]object|None|False|None|None|
|hashes|[]object|None|False|None|None|
|ips|[]object|None|False|None|None|
|linkDomains|[]object|None|False|None|None|
|servers|[]object|None|False|None|None|
|urls|[]object|None|False|None|None|
  
**scan_page**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|asn|string|None|False|None|None|
|asnname|string|None|False|None|None|
|city|string|None|False|None|None|
|country|string|None|False|None|None|
|domain|string|None|False|None|None|
|ip|string|None|False|None|None|
|ptr|string|None|False|None|None|
|server|string|None|False|None|None|
|url|string|None|False|None|None|
  
**scan_task**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|domURL|string|None|False|None|None|
|method|string|None|False|None|None|
|options|object|None|False|None|None|
|reportURL|string|None|False|None|None|
|screenshotURL|string|None|False|None|None|
|source|string|None|False|None|None|
|time|string|None|False|None|None|
|url|string|None|False|None|None|
|userAgent|string|None|False|None|None|
|uuid|string|None|False|None|None|
|visibility|string|None|False|None|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 4.1.2 - Bumping requirements.txt | SDK Bump to 6.1.4
* 4.1.1 - Fix issue: Search - Add PluginException for 400 response code
* 4.1.0 - Cloud enabled
* 4.0.2 - Fix error handling while submit URL which is in blacklist of URLScan API | Update SDK to version 4
* 4.0.1 - Fix issue with not compatible types in custom output type for Get Scan Result action | Add unit tests for Get Scan Result | Refactor existing unit tests
* 4.0.0 - Improve pagination in Search action
* 3.0.1 - Add unit test for Submit URL for Scan action | Add error handling for HTTP 429 status code in Submit URL for Scan action
* 3.0.0 - Major version bump to ensure awareness of a breaking change related to the addition of the `was_scan_skipped` output in Submit URL for Scan action in the previous version
* 2.3.0 - Add logger when submitted domain is in blacklist for Submit URL for Scan action
* 2.2.0 - Add new input Input Type in Search action
* 2.1.8 - Correct spelling in help.md
* 2.1.7 - Add missing outputs to Get Scan Results action
* 2.1.6 - Add default input
* 2.1.5 - Add example input
* 2.1.4 - Use input and output constants | Added 'f' strings
* 2.1.3 - New spec and help.md format for the Extension Library
* 2.1.2 - Set User-Agent string to Rapid7 InsightConnect | Update to use the `komand/python-3-37-slim-plugin:3` Docker image to reduce plugin size | Run plugin as least privileged user | Improve error handling and logging | Fix issue in Submit URL for Scan action where improper POST body was sent
* 2.1.1 - Add error messaging to Get Scan Results action to provide assistance for unavailable scan results | Update to Python 3.7 Slim SDK (plugin size reduction)
* 2.1.0 - Added ScreenshotURL to get scan results output
* 2.0.0 - Fixed issue where output of Get Scan Results did not match API output | Update connection input to secret key instead of token | Updates to help
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [urlscan](https://urlscan.io/)

## References

* [Urlscan.io](https://urlscan.io/)
* [Urlscan API](https://urlscan.io/about-api/)
* [Urlscan Search API](https://urlscan.io/docs/search/)