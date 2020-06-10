# Description

The Cylance Protect plugin allows you to manage all your CylancePROTECT operations

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Documentation
## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|application_id|credential_secret_key|None|True|Application ID for Cylance Protect instance|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|application_secret|credential_secret_key|None|True|Generated token that allows access to Cylance Resources|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|tenant_id|credential_secret_key|None|True|The unique tenant ID of the tenant that the device belongs to|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|
|url|string|None|True|Web API URL|None|https://example.com|

Example input:

```
{
  "application_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "application_secret": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "tenant_id": "1abc234d-5efa-6789-bcde-0f1abcde23f5",
  "url": "https://example.com"
}
```
## Technical Details

### Actions

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

This action is used to single input to obtain agent information.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts MAC address, hostname, or agent ID|None|1abc234d-5efa-6789-bcde-0f1abcde23f5|

Example input:

```
{
  "agent": "1abc234d-5efa-6789-bcde-0f1abcde23f5"
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
          "10.5.33.69"
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

* 1.0.0 - Initial plugin

# Links

## References

* [Cylance Protect](https://www.cylance.com)
