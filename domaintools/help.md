# Description

[DomainTools](https://www.domaintools.com) data and products work in harmony to enable security teams to start getting ahead of attacks, gain context and visibility into potential threats, and lower the skills barrier. The DomainTools plugin for InsightConnect allows for the automation of domain lookups and retrieval of threat information related to the domain.

This plugin utilizes the [DomainTools Python API](https://github.com/domaintools/python_api).

# Key Features

* Whois
* Domain search
* Brand monitor

# Requirements

* Requires an API Key from DomainTools

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|False|Enter the API username|None|
|key|credential_token|None|True|Enter the API key|None|

## Technical Details

### Actions

#### Brand Monitor

This action is used to search across all new domain registrations worldwide.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|One or more terms separated by the pipe character|None|
|days_back|integer|0|False|Use this parameter when you need to search domains registered up to six days prior to the current date|None|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|
|exclude|string|None|False|Domain names with these words will be excluded from the result set. Separate multiple terms with the pipe character|None|
|domain_status|string|None|False|Sets the scope of domain names to search|['new', 'on-hold']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|brand_monitor_response|False|None|

Example output:

```

{
  "response": {
  "exclude": [],
  "total": 5,
  "date": "2017-05-17",
  "new": true,
  "alerts": [
    {
      "domain": "africangoogle.com",
      "status": "new"
    },
    {
      "domain": "immogoogle.com",
      "status": "new"
    },
    {
      "domain": "myindiagoogle.com",
      "status": "new"
    },
    {
      "domain": "obgoogle.com",
      "status": "new"
    },
    {
      "domain": "youtubetogoogle.com",
      "status": "new"
    }
  ],
  "utf8": false,
  "query": "google.com",
  "limit": 5000,
  "on-hold": false
  }
}

```

#### IP Monitor

This action is used to retrieve the daily activity of all our monitored TLDs on any given IP address

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|One or more terms separated by the pipe character|None|
|days_back|integer|0|False|Use this parameter when you need to search domains registered up to six days prior to the current date| [1, 2, 3, 4, 5, 6]|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|ip_monitor_response|False|None|

Example output:

```

{
  "response": {
    "date": "2017-05-17",
    "total": "0",
    "limit": 1000,
    "ip_address": "65.55.53.233",
    "page_count": 0,
    "alerts": [],
    "page": 1
  }
}

```

#### Name Server Monitor

This action is used to search the daily activity of all our monitored TLDs on any given name server

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|One or more terms separated by the pipe character|None|
|days_back|integer|0|False|Use this parameter when you need to search domains registered up to six days prior to the current date| [1, 2, 3, 4, 5, 6]|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|name_server_monitor_response|False|None|

Example output:

```

{
  "response": {
    "name_server": "google.com",
    "total": "50",
    "alerts": [
      {
        "new_name_server": "google.com",
        "action": "Transfer In",
        "old_name_server": "bluehost.com",
        "domain": "AARZ.PK"
      },
      {
        "new_name_server": "ahack.ru",
        "action": "Transfer Out",
        "old_name_server": "google.com",
        "domain": "AHCO.RU"
      }
    ],
    "page_count": 1,
    "limit": 1000,
    "page": 1,
    "date": "2017-05-18"
  }
}

```

#### Domain Search

This action is used to search for domain names that match your specific search string

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|each term in the query string must be at least three characters long|None|
|exclude_query|string|None|False|Terms to exclude from matching - each term in the query string must be at least three characters long|None|
|max_length|integer|25|False|Limit the maximum domain character count|None|
|min_length|integer|25|False|Limit the minimum domain character count|None|
|has_hyphen|boolean|True|False|Return results with hyphens in the domain name|None|
|has_hyphen|boolean|True|False|Return results with numbers in the domain name|None|
|active_only|boolean|False|Fase|Return only domains currently registered|None|
|deleted_only|boolean|False|Fase|Return only domains previously registered but not currently registered|None|
|anchor_left|boolean|False|Fase|Return only domains that start with the query term|None|
|anchor_right|boolean|False|Fase|Return only domains that end with the query term|None|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|domain_search_response|False|None|

Example output:

```

{
  "response": {
    "results": [],
    "query_info": {
      "anchor_left": false,
      "min_length": 1,
      "has_hyphen": true,
      "exclude_query": "",
      "page": 1,
      "has_number": true,
      "limit": 100,
      "active_only": false,
      "max_length": 25,
      "anchor_right": false,
      "deleted_only": false,
      "total_results": 0
    }
  }
}

```

#### Domain Profile

This action is used to provide basic domain name registration details and a preview of additional data

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|False|Domain name you wish to query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|domain_profile_response|False|None|

Example output:

```

{
  "response": {
    "registrant": {
      "domains": 19325,
      "product_url": "https://reversewhois.domaintools.com/?all[]=Google+Inc.&none[]=",
      "name": "Google Inc."
    },
    "website_data": {
      "response_code": 200,
      "meta": {
        "description": "Search the world s information, including webpages, images, videos and more. Google has many special features to help you find exactly what you re looking for."
      },
      "server": "gws",
      "product_url": "https://whois.domaintools.com/google.com",
      "title": "Google"
    },
    "name_servers": [
      {
        "server": "NS1.GOOGLE.COM",
        "product_url": "https://reversens.domaintools.com/search/?q=NS1.GOOGLE.COM"
      },
      {
        "server": "NS2.GOOGLE.COM",
        "product_url": "https://reversens.domaintools.com/search/?q=NS2.GOOGLE.COM"
      },
      {
        "server": "NS3.GOOGLE.COM",
        "product_url": "https://reversens.domaintools.com/search/?q=NS3.GOOGLE.COM"
      },
      {
        "server": "NS4.GOOGLE.COM",
        "product_url": "https://reversens.domaintools.com/search/?q=NS4.GOOGLE.COM"
      }
    ],
    "history": {
      "registrar": {
        "events": 3,
        "product_url": "https://research.domaintools.com/research/hosting-history/?q=google.com",
        "earliest_event": "2002-10-03"
      },
      "ip_address": {
        "events": 299,
        "timespan_in_years": 14,
        "product_url": "https://research.domaintools.com/research/hosting-history/?q=google.com"
      },
      "name_server": {
        "events": 0,
        "timespan_in_years": 0,
        "product_url": "https://research.domaintools.com/research/hosting-history/?q=google.com"
      },
      "whois": {
        "records": 5267,
        "earliest_event": "2001-05-03",
        "product_url": "https://research.domaintools.com/research/whois-history/search/?q=google.com"
      }
    },
    "server": {
      "product_url": "https://reverseip.domaintools.com/search/?q=google.com",
      "ip_address": "64.233.160.99",
      "other_domains": 34
    },
    "registration": {
      "registrar": "MARKMONITOR INC.",
      "created": "1997-09-15",
      "updated": "2011-07-20",
      "statuses": [
        "clientDeleteProhibited",
        "clientTransferProhibited",
        "clientUpdateProhibited",
        "serverDeleteProhibited",
        "serverTransferProhibited",
        "serverUpdateProhibited"
      ],
      "expires": "2020-09-14"
    },
    "seo": {
      "product_url": "https://research.domaintools.com/seo-browser/?domain=google.com",
      "score": 89
    }
  }
}

```

#### Hosting History

This action is used to provide a list of changes that have occurred in a Domain Names registrar, IP address, and name servers

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name you wish to query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|hosting_history_response|False|None|

Example output:

```

{
  "response": {
    "registrar_history": [
      {
        "registrartag": "Alldomains",
        "date_created": "1997-09-15",
        "date_lastchecked": "2005-07-19",
        "registrar": "Alldomains",
        "date_expires": "2011-09-14",
        "domain": "GOOGLE.COM",
        "date_updated": "2002-10-03"
      },
      {
        "registrartag": "eMarkMonitor",
        "date_created": "1997-09-15",
        "date_lastchecked": "2006-11-20",
        "registrar": "MarkMonitor",
        "date_expires": "2011-09-14",
        "domain": "GOOGLE.COM",
        "date_updated": "2006-04-10"
      }
    ],
    "ip_history": [
      {
        "pre_ip": "",
        "action": "N",
        "actiondate": "2004-04-24",
        "action_in_words": "New",
        "domain": "GOOGLE.COM",
        "post_ip": "216.239.57.99"
      },
      {
        "pre_ip": "216.239.57.99",
        "action": "C",
        "actiondate": "2004-05-08",
        "action_in_words": "Change",
        "domain": "GOOGLE.COM",
        "post_ip": "66.102.7.99"
      }
    ],
    "domain_name": "google.com",
    "nameserver_history": []
  }
}

```

#### Reputation

This action is used to retrieve reputation score of specified domain name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Input domain for which the risk score is desired|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|reputation_response|False|None|

Example output:

```

{
  "response": {
    "domain": "google.com",
    "risk_score": 0
  }
}

```

#### Parsed WHOIS

This action is used to provide parsed information extracted from the raw WHOIS record

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name you wish to query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|parsed_whois__response|False|None|

Example output:

```

{
  "response": {
    "name_servers": [
      "NS1.GOOGLE.COM",
      "NS2.GOOGLE.COM",
      "NS3.GOOGLE.COM",
      "NS4.GOOGLE.COM"
    ],
    "registration": {
      "expires": "2020-09-14",
      "updated": "2011-07-20",
      "registrar": "MARKMONITOR INC.",
      "statuses": [
        "clientDeleteProhibited",
        "clientTransferProhibited",
        "clientUpdateProhibited",
        "serverDeleteProhibited",
        "serverTransferProhibited",
        "serverUpdateProhibited"
      ],
      "created": "1997-09-15"
    },
    "record_source": "google.com",
    "whois": {
      "date": "2017-05-17",
      "record": "Domain Name: google.com\nRegistry Domain ID: 2138514_DOMAIN_COM-VRSN\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar URL: http://www.markmonitor.com\nUpdated Date: 2015-06-12T10:38:52-0700\nCreation Date: 1997-09-15T00:00:00-0700\nRegistrar Registration Expiration Date: 2020-09-13T21:00:00-0700\nRegistrar: MarkMonitor, Inc.\nRegistrar IANA ID: 292\nRegistrar Abuse Contact Email: abusecomplaints@markmonitor.com\nRegistrar Abuse Contact Phone: +1.2083895740\nDomain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)\nDomain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)\nDomain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)\nDomain Status: serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)\nDomain Status: serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)\nDomain Status: serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)\nRegistry Registrant ID: \nRegistrant Name: Dns Admin\nRegistrant Organization: Google Inc.\nRegistrant Street: Please contact contact-admin@google.com, 1600 Amphitheatre Parkway\nRegistrant City: Mountain View\nRegistrant State/Province: CA\nRegistrant Postal Code: 94043\nRegistrant Country: US\nRegistrant Phone: +1.6502530000\nRegistrant Phone Ext: \nRegistrant Fax: +1.6506188571\nRegistrant Fax Ext: \nRegistrant Email: dns-admin@google.com\nRegistry Admin ID: \nAdmin Name: DNS Admin\nAdmin Organization: Google Inc.\nAdmin Street: 1600 Amphitheatre Parkway\nAdmin City: Mountain View\nAdmin State/Province: CA\nAdmin Postal Code: 94043\nAdmin Country: US\nAdmin Phone: +1.6506234000\nAdmin Phone Ext: \nAdmin Fax: +1.6506188571\nAdmin Fax Ext: \nAdmin Email: dns-admin@google.com\nRegistry Tech ID: \nTech Name: DNS Admin\nTech Organization: Google Inc.\nTech Street: 2400 E. Bayshore Pkwy\nTech City: Mountain View\nTech State/Province: CA\nTech Postal Code: 94043\nTech Country: US\nTech Phone: +1.6503300100\nTech Phone Ext: \nTech Fax: +1.6506181499\nTech Fax Ext: \nTech Email: dns-admin@google.com\nName Server: ns3.google.com\nName Server: ns1.google.com\nName Server: ns4.google.com\nName Server: ns2.google.com\nDNSSEC: unsigned\nURL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/\n"
    },
    "registrant": "Google Inc.",
    "parsed_whois": {
      "statuses": [
        "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
        "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
        "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)",
        "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)",
        "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)",
        "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
      ],
      "name_servers": [
        "ns1.google.com",
        "ns2.google.com",
        "ns3.google.com",
        "ns4.google.com"
      ],
      "created_date": "1997-09-15T00:00:00-07:00",
      "registrar": {
        "abuse_contact_phone": "12083895740",
        "url": "http://www.markmonitor.com",
        "abuse_contact_email": "abusecomplaints@markmonitor.com",
        "name": "MarkMonitor, Inc.",
        "whois_server": "whois.markmonitor.com",
        "iana_id": "292"
      },
      "other_properties": {
        "dnssec": "unsigned",
        "registry_id": "2138514_DOMAIN_COM-VRSN"
      },
      "contacts": {
        "admin": {
          "postal": "94043",
          "country": "US",
          "city": "Mountain View",
          "email": "dns-admin@google.com",
          "street": [
            "1600 Amphitheatre Parkway"
          ],
          "name": "DNS Admin",
          "org": "Google Inc.",
          "phone": "16506234000",
          "state": "CA",
          "fax": "16506188571"
        },
        "billing": {
          "postal": "",
          "country": "",
          "city": "",
          "email": "",
          "street": [],
          "name": "",
          "org": "",
          "phone": "",
          "state": "",
          "fax": ""
        },
        "registrant": {
          "postal": "94043",
          "country": "US",
          "city": "Mountain View",
          "email": "dns-admin@google.com",
          "street": [
            "Please contact contact-admin@google.com, 1600 Amphitheatre Parkway"
          ],
          "name": "Dns Admin",
          "org": "Google Inc.",
          "phone": "16502530000",
          "state": "CA",
          "fax": "16506188571"
        },
        "tech": {
          "postal": "94043",
          "country": "US",
          "city": "Mountain View",
          "email": "dns-admin@google.com",
          "street": [
            "2400 E. Bayshore Pkwy"
          ],
          "name": "DNS Admin",
          "org": "Google Inc.",
          "phone": "16503300100",
          "state": "CA",
          "fax": "16506181499"
        }
      },
      "updated_date": "2015-06-12T10:38:52-07:00",
      "domain": "google.com",
      "expired_date": "2020-09-13T21:00:00-07:00"
    }
  }
}

```

#### Registrant Monitor

This action is used to search the ownership (WHOIS) records of domain names for specific search terms.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|One or more terms separated by the pipe character|None|
|days_back|integer|0|False|Use this parameter when you need to search domains registered up to six days prior to the current date| [1, 2, 3, 4, 5, 6]|
|exclude|string|None|False|Domain names with these words will be excluded from the result set. Separate multiple terms with the pipe character|None|
|limit|integer|None|False|Limit the number of matched domain names that are returned in your result set|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|registrant_monitor__response|False|None|

Example output:

```

{
  "response": {
    "alerts": [],
    "total": 7,
    "limit": 0,
    "query": "google.com",
    "date": "2017-05-17"
  }
}

```

#### Reverse IP

This action is used to provide a list of domain names that share the same Internet host (i.e. the same IP address)

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name you wish to query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|reverse_ip_response|False|None|

Example output:

```

{
  "response": {
    "ip_addresses": [
      {
        "domain_count": 330,
        "domain_names": [],
        "ip_address": "172.217.3.206"
      },
      {
        "domain_count": 34,
        "domain_names": [],
        "ip_address": "64.233.160.99"
      }
    ]
  }
}

```

#### Reverse IP WHOIS

This action is used to provide a list of IP ranges that are owned by an Organization.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip|string|None|True|Required for single IP result|None|
|query|string|None|False|A space separated list of free text query terms|None|
|country|string|None|False|Limits results to IP addresses allocated to an entity with a particular country|None|
|server|string|None|False|Limits results to ranges from a particular WHOIS server|None|
|include_total_count|boolean|False|False|Returns the total number of results for a query|None|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|reverse_ip_whois_response|False|None|

Example output:

```

{
  "response": {
    "record_ip": "65.52.0.98",
    "ip_to_alloc": "65.55.255.255",
    "country": "US",
    "organization": "Microsoft Corporation",
    "whois_record": "NetRange:       65.52.0.0 - 65.55.255.255\nCIDR:           65.52.0.0/14\nNetName:        MICROSOFT-1BLK\nNetHandle:      NET-65-52-0-0-1\nParent:         NET65 (NET-65-0-0-0-0)\nNetType:        Direct Assignment\nOriginAS:       \nOrganization:   Microsoft Corporation (MSFT)\nRegDate:        2001-02-14\nUpdated:        2013-08-20\nRef:            https://whois.arin.net/rest/net/NET-65-52-0-0-1\n\nOrgName:        Microsoft Corporation\nOrgId:          MSFT\nAddress:        One Microsoft Way\nCity:           Redmond\nStateProv:      WA\nPostalCode:     98052\nCountry:        US\nRegDate:        1998-07-09\nUpdated:        2017-01-28\nComment:        To report suspected security issues specific to traffic emanating from Microsoft online services, including the distribution of malicious content or other illicit or illegal material through a Microsoft online service, please submit reports to:\nComment:        * https://cert.microsoft.com.  \nComment:        \nComment:        For SPAM and other abuse issues, such as Microsoft Accounts, please contact:\nComment:        * abuse@microsoft.com.  \nComment:        \nComment:        To report security vulnerabilities in Microsoft products and services, please contact:\nComment:        * secure@microsoft.com.  \nComment:        \nComment:        For legal and law enforcement-related requests, please contact:\nComment:        * msndcc@microsoft.com\nComment:        \nComment:        For routing, peering or DNS issues, please \nComment:        contact:\nComment:        * IOC@microsoft.com\nRef:            https://whois.arin.net/rest/org/MSFT\n\nOrgTechHandle: MRPD-ARIN\nOrgTechName:   Microsoft Routing, Peering, and DNS\nOrgTechPhone:  +1-425-882-8080 \nOrgTechEmail:  IOC@microsoft.com\nOrgTechRef:    https://whois.arin.net/rest/poc/MRPD-ARIN\n\nOrgAbuseHandle: MAC74-ARIN\nOrgAbuseName:   Microsoft Abuse Contact\nOrgAbusePhone:  +1-425-882-8080 \nOrgAbuseEmail:  abuse@microsoft.com\nOrgAbuseRef:    https://whois.arin.net/rest/poc/MAC74-ARIN\n",
    "record_date": "2017-05-17",
    "ip_to": "65.55.255.255",
    "ip_from_alloc": "65.52.0.0",
    "ip_from": "65.52.0.0",
    "range": "65.52.0.0/14",
    "server": "whois.arin.net"
  }
}

```

#### Reverse WHOIS

This action is used to provide a list of domain names that share the same Registrant Information

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|terms|string|None|True|List of one or more terms to search for in the WHOIS record, separated with the pipe character|None|
|exclude|string|None|False|Domain names with WHOIS records that match these terms will be excluded from the result set. Separate multiple terms with the pipe character.|None|
|scope|string|None|False|Sets the scope of the report to include only current WHOIS records, or to include both current and historic records|None|
|mode|string|None|False|quote only lists the size and retail price of the query whiles purchase includes the complete list of domain names|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|reverse_whois_response|False|None|

Example output:

```

{
  "response": {
    "domain_count": {
      "historic": 189998,
      "current": 148808
    },
    "report_cost": {
      "historic": 0,
      "current": 0
    },
    "report_price": {
      "historic": 18999,
      "current": 14880
    }
  }
}

```

#### WHOIS

This action is used to provide the ownership record for a domain name or IP address with basic registration details

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Domain name or an IP address to perform a whois lookup|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|whois_response|False|None|

Example output:

```

{
  "response": {
    "name_servers": [
      "NS1.GOOGLE.COM",
      "NS2.GOOGLE.COM",
      "NS3.GOOGLE.COM",
      "NS4.GOOGLE.COM"
    ],
    "whois": {
      "date": "2017-05-17",
      "record": "Domain Name: google.com\nRegistry Domain ID: 2138514_DOMAIN_COM-VRSN\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar URL: http://www.markmonitor.com\nUpdated Date: 2015-06-12T10:38:52-0700\nCreation Date: 1997-09-15T00:00:00-0700\nRegistrar Registration Expiration Date: 2020-09-13T21:00:00-0700\nRegistrar: MarkMonitor, Inc.\nRegistrar IANA ID: 292\nRegistrar Abuse Contact Email: abusecomplaints@markmonitor.com\nRegistrar Abuse Contact Phone: +1.2083895740\nDomain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)\nDomain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)\nDomain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)\nDomain Status: serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)\nDomain Status: serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)\nDomain Status: serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)\nRegistry Registrant ID: \nRegistrant Name: Dns Admin\nRegistrant Organization: Google Inc.\nRegistrant Street: Please contact contact-admin@google.com, 1600 Amphitheatre Parkway\nRegistrant City: Mountain View\nRegistrant State/Province: CA\nRegistrant Postal Code: 94043\nRegistrant Country: US\nRegistrant Phone: +1.6502530000\nRegistrant Phone Ext: \nRegistrant Fax: +1.6506188571\nRegistrant Fax Ext: \nRegistrant Email: dns-admin@google.com\nRegistry Admin ID: \nAdmin Name: DNS Admin\nAdmin Organization: Google Inc.\nAdmin Street: 1600 Amphitheatre Parkway\nAdmin City: Mountain View\nAdmin State/Province: CA\nAdmin Postal Code: 94043\nAdmin Country: US\nAdmin Phone: +1.6506234000\nAdmin Phone Ext: \nAdmin Fax: +1.6506188571\nAdmin Fax Ext: \nAdmin Email: dns-admin@google.com\nRegistry Tech ID: \nTech Name: DNS Admin\nTech Organization: Google Inc.\nTech Street: 2400 E. Bayshore Pkwy\nTech City: Mountain View\nTech State/Province: CA\nTech Postal Code: 94043\nTech Country: US\nTech Phone: +1.6503300100\nTech Phone Ext: \nTech Fax: +1.6506181499\nTech Fax Ext: \nTech Email: dns-admin@google.com\nName Server: ns3.google.com\nName Server: ns1.google.com\nName Server: ns4.google.com\nName Server: ns2.google.com\nDNSSEC: unsigned\nURL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/\n"
    },
    "registration": {
      "updated": "2011-07-20",
      "registrar": "MARKMONITOR INC.",
      "statuses": [
        "clientDeleteProhibited",
        "clientTransferProhibited",
        "clientUpdateProhibited",
        "serverDeleteProhibited",
        "serverTransferProhibited",
        "serverUpdateProhibited"
      ],
      "created": "1997-09-15",
      "expires": "2020-09-14"
    },
    "record_source": "google.com",
    "registrant": "Google Inc."
  }
}

```

#### WHOIS History

This action is used to provide a list of historic WHOIS records for a domain name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name you wish to query|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|whois_history_response|False|None|

Example output:

```

{
  "response": {
    "history": [
      {
        "date": "2003-09-14",
        "whois": {
          "registrant": "Woot, Inc.",
          "registration": {
            "registrar": "REGISTER.COM, INC.",
            "created": "2000-01-12",
            "statuses": [
              "ACTIVE"
            ],
            "expires": "2006-01-12"
          },
          "record": "Register.com for information purposes only, that is, to assist you in\nobtaining information about or related to a domain name registration\nrecord.  Register.com makes this information available \"as is,\" and\ndoes not guarantee its accuracy.  By submitting a WHOIS query, you\nagree that you will use this data only for lawful purposes and that,\nunder no circumstances will you use this data to: (1) allow, enable,\nor otherwise support the transmission of mass unsolicited, commercial\nadvertising or solicitations via direct mail, electronic mail, or by\ntelephone; or (2) enable high volume, automated, electronic processes\nthat apply to Register.com (or its systems).  The compilation,\nrepackaging, dissemination or other use of this data is expressly\nprohibited without the prior written consent of Register.com. \nRegister.com reserves the right to modify these terms at any time.\n\n   Organization:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: mrutledge@synmicro.com\n\n   Registrar Name....: Register.com\n   Registrar Whois...: whois.register.com\n   Registrar Homepage: http://www.register.com\n\n   Domain Name: WOOT.COM\n\n      Created on..............: Wed, Jan 12, 2000\n      Expires on..............: Thu, Jan 12, 2006\n      Record last updated on..: Fri, Aug 15, 2003\n\n   Administrative Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: mrutledge@synmicro.com\n\n   Technical Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: mrutledge@synmicro.com\n\n   Zone Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: mrutledge@synmicro.com\n\n   Domain servers in listed order:\n\n   DNS9.REGISTER.COM                                 216.21.234.75     \n   DNS10.REGISTER.COM                                216.21.226.75\n",
          "name_servers": [
            "DNS9.REGISTER.COM"
          ]
        },
        "is_private": 0
      },
      {
        "date": "2003-10-31",
        "whois": {
          "registrant": "Woot, Inc.",
          "registration": {
            "registrar": "REGISTER.COM, INC.",
            "created": "2000-01-12",
            "statuses": [
              "ACTIVE"
            ],
            "expires": "2006-01-12"
          },
          "record": "Organization:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: mrutledge@synmicro.com\n\n   Registrar Name....: Register.com\n   Registrar Whois...: whois.register.com\n   Registrar Homepage: http://www.register.com\n\n   Domain Name: WOOT.COM\n\n      Created on..............: Wed, Jan 12, 2000\n      Expires on..............: Thu, Jan 12, 2006\n      Record last updated on..: Fri, Aug 15, 2003\n\n   Administrative Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: mrutledge@synmicro.com\n\n   Technical Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: mrutledge@synmicro.com\n\n   Zone Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: mrutledge@synmicro.com\n\n   Domain servers in listed order:\n\n   DNS9.REGISTER.COM                                 216.21.234.75\n   DNS10.REGISTER.COM                                216.21.226.75\n",
          "name_servers": [
            "DNS9.REGISTER.COM"
          ]
        },
        "is_private": 0
      }
    ],
    "record_count": 383
  }
}

```

#### Reverse Name Server

This action is used to provide a list of domain names that share the same primary or secondary name server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name you wish to query|None|
|limit|integer|None|False|Limits the size of the domain list than can appear in a response|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|reverse_name_server_response|False|None|

Example output:

```

{
  "response": {
    "secondary_domains": [],
    "name_server": {
      "primary": 12856,
      "hostname": "google.com",
      "secondary": 452,
      "total": 13308
    },
    "primary_domains": []
  }
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types | Bug fix logging credentials
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [DomainTools](https://www.domaintools.com)
* [DomainTools API](https://www.domaintools.com/resources/api-documentation/)
* [DomainTools Python API](https://github.com/domaintools/python_api)

