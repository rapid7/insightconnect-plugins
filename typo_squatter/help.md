# Description

Typo Squatter detects cybersquatting of domains and allows for domain scoring. This plugin can be used
to aid in phishing investigation and analysis, and can be a very useful tool in keeping your organization safe
from threats.

# Key Features

* Score domains
* Detect cybersquatters

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Check for Squatters

This action is used to look for potential squatters.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|google.com|True|Domain to check|None|
|flag|string|None|False|Flag to pass for dnstwist (Advanced)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|potential_squatters|[]object|False|JSON representation of potential squatters|

#### Score Domain

This action is used to get phishing score for domain. score > 90: very suspicous, > 65 likely phising.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|google.com|True|Domain to check|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|score|number|False|Phishing score|

### Triggers

#### Search Certstream

This trigger is used to searches certstream for new certs matching query.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|False|Query to match|None|
|domain|string|google.com|False|Domain to check|None|
|levenshtein|number|None|False|Levenshtein distance from domain score to match|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain|string|False|Matched domain|
|score|number|False|Phishing score|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Support web server mode | Rename "Score domain" action to "Score Domain" | Rename "Search certstream" trigger to "Search Certstream"
* 0.1.1 - Search certstream flag bug fix
* 0.1.0 - Initial plugin

# Links

## References

* [dnstwist](https://github.com/elceef/dnstwist)
* [phishing_catcher](https://github.com/x0rz/phishing_catcher)
* [Typo Squatting](https://en.wikipedia.org/wiki/Typosquatting)

