# Description

Stop modern attacks with the industry’s first extended detection and response platform that spans your endpoint, network and cloud data.

# Key Features

* Get Endpoint Information
* Isolate or Unisolate endpoints

# Requirements

* An API Key
* The API Key ID
* The FQDN to your API instance

The required connection information is available in the Cortex XDR web dashboard. Go 
to the gear icon, click settings, and then click on API Keys in the left. 

The API Key will be generated when you create a new API key. 

The API Key ID is the value from the ID column

To get the FQDN, right click on your API key and pick generate examples. In the example
that's generated will be a URL that looks like "https://api-yourorg.xdr.us.paloaltonetworks.com/api_keys/validate/". 
Copy the part that looks like "https://api-yourorg.xdr.us.paloaltonetworks.com". That is your FQDN. 


# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|The API Key that is generated when creating a new key|None|1234123412341234asdfasdfasdfasdfasdf1234123412341234123412341234asdfasdfasdfasdfasdf123412341234123412341234asdfasdfasdfasdfasdf|
|api_key_id|int|None|True|The API Key ID shown in the API Keys table in settings. e.g. 1, 2, 3|None|1|
|fqdn|string|None|True|Fully qualified domain name|None|https://api-example.xdr.us.paloaltonetworks.com/|
|security_level|string|Standard|True|The Security Level of the key provided. This can be found in the API Key settings table in the Cortex XDR settings|['Advanced', 'Standard']|Standard|

Example input:

```
{
  "api_key": "1234123412341234asdfasdfasdfasdfasdf1234123412341234123412341234asdfasdfasdfasdfasdf123412341234123412341234asdfasdfasdfasdfasdf",
  "api_key_id": 1,
  "fqdn": "https://api-example.xdr.us.paloaltonetworks.com/",
  "security_level": "Standard"
}
```

## Technical Details

### Actions

#### Isolate Endpoint

This action is used to isolate an endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|endpoint|string|None|True|Endpoint to take isolation action on. This can be IPv4, hostnames, and endpoint IDs|None|0123456abcdef12345abcde12345abcd|
|isolation_state|string|Isolate|True|True to isolate host, false to unisolate a host|['Isolate', 'Unisolate']|Unisolate|
|whitelist|[]string|[]|False|This list contains a set of devices that should not be blocked. This can include IPs, hostnames, and device IDs|None|["198.51.100.100", "hostname123", "225494730938493804"]|

Example input:

```
{
  "endpoint": "0123456abcdef12345abcde12345abcd",
  "isolation_state": "Unisolate",
  "whitelist": [
    "198.51.100.100",
    "hostname123",
    "225494730938493804"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|isolation_result|True|The result of the isolation request|

Example output:

```
```

#### Get Endpoint Details

This action is used to get information about an endpoint.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|endpoint|string|None|True|The endpoint to get information about. Endpoint will accept IPv4, hostnames, and endpoint IDs|None|0123456abcdef12345abcde12345abcd|

Example input:

```
{
  "endpoint": "0123456abcdef12345abcde12345abcd"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|endpoints|[]endpoint|True|Any endpoints that match the given endpoint information|
|total_count|integer|True|Number of results found (max 100)|

Example output:

```
```

### Triggers

#### Get Incidents

This trigger is used to get Incidents.

##### Input

_This trigger does not contain any inputs._

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|object|False|Incident|

Example output:

```
```

### Custom Output Types

#### incident

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert Count|integer|False|Alert Count|
|Assigned User Mail|string|False|Assigned User Mail|
|Assigned User Pretty Name|string|False|Assigned User Pretty Name|
|Creation Time|integer|False|Creation Time|
|Description|string|False|Description|
|Detection Time|integer|False|Detection Time|
|High Severity Alert Count|integer|False|High Severity Alert Count|
|Host Count|integer|False|Host Count|
|Hosts|[]string|False|Hosts|
|Incident ID|string|False|Incident ID|
|Incident Name|string|False|Incident Name|
|Incident Sources|[]string|False|Incident Sources|
|Low Severity Alert Count|integer|False|Low Severity Alert Count|
|Manual Description|string|False|Manual Description|
|Manual Score|integer|False|Manual Score|
|Manual Severity|string|False|Manual Severity|
|Med Severity Alert Count|integer|False|Med Severity Alert Count|
|Modification Time|integer|False|Modification Time|
|Notes|string|False|Notes|
|Resolve Comment|string|False|Resolve Comment|
|Rule Based Score|integer|False|Rule Based Score|
|Severity|string|False|Severity|
|Starred|boolean|False|Starred|
|Status|string|False|Status|
|User Count|integer|False|User Count|
|Users|[]string|False|Users|
|XDR URL|string|False|XDR URL|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Cortex XDR](LINK TO PRODUCT/VENDOR WEBSITE)
