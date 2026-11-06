# Description

Find, isolate and restore endpoints managed by Bitdefender GravityZone

# Key Features

* Find exactly one managed endpoint by hostname or FQDN, refusing ambiguous matches
* List endpoints using GravityZone filters
* Get the details of a managed endpoint
* Isolate an endpoint from the network and restore it from isolation

# Requirements

* A GravityZone API key with the Network API and the Incidents API enabled
* The GravityZone Control Center URL, for example https://cloud.gravityzone.bitdefender.com

# Supported Product Versions

* GravityZone Public API v1.0

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|A GravityZone API key with the Network API and the Incidents API enabled|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|url|string|None|True|The GravityZone Control Center URL. A trailing /api is accepted and removed|None|https://cloud.gravityzone.bitdefender.com|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "url": "https://cloud.gravityzone.bitdefender.com"
}
```

## Technical Details

### Actions


#### Find Endpoint

This action is used to find exactly one managed endpoint by hostname or FQDN, using an exact, case-insensitive match. 
When no endpoint or more than one endpoint matches, it returns found false instead of guessing

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hostname|string|None|True|The short hostname or the FQDN of the endpoint. An FQDN is matched against the endpoint FQDN first. If none matches, its first label is matched against the endpoint name, and a single endpoint with a different FQDN is not a match|None|workstation-01.example.com|None|None|
  
Example input:

```
{
  "hostname": "workstation-01.example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpoint|endpoint_summary|True|The matching endpoint when exactly one endpoint matches, otherwise an empty object|{'id': '5a4f2c3b6e9d1a0012345678', 'name': 'WORKSTATION-01', 'fqdn': 'workstation-01.example.com', 'ip': '10.0.0.15', 'macs': ['00:1a:2b:3c:4d:5e'], 'is_managed': True, 'is_isolated': False}|
|found|boolean|True|True only when exactly one managed endpoint matches the hostname|True|
|match_count|integer|True|The number of managed endpoints that match the hostname exactly|1|
  
Example output:

```
{
  "endpoint": {
    "fqdn": "workstation-01.example.com",
    "id": "5a4f2c3b6e9d1a0012345678",
    "ip": "10.0.0.15",
    "is_isolated": false,
    "is_managed": true,
    "macs": [
      "00:1a:2b:3c:4d:5e"
    ],
    "name": "WORKSTATION-01"
  },
  "found": true,
  "match_count": 1
}
```

#### Get Endpoints List

This action is used to get a page of endpoints from GravityZone, optionally narrowed with GravityZone filters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filters|object|None|False|A GravityZone filters object, passed to the API unchanged. For example details.name matches names that start with the value, and depth.allItemsRecursively includes endpoints in subgroups|None|{'details': {'name': 'WORKSTATION'}, 'depth': {'allItemsRecursively': True}}|None|None|
|is_managed|boolean|None|False|Set to true to return only managed endpoints, or to false to return only unmanaged endpoints. Leave empty to return both|None|True|None|None|
|page|integer|1|False|The page number to return, starting at 1|None|1|None|None|
|parent_id|string|None|False|The ID of the target company or group. If omitted, the endpoints under Computers and Groups are returned|None|5a4f2c3b6e9d1a0012345678|None|None|
|per_page|integer|30|False|The number of endpoints per page, from 1 to 100|None|30|None|None|
  
Example input:

```
{
  "filters": {
    "depth": {
      "allItemsRecursively": true
    },
    "details": {
      "name": "WORKSTATION"
    }
  },
  "is_managed": true,
  "page": 1,
  "parent_id": "5a4f2c3b6e9d1a0012345678",
  "per_page": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpoints|[]endpoint_item|True|The endpoints on the requested page|[{"id": "5a4f2c3b6e9d1a0012345678", "name": "WORKSTATION-01", "label": "", "fqdn": "workstation-01.example.com", "group_id": "5a4f2c3b6e9d1a0012345679", "is_managed": True, "machine_type": 1, "operating_system_version": "Windows 11 Pro", "ip": "10.0.0.15", "macs": ["00:1a:2b:3c:4d:5e"], "managed_with_best": True, "is_isolated": False}]|
|page|integer|True|The page number returned|1|
|pages_count|integer|False|The total number of pages|1|
|per_page|integer|True|The number of endpoints per page|30|
|total|integer|True|The total number of endpoints that match the request|1|
  
Example output:

```
{
  "endpoints": [
    {
      "fqdn": "workstation-01.example.com",
      "group_id": "5a4f2c3b6e9d1a0012345679",
      "id": "5a4f2c3b6e9d1a0012345678",
      "ip": "10.0.0.15",
      "is_isolated": false,
      "is_managed": true,
      "label": "",
      "machine_type": 1,
      "macs": [
        "00:1a:2b:3c:4d:5e"
      ],
      "managed_with_best": true,
      "name": "WORKSTATION-01",
      "operating_system_version": "Windows 11 Pro"
    }
  ],
  "page": 1,
  "pages_count": 1,
  "per_page": 30,
  "total": 1
}
```

#### Get Managed Endpoint Details

This action is used to get the details of a managed endpoint, including its isolation state, agent, policy, modules and
 risk score

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint_id|string|None|True|The ID of the managed endpoint|None|5a4f2c3b6e9d1a0012345678|None|None|
|include_last_logged_users|boolean|False|False|Whether to include the users logged in on the endpoint at the time of the request|None|False|None|None|
|include_scan_logs|boolean|False|False|Whether to include the last successful scan in the response|None|False|None|None|
  
Example input:

```
{
  "endpoint_id": "5a4f2c3b6e9d1a0012345678",
  "include_last_logged_users": false,
  "include_scan_logs": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpoint_details|object|True|The endpoint details as returned by GravityZone|{'id': '5a4f2c3b6e9d1a0012345678', 'name': 'WORKSTATION-01', 'isIsolated': False, 'state': 1}|
  
Example output:

```
{
  "endpoint_details": {
    "id": "5a4f2c3b6e9d1a0012345678",
    "isIsolated": false,
    "name": "WORKSTATION-01",
    "state": 1
  }
}
```

#### Isolate Endpoint

This action is used to create a GravityZone task that isolates a managed endpoint from the network. The step fails 
unless GravityZone confirms that the task was created

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint_id|string|None|True|The ID of the managed endpoint to isolate|None|5a4f2c3b6e9d1a0012345678|None|None|
  
Example input:

```
{
  "endpoint_id": "5a4f2c3b6e9d1a0012345678"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|True when GravityZone created the isolation task|True|
  
Example output:

```
{
  "success": true
}
```

#### Restore Endpoint

This action is used to create a GravityZone task that restores a managed endpoint from network isolation. The step 
fails unless GravityZone confirms that the task was created

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint_id|string|None|True|The ID of the managed endpoint to restore from isolation|None|5a4f2c3b6e9d1a0012345678|None|None|
  
Example input:

```
{
  "endpoint_id": "5a4f2c3b6e9d1a0012345678"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|True when GravityZone created the restore task|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**endpoint_item**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|FQDN|string|None|False|The fully qualified domain name of the endpoint|workstation-01.example.com|
|Group ID|string|None|False|The ID of the group the endpoint belongs to|5a4f2c3b6e9d1a0012345679|
|Endpoint ID|string|None|True|The ID of the endpoint|5a4f2c3b6e9d1a0012345678|
|IP Address|string|None|False|The local IP address of the endpoint|10.0.0.15|
|Is Isolated|boolean|None|False|Whether the endpoint is currently isolated from the network|False|
|Is Managed|boolean|None|False|Whether the endpoint is managed by GravityZone|True|
|Label|string|None|False|The label set on the endpoint|Finance laptop|
|Machine Type|integer|None|False|The type of machine: 1 for a computer, 2 for a virtual machine, 3 for an EC2 instance, 0 for other|1|
|MAC Addresses|[]string|None|False|The MAC addresses of the endpoint|["00:1a:2b:3c:4d:5e"]|
|Managed with BEST|boolean|None|False|Whether the Bitdefender Endpoint Security Tools agent is installed on the endpoint|True|
|Name|string|None|True|The name of the endpoint|WORKSTATION-01|
|Operating System Version|string|None|False|The operating system version of the endpoint|Windows 11 Pro|
  
**endpoint_summary**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|FQDN|string|None|False|The fully qualified domain name of the endpoint|workstation-01.example.com|
|Endpoint ID|string|None|False|The ID of the endpoint|5a4f2c3b6e9d1a0012345678|
|IP Address|string|None|False|The local IP address of the endpoint|10.0.0.15|
|Is Isolated|boolean|None|False|Whether the endpoint is currently isolated from the network|False|
|Is Managed|boolean|None|False|Whether the endpoint is managed by GravityZone|True|
|MAC Addresses|[]string|None|False|The MAC addresses of the endpoint|["00:1a:2b:3c:4d:5e"]|
|Name|string|None|False|The name of the endpoint|WORKSTATION-01|


## Troubleshooting

* The connection test uses the Network API only. Isolate Endpoint and Restore Endpoint also need the Incidents API: without it they fail with GravityZone error -32001, API Key is not allowed to access the selected API
* Use the Control Center URL, for example https://cloud.gravityzone.bitdefender.com. A trailing /api is accepted and removed
* Find Endpoint searches managed endpoints only. The part of the hostname before the first dot must be at least 3 characters long, because the GravityZone name filter needs 3 characters
* Find Endpoint returns `found` false with `match_count` 0 when no managed endpoint has that exact name or FQDN, and `found` false with a `match_count` above 1 when the hostname is ambiguous. Pass the FQDN to tell apart endpoints that share a short name
* When an FQDN matches no endpoint FQDN, Find Endpoint compares its first label with the endpoint names. A single endpoint with that name counts only if GravityZone has no FQDN for it: an endpoint whose FQDN is in another domain is not a match
* Isolate Endpoint and Restore Endpoint fail unless GravityZone confirms that the task was created. The task then runs on the endpoint asynchronously
* GravityZone limits the number of requests per API key. When it returns HTTP 429, the plugin waits for the Retry-After period and retries up to 3 times, as long as Retry-After is 60 seconds or less

# Version History

* 1.0.0 - Initial plugin

# Links

* [Bitdefender GravityZone](https://www.bitdefender.com/en-us/business)

## References

* [GravityZone Public API](https://www.bitdefender.com/business/support/en/77212-125277-public-api.html)