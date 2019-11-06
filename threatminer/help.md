# Description

[Threat Miner](https://www.threatminer.org) is an open source search engine for
fast threat intelligence research and pivoting with context.

This plugin utilizes the [ThreatMiner API](https://www.threatminer.org/api.php).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Domain Lookup

This action is used to fetches information related to a domain by URIs, certificates, or related samples.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query_type|string|None|True|None|['WHOIS', 'PASSIVE DNS', 'Example Query URI', 'Report Tagging']|
|domain|string|None|True|Domain to search|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Email (Reverse WHOIS) - Report Tagging

This action is used to fetches information related to an email address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|Email address to search e.g. janagreen2000@example.com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### IP Lookup

This action is used to fetch information related to an IP by Whois, URIs, passive DNS, or report tagging.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query_type|string|None|True|None|['WHOIS', 'PASSIVE DNS', 'URIs', 'Report Tagging']|
|address|string|None|True|IP address to search|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Search APTNotes

This action is used to fetches information related to a text search.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Text to search e.g. sofacy|None|
|query_type|string|None|True|None|['Full Text', 'By Year']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### SSL Hosts

This action is used to fetches host information related to a certificate.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Certificate SHA1 hash to search e.g. 42a8d5b3a867a59a79f44ffadd61460780fe58f2|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Domain Lookup Extended

This action is used to fetch information related to a domain by URIs, certificates, or related samples.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query_type|string|None|True|None|['Related Samples', 'Subdomains']|
|domain|string|None|True|Domain to search|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Hash Report

This action is used to fetches information related to a hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|SHA1 hash to search e.g. 1f4f257947c1b713ca7f9bc25f914039|None|
|query_type|string|None|True|None|['Samples', 'Report Tagging']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Hash Samples

This action is used to fetches information related to a hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|SHA1 hash to search e.g. 1f4f257947c1b713ca7f9bc25f914039|None|
|query_type|string|None|True|None|['Samples', 'Report Tagging']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### AV Report

This action is used to query for an AV report.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Virus name to query e.g. Trojan.Enfal|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|Response|

Example output:

```
```

#### Get Samples

This action is used to fetches samples of data intelligence data by metadata, http traffic, hosts, mutants, registry keys, av detections, or report tagging.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|MD5, SHA1, or SHA256 hash to search|None|
|query_type|string|None|True|None|['Metadata', 'HTTP Traffic', 'Hosts', 'Mutants', 'Registry keys', 'AV detections', 'Report Tagging']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Email (Reverse WHOIS) - Domain

This action is used to fetches information related to an email address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|Email address to search e.g. janagreen2000@example.com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### Search IOC Reports

This action is used to fetch information related to an indicator by domains, hosts, emails, or samples.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query_type|string|None|True|None|['Domains', 'Hosts', 'Emails', 'Samples']|
|filename|string|None|True|Indicator to search e.g. C5_APT_C2InTheFifthDomain.pdf|None|
|year|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### SSDeep Report

This action is used to fetches information related to a fuzzy hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|SSDeep fuzzy hash to search e.g. 1536\:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4\:TJs0oG2KSTj3o8a9PFeEHn4l|None|
|query_type|string|None|True|None|['Samples', 'Report Tagging']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### SSDeep Samples

This action is used to fetches information related to a fuzzy hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|SSDeep fuzzy hash to search e.g. 1536\:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4\:TJs0oG2KSTj3o8a9PFeEHn4l|None|
|query_type|string|None|True|None|['Samples', 'Report Tagging']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### AV Samples

This action is used to fetches information related to a virus.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Virus name to query e.g. Trojan.Enfal|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### SSL Report

This action is used to fetches information related to a certificate.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Certificate SHA1 hash to search e.g. 42a8d5b3a867a59a79f44ffadd61460780fe58f2|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### IP Lookup Extended

This action is used to fetch information related to an IP by SSL certificates, or related samples.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query_type|string|None|True|None|['Related Samples', 'SSL Certificates']|
|address|string|None|True|IP address to search|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

#### AV Detection Samples

This action is used to fetches information related to a virus.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Virus name to query e.g. Trojan.Enfal|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

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

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Rename "Email (Reverse WHOIS) - Report tagging" action to "Email (Reverse WHOIS) - Report Tagging"
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Threat Miner](https://www.threatminer.org)
* [Threat Miner API](http://www.threatminer.org/api.php)

