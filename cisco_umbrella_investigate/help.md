# Description

[Cisco Umbrella Enforcement](https://docs.umbrella.com/developer/networkdevices-api/) allows partners and customers with their own homegrown SIEM/Threat Intelligence Platform (TIP) environments to inject events and/or threat intelligence into their Umbrella environment. These events are then instantly converted into visibility and enforcement that can extend beyond the perimeter and thus the reach of the systems that might have generated those events or threat intelligence.
The Cisco Umbrella Enforcement InsightConnect plugin allows you to lookup sample artifacts, sample connections, sample samples, WHOIS details, IP and domain history etc.
This plugin utilizes the [Python OpenDNS Investigate](https://github.com/opendns/pyinvestigate) library.

# Key Features

* Retrieve details of sample artifacts, sample connections, sample samples
* Retrieve WHOIS details by email, domain and name server
* Retrieve IP's and domain's history
* Retrieve domain's security features, content category, security category

# Requirements

* Cisco Umbrella Investigate API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Enter API key e.g. 1452d258-7c12-7c12-7c12-1452d25874c2|None|1452d258-7c12-7c12-7c12-1452d25874c2|

The API key is a UUID-v4 [customer key](https://docs.umbrella.com/developer/enforcement-api/authentication-and-versioning/).

Example input:

```
{
  "api_key": "1452d258-7c12-7c12-7c12-1452d25874c2"
}
```

## Technical Details

### Actions

#### Timeline

This action shows when a domain, IP or URL was given attribution of a particular security categorization or threat type.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Domain name, IP address or URL|None|example.com|

Example input:

```
{
  "name": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timeline|[]timeline|True|Provided data for a queried domain name, IP address or URL|

Example output:

```
{
  "timeline": [
    {
      "attacks": [
        "WebCryptoMiner"
      ],
      "categories": [
        "Cryptomining",
        "Potentially Harmful"
      ],
      "threatTypes": [
        "Potentially Unwanted Application"
      ],
      "timestamp": 1518718964025
    }
  ]
}
```

#### Passive DNS

This action provides historical data from our resolvers for domains, IPs, and other resource records.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Domain name, IP address or text|None|example.com|
|recordType|string|A|False|The record types (A, NS, MX, TXT, CNAME) to return, use commas to separate multiple record types|None|A|
|resource_records|string|Domain|True|Resource records for which historical data is provided|['Domain', 'Name', 'IP Address', 'Raw Text', 'Timeline']|Domain|

Example input:

```
{
  "name": "example.com",
  "recordType": "A",
  "resource_records": "Domain"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|pageInfo|page_info|False|Information about page|
|recordInfo|record_info|False|Information about record|
|records|[]records|False|Provided records for a queried domain name, IP address or text|
|timeline_data|[]dns_timeline|False|Snapshot of passive DNS and categorization history for a queried domain name|

Example output:

```
{
  "records": [
    {
      "minTtl": 86400,
      "maxTtl": 86400,
      "firstSeen": 1403611920,
      "lastSeen": 1602604809,
      "name": "umbrella.com",
      "type": "NS",
      "rr": "auth1.opendns.com.",
      "securityCategories": [],
      "contentCategories": ["Software/Technology"],
      "firstSeenISO": "2014-06-24T12:12Z",
      "lastSeenISO": "2020-10-13T16:00Z"
    },
    {
      "minTtl": 86400,
      "maxTtl": 86400,
      "firstSeen": 1403611920,
      "lastSeen": 1602604809,
      "name": "umbrella.com",
      "type": "NS",
      "rr": "auth2.opendns.com.",
      "securityCategories": [],
      "contentCategories": ["Software/Technology"],
      "firstSeenISO": "2014-06-24T12:12Z",
      "lastSeenISO": "2020-10-13T16:00Z"
    }
  ],
  "pageInfo": {
    "hasMoreRecords": false,
    "offset": 0,
    "limit": 500,
    "totalNumRecords": 2
  },
  "recordInfo": {
    "minTtl": 86400,
    "maxTtl": 86400,
    "totalMaliciousIP": 0
  }
}
```

#### DNS RR History for IP Address

This action is used to return the history that umbrella has seen for a given IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip|string|None|True|IP address|None|198.51.100.100|
|type|string|None|False|DNS record query type (A, NS, MX, TXT and CNAME are supported)|None|NS|

Example input:

```
{
  "domain": "example.com",
  "type": "A"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|features|[]ip_feature|True|Features|
|rrs|[]ip_resource_record|True|RRS|

Example output:

```
{
  "features": [
    {
      "rr_count": 0,
      "ld2_count": 0,
      "ld3_count": 0,
      "ld2_1_count": 0,
      "ld2_2_count": 0,
      "div_ld2": 0.0,
      "div_ld3": 0.0,
      "div_ld2_1": 0.0,
      "div_ld2_2": 0.0
    }
  ],
  "rrs": []
}
```

#### WHOIS by Nameserver

This action is used to allows you to search a nameserver to find all domains registered by that nameserver.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|nameserver|string|None|True|Nameserver's domain name|None|198.51.100.100|

Example input:

```
{
  "nameserver": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain|[]email_whois|True|Array of WHOIS results for the domain provided with all available information|

Example output:

```
{
  "domain": [
    {
      "more_data_available": false,
      "limit": 500,
      "domains": [
        {
          "domain": "carltonmedia.org",
          "current": false
        },
        {
          "domain": "natickpegasus.org",
          "current": false
        },
        {
          "domain": "sevenstar.org.tw",
          "current": false
        }
      ],
      "total_results": 3
    }
  ]
}
```

#### Co-occurrences for a Domain

This action is used to return co-occurrences for the specified domain.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain name|None|example.com|

Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cooccurrences|array|True|Array of [domain name, scores] tuples. The values range between 0 and 1 and should not exceed 1. All co-occurrences of requests from client IPs are returned for the previous seven days whether the co-occurrence is suspicious or not|

Example output:

```
{
  "cooccurrences": [
    [
      "safebrowsing.googleapis.com",
      1.0
    ]
  ]
}
```

#### WHOIS by Domain

This action is used to a standard WHOIS response record for a single domain with all available WHOIS data returned in an array.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain name without wildcards and including TLD|None|example.com|

Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|whois|array|True|Array of WHOIS results for the domain provided with all available information|

Example output:

```
{
  "whois": [
    {
      "administrativeContactFax": null,
      "whoisServers": "whois.markmonitor.com",
      "addresses": [],
      "administrativeContactName": null,
      "zoneContactEmail": null,
      "billingContactFax": null,
      "administrativeContactTelephoneExt": null,
      "administrativeContactEmail": null,
      "technicalContactEmail": null,
      "technicalContactFax": null,
      "nameServers": [
        "ns-1390.awsdns-45.org",
        "ns-1653.awsdns-14.co.uk",
        "ns-439.awsdns-54.com",
        "ns-739.awsdns-28.net"
      ],
      "zoneContactName": null,
      "billingContactPostalCode": null,
      "zoneContactFax": null,
      "registrantTelephoneExt": null,
      "zoneContactFaxExt": null,
      "technicalContactTelephoneExt": null,
      "billingContactCity": null,
      "zoneContactStreet": [],
      "created": "2000-05-25",
      "administrativeContactCity": null,
      "registrantName": null,
      "zoneContactCity": null,
      "domainName": "rapid7.com",
      "zoneContactPostalCode": null,
      "administrativeContactFaxExt": null,
      "technicalContactCountry": "UNITED STATES",
      "registrarIANAID": "292",
      "updated": "2019-04-24",
      "administrativeContactStreet": [],
      "billingContactEmail": null,
      "status": [
        "clientDeleteProhibited clientTransferProhibited clientUpdateProhibited"
      ],
      "registrantCity": null,
      "billingContactCountry": null,
      "expires": "2021-05-25",
      "technicalContactStreet": [],
      "registrantOrganization": "Rapid7",
      "billingContactStreet": [],
      "registrarName": "MarkMonitor, Inc.",
      "registrantPostalCode": null,
      "zoneContactTelephone": null,
      "registrantEmail": null,
      "technicalContactFaxExt": null,
      "technicalContactOrganization": "Rapid7",
      "emails": [],
      "registrantStreet": [],
      "technicalContactTelephone": null,
      "technicalContactState": "MA",
      "technicalContactCity": null,
      "registrantFax": null,
      "registrantCountry": "UNITED STATES",
      "billingContactFaxExt": null,
      "timestamp": null,
      "zoneContactOrganization": null,
      "administrativeContactCountry": "UNITED STATES",
      "billingContactName": null,
      "registrantState": "MA",
      "registrantTelephone": null,
      "administrativeContactState": "MA",
      "registrantFaxExt": null,
      "technicalContactPostalCode": null,
      "zoneContactTelephoneExt": null,
      "administrativeContactOrganization": "Rapid7",
      "billingContactTelephone": null,
      "billingContactTelephoneExt": null,
      "zoneContactState": null,
      "administrativeContactTelephone": null,
      "billingContactOrganization": null,
      "technicalContactName": null,
      "administrativeContactPostalCode": null,
      "zoneContactCountry": null,
      "billingContactState": null,
      "auditUpdatedDate": "2019-05-28 05:23:28.000 UTC",
      "recordExpired": false,
      "timeOfLatestRealtimeCheck": 1559048253693,
      "hasRawText": true
    }
  ]
}
```

#### Related Domains

This action is used to returns a list of domain names that have been frequently seen.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain name|None|example.com|

Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|related|array|True|Array of [domain name, scores] tuples where the score is the number of client IP requests to the site in 60 seconds from the time of the original lookup request|

Example output:

```
{
  "related": [
    [
      "octoperf.com",
      4
    ],
    [
      "blog.rapid7.com",
      3
    ]
  ]
}
```

#### File Sample

This action is used to return a file, or a file-like object, such as a process running in memory.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|Search sample by hash (SHA-256, SHA-1 or MD5)|None|9de5069c5afe602b2ea0a04b66beb2c0|
|limit|string|None|False|Default of 10, can be extended for a larger data set|None|10|
|offset|string|None|False|The offset of the individual entities in the query’s response, used for pagination|None|10|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0",
  "limit": 10,
  "offset": 10
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sample|sample_info|False|Sample|

Example output:

```
{
  "sha256": "65f33f9e6d16918ba72bc20bcd85ebd75bc735df5666a843cab9c6dec9c0b1c1",
  "sha1": "ccdeb2319d6b924e359f563527404a0af3d1ac54",
  "md5": "0c340a220817e157346bef7976a0d0b6",
  "magicType": "PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed",
  "threatScore": 100,
  "size": 22020,
  "firstSeen": 1466410880000,
  "lastSeen": 1518410873000,
  "visible": false,
  "avresults": [
    {
      "signature": "Win.Worm.Mydoom",
      "product": "ClamAV"
    }
  ],
  "samples": {
    "totalResults": 0,
    "moreDataAvailable": false,
    "limit": 1,
    "offset": 0,
    "samples": []
  },
  "connections": {
    "totalResults": 1,
    "moreDataAvailable": true,
    "limit": 1,
    "offset": 0,
    "connections": [
      {
        "name": "166.16.123.158",
        "firstSeen": 1518410873000,
        "lastSeen": 1518410873000,
        "lastCommit": null,
        "securityCategories": [],
        "attacks": [],
        "threatTypes": [],
        "type": "IP",
        "firstQueried": null,
        "popularity": null,
        "popularityWeek": null,
        "popularity1Month": null,
        "popularity3Month": null,
        "ips": [],
        "urls": []
      }
    ]
  },
  "behaviors": [
    {
      "name": "registry-autorun-key-modified",
      "title": "Process Modified Autorun Registry Key Value",
      "hits": 1,
      "confidence": 60,
      "severity": 80,
      "tags": [
        "process",
        "autorun",
        "registry"
      ],
      "threat": 48,
      "category": [
        "persistence"
      ]
    },
    {
      "name": "pe-packed-upx",
      "title": "Executable Packed with UPX",
      "hits": 200,
      "confidence": 30,
      "severity": 30,
      "tags": [
        "packer",
        "crypter",
        "encoding",
        "PE"
      ],
      "threat": 9,
      "category": [
        "attribute"
      ]
    }
  ]
}
```

#### DNS RR History

This action is used to return the history that Umbrella has seen for a given domain.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain name|None|example.com|
|type|string|None|False|DNS record query type (A, NS, MX, TXT and CNAME are supported)|None|A|

Example input:

```
{
  "domain": "example.com",
  "type": "A"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|features|[]feature|True|Features|
|rrs_tf|[]resource_record|True|RRS TF|

Example output:

```
{
  "features": [
    {
      "base_domain": "example.com",
      "is_subdomain": false,
      "age": 92,
      "ttls_mean": 43823.260869565216,
      "ttls_min": 3535,
      "ttls_max": 86400,
      "ttls_median": 7200.0,
      "ttls_stddev": 40782.635787281266,
      "country_codes": [
        "DE",
        "US"
      ],
      "country_count": 2,
      "locations": [
        {
          "lat": 41.26190185546875,
          "lon": -95.86080169677734
        },
        {
          "lat": 47.9989013671875,
          "lon": 11.176803588867188
        }
      ],
      "locations_count": 4,
      "asns": [
        15169,
        25560,
        24940,
        15133
      ],
      "asns_count": 4,
      "non_routable": false,
      "mail_exchanger": true,
      "geo_distance_sum": 13973.73568990544,
      "geo_distance_mean": 3493.43392247636,
      "rips_stability": 0.1111111111111111,
      "rips": 5,
      "div_rips": 0.8,
      "ff_candidate": false,
      "prefixes": [
        "93.184.216.0",
        "95.143.160.0",
        "88.198.0.0",
        "23.236.48.0"
      ],
      "prefixes_count": 4,
      "cname": false
    }
  ],
  "rrs_tf": [
    {
      "rrs": [
        {
          "name": "example.com.",
          "ttl": 3600,
          "type": "A",
          "rr": "23.236.62.147",
          "class": "IN"
        }
      ],
      "first_seen": "2020-08-27",
      "last_seen": "2020-08-27"
    },
    {
      "rrs": [
        {
          "name": "example.com.",
          "ttl": 3600,
          "type": "A",
          "rr": "23.236.62.147",
          "class": "IN"
        },
        {
          "name": "example.com.",
          "ttl": 86400,
          "type": "A",
          "rr": "93.184.216.34",
          "class": "IN"
      ],
      "first_seen": "2020-08-26",
      "last_seen": "2020-08-26"
    },
    {
      "rrs": [
        {
          "name": "example.com.",
          "ttl": 3600,
          "type": "A",
          "rr": "95.143.172.244",
          "class": "IN"
        }
      ],
      "first_seen": "2020-08-25",
      "last_seen": "2020-08-25"
    },
    {
      "rrs": [
        {
          "name": "example.com.",
          "ttl": 3600,
          "type": "A",
          "rr": "23.236.62.147",
          "class": "IN"
        }
      ],
      "first_seen": "2020-08-24",
      "last_seen": "2020-08-24"
    },
    {
      "rrs": [
        {
          "name": "example.com.",
          "ttl": 3600,
          "type": "A",
          "rr": "95.143.172.244",
          "class": "IN"
        }
      ],
      "first_seen": "2020-08-23",
      "last_seen": "2020-08-23"
    },
    {
      "rrs": [
        {
          "name": "example.com.",
          "ttl": 3600,
          "type": "A",
          "rr": "95.143.172.244",
          "class": "IN"
        }
      ],
      "first_seen": "2020-08-22",
      "last_seen": "2020-08-22"
    },
    {
      "rrs": [
        {
          "name": "example.com.",
          "ttl": 3600,
          "type": "A",
          "rr": "23.236.62.147",
          "class": "IN"
        }
}
```

#### Latest Malicious Domains by IP

This action is used to return associated malicious domains for an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ip|string|None|True|IP Address to check for malicious domains|None|198.51.100.100|

Example input:

```
{
  "ip": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|[]string|True|The block list domain associated with the IP|

Example output:

```

```

#### Sample Artifacts

This action is used to return artifacts which are files created or modified during a sample analysis.
*Note:* Only Threat Grid customers have access to artifact data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|Search sample by hash (SHA-256, SHA-1 or MD5)|None|9de5069c5afe602b2ea0a04b66beb2c0|
|limit|string|None|False|Default of 10, can be extended for a larger data set|None|10|
|offset|string|None|False|Used to paginate between sets of data|None|5|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0",
  "limit": 10,
  "offset": 5
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|artifacts|array|True|Artifacts|

Example output:

```

```

#### WHOIS Information by Email

This action is used to returns the WHOIS information for the specified email address(es), nameserver(s) and domains.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email address following rfc5322 conventions|None|user@example.com|

Example input:

```
{
  "email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email_whois|[]email_whois|True|Domains registered by this email address|

Example output:

```
{
  "email_whois": [
    {
      "more_data_available": false,
      "limit": 500,
      "domains": [],
      "total_results": 0
    }
  ]
}
```

#### Sample Connections

This action is used to return network activity information associated with a sample.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|Search sample by hash (SHA-256, SHA-1 or MD5)|None|9de5069c5afe602b2ea0a04b66beb2c0|
|limit|string|None|False|Default of 10, can be extended for a larger data set|None|10|
|offset|string|None|False|Used to paginate between sets of data|None|10|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0",
  "limit": 10,
  "offset": 10
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|connections|array|True|Connections|

Example output:

```
{
  "totalResults": 10,
  "moreDataAvailable": true,
  "limit": 10,
  "offset": 5,
  "connections": [
    {
      "name": "aer-mx-01.cisco.com",
      "firstSeen": 1518410872000,
      "lastSeen": 1518410873000,
      "lastCommit": null,
      "securityCategories": [],
      "attacks": [],
      "threatTypes": [],
      "type": "HOST",
      "firstQueried": null,
      "popularity": null,
      "popularityWeek": null,
      "popularity1Month": null,
      "popularity3Month": null,
      "ips": [
        "173.38.212.150"
      ],
      "urls": []
    },
    {
      "name": "16.150.109.72",
      "firstSeen": 1518410873000,
      "lastSeen": 1518410873000,
      "lastCommit": null,
      "securityCategories": [],
      "attacks": [],
      "threatTypes": [],
      "type": "IP",
      "firstQueried": null,
      "popularity": null,
      "popularityWeek": null,
      "popularity1Month": null,
      "popularity3Month": null,
      "ips": [],
      "urls": []
    }
  ]
}
```

#### Pattern Search

This action is used to the pattern search functionality in investigate uses regular expressions (regex) to search against the investigate database.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|expression|string|None|True|A standard RegEx pattern search|None|..example.com|
|include_category|boolean|None|False|Default is false, if set to true this will include security categories in the results and may slow the return times|None|False|
|limit|integer|None|False|Default is 1000, limit request response|None|1000|
|start|string|None|True|If specifying in absolute, use millisecond timestamp within the last 30 days as the Start. If specifying in relative, use either seconds, minutes, hours, days or weeks with a minus sign in front. As an example -1days, -1000minutes|None|-1000minutes|

Example input:

```
{
  "expression": "..example.com",
  "include_category": false,
  "limit": 1000,
  "start": "-1000minutes"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|expression|string|True|This is the RegEx in the query as seen from the API. If results from your query do not match what you may have expected, check to see that the RegEx matches the one you tried to enter and that characters are correctly escaped in the query string|
|limit|integer|True|Default is 100, can be expanded to 1000 which is the maximum number of results for this endpoint|
|matches|array|True|Each match will contain the name of the domain matches, the and the first seen time, both in Epoch and ISO time format. This endpoint returns the security categories as strings rather than integers (eg: 'malware','botnet', etc) if includeCategory is true|
|moreDataAvailable|boolean|True|Whether more data is available than what is displayed. Will be true if totalResults exceed limit. We recommend refining your filter if this value is true|
|totalResults|integer|True|Total results from this search string. The default number of results is 100 and can be expanded using the limit parameter|

Example output:

```

```

#### Domain Status and Categorization

This action is used to return if domain has been flagged as malicious by the cisco security labs team.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domains|[]string|None|True|Domain names|None|example.com|

Example input:

```
{
  "domains": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|categories|[]category|True|Information about content categories and security categories|

Example output:

```
{
  "categories": [
    {
      "name": "rapid7.com",
      "status": 1,
      "security_categories": [],
      "content_categories": [
        "Software/Technology",
        "Computer Security"
      ]
    }
  ]
}
```

#### Domain Tags

This action is used to returns the date range when the domain being queried was a part of the umbrella block list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain name|None|example.com|

Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain_tags|[]tag_date|True|Date range for which this domain has been in the block list, domain tag such as malware or phishing, identifying the security category of the domain, if available or possible, list the specific URL hosting the malicious content|

Example output:

```

```

#### Samples by Domain

This action is used to return all samples associated with the domain.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|limit|string|None|False|The number of responses; default of 10 as a limit on response, can be extended|None|10|
|offset|string|None|False|Default to 0, used to pagination between sets of data if limit is exceeded|None|10|
|sortby|string|None|False|Default is score. Choose from ['first-seen', 'last-seen', 'score']. 'first-seen' sorts the samples in date descending order. 'last-seen' sorts the samples in ascending order. 'score' sorts the samples by the ThreatScore|None|first-seen|
|url|string|None|True|Search sample by domain, IP|None|example.com|

Example input:

```
{
  "limit": 10,
  "offset": 10,
  "sortby": "first-seen",
  "url": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|limit|integer|True|Number of sample results|
|moreDataAvailable|boolean|True|If more data is available. Extend the limit and/or offset to view|
|offset|integer|True|The offset of the individual entities in the query’s response; used for pagination|
|query|string|True|What string was queried or seen by the API|
|samples|[]sample_info|True|Information about the actual sample|
|totalResults|integer|True|The number of results returned. Same as limit if limit is reached and moreDataAvailable is true|

Example output:

```
{
  "query": "rapid7.com",
  "totalResults": 2,
  "moreDataAvailable": true,
  "limit": 2,
  "offset": 2,
  "samples": [
    {
      "sha256": "6842039f6c7b11595c09f9fb5be68a02dea5da16a6a9eadf23de3aa2b3f0d6ab",
      "sha1": "713469e07f2940bf5c5c2a71f577395c5ffd1707",
      "md5": "c47a40abfa1936b2a7ad19c57d5f6cb8",
      "magicType": "MS Windows 95 Internet shortcut text (URL=<http://info.rapid7.com/z0qY1JG0000AaZqSNSe0K00>), ASCII text",
      "threatScore": 64,
      "size": 69,
      "firstSeen": 1593103899000,
      "lastSeen": 1593103899000,
      "visible": true,
      "avresults": [],
      "behaviors": []
    },
    {
      "sha256": "8506457d830242fe8abbfe67d65ca5c5ff01339dc2da3ca25d175e7e9b04c967",
      "sha1": "6f034f7a8ced16b918d8325d0c2b2ccb8c445750",
      "md5": "d1db6afeceed26829d520967db359f92",
      "magicType": "PDF document, version 1.7",
      "threatScore": 81,
      "size": 16483096,
      "firstSeen": 1588247793000,
      "lastSeen": 1588247798000,
      "visible": true,
      "avresults": [],
      "behaviors": []
    }
  ]
}
```

#### Other Samples

This action is used to return other samples associated with a sample.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|Search sample by hash (SHA-256, SHA-1 or MD5)|None|9de5069c5afe602b2ea0a04b66beb2c0|
|limit|string|None|False|Default of 10, can be extended for a larger data set|None|10|
|offset|string|None|False|Used to paginate between sets of data|None|10|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0",
  "limit": 10,
  "offset": 10
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|samples|array|True|Samples|

Example output:

```

```

#### Security Information

This action is used to returns scores or security features.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain name|None|example.com|

Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asn_score|number|False|ASN reputation score, ranges from -100 to 0 with -100 being very suspicious|
|attack|string|False|The name of any known attacks associated with this domain. Returns blank if no known threat associated with domain|
|dga_score|number|True|Domain Generation Algorithm. This score is generated based on the likeliness of the domain name being generated by an algorithm rather than a human|
|entropy|number|True|The number of bits required to encode the domain name, as a score. This score is to be used in conjunction with DGA and Perplexity|
|geodiversity|array|True|A score representing the number of queries from clients visiting the domain, broken down by country. Score is a non-normalized ratio between 0 and 1|
|geodiversity_normalized|array|True|A score representing the amount of queries for clients visiting the domain, broken down by country. Score is a normalized ratio between 0 and 1|
|geoscore|number|True|A score that represents how far the different physical locations serving this name are from each other|
|ks_test|number|True|Kolmogorov–Smirnov test on geodiversity. 0 means that the client traffic matches what is expected for this TLD|
|pagerank|number|True|Popularity according to Google's pagerank algorithm|
|perplexity|number|True|A second score on the likeliness of the name to be algorithmically generated, on a scale from 0 to 1|
|popularity|number|True|The number of unique client IPs visiting this site, relative to the all requests to all sites. A score of how many different client/unique IPs go to this domain compared to others|
|prefix_score|number|False|Prefix ranks domains given their IP prefixes (an IP prefix is the first three octets in an IP address) and the reputation score of these prefixes. Ranges from -100 to 0, -100 being very suspicious|
|rip_score|number|False|RIP ranks domains given their IP addresses and the reputation score of these IP addresses. Ranges from -100 to 0, -100 being very suspicious|
|securerank2|number|True|Securerank is designed to identify hostnames requested by known infected clients but never requested by clean clients, assuming these domains are more likely to be bad. Scores range from -100 (suspicious) to 100 (benign)|
|threat_type|string|False|The type of the known attack, such as botnet or APT. Returns blank if no known threat associated with domain|
|tld_geodiversity|array|True|A score that represents the TLD country code geodiversity as a percentage of clients visiting the domain. Occurs most often with domains that have a ccTLD. Score is normalized ratio between 0 and 1|

Example output:

```
{
  "dga_score": 0.0,
  "perplexity": 0.2727996425912349,
  "entropy": 2.8073549220576037,
  "securerank2": -0.0019093637905225065,
  "pagerank": 0.0,
  "asn_score": -0.03841224692930313,
  "prefix_score": -0.04483817171527547,
  "rip_score": 0.0,
  "popularity": 0.0,
  "fastflux": false,
  "geodiversity": [
    [
      "US",
      0.5
    ],
    [
      "GB",
      0.2333
    ]
  ],
  "geodiversity_normalized": [
    [
      "NZ",
      0.39535205076951657
    ]
  ],
  "tld_geodiversity": [],
  "geoscore": 0.0,
  "ks_test": 0.0,
  "attack": "",
  "threat_type": "",
  "found": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### category

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Content Categories|array|False|The Umbrella content category or categories that match this domain. If none match, the return will be blank|
|Name|string|False|Domain name|
|Security Categories|array|False|The Umbrella security category, or categories, that match this domain or that this domain is associated with. If none match, the return will be blank|
|Status|integer|False|The status will be '-1' if the domain is believed to be malicious, '1' if the domain is believed to be benign, '0' if it hasn't been classified yet|

#### dns_timeline

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Date|date|False|The date|
|DNS Data|array|False|Contains the DNS record type and data that started/stopped being seen on the given date|

#### email_whois

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Domains|[]whois_domain|True|Domains registered by this email and whether the domain is current, meaning currently registered by this email address|
|Limit|integer|True|Total number of results for this page of results, default 500|
|More Data Available|boolean|True|Whether or not there are more than 500 results for this email, either yes or no|
|Total Results|integer|False|Total number of results for this email|

#### feature

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Age|integer|False|The day in days between now and the last request for this domain. This value is only useful if present. A low score helps isolate attack domains that are short-lived|
|ASNs|array|False|List of ASN numbers the IPs are in|
|ASNs Count|integer|False|Number of ASNs the IPs map to|
|Base Domain|string|True|The base domain of the requested domain|
|CNAME|boolean|False|Returns true if a CNAME record has been seen for this domain name|
|Country Codes|array|False|List of country codes (ex: US, FR, TW) for the IPs the name maps to|
|Country Count|integer|False|Number of countries the IPs are hosted in|
|Div Rips|number|False|The number of prefixes over the number of IPs|
|FF Candidate|boolean|False|If the domain name looks like a candidate for fast flux. This does not necessarily mean the domain is in fast flux, but rather that the IP address the domain resolves to changes rapidly (or has changed rapidly)|
|Geo Distance Mean|number|False|Mean distance between the geo median and each location, in kilometers|
|Geo Distance Sum|number|False|Minimum sum of distance between locations, in kilometers|
|Is Subdomain|boolean|True|Returns true if the requested domain is a subdomain of another|
|Locations|array|False|List of geo coordinates (WGS84 datum, decimal format) the IPs are mapping to|
|Locations Count|integer|False|Number of distinct geo coordinates the IPs are mapping to|
|Mail Exchanger|boolean|False|If an MX query for this domain name has been seen|
|Non Routable|boolean|False|If one of the IPs is in a reserved, non-routable IP range|
|Prefixes|array|False|List of network prefixes the IPs map to|
|Prefixes Count|integer|False|Number of network prefixes the IPs map to|
|Rips|integer|False|Number of IPs seen for the domain name|
|Rips Stability|number|False|1.0 divided by the number of times the set of IP addresses changed|
|TTL Max|integer|False|Maximum amount of time set that DNS records should be cached|
|TTL Mean|number|False|Average amount of time set that DNS records should be cached|
|TTL Median|number|False|Median amount of time set that DNS records should be cached|
|TTL Min|integer|False|Minimum amount of time set that DNS records should be cached|
|TTL Standard Deviation|number|False|Standard deviation of the amount of time set that DNS records should be cached|

#### ip_feature

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Div Ld2|number|True|ld2_count divided by the number of records|
|Div Ld2 1|number|True|ld2_1_count divided by the number of records|
|Div Ld2 2|number|True|ld2_2_count divided by the number of records|
|Div Ld3|number|True|ld3_count divided by the number of records|
|Ld2 1 Count|integer|True|Number of 2-level names, without the TLD, mapping to the given IP (for www.example.com, this considers example)|
|Ld2 2 Count|integer|True|Number of 3-level names, without the TLD, mapping to a given IP (for www.example.com, this considers www.example)|
|Ld2 Count|integer|True|Number of 2-level names mapping to the given IP (for www.example.com, this considers example.com)|
|Ld3 Count|integer|True|Number of 3-level names mapping to the given IP (for www.example.com, this considers www.example.com)|
|Rr Count|integer|True|Number of records of that type mapping to the given IP|

#### ip_resource_record

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Class|string|True|DNS class type|
|Name|string|True|The looked up IP address|
|Rr|string|True|Resource record owner|
|Ttl|integer|False|Time to live for this record|
|Type|string|True|Query type|

#### page_info

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Has More Records|boolean|False|Whether the query has more records|
|Limit|integer|False|The maximum number of records to return|
|Offset|integer|False|The amount by which to offset the records|
|Total Number Of Records|integer|False|Total number of records provided for a query|

#### record_info

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Maximum TTL|integer|False|The maximum TTL for the record in seconds|
|Minimum TTL|integer|False|The minimum TTL for the record in seconds|
|Total Malicious Domain|integer|False|Total number of malicious domains for a query|
|Total Malicious IP|integer|False|Total number of malicious IPs for a query|

#### records

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Content Categories|array|False|The Umbrella content categories|
|First Seen|integer|False|The first time a query was seen by Umbrella for the domain, in epoch time|
|First Seen ISO|string|False|The first time a query was seen by Umbrella for the domain, in ISO date and time format|
|Last Seen|integer|False|The last time a query was seen by Umbrella for the domain, in epoch time|
|Last Seen ISO|string|False|The last time a query was seen by Umbrella for the domain, in ISO date and time format|
|Maximum TTL|integer|False|The maximum TTL for the record in seconds|
|Minimum TTL|integer|False|The minimum TTL for the record in seconds|
|Name|string|False|The query|
|RR|string|False|The DNS resource record (RR)|
|Security Categories|array|False|The Umbrella security categories|
|Type|string|False|The DNS record type|

#### resource_record

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Class|string|False|DNS class type|
|First Seen|string|True|Date when the domain was first seen to our DNS database|
|Last Seen|string|True|Date when domain was last seen in our DNS database|
|Name|string|False|Name of the domain|
|RR|string|False|Resource record IP for the domain|
|TTL|integer|False|TTL of the domain|
|Type|string|False|Query type|

#### sample_info

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AV Results|array|True|AntiVirus results according to ClamAV. A sample can have more than one signature if it is possibly detected under more than one family of malware. A sample may also have no signatures associated|
|FirstSeen|number|True|The epoch time stamp for when this sample was first seen by Threat Grid|
|LastSeen|number|True|The epoch time stamp for when this sample was last seen by Threat Grid. The lastSeen and firstSeen will often be the same if the sample is more recent|
|MagicType|string|True|A ‘magic type’ is better understood as a file type. Specifically, it is the output of the Linux “file” utility|
|MD5|string|True|The MD5 checksum of the sample, as above, can be searched in /sample/ endpoint|
|SHA1|string|True|The SHA1 checksum of the sample. As above, can be searched in /sample/ endpoint|
|SHA256|string|True|The SHA256 checksum of the sample. This checksum is important if you’d like to find out more about this sample in the /sample/ endpoint|
|Size|integer|True|The size of the sample in bytes|
|ThreatScore|integer|True|A threatScore is a measure of the amount of system weakening, obfuscation, persistence, modification, data exfiltration, and other behaviors which may be a threat to the host system’s integrity|
|Visible|boolean|True|Boolean, either true or false. For internal Umbrella use only, please ignore|

#### tag_date

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Begin|string|True|The date of adding the domain to the block list. If the domain is currently in the block list, this date will be 'Current'|
|Category|string|True|The Umbrella security category or categories that match this domain|
|End|string|True|The date of removing the domain to the block list. If the domain is currently in the block list, this date will be 'Current'|
|URL|string|True|The full URL containing the malicious code at the domain requested. Return is null if URL is not available|

#### timeline

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attacks|array|False|Which named attacks, if any, matched the input|
|Categories|array|False|Which Umbrella security category, if any, matched the input|
|Threat Types|array|False|Which threat type, if any, matched in the input|
|Timestamp|integer|False|The time when the attribution for this domain or URL changed. This is given in epoch (unix) time stamps|

#### whois_domain

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Current|boolean|True|Whether the domain is current, meaning currently registered by this email address|
|Domain|string|True|Domain registered by this email|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 3.1.0 - Add Passive DNS and Timeline actions
* 3.0.0 - Add action input and output examples to documentation | Set `title` in action input and output sections in schema | Update domain name in `investigate.py` | Improve error handling | Change action input names to lowercase in action Latest Malicious Domains by IP, DNS RR History for IP Address and Samples by Domain
* 2.0.0 - New spec and help.md format for the Extension Library | Fix spelling of variable titled Co-occurrences
* 1.0.2 - Added change allowing categorization to work with a Tier1 API key by utilizing the single domain API endpoint instead of the bulk API endpoint when a single-element array of domains is passed in
* 1.0.1 - Add connection test | Fix where connection was returning "Wrong api_key" on valid keys | Run plugin as least privileged user | Update to use the `komand/python-3-slim-plugin` Docker image to reduce plugin size
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Cisco Umbrella Investigate](https://learn-umbrella.cisco.com/threat-intelligence/cisco-umbrella-investigate-overview)
* [Python OpenDNS Investigate](https://github.com/opendns/pyinvestigate)
* [Authentication](https://docs.umbrella.com/developer/enforcement-api/authentication-and-versioning/)
