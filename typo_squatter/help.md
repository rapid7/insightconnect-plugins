
# Typo Squatter

## About

The Type Squatter plugin looks for cybersquatters on a domain.

## Actions

### Check for Squatters

This action is used to look for potential squatters.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|google.com|True|Domain to check|None|
|flag|string|None|False|Flag to pass for dnstwist (Advanced)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|potential_squatters|[]object|False|JSON representation of potential squatters|

### Score Domain

This action is used to get phishing score for domain. score > 90: very suspicous, > 65 likely phising.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|google.com|True|Domain to check|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|score|number|False|Phishing score|

## Triggers

### Search Certstream

This trigger is used to searches certstream for new certs matching query.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|False|Query to match|None|
|domain|string|google.com|False|Domain to check|None|
|levenshtein|number|None|False|Levenshtein distance from domain score to match|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain|string|False|Matched domain|
|score|number|False|Phishing score|

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - Search certstream flag bug fix
* 1.0.0 - Support web server mode | Rename "Score domain" action to "Score Domain" | Rename "Search certstream" trigger to "Search Certstream"

## Workflows

Examples:

* Uncover squatting attacks

## References

* [dnstwist](https://github.com/elceef/dnstwist)
* [phishing_catcher](https://github.com/x0rz/phishing_catcher)
* [Typo Squatting](https://en.wikipedia.org/wiki/Typosquatting)
