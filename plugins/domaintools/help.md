# Description

[DomainTools](https://www.domaintools.com) data and products work in harmony to enable security teams to start getting ahead of attacks, gain context and visibility into potential threats, and lower the skills barrier. The DomainTools plugin for InsightConnect allows for the automation of domain lookups and retrieval of threat information related to the domain.
This plugin utilizes the [DomainTools Python API](https://github.com/domaintools/python_api).

# Key Features

* WHOIS
* Domain Search
* Brand Monitor

# Requirements

* Requires an API Key from DomainTools

# Supported Product Versions

* DomainTools_api 2.0.0

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Enter the API key|None|9de50-69c5a-fe602-b2ea0-a04b6|None|None|
|username|string|None|True|Enter the API username|None|username|None|None|

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

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|None|False|Use this parameter when you need to search domains registered up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|0|None|None|
|domain_status|string|None|False|Sets the scope of domain names to search|["new", "on-hold"]|new|None|None|
|exclude|string|None|False|Domain names with these words will be excluded from the result set. Separate multiple terms with the pipe character|None|auto|None|None|
|query|string|None|True|One or more terms separated by the pipe character|None|domaintools|None|None|
  
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
  "response": "{\"query: \"domaintools\", \"exclude\": [], \"new\": true, \"total\": 0, \"alerts\": [], \"on-hold\": true}"
}
```

#### Domain Profile

This action is used to provides basic domain name registration details and a preview of additional data

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|None|None|
  
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
    "history": {},
    "name_servers": [],
    "registrant": {
      "domains": 258,
      "name": "DOMAINTOOLS, LLC",
      "product_url": "https://reversewhois.domaintools.com/?all[]=DOMAINTOOLS%2C+LLC&none[]="
    },
    "registration": {
      "created": "1998-08-02",
      "expires": "2017-08-01",
      "registrar": "ENOM, INC.",
      "statuses": [
        "clientTransferProhibited"
      ],
      "updated": "2014-10-18"
    },
    "seo": {
      "product_url": "http://research.domaintools.com/seo-browser/?domain=domaintools.com",
      "score": 77
    },
    "server": {
      "ip_address": "199.30.228.112",
      "other_domains": 2,
      "product_url": "https://reverseip.domaintools.com/search/?q=domaintools.com"
    },
    "website_data": {}
  }
}
```

#### Domain Search

This action is used to searches for domain names that match your specific search string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|active_only|boolean|False|False|Return only domains currently registered|None|False|None|None|
|anchor_left|boolean|False|False|Return only domains that start with the query term|None|default|None|None|
|anchor_right|boolean|False|False|Return only domains that end with the query term|None|False|None|None|
|deleted_only|boolean|False|False|Return only domains previously registered but not currently registered|None|default|None|None|
|exclude_query|string|None|False|Terms to exclude from matching, each term in the query string must be at least three characters long|None|test|None|None|
|has_hyphen|boolean|True|False|Return results with hyphens in the domain name|None|True|None|None|
|has_number|boolean|True|False|Return results with numbers in the domain name|None|True|None|None|
|max_length|integer|25|False|Limit the maximum domain character count|None|25|None|None|
|min_length|integer|1|False|Limit the minimum domain character count|None|1|None|None|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|1|None|None|
|query|string|None|True|Query string, each term in the query string must be at least three characters long|None|domaintools|None|None|
  
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
    "query_info": {},
    "results": []
  }
}
```

#### Hosting History

This action is used to provides a list of changes that have occurred in a Domain Name\'s registrar, IP address, and 
name servers

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|None|None|
  
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
    "domain_name": "example.com",
    "ip_history": [],
    "nameserver_history": [],
    "registrar_history": []
  }
}
```

#### IP Monitor

This action is used to searches the daily activity of all our monitored TLDs on any given IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|0|False|Use this parameter when you need to search domain changes up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|0|None|None|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|1|None|None|
|query|string|None|True|The IP Address you wish to query|None|65.55.53.233|None|None|
  
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
    "alerts": [],
    "date": "2013-11-18",
    "ip_address": "65.55.53.233",
    "page": 1,
    "page_count": 0,
    "total": 0
  }
}
```

#### Name Server Monitor

This action is used to searches the daily activity of all our monitored TLDs on any given name server. 

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|int|0|False|Use this parameter search domain changes up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|0|None|None|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|1|None|None|
|query|string|None|True|The hostname of the Name Server you wish to query|None|DNSPOD.NET|None|None|
  
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
    "alerts": [],
    "date": "2013-11-20",
    "limit": 1000,
    "name_server": "DNSPOD.NET",
    "page": 1,
    "page_count": 0,
    "total": 0
  }
}
```

#### Parsed WHOIS

This action is used to provides parsed information extracted from the raw WHOIS record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|None|None|
  
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
      "NS1.P09.DYNECT.NET",
      "NS2.P09.DYNECT.NET",
      "NS3.P09.DYNECT.NET",
      "NS4.P09.DYNECT.NET"
    ],
    "parsed_whois": {},
    "registrant": "DomainTools, LLC",
    "registration": {
      "created": "1998-08-02",
      "expires": "2014-08-01",
      "registrar": "NAME TRANCE LLC",
      "statuses": [
        "clientTransferProhibited"
      ],
      "updated": "2014-06-27"
    },
    "whois": {}
  }
}
```

#### Registrant Monitor

This action is used to searches the ownership (WHOIS) records of domain names for specific search terms

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|None|False|Use this parameter in exceptional circumstances where you need to search domains registered up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|0|None|None|
|exclude|string|None|False|WHOIS records with these words will be excluded from the result set. Separate multiple terms with the pipe character|None|Private|Proxy|None|None|
|limit|integer|None|False|Limit the number of matched domain names that are returned in your result set|None|100|None|None|
|query|string|None|True|One or more terms separated by the pipe character|None|John Doe|Example Company|None|None|
  
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
    "date": "2011-03-02",
    "limit": 500,
    "query": "DomainTools",
    "total": 2
  }
}
```

#### Reputation

This action is used to retrieves reputation score of specified domain name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Input domain for which the risk score is desired|None|example.com|None|None|
|include_reasons|boolean|False|False|Return a list of reasons for the risk score determination|None|False|None|None|
  
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
    "domain": "domaintools.com",
    "reasons": [
      "registrant"
    ],
    "risk_score": 21.13
  }
}
```

#### Reverse IP

This action is used to provides a list of domain names that share the same Internet host (i.e. the same IP address)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|None|None|
|limit|integer|None|False|Limits the size of the domain list than can appear in a response|None|100|None|None|
  
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
    "ip_addresses": []
  }
}
```

#### Reverse IP WHOIS

This action is used to provides a list of IP network ranges with WHOIS records that match a specific query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|country|string|None|False|Limits results to IP addresses allocated to an entity with a particular country|None|US|None|None|
|include_total_count|boolean|False|False|Returns the total number of results for a query|None|False|None|None|
|ip|string|None|False|Required for single IP result|None|0.0.0.0|None|None|
|page|string|None|False|Providing the page number allows access to additional pages of data|None|2|None|None|
|server|string|None|False|Limits results to ranges from a particular WHOIS server|None|whois.arin.net|None|None|
  
Example input:

```
{
  "country": "US",
  "include_total_count": false,
  "ip": "0.0.0.0",
  "page": 2,
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
    "has_more_pages": true,
    "page": 1,
    "record_count": 1000,
    "records": [],
    "total_count": 1105
  }
}
```

#### Reverse Name Server

This action is used to provides a list of domain names that share the same primary or secondary name server

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|None|None|
|limit|integer|None|False|Limits the size of the domain list than can appear in a response|None|100|None|None|
  
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
    "name_server": {
      "hostname": "domaintools.net",
      "primary": 159,
      "secondary": 0,
      "total": 159
    },
    "primary_domains": [],
    "secondary_domains": []
  }
}
```

#### Reverse WHOIS

This action is used to provides a list of domain names that share the same Registrant Information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|exclude|string|None|False|Domain names with WHOIS records that match these terms will be excluded from the result set. Separate multiple terms with the pipe character|None|Private|Proxy|None|None|
|mode|string|None|False|Quote only lists the size and retail price of the query whiles purchase includes the complete list of domain names|None|purchase|None|None|
|scope|string|None|False|Sets the scope of the report to include only current WHOIS records, or to include both current and historic records|["current", "historic"]|current|None|None|
|terms|string|None|True|List of one or more terms to search for in the WHOIS record, separated with the pipe character|None|John Doe|Example Company|None|None|
  
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
      "current": 310,
      "historic": 412
    },
    "domains": [],
    "report_price": {
      "current": 299,
      "historic": 299
    }
  }
}
```

#### WHOIS

This action is used to provides the ownership record for a domain name or IP address with basic registration details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Domain name or an IP address to perform a WHOIS lookup|None|example.com|None|None|
  
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
      "NS1.P09.DYNECT.NET",
      "NS2.P09.DYNECT.NET",
      "NS3.P09.DYNECT.NET",
      "NS4.P09.DYNECT.NET"
    ],
    "record_source": "domaintools.com",
    "registrant": "DomainTools, LLC",
    "registration": {
      "created": "1998-08-02",
      "expires": "2027-08-01",
      "registrar": "eNon, LLC",
      "statuses": [
        "clientTransferProhibited"
      ],
      "updated": "2020-01-09"
    },
    "whois": {}
  }
}
```

#### WHOIS History

This action is used to provides a list of historic WHOIS records for a domain name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|example.com|None|None|
  
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
    "history": [],
    "record_count": 744
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
|meta|[]string|None|False|None|None|
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
|reasons|[]string|None|False|None|None|
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
|server|string|None|False|None|None|
  
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

There is no troubleshooting for this Plugin

# Version History

* 2.0.2 - Updated SDK and packages to the latest version
* 2.0.1 - 'SDK' Bump | adding 'anyio' into requirements and bumping 'DomainTools' to '2.0.0'
* 2.0.0 - Update `DomainTools` to `1.0.1` | Update to latest SDK version | Fix import issues on all actions | Change `Days Back` input of `Name Server Monitor` to type `int` | Remove `Query` input from `Reverse IP WHOIS` | Add `Server` to `WHOIS History` output `Response` | Add `Reasons` to `Reputation` output `Response` | Change `Meta` to type `List` for `Domain Profile` output `Response`
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