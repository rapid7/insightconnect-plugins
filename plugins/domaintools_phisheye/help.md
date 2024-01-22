# Description

[DomainTools PhishEye](https://www.domaintools.com/resources/user-guides/phisheye) is a potent tool in your battle against nefarious domains and the criminals who operate them. Leveraging DomainTools’ unique visibility into over 315 million current domains, PhishEye finds domains that mimic your properties, whether by typo or by combining your brand with other terms—terms like “account,” “login,” “online,” or countless others.

This plugin allows you to enter a keyword, and PhishEye will return a sample of the existing domains that mimic that term.

# Key Features

* Identify phishing domains

# Requirements

* Requires an API Key

# Supported Product Versions
  
* Domain Tools API 18-01-24

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|API key|None|11111-aaaaa-aaa11-111aa-aaa11|
|username|string|None|True|API username|None|user1|

Example input:

```
{
  "api_key": "11111-aaaaa-aaa11-111aa-aaa11",
  "username": "user1"
}
```

## Technical Details

### Actions

#### Domain List
  
This action is used to returns domain results for monitored terms

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_back|integer|None|False|Use this parameter in exceptional circumstances where you need to find domains up to seven days prior to the current date|[0, 1, 2, 3, 4, 5, 6, 7]|1|
|query|string|None|True|Term for which the day's domains are desired|None|example|
  
Example input:

```
{
  "days_back": 1,
  "query": "example"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|date|string|False|Date when query run|2016-11-01|
|domains|[]domains|True|Domains for query|None|
|term|string|True|Query term|apple|
  
Example output:

```
{
  "date": "2016-11-01",
  "domains": [
    {
      "Created Date": {},
      "Domain": "appeltypoexample.com",
      "IP Addresses": [
        {
          "Country Code": {},
          "IPv4": {}
        }
      ],
      "Name Servers": "ns57.domaincontrol.com",
      "Registrant Email": {},
      "Registrar Name": {},
      "Risk Score": 24,
      "TLD": {}
    }
  ],
  "term": "apple"
}
```

### Triggers
  
*This plugin does not contain any triggers.*

### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**ip_addresses**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Country Code|string|None|True|Country code|US|
|IPv4|string|None|True|IPv4 address|1.1.1.1|
  
**domains**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created Date|string|None|False|Date when domain created|2016-10-31|
|Domain|string|None|True|Links to WHOIS page for the domain|appeltypoexample.com|
|IP Addresses|[]ip_addresses|None|False|IPv4 addresses|None|
|Name Servers|[]string|None|False|Name servers used by domain|['ns57.domaincontrol.com', 'ns58.domaincontrol.com']|
|Registrant Email|string|None|False|Email used for register|user@example.com|
|Registrar Name|string|None|False|Registrar name where domain was registered|GoDaddy.com, LLC|
|Risk Score|integer|None|False|Calculated by the Domain Risk Score|24|
|TLD|string|None|True|TLD domain|com|


## Troubleshooting

Users configure terms (not domains) in DomainTools PhishEye Monitor. It may take up to 24 hours for discovery to be completed within PhishEye.
Following initial discovery, new alerts are generated in PhishEye every 24 hours containing new domains that can be searched with the Domain List action.

If a term is searched for in the Domain List action but not monitored in PhishEye, the action will fail and return a list of the monitored terms from which the user can use.

# Version History

* 1.0.2 - Update `domaintools-api` v0.3.3 -> v1.0.1 | Update SDK
* 1.0.1 - Add `0` parameter to Days Back input in Domain List action to get current day results
* 1.0.0 - Initial plugin

# Links

* [DomainTools PhishEye](https://www.domaintools.com/resources/user-guides/phisheye)

## References

* [DomainTools API](https://www.domaintools.com/resources/api-documentation/)
* [DomainTools Python API](https://github.com/domaintools/python_api)
