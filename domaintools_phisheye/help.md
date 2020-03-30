# Description

Monitor the Internet for 'Phishy' Domains

# Key Features

Identify key features of plugin.

# Requirements

* Requires an API Key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|Enter the API key e.g. 11111-aaaaa-aaa11-111aa-aaa11|None|
|username|string|None|True|Enter the API username|None|

Example input:

```
{
  "api_key": {
    "secretKey": "11111-aaaaa-aaa11-111aa-aaa11"
  },
  "username": "username"
}
```

## Technical Details

### Actions

#### Domain List

This action returns domain results for monitored terms.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|days_back|integer|None|False|Use this parameter in exceptional circumstances where you need to find domains up to seven days prior to the current date. Set the value to an integer in the range of 1-7|None|
|query|string|None|True|Term for which the day's domains are desired|None|

Example input:

```
{
  "query": "rapid7",
  "days_back": 10
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|string|False|Date when query run|
|domains|[]domains|True|Domains for query|
|term|string|True|Query term|

Example output:

```
{
  "domains": [],
  "term": "rapid7"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### domains

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created Date|string|False|Date when domain created|
|Domain|string|True|Links to WHOIS page for the domain|
|IP Addresses|[]ip_addresses|False|IPv4 Addresses|
|Name Servers|[]string|False|Name servers used by domain|
|Registrant Email|string|False|Email used for register|
|Registrar Name|string|False|Registrar name where domain was registered|
|Risk Score|integer|False|Calculated by the Domain Risk Score|
|TLD|string|True|TLD domain|

#### ip_addresses

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Country Code|string|True|Country code|
|IPv4|string|True|IPv4 Address|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [DomainTools PhishEye](https://www.domaintools.com/resources/user-guides/phisheye)
* [DomainTools API](https://www.domaintools.com/resources/api-documentation/)
* [DomainTools Python API](https://github.com/domaintools/python_api)
