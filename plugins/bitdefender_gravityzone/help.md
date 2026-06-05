# Description

Interact with Bitdefender GravityZone to manage endpoints, including listing managed devices and isolating compromised hosts

# Key Features

* List endpoints managed by Bitdefender GravityZone
* Isolate compromised endpoints from the network

# Requirements

* Bitdefender GravityZone API key with appropriate permissions
* Access to the GravityZone Control Center

# Supported Product Versions

* GravityZone Cloud API v1.0

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|GravityZone API key with required service permissions|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|url|string|None|True|The base GravityZone Control Center URL|None|https://cloud.gravityzone.bitdefender.com|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "url": "https://cloud.gravityzone.bitdefender.com"
}
```

## Technical Details

### Actions


#### Get Endpoints List

This action is used to returns a paginated list of endpoints managed by Bitdefender GravityZone

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|is_managed|boolean|None|False|Filter by management state. True returns only managed endpoints, False returns unmanaged|None|True|None|None|
|name_filter|string|None|False|Partial match filter for endpoint names (minimum 3 characters)|None|workstation*|None|None|
|page|integer|1|False|The page number to return|None|1|None|None|
|parent_id|string|None|False|The ID of the target company or group. If omitted, returns endpoints associated with the API key|None|5a4f2c3b6e9d1a0012345678|None|None|
|per_page|integer|30|False|Number of items per page (1-100)|None|30|None|None|
  
Example input:

```
{
  "is_managed": true,
  "name_filter": "workstation*",
  "page": 1,
  "parent_id": "5a4f2c3b6e9d1a0012345678",
  "per_page": 30
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpoints|[]endpoint_item|True|List of endpoint objects matching the filter criteria|[{"id": "5a4f2c3b6e9d1a0012345678", "name": "WORKSTATION-001"}]|
|page|integer|True|The current page number returned|1|
|pages_count|integer|False|Total number of available pages|5|
|per_page|integer|True|The number of items per page|30|
|total|integer|True|Total number of endpoints matching the criteria|25|
  
Example output:

```
{
  "endpoints": [
    {
      "id": "5a4f2c3b6e9d1a0012345678",
      "name": "WORKSTATION-001"
    }
  ],
  "page": 1,
  "pages_count": 5,
  "per_page": 30,
  "total": 25
}
```

#### Isolate Endpoint

This action is used to isolates a managed endpoint from the network to contain a potential threat

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpoint_id|string|None|True|The unique 24-character hex ID of the endpoint to isolate|None|5a4f2c3b6e9d1a0012345678|None|None|
  
Example input:

```
{
  "endpoint_id": "5a4f2c3b6e9d1a0012345678"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the isolation task was successfully created|True|
  
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
|FQDN|string|None|False|Fully qualified domain name of the endpoint|None|
|Group ID|string|None|False|The ID of the group the endpoint belongs to|None|
|Endpoint ID|string|None|True|The unique identifier of the endpoint|None|
|IP Address|string|None|False|Primary IP address of the endpoint|None|
|Is Managed|boolean|None|False|Whether the endpoint has an active management agent|None|
|Label|string|None|False|Custom label assigned to the endpoint|None|
|Machine Type|integer|None|False|Type of machine: 1=Computer, 2=Virtual Machine, 3=EC2 Instance, 0=Other|None|
|MAC Addresses|[]string|None|False|List of MAC addresses for the endpoint|None|
|Managed With BEST|boolean|None|False|Whether Bitdefender Endpoint Security Tools is active|None|
|Name|string|None|True|The hostname of the endpoint|None|
|Operating System Version|string|None|False|The OS name and version|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.0 - Initial plugin with Get Endpoints List and Isolate Endpoint actions

# Links

* [Bitdefender GravityZone](https://www.bitdefender.com/business/products/gravityzone-business-security.html)

## References

* [GravityZone API Documentation](https://www.bitdefender.com/business/support/en/77209-128490-public-api.html)