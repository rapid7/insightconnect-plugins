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
{
  "address_record": {
    "autonomous_system_name": "Level 3 Parent, LLC",
    "autonomous_system_number": 3356,
    "country": "US",
    "ever_compromised": false,
    "latitude": 37.751007080078125,
    "longitude": -97.8219985961914,
    "network": "4.0.0.0/9",
    "sinkhole": false,
    "tags": []
  },
  "found": true
}
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
{
  "found": true,
  "record": {
    "results": [
      {
        "admin": {},
        "billing": {},
        "domain": "example.com",
        "expiresAt": "2020-08-12T21:00:00.000-0700",
        "lastLoadedAt": "2020-01-08T14:40:51.413-0800",
        "name": "N/A",
        "nameServers": [
          "a.iana-servers.net",
          "b.iana-servers.net"
        ],
        "organization": "N/A",
        "rawText": "Domain Name: EXAMPLE.COM\n   Registry Domain ID: 2336799_DOMAIN_COM-VRSN\n   Registrar WHOIS Server: whois.iana.org\n   Registrar URL: http://res-dom.iana.org\n   Updated Date: 2019-08-14T07:04:41Z\n   Creation Date: 1995-08-14T04:00:00Z\n   Registry Expiry Date: 2020-08-13T04:00:00Z\n   Registrar: RESERVED-Internet Assigned Numbers Authority\n   Registrar IANA ID: 376\n   Registrar Abuse Contact Email:\n   Registrar Abuse Contact Phone:\n   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\n   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\n   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\n   Name Server: A.IANA-SERVERS.NET\n   Name Server: B.IANA-SERVERS.NET\n   DNSSEC: signedDelegation\n   DNSSEC DS Data: 31589 8 1 3490A6806D47F17A34C29E2CE80E8A999FFBE4BE\n   DNSSEC DS Data: 31589 8 2 CDE0D742D6998AA554A92D890F8184C698CFAC8A26FA59875A990C03E576343C\n   DNSSEC DS Data: 43547 8 1 B6225AB2CC613E0DCA7962BDC2342EA4F1B56083\n   DNSSEC DS Data: 43547 8 2 615A64233543F66F44D68933625B17497C89A70E858ED76A2145997EDF96A918\n   DNSSEC DS Data: 31406 8 1 189968811E6EBA862DD6C209F75623D8D9ED9142\n   DNSSEC DS Data: 31406 8 2 F78CF3344F72137235098ECBBD08947C2C9001C7F6A085A17F518B5D8F6B916D\n   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/\n\u003e\u003e\u003e Last update of whois database: 2019-08-17T10:53:50Z \u003c\u003c\u003c\n\nFor more information on Whois status codes, please visit https://icann.org/epp\n\nNOTICE: The expiration date displayed in this record is the date the\nregistrar's sponsorship of the domain name registration in the registry is\ncurrently set to expire. This date does not necessarily reflect the expiration\ndate of the domain name registrant's agreement with the sponsoring\nregistrar.  Users may consult the sponsoring registrar's Whois database to\nview the registrar's reported date of expiration for this registration.\n\nTERMS OF USE: You are not authorized to access or query our Whois\ndatabase through the use of electronic processes that are high-volume and\nautomated except as reasonably necessary to register domain names or\nmodify existing registrations; the Data in VeriSign Global Registry\nServices' (\"VeriSign\") Whois database is provided by VeriSign for\ninformation purposes only, and to assist persons in obtaining information\nabout or related to a domain name registration record. VeriSign does not\nguarantee its accuracy. By submitting a Whois query, you agree to abide\nby the following terms of use: You agree that you may use this Data only\nfor lawful purposes and that under no circumstances will you use this Data\nto: (1) allow, enable, or otherwise support the transmission of mass\nunsolicited, commercial advertising or solicitations via e-mail, telephone,\nor facsimile; or (2) enable high volume, automated, electronic processes\nthat apply to VeriSign (or its computer systems). The compilation,\nrepackaging, dissemination or other use of this Data is expressly\nprohibited without the prior written consent of VeriSign. You agree not to\nuse electronic processes that are automated and high-volume to access or\nquery the Whois database except as reasonably necessary to register\ndomain names or modify existing registrations. VeriSign reserves the right\nto restrict your access to the Whois database in its sole discretion to ensure\noperational stability.  VeriSign may restrict or terminate your access to the\nWhois database for failure to abide by these terms of use. VeriSign\nreserves the right to modify these terms at any time.\n\nThe Registry database contains ONLY .COM, .NET, .EDU domains and\nRegistrars.\n\n%!!(MISSING)I(MISSING)ANA WHOIS server\n%!!(MISSING)f(MISSING)or more information on IANA, visit http://www.iana.org\n%!!(MISSING)T(MISSING)his query returned 1 object\n\ndomain:       EXAMPLE.COM\n\norganisation: Internet Assigned Numbers Authority\n\ncreated:      1992-01-01\nsource:       IANA",
        "registered": "1995-08-13T21:00:00.000-0700",
        "registrant": {},
        "registrar": "RESERVED-Internet Assigned Numbers Authority",
        "registryUpdatedAt": "2019-08-14T00:04:41.000-0700",
        "tech": {},
        "telephone": "N/A",
        "whoisServer": "whois.iana.org",
        "zone": {}
      }
    ]
  }
}
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
{
  "found": true,
  "record": {
    "admin": {},
    "billing": {},
    "domain": "example.com",
    "expiresAt": "2020-08-12T21:00:00.000-0700",
    "lastLoadedAt": "2020-01-08T14:40:51.413-0800",
    "name": "N/A",
    "nameServers": [
      "a.iana-servers.net",
      "b.iana-servers.net"
    ],
    "organization": "N/A",
    "rawText": "Domain Name: EXAMPLE.COM\n   Registry Domain ID: 2336799_DOMAIN_COM-VRSN\n   Registrar WHOIS Server: whois.iana.org\n   Registrar URL: http://res-dom.iana.org\n   Updated Date: 2019-08-14T07:04:41Z\n   Creation Date: 1995-08-14T04:00:00Z\n   Registry Expiry Date: 2020-08-13T04:00:00Z\n   Registrar: RESERVED-Internet Assigned Numbers Authority\n   Registrar IANA ID: 376\n   Registrar Abuse Contact Email:\n   Registrar Abuse Contact Phone:\n   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\n   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\n   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\n   Name Server: A.IANA-SERVERS.NET\n   Name Server: B.IANA-SERVERS.NET\n   DNSSEC: signedDelegation\n   DNSSEC DS Data: 31589 8 1 3490A6806D47F17A34C29E2CE80E8A999FFBE4BE\n   DNSSEC DS Data: 31589 8 2 CDE0D742D6998AA554A92D890F8184C698CFAC8A26FA59875A990C03E576343C\n   DNSSEC DS Data: 43547 8 1 B6225AB2CC613E0DCA7962BDC2342EA4F1B56083\n   DNSSEC DS Data: 43547 8 2 615A64233543F66F44D68933625B17497C89A70E858ED76A2145997EDF96A918\n   DNSSEC DS Data: 31406 8 1 189968811E6EBA862DD6C209F75623D8D9ED9142\n   DNSSEC DS Data: 31406 8 2 F78CF3344F72137235098ECBBD08947C2C9001C7F6A085A17F518B5D8F6B916D\n   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/\n\u003e\u003e\u003e Last update of whois database: 2019-08-17T10:53:50Z \u003c\u003c\u003c\n\nFor more information on Whois status codes, please visit https://icann.org/epp\n\nNOTICE: The expiration date displayed in this record is the date the\nregistrar's sponsorship of the domain name registration in the registry is\ncurrently set to expire. This date does not necessarily reflect the expiration\ndate of the domain name registrant's agreement with the sponsoring\nregistrar.  Users may consult the sponsoring registrar's Whois database to\nview the registrar's reported date of expiration for this registration.\n\nTERMS OF USE: You are not authorized to access or query our Whois\ndatabase through the use of electronic processes that are high-volume and\nautomated except as reasonably necessary to register domain names or\nmodify existing registrations; the Data in VeriSign Global Registry\nServices' (\"VeriSign\") Whois database is provided by VeriSign for\ninformation purposes only, and to assist persons in obtaining information\nabout or related to a domain name registration record. VeriSign does not\nguarantee its accuracy. By submitting a Whois query, you agree to abide\nby the following terms of use: You agree that you may use this Data only\nfor lawful purposes and that under no circumstances will you use this Data\nto: (1) allow, enable, or otherwise support the transmission of mass\nunsolicited, commercial advertising or solicitations via e-mail, telephone,\nor facsimile; or (2) enable high volume, automated, electronic processes\nthat apply to VeriSign (or its computer systems). The compilation,\nrepackaging, dissemination or other use of this Data is expressly\nprohibited without the prior written consent of VeriSign. You agree not to\nuse electronic processes that are automated and high-volume to access or\nquery the Whois database except as reasonably necessary to register\ndomain names or modify existing registrations. VeriSign reserves the right\nto restrict your access to the Whois database in its sole discretion to ensure\noperational stability.  VeriSign may restrict or terminate your access to the\nWhois database for failure to abide by these terms of use. VeriSign\nreserves the right to modify these terms at any time.\n\nThe Registry database contains ONLY .COM, .NET, .EDU domains and\nRegistrars.\n\n%!!(MISSING)I(MISSING)ANA WHOIS server\n%!!(MISSING)f(MISSING)or more information on IANA, visit http://www.iana.org\n%!!(MISSING)T(MISSING)his query returned 1 object\n\ndomain:       EXAMPLE.COM\n\norganisation: Internet Assigned Numbers Authority\n\ncreated:      1992-01-01\nsource:       IANA",
    "registered": "1995-08-13T21:00:00.000-0700",
    "registrant": {},
    "registrar": "RESERVED-Internet Assigned Numbers Authority",
    "registryUpdatedAt": "2019-08-14T00:04:41.000-0700",
    "tech": {},
    "telephone": "N/A",
    "whoisServer": "whois.iana.org",
    "zone": {}
  }
}
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
{
  "count": 3,
  "results": [
    {
      "fieldMatch": "address",
      "focusPoint": "example.com",
      "matchType": "domain"
    },
    {
      "fieldMatch": "name",
      "focusPoint": "example.tw",
      "matchType": "domain"
    },
    {
      "fieldMatch": "email",
      "focusPoint": "example.tw",
      "matchType": "domain"
    }
  ]
}
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
{
  "count": 2,
  "subdomains": [
    "go",
    "opendata",
  ]
}

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
{
  "artifact": [
    {
      "guid": "a403c430-c852-45d4-ad9a-4dd9d9f3cc80",
      "monitorable": false,
      "organization": "",
      "query": "google.com",
      "creator": "user@example.com",
      "created": "2020-01-27T18:05:28.255000",
      "type": "domain",
      "project": "acaca120-8101-4618-88d6-cfdd92699218",
      "monitor": false,
      "links": {
        "tag": "/v2/artifact/tag?artifact=a403c430-c852-45d4-ad9a-4dd9d9f3cc80",
        "project": "/v2/project?project=acaca120-8101-4618-88d6-cfdd92699218",
        "self": "/v2/artifact?artifact=a403c430-c852-45d4-ad9a-4dd9d9f3cc80"
      },
      "owner": "user@example.com",
      "tags": [],
      "tag_meta": {},
      "system_tags": [
        "known_compromise"
      ],
      "user_tags": []
    }
  ]
}
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
