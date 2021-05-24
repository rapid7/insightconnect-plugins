# Description

Stop modern attacks with the industry’s first extended detection and response platform that spans your endpoint, network and cloud data.

# Key Features

* Get Endpoint Information
* Isolate or Unisolate endpoints

# Requirements

* A Palo Alto Cortex XDR API key
* A Palo Alto Cortex XDR API key ID
* The fully-qualified domain name (FQDN) to your Palo Alto Cortex XDR API instance

The required connection information is available in the Cortex XDR web dashboard. Click the gear icon, click settings, and then click on API Keys on the left. 

The API Key will be generated when you create a new API key. 

The API Key ID is the value from the ID column

To get the FQDN, right click on your API key and pick generate examples. The generated example is a URL that should look similar to "https://api-yourorg.xdr.us.paloaltonetworks.com/api_keys/validate/". 
In our example the FQDN is "https://api-yourorg.xdr.us.paloaltonetworks.com" and should be copied.


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

#### Block File

This action is used to add a file to the block list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|File blocked by InsightConnect|True|String that represents additional information regarding the action|None|File blocked by InsightConnect|
|file_hash|string|None|True|A SHA256 file hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|incident_id|string|None|False|If this is related to an incident, the ID should be entered here|None|5|

Example input:

```
{
  "comment": "File blocked by InsightConnect",
  "file_hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "incident_id": "5"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was the operation successful|

Example output:

```
{
  "success": true
}
```

#### Allow File

This action is used to add a file to the allow list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|File allowed by InsightConnect|True|String that represents additional information regarding the action|None|File allowed by InsightConnect|
|file_hash|string|None|True|A SHA256 file hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
|incident_id|string|None|False|If this is related to an incident, the ID should be entered here|None|5|

Example input:

```
{
  "comment": "File allowed by InsightConnect",
  "file_hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
  "incident_id": "5"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was the operation successful|

Example output:

```
{
  "success": true
}
```

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
{
  "result": {
    "action_id": 14,
    "endpoints_count": 1
  }
}
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
{
  "endpoints": [
    {
      "endpoint_id": "0123456abcdef12345abcde12345abcd",
      "endpoint_name": "EXAMPLEHOST",
      "endpoint_type": "AGENT_TYPE_WORKSTATION",
      "endpoint_status": "CONNECTED",
      "os_type": "AGENT_OS_WINDOWS",
      "ip": [
        "192.168.50.1"
      ],
      "users": [
        "ExampleUser"
      ],
      "domain": "WORKGROUP",
      "first_seen": 1621361378523,
      "last_seen": 1621449040261,
      "content_version": "181-58715",
      "installation_package": "Example-Install-Package",
      "install_date": 1621361378541,
      "endpoint_version": "7.3.2.26319",
      "is_isolated": "AGENT_UNISOLATED",
      "group_name": [],
      "operational_status": "PROTECTED",
      "operational_status_description": "[]",
      "scan_status": "SCAN_STATUS_IN_PROGRESS"
    }
  ],
  "total_count": 1
}
```

### Triggers

#### Get Incidents

This trigger is used to get Incidents.

##### Input

_This trigger does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|object|False|Incident|

Example output:

```
{
   "incident":{
      "incident_id":"1",
      "incident_name":null,
      "creation_time":1621448873194,
      "modification_time":1621448873194,
      "detection_time":null,
      "status":"new",
      "severity":"high",
      "description":"'Behavioral Threat' generated by XDR Agent detected on host msedgewin10 involving user ieuser",
      "assigned_user_mail":null,
      "assigned_user_pretty_name":null,
      "alert_count":1,
      "low_severity_alert_count":0,
      "med_severity_alert_count":0,
      "high_severity_alert_count":1,
      "user_count":1,
      "host_count":1,
      "notes":null,
      "resolve_comment":null,
      "manual_severity":null,
      "manual_description":null,
      "xdr_url":"https://example.xdr.us.paloaltonetworks.com/incident-view/1",
      "starred":false,
      "hosts":[
         "examplehost:0123456abcdef12345abcde12345abcd"
      ],
      "users":[
         "exampleuser"
      ],
      "incident_sources":[
         "XDR Agent"
      ],
      "rule_based_score":null,
      "manual_score":null
   }
}
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

* Isolate Endpoint fails with 500 error - This will happen if an isolation action (Isolate or Unisolate) is in progress on the selected endpoint. Wait a few minutes and try again. 

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Cortex XDR](LINK TO PRODUCT/VENDOR WEBSITE)
