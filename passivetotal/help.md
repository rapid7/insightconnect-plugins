# Description

RiskIQ's [PassiveTotal](https://www.passivetotal.org/) overcomes the challenges in discovering and proactively 
blocking malicious infrastructure. Using innovative techniques and research processes, 
PassiveTotal provides analysts with a single view into all the data they need.

# Key Features

* Look up domains and addresses
* Search WHOIS

# Requirements

* PassiveTotal account
* PassiveTotal API key

# Documentation

## Setup

This plugin requires a PassiveTotal username and API key to authenticate.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key for PassiveTotal|None|
|username|string|None|True|Username|None|

## Technical Details

### Actions

#### Lookup Domains

This action is used to check for information about a given string `array` of domains.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domains|[]string|None|True|Domains|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain_records|[]domain_record|False|Domain Records|
|found_domains|[]string|False|Domains found|

Example output:

```
{
  "domain_records": [
    {
      "dynamic_dns": false,
      "ever_compromised": false,
      "primary_domain": "rapid7.com",
      "subdomains": [
        "accounts",
        "blog",
        "brand",
      ],
      "tags": [],
      "tld": "com"
    }
  ],
  "found_records": [
    "rapid7.com"
  ]
}
```

#### History SSL

This action is used to check for historical information about an SSL certificate by its IP address or SHA1 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|IP Address or SHA-1 Hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]object|False|Results as JSON|

Example output:

```
{
  "results": [
    {
      "firstSeen": "2015-12-14",
      "ipAddresses": [
        "52.8.228.23"
      ],
      "lastSeen": "2020-01-24",
      "sha1": "917e732d330f9a12404f73d8bea36948b929dffc"
    },
    {
      "firstSeen": "2013-10-30",
      "ipAddresses": [
        "52.8.228.23"
      ],
      "lastSeen": "2015-10-12",
      "sha1": "96e64014dd4d542b33da8698094fce09098f7c97"
    },
    {
      "firstSeen": "2016-02-29",
      "ipAddresses": [
        "52.8.228.23"
      ],
      "lastSeen": "2016-06-20",
      "sha1": "36d9e569ddf60f81d42220e3a8f905d9924da971"
    }
  ],
  "success": true
}
```

#### Lookup SSL

This action is used to check for information about an SSL certificate by its SHA1 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sha1|string|None|True|SHA1 Certificate Hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_record|address_record|False|IP Address Record|
|found|boolean|False|True if found|

Example output:

```
{
  "found": true,
  "results": [
    {
      "expirationDate": "Jun 07 17:38:10 2016 GMT",
      "fingerprint": "3d:7d:ba:f2:57:52:0e:7d:06:c0:92:94:8b:7a:7b:a9:91:99:dc:df",
      "firstSeen": 1433746800000,
      "issueDate": "Jun 06 23:10:00 2015 GMT",
      "issuerCommonName": "RapidSSL SHA256 CA - G3",
      "issuerCountry": "US",
      "issuerEmailAddress": null,
      "issuerGivenName": null,
      "issuerLocalityName": null,
      "issuerOrganizationName": "GeoTrust Inc.",
      "issuerOrganizationUnitName": null,
      "issuerProvince": null,
      "issuerSerialNumber": null,
      "issuerStateOrProvinceName": null,
      "issuerStreetAddress": null,
      "issuerSurname": null,
      "lastSeen": 1433746800000,
      "serialNumber": "319720",
      "sha1": "3d7dbaf257520e7d06c092948b7a7ba99199dcdf",
      "sslVersion": "3",
      "subjectAlternativeNames": [
        "www.mobahive.com",
        "mobahive.com"
      ],
      "subjectCommonName": "www.mobahive.com",
      "subjectCountry": null,
      "subjectEmailAddress": null,
      "subjectGivenName": null,
      "subjectLocalityName": null,
      "subjectOrganizationName": null,
      "subjectOrganizationUnitName": "GT11096887",
      "subjectProvince": null,
      "subjectSerialNumber": null,
      "subjectStateOrProvinceName": null,
      "subjectStreetAddress": null,
      "subjectSurname": null
    }
  ],
  "success": true
}
```

#### Lookup Domain

This action is used to check for information about a given domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain, e.g. 4.2.2.2|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain_record|domain_record|False|Domain Record|
|found|boolean|False|True if found|

Example output:

```
{
  "domain_record": {
    "dynamic_dns": false,
    "ever_compromised": false,
    "primary_domain": "rapid7.com",
    "subdomains": [
      "accounts",
      "www",
      "www.userinsight"
    ],
    "tags": [],
    "tld": "com"
  },
  "found": true
}

```

#### Lookup Addresses

This action is used to check for information about a given string `array` of IP addresses.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|addresses|[]string|None|True|IP Addresses|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_records|[]address_record|False|IP Address Records|
|found_addresses|[]string|False|IP Addresses Found|

Example output:

```
{
  "address_records": [
    {
      "ever_compromised": false,
      "sinkhole": false,
      "tags": []
    },
    {
      "ever_compromised": false,
      "sinkhole": false,
      "tags": []
    }
  ],
  "found_records": [
    "rapid7.com",
    "127.0.0.1"
  ]
}
```

#### Lookup Address

This action is used to check for information about a given IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IP Address, e.g. 4.2.2.2|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_record|address_record|False|IP Address Record|
|found|boolean|False|True if found|

Example output:

```

```

#### Search WHOIS

This action is used to [search WHOIS](https://api.passivetotal.org/api/docs/#api-whois-getv2whoissearchqueryfield).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|field|string|None|True|Field to search on|['domain', 'email', 'name', 'organization', 'address', 'phone', 'nameserver']|
|query|string|None|True|Input query, e.g. email@passivetotal.org|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|record|whois_record|False|WHOIS Record Result|

Example output:

```

```

#### Get WHOIS

This action is used to [query WHOIS](https://api.passivetotal.org/api/docs/#api-whois-getv2whoisquery).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|compact_record|boolean|None|True|Set to true to return a compact record|None|
|query|string|None|True|Input query, e.g. passivetotal.org|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|record|whois_record|False|WHOIS Record Result|

Example output:

```

```

#### Search WHOIS by Keyword

This action is used to search whois by keyword.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Input query, e.g. email@passivetotal.org|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Number of results returned|
|results|[]whois_keyword_result|False|WHOIS Keyword Results|

Example output:

```

```

#### Get Monitor Alerts

This action is used to retrieve all alerts associated with an artifact or project.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|end|date|None|False|Filter results to before this datetime|None|
|project|string|None|False|The name of the project to search by|None|
|start|date|None|False|Filter results to after this datetime|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|False|Retrieved alerts|
|total_records|number|False|Number of alerts returned|


Example output:

```
{
  "results": {},
  "total_records": 0
}
```

#### Get Subdomains

This action is used to [get subdomains](https://api.passivetotal.org/api/docs/#api-enrichment-getv2enrichmentsubdomains).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Input query, e.g. *.passivetotal.org|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Number of results returned|
|subdomains|[]string|False|Subdomains returned, e.g [foo, bar, api]|

Example output:

```
```

### Triggers

#### Project Updated

_This trigger is used to look for updates to a project._

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|frequency|integer|300|False|The time between updates in seconds|None|
|project_name|string|None|True|The name of the project to retrieve artifacts from|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|updated_list|[]artifact|False|Results as list of JSON|

Example output:

```

```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.2 - Update help.md and type for Autonomous System Number
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Support web server mode | Update to new credential types
* 0.4.0 - Add trigger to pull new artifacts
* 0.3.1 - SSL bug fix in SDK
* 0.3.0 - Monitor - Get Alerts action added
* 0.1.0 - Initial plugin

# Links

## References

* [PassiveTotal](https://www.passivetotal.org/)
* [PassiveTotal API](https://api.passivetotal.org/api/docs/)
