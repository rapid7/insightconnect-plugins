# Description

[DomainTools](https://www.domaintools.com) data and products work in harmony to enable security teams to start getting ahead of attacks, gain context and visibility into potential threats, and lower the skills barrier. The DomainTools plugin for InsightConnect allows for the automation of domain lookups and retrieval of threat information related to the domain.

This plugin utilizes the [DomainTools Python API](https://github.com/domaintools/python_api).

# Key Features

* WHOIS
* Domain search
* Brand monitor

# Requirements

* Requires an API Key from DomainTools

# Supported Product Versions
  
* DomainTools_api 1.0.1

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Enter the API key|None|9de50-69c5a-fe602-b2ea0-a04b6|
|username|string|None|True|Enter the API username|None|username|
  
Example input:

```
{
  "api_key": "9de50-69c5a-fe602-b2ea0-a04b6",
  "username": "username"
}
```

## Technical Details

### Actions


#### Brand Monitor
  
This action is used to searches across all new domain registrations worldwide

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|None|False|Use this parameter when you need to search domains registered up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|0|
|domain_status|string|None|False|Sets the scope of domain names to search|["new", "on-hold"]|new|
|exclude|string|None|False|Domain names with these words will be excluded from the result set. Separate multiple terms with the pipe character|None|auto|
|query|string|None|True|One or more terms separated by the pipe character|None|domaintools|
  
Example input:

```
{
  "days_back": 0,
  "domain_status": "new",
  "exclude": "auto",
  "query": "domaintools"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|brand_monitor_response|False|Response|{"query: "domaintools", "exclude": [], "new": true, "total": 0, "alerts": [], "on-hold": true}|
  
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

#### Domain Profile
  
This action is used to provides basic domain name registration details and a preview of additional data

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|domain_profile_response|False|Response|{"registrant": {"name": "DOMAINTOOLS, LLC", "domains": 258, "product_url": "https://reversewhois.domaintools.com/?all[]=DOMAINTOOLS%2C+LLC&none[]="}, "server": {"ip_address": "199.30.228.112", "other_domains": 2, "product_url": "https://reverseip.domaintools.com/search/?q=domaintools.com"}, "registration": {"created": "1998-08-02", "expires": "2017-08-01", "updated": "2014-10-18", "registrar": "ENOM, INC.", "statuses": ["clientTransferProhibited"]}, "name_servers": [], "history": {}, "seo": {"score": 77, "product_url": "http://research.domaintools.com/seo-browser/?domain=domaintools.com"}, "website_data": {}}|
  
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

#### Domain Search
  
This action is used to searches for domain names that match your specific search string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|active_only|boolean|False|False|Return only domains currently registered|None|False|
|anchor_left|boolean|False|False|Return only domains that start with the query term|None|default|
|anchor_right|boolean|False|False|Return only domains that end with the query term|None|False|
|deleted_only|boolean|False|False|Return only domains previously registered but not currently registered|None|default|
|exclude_query|string|None|False|Terms to exclude from matching, each term in the query string must be at least three characters long|None|test|
|has_hyphen|boolean|True|False|Return results with hyphens in the domain name|None|True|
|has_number|boolean|True|False|Return results with numbers in the domain name|None|True|
|max_length|integer|25|False|Limit the maximum domain character count|None|25|
|min_length|integer|1|False|Limit the minimum domain character count|None|1|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|1|
|query|string|None|True|Query string, each term in the query string must be at least three characters long|None|domaintools|
  
Example input:

```
{
  "active_only": false,
  "anchor_left": false,
  "anchor_right": false,
  "deleted_only": false,
  "exclude_query": "test",
  "has_hyphen": true,
  "has_number": true,
  "max_length": 25,
  "min_length": 1,
  "page": 1,
  "query": "domaintools"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|domain_search_response|False|Response|{"query_info": {}, "results": []}|
  
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

#### Hosting History
  
This action is used to provides a list of changes that have occurred in a Domain Name\'s registrar, IP address, and name
 servers

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|hosting_history_response|False|Response|{"domain_name": "example.com", "ip_history": [], "nameserver_history": [], "registrar_history": []}|
  
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

#### IP Monitor
  
This action is used to searches the daily activity of all our monitored TLDs on any given IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|0|False|Use this parameter when you need to search domain changes up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|0|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|1|
|query|string|None|True|The IP Address you wish to query|None|65.55.53.233|
  
Example input:

```
{
  "days_back": 0,
  "page": 1,
  "query": "65.55.53.233"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|ip_monitor_response|False|Response|{"alerts": [], "date": "2013-11-18", "ip_address": "65.55.53.233", "page": 1, "page_count": 0, "total": 0}|
  
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
  
This action is used to searches the daily activity of all our monitored TLDs on any given name server. 

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|string|0|False|Use this parameter search domain changes up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|0|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|1|
|query|string|None|True|The hostname of the Name Server you wish to query|None|DNSPOD.NET|
  
Example input:

```
{
  "days_back": 0,
  "page": 1,
  "query": "DNSPOD.NET"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|name_server_monitor_response|False|Response|{"alerts": [], "date": "2013-11-20", "limit": 1000, "name_server": "DNSPOD.NET", "page": 1, "page_count": 0, "total": 0}|
  
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

#### Parsed WHOIS
  
This action is used to provides parsed information extracted from the raw WHOIS record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|parsed_whois_response|False|Response|{"registrant": "DomainTools, LLC", "registration": {"created": "1998-08-02", "expires": "2014-08-01", "updated": "2014-06-27", "registrar": "NAME TRANCE LLC", "statuses": ["clientTransferProhibited"]}, "name_servers": ["NS1.P09.DYNECT.NET", "NS2.P09.DYNECT.NET", "NS3.P09.DYNECT.NET", "NS4.P09.DYNECT.NET"], "parsed_whois": {}, "whois": {}}|
  
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
      "record": "Domain Name: google.com\nRegistry Domain ID: 2138514_DOMAIN_COM-VRSN\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar URL: http://www.markmonitor.com\nUpdated Date: 2015-06-12T10:38:52-0700\nCreation Date: 1997-09-15T00:00:00-0700\nRegistrar Registration Expiration Date: 2020-09-13T21:00:00-0700\nRegistrar: MarkMonitor, Inc.\nRegistrar IANA ID: 292\nRegistrar Abuse Contact Email: user@example.com\nRegistrar Abuse Contact Phone: +1.2083895740\nDomain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)\nDomain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)\nDomain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)\nDomain Status: serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)\nDomain Status: serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)\nDomain Status: serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)\nRegistry Registrant ID: \nRegistrant Name: Dns Admin\nRegistrant Organization: Google Inc.\nRegistrant Street: Please contact user@example.com, 1600 Amphitheatre Parkway\nRegistrant City: Mountain View\nRegistrant State/Province: CA\nRegistrant Postal Code: 94043\nRegistrant Country: US\nRegistrant Phone: +1.6502530000\nRegistrant Phone Ext: \nRegistrant Fax: +1.6506188571\nRegistrant Fax Ext: \nRegistrant Email: user@example.com\nRegistry Admin ID: \nAdmin Name: DNS Admin\nAdmin Organization: Google Inc.\nAdmin Street: 1600 Amphitheatre Parkway\nAdmin City: Mountain View\nAdmin State/Province: CA\nAdmin Postal Code: 94043\nAdmin Country: US\nAdmin Phone: +1.6506234000\nAdmin Phone Ext: \nAdmin Fax: +1.6506188571\nAdmin Fax Ext: \nAdmin Email: user@example.com\nRegistry Tech ID: \nTech Name: DNS Admin\nTech Organization: Google Inc.\nTech Street: 2400 E. Bayshore Pkwy\nTech City: Mountain View\nTech State/Province: CA\nTech Postal Code: 94043\nTech Country: US\nTech Phone: +1.6503300100\nTech Phone Ext: \nTech Fax: +1.6506181499\nTech Fax Ext: \nTech Email: user@example.com\nName Server: ns3.google.com\nName Server: ns1.google.com\nName Server: ns4.google.com\nName Server: ns2.google.com\nDNSSEC: unsigned\nURL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/\n"
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
        "abuse_contact_email": "user@example.com",
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
          "email": "user@example.com",
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
          "email": "user@example.com",
          "street": [
            "Please contact user@example.com, 1600 Amphitheatre Parkway"
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
          "email": "user@example.com",
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
  
This action is used to searches the ownership (WHOIS) records of domain names for specific search terms

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|None|False|Use this parameter in exceptional circumstances where you need to search domains registered up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|0|
|exclude|string|None|False|WHOIS records with these words will be excluded from the result set. Separate multiple terms with the pipe character|None|Private|Proxy|
|limit|integer|None|False|Limit the number of matched domain names that are returned in your result set|None|100|
|query|string|None|True|One or more terms separated by the pipe character|None|John Doe|Example Company|
  
Example input:

```
{
  "days_back": 0,
  "exclude": "Private|Proxy",
  "limit": 100,
  "query": "John Doe|Example Company"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|registrant_monitor_response|False|Response|{"query": "DomainTools", "limit": 500, "total": 2, "date": "2011-03-02", "alerts": []}|
  
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

#### Reputation
  
This action is used to retrieves reputation score of specified domain name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Input domain for which the risk score is desired|None|example.com|
|include_reasons|boolean|False|False|Return a list of reasons for the risk score determination|None|False|
  
Example input:

```
{
  "domain": "example.com",
  "include_reasons": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reputation_response|False|Response|{"domain": "domaintools.com", "risk_score": 21.13, "reasons": ["registrant"]}|
  
Example output:

```
{
  "response": {
    "domain": "google.com",
    "risk_score": 0
  }
}
```

#### Reverse IP
  
This action is used to provides a list of domain names that share the same Internet host (i.e. the same IP address)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|
|limit|integer|None|False|Limits the size of the domain list than can appear in a response|None|100|
  
Example input:

```
{
  "domain": "example.com",
  "limit": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reverse_ip_response|False|Response|{"ip_addresses": []}|
  
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
  
This action is used to provides a list of IP network ranges with WHOIS records that match a specific query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|country|string|None|False|Limits results to IP addresses allocated to an entity with a particular country|None|US|
|include_total_count|boolean|False|False|Returns the total number of results for a query|None|False|
|ip|string|None|False|Required for single IP result|None|0.0.0.0|
|page|string|None|False|Providing the page number allows access to additional pages of data|None|2|
|query|string|None|False|A space separated list of free text query terms|None|technology|internet|
|server|string|None|False|Limits results to ranges from a particular WHOIS server|None|whois.arin.net|
  
Example input:

```
{
  "country": "US",
  "include_total_count": false,
  "ip": "0.0.0.0",
  "page": 2,
  "query": "technology|internet",
  "server": "whois.arin.net"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reverse_ip_whois_response|False|Response|{"has_more_pages": true, "page": 1, "total_count": 1105, "record_count": 1000, "records": []}|
  
Example output:

```
{
  "response": {
    "record_ip": "65.52.0.98",
    "ip_to_alloc": "65.55.255.255",
    "country": "US",
    "organization": "Microsoft Corporation",
    "whois_record": "NetRange:       65.52.0.0 - 65.55.255.255\nCIDR:           65.52.0.0/14\nNetName:        MICROSOFT-1BLK\nNetHandle:      NET-65-52-0-0-1\nParent:         NET65 (NET-65-0-0-0-0)\nNetType:        Direct Assignment\nOriginAS:       \nOrganization:   Microsoft Corporation (MSFT)\nRegDate:        2001-02-14\nUpdated:        2013-08-20\nRef:            https://whois.arin.net/rest/net/NET-65-52-0-0-1\n\nOrgName:        Microsoft Corporation\nOrgId:          MSFT\nAddress:        One Microsoft Way\nCity:           Redmond\nStateProv:      WA\nPostalCode:     98052\nCountry:        US\nRegDate:        1998-07-09\nUpdated:        2017-01-28\nComment:        To report suspected security issues specific to traffic emanating from Microsoft online services, including the distribution of malicious content or other illicit or illegal material through a Microsoft online service, please submit reports to:\nComment:        * https://cert.microsoft.com.  \nComment:        \nComment:        For SPAM and other abuse issues, such as Microsoft Accounts, please contact:\nComment:        * user@example.com \nComment:        \nComment:        To report security vulnerabilities in Microsoft products and services, please contact:\nComment:        * user@example.com  \nComment:        \nComment:        For legal and law enforcement-related requests, please contact:\nComment:        * user@example.com \nComment:        \nComment:        For routing, peering or DNS issues, please \nComment:        contact:\nComment:        * user@example.com \nRef:            https://whois.arin.net/rest/org/MSFT\n\nOrgTechHandle: MRPD-ARIN\nOrgTechName:   Microsoft Routing, Peering, and DNS\nOrgTechPhone:  +1-425-882-8080 \nOrgTechEmail:  user@example.com \nOrgTechRef:    https://whois.arin.net/rest/poc/MRPD-ARIN\n\nOrgAbuseHandle: MAC74-ARIN\nOrgAbuseName:   Microsoft Abuse Contact\nOrgAbusePhone:  +1-425-882-8080 \nOrgAbuseEmail:  user@example.com \nOrgAbuseRef:    https://whois.arin.net/rest/poc/MAC74-ARIN\n",
    "record_date": "2017-05-17",
    "ip_to": "65.55.255.255",
    "ip_from_alloc": "65.52.0.0",
    "ip_from": "65.52.0.0",
    "range": "65.52.0.0/14",
    "server": "whois.arin.net"
  }
}
```

#### Reverse Name Server
  
This action is used to provides a list of domain names that share the same primary or secondary name server

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|
|limit|integer|None|False|Limits the size of the domain list than can appear in a response|None|100|
  
Example input:

```
{
  "domain": "example.com",
  "limit": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reverse_name_server_response|False|Response|{"name_server": {"hostname": "domaintools.net", "primary": 159, "secondary": 0, "total": 159}, "primary_domains": [], "secondary_domains": []}|
  
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

#### Reverse WHOIS
  
This action is used to provides a list of domain names that share the same Registrant Information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|exclude|string|None|False|Domain names with WHOIS records that match these terms will be excluded from the result set. Separate multiple terms with the pipe character|None|Private|Proxy|
|mode|string|None|False|Quote only lists the size and retail price of the query whiles purchase includes the complete list of domain names|None|purchase|
|scope|string|None|False|Sets the scope of the report to include only current WHOIS records, or to include both current and historic records|["current", "historic"]|current|
|terms|string|None|True|List of one or more terms to search for in the WHOIS record, separated with the pipe character|None|John Doe|Example Company|
  
Example input:

```
{
  "exclude": "Private|Proxy",
  "mode": "purchase",
  "scope": "current",
  "terms": "John Doe|Example Company"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reverse_whois_response|False|Response|{"domain_count": {"current": 310, "historic": 412}, "domains": [], "report_price": {"current": 299, "historic": 299}}|
  
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
  
This action is used to provides the ownership record for a domain name or IP address with basic registration details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Domain name or an IP address to perform a WHOIS lookup|None|example.com|
  
Example input:

```
{
  "query": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|whois_response|False|Response|{"registrant": "DomainTools, LLC", "registration": {"created": "1998-08-02", "expires": "2027-08-01", "updated": "2020-01-09", "registrar": "eNon, LLC", "statuses": ["clientTransferProhibited"]}, "name_servers": ["NS1.P09.DYNECT.NET", "NS2.P09.DYNECT.NET", "NS3.P09.DYNECT.NET", "NS4.P09.DYNECT.NET"], "whois": {}, "record_source": "domaintools.com"}|
  
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
      "record": "Domain Name: google.com\nRegistry Domain ID: 2138514_DOMAIN_COM-VRSN\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar URL: http://www.markmonitor.com\nUpdated Date: 2015-06-12T10:38:52-0700\nCreation Date: 1997-09-15T00:00:00-0700\nRegistrar Registration Expiration Date: 2020-09-13T21:00:00-0700\nRegistrar: MarkMonitor, Inc.\nRegistrar IANA ID: 292\nRegistrar Abuse Contact Email: user@example.com\nRegistrar Abuse Contact Phone: +1.2083895740\nDomain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)\nDomain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)\nDomain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)\nDomain Status: serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)\nDomain Status: serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)\nDomain Status: serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)\nRegistry Registrant ID: \nRegistrant Name: Dns Admin\nRegistrant Organization: Google Inc.\nRegistrant Street: Please contact user@example.com, 1600 Amphitheatre Parkway\nRegistrant City: Mountain View\nRegistrant State/Province: CA\nRegistrant Postal Code: 94043\nRegistrant Country: US\nRegistrant Phone: +1.6502530000\nRegistrant Phone Ext: \nRegistrant Fax: +1.6506188571\nRegistrant Fax Ext: \nRegistrant Email: user@example.com\nRegistry Admin ID: \nAdmin Name: DNS Admin\nAdmin Organization: Google Inc.\nAdmin Street: 1600 Amphitheatre Parkway\nAdmin City: Mountain View\nAdmin State/Province: CA\nAdmin Postal Code: 94043\nAdmin Country: US\nAdmin Phone: +1.6506234000\nAdmin Phone Ext: \nAdmin Fax: +1.6506188571\nAdmin Fax Ext: \nAdmin Email: user@example.com\nRegistry Tech ID: \nTech Name: DNS Admin\nTech Organization: Google Inc.\nTech Street: 2400 E. Bayshore Pkwy\nTech City: Mountain View\nTech State/Province: CA\nTech Postal Code: 94043\nTech Country: US\nTech Phone: +1.6503300100\nTech Phone Ext: \nTech Fax: +1.6506181499\nTech Fax Ext: \nTech Email: user@example.com\nName Server: ns3.google.com\nName Server: ns1.google.com\nName Server: ns4.google.com\nName Server: ns2.google.com\nDNSSEC: unsigned\nURL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/\n"
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
  
This action is used to provides a list of historic WHOIS records for a domain name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|whois_history_response|False|Response|{"record_count": 744, "history": []}|
  
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
          "record": "Register.com for information purposes only, that is, to assist you in\nobtaining information about or related to a domain name registration\nrecord.  Register.com makes this information available \"as is,\" and\ndoes not guarantee its accuracy.  By submitting a WHOIS query, you\nagree that you will use this data only for lawful purposes and that,\nunder no circumstances will you use this data to: (1) allow, enable,\nor otherwise support the transmission of mass unsolicited, commercial\nadvertising or solicitations via direct mail, electronic mail, or by\ntelephone; or (2) enable high volume, automated, electronic processes\nthat apply to Register.com (or its systems).  The compilation,\nrepackaging, dissemination or other use of this data is expressly\nprohibited without the prior written consent of Register.com. \nRegister.com reserves the right to modify these terms at any time.\n\n   Organization:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: user@example.com\n\n   Registrar Name....: Register.com\n   Registrar Whois...: whois.register.com\n   Registrar Homepage: http://www.register.com\n\n   Domain Name: WOOT.COM\n\n      Created on..............: Wed, Jan 12, 2000\n      Expires on..............: Thu, Jan 12, 2006\n      Record last updated on..: Fri, Aug 15, 2003\n\n   Administrative Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: user@example.com\n\n   Technical Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: user@example.com\n\n   Zone Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: user@example.com\n\n   Domain servers in listed order:\n\n   DNS9.REGISTER.COM                                 216.21.234.75     \n   DNS10.REGISTER.COM                                216.21.226.75\n",
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
          "record": "Organization:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: user@example.com\n\n   Registrar Name....: Register.com\n   Registrar Whois...: whois.register.com\n   Registrar Homepage: http://www.register.com\n\n   Domain Name: WOOT.COM\n\n      Created on..............: Wed, Jan 12, 2000\n      Expires on..............: Thu, Jan 12, 2006\n      Record last updated on..: Fri, Aug 15, 2003\n\n   Administrative Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: user@example.com\n\n   Technical Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: user@example.com\n\n   Zone Contact:\n      Woot, Inc.\n      Matt Rutledge\n      2060 Luna Road, Building 100\n      Carrollton, TX 75006\n      US\n      Phone: 214-764-2483\n      Email: user@example.com\n\n   Domain servers in listed order:\n\n   DNS9.REGISTER.COM                                 216.21.234.75\n   DNS10.REGISTER.COM                                216.21.226.75\n",
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
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**registrar**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|abuse_contact_email|string|None|False|None|None|
|abuse_contact_phone|string|None|False|None|None|
|iana_id|string|None|False|None|None|
|name|string|None|False|None|None|
|url|string|None|False|None|None|
|whois_server|string|None|False|None|None|
  
**ip_address**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|events|int|None|False|None|None|
|product_url|string|None|False|None|None|
|timespan_in_years|int|None|False|None|None|
  
**brand_monitor_alerts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|False|None|None|
|status|string|None|False|None|None|
  
**brand_monitor_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|alerts|[]brand_monitor_alerts|None|False|None|None|
|date|string|None|False|None|None|
|exclude|[]object|None|False|None|None|
|limit|int|None|False|None|None|
|new|bool|None|False|None|None|
|on-hold|bool|None|False|None|None|
|query|string|None|False|None|None|
|total|int|None|False|None|None|
|utf8|bool|None|False|None|None|
  
**ip_monitor_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|alerts|[]object|None|False|None|None|
|date|string|None|False|None|None|
|ip_address|string|None|False|None|None|
|limit|int|None|False|None|None|
|page|int|None|False|None|None|
|page_count|int|None|False|None|None|
|total|string|None|False|None|None|
  
**name_server_monitor_alerts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|False|None|None|
|domain|string|None|False|None|None|
|new_name_server|string|None|False|None|None|
|old_name_server|string|None|False|None|None|
  
**name_server_monitor_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|alerts|[]name_server_monitor_alerts|None|False|None|None|
|date|string|None|False|None|None|
|limit|int|None|False|None|None|
|name_server|string|None|False|None|None|
|page|int|None|False|None|None|
|page_count|int|None|False|None|None|
|total|string|None|False|None|None|
  
**query_info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|active_only|bool|None|False|None|None|
|anchor_left|bool|None|False|None|None|
|anchor_right|bool|None|False|None|None|
|deleted_only|bool|None|False|None|None|
|exclude_query|string|None|False|None|None|
|has_hyphen|bool|None|False|None|None|
|has_number|bool|None|False|None|None|
|limit|int|None|False|None|None|
|max_length|int|None|False|None|None|
|min_length|int|None|False|None|None|
|page|int|None|False|None|None|
|total_results|int|None|False|None|None|
  
**domain_search_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|query_info|query_info|None|False|None|None|
|results|[]object|None|False|None|None|
  
**ip_addresses**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|domain_count|int|None|False|None|None|
|domain_names|[]string|None|False|None|None|
|IP Address|string|None|False|None|None|
  
**whois**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|earliest_event|string|None|False|None|None|
|product_url|string|None|False|None|None|
|records|int|None|False|None|None|
  
**domain_profile_history**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP Address|ip_address|None|False|None|None|
|name_server|ip_address|None|False|None|None|
|registrar|registrar|None|False|None|None|
|whois|whois|None|False|None|None|
  
**name_servers**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|product_url|string|None|False|None|None|
|server|string|None|False|None|None|
  
**registrant**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|domains|int|None|False|None|None|
|name|string|None|False|None|None|
|product_url|string|None|False|None|None|
  
**registration**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|created|string|None|False|None|None|
|expires|string|None|False|None|None|
|registrar|string|None|False|None|None|
|statuses|[]string|None|False|None|None|
|updated|string|None|False|None|None|
  
**seo**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|product_url|string|None|False|None|None|
|score|int|None|False|None|None|
  
**server**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP Address|string|None|False|None|None|
|other_domains|int|None|False|None|None|
|product_url|string|None|False|None|None|
  
**meta**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|None|None|
  
**website_data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|meta|meta|None|False|None|None|
|product_url|string|None|False|None|None|
|response_code|int|None|False|None|None|
|server|string|None|False|None|None|
|title|string|None|False|None|None|
  
**domain_profile_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|history|domain_profile_history|None|False|None|None|
|name_servers|[]name_servers|None|False|None|None|
|registrant|registrant|None|False|None|None|
|registration|registration|None|False|None|None|
|seo|seo|None|False|None|None|
|server|server|None|False|None|None|
|website_data|website_data|None|False|None|None|
  
**ip_history**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|False|None|None|
|action_in_words|string|None|False|None|None|
|actiondate|string|None|False|None|None|
|domain|string|None|False|None|None|
|Post IP|string|None|False|None|None|
|Pre IP|string|None|False|None|None|
  
**registrar_history**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|date_created|string|None|False|None|None|
|date_expires|string|None|False|None|None|
|date_lastchecked|string|None|False|None|None|
|date_updated|string|None|False|None|None|
|domain|string|None|False|None|None|
|registrar|string|None|False|None|None|
|registrartag|string|None|False|None|None|
  
**hosting_history_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|domain_name|string|None|False|None|None|
|IP History|[]ip_history|None|False|None|None|
|nameserver_history|[]object|None|False|None|None|
|registrar_history|[]registrar_history|None|False|None|None|
  
**reputation_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|False|None|None|
|risk_score|int|None|False|None|None|
  
**admin**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|city|string|None|False|None|None|
|country|string|None|False|None|None|
|email|string|None|False|None|None|
|fax|string|None|False|None|None|
|name|string|None|False|None|None|
|org|string|None|False|None|None|
|phone|string|None|False|None|None|
|postal|string|None|False|None|None|
|state|string|None|False|None|None|
|street|[]string|None|False|None|None|
  
**contacts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|admin|admin|None|False|None|None|
|billing|admin|None|False|None|None|
|registrant|admin|None|False|None|None|
|tech|admin|None|False|None|None|
  
**other_properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|dnssec|string|None|False|None|None|
|registry_id|string|None|False|None|None|
  
**parsed_whois**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|contacts|contacts|None|False|None|None|
|created_date|string|None|False|None|None|
|domain|string|None|False|None|None|
|expired_date|string|None|False|None|None|
|name_servers|[]string|None|False|None|None|
|other_properties|other_properties|None|False|None|None|
|registrar|registrar|None|False|None|None|
|statuses|[]string|None|False|None|None|
|updated_date|string|None|False|None|None|
  
**parsed_whois_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|name_servers|[]string|None|False|None|None|
|parsed_whois|parsed_whois|None|False|None|None|
|record_source|string|None|False|None|None|
|registrant|string|None|False|None|None|
|registration|registration|None|False|None|None|
|whois|whois|None|False|None|None|
  
**registrant_monitor_alerts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|created|string|None|False|None|None|
|current_owner|string|None|False|None|None|
|domain|string|None|False|None|None|
|last_owner|string|None|False|None|None|
|match_type|string|None|False|None|None|
|modified|string|None|False|None|None|
  
**registrant_monitor_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|alerts|[]registrant_monitor_alerts|None|False|None|None|
|date|string|None|False|None|None|
|limit|int|None|False|None|None|
|query|string|None|False|None|None|
|total|int|None|False|None|None|
  
**reverse_ip_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP Addresses|[]ip_addresses|None|False|None|None|
  
**reverse_ip_whois_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|country|string|None|False|None|None|
|IP From|string|None|False|None|None|
|IP From Alloc|string|None|False|None|None|
|IP To|string|None|False|None|None|
|IP To Alloc|string|None|False|None|None|
|organization|string|None|False|None|None|
|range|string|None|False|None|None|
|record_date|string|None|False|None|None|
|Record IP|string|None|False|None|None|
|server|string|None|False|None|None|
|whois_record|string|None|False|None|None|
  
**domain_count**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|current|int|None|False|None|None|
|historic|int|None|False|None|None|
  
**reverse_whois_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|domain_count|domain_count|None|False|None|None|
|report_cost|domain_count|None|False|None|None|
|report_price|domain_count|None|False|None|None|
  
**whois_whois**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|date|string|None|False|None|None|
|record|string|None|False|None|None|
  
**whois_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|name_servers|[]string|None|False|None|None|
|record_source|string|None|False|None|None|
|registrant|string|None|False|None|None|
|registration|registration|None|False|None|None|
|whois|whois_whois|None|False|None|None|
  
**whois_history_whois**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|name_servers|[]string|None|False|None|None|
|record|string|None|False|None|None|
|registrant|string|None|False|None|None|
|registration|registration|None|False|None|None|
  
**history**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|date|string|None|False|None|None|
|is_private|int|None|False|None|None|
|whois|whois_history_whois|None|False|None|None|
  
**whois_history_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|history|[]history|None|False|None|None|
|record_count|int|None|False|None|None|
  
**name_server**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|hostname|string|None|False|None|None|
|primary|int|None|False|None|None|
|secondary|int|None|False|None|None|
|total|int|None|False|None|None|
  
**reverse_name_server_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|name_server|name_server|None|False|None|None|
|primary_domains|[]string|None|False|None|None|
|secondary_domains|[]object|None|False|None|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 1.0.2 - Update vulnerability and to latest SDK version 
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types | Bug fix logging credentials
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [DomainTools](https://www.domaintools.com)

## References

* [DomainTools](https://www.domaintools.com)
* [DomainTools API](https://www.domaintools.com/resources/api-documentation/)
* [DomainTools Python API](https://github.com/domaintools/python_api)

