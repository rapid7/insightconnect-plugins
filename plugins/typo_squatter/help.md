# Description

Typo Squatter detects cybersquatting of domains and allows for domain scoring. This plugin can be used
to aid in phishing investigation and analysis, and can be a very useful tool in keeping your organization safe
from threats.

# Key Features

* Identify potential cybersquatters for your domain
* Get phishing score for a domain

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* dnstwist 20240116

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Check for Squatters

This action is used to look for potential squatters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|example.com|True|Domain to check|None|example.com|None|None|
|flag|string|None|False|Flag to pass for dnstwist (Advanced)|None|--geoip|None|None|
  
Example input:

```
{
  "domain": "example.com",
  "flag": "--geoip"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|potential_squatters|[]object|False|JSON representation of potential squatters|[{"dns_a":["1.2.3.4"],"dns_mx":["test.example.com"],"dns_ns":["dns.example.com"],"domain":"example.com","fuzzer":"*original","geoip":"United States","phishing_score":20}]|
  
Example output:

```
{
  "potential_squatters": [
    {
      "dns_a": [
        "1.2.3.4"
      ],
      "dns_mx": [
        "test.example.com"
      ],
      "dns_ns": [
        "dns.example.com"
      ],
      "domain": "example.com",
      "fuzzer": "*original",
      "geoip": "United States",
      "phishing_score": 20
    }
  ]
}
```

#### Score Domain

This action is used to get phishing score for a domain. Scores over 65 should be considered likely phishing attempts 
with scores over 90 being very suspicious

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|example.com|True|Domain to check|None|example.com|None|None|
  
Example input:

```
{
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|score|number|False|Phishing score|50|
  
Example output:

```
{
  "score": 50
}
```
### Triggers


#### Search Certstream

This trigger is used to searches certstream for new certs matching query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|example.com|False|Domain to check|None|example.com|None|None|
|levenshtein|number|None|False|Levenshtein distance from domain score to match|None|2|None|None|
|query|string|None|False|Query to match|None|[a-z0-9.]+.com|None|None|
  
Example input:

```
{
  "domain": "example.com",
  "levenshtein": 2,
  "query": "[a-z0-9.]+.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|domain|string|False|Matched domain|example.com|
|score|number|False|Phishing score|50|
  
Example output:

```
{
  "domain": "example.com",
  "score": 50
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.3 - Updated SDK and packages to the latest version
* 1.0.2 - Fix Check for Squatters action | Fix Search Certstream trigger | Update container image | Code refactor | Add input and output examples in plugin spec and help.md
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode | Rename "Score domain" action to "Score Domain" | Rename "Search certstream" trigger to "Search Certstream"
* 0.1.1 - Search certstream flag bug fix
* 0.1.0 - Initial plugin

# Links

* [dnstwist](https://github.com/elceef/dnstwist)

## References

* [dnstwist](https://github.com/elceef/dnstwist)
* [phishing_catcher](https://github.com/x0rz/phishing_catcher)
* [Typo Squatting](https://en.wikipedia.org/wiki/Typosquatting)