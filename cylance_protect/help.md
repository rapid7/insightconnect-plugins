# Description

The [BlackBerry CylancePROTECT](https://www.cylance.com/en-us/platform/products/cylance-protect.html) plugin allows you to automate response operations.

# Key Features

* Get agent details
* Blacklist a malicious hash

# Requirements

* CylancePROTECT configured with an Custom Application

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|application_id|credential_secret_key|None|True|Application ID for CylancePROTECT instance|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|application_secret|credential_secret_key|None|True|Generated token that allows access to Cylance Resources|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|tenant_id|credential_secret_key|None|True|The unique tenant ID of the tenant that the device belongs to|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|url|string|https://protectapi.cylance.com|True|Web API URL|None|https://protectapi.cylance.com|

Example input:

```
{
  "application_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "application_secret": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "tenant_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "url": "https://protectapi.cylance.com"
}
```

## Technical Details

### Actions

#### Search Threats

This action finds and displays detailed information about one or more threats.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|score|integer|None|False|Filter the search by the Cylance score assigned to the threat. Accepts an integer within the range [-1,1]|None|-1|
|threat_identifier|[]string|None|True|The threat(s) to search for. The input should be an array of threat names, md5, or sha256 hashes|None|["9de5069c5afe602b2ea0a04b66beb2c0", "02699626f388ed830012e5b787640e71c56d42d8", "Example-Threat-Name"]|

Example input:

```
{
  "score": -1,
  "threat_identifier": [
    "9de5069c5afe602b2ea0a04b66beb2c0",
    "02699626f388ed830012e5b787640e71c56d42d8",
    "Example-Threat-Name"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threats|[]threat|True|Detailed information about threats found|

Example output:

```
```

#### Search Threat Agents

This action finds and displays detailed information about threat and device details for a threat.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|threat_identifier|string|None|True|The threat to search for. The input should be a threat name, md5, or sha256 hash|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "threat_identifier": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|threat_agents|[]threat_device|True|Detailed information about threat agents found|

Example output:

```
```

#### Quarantine

This action is used to quarantine (isolate) an endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Device to perform quarantine action on. Accepts IP address, MAC address, hostname, or device ID|None|Example-Hostname|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be blocked. This can include IPs, hostnames or device IDs|None|["198.51.100.100", "Example-Hostname", "1abc234d-5efa-6789-bcde-0f1abcde23f5"]|

Example input:

```
{
  "agent": "Example-Hostname",
  "whitelist": [
    "198.51.100.100",
    "Example-Hostname",
    "1abc234d-5efa-6789-bcde-0f1abcde23f5"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|lockdown_details|lockdown_response|True|Detailed information about the device lockdown|

Example output:

```
{
    "status": "COMPLETE",
    "data": {
        "id": "1ABC234D5EFA6789BCDE0F1ABCDE23F5",
        "hostname": "Example-Hostname",
        "tenant_id": "1abc234d5efa6789bcde0f1abcde23f5",
        "connection_status": "locked",
        "optics_device_version": "2.4.2100.1015",
        "password": "unlock-pa22-w0rd",
        "lockdown_expiration": "2020-07-11T21:15:29Z",
        "lockdown_initiated": "2020-07-08T21:15:29Z"
    }
}
```

#### Blacklist

This action is used to blacklist (quarantine) a hash globally.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|blacklist_state|boolean|None|True|True to blacklist hash, false to unblacklist hash|None|True|
|description|string|Hash Blacklisted from InsightConnect|True|Description for why the hash is blacklisted|None|Hash Blacklisted from InsightConnect|
|hash|string|None|True|Create a blacklist item from a SHA256 hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|

Example input:

```
{
  "blacklist_state": true,
  "description": "Hash Blacklisted from InsightConnect",
  "hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if blacklist item was created or deleted|

Example output:

```
{
  "success": true
}
```

#### Get Agent Details

This action is used to obtain agent information.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts MAC address, hostname, or agent ID|None|cylance-agent-win12|

Example input:

```
{
  "agent": "cylance-agent-win12"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent|True|Details for an agent|

Example output:

```
{
      "agent": {
        "id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
        "name": "NA-TESTX-NAM11",
        "host_name": "na-testx-nam11",
        "os_version": "Microsoft Windows Server 2012 Standard",
        "state": "Online",
        "agent_version": "2.0.1540",
        "policy": {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "Default"
        },
        "last_logged_in_user": "NA-TESTX-NAM11\\Administrator",
        "update_available": false,
        "background_detection": false,
        "is_safe": false,
        "date_first_registered": "2020-05-28T14:00:50",
        "ip_addresses": [
          "198.51.100.100"
        ],
        "mac_addresses": [
          "00-60-26-26-D5-19"
        ]
      }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.3.0 - New actions Search Threats, Search Threat Agents
* 1.1.0 - New action Quarantine
* 1.0.3 - Match official branding in plugin title
* 1.0.2 - Update to fix connection test
* 1.0.1 - Add SHA256 input validation in Blacklist action
* 1.0.0 - Initial plugin

# Links

## References

* [BlackBerry CylancePROTECT](https://www.cylance.com)
