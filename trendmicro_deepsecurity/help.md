# Description

[Trend Micro Deep Security](https://www.trendmicro.com/en_us/business/products/hybrid-cloud/deep-security.html) is an endpoint protection software with multiple modules such as Anti-Virus, Intrusion Prevention (Virtual Patching), Integrity Monitoring and more.

# Key Features

* Utilize the Deep Security IPS engine to protect against vulnerabilities without installing a patch (virtual patching)

# Requirements

* Trend Micro Deep Security

# Documentation

## Setup

* [Create an API key for Deep Security](https://help.deepsecurity.trendmicro.com/api-key.html)
* Create a new connection and enter the Deep Security Manager URL and API key

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|dsm_api_key|credential_secret_key|None|True|API key of the Deep Security Manager|None|12345678-ABCD-1234-ABCD-123456789012:ABCDEFGH-1234-ABCD-1234-ABCDEFGHIJKL:12345678901234567890123456789012345678901234|
|dsm_url|string|https://app.deepsecurity.trendmicro.com|True|URL of the Deep Security Manager|None|https://192.51.100.100:4119|
|dsm_verify_ssl|boolean|True|True|Check the certificate of the Deep Security Manager|None|True|

## Technical Details

### Actions

#### List

This action is used to list IPS rules.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|computer_or_policy|string|None|True|Get IPS rules from a computer or policy|['computer', 'policy']|policy|
|id|integer|None|True|ID of the computer or policy|None|23|

Example input:

```
{
  "computer_or_policy": "policy",
  "id": 23
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rules_assigned|[]integer|False|All IPS rules currently assigned|
|rules_not_recommended|[]integer|False|IPS rules that are not recommended|
|rules_recommended|[]integer|False|Recommended IPS rules|

Example output:

```
{
  "rules_assigned": [
    108,
    2874,
    2875,
    2876,
    3317,
    3318,
    6348
  ],
  "rules_not_recommended": [],
  "rules_recommended": []
}
```

#### Search

Search for matching IPS rules in Deep Security by CVE ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|vulnerabilities|[]string|None|True|CVEs to protect against|None|['CVE-2005-0045', 'CVE-2014-0160', 'CVE-2017-0144', 'CVE-1337-1337']|

Example input:

```
{
  "vulnerabilities": [
    "CVE-2005-0045",
    "CVE-2014-0160",
    "CVE-2017-0144",
    "CVE-1337-1337"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ips_rules|[]integer|False|IPS rules matching the given CVEs|
|matched_cves|[]string|False|CVEs with at least one matching IPS rule|
|missed_cves|[]string|False|CVEs without matching IPS rules|

Example output:

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

Deploy the given Deep Security IPS rules to a computer or policy

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|computer_or_policy|string|None|True|Target for rule assignment|['computer', 'policy']|policy|
|id|integer|None|True|ID of the target computer or policy|None|23|
|rules|[]integer|None|True|IPS rules to assign|None|[108, 6745, 2874, 2875, 2876, 3317, 3318]|

Example input:

```
{
  "computer_or_policy": "policy",
  "id": 23,
  "rules": [108, 6745, 2874, 2875, 2876, 3317, 3318]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rules_assigned|[]integer|False|All IPS rules currently assigned|
|rules_not_assigned|[]integer|False|Unassigned IPS rules|

Example output:

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

* 2.0.0 - Add an option to toggle DSM certificate verification in the connection
* 1.0.0 - Initial plugin

# Links

## References

* [Trend Micro Deep Security](https://www.trendmicro.com/en_us/business/products/hybrid-cloud/deep-security.html)
