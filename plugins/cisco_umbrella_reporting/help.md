# Description

This plugin utilizes Cisco Umbrella to get the most complete view of the relationships and evolution of Internet domains, IP addresses, and autonomous systems to pinpoint attackers infrastructures and predict future threats

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

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Cisco Umbrella API key|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|api_secret|credential_secret_key|None|True|Cisco Umbrella API secret key|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|

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

This action is used to get a list of computers that visited a domain within the last 24 hours for up to 500 computers

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|False|Domain, IP address, or URL to search for computer visits. If a URL is provided it will be stripped down to a domain or IP address. If this field is empty, it will return activities for all domains in the organization|None|example.com|None|None|
|from|string|-1days|True|A timestamp or relative time string (for example, '-1days', '-31days') that filters for data appearing after this time, described in ISO 8601 format, where the maximum value is '-31days'|None|-1days|None|None|
|limit|integer|0|True|A timestamp or relative time string (for example, '-1days', '-31days') that filters for data appearing after this time, described in ISO 8601 format, where the maximum value is '-31days'. To search for all records, set the limit to 0|None|100|None|None|
|order|string|Descending|False|Describes how the results obtained should be ordered. Defaults to descending, even if it's empty|["", "Ascending", "Descending"]|Descending|None|None|
|threatTypes|[]string|None|False|The array of threat types for results to be filtered on|None|["Malware", "Ransomware"]|None|None|
|threats|[]string|None|False|The array of threat names for results to be filtered on|None|["Example", "Example2"]|None|None|
|verdict|[]string|None|False|The array of verdicts for results to be filtered on, where possible values are (Allowed, Blocked, Proxied)|None|["Allowed", "Blocked"]|None|None|
  
Example input:

```
{
  "address": "example.com",
  "from": "-1days",
  "limit": 0,
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|domain_visits|[]record|True|List of computers that visited a domain|None|
  
Example output:

```
{
  "domain_visits": [
    {
      "All Applications": {},
      "Allowed Applications": {},
      "Blocked Applications": {},
      "Categories": [
        {}
      ],
      "Datetime": "",
      "Domain": {},
      "External IP": {},
      "Identities": [
        {
          "Deleted": "true",
          "ID": {},
          "Label": {}
        }
      ],
      "Internal IP": "",
      "Query Type": {},
      "Threats": {},
      "Timestamp": 0,
      "Verdict": {}
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**identity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Deleted|boolean|None|False|A true/false flag indicating whether or not the identity is deleted|None|
|ID|integer|None|False|The identifier of an identity|None|
|Label|string|None|False|The label of an identity|None|
  
**threat**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Label|string|None|False|The threat label|None|
|Type|string|None|False|Type of threat|None|
  
**record**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|All Applications|[]string|None|False|An array of all applications for entry|None|
|Allowed Applications|[]string|None|False|An array of allowed applications for entry|None|
|Blocked Applications|[]string|None|False|An array of blocked applications for entry|None|
|Categories|[]string|None|False|Which categories, if any, the destination for which this request was made falls into|None|
|Datetime|date|None|False|UTC Datetime at which the event occurred, represented in ISO 8601 format|None|
|Domain|string|None|False|Domain to which this request was made|None|
|External IP|string|None|False|External IP address of the identity making the request|None|
|Identities|[]identity|None|False|An array of identities for entry|None|
|Internal IP|string|None|False|Internal IP address of the identity making the request|None|
|Query Type|string|None|False|The type of DNS request that was made|None|
|Threats|[]string|None|False|An array of threats for entry|None|
|Timestamp|integer|None|False|The unix UTC timestamp in milliseconds|None|
|Verdict|string|None|False|The entry verdict|None|


## Troubleshooting

* The Cisco Umbrella Legacy API Keys are no longer used. Please use the Cisco Umbrella API Keys. Refer to the links section for information on how to create/refresh/delete the API key.
* The Get Domain Visits action accepts domains, IPs, and URLs as the address. URLs will automatically be stripped down to the domain since the Umbrella API does not accept URLs.
* If no address is provided to the Get Domain Visits action, it will return activities for all domains in the organization.

# Version History

* 2.0.1 - Updated SDK to the latest version (6.6.0) | Updated dependencies
* 2.0.0 - Updated plugin to use API v2 | OAuth20 authentication method is now used | Removed organization ID from the connection inputs
* 1.0.1 - Docs - Update help.md to include information about legacy keys
* 1.0.0 - Initial plugin

# Links

* [Cisco Umbrella](https://umbrella.cisco.com/)

## References

* [Cisco Umbrella Docs](https://docs.umbrella.com/)
* [Cisco Umbrella Reporting](https://docs.umbrella.com/deployment-umbrella/docs/getting-started-learning-to-use-reports-and-exporting-reports)
* [Creating/Refreshing/Deleting Umbrella API Keys](https://developer.cisco.com/docs/cloud-security/#!authentication/manage-api-keys)