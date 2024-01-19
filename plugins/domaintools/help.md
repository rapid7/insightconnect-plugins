# Description

Domain name search tool that allows a wildcard search, monitoring of WHOIS record changes and history caching, as well as Reverse IP queries

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
*This plugin does not contain any supported product versions.*

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Enter the API key|None|None|
|username|string|None|True|Enter the API username|None|None|
  
Example input:

```
{
  "api_key": {
    "secretKey": ""
  },
  "username": ""
}
```

## Technical Details

### Actions


#### Brand Monitor
  
Searches across all new domain registrations worldwide

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|None|False|Use this parameter when you need to search domains registered up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|None|
|domain_status|string|None|False|Sets the scope of domain names to search|['new', 'on-hold']|None|
|exclude|string|None|False|Domain names with these words will be excluded from the result set. Separate multiple terms with the pipe character|None|None|
|query|string|None|True|One or more terms separated by the pipe character|None|None|
  
Example input:

```
{
  "days_back": 0,
  "domain_status": "new",
  "exclude": "",
  "query": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|brand_monitor_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "alerts": [
      {
        "domain": "",
        "status": {}
      }
    ],
    "date": {},
    "exclude": [
      {}
    ],
    "limit": 0,
    "new": "true",
    "on-hold": {},
    "query": {},
    "total": {},
    "utf8": {}
  }
}
```

#### Domain Profile
  
Provides basic domain name registration details and a preview of additional data

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|None|
  
Example input:

```
{
  "domain": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|domain_profile_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "history": {
      "IP Address": {
        "events": 0,
        "product_url": "",
        "timespan_in_years": {}
      },
      "name_server": {},
      "registrar": {
        "abuse_contact_email": {},
        "abuse_contact_phone": {},
        "iana_id": {},
        "name": {},
        "url": {},
        "whois_server": {}
      },
      "whois": {
        "earliest_event": {},
        "product_url": {},
        "records": {}
      }
    },
    "name_servers": [
      {
        "product_url": {},
        "server": {}
      }
    ],
    "registrant": {
      "domains": {},
      "name": {},
      "product_url": {}
    },
    "registration": {
      "created": {},
      "expires": {},
      "registrar": {},
      "statuses": [
        {}
      ],
      "updated": {}
    },
    "seo": {
      "product_url": {},
      "score": {}
    },
    "server": {
      "IP Address": {},
      "other_domains": {},
      "product_url": {}
    },
    "website_data": {
      "meta": {
        "description": {}
      },
      "product_url": {},
      "response_code": {},
      "server": {},
      "title": {}
    }
  }
}
```

#### Domain Search
  
Searches for domain names that match your specific search string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|active_only|boolean|False|False|Return only domains currently registered|None|None|
|anchor_left|boolean|False|False|Return only domains that start with the query term|None|None|
|anchor_right|boolean|False|False|Return only domains that end with the query term|None|None|
|deleted_only|boolean|False|False|Return only domains previously registered but not currently registered|None|None|
|exclude_query|string|None|False|Terms to exclude from matching — each term in the query string must be at least three characters long|None|None|
|has_hyphen|boolean|True|False|Return results with hyphens in the domain name|None|None|
|has_number|boolean|True|False|Return results with numbers in the domain name|None|None|
|max_length|integer|25|False|Limit the maximum domain character count|None|None|
|min_length|integer|1|False|Limit the minimum domain character count|None|None|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|None|
|query|string|None|True|Query string — each term in the query string must be at least three characters long|None|None|
  
Example input:

```
{
  "active_only": false,
  "anchor_left": false,
  "anchor_right": false,
  "deleted_only": false,
  "exclude_query": "",
  "has_hyphen": true,
  "has_number": true,
  "max_length": 25,
  "min_length": 1,
  "page": 1,
  "query": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|domain_search_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "query_info": {
      "active_only": "true",
      "anchor_left": {},
      "anchor_right": {},
      "deleted_only": {},
      "exclude_query": "",
      "has_hyphen": {},
      "has_number": {},
      "limit": 0,
      "max_length": {},
      "min_length": {},
      "page": {},
      "total_results": {}
    },
    "results": [
      {}
    ]
  }
}
```

#### Hosting History
  
Provides a list of changes that have occurred in a Domain Name\'s registrar, IP address, and name servers

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|None|
  
Example input:

```
{
  "domain": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|hosting_history_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "IP History": [
      {
        "Post IP": {},
        "Pre IP": {},
        "action": {},
        "action_in_words": {},
        "actiondate": {},
        "domain": {}
      }
    ],
    "domain_name": "",
    "nameserver_history": [
      {}
    ],
    "registrar_history": [
      {
        "date_created": {},
        "date_expires": {},
        "date_lastchecked": {},
        "date_updated": {},
        "domain": {},
        "registrar": {},
        "registrartag": {}
      }
    ]
  }
}
```

#### IP Monitor
  
Searches the daily activity of all our monitored TLDs on any given IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|0|False|Use this parameter when you need to search domain changes up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|None|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|None|
|query|string|None|True|The IP Address you wish to query (i.e. 65.55.53.233)|None|None|
  
Example input:

```
{
  "days_back": 0,
  "page": 1,
  "query": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|ip_monitor_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "alerts": [
      {}
    ],
    "date": "",
    "ip_address": {},
    "limit": 0,
    "page": {},
    "page_count": {},
    "total": {}
  }
}
```

#### Name Server Monitor
  
Searches the daily activity of all our monitored TLDs on any given name server. 

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|string|0|False|Use this parameter search domain changes up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|None|
|page|integer|1|False|If the result set is larger than 1000 records for a given day, request additional pages with this parameter|None|None|
|query|string|None|True|The hostname of the Name Server you wish to query ( i.e. dynect.net )|None|None|
  
Example input:

```
{
  "days_back": 0,
  "page": 1,
  "query": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|name_server_monitor_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "alerts": [
      {
        "action": "",
        "domain": {},
        "new_name_server": {},
        "old_name_server": {}
      }
    ],
    "date": {},
    "limit": 0,
    "name_server": {},
    "page": {},
    "page_count": {},
    "total": {}
  }
}
```

#### Parsed WHOIS
  
Provides parsed information extracted from the raw WHOIS record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|None|
  
Example input:

```
{
  "domain": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|parsed_whois_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "name_servers": [
      ""
    ],
    "parsed_whois": {
      "contacts": {
        "admin": {
          "city": {},
          "country": {},
          "email": {},
          "fax": {},
          "name": {},
          "org": {},
          "phone": {},
          "postal": {},
          "state": {},
          "street": {}
        },
        "billing": {},
        "registrant": {},
        "tech": {}
      },
      "created_date": {},
      "domain": {},
      "expired_date": {},
      "name_servers": {},
      "other_properties": {
        "dnssec": {},
        "registry_id": {}
      },
      "registrar": {
        "abuse_contact_email": {},
        "abuse_contact_phone": {},
        "iana_id": {},
        "name": {},
        "url": {},
        "whois_server": {}
      },
      "statuses": {},
      "updated_date": {}
    },
    "record_source": {},
    "registrant": {},
    "registration": {
      "created": {},
      "expires": {},
      "registrar": {},
      "statuses": {},
      "updated": {}
    },
    "whois": {
      "earliest_event": {},
      "product_url": {},
      "records": 0
    }
  }
}
```

#### Registrant Monitor
  
Searches the ownership (WHOIS) records of domain names for specific search terms

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|None|False|Use this parameter in exceptional circumstances where you need to search domains registered up to six days prior to the current date|[0, 1, 2, 3, 4, 5, 6]|None|
|exclude|string|None|False|WHOIS records with these words will be excluded from the result set. Separate multiple terms with the pipe character|None|None|
|limit|integer|None|False|Limit the number of matched domain names that are returned in your result set|None|None|
|query|string|None|True|One or more terms separated by the pipe character|None|None|
  
Example input:

```
{
  "days_back": 0,
  "exclude": "",
  "limit": 0,
  "query": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|registrant_monitor_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "alerts": [
      {
        "created": "",
        "current_owner": {},
        "domain": {},
        "last_owner": {},
        "match_type": {},
        "modified": {}
      }
    ],
    "date": {},
    "limit": 0,
    "query": {},
    "total": {}
  }
}
```

#### Reputation
  
Retrieves reputation score of specified domain name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Input domain for which the risk score is desired|None|None|
|include_reasons|boolean|False|False|Return a list of reasons for the risk score determination|None|None|
  
Example input:

```
{
  "domain": "",
  "include_reasons": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reputation_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "domain": "",
    "risk_score": 0
  }
}
```

#### Reverse IP
  
Provides a list of domain names that share the same Internet host (i.e. the same IP address)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|None|
|limit|integer|None|False|Limits the size of the domain list than can appear in a response|None|None|
  
Example input:

```
{
  "domain": "",
  "limit": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reverse_ip_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "IP Addresses": [
      {
        "IP Address": {},
        "domain_count": 0,
        "domain_names": [
          ""
        ]
      }
    ]
  }
}
```

#### Reverse IP WHOIS
  
Provides a list of IP network ranges with WHOIS records that match a specific query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|country|string|None|False|Limits results to IP addresses allocated to an entity with a particular country|None|None|
|include_total_count|boolean|False|False|Returns the total number of results for a query|None|None|
|ip|string|None|False|Required for single IP result|None|None|
|page|string|None|False|Providing the page number allows access to additional pages of data|None|None|
|query|string|None|False|A space separated list of free text query terms|None|None|
|server|string|None|False|Limits results to ranges from a particular WHOIS server|None|None|
  
Example input:

```
{
  "country": "",
  "include_total_count": false,
  "ip": "",
  "page": "",
  "query": "",
  "server": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reverse_ip_whois_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "IP From": {},
    "IP From Alloc": {},
    "IP To": {},
    "IP To Alloc": {},
    "Record IP": {},
    "country": "",
    "organization": {},
    "range": {},
    "record_date": {},
    "server": {},
    "whois_record": {}
  }
}
```

#### Reverse Name Server
  
Provides a list of domain names that share the same primary or secondary name server

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|None|
|limit|integer|None|False|Limits the size of the domain list than can appear in a response|None|None|
  
Example input:

```
{
  "domain": "",
  "limit": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reverse_name_server_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "name_server": {
      "hostname": "",
      "primary": 0,
      "secondary": {},
      "total": {}
    },
    "primary_domains": [
      {}
    ],
    "secondary_domains": [
      {}
    ]
  }
}
```

#### Reverse WHOIS
  
Provides a list of domain names that share the same Registrant Information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|exclude|string|None|False|Domain names with WHOIS records that match these terms will be excluded from the result set. Separate multiple terms with the pipe character|None|None|
|mode|string|None|False|Quote only lists the size and retail price of the query whiles purchase includes the complete list of domain names|None|None|
|scope|string|None|False|Sets the scope of the report to include only current WHOIS records, or to include both current and historic records|['current', 'historic']|None|
|terms|string|None|True|List of one or more terms to search for in the WHOIS record, separated with the pipe character|None|None|
  
Example input:

```
{
  "exclude": "",
  "mode": "",
  "scope": "current",
  "terms": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|reverse_whois_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "domain_count": {
      "current": 0,
      "historic": {}
    },
    "report_cost": {},
    "report_price": {}
  }
}
```

#### WHOIS
  
Provides the ownership record for a domain name or IP address with basic registration details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Domain name or an IP address to perform a whois lookup|None|None|
  
Example input:

```
{
  "query": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|whois_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "name_servers": [
      ""
    ],
    "record_source": {},
    "registrant": {},
    "registration": {
      "created": {},
      "expires": {},
      "registrar": {},
      "statuses": {},
      "updated": {}
    },
    "whois": {
      "date": {},
      "record": {}
    }
  }
}
```

#### WHOIS History
  
Provides a list of historic WHOIS records for a domain name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name you wish to query|None|None|
  
Example input:

```
{
  "domain": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|whois_history_response|False|Response|None|
  
Example output:

```
{
  "response": {
    "history": [
      {
        "date": "",
        "is_private": 0,
        "whois": {
          "name_servers": [
            {}
          ],
          "record": {},
          "registrant": {},
          "registration": {
            "created": {},
            "expires": {},
            "registrar": {},
            "statuses": {},
            "updated": {}
          }
        }
      }
    ],
    "record_count": {}
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
  
*This plugin does not contain a version history.*

# Links


## References
  
*This plugin does not contain any references.*