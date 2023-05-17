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
{
  "response": {
    "status_code": 200,
    "status_message": "Results found.",
    "results": [
      {
        "filename": "example.pdf",
        "year": "2023",
        "URL": "www.example.com"
      }
    ]
}
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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      "44d88612fea8a8f36de82e1278abb02f"
   ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      {
         "domain":"vwrm.com",
         "is_subdomain":false,
         "root_domain":"",
         "whois":{
            "updated_date":"2012-03-26 12:04:11",
            "whois_md5":"f8c433f165d39ce655c18e91d685cca0",
            "billing_info":{
               "Organization":" Aliant Telecom",
               "City":" Saint John",
               "State":" New Brunswick",
               "Country":" Canada",
               "Postal_Code":" E2L4K2"
            },
            "registrant_info":{
               "City":" Kentville",
               "Country":" Canada",
               "State":" Nova Scotia",
               "Street":" PO Box 895",
               "Postal_Code":" B4N4H8",
               "Organization":" Valley Waste Resource Management"
            },
            "creation_date":"1999-04-01 05:00:00",
            "whois_server":"whois.register.com",
            "emails":{
               "admin":"",
               "tech":"",
               "registrant":"",
               "billing":""
            },
            "tech_info":{
               "Organization":" Aliant Telecom",
               "City":" Saint John",
               "State":" New Brunswick",
               "Country":" Canada",
               "Postal_Code":" E2L4K2"
            },
            "admin_info":{
               "Organization":" Aliant Telecom",
               "City":" Saint John",
               "State":" New Brunswick",
               "Country":" Canada",
               "Postal_Code":" E2L4K2"
            },
            "nameservers":[
               "onyx.nbnet.nb.ca",
               "opal.nbnet.nb.ca"
            ],
            "expiration_date":"2017-04-01 04:00:00",
            "email_hashes":{
               "admin":"",
               "tech":"",
               "registrant":"",
               "billing":""
            },
            "registrar":"register.com, inc.",
            "date_checked":"2016-11-22 14:10:14",
            "reg_info":{
               "Organization":" Aliant Telecom",
               "City":" Saint John",
               "State":" New Brunswick",
               "Country":" Canada",
               "Postal_Code":" E2L4K2"
            }
         },
         "last_updated":{
            "sec":1573985686,
            "usec":632000
         }
      }
   ]
}

```


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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      {
         "domain":"vwrm.com",
         "is_subdomain":false,
         "root_domain":"",
         "whois":{
            "updated_date":"2012-03-26 12:04:11",
            "whois_md5":"f8c433f165d39ce655c18e91d685cca0",
            "billing_info":{
               "Organization":" Aliant Telecom",
               "City":" Saint John",
               "State":" New Brunswick",
               "Country":" Canada",
               "Postal_Code":" E2L4K2"
            },
            "registrant_info":{
               "City":" Kentville",
               "Country":" Canada",
               "State":" Nova Scotia",
               "Street":" PO Box 895",
               "Postal_Code":" B4N4H8",
               "Organization":" Valley Waste Resource Management"
            },
            "creation_date":"1999-04-01 05:00:00",
            "whois_server":"whois.register.com",
            "emails":{
               "admin":"",
               "tech":"",
               "registrant":"",
               "billing":""
            },
            "tech_info":{
               "Organization":" Aliant Telecom",
               "City":" Saint John",
               "State":" New Brunswick",
               "Country":" Canada",
               "Postal_Code":" E2L4K2"
            },
            "admin_info":{
               "Organization":" Aliant Telecom",
               "City":" Saint John",
               "State":" New Brunswick",
               "Country":" Canada",
               "Postal_Code":" E2L4K2"
            },
            "nameservers":[
               "onyx.nbnet.nb.ca",
               "opal.nbnet.nb.ca"
            ],
            "expiration_date":"2017-04-01 04:00:00",
            "email_hashes":{
               "admin":"",
               "tech":"",
               "registrant":"",
               "billing":""
            },
            "registrar":"register.com, inc.",
            "date_checked":"2016-11-22 14:10:14",
            "reg_info":{
               "Organization":" Aliant Telecom",
               "City":" Saint John",
               "State":" New Brunswick",
               "Country":" Canada",
               "Postal_Code":" E2L4K2"
            }
         },
         "last_updated":{
            "sec":1573985686,
            "usec":632000
         }
      }
   ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      "my-dejanews.com"
   ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      "my-dejanews.com"
   ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      "4c60f3f5cccdfad6137eb0a3218ec4caa3294b164c86dbda8922f1c9a75558fd"
   ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      "4c60f3f5cccdfad6137eb0a3218ec4caa3294b164c86dbda8922f1c9a75558fd"
   ]
}
```

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

Example output:

```
{
  "status_code":"200",
  "status_message":"Results found.",
  "results":[
     {
        "reverse_name":"51.38.21.104.in-addr.arpa.",
        "bgp_prefix":"104.21.32.0/20",
        "cc":"US",
        "asn":"13335",
        "asn_name":"",
        "org_name":"Cloudflare, Inc.",
        "register":"Arin"
     }
  ]
}
```

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

Example output:

```
{
  "status_code":"200",
  "status_message":"Results found.",
  "results":[
     {
        "reverse_name":"51.38.21.104.in-addr.arpa.",
        "bgp_prefix":"104.21.32.0/20",
        "cc":"US",
        "asn":"13335",
        "asn_name":"",
        "org_name":"Cloudflare, Inc.",
        "register":"Arin"
     }
  ]
}
```


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

Example output:

```
{
  "status_code":"200",
  "status_message":"Results found.",
  "results": [
    {
      "filename":"shadows-in-the-cloud.pdf",
      "year":"2010",
      "URL":"https://www.threatminer.org/report.php?q=shadows-in-the-cloud.pdf&y=2010"
    }
  ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      {
         "filename":"shadows-in-the-cloud.pdf",
         "year":"2010",
         "URL":"https://www.threatminer.org/report.php?q=shadows-in-the-cloud.pdf&y=2010"
      }
   ]
}
```

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

Example output:

```
{
  "status_code":"200",
  "status_message":"Results found.",
  "results": [
    {
      "filename":"shadows-in-the-cloud.pdf",
      "year":"2010",
      "URL":"https://www.threatminer.org/report.php?q=shadows-in-the-cloud.pdf&y=2010"
    }
  ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      {
         "filename":"shadows-in-the-cloud.pdf",
         "year":"2010",
         "URL":"https://www.threatminer.org/report.php?q=shadows-in-the-cloud.pdf&y=2010"
      }
   ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      "ecc5943b5c2ec75065ba1bdb668bb0a2c63c0451be259dea47a902811b318c00"
   ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      "149.154.157.170",
      "149.154.157.171"
   ]
}
```

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

Example output:

```
{
   "status_code":"200",
   "status_message":"Results found.",
   "results":[
      {
         "filename":"fireeye-operation-ke3chang.pdf",
         "year":"2013",
         "URL":"https:\/\/www.threatminer.org\/report.php?q=fireeye-operation-ke3chang.pdf&y=2013"
      }
   ]
}
```

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
