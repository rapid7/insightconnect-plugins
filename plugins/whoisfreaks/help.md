# Description

Enrich domains, IP addresses and ASNs with WhoisFreaks WHOIS, DNS, SSL, geolocation and reputation intelligence, and ingest the WhoisFreaks newly registered domain and threat feeds

# Key Features

* Live, historical, reverse and bulk WHOIS lookups
* Live, historical, reverse and bulk DNS lookups
* Domain availability, typosquatting, subdomain and SSL certificate lookups
* Domain reputation and IP security (threat, proxy, VPN, TOR and bot) assessment
* IP geolocation, IP WHOIS and ASN WHOIS lookups
* Account credit and subscription usage reporting
* Stateful ingestion of the newly registered domain feeds and the phishing, malware and spam threat feeds

# Requirements

* A WhoisFreaks API key
* Lookup actions require WhoisFreaks API credits. The newly registered domain feeds and the threat feeds each require their own WhoisFreaks subscription
* Outbound HTTPS (TCP 443) access from the orchestrator to api.whoisfreaks.com and files.whoisfreaks.com

# Supported Product Versions

* WhoisFreaks API (lookups v1.0 to v3.0, feeds v3.3 and v3.4) tested on 2026-11-04

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|WhoisFreaks API key. It is sent only in the X-API-KEY request header|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions


#### ASN WHOIS

This action is used to retrieve the registration and routing data of an autonomous system number

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asn|string|None|True|Autonomous system number, with or without the AS prefix|None|AS15169|None|None|
  
Example input:

```
{
  "asn": "AS15169"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|as_name|string|False|Name of the autonomous system|GOOGLE|
|country|string|False|Country of the organization|US|
|found|boolean|True|Whether a record was returned|True|
|message|string|False|Explanation when no record was returned|Record not found|
|organization_name|string|False|Name of the organization that holds the autonomous system|Google LLC|
|response|object|False|Complete ASN record returned by WhoisFreaks|{'asNumber': '15169', 'asName': 'GOOGLE'}|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
  
Example output:

```
{
  "as_name": "GOOGLE",
  "country": "US",
  "found": true,
  "message": "Record not found",
  "organization_name": "Google LLC",
  "response": {
    "asName": "GOOGLE",
    "asNumber": "15169"
  },
  "status_code": 200
}
```

#### Bulk DNS

This action is used to retrieve the live DNS records of up to 100 domains and up to 100 IP addresses in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cname_depth|integer|None|False|Number of CNAME hops to follow (0 to 4)|None|1|None|None|
|domains|[]string|None|False|Domain names to resolve (up to 100). Domains or IP Addresses is required|None|["example.com", "example.org"]|None|None|
|ip_addresses|[]string|None|False|IP addresses to resolve (up to 100). Domains or IP Addresses is required|None|["8.8.8.8", "1.1.1.1"]|None|None|
|record_types|string|all|True|Record types to return, either all or a comma-separated list of A, AAAA, MX, NS, TXT, SOA, SPF, CNAME and PTR|None|A,MX|None|None|
  
Example input:

```
{
  "cname_depth": 1,
  "domains": [
    "example.com",
    "example.org"
  ],
  "ip_addresses": [
    "8.8.8.8",
    "1.1.1.1"
  ],
  "record_types": "all"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]object|True|One live DNS result per domain or IP address|[{"domainName": "example.com", "dnsRecords": []}]|
|skipped|[]object|True|Input values that were not sent to WhoisFreaks, with the reason|[{"value": "10.0.0.1", "reason": "Private, reserved or special-use IP address"}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
  
Example output:

```
{
  "results": [
    {
      "dnsRecords": [],
      "domainName": "example.com"
    }
  ],
  "skipped": [
    {
      "reason": "Private, reserved or special-use IP address",
      "value": "10.0.0.1"
    }
  ],
  "status_code": 200
}
```

#### Bulk Domain Availability

This action is used to check the availability of up to 100 domains, or of one name across up to 100 TLDs

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|False|Domain whose name is checked under every TLD in TLDs|None|example.com|None|None|
|domains|[]string|None|False|Domain names to check (up to 100). Use either Domains, or Domain together with TLDs|None|["example.com", "example.org"]|None|None|
|tlds|[]string|None|False|TLDs to check the name of Domain under (up to 100)|None|["net", "org"]|None|None|
  
Example input:

```
{
  "domain": "example.com",
  "domains": [
    "example.com",
    "example.org"
  ],
  "tlds": [
    "net",
    "org"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]object|True|Availability of each domain|[{"domain": "example.com", "availability": "UNAVAILABLE", "status": True}]|
|skipped|[]object|True|Input values that were not sent to WhoisFreaks, with the reason|[{"value": "not a domain", "reason": "Not a valid domain name"}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks (206 when some domains could not be checked)|200|
  
Example output:

```
{
  "results": [
    {
      "availability": "UNAVAILABLE",
      "domain": "example.com",
      "status": true
    }
  ],
  "skipped": [
    {
      "reason": "Not a valid domain name",
      "value": "not a domain"
    }
  ],
  "status_code": 200
}
```

#### Bulk IP Geolocation

This action is used to retrieve the approximate location of up to 100 IP addresses in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_addresses|[]string|None|True|Public IPv4 or IPv6 addresses to look up (1 to 100). Special-use and invalid values are reported in skipped|None|["8.8.8.8", "1.1.1.1"]|None|None|
  
Example input:

```
{
  "ip_addresses": [
    "8.8.8.8",
    "1.1.1.1"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]object|True|One geolocation record per IP address|[{"ip": "8.8.8.8", "location": {"country_code2": "US"}}]|
|skipped|[]object|True|Input values that were not sent to WhoisFreaks, with the reason|[{"value": "10.0.0.1", "reason": "Private, reserved or special-use IP address"}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
  
Example output:

```
{
  "results": [
    {
      "ip": "8.8.8.8",
      "location": {
        "country_code2": "US"
      }
    }
  ],
  "skipped": [
    {
      "reason": "Private, reserved or special-use IP address",
      "value": "10.0.0.1"
    }
  ],
  "status_code": 200
}
```

#### Bulk IP Security

This action is used to retrieve the security assessment of up to 100 IP addresses in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_addresses|[]string|None|True|Public IPv4 or IPv6 addresses to check (1 to 100). Special-use and invalid values are reported in skipped|None|["8.8.8.8", "1.1.1.1"]|None|None|
  
Example input:

```
{
  "ip_addresses": [
    "8.8.8.8",
    "1.1.1.1"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]object|True|One security assessment per IP address|[{"ip": "8.8.8.8", "security": {"threat_score": 5}}]|
|skipped|[]object|True|Input values that were not sent to WhoisFreaks, with the reason|[{"value": "10.0.0.1", "reason": "Private, reserved or special-use IP address"}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
  
Example output:

```
{
  "results": [
    {
      "ip": "8.8.8.8",
      "security": {
        "threat_score": 5
      }
    }
  ],
  "skipped": [
    {
      "reason": "Private, reserved or special-use IP address",
      "value": "10.0.0.1"
    }
  ],
  "status_code": 200
}
```

#### Bulk WHOIS

This action is used to retrieve the current WHOIS records of up to 100 domains in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domains|[]string|None|True|Domain names to look up (1 to 100). Duplicates are removed and invalid values are reported in skipped|None|["example.com", "example.org"]|None|None|
  
Example input:

```
{
  "domains": [
    "example.com",
    "example.org"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]object|True|One WHOIS record per domain, in request order|[{"domain_name": "example.com", "domain_registered": "yes"}]|
|skipped|[]object|True|Input values that were not sent to WhoisFreaks, with the reason|[{"value": "not a domain", "reason": "Not a valid domain name"}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks (206 when some records are partial)|200|
  
Example output:

```
{
  "results": [
    {
      "domain_name": "example.com",
      "domain_registered": "yes"
    }
  ],
  "skipped": [
    {
      "reason": "Not a valid domain name",
      "value": "not a domain"
    }
  ],
  "status_code": 200
}
```

#### DNS Lookup

This action is used to retrieve the live DNS records of a domain, or the PTR record of an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cname_depth|integer|None|False|Number of CNAME hops to follow (0 to 4)|None|1|None|None|
|domain|string|None|False|Domain name to resolve. Either Domain or IP Address is required|None|example.com|None|None|
|ip_address|string|None|False|IP address to resolve (PTR lookup). Either Domain or IP Address is required|None|8.8.8.8|None|None|
|record_types|string|all|True|Record types to return, either all or a comma-separated list of A, AAAA, MX, NS, TXT, SOA, SPF, CNAME and PTR|None|A,MX|None|None|
|relative_records|boolean|True|True|Also return records of related names, such as the targets of MX and CNAME records|None|True|None|None|
  
Example input:

```
{
  "cname_depth": 1,
  "domain": "example.com",
  "ip_address": "8.8.8.8",
  "record_types": "all",
  "relative_records": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|True|Whether WhoisFreaks returned DNS records|True|
|message|string|False|Explanation when no record was found or the IP address was not looked up|Record not found|
|records|[]object|False|DNS records|[{"name": "example.com", "type": 1, "dnsType": "A", "ttl": 300, "address": "93.184.215.14"}]|
|response|object|False|Complete DNS response returned by WhoisFreaks|{'domainName': 'example.com', 'domainRegistered': True}|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
  
Example output:

```
{
  "found": true,
  "message": "Record not found",
  "records": [
    {
      "address": "93.184.215.14",
      "dnsType": "A",
      "name": "example.com",
      "ttl": 300,
      "type": 1
    }
  ],
  "response": {
    "domainName": "example.com",
    "domainRegistered": true
  },
  "status_code": 200
}
```

#### Domain Availability

This action is used to check whether a domain is available for registration, optionally with available alternatives

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name to check|None|example.com|None|None|
|suggestion_count|integer|5|True|Number of alternatives to return when Suggestions is enabled (1 to 100)|None|5|None|None|
|suggestions|boolean|False|True|Also return available alternative domains. Each suggestion block costs extra WhoisFreaks credits|None|False|None|None|
  
Example input:

```
{
  "domain": "example.com",
  "suggestion_count": 5,
  "suggestions": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|availability|string|False|AVAILABLE, UNAVAILABLE or UNKNOWN|UNAVAILABLE|
|available|boolean|False|True when the domain is available. Not set when the availability is unknown|False|
|found|boolean|True|Whether WhoisFreaks returned an availability result|True|
|message|string|False|Message returned by WhoisFreaks|Domain is not available|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|suggestions|[]object|False|Alternative domains and their availability|[{"domain": "example.net", "availability": "AVAILABLE"}]|
  
Example output:

```
{
  "availability": "UNAVAILABLE",
  "available": false,
  "found": true,
  "message": "Domain is not available",
  "status_code": 200,
  "suggestions": [
    {
      "availability": "AVAILABLE",
      "domain": "example.net"
    }
  ]
}
```

#### Domain Reputation

This action is used to retrieve the risk verdict, trust score and supporting evidence for a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name to assess|None|example.com|None|None|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|confidence|number|False|Confidence of the risk verdict, from 0 to 1|0.92|
|found|boolean|True|Whether an assessment was returned|True|
|is_dga|boolean|False|Whether the domain name looks algorithmically generated|False|
|message|string|False|Explanation when no assessment was returned|Record not found|
|response|object|False|Complete reputation assessment returned by WhoisFreaks|{'risk_category': {'verdict': 'clean'}, 'trust_signals': {'trust_score': 85}}|
|severity|string|False|Severity of the risk verdict|low|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|trust_score|integer|False|Trust score of the domain, higher is more trustworthy|85|
|verdict|string|False|Risk verdict assigned by WhoisFreaks. It is an assessment, not proof of malicious activity|clean|
  
Example output:

```
{
  "confidence": 0.92,
  "found": true,
  "is_dga": false,
  "message": "Record not found",
  "response": {
    "risk_category": {
      "verdict": "clean"
    },
    "trust_signals": {
      "trust_score": 85
    }
  },
  "severity": "low",
  "status_code": 200,
  "trust_score": 85,
  "verdict": "clean"
}
```

#### Get Account Usage

This action is used to retrieve the remaining API credits and the subscription usage of the account

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|True|Complete usage record returned by WhoisFreaks, without the API key|{'apiCredits': {'totalCredits': 10000, 'servedRequest': 250}}|
|subscription_request_limit|integer|False|Requests included in the subscription period|100000|
|subscription_requests_used|integer|False|Requests consumed in the subscription period|5000|
|subscription_status|string|False|Status of the subscription plan|active|
|total_credits|integer|False|Total API credits of the account|10000|
|used_credits|integer|False|API credits consumed|250|
  
Example output:

```
{
  "response": {
    "apiCredits": {
      "servedRequest": 250,
      "totalCredits": 10000
    }
  },
  "subscription_request_limit": 100000,
  "subscription_requests_used": 5000,
  "subscription_status": "active",
  "total_credits": 10000,
  "used_credits": 250
}
```

#### Historical DNS

This action is used to retrieve historical DNS snapshots of a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name to look up|None|example.com|None|None|
|page|integer|1|True|Page number to retrieve, starting at 1. Each page costs WhoisFreaks credits|None|1|None|None|
|record_types|string|all|True|Record types to return, either all or a comma-separated list of A, AAAA, MX, NS, TXT, SOA, SPF and CNAME|None|A,MX|None|None|
  
Example input:

```
{
  "domain": "example.com",
  "page": 1,
  "record_types": "all"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|current_page|integer|False|Page number of these results|1|
|found|boolean|True|Whether any snapshot was found|True|
|message|string|False|Explanation when no snapshot was found|Record not found|
|records|[]object|False|DNS snapshots on this page|[{"domainName": "example.com", "queryTime": "2026-01-01 10:00:00", "dnsRecords": []}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|total_pages|integer|False|Number of result pages|1|
|total_records|integer|False|Number of snapshots across all pages|42|
  
Example output:

```
{
  "current_page": 1,
  "found": true,
  "message": "Record not found",
  "records": [
    {
      "dnsRecords": [],
      "domainName": "example.com",
      "queryTime": "2026-01-01 10:00:00"
    }
  ],
  "status_code": 200,
  "total_pages": 1,
  "total_records": 42
}
```

#### Historical WHOIS

This action is used to retrieve every historical WHOIS record of a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name to look up|None|example.com|None|None|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|True|Whether WhoisFreaks returned any record|True|
|message|string|False|Explanation when no record was found|Record not found|
|records|[]object|False|Historical WHOIS records, newest first|[{"domain_name": "example.com", "query_time": "2026-01-01 10:00:00", "create_date": "1995-08-14"}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|total_records|integer|False|Number of historical records|12|
  
Example output:

```
{
  "found": true,
  "message": "Record not found",
  "records": [
    {
      "create_date": "1995-08-14",
      "domain_name": "example.com",
      "query_time": "2026-01-01 10:00:00"
    }
  ],
  "status_code": 200,
  "total_records": 12
}
```

#### IP Geolocation

This action is used to retrieve the approximate location, network and currency of an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|Public IPv4 or IPv6 address to look up|None|8.8.8.8|None|None|
  
Example input:

```
{
  "ip_address": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|city|string|False|City name|Mountain View|
|country_code|string|False|ISO 3166-1 alpha-2 country code. Geolocation is an estimate, not a verified physical location|US|
|country_name|string|False|Country name|United States|
|found|boolean|True|Whether a location was returned|True|
|message|string|False|Explanation when no location was returned or the IP address was not looked up|Private, reserved or special-use IP address|
|response|object|False|Complete geolocation record returned by WhoisFreaks|{'ip': '8.8.8.8', 'location': {'country_code2': 'US'}}|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
  
Example output:

```
{
  "city": "Mountain View",
  "country_code": "US",
  "country_name": "United States",
  "found": true,
  "message": "Private, reserved or special-use IP address",
  "response": {
    "ip": "8.8.8.8",
    "location": {
      "country_code2": "US"
    }
  },
  "status_code": 200
}
```

#### IP Security

This action is used to retrieve the threat score and the TOR, proxy, VPN, relay, bot, spam and cloud-provider signals 
of an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|Public IPv4 or IPv6 address to check|None|8.8.8.8|None|None|
  
Example input:

```
{
  "ip_address": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|True|Whether an assessment was returned|True|
|is_bot|boolean|False|Whether the address is associated with bot traffic|False|
|is_cloud_provider|boolean|False|Whether the address belongs to a cloud or hosting provider|True|
|is_known_attacker|boolean|False|Whether the address has been reported for attacks|False|
|is_proxy|boolean|False|Whether the address is a known proxy|False|
|is_spam|boolean|False|Whether the address is associated with spam|False|
|is_tor|boolean|False|Whether the address is a TOR node|False|
|is_vpn|boolean|False|Whether the address belongs to a VPN provider|False|
|message|string|False|Explanation when no assessment was returned or the IP address was not looked up|Private, reserved or special-use IP address|
|response|object|False|Complete security assessment returned by WhoisFreaks|{'ip': '8.8.8.8', 'security': {'threat_score': 5, 'is_tor': False}}|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|threat_score|integer|False|WhoisFreaks threat score. A high score indicates risk, not proof of an attack|5|
  
Example output:

```
{
  "found": true,
  "is_bot": false,
  "is_cloud_provider": true,
  "is_known_attacker": false,
  "is_proxy": false,
  "is_spam": false,
  "is_tor": false,
  "is_vpn": false,
  "message": "Private, reserved or special-use IP address",
  "response": {
    "ip": "8.8.8.8",
    "security": {
      "is_tor": false,
      "threat_score": 5
    }
  },
  "status_code": 200,
  "threat_score": 5
}
```

#### IP WHOIS

This action is used to retrieve the regional internet registry registration of an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|True|Public IPv4 or IPv6 address to look up|None|8.8.8.8|None|None|
  
Example input:

```
{
  "ip_address": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|True|Whether a registration record was returned|True|
|message|string|False|Explanation when no record was returned or the IP address was not looked up|Private, reserved or special-use IP address|
|organization_name|string|False|Name of the organization that holds the address block|Google LLC|
|response|object|False|Complete IP WHOIS record returned by WhoisFreaks|{'ip_address': '8.8.8.8', 'whois_server': 'whois.arin.net'}|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
  
Example output:

```
{
  "found": true,
  "message": "Private, reserved or special-use IP address",
  "organization_name": "Google LLC",
  "response": {
    "ip_address": "8.8.8.8",
    "whois_server": "whois.arin.net"
  },
  "status_code": 200
}
```

#### Live WHOIS

This action is used to retrieve the current WHOIS record of a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name to look up|None|example.com|None|None|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|create_date|string|False|Registration date|1995-08-14|
|domain_status|[]string|False|EPP status codes of the domain|["clientDeleteProhibited", "clientTransferProhibited"]|
|expiry_date|string|False|Expiry date|2027-08-13|
|found|boolean|True|Whether WhoisFreaks returned a record|True|
|message|string|False|Explanation when the record is missing, partial or cached|Record not found|
|name_servers|[]string|False|Name servers of the domain|["a.iana-servers.net", "b.iana-servers.net"]|
|registered|boolean|False|Whether the domain is registered|True|
|registrar_name|string|False|Name of the registrar|RESERVED-Internet Assigned Numbers Authority|
|response|object|False|Complete WHOIS record returned by WhoisFreaks|{'domain_name': 'example.com', 'domain_registered': 'yes', 'create_date': '1995-08-14'}|
|status_code|integer|False|HTTP status code returned by WhoisFreaks (200 complete, 206 partial, 210 cached, 404 not found)|200|
|update_date|string|False|Last update date|2026-08-14|
  
Example output:

```
{
  "create_date": "1995-08-14",
  "domain_status": [
    "clientDeleteProhibited",
    "clientTransferProhibited"
  ],
  "expiry_date": "2027-08-13",
  "found": true,
  "message": "Record not found",
  "name_servers": [
    "a.iana-servers.net",
    "b.iana-servers.net"
  ],
  "registered": true,
  "registrar_name": "RESERVED-Internet Assigned Numbers Authority",
  "response": {
    "create_date": "1995-08-14",
    "domain_name": "example.com",
    "domain_registered": "yes"
  },
  "status_code": 200,
  "update_date": "2026-08-14"
}
```

#### Reverse DNS

This action is used to find domains that have a DNS record with the given value, such as an IP address, mail server or 
name server

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|exact|boolean|True|True|Match the value exactly instead of partially|None|True|None|None|
|page|integer|1|True|Page number to retrieve, starting at 1. Each page costs WhoisFreaks credits|None|1|None|None|
|record_type|string|a|True|DNS record type to search|["a", "aaaa", "cname", "mx", "ns", "soa", "txt"]|a|None|None|
|sort|string|None|False|Sort order of the results|["asc", "desc"]|asc|None|None|
|value|string|None|True|Record value to search for, for example an IP address for A records or a host name for MX and NS records|None|8.8.8.8|None|None|
  
Example input:

```
{
  "exact": true,
  "page": 1,
  "record_type": "a",
  "sort": "asc",
  "value": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|current_page|integer|False|Page number of these results|1|
|found|boolean|True|Whether any matching domain was found|True|
|message|string|False|Explanation when no domain was found|Record not found|
|records|[]object|False|Matching domains with their DNS records on this page|[{"domainName": "example.com", "dnsRecords": []}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|total_pages|integer|False|Number of result pages|15|
|total_records|integer|False|Number of matching domains across all pages|1500|
  
Example output:

```
{
  "current_page": 1,
  "found": true,
  "message": "Record not found",
  "records": [
    {
      "dnsRecords": [],
      "domainName": "example.com"
    }
  ],
  "status_code": 200,
  "total_pages": 15,
  "total_records": 1500
}
```

#### Reverse WHOIS

This action is used to find domains whose WHOIS records contain a keyword, email address, owner name or company name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|company|string|None|False|Registrant company name|None|Example Inc|None|None|
|email|string|None|False|Registrant email address|None|user@example.com|None|None|
|exact|boolean|False|True|Match the search value exactly instead of partially|None|False|None|None|
|keyword|string|None|False|Keyword that appears in the domain name|None|example|None|None|
|mode|string|default|True|Level of detail of each record. Mini returns up to 100 records per page, default returns up to 50|["default", "mini"]|default|None|None|
|owner|string|None|False|Registrant name|None|John Doe|None|None|
|page|integer|1|True|Page number to retrieve, starting at 1. Each page costs WhoisFreaks credits|None|1|None|None|
  
Example input:

```
{
  "company": "Example Inc",
  "email": "user@example.com",
  "exact": false,
  "keyword": "example",
  "mode": "default",
  "owner": "John Doe",
  "page": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|current_page|integer|False|Page number of these results|1|
|found|boolean|True|Whether any matching domain was found|True|
|message|string|False|Explanation when no domain was found|Record not found|
|records|[]object|False|Matching WHOIS records on this page|[{"domain_name": "example.net", "email": "user@example.com"}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|total_pages|integer|False|Number of result pages|3|
|total_records|integer|False|Number of matching domains across all pages|120|
  
Example output:

```
{
  "current_page": 1,
  "found": true,
  "message": "Record not found",
  "records": [
    {
      "domain_name": "example.net",
      "email": "user@example.com"
    }
  ],
  "status_code": 200,
  "total_pages": 3,
  "total_records": 120
}
```

#### SSL Lookup

This action is used to retrieve the live SSL/TLS certificate of a domain, optionally with the full chain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name whose certificate is retrieved|None|example.com|None|None|
|include_chain|boolean|False|True|Also return the intermediate and root certificates. This costs extra WhoisFreaks credits|None|False|None|None|
|include_raw|boolean|False|True|Also return the raw PEM certificates|None|False|None|None|
  
Example input:

```
{
  "domain": "example.com",
  "include_chain": false,
  "include_raw": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|certificates|[]object|False|Certificates, with the domain certificate first|[{"chainOrder": "end-user", "serialNumber": "0a1b2c", "signatureAlgorithm": "SHA256withRSA"}]|
|found|boolean|True|Whether a certificate was returned|True|
|message|string|False|Explanation when no certificate was found|No SSL certificate exists for this domain|
|response|object|False|Complete SSL response returned by WhoisFreaks|{'domainName': 'example.com', 'queryTime': '2026-11-04 10:00:00'}|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|valid_from|string|False|Start of the validity period of the domain certificate|2026-01-15 00:00:00 UTC|
|valid_to|string|False|End of the validity period of the domain certificate|2027-01-15 23:59:59 UTC|
  
Example output:

```
{
  "certificates": [
    {
      "chainOrder": "end-user",
      "serialNumber": "0a1b2c",
      "signatureAlgorithm": "SHA256withRSA"
    }
  ],
  "found": true,
  "message": "No SSL certificate exists for this domain",
  "response": {
    "domainName": "example.com",
    "queryTime": "2026-11-04 10:00:00"
  },
  "status_code": 200,
  "valid_from": "2026-01-15 00:00:00 UTC",
  "valid_to": "2027-01-15 23:59:59 UTC"
}
```

#### Subdomains

This action is used to retrieve the known subdomains of a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|after|string|None|False|Only return subdomains seen on or after this date (YYYY-MM-DD)|None|2026-01-01|None|None|
|before|string|None|False|Only return subdomains seen on or before this date (YYYY-MM-DD). It cannot be later than today|None|2026-10-31|None|None|
|domain|string|None|True|Domain whose subdomains are retrieved|None|example.com|None|None|
|page|integer|1|True|Page number to retrieve, starting at 1. Each page costs WhoisFreaks credits|None|1|None|None|
|status|string|None|False|Only return active or inactive subdomains|["active", "inactive"]|active|None|None|
  
Example input:

```
{
  "after": "2026-01-01",
  "before": "2026-10-31",
  "domain": "example.com",
  "page": 1,
  "status": "active"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|current_page|integer|False|Page number of these results|1|
|found|boolean|True|Whether any subdomain was found|True|
|message|string|False|Explanation when no subdomain was found|Record not found|
|records|[]object|False|Subdomains on this page with their first and last seen dates|[{"subdomain": "www.example.com", "first_seen": "2024-01-01", "last_seen": "2026-11-01"}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|total_pages|integer|False|Number of result pages|1|
|total_records|integer|False|Number of subdomains across all pages|80|
  
Example output:

```
{
  "current_page": 1,
  "found": true,
  "message": "Record not found",
  "records": [
    {
      "first_seen": "2024-01-01",
      "last_seen": "2026-11-01",
      "subdomain": "www.example.com"
    }
  ],
  "status_code": 200,
  "total_pages": 1,
  "total_records": 80
}
```

#### Typosquatting

This action is used to find registered look-alike domains of a brand keyword or a domain pattern

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fetch_size|integer|100|True|Number of domains per page (1 to 100)|None|100|None|None|
|keyword|string|None|False|Brand keyword to find look-alike domains of. Use either Keyword or Pattern|None|example|None|None|
|page_token|string|None|False|Next Page Token from a previous run, to retrieve the next page|None|eyJsYXN0SWQiOjEwMH0=|None|None|
|pattern|string|None|False|Domain pattern to find look-alike domains of. Use either Keyword or Pattern|None|example.com|None|None|
  
Example input:

```
{
  "fetch_size": 100,
  "keyword": "example",
  "page_token": "eyJsYXN0SWQiOjEwMH0=",
  "pattern": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|current_page|integer|False|Page number of these results|1|
|found|boolean|True|Whether any look-alike domain was found|True|
|has_next_page|boolean|False|Whether another page is available|True|
|message|string|False|Explanation when no domain was found|Record not found|
|next_page_token|string|False|Token to pass as Page Token to retrieve the next page|eyJsYXN0SWQiOjIwMH0=|
|records|[]object|False|Look-alike domains on this page|[{"domainName": "examp1e.com", "createDate": "2026-10-01", "isDropped": False}]|
|status_code|integer|False|HTTP status code returned by WhoisFreaks|200|
|total_pages|integer|False|Number of result pages|3|
|total_records|integer|False|Number of look-alike domains across all pages|250|
  
Example output:

```
{
  "current_page": 1,
  "found": true,
  "has_next_page": true,
  "message": "Record not found",
  "next_page_token": "eyJsYXN0SWQiOjIwMH0=",
  "records": [
    {
      "createDate": "2026-10-01",
      "domainName": "examp1e.com",
      "isDropped": false
    }
  ],
  "status_code": 200,
  "total_pages": 3,
  "total_records": 250
}
```
### Triggers


#### Newly Registered Domains

This trigger is used to ingest the daily WhoisFreaks newly registered domain feeds for generic and country-code TLDs, 
in batches. Enable one or both feeds; each keeps its own progress

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|batch_size|integer|500|True|Rows requested per page and the maximum rows per event (1 to 1000)|None|500|None|None|
|catch_up_missed_dates|boolean|False|True|Ingest every date after the last completed date, in order, instead of jumping to the latest date|None|False|None|None|
|domain_keywords|[]string|None|False|Only emit domains that contain at least one of these keywords (case-insensitive)|None|["example", "brand"]|None|None|
|include_country_code_tlds|boolean|False|True|Ingest the newly registered domains feed for country-code TLDs such as uk, de and in (cctld)|None|False|None|None|
|include_generic_tlds|boolean|True|True|Ingest the newly registered domains feed for generic TLDs such as com, net and org (gtld)|None|True|None|None|
|include_whois|boolean|False|True|Include the full WHOIS record of every domain. When disabled, only domain names are returned|None|False|None|None|
|poll_interval_minutes|integer|360|True|Minutes to wait for a new feed date after the latest date was ingested (60 to 10080). Feeds are published once per day|None|360|None|None|
|start_date|string|None|False|Feed date (YYYY-MM-DD) to ingest first. When it is empty or outside the feed availability window, the latest date is used. Ignored when the trigger resumes from saved progress|None|2026-11-01|None|None|
|tld_filter|[]string|None|False|Only emit domains under these TLDs, for example com or co.uk|None|["com", "net"]|None|None|
  
Example input:

```
{
  "batch_size": 500,
  "catch_up_missed_dates": false,
  "domain_keywords": [
    "example",
    "brand"
  ],
  "include_country_code_tlds": false,
  "include_generic_tlds": true,
  "include_whois": false,
  "poll_interval_minutes": 360,
  "start_date": "2026-11-01",
  "tld_filter": [
    "com",
    "net"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of rows in Events|500|
|events|[]object|True|Rows of this batch. Each row has domain_name, and the WHOIS columns when Include WHOIS is enabled|[{"domain_name": "example-new.com"}]|
|feed|string|True|Feed that produced the batch, newly.gtld or newly.cctld|newly.gtld|
|feed_date|string|True|Feed date of the batch|2026-11-03|
|next_offset|integer|True|Row offset where the next batch starts within the feed date|500|
|offset|integer|True|Row offset of the first row of the batch within the feed date|0|
  
Example output:

```
{
  "count": 500,
  "events": [
    {
      "domain_name": "example-new.com"
    }
  ],
  "feed": "newly.gtld",
  "feed_date": "2026-11-03",
  "next_offset": 500,
  "offset": 0
}
```

#### Threat Feed

This trigger is used to ingest the daily WhoisFreaks phishing, malware and spam threat feeds, in batches. Enable one or
 more feeds; each keeps its own progress

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|batch_size|integer|500|True|Rows requested per page and the maximum rows per event (1 to 1000)|None|500|None|None|
|catch_up_missed_dates|boolean|False|True|Ingest every date after the last completed date, in order, instead of jumping to the latest date|None|False|None|None|
|domain_keywords|[]string|None|False|Only emit domains that contain at least one of these keywords (case-insensitive)|None|["example", "brand"]|None|None|
|include_malware|boolean|False|True|Ingest the malware threat feed|None|False|None|None|
|include_phishing|boolean|True|True|Ingest the phishing threat feed|None|True|None|None|
|include_spam|boolean|False|True|Ingest the spam threat feed|None|False|None|None|
|min_confidence|number|None|False|Only emit rows whose confidence is at least this value (0 to 1)|None|0.8|None|None|
|poll_interval_minutes|integer|360|True|Minutes to wait for a new feed date after the latest date was ingested (60 to 10080). Feeds are published once per day|None|360|None|None|
|start_date|string|None|False|Feed date (YYYY-MM-DD) to ingest first. When it is empty or outside the feed availability window, the latest date is used. Ignored when the trigger resumes from saved progress|None|2026-11-01|None|None|
  
Example input:

```
{
  "batch_size": 500,
  "catch_up_missed_dates": false,
  "domain_keywords": [
    "example",
    "brand"
  ],
  "include_malware": false,
  "include_phishing": true,
  "include_spam": false,
  "min_confidence": 0.8,
  "poll_interval_minutes": 360,
  "start_date": "2026-11-01"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of rows in Events|500|
|events|[]object|True|Threat feed rows of this batch|[{"domain": "examp1e-login.com", "threat_type": "phishing", "confidence": 1.0, "first_seen": "2026-11-02T00:16:16.035483+00:00", "is_seed": True}]|
|feed|string|True|Feed that produced the batch, threat_feed.phishing, threat_feed.malware or threat_feed.spam|threat_feed.phishing|
|feed_date|string|True|Feed date of the batch|2026-11-03|
|next_offset|integer|True|Row offset where the next batch starts within the feed date|500|
|offset|integer|True|Row offset of the first row of the batch within the feed date|0|
  
Example output:

```
{
  "count": 500,
  "events": [
    {
      "confidence": 1.0,
      "domain": "examp1e-login.com",
      "first_seen": "2026-11-02T00:16:16.035483+00:00",
      "is_seed": true,
      "threat_type": "phishing"
    }
  ],
  "feed": "threat_feed.phishing",
  "feed_date": "2026-11-03",
  "next_offset": 500,
  "offset": 0
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* Connection tests and actions fail with `WhoisFreaks rejected the API key` when the key is wrong, inactive or rotated. Update the API key in the connection
* An error mentioning credits, surcharge or plan limits means the account has no remaining credits or the plan limit was reached. Run the `Get Account Usage` action to check the balance
* Newly registered domain feeds, threat feeds and lookup credits are sold separately. An enabled feed that is not in the WhoisFreaks subscription is skipped with a warning in the trigger log and checked again every 24 hours, while the other enabled feeds continue. The trigger stops with an error only when none of its enabled feeds can be downloaded
* WhoisFreaks enforces a per-minute rate limit per endpoint. The plugin waits for the rate limit window to reset and retries automatically. Persistent `rate limit` errors mean too many workflows share one API key
* Feed files are published once per day. A `Poll Interval` between 360 and 1440 minutes is recommended. The minimum is 60 minutes
* Triggers save their position after every batch and resume after a restart, so at most one batch can be delivered twice after an unexpected shutdown. Deduplicate on the domain and the feed date if exactly-once processing is required
* Private, reserved, loopback and other special-use IP addresses are never sent to WhoisFreaks. Single lookups return `found` set to false, and bulk lookups list them in `skipped`
* Lookups that find no record return `found` set to false instead of failing, so workflows can branch on the result
* The plugin honours the orchestrator HTTPS proxy settings. TLS certificate errors usually mean a TLS-inspecting proxy whose CA is not trusted by the orchestrator

# Version History

* 1.0.0 - Initial plugin

# Links

* [WhoisFreaks](https://whoisfreaks.com)

## References

* [WhoisFreaks API Documentation](https://whoisfreaks.com/documentation)
* [WhoisFreaks Newly Registered Domains](https://whoisfreaks.com/products/newly-registered-domains)
* [WhoisFreaks Threat Intelligence Feed](https://whoisfreaks.com/products/threat-intelligence-feed)