# Description

This plugin utilizes Cisco Umbrella to get the most complete view of the relationships and evolution of internet domains, IP addresses, and autonomous systems to pinpoint attackers infrastructures and predict future threats

# Key Features

* Most Recent Requests
* Security Activity Report

# Requirements

* Requires an API Key and Secret from Cisco Umbrella
* Requires Cisco Umbrella organization ID

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Cisco Umbrella API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|api_secret|credential_secret_key|None|True|Cisco Umbrella API secret key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|organization_id|string|None|True|ID of your Cisco Umbrella organization|None|2961483|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "api_secret": "9de5069c5afe602b2ea0a04b66beb2c0",
  "organization_id": 2961483
}
```

## Technical Details

### Actions

#### Get Domain Visits

This action is used to get a list of computers that visited an address for the last 24 hours, up to 500 results of computers that accessed the address
.
It accepts the following address types as input: domains, IPs, and URLs. URLs will automatically be stripped down to the domain since the Umbrella API does not accept URLs. If no address is provided, then the action will return activities for all domains in the organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|False|Domain, IP address, or URL to search for computer visits. If a URL is provided it will be converted to a domain or IP address. If this field is empty, it will return activities for all domains in the organization.|None|example.com|

Example input:

```
{
  "address": "example.com"
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
      "tags": [],
      "originId": 121212121,
      "originType": "AD Users",
      "internalIp": "198.51.100.100",
      "externalIp": "198.51.100.100",
      "categories": [
        "Dynamic DNS",
        "Web Hosting"
      ],
      "destination": "example.com",
      "originLabel": "User (user@example.com)",
      "actionTaken": "BLOCKED",
      "datetime": "2020-11-05T23:29:55.000Z"
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### record

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action Taken|string|False|Either Blocked or Allowed|
|Categories|[]string|False|Which categories, if any, the destination for which this request was made falls into|
|Datetime|string|False|Datetime at which the event occurred, in UTC|
|Destination|string|False|Destination to which this request was made|
|External IP|string|False|External IP address of the identity making the request|
|Internal IP|string|False|Internal IP address of the identity making the request|
|Origin Label|string|False|Human readable name for the identity, matches the one seen in the dashboard|
|Origin Type|string|False|Identity type (such as network, roaming computer, AD User, etc)|
|Origin ID|integer|False|Numerical identifier for the identity making the request|
|Tags|[]string|False|Which tags, if any, the destination for which this request was made falls into|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Umbrella](https://umbrella.cisco.com/)
* [Cisco Umbrella Docs](https://docs.umbrella.com/)
* [Cisco Umbrella Reporting](https://docs.umbrella.com/deployment-umbrella/docs/getting-started-learning-to-use-reports-and-exporting-reports)
