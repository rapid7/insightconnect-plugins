# Description

This plugin utilizes Cisco Umbrella to get the most complete view of the relationships and evolution of internet domains, IP addresses, and autonomous systems to pinpoint attackers infrastructures and predict future threats

# Key Features

* Most Recent Requests
* Security Activity Report

# Requirements

* Requires an API Key and Secret from Cisco Umbrella (API Key) - refer to the links section for information on how to create/refresh/delete the API key

# Supported Product Versions

* Cisco Umbrella Reporting API v2

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Cisco Umbrella API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|api_secret|credential_secret_key|None|True|Cisco Umbrella API secret key|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "api_secret": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions

#### Get Domain Visits

This action is used to get a list of computers that visited an address for the last 24 hours, up to 500 results of computers that accessed the address.
It accepts the following address types as input: domains, IPs, and URLs. URLs will automatically be stripped down to the domain since the Umbrella API does not accept URLs. If no address is provided, then the action will return activities for all domains in the organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|False|Domain, IP address, or URL to search for computer visits. If a URL is provided it will be stripped down to a domain or IP address. If this field is empty, it will return activities for all domains in the organization|None|example.com|
|from|string|-1days|True|A timestamp or relative time string (for example, '-1days', '-31days') that filters for data appearing after this time, described in ISO 8601 format, where the maximum value is '-31days'|None|-1days|
|limit|integer|0|True|A timestamp or relative time string (for example, '-1days', '-31days') that filters for data appearing after this time, described in ISO 8601 format, where the maximum value is '-31days'. To search for all records, set the limit to 0|None|100|
|order|string|Descending|False|Describes how the results obtained should be ordered. Defaults to descending, even if it's empty|['', 'Ascending', 'Descending']|Descending|
|threatTypes|[]string|None|False|The array of threat types for results to be filtered on|None|["Malware", "Ransomware"]|
|threats|[]string|None|False|The array of threat names for results to be filtered on|None|["Example", "Example2"]|
|verdict|[]string|None|False|The array of verdicts for results to be filtered on, where possible values are (Allowed, Blocked, Proxied)|None|["Allowed", "Blocked"]|

Example input:

```
{
  "address": "example.com",
  "from": "-1days",
  "limit": 100,
  "order": "Descending",
  "threatTypes": [
    "Malware",
    "Ransomware"
  ],
  "threats": [
    "Example",
    "Example2"
  ],
  "verdict": [
    "Allowed",
    "Blocked"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domain_visits|[]record|True|List of computers that visited a domain|

Example output:

```
{
  "domain_visits": [
    {
      "externalIp": "255.255.255.255",
      "internalIp": "255.255.255.255",
      "categories": [
        "Malware"
      ],
      "verdict": "allowed",
      "domain": "example.com",
      "datetime": "2019-01-24T06:31:46",
      "timestamp": 1548311506,
      "identities": [
        {
          "id": 1,
          "label": "ExampleName",
          "deleted": true
        }
      ],
      "threats": [
        {
          "label": "Wannacry",
          "type": "Ransomware"
        }
      ],
      "allApplications": [
        "ExampleApp"
      ],
      "allowedApplications": [
        "ExampleApp"
      ],
      "queryType": "MX"
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### identity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Deleted|boolean|False|A true/false flag indicating whether or not the identity is deleted|
|ID|integer|False|The identifier of an identity|
|Label|string|False|The label of an identity|

#### record

|Name|Type|Required|Description|
|----|----|--------|-----------|
|All Applications|[]string|False|An array of all applications for entry|
|Allowed Applications|[]string|False|An array of allowed applications for entry|
|Blocked Applications|[]string|False|An array of blocked applications for entry|
|Categories|[]string|False|Which categories, if any, the destination for which this request was made falls into|
|Datetime|date|False|UTC Datetime at which the event occurred, represented in ISO 8601 format|
|Domain|string|False|Domain to which this request was made|
|External IP|string|False|External IP address of the identity making the request|
|Identities|[]identity|False|An array of identities for entry|
|Internal IP|string|False|Internal IP address of the identity making the request|
|Query Type|string|False|The type of DNS request that was made|
|Threats|[]string|False|An array of threats for entry|
|Timestamp|integer|False|The unix UTC timestamp in milliseconds|
|Verdict|string|False|The entry verdict|

#### threat

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Label|string|False|The threat label|
|Type|string|False|Type of threat|


## Troubleshooting

* The Cisco Umbrella Legacy API Keys are no longer used. Please use the Cisco Umbrella API Keys. Refer to the links section for information on how to create/refresh/delete the API key.

# Version History

* 2.0.0 - Updated plugin to use API v2 | OAuth20 authentication method is now used | Removed organization ID from the connection inputs
* 1.0.1 - Docs - Update help.md to include information about legacy keys
* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Umbrella](https://umbrella.cisco.com/)
* [Cisco Umbrella Docs](https://docs.umbrella.com/)
* [Cisco Umbrella Reporting](https://docs.umbrella.com/deployment-umbrella/docs/getting-started-learning-to-use-reports-and-exporting-reports)
* [Creating/Refreshing/Deleting Umbrella API Keys](https://developer.cisco.com/docs/cloud-security/#!authentication/manage-api-keys)
