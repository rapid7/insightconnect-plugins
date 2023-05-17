# Description

[Threat Miner](https://www.threatminer.org) is an open source search engine for fast threat intelligence research and pivoting with context. 
With the Threat Miner plugin for Rapid7 InsightConnect, users can lookup various pieces of information for threat intelligence gathering
The Threat Miner plugin can aid in phishing analysis through its various lookup actions for domains, IP addresses, and
email addresses. In addition, it can assist in malicious attachment detection when used with email plugins using its hash report feature.

# Key Features

* Domain lookup

# Requirements

 _This plugin does not contain any requirements._

# Supported Product Versions

* 2023-05-17

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### AV Report

This action is used to obtain an AV Report.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Virus name to query|None|Trojan.Enfal|

Example input:

```
{
  "query": "Trojan.Enfal"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

Example output:

```
```

#### AV Detection Samples

This action fetches information related to a virus.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Virus name to query|None|Trojan.Enfal|

Example input:

```
{
  "query": "Trojan.Enfal"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### Domain Lookup

This action fetches information related to a domain by URIs, certificates, or related samples.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain to search|None|www.example.com|
|query_type|string|None|True|Query Type|['WHOIS', 'PASSIVE DNS', 'Example Query URI', 'Report Tagging']|WHOIS|

Example input:

```
{
  "domain": "www.example.com",
  "query_type": "WHOIS"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|


#### Domain Lookup Extended

This action fetches information related to a domain by URIs, certificates, or related samples.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain to search|None|www.example.com|
|query_type|string|None|True|Query type|['Related Samples', 'Subdomains']|Subdomains|

Example input:

```
{
  "domain": "www.example.com",
  "query_type": "Subdomains"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|


#### Email Reverse WHOIS - Domain

This action fetches information related to an email address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email address to search|None|user@example.com|

Example input:

```
{
  "email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### Email Reverse WHOIS - Report Tagging

This action fetches information related to an email address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email address to search|None|user@example.com|

Example input:

```
{
  "email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### Hash Report

This action fetches information related to a hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|SHA1 hash to search e.g. 1f4f257947c1b713ca7f9bc25f914039|None|02699626f388ed830012e5b787640e71c56d42d8|

Example input:

```
{
  "query": "02699626f388ed830012e5b787640e71c56d42d8"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### Hash Samples

This action fetches information related to a hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|SHA1 hash to search e.g. 1f4f257947c1b713ca7f9bc25f914039|None|02699626f388ed830012e5b787640e71c56d42d8|

Example input:

```
{
  "query": "02699626f388ed830012e5b787640e71c56d42d8"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Query|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### IP Lookup

This action fetches information related to an IP by Whois, URIs, passive DNS, or report tagging.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|IP address to search|None|192.0.2.0/24|
|query_type|string|None|True|Query Type|['WHOIS', 'PASSIVE DNS', 'URIs', 'Report Tagging']|WHOIS|

Example input:

```
{
  "address": "192.0.2.0/24",
  "query_type": "WHOIS"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### IP Lookup Extended

This action fetches information related to an IP by certificates, or related samples.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|IP address to search|None|192.0.2.0/24|
|query_type|string|None|True|Query type|['Related Samples', 'SSL Certificates']|Related Samples|

Example input:

```
{
  "address": "192.0.2.0/24",
  "query_type": "Related Samples"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|


#### Search IOC Reports

This action fetches information related to an indicator by domains, hosts, emails, or samples.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filename|string|None|True|Indicator to search|None|C5_APT_C2InTheFifthDomain.pdf|
|query_type|string|None|True|Query Type|['Domains', 'Hosts', 'Emails', 'Samples']|Domains|
|year|string|None|True|Year to search|None|2013|

Example input:

```
{
  "filename": "C5_APT_C2InTheFifthDomain.pdf",
  "query_type": "Domains",
  "year": 2013
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### Get Samples

This action fetches samples of data intelligence data by metadata, HTTP traffic, hosts, mutants, registry keys, AV detections, or report tagging.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|MD5, SHA1, or SHA256 hash to search|None|9de5069c5afe602b2ea0a04b66beb2c0|
|query_type|string|None|True|Query Type|['Metadata', 'HTTP Traffic', 'Hosts', 'Mutants', 'Registry keys', 'AV detections', 'Report Tagging']|Metadata|

Example input:

```
{
  "query": "9de5069c5afe602b2ea0a04b66beb2c0",
  "query_type": "Metadata"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### Search APTNotes

This action fetches information related to a text search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Text to search|None|sofacy|
|query_type|string|None|True|Query Type|['Full Text', 'By Year']|Full Text|

Example input:

```
{
  "query": "sofacy",
  "query_type": "Full Text"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### SSDeep Report

This action fetches information related to a fuzzy hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|SSDeep fuzzy hash to search|None|1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l|

Example input:

```
{
  "query": "1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### SSDeep Sample

This action fetches information related to a fuzzy hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|SSDeep fuzzy hash to search|None|1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l|

Example input:

```
{
  "query": "1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### SSL Hosts

This action fetches host information related to a certificate.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Certificate SHA1 hash to search|None|42a8d5b3a867a59a79f44ffadd61460780fe58f2|

Example input:

```
{
  "query": "42a8d5b3a867a59a79f44ffadd61460780fe58f2"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

#### SSL Report

This action fetches information related to a certificate.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Certificate SHA1 hash to search|None|42a8d5b3a867a59a79f44ffadd61460780fe58f2|

Example input:

```
{
  "query": "42a8d5b3a867a59a79f44ffadd61460780fe58f2"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|response|response|False|Response|{'response': {'status_code': '404', 'status_message': 'No results found.', 'results': []}}|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Results|[]object|False|Results|
|Status Code|integer|False|Status Code|
|Status Message|string|False|Status message|


## Troubleshooting

There are three key attributes in each `response` object:

|Name|Type|Description|
|----|----|-----------|
|status_code|string|200 if results are found, 400 if not|
|status_message|string|Text explanation of the status_code|
|results|[]object|This is where the results are returned and the exact JSON structure returned differs per query type|

The raw object returned by each action looks like this:

```

"response": {
  "status_message": "Results found.",
  "results": [],
  "status_code": "200"
}

```

An example raw response from the domain action:

```

"response": {
  "status_message": "Results found.",
  "results": [
    {
      "ip": "",
      "last_seen": "2014-07-17 16:51:28",
      "domain": "vwrm.com",
      "uri": "http://vwrm.com/maps/iexplorer.zip"
    },
    {
      "ip": "",
      "last_seen": "2013-04-23 18:48:53",
      "domain": "vwrm.com",
      "uri": "http://vwrm.com/"
    }
  ],
  "status_code": "200"
}

```

Working through the `[]results` object array which resides in the `result` object, will require some JSON manipulation to get what you need.
The [jq](https://market.komand.com/plugins/komand/jq/0.1.0) and [JSON](https://market.komand.com/plugins/komand/json/0.1.1) plugins are great at sifting through the data.

#


# Version History

* 3.0.0 - Updated Requests version to 2.20.0 | Fixed AV Report Status Code Bug
* 2.0.0 - Update to v3 Python plugin architecture | Convert import_hash_report API status codes to int | Update documentation
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Rename "Email (Reverse WHOIS) - Report tagging" action to "Email (Reverse WHOIS) - Report Tagging"
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin


# Links

* [Threat Miner](https://www.threatminer.org)

## References

* [Threat Miner](https://www.threatminer.org)
* [Threat Miner API](http://www.threatminer.org/api.php)
