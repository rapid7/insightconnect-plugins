# Description

[Trend Micro Deep Security](https://www.trendmicro.com/en_us/business/products/hybrid-cloud/deep-security.html) is an endpoint protection software with multiple modules such as Anti-Virus, Intrusion Prevention (Virtual Patching), Integrity Monitoring and more.

# Key Features

* Utilise the Deep Security IPS engine to protect against vulnerabilities without installing a patch (virtual patching)

# Requirements

* Trend Micro Deep Security

# Documentation

## Setup

* Enter Credentials for the Deep Security Manager

## Technical Details

### Actions

#### Search

Search for matching IPS rules in Deep Security by CVE ID

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|asset_hostname_dsm|string|None|False|Hostname of the asset in the Deep Security Manager|None|
|asset_hostname_ivm|string|None|False|Hostname of the asset in InsightVM|None|
|dsm_api_key|string|None|True|API key of the Deep Security Manager|None|
|dsm_url|string|https://app.deepsecurity.trendmicro.com|True|URL of the Deep Security Manager|None|
|ivm_password|password|None|False|InsightVM Password|None|
|ivm_url|string|https://insightvm.company.de:3780/|False|URL of the InsightVM console|None|
|ivm_user|string|nxadmin|False|InsightVM Username|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ips_rules|[]integer|False|IPS rules matching the given CVE numbers|
|matched_cves|[]string|False|CVEs that have at least one matching IPS rule in Deep Security|
|missed_cves|[]string|False|CVEs without matching IPS rule in Deep Security|

###### Example

```
{
  "ips_rules": [
    108,
    6348,
    3317,
    3318,
    2874,
    2875,
    2876
  ],
  "matched_cves": [
    "CVE-2005-0045",
    "CVE-2017-0144",
    "CVE-2014-0160"
  ],
  "missed_cves": [
    "CVE-1337-1337"
  ]
}
```

#### Deploy

This action is used to search Deep Security IPS rules for given CVEs.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|computer_or_policy|string|None|True|Define if the rules get assigned to a computer or policy|['computer', 'policy']|
|id|integer|None|True|ID of the target asset or policy in Deep Security|None|
|rules|[]integer|None|True|IPS rules to assign|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rules_assigned|[]integer|False|All rules that are currently assigned to the asset|
|rules_not_assigned|[]integer|False|Rules that were not assigned|

###### Example

```
{
  "rules_assigned": [
    108,
    2874,
    2875,
    2876,
    3118,
    3124,
    3125,
    3126,
    3317,
    3318,
    4593,
    5177,
    5892,
    6348,
    6745
  ],
  "rules_not_assigned": []
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Trend Micro Deep Security](https://www.trendmicro.com/en_us/business/products/hybrid-cloud/deep-security.html)

## Author

* [Philipp Behmer](http://philippbehmer.de)
