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
|username|string|None|True|Username|None|
|api_key|credential_secret_key|None|True|API key for PassiveTotal|None|

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
|found_domains|[]string|False|Domains found|
|domain_records|[]domain_record|False|Domain Records|

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

#### Lookup SSL

This action is used to check for information about an SSL certificate by its SHA1 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sha1|string|None|True|SHA1 Certificate Hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|address_record|address_record|False|IP Address Record|

#### Lookup Domain

This action is used to check for information about a given domain.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain, e.g. 4.2.2.2|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|domain_record|domain_record|False|Domain Record|

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

#### Lookup Address

This action is used to check for information about a given IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IP Address, e.g. 4.2.2.2|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|address_record|address_record|False|IP Address Record|

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
|found|boolean|False|true if found|
|record|whois_record|False|WHOIS Record Result|

#### Get WHOIS

This action is used to [query WHOIS](https://api.passivetotal.org/api/docs/#api-whois-getv2whoisquery).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Input query, e.g. example.org|None|
|compact_record|boolean|None|False|Set to true to return a compact record.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|true if found|
|record|whois_record|False|WHOIS Record Result|

#### Search WHOIS by Keyword

This action is used to search whois by keyword.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|True|Input query, e.g. email@passivetotal.org|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|## of results returned|
|results|[]whois_keyword_result|False|WHOIS Keyword Results|

#### Get Monitor Alerts

This action is used to retrieve all alerts associated with an artifact or project.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|project|string|None|False|The name of the project to search by|None|
|start|date|None|False|Filter results to after this datetime|None|
|end|date|None|False|Filter results to before this datetime|None|
|artifact|string|None|False|The name of the artifact to search by|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|total_records|number|False|Number of alerts returned|
|results|object|False|Retrieved alerts|

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

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode | Update to new credential types
* 0.4.0 - Add trigger to pull new artifacts
* 0.3.1 - SSL bug fix in SDK
* 0.3.0 - Monitor - Get Alerts action added
* 0.1.0 - Initial plugin

# Links

## References

* [PassiveTotal](https://www.passivetotal.org/)
* [PassiveTotal API](https://api.passivetotal.org/api/docs/)
