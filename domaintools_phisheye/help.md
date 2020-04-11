# Description

[DomainTools PhishEye](https://www.domaintools.com/resources/user-guides/phisheye) is a potent tool in your battle against nefarious domains and the criminals who operate them. Leveraging DomainTools’ unique visibility into over 315 million current domains, PhishEye finds domains that mimic your properties, whether by typo or by combining your brand with other terms—terms like “account,” “login,” “online,” or countless others.

This plugin allows you to enter a keyword, and PhishEye will return a sample of the existing domains that mimic that term.

# Key Features

* Identify phishing domains

# Requirements

* Requires an API Key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API key e.g. 11111-aaaaa-aaa11-111aa-aaa11|None|11111-aaaaa-aaa11-111aa-aaa11|
|username|string|None|True|API username|None|user1|

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

This action returns domain results for monitored terms. By default, the API will return domains discovered in the last 24 hours.
Terms must be created (monitored) in PhishEye before they can be returned by this action.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|days_back|integer|None|False|Use this parameter in exceptional circumstances where you need to find domains up to seven days prior to the current date. Set the value to an integer in the range of 1-7|None|1|
|query|string|None|True|Term for which the day's domains are desired|None|example|

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
  "date": "2020-04-10",
  "domains": [
    {
      "created_date": "2020-04-09",
      "domain": "2020insightsolutions.com",
      "ip_addresses": [
        {
          "country_code": "US",
          "ip": "50.63.202.50"
        },
        {
          "country_code": "US",
          "ip": "50.63.202.50"
        }
      ],
      "name_servers": [
        "ns11.domaincontrol.com",
        "ns12.domaincontrol.com"
      ],
      "registrant_email": "2020insightsolutions.com@domainsbyproxy.com",
      "registrar_name": "GoDaddy.com, LLC",
      "risk_score": 15,
      "tld": "com"
    },
    {
      "created_date": "2020-04-09",
      "domain": "accelerateinsights.org",
      "ip_addresses": [
        {
          "country_code": "US",
          "ip": "184.168.221.57"
        },
        {
          "country_code": "US",
          "ip": "184.168.221.57"
        }
      ],
      "name_servers": [
        "ns65.domaincontrol.com",
        "ns66.domaincontrol.com"
      ],
      "registrar_name": "GoDaddy.com, LLC",
      "risk_score": 14,
      "tld": "org"
    },
    {
      "created_date": "2020-04-04",
      "domain": "zthetrueinsight.uk",
      "ip_addresses": [
        {
          "country_code": "US",
          "ip": "184.168.221.63"
        },
        {
          "country_code": "US",
          "ip": "184.168.221.63"
        }
      ],
      "name_servers": [
        "ns29.domaincontrol.com",
        "ns30.domaincontrol.com"
      ],
      "registrar_name": "GoDaddy.com, LLC. [Tag = GODADDY]",
      "risk_score": 14,
      "tld": "uk"
    }
  ],
  "term": "insight"
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

Users configure terms (not domains) in DomainTools PhishEye Monitor. It may take up to 24 hours for discovery to be completed within PhishEye.
Following initial discovery, new alerts are generated in PhishEye every 24 hours containing new domains that can be searched with the Domain List action.

If a term is searched for in the Domain List action but not monitored in PhishEye, the action will fail and return a list of the monitored terms from which the user can use.

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [DomainTools PhishEye](https://www.domaintools.com/resources/user-guides/phisheye)
* [DomainTools API](https://www.domaintools.com/resources/api-documentation/)
* [DomainTools Python API](https://github.com/domaintools/python_api)
