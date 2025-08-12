# Description

InsightVM is a powerful vulnerability management tool which finds, prioritizes, and remediates vulnerabilities. This plugin uses an orchestrator to get top remediations, scan results and start scans

# Key Features

* Get top remediations
* Start scans
* Get scan results

# Requirements

* Username and password for a user with the necessary permissions

# Supported Product Versions

* Rapid7 InsightVM API v3 2022-05-25

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username and password|None|{'username': 'user1', 'password': 'mypassword'}|None|None|
|ssl_verify|boolean|True|True|Specify whether to verify SSL or not|None|True|None|None|
|url|string|None|True|URL to your InsightVM console, without trailing slashes|None|https://insightvm.example.com:3780|None|None|

Example input:

```
{
  "credentials": "{'username': 'user1', 'password': 'mypassword'}",
  "ssl_verify": true,
  "url": "https://insightvm.example.com:3780"
}
```

## Technical Details

### Actions


#### Add Scan Engine Pool Engine

This action is used to add a scan engine to a scan engine pool (AWS pre-authorized engine AMI engines cannot be pooled)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|engine_id|integer|None|True|Scan engine ID|None|1234567|None|None|
|pool_id|integer|None|True|Scan engine pool ID|None|1234|None|None|
  
Example input:

```
{
  "engine_id": 1234567,
  "pool_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Add User Asset Group Access

This action is used to grant an user account access to an asset group by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_group_id|integer|None|True|The identifier of the asset group|None|5678|None|None|
|user_id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "asset_group_id": 5678,
  "user_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Add User Site Access

This action is used to grant an user account access to a site by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|site_id|integer|None|True|The identifier of the site|None|4567|None|None|
|user_id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "site_id": 4567,
  "user_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Asset Search

This action is used to search for assets using filtered asset search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|searchCriteria|object|None|True|Tag search criteria - options documentation: https://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|{'risk-score': 'asc', 'criticality-tag': 'desc'}|None|None|
|size|number|0|False|The number of records to retrieve. If blank or '0' all assets that match the search will be returned|None|100|None|None|
|sort_criteria|object|None|False|JSON object for sorting by criteria. Multiple criteria can be specified with an order of 'asc' (ascending) or 'desc' (descending)|None|{'risk-score': 'asc', 'criticality-tag': 'desc'}|None|None|
  
Example input:

```
{
  "searchCriteria": "{'risk-score': 'asc', 'criticality-tag': 'desc'}",
  "size": 0,
  "sort_criteria": "{'risk-score': 'asc', 'criticality-tag': 'desc'}"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assets|[]asset|True|List of asset details returned by the search|[]|
  
Example output:

```
{
  "assets": []
}
```

#### Get Asset Vulnerability Solutions

This action is used to return the highest-superceding rollup solutions for a list of vulnerabilities on an asset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_id|integer|None|True|The identifier of the asset|None|423|None|None|
|vulnerability_ids|[]string|None|True|A list of identifiers of the vulnerabilities|None|["flash_player-cve-2017-11305"]|None|None|
  
Example input:

```
{
  "asset_id": 423,
  "vulnerability_ids": [
    "flash_player-cve-2017-11305"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerabilities_solution|[]vulnerability_solution|True|Highest-superceding rollup solutions for a vulnerabilities on an asset|[]|
  
Example output:

```
{
  "vulnerabilities_solution": []
}
```

#### Create Asset Group

This action is used to create an asset group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|True|Asset group description|None|example description|None|None|
|name|string|None|True|Asset group name|None|example name|None|None|
|searchCriteria|object|None|False|Asset group search criteria - options documentation: https://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|{'risk-score': 'asc', 'criticality-tag': 'desc'}|None|None|
|type|string|None|True|Asset group type|["dynamic", "static"]|dynamic|None|None|
  
Example input:

```
{
  "description": "example description",
  "name": "example name",
  "searchCriteria": "{'risk-score': 'asc', 'criticality-tag': 'desc'}",
  "type": "dynamic"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|ID of the created tag|20|
  
Example output:

```
{
  "id": 20
}
```

#### Create Vulnerability Exception Submission

This action is used to create a vulnerability exception submission

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|Exception created with InsightConnect|True|Comment to include in the vulnerability exception submission|None|example comment|None|None|
|expiration|date|None|False|The date the vulnerability exception expires|None|2021-12-30 00:00:00|None|None|
|key|string|None|False|The key to identify a specific instance if the type is Instance|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|port|integer|None|False|The port the vulnerability appears on if the type is Instance|None|40000|None|None|
|reason|string|None|True|Reason for the exception|["False Positive", "Compensating Control", "Acceptable Use", "Acceptable Risk", "Other"]|False Positive|None|None|
|scope|integer|None|False|The ID of the scope the vulnerability exception applies to. May be empty if type is Global|None|1234|None|None|
|type|string|None|True|The type of vulnerability exception to create|["Global", "Site", "Asset", "Asset Group", "Instance"]|Global|None|None|
|vulnerability|string|None|True|The vulnerability this exception applies to|None|vulnerability|None|None|
  
Example input:

```
{
  "comment": "Exception created with InsightConnect",
  "expiration": "2021-12-30 00:00:00",
  "key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "port": 40000,
  "reason": "False Positive",
  "scope": 1234,
  "type": "Global",
  "vulnerability": "vulnerability"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|The vulnerability exception that was created|35|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 35,
  "links": []
}
```

#### Create Scan Engine

This action is used to create a new scan engine with console engine connectivity

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|Scan engine address (IP/hostname)|None|10.4.36.120|None|None|
|name|string|None|True|Scan engine name|None|example name|None|None|
|port|integer|40814|True|Scan engine connectivity port|None|40814|None|None|
|sites|[]integer|[]|False|List of site IDs with which to associate the engine|None|[1234, 5678]|None|None|
  
Example input:

```
{
  "address": "10.4.36.120",
  "name": "example name",
  "port": 40814,
  "sites": []
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|Scan engine ID|12|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 12,
  "links": []
}
```

#### Create Scan Engine Pool

This action is used to create a new scan engine pool

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|engines|[]integer|None|False|List of scan engine IDs to associate with the scan engine pool|None|[1234, 5678]|None|None|
|name|string|None|True|Scan engine pool name|None|example name|None|None|
  
Example input:

```
{
  "engines": [
    1234,
    5678
  ],
  "name": "example name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|Scan engine pool ID|13|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 13,
  "links": []
}
```

#### Create Site

This action is used to create a new site

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|The site's description|None|example description|None|None|
|engine_id|integer|None|False|The identifier of a scan engine. Default scan engine is selected when not specified|None|1234|None|None|
|excluded_addresses|[]string|[]|False|List of addresses to exclude in scan scope|None|["1234-abcd", "4567-def"]|None|None|
|excluded_asset_groups|[]integer|[]|False|Assets associated with these asset group IDs will be excluded in the site|None|[1234, 5768]|None|None|
|importance|string|normal|False|The site importance|["very_low", "low", "normal", "high", "very_high"]|low|None|None|
|included_addresses|[]string|[]|False|List of addresses to include in scan scope|None|["1234-abcd", "4567-def"]|None|None|
|included_asset_groups|[]integer|[]|False|Assets associated with these asset group IDs will be included in the site|None|[1234, 5768]|None|None|
|name|string|None|True|The site name. Name must be unique|None|example name|None|None|
|scan_template_id|string|None|False|The identifier of a scan template|None|12345-abcd|None|None|
  
Example input:

```
{
  "description": "example description",
  "engine_id": 1234,
  "excluded_addresses": [],
  "excluded_asset_groups": [],
  "importance": "normal",
  "included_addresses": [],
  "included_asset_groups": [],
  "name": "example name",
  "scan_template_id": "12345-abcd"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|The identifier of the created site|15|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 15,
  "links": []
}
```

#### Create Tag

This action is used to create a new tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|color|string|default|False|Tag color (only available for custom tags)|["default", "blue", "green", "orange", "purple", "red"]|default|None|None|
|name|string|None|True|Tag name|None|example name|None|None|
|searchCriteria|object|None|False|Tag search Criteria - options documentation https://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|{'risk-score': 'asc', 'criticality-tag': 'desc'}|None|None|
|type|string|None|True|Tag type|["owner", "location", "custom"]|owner|None|None|
  
Example input:

```
{
  "color": "default",
  "name": "example name",
  "searchCriteria": "{'risk-score': 'asc', 'criticality-tag': 'desc'}",
  "type": "owner"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|ID of the created tag|665|
  
Example output:

```
{
  "id": 665
}
```

#### Create User

This action is used to create a new user account (limited to external authentication sources)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|access_all_asset_groups|boolean|False|True|Whether to grant the user access to all asset groups|None|False|None|None|
|access_all_sites|boolean|False|True|Whether to grant the user access to all sites|None|False|None|None|
|authentication_id|integer|None|False|The identifier of the authentication source to use to authenticate the user. The source with the specified identifier must be of the type specified by Authentication Type. If Authentication ID is omitted, then one source of the specified Authentication Type is selected|None|1234|None|None|
|authentication_type|string|ldap|True|The type of the authentication source to use to authenticate the user|["kerberos", "ldap", "saml"]|ldap|None|None|
|email|string|None|True|The email address of the user|None|user@example.com|None|None|
|enabled|boolean|True|True|Whether the user account is enabled|None|True|None|None|
|login|string|None|True|The login name of the user|None|jdoe24|None|None|
|name|string|None|True|The full name of the user|None|John Doe|None|None|
|role_id|string|None|True|The identifier of the role to which the user should be assigned|None|global-admin|None|None|
  
Example input:

```
{
  "access_all_asset_groups": false,
  "access_all_sites": false,
  "authentication_id": 1234,
  "authentication_type": "ldap",
  "email": "user@example.com",
  "enabled": true,
  "login": "jdoe24",
  "name": "John Doe",
  "role_id": "global-admin"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|The identifier of the created user account|83|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 83,
  "links": []
}
```

#### Delete an Asset

This action is used to delete an Asset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Asset ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was the operation successful|False|
  
Example output:

```
{
  "success": false
}
```

#### Delete Asset Group

This action is used to delete an existing asset group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Asset group ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Delete Vulnerability Exception

This action is used to delete an existing vulnerability exception

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|exception_id|integer|None|True|Vulnerability exception ID to delete|None|1234|None|None|
  
Example input:

```
{
  "exception_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Delete Scan Engine

This action is used to delete an existing scan engine from the security console

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Scan engine identifier|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Delete Scan Engine Pool

This action is used to delete an existing scan engine pool from the security console

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Scan engine pool identifier|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Delete Site

This action is used to delete an existing site

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Site ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Delete Tag

This action is used to delete an existing tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Tag ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Delete User

This action is used to delete an user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Disable User

This action is used to disable an user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Download Report

This action is used to returns the contents of a generated report

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Identifier of the report to download|None|1234|None|None|
|instance|string|None|True|The identifier of the report instance, 'latest' or ID|None|latest|None|None|
  
Example input:

```
{
  "id": 1234,
  "instance": "latest"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|report|bytes|False|Base64 encoded report|ZXhhbXBsZQ==|
  
Example output:

```
{
  "report": "ZXhhbXBsZQ=="
}
```

#### Enable User

This action is used to enable an user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Generate AdHoc SQL Report

This action is used to create, generate, download, and cleanup a SQL report based on the provided query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filters|string|{}|False|Filters in JSON format to be applied to the contents of the report; review InsightVM API documentation for filter options|None|{filters}|None|None|
|query|string|None|True|Reporting Data Model SQL query|None|select * from dim_asset|None|None|
|scope|string|none|True|Scope context for generated report; if set, remediations will be scoped by each in scope ID, e.g Site ID, Tag ID, Asset Group ID; scan scope only supports single scan ID as input|["none", "assets", "assetGroups", "sites", "tags", "scan"]|none|None|None|
|scope_ids|[]integer|[]|False|Scope IDs for which tickets should be generated, by default all are included|None|[1234, 5678]|None|None|
  
Example input:

```
{
  "filters": {},
  "query": "select * from dim_asset",
  "scope": "none",
  "scope_ids": []
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|report|file|True|Base64 encoded file making up the report|{'filename': '<name>', 'content': 'UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=='}|
  
Example output:

```
{
  "report": {
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
    "filename": "<name>"
  }
}
```

#### Generate Shared Secret

This action is used to generate a shared secret to pair a scan engine to a security console

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|time_to_live|integer|3600|True|Time to live in seconds for the shared secret|None|3600|None|None|
  
Example input:

```
{
  "time_to_live": 3600
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|shared_secret|string|True|Scan engine pairing shared secret|99DB-B9F0-CD8B-5997-06BF-607B-BA21-0A81|
  
Example output:

```
{
  "shared_secret": "99DB-B9F0-CD8B-5997-06BF-607B-BA21-0A81"
}
```

#### Get Asset

This action is used to gets an asset by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_id|integer|None|True|Identifier of asset|None|1234|None|None|
  
Example input:

```
{
  "asset_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset|asset|True|Asset details|{}|
  
Example output:

```
{
  "asset": {}
}
```

#### Get Asset Group

This action is used to get an asset group by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Asset group ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset_group|asset_group|True|Asset group|[]|
  
Example output:

```
{
  "asset_group": []
}
```

#### Get Asset Group Assets

This action is used to get asset group assets

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Asset group ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
|resources|[]integer|False|The identifiers of the associated resources|[]|
  
Example output:

```
{
  "links": [],
  "resources": []
}
```

#### Get Asset Groups

This action is used to get a list of asset groups

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string||False|Asset group name regular expression by which to filter|None|example name|None|None|
  
Example input:

```
{
  "name": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset_groups|[]asset_group|True|List of asset groups|[]|
  
Example output:

```
{
  "asset_groups": []
}
```

#### Get Asset Software

This action is used to get software found on an asset. Can only be used if the asset has first been scanned

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_id|integer|None|True|ID of the asset for which to find software|None|234|None|None|
  
Example input:

```
{
  "asset_id": 234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|software|[]software|False|Software found on the asset|[]|
  
Example output:

```
{
  "software": []
}
```

#### Get Asset Tags

This action is used to get a listing of all tags for an asset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_id|integer|None|True|Identifier of asset|None|1234|None|None|
  
Example input:

```
{
  "asset_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|tags|[]tag|True|List of tags|[]|
  
Example output:

```
{
  "tags": []
}
```

#### Get Asset Vulnerabilities

This action is used to get vulnerabilities found on an asset. Can only be used if the asset has first been scanned

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_id|integer|None|True|ID of the asset for which to find vulnerabilities|None|234|None|None|
|get_risk_score|boolean|None|False|Return risk score along with other vulnerability data|None|True|None|None|
  
Example input:

```
{
  "asset_id": 234,
  "get_risk_score": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerabilities|[]asset_vulnerability|False|Vulnerabilities found on the asset|[]|
  
Example output:

```
{
  "vulnerabilities": []
}
```

#### Get Authentication Source

This action is used to get the details for an authentication source

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Authentication source ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|authentication_source|authentication_source|True|User authentication source|{}|
  
Example output:

```
{
  "authentication_source": {}
}
```

#### Get Authentication Sources

This action is used to list authentication sources available for InsightVM users

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|False|Authentication source name by which to filter, accepts regular expression patterns|None|example name|None|None|
|type|string||False|Authentication source type by which to filter|["", "admin", "kerberos", "ldap", "normal", "saml"]|admin|None|None|
  
Example input:

```
{
  "name": "example name",
  "type": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|authentication_sources|[]authentication_source|True|List of authentication sources|[]|
  
Example output:

```
{
  "authentication_sources": []
}
```

#### Get Expiring Vulnerability Exceptions

This action is used to return a list of expiring vulnerability exceptions

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expires_in_less_than|integer|7|True|Number of days left until the exception expires|None|7|None|None|
  
Example input:

```
{
  "expires_in_less_than": 7
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|exceptions|[]vulnerability_exception|False|Exceptions about to expire|[]|
  
Example output:

```
{
  "exceptions": []
}
```

#### Get Role

This action is used to get role details by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Role ID|None|global-admin|None|None|
  
Example input:

```
{
  "id": "global-admin"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|role|role|True|Role details|{}|
  
Example output:

```
{
  "role": {}
}
```

#### Get Roles

This action is used to list role details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|False|Role name by which to filter, accepts regular expression patterns|None|example name|None|None|
  
Example input:

```
{
  "name": "example name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|roles|[]role|True|List of roles|[]|
  
Example output:

```
{
  "roles": []
}
```

#### Get Scan

This action is used to get the status of a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_id|string|None|True|ID of the scan to obtain|None|11234abc-65c8-4628-adf4-e27f36ea0e2b|None|None|
  
Example input:

```
{
  "scan_id": "11234abc-65c8-4628-adf4-e27f36ea0e2b"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assets|integer|False|Number of assets within the scan|0|
|duration|string|False|Duration of the scan in ISO8601 format|2018-04-23 04:21:05.500000+00:00|
|endTime|string|False|End time of the scan in ISO8601 format|2018-04-23 04:21:05.500000+00:00|
|engineName|string|False|Name of the engine used for the scan|Local scan engine|
|id|integer|False|ID of the scan|188934|
|links|[]link|False|Hypermedia links to corresponding or related resources|[{"href": "https://insightvm:3780/api/3/scans/188934", "rel": "self"}]|
|scanName|string|False|User-driven scan name for the scan|API Scan - 2018-04-23T04:21:05Z|
|scanType|string|False|Scan type (manual, automated, scheduled)|Manual|
|startTime|string|False|Start time of the scan in ISO8601 format|2018-04-23 04:21:05.500000+00:00|
|status|string|False|Scan status (aborted, unknown, running, finished, stopped, error, paused, dispatched or integrating)|running|
|vulnerabilities|vulnerabilities_count|False|Counts of vulnerabilities found within the scan|{'critical': 0, 'moderate': 0, 'severe': 0, 'total': 0}|
  
Example output:

```
{
  "assets": 0,
  "duration": "2018-04-23 04:21:05.500000+00:00",
  "endTime": "2018-04-23 04:21:05.500000+00:00",
  "engineName": "Local scan engine",
  "id": 188934,
  "links": [
    {
      "href": "https://insightvm:3780/api/3/scans/188934",
      "rel": "self"
    }
  ],
  "scanName": "API Scan - 2018-04-23T04:21:05Z",
  "scanType": "Manual",
  "startTime": "2018-04-23 04:21:05.500000+00:00",
  "status": "running",
  "vulnerabilities": {
    "critical": 0,
    "moderate": 0,
    "severe": 0,
    "total": 0
  }
}
```

#### Get Scan Assets

This action is used to gets assets for a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_id|integer|None|True|ID of the scan to get assets for|None|123456789|None|None|
  
Example input:

```
{
  "scan_id": 123456789
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assets|[]asset|False|Assets|[]|
  
Example output:

```
{
  "assets": []
}
```

#### Get Scan Engine

This action is used to get a scan engine by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Scan engine identifier|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan_engine|scan_engine|True|Scan engine details|{}|
  
Example output:

```
{
  "scan_engine": {}
}
```

#### Get Scan Engine Pool

This action is used to retrieve scan engine pool details by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Scan engine pool identifier|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan_engine_pool|scan_engine_pool|True|Scan engine pool details|{}|
  
Example output:

```
{
  "scan_engine_pool": {}
}
```

#### Get Scan Engine Pools

This action is used to retrieve a list of configured scan engine pools

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|False|Scan engine pool name by which to filter, accepts regular expression patterns|None|example name|None|None|
  
Example input:

```
{
  "name": "example name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan_engine_pools|[]scan_engine_pool|True|List of scan engine pool details|[]|
  
Example output:

```
{
  "scan_engine_pools": []
}
```

#### Get Scan Engines

This action is used to list scan engines paired with the security console

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|False|Optional address (IP/hostname) by which to filter, accepts regular expression patterns|None|10.4.36.120|None|None|
|name|string|None|False|Optional engine name by which to filter, accepts regular expression patterns|None|example name|None|None|
  
Example input:

```
{
  "address": "10.4.36.120",
  "name": "example name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan_engines|[]scan_engine|True|List of scan engines details|[]|
  
Example output:

```
{
  "scan_engines": []
}
```

#### Get Scans

This action is used to get scans with optional site filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|active|boolean|False|False|Return running scans or past scans|None|False|None|None|
|id|integer|None|False|Site ID|None|1234|None|None|
  
Example input:

```
{
  "active": false,
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scans|[]scan|True|List of scan details|[]|
  
Example output:

```
{
  "scans": []
}
```

#### Get Site

This action is used to get a site by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Site ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|site|site|True|Site details|{}|
  
Example output:

```
{
  "site": {}
}
```

#### Get Site Assets

This action is used to gets assets for a site

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|site_id|string|None|True|ID of the site to get assets for|None|11234abc-65c8-4628-adf4-e27f36ea0e2b|None|None|
  
Example input:

```
{
  "site_id": "11234abc-65c8-4628-adf4-e27f36ea0e2b"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assets|[]asset|False|Assets|[]|
  
Example output:

```
{
  "assets": []
}
```

#### Get Sites

This action is used to get a list of sites

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string||False|Site name regular expression by which to filter|None|example name|None|None|
  
Example input:

```
{
  "name": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|sites|[]site|True|List of sites|[]|
  
Example output:

```
{
  "sites": []
}
```

#### Get Tag

This action is used to get tag details by tag ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Tag ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|tag|tag|True|Tag Details|{}|
  
Example output:

```
{
  "tag": {}
}
```

#### Get Tag Asset Groups

This action is used to get asset groups associated with a tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Tag ID for which to retrieve asset group associations|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset_group_ids|[]integer|True|Asset group IDs associated with the tag|[]|
  
Example output:

```
{
  "asset_group_ids": []
}
```

#### Get Tag Assets

This action is used to get asset IDs associated with a tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Tag ID to add to site|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assets|[]tag_asset|True|Asset IDs and tag association sources for the tag|[]|
  
Example output:

```
{
  "assets": []
}
```

#### Get Tag Sites

This action is used to get site IDs associated with a tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Tag ID for which to retrieve site associations|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|site_ids|[]integer|True|Site IDs associated with the tag|[]|
  
Example output:

```
{
  "site_ids": []
}
```

#### Get Tags

This action is used to get a listing of all tags and return their details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string||False|Tag name regular expression by which to filter|None|example name|None|None|
|type|string||False|Type of tag by which to filter, all types are returned if none is specified|["owner", "location", "custom", "criticality", ""]|owner|None|None|
  
Example input:

```
{
  "name": "",
  "type": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|tags|[]tag|True|List of tags|[]|
  
Example output:

```
{
  "tags": []
}
```

#### Get User

This action is used to get user account details by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|User account ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user_account|True|User account details|{}|
  
Example output:

```
{
  "user": {}
}
```

#### Get Users

This action is used to list user accounts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|login|string|None|False|User account login name by which to filter, accepts regular expression patterns|None|account|None|None|
|name|string|None|False|User account name by which to filter, accepts regular expression patterns|None|example name|None|None|
  
Example input:

```
{
  "login": "account",
  "name": "example name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|users|[]user_account|True|List of user account details|[]|
  
Example output:

```
{
  "users": []
}
```

#### Get Vulnerabilities by CVE

This action is used to get vulnerability details associated with a CVE

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cve_id|string|None|True|Common Vulnerabilities and Exposures ID|None|CVE-2018-12345|None|None|
  
Example input:

```
{
  "cve_id": "CVE-2018-12345"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerabilities|[]vulnerability|True|Vulnerability details|[]|
  
Example output:

```
{
  "vulnerabilities": []
}
```

#### Get Vulnerability Details

This action is used to get the details of a specific vulnerability by id

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The identifier of the vulnerability to retrieve from InsightVM|None|1234-abcd|None|None|
  
Example input:

```
{
  "id": "1234-abcd"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerability|vulnerability|True|The details of the vulnerability requested|{}|
  
Example output:

```
{
  "vulnerability": {}
}
```

#### Get Vulnerability Affected Assets

This action is used to get the assets affected by the vulnerability

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|vulnerability_id|string|None|True|The identifier of the vulnerability|None|jre-vuln-cve-2013-2471|None|None|
  
Example input:

```
{
  "vulnerability_id": "jre-vuln-cve-2013-2471"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
|resources|[]integer|True|The identifiers of the associated resources|[]|
  
Example output:

```
{
  "links": [],
  "resources": []
}
```

#### List Inactive Assets

This action is used to returns a list of inactive assets (limit 1000) determined by how many days ago they were scanned

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|days_ago|integer|14|True|How many days ago should an asset be considered still active|None|14|None|None|
|size|number|500|False|The number of assets to retrieve. If blank then 500 inactive assets will be returned, the maximum limit is 1000 assets|None|100|None|None|
  
Example input:

```
{
  "days_ago": 14,
  "size": 500
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assets|[]asset|True|A list of inactive assets|[]|
  
Example output:

```
{
  "assets": []
}
```

#### List Reports

This action is used to list reports and return their identifiers

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|False|Name of report, otherwise all reports by criteria|None|Name|None|None|
|sort|string|None|True|Sort order, ascending or descending|["Ascending", "Descending"]|Ascending|None|None|
  
Example input:

```
{
  "name": "Name",
  "sort": "Ascending"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|Whether optional user supplied report name was found|False|
|list|[]report_id|False|List of report identifiers|[]|
  
Example output:

```
{
  "found": false,
  "list": []
}
```

#### Remove Asset Group Tags

This action is used to remove all tags from an asset group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Asset group ID from which to remove all tags|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Remove Asset Tag

This action is used to remove a tag from an asset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_id|integer|None|True|Asset ID from which to remove the tag|None|12345|None|None|
|tag_id|integer|None|True|Tag ID to remove from the asset|None|1234|None|None|
  
Example input:

```
{
  "asset_id": 12345,
  "tag_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Remove Scan Engine Pool Engine

This action is used to remove a scan engine from a scan engine pool

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|engine_id|integer|None|True|Scan engine ID|None|5678|None|None|
|pool_id|integer|None|True|Scan engine pool ID|None|1234|None|None|
  
Example input:

```
{
  "engine_id": 5678,
  "pool_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Remove Tag Asset Groups

This action is used to remove all asset group associations from a tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Tag ID from which to remove all asset group associations|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Remove Tag Search Criteria

This action is used to remove all search criteria from a tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Tag ID from which to remove all search criteria|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Remove Tag Sites

This action is used to remove all site associations from a tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Tag ID from which to remove all site associations|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Remove User Asset Group Access

This action is used to remove asset group access from an user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_group_id|integer|None|True|The identifier of the asset group|None|4567|None|None|
|user_id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "asset_group_id": 4567,
  "user_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Remove User Site Access

This action is used to remove site access from an user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|site_id|integer|None|True|The identifier of the site|None|4567|None|None|
|user_id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "site_id": 4567,
  "user_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Review Vulnerability Exception

This action is used to approve or Reject a Vulnerability Exception

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|False|Comment to include in the review|None|example comment|None|None|
|exception|integer|None|True|The vulnerability exception ID to approve or reject|None|1234|None|None|
|review|string|None|True|Approval or rejection of the exception|["Approved", "Rejected"]|Approved|None|None|
  
Example input:

```
{
  "comment": "example comment",
  "exception": 1234,
  "review": "Approved"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Scan

This action is used to start a scan on a site

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hosts|[]string|None|False|The hosts that should be included in the scan|None|["192.0.2.3", "192.0.2.10-192.0.2.20", "ADSRV.local"]|None|None|
|override_blackout|boolean|False|False|Set True to override any scan blackout window|None|False|None|None|
|site_id|string|None|True|ID of the site to scan|None|1|None|None|
  
Example input:

```
{
  "hosts": [
    "192.0.2.3",
    "192.0.2.10-192.0.2.20",
    "ADSRV.local"
  ],
  "override_blackout": false,
  "site_id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|False|Identifier of the resource created|188935|
|links|[]link|False|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 188935,
  "links": []
}
```

#### Tag Asset

This action is used to add a tag to an asset

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_id|integer|None|True|Asset ID to tag|None|12345|None|None|
|tag_id|integer|None|True|Tag ID to add to site|None|1234|None|None|
  
Example input:

```
{
  "asset_id": 12345,
  "tag_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Tag Asset Group

This action is used to add a tag to an asset group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_group_id|integer|None|True|Asset group ID to tag|None|12345|None|None|
|tag_id|integer|None|True|Tag ID to add to site|None|1234|None|None|
  
Example input:

```
{
  "asset_group_id": 12345,
  "tag_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Tag Assets

This action is used to add a tag to multiple assets in bulk. Please note this does not work with 'built-in' tags

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_ids|[]integer|None|True|Asset IDs to tag|None|[1, 2, 3, 4]|None|None|
|tag_id|integer|None|True|ID of tag to add to assets|None|12345|None|None|
|tag_name|string|None|True|Name of tag to add to assets|None|Very High|None|None|
|tag_source|string|None|True|Source of tag to add to assets|None|VM|None|None|
|tag_type|string|None|True|Type of tag to add to assets|None|owner|None|None|
  
Example input:

```
{
  "asset_ids": [
    1,
    2,
    3,
    4
  ],
  "tag_id": 12345,
  "tag_name": "Very High",
  "tag_source": "VM",
  "tag_type": "owner"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was the operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Tag Site

This action is used to add a tag to a site

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|site_id|integer|None|True|Site ID to tag|None|12345|None|None|
|tag_id|integer|None|True|Tag ID to add to site|None|1234|None|None|
  
Example input:

```
{
  "site_id": 12345,
  "tag_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Top Remediations

This action is used to generate results for the top remediations based on a defined scope

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_limit|integer|None|False|The amount of assets to be returned with each top remediation; this can be used to reduce message size and processing time|None|4|None|None|
|limit|integer|25|True|Number of remediations for which tickets should be generated|[10, 25, 50, 100]|10|None|None|
|scope|string|none|True|Scope context for generated report; if set remediations will be scoped by each in scope ID|["none", "assets", "assetGroups", "sites", "tags", "scan"]|none|None|None|
|scope_ids|[]integer|[]|False|Scope IDs for which tickets should be generated, by default all are included|None|[1234, 45]|None|None|
|vulnerability_limit|integer|None|False|The amount of vulnerabilities to be returned with each top remediation; this can be used to reduce message size and processing time|None|2|None|None|
  
Example input:

```
{
  "asset_limit": 4,
  "limit": 25,
  "scope": "none",
  "scope_ids": [],
  "vulnerability_limit": 2
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|remediations|[]remediation|True|List of top remediations|[]|
  
Example output:

```
{
  "remediations": []
}
```

#### Update Asset Group Search Criteria

This action is used to update the search criteria for an existing asset group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Asset group ID|None|1234|None|None|
|searchCriteria|object|None|True|Asset group search criteria - options documentation: https://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|{'risk-score': 'asc', 'criticality-tag': 'desc'}|None|None|
  
Example input:

```
{
  "id": 1234,
  "searchCriteria": "{'risk-score': 'asc', 'criticality-tag': 'desc'}"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Update Scan Status

This action is used to update the status of a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Scan ID|None|1234|None|None|
|status|string|stop|True|Status to which the scan should be set (stop, resume, pause)|["stop", "resume", "pause"]|stop|None|None|
  
Example input:

```
{
  "id": 1234,
  "status": "stop"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Update Shared Credentials

This action is used to update shared credentials

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account|account|None|True|Specify the type of service to authenticate as well as all of the information required by that service|None|{'authentication_type': 'no-authentication', 'community_name': 'rapid community', 'database': 'rapid7_database', 'domain': 'rapid7.com', 'enumerate_sids': False, 'notes_id_password': 'notes_id_password', 'ntlm_hash': '86956E15C7F452086BEEB6BB005E0388', 'oracle_listener_password': 'oracle_listener_password', 'password': 'password', 'pem_key': '-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEA3Tz2mr7SZiAMfQyuvBj...', 'permission_elevation': 'sudo', 'permission_elevation_password': 'permission_elevation_password', 'permission_elevation_username': 'permission_elevation_username', 'privacy_password': 'privacy_password', 'privacy_type': 'no-privacy', 'private_key_password': 'private_key_password', 'realm': 'realm0', 'service': 'telnet', 'sid': 'rapid7_database2', 'use_windows_authentication': False, 'username': 'username'}|None|None|
|description|string|None|False|The description of the credential|None|example input with every field filled. Note real input will only have specific fields filled|None|None|
|host_restriction|string|None|False|The host name or IP address that you want to restrict the credentials to|None|my-macbook-name|None|None|
|id|integer|None|False|The identifier of the credential|None|123|None|None|
|name|string|None|True|The name of the credential|None|my-AS400-credentials|None|None|
|port_restriction|string|None|False|Further restricts the credential to attempt to authenticate on a specific port. The port can only be restricted if the property hostRestriction is specified|None|8888|None|None|
|site_assignment|string|None|True|Assigns the shared scan credential either to be available to all sites or to a specific list of sites. All sites - The shared scan credential is assigned to all current and future sites. specific-sites - The shared scan credential is assigned to zero sites by default. Administrators must explicitly assign sites to the shared credential. Shared scan credentials assigned to a site can disabled within the site configuration, if needed|["all-sites", "specific-sites"]|all-sites|None|None|
|sites|[]integer|None|False|List of site identifiers. These sites are explicitly assigned access to the shared scan credential, allowing the site to use the credential for authentication during a scan. This property can only be set if the value of property siteAssignment is set to "specific-sites". When the property siteAssignment is set to "all-sites", this property will be null|None|[]|None|None|
  
Example input:

```
{
  "account": {
    "authentication_type": "no-authentication",
    "community_name": "rapid community",
    "database": "rapid7_database",
    "domain": "rapid7.com",
    "enumerate_sids": false,
    "notes_id_password": "notes_id_password",
    "ntlm_hash": "86956E15C7F452086BEEB6BB005E0388",
    "oracle_listener_password": "oracle_listener_password",
    "password": "password",
    "pem_key": "-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEA3Tz2mr7SZiAMfQyuvBj...",
    "permission_elevation": "sudo",
    "permission_elevation_password": "permission_elevation_password",
    "permission_elevation_username": "permission_elevation_username",
    "privacy_password": "privacy_password",
    "privacy_type": "no-privacy",
    "private_key_password": "private_key_password",
    "realm": "realm0",
    "service": "telnet",
    "sid": "rapid7_database2",
    "use_windows_authentication": false,
    "username": "username"
  },
  "description": "example input with every field filled. Note real input will only have specific fields filled",
  "host_restriction": "my-macbook-name",
  "id": 123,
  "name": "my-AS400-credentials",
  "port_restriction": 8888,
  "site_assignment": "all-sites",
  "sites": []
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Update Site

This action is used to update an existing site

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|True|The site's description|None|example description|None|None|
|engine_id|integer|None|True|The identifier of a scan engine. Default scan engine is selected when not specified|None|1234|None|None|
|id|integer|None|True|The identifier of the site|None|1234|None|None|
|importance|string|normal|True|The site importance|["very_low", "low", "normal", "high", "very_high"]|low|None|None|
|name|string|None|True|The site name. Name must be unique|None|example name|None|None|
|scan_template_id|string|None|True|The identifier of a scan template|None|1234|None|None|
  
Example input:

```
{
  "description": "example description",
  "engine_id": 1234,
  "id": 1234,
  "importance": "normal",
  "name": "example name",
  "scan_template_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|The identifier of the updated site|332|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 332,
  "links": []
}
```

#### Update Site Excluded Asset Groups

This action is used to update an existing site scope of excluded asset groups

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|excluded_asset_groups|[]integer|None|False|Assets associated with these asset group IDs will be excluded from the site|None|[1234, 567]|None|None|
|id|integer|None|True|The identifier of the site|None|1234|None|None|
|overwrite|boolean|True|True|Whether to overwrite the excluded asset group IDs to the current site or append to the previous list of asset group IDs|None|True|None|None|
  
Example input:

```
{
  "excluded_asset_groups": [
    1234,
    567
  ],
  "id": 1234,
  "overwrite": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|The identifier of the updated site|332|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 332,
  "links": []
}
```

#### Update Site Excluded Targets

This action is used to update an existing site scope of excluded IP address and hostname targets

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|excluded_targets|[]string|None|False|List of addresses that represent either a hostname, IPv4 address, IPv4 address range, IPv6 address, or CIDR notation|None|["10.2.144", "10.8.36.144"]|None|None|
|id|integer|None|True|The identifier of the site|None|1234|None|None|
|overwrite|boolean|True|True|Whether to overwrite the excluded targets to the current site or append to the previous list of excluded targets|None|True|None|None|
  
Example input:

```
{
  "excluded_targets": [
    "10.2.144",
    "10.8.36.144"
  ],
  "id": 1234,
  "overwrite": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|The identifier of the updated site|1234|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 1234,
  "links": []
}
```

#### Update Site Included Asset Groups

This action is used to update an existing site scope of included asset groups

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|The identifier of the site|None|1234|None|None|
|included_asset_groups|[]integer|None|False|Assets associated with these asset group IDs will be included in the site|None|[1234, 567]|None|None|
|overwrite|boolean|True|True|Whether to overwrite the included asset group IDs to the current site or append to the previous list of asset group IDs|None|True|None|None|
  
Example input:

```
{
  "id": 1234,
  "included_asset_groups": [
    1234,
    567
  ],
  "overwrite": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|The identifier of the updated site|332|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 332,
  "links": []
}
```

#### Update Site Included Targets

This action is used to update an existing site scope of included IP address and hostname targets

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|The identifier of the site|None|1234|None|None|
|included_targets|[]string|None|False|List of addresses that represent either a hostname, IPv4 address, IPv4 address range, IPv6 address, or CIDR notation|None|["10.2.144", "10.8.36.144"]|None|None|
|overwrite|boolean|True|True|Whether to overwrite the included targets to the current site or append to the previous list of included targets|None|True|None|None|
  
Example input:

```
{
  "id": 1234,
  "included_targets": [
    "10.2.144",
    "10.8.36.144"
  ],
  "overwrite": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|True|The identifier of the updated site|1234|
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "id": 1234,
  "links": []
}
```

#### Update Site Scan Engine

This action is used to update the scan engine/scan engine pool associated with a site

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|engine_id|integer|None|True|Identifier of the scan engine/scan engine pool to associate with the site|None|5678|None|None|
|site_id|integer|None|True|Identifier of the site to update|None|1234|None|None|
  
Example input:

```
{
  "engine_id": 5678,
  "site_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Update Tag Search Criteria

This action is used to update the search criteria for an existing tag

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|Tag ID|None|1234|None|None|
|searchCriteria|object|None|True|Tag search criteria - options documentation: https://help.rapid7.com/insightvm/en-us/api/#section/Responses/SearchCriteria|None|{'risk-score': 'asc', 'criticality-tag': 'desc'}|None|None|
  
Example input:

```
{
  "id": 1234,
  "searchCriteria": "{'risk-score': 'asc', 'criticality-tag': 'desc'}"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Update User

This action is used to update the configuration of an existing user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|access_all_asset_groups|boolean|False|True|Whether to grant the user access to all asset groups|None|False|None|None|
|access_all_sites|boolean|False|True|Whether to grant the user access to all sites|None|False|None|None|
|authentication_id|integer|None|False|The identifier of the authentication source to use to authenticate the user. The source with the specified identifier must be of the type specified by Authentication Type. If Authentication ID is omitted, then one source of the specified Authentication Type is selected|None|567|None|None|
|authentication_type|string|ldap|True|The type of the authentication source to use to authenticate the user|["normal", "admin", "kerberos", "ldap", "saml"]|ldap|None|None|
|email|string|None|True|The email address of the user|None|user@example.com|None|None|
|enabled|boolean|True|True|Whether the user account is enabled|None|True|None|None|
|id|integer|None|True|The identifier of the user|None|1234|None|None|
|login|string|None|True|The login name of the user|None|jdoe24|None|None|
|name|string|None|True|The full name of the user|None|John Doe|None|None|
|role_id|string|None|True|The identifier of the role to which the user should be assigned|None|global-admin|None|None|
  
Example input:

```
{
  "access_all_asset_groups": false,
  "access_all_sites": false,
  "authentication_id": 567,
  "authentication_type": "ldap",
  "email": "user@example.com",
  "enabled": true,
  "id": 1234,
  "login": "jdoe24",
  "name": "John Doe",
  "role_id": "global-admin"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Update User Asset Group Access

This action is used to update the asset groups to which a user has access in bulk. It can be used to remove asset group
 access as well

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_group_ids|[]integer|None|True|The identifiers of the asset groups to which the user account should be granted access, ignored if the user has access to all asset groups|None|[1234, 5678]|None|None|
|user_id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "asset_group_ids": [
    1234,
    5678
  ],
  "user_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Update User Role

This action is used to update the role associated with an user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|access_all_asset_groups|boolean|False|True|Whether to grant the user access to all asset groups|None|False|None|None|
|access_all_sites|boolean|False|True|Whether to grant the user access to all sites|None|False|None|None|
|role_id|string|None|True|The identifier of the role to which the user should be assigned|None|global-admin|None|None|
|user_id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "access_all_asset_groups": false,
  "access_all_sites": false,
  "role_id": "global-admin",
  "user_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Update User Site Access

This action is used to update the sites to which a user has access in bulk. It can be used to remove sites as well

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|site_ids|[]integer|None|True|The identifiers of the sites to which the user account should be granted access, ignored if the user has access to all sites|None|[1234, 567]|None|None|
|user_id|integer|None|True|The identifier of the user account|None|1234|None|None|
  
Example input:

```
{
  "site_ids": [
    1234,
    567
  ],
  "user_id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|links|[]link|True|Hypermedia links to corresponding or related resources|[]|
  
Example output:

```
{
  "links": []
}
```

#### Update Vulnerability Exception Expiration Date

This action is used to update vulnerability exception expiration date

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|date|string|None|True|Expiration date|None|2020-02-24T06:59:59.999Z|None|None|
|id|integer|None|True|Asset ID|None|42|None|None|
  
Example input:

```
{
  "date": "2020-02-24T06:59:59.999Z",
  "id": 42
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers


#### New Vulnerability Exception

This trigger is used to check for new InsightVM vulnerability exceptions

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|5|True|How often the trigger should check for new vulnerability exception requests|None|5|None|None|
|status_filter|[]string|["Under Review"]|False|List of vulnerability statuses to match against. Options include: Under Review and Approved|None|["Under Review"]|None|None|
  
Example input:

```
{
  "frequency": 5,
  "status_filter": [
    "Under Review"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|exception|vulnerability_exception|False|InsightVM vulnerability exception|{}|
  
Example output:

```
{
  "exception": {}
}
```

#### New Scans

This trigger is used to check for new InsightVM scans by site and scan status

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|5|True|How often the trigger should check for new scans in minutes|None|5|None|None|
|most_recent_scan|boolean|True|True|Only process the most recent scan for a site since the last time the trigger was run|None|True|None|None|
|site_name_filter|string|.*|True|Regular expression to match sites where new scans should be triggered|None|example name|None|None|
|status_filter|[]string|["Successful"]|False|List of scan statuses to match for trigger; options include: Aborted, Successful, Running, Stopped, Failed, Paused, Unknown|None|["Successful"]|None|None|
  
Example input:

```
{
  "frequency": 5,
  "most_recent_scan": true,
  "site_name_filter": ".*",
  "status_filter": [
    "Successful"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan|scan|False|InsightVM Scan|{}|
  
Example output:

```
{
  "scan": {}
}
```

#### Scan Completed

This trigger is used to fire upon completed scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|5|True|How often the trigger should check for new vulnerability scans in minutes|None|5|None|None|
|site_id|string|None|False|Site ID|None|219|None|None|
  
Example input:

```
{
  "interval": 5,
  "site_id": 219
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan_completed_output|[]scanCompleted|False|An array containing all the info|{}|
|scan_id|integer|False|The ID of the scan|42|
  
Example output:

```
{
  "scan_completed_output": {},
  "scan_id": 42
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**scanCompleted**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Best Solution|string|None|False|Best solution|None|
|CVSS Score|float|None|False|CVSS Score|None|
|CVSS V3 Score|float|None|False|CVSS v3 score|None|
|Date First Seen On Asset|string|None|False|Date first seen on the asset|None|
|Date Most Recently Seen On Asset|string|None|False|Date most recently seen on the asset|None|
|Days Present On Asset|integer|None|False|Days present on the asset|None|
|Days Since Vulnerability First Published|integer|None|False|Days since the vulnerability was first published|None|
|Estimated Time To Fix Per Asset|string|None|False|Estimated time to fix per asset|None|
|Exploits|integer|None|False|Number of public exploits|None|
|Hostname|string|None|False|Hostname|None|
|IP Address|string|None|False|IP address for the asset|None|
|Malware Kits|integer|None|False|Number of malware kits known|None|
|Member of Sites|[]string|None|False|Show which sites the vuln is a member of|None|
|Nexpose ID|string|None|False|Nexpose ID|None|
|Operating System|string|None|False|OS|None|
|Risk Score|integer|None|False|Risk score|None|
|Severity|string|None|False|Severity|None|
|Solution ID|integer|None|False|Solution ID|None|
|Solution Type|string|None|False|The type of the solution for the vulnerability|None|
|Date Vulnerability First Published|string|None|False|Date the vulnerability was first published|None|
|Vulnerability Details|string|None|False|Vulnerability details|None|
|Vulnerability ID|integer|None|False|Vulnerability ID|None|
|Vulnerability Instances|integer|None|False|Vulnerability count on asset|None|
|Vulnerability Name|string|None|False|Vulnerability name|None|
  
**report_id**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Report ID|integer|None|False|Identifer|None|
|Report Name|string|None|False|Name of report|None|
  
**link**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|URL|string|None|False|A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)|None|
|Rel|string|None|False|Link relation type following RFC 5988|None|
  
**fingerprint**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|None|None|
|Family|string|None|False|None|None|
|Product|string|None|False|None|None|
|Vendor|string|None|False|None|None|
|Version|string|None|False|None|None|
  
**match**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Confidence|string|None|False|None|None|
|Fingerprint|fingerprint|None|False|None|None|
  
**step**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HTML|string|None|False|None|None|
|text|string|None|False|None|None|
  
**summary**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HTML|string|None|False|None|None|
|text|string|None|False|None|None|
  
**resources**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Applies To|string|None|False|None|None|
|Confidence|string|None|False|None|None|
|Estimate|string|None|False|None|None|
|ID|string|None|False|None|None|
|links|[]link|None|False|None|None|
|Matches|[]match|None|False|None|None|
|Steps|step|None|False|None|None|
|Summary|summary|None|False|None|None|
|Type|string|None|False|None|None|
  
**address**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP|string|None|False|IPv4 or IPv6 address|None|
|MAC|string|None|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|None|
  
**configuration**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name of the configuration value|None|
|Value|string|None|False|Configuration value|None|
  
**database**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description of the database instance|None|
|ID|integer|None|False|Identifier of the database|None|
|Name|string|None|False|Name of the database instance|None|
  
**insightvm_file**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attributes|[]configuration|None|False|Attributes detected on the file|None|
|Contents|bytes|None|False|Contents of the file|None|
|Name|string|None|False|Name of the file|None|
|Size|integer|None|False|Size of the regular file (in bytes). If the file is a directory, no value is returned|None|
|Type|string|None|False|Type of the file, e.g. file or directory|None|
  
**history**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Date|string|None|False|Date the asset information was collected or changed|None|
|Description|string|None|False|Additional information describing the change|None|
|Scan ID|integer|None|False|If a scan-oriented change, the identifier of the corresponding scan the asset was scanned in|None|
|Type|string|None|False|Type, for additional information see the help section of this plugin|None|
|User|string|None|False|User|None|
|Version|integer|None|False|Version|None|
|Vulnerability Exception ID|integer|None|False|Vulnerability exception ID|None|
  
**hostName**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
|Source|string|None|False|Source|None|
  
**id**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID|None|
|Source|string|None|False|Source|None|
  
**cpe**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Edition|string|None|False|Edition-related terms applied by the vendor to the product|None|
|Language|string|None|False|Defines the language supported in the user interface of the product being described. The format of the language tag adheres to RFC 5646|None|
|Other|string|None|False|Captures any other general descriptive or identifying information which is vendor- or product-specific and which does not logically fit in any other attribute value|None|
|Part|string|None|False|A single letter code that designates the particular platform part that is being identified|None|
|Product|string|None|False|Most common and recognizable title or name of the product|None|
|Software Edition|string|None|False|Characterizes how the product is tailored to a particular market or class of end users|None|
|Target Hardware|string|None|False|Characterize the instruction set architecture on which the product operates|None|
|Target Software|string|None|False|Characterizes the software computing environment within which the product operates|None|
|Update|string|None|False|Vendor-specific alphanumeric strings characterizing the particular update, service pack, or point release of the product|None|
|Version 2.2|string|None|False|The full CPE string in the CPE 2.2 format|None|
|Version 2.3|string|None|False|The full CPE string in the CPE 2.3 format|None|
|Vendor|string|None|False|The person or organization that manufactured or created the product|None|
|Version|string|None|False|Vendor-specific alphanumeric strings characterizing the particular release version of the product|None|
  
**osFingerprint**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Architecture|string|None|False|The architecture of the operating system|None|
|Configuration|[]configuration|None|False|Configuration key-values pairs enumerated on the operating system|None|
|CPE|cpe|None|False|Common Platform Enumeration|None|
|Description|string|None|False|The description of the operating system (containing vendor, family, product, version and architecture in a single string)|None|
|Family|string|None|False|Family of the operating system|None|
|ID|integer|None|False|Identifier of the operating system|None|
|Product|string|None|False|Name of the operating system|None|
|System Name|string|None|False|A combination of vendor and family (with redundancies removed), suitable for grouping|None|
|Type|string|None|False|Type of operating system|None|
|Vendor|string|None|False|Vendor of the operating system|None|
|Version|string|None|False|Version of the operating system|None|
  
**userGroup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Identifier of the user group|None|
|Name|string|None|False|Name of the user group|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Full Name|string|None|False|Full name of the user account|None|
|ID|integer|None|False|Identifier of the user account|None|
|Name|string|None|False|Name of the user account|None|
  
**page**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Link Type|string|None|False|Type of link used to traverse or detect the page|None|
|Path|string|None|False|Path to the page (URI)|None|
|Response|integer|None|False|HTTP response code observed with retrieving the page|None|
  
**webApplication**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Identifier of the web application|None|
|Pages|[]page|None|False|Pages|None|
|Root|string|None|False|Web root of the web application|None|
|Virtual Host|string|None|False|Virtual host of the web application|None|
  
**service**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Configurations|[]configuration|None|False|Configuration key-values pairs enumerated on the service|None|
|Databases|[]database|None|False|Databases enumerated on the service|None|
|Family|string|None|False|Family of the service|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Name|string|None|False|Name of the service|None|
|Port|integer|None|False|Port of the service|None|
|Product|string|None|False|Product running the service|None|
|Protocol|string|None|False|Protocol of the service|None|
|User Groups|[]userGroup|None|False|User groups|None|
|Users|[]user|None|False|Users|None|
|Vendor|string|None|False|Vendor of the service|None|
|Version|string|None|False|Version of the service|None|
|Web Applications|[]webApplication|None|False|Web applications found on the service|None|
  
**software**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Configurations|[]configuration|None|False|Configurations|None|
|CPE|cpe|None|False|CPE|None|
|Description|string|None|False|Description of the software|None|
|Family|string|None|False|Family of the software|None|
|ID|integer|None|False|ID|None|
|Product|string|None|False|Product of the software|None|
|Type|string|None|False|Type of the software|None|
|Vendor|string|None|False|Vendor of the software|None|
|Version|string|None|False|Version of the software|None|
  
**vulnerabilities**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Critical|integer|None|False|Number of critical vulnerabilities|None|
|Exploits|integer|None|False|Number of distinct exploits that can exploit any of the vulnerabilities on the asset|None|
|Malware Kits|integer|None|False|Number of distinct malware kits that vulnerabilities on the asset are susceptible to|None|
|Moderate|integer|None|False|Number of moderate vulnerabilities|None|
|Severe|integer|None|False|Number of severe vulnerabilities|None|
|Total|integer|None|False|Total number of vulnerabilities|None|
  
**vulnerabilities_count**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Critical|integer|None|False|Number of critical vulnerabilities|None|
|Moderate|integer|None|False|Number of moderate vulnerabilities|None|
|Severe|integer|None|False|Number of severe vulnerabilities|None|
|Total number of vulnerabilities|integer|None|False|Total|None|
  
**vulnerability_exception**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Expires|date|None|False|The date and time the vulnerability exception is set to expire|None|
|Vulnerability Exception ID|integer|None|True|The ID uniquely identifying the vulnerability exception|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Review Details|object|None|False|Details of the exception review|None|
|Exception Scope|object|None|True|Details of the scope of the exception|None|
|State|string|None|True|The state of the vulnerability exception|None|
|Submission Details|object|None|True|Details of the exception submission|None|
  
**exception_review**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Review Comment|string|None|False|The comment from the reviewer detailing the review|None|
|Review Date|date|None|False|The date and time the review took place|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Reviewer Name|string|None|False|The login name of the user that reviewed the vulnerability exception|None|
|Reviewer ID|integer|None|False|The identifier of the user that reviewed the vulnerability exception|None|
  
**exception_submit**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Submit Comment|string|None|False|The comment from the submit detailing the exception|None|
|Submit Date|date|None|False|The date and time the exception request took place|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Submitter Name|string|None|False|The login name of the user that submitted the vulnerability exception|None|
|Submitter ID|integer|None|False|The identifier of the user that submitted the vulnerability exception|None|
  
**exception_scope**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Vulnerability Scope ID|integer|None|True|The identifer of the scope (asset, group, site) the vulnerability exception applies to|None|
|Exception Scope Key|string|None|False|Optional key to discriminate the instance when the scope type is Instance|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Port|integer|None|False|If the scope type is Instance, the port the exception applies to|None|
|Exception Scope Type|string|None|True|The type of vulnerability exception - Global, Site, Asset, Asset Group, Instance|None|
|Vulnerability|string|None|True|The vulnerability the exception applies to|None|
  
**asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Addresses|[]address|None|False|All addresses discovered on the asset|None|
|Assessed for Policies|boolean|None|False|Whether the asset has been assessed for policies at least once|None|
|Assessed for Vulnerabilities|boolean|None|False|Whether the asset has been assessed for vulnerabilities at least once|None|
|Configurations|[]configuration|None|False|Configuration key-values pairs enumerated on the asset|None|
|Databases|[]database|None|False|Databases enumerated on the asset|None|
|Files|[]insightvm_file|None|False|Files discovered with searching on the asset|None|
|History|[]history|None|False|History of changes to the asset over time|None|
|Hostname|string|None|False|Primary host name (local or FQDN) of the asset|None|
|Hostnames|[]hostName|None|False|All hostnames or aliases discovered on the asset|None|
|ID|integer|None|False|Identifier of the asset|None|
|IDs|[]id|None|False|Unique identifiers found on the asset, such as hardware or operating system identifiers|None|
|IP|string|None|False|Primary IPv4 or IPv6 address of the asset|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|MAC|string|None|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|None|
|OS|string|None|False|Full description of the operating system of the asset|None|
|OS Fingerprint|osFingerprint|None|False|Details of the operating system of the asset|None|
|Raw Risk Score|float|None|False|Base risk score of the asset|None|
|Risk Score|float|None|False|Risk score (with criticality adjustments) of the asset|None|
|Services|[]service|None|False|Services discovered on the asset|None|
|Software|[]software|None|False|Software discovered on the asset|None|
|Type|string|None|False|Type of asset e.g. unknown, guest, hypervisor, physical, mobile|None|
|User Groups|[]userGroup|None|False|User group accounts enumerated on the asset|None|
|Users|[]user|None|False|User accounts enumerated on the asset|None|
|Vulnerabilities|vulnerabilities|None|False| Summary information for vulnerabilities on the asset|None|
  
**asset_vulnerability_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Check ID|string|None|False|Check ID, ie. ssh-openssh-x11uselocalhost-x11-forwarding-session-hijack|None|
|Exceptions|[]integer|None|False|If the result is vulnerable with exceptions applied, the identifier(s) of the exceptions actively applied to the result|None|
|Key|string|None|False|An additional discriminating key used to uniquely identify between multiple instances of results on the same finding|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Port|integer|None|False|Port of the service the result was discovered on e.g. 22|None|
|Proof|string|None|False|Proof of the vulnerability, ie. <p><p>OpenBSD OpenSSH 4.3 on Linux</p></p>|None|
|Protocol|string|None|False|Protocol of the service the result was discovered on, ie. TCP|None|
|Status|string|None|False|Status of the vulnerability check result, ie. vulnerable-version|None|
  
**asset_vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Vulnerability ID, ie. ssh-openssh-x11uselocalhost-x11-forwarding-session-hijack|None|
|Instances|integer|None|False|Identifier of the report instance|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Results|[]asset_vulnerability_result|None|False|The vulnerability check results for the finding. Multiple instances may be present if one or more checks fired, or a check has multiple independent results|None|
|Risk Score|float|None|False|The risk score for the vulnerability|None|
|Since|string|None|False|The date when this vulnerability was first detected|None|
|Status|string|None|False|Status, ie. vulnerable|None|
  
**site**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assets|integer|None|True|Site asset count|None|
|Connection Type|string|None|False|Site discovery connection type (if applicable)|None|
|Description|string|None|False|Site description|None|
|ID|integer|None|True|Identifier of the site|None|
|Importance|string|None|True|Site importance, used with the 'weighted' risk scoring strategy|None|
|Last Scan Time|date|None|False|Site last scan time|None|
|Links|[]link|None|True|Hypermedia links to corresponding or related resources|None|
|Name|string|None|True|Site name|None|
|Risk Score|float|None|True|Site risk score|None|
|Scan Engine|integer|None|True|Site default scan engine ID|None|
|Scan Template|string|None|True|Site default scan template|None|
|Type|string|None|True|Site type|None|
|Vulnerabilities|vulnerabilities_count|None|True|Site vulnerability counts|None|
  
**asset_group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assets|integer|None|True|Site asset count|None|
|Description|string|None|False|Asset group description|None|
|ID|integer|None|True|Site ID|None|
|Links|[]link|None|True|Hypermedia links to corresponding or related resources|None|
|Name|string|None|True|Asset group name|None|
|Risk Score|float|None|True|Site risk score|None|
|Search Criteria|object|None|False|Asset group search criteria|None|
|Type|string|None|True|Asset group type|None|
|Vulnerabilities|vulnerabilities_count|None|True|Asset group vulnerability counts|None|
  
**vulnerability_description**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HTML|string|None|None|Vulnerability description HTML|None|
|Text|string|None|None|Vulnerability description raw text|None|
  
**pci**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Adjusted CVSS score|integer|None|None|PCI adjusted CVSS score|None|
|Adjusted severity score|integer|None|None|PCI adjusted severity score|None|
|Fail|boolean|None|None|Whether this vulnerability results in a PCI assessment failure|None|
|Special Notes|string|None|None|PCI special notes|None|
|Status|string|None|None|PCI status|None|
  
**cvss_v2**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access Complexity|string|None|None|CVSSv2 access complexity metric|None|
|Access Vector|string|None|None|CVSSv2 access vector metric|None|
|Authentication|string|None|None|CVSSv2 authentication metric|None|
|Availability Impact|string|None|None|CVSSv2 availability impact metric|None|
|Confidentiality Impact|string|None|None|CVSSv2 confidentiality impact metric|None|
|Exploit Score|float|None|None|CVSSv2 combined exploit metric score (Access Complexity/Access Vector/Authentication)|None|
|Impact Score|float|None|None|CVSSv2 combined impact metric score (Confidentiality/Integrity/Availability)|None|
|Integrity Impact|string|None|None|CVSSv2 integrity impact metric|None|
|Score|float|None|None|CVSSv2 score|None|
|Vector|string|None|None|CVSSv2 combined vector string|None|
  
**cvss_v3**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attack Complexity|string|None|None|CVSSv3 attack complexity metric|None|
|Attack Vector|string|None|None|CVSSv3 attack vector metric|None|
|Availability Impact|string|None|None|CVSSv3 availability impact metric|None|
|Confidentiality Impact|string|None|None|CVSSv3 confidentiality impact metric|None|
|Exploit Score|float|None|None|CVSSv3 combined exploit metric score (Attack Complexity/Attack Vector/Privilege Required/Scope/User Interaction)|None|
|Impact Score|float|None|None|CVSSv3 combined impact metric score (Confidentiality/Integrity/Availability)|None|
|Integrity Impact|string|None|None|CVSSv3 integrity impact metric|None|
|Privilege Required|string|None|None|CVSSv3 privilege required metric|None|
|Scope|string|None|None|CVSSv3 scope metric|None|
|Score|float|None|None|CVSSv3 score|None|
|User Interaction|string|None|None|CVSSv3 user interaction metric|None|
|Vector|string|None|None|CVSSv3 combined vector string|None|
  
**cvss**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Links|[]link|None|None|List of hypermedia links to corresponding resources|None|
|V2|cvss_v2|None|None|CVSSv2 details|None|
|V3|cvss_v3|None|None|CVSSv3 details|None|
  
**vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Added|date|None|None|Date that the vulnerability was added to InsightVM|None|
|Categories|[]string|None|None|List of vulnerabilities categories with which this vulnerability is affiliated|None|
|CVEs|[]string|None|None|List of CVE identifiers associated with this vulnerability|None|
|CVSS|cvss|None|None|Vulnerability CVSS details|None|
|Denial of Service|boolean|None|None|Whether the vulnerability is a denial of service vulnerability|None|
|Description|vulnerability_description|None|None|Vulnerability description|None|
|Exploits|integer|None|None|Exploit count|None|
|ID|string|None|None|Vulnerability ID|None|
|Links|[]link|None|None|List of hypermedia links to corresponding resources|None|
|Malware Kits|integer|None|None|Malware kit count|None|
|Modified|date|None|None|Date the vulnerability was last modified in InsightVM|None|
|PCI|pci|None|None|Vulnerability PCI details|None|
|Published|date|None|None|Date the vulnerability was published|None|
|Risk Score|float|None|None|Vulnerability risk score using the configured risk scoring strategy (RealRisk by default)|None|
|Severity|string|None|None|Vulnerability severity string (Moderate/Severe/Critical)|None|
|Severity Score|integer|None|None|Vulnerability severity score|None|
|Title|string|None|None|Vulnerability title|None|
  
**tag**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Color|string|None|False|Tag color|None|
|Created|date|None|None|Tag creation date|None|
|ID|integer|None|True|Tag ID|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Name|string|None|True|Tag name|None|
|Risk Modifier|string|None|False|Tag risk score modifier|None|
|Search Criteria|object|None|False|Tag search criteria|None|
|Source|string|None|False|Tag source|None|
|Type|string|None|True|Tag type|None|
  
**tag_asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|True|Asset ID|None|
|Sources|[]string|None|True|Tag association sources|None|
  
**scan**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assets|integer|None|None|Count of assets identified during the scan|None|
|Duration|date|None|None|Duration of the scan|None|
|End Time|date|None|None|End time of the scan|None|
|Engine ID|integer|None|None|ID for the scan engine/scan engine pool used for the scan|None|
|Engine Name|string|None|None|Name of the scan engine/scan engine pool used for the scan|None|
|ID|integer|None|None|ID of the scan|None|
|Links|[]link|None|None|List of hypermedia links to corresponding resources|None|
|Message|string|None|None|Scan status message|None|
|Scan Name|string|None|None|Name of the scan|None|
|Scan Type|string|None|None|Type of scan (automated, manual, scheduled)|None|
|Site ID|integer|None|None|ID of the site scanned|None|
|Site Name|string|None|None|Name of the site scanned|None|
|Start Time|date|None|None|Start time for the scan|None|
|Started By|string|None|None|User that started the scan|None|
|Status|string|None|None|Scan status (aborted, unknown, running, finished, stopped, error, paused, dispatched, integrating)|None|
|Vulnerabilities|vulnerabilities_count|None|None|Counts of vulnerabilities identified during the scan|None|
  
**scan_engine**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Address|string|None|True|Scan engine address (IP/hostname)|None|
|Content Version|string|None|False|Scan engine content version|None|
|Engine Pools|[]integer|None|True|Engine pool IDs with which the scan engine is associated|None|
|ID|integer|None|True|Scan engine identifier|None|
|Last Refreshed Date|date|None|False|Date and time when the engine last communicated with the console|None|
|Last Updated Date|date|None|False|Date and time when the engine was last updated|None|
|Links|[]link|None|True|List of hypermedia links to corresponding resources|None|
|Name|string|None|True|Scan engine name|None|
|Port|integer|None|True|Scan engine communication port|None|
|Product Version|string|None|False|Scan engine product version|None|
|Sites|[]integer|None|False|Sites with which the scan engine is associated|None|
  
**scan_engine_pool**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Engines|[]integer|None|True|List of scan engine IDs associated with the scan engine pool|None|
|ID|integer|None|True|Scan engine pool identifier|None|
|Links|[]link|None|True|List of hypermedia links to corresponding resources|None|
|Name|string|None|True|Scan engine pool name|None|
  
**authentication_source**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|External|boolean|None|True|Whether the authentication source is external (true) or internal (false)|None|
|ID|integer|None|True|Authentication source identifier|None|
|Links|[]link|None|True|List of hypermedia links to corresponding or related resources|None|
|Name|string|None|True|Authentication source name|None|
|Type|string|None|True|Authentication source type|None|
  
**role**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|True|The description of the role|None|
|id|string|None|True|ID of the role, e.g 'global-admin'|None|
|Links|[]link|None|True|List of hypermedia links to corresponding or related resources|None|
|Name|string|None|True|Name of the role|None|
|Privileges|[]string|None|True|List of privileges assigned to the role|None|
  
**user_account_role**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|All Asset Groups|boolean|None|False|Whether the user has access to all asset groups|None|
|All Sites|boolean|None|False|Whether the user has access to all sites|None|
|ID|string|None|False|The identifier of the role the user is assigned to|None|
|Privileges|[]string|None|False|None|None|
|Superuser|boolean|None|False|Whether the user is a superuser|None|
  
**user_account_locale**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Default|string|None|True|Default locale|None|
|Reports|string|None|True|Reports locale|None|
  
**user_account**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Authentication|authentication_source|None|False|The authentication source used to authenticate the user|None|
|Email|string|None|False|The email address of the user|None|
|Enabled|boolean|None|False|Whether the user account is enabled|None|
|ID|integer|None|False|The identifier of the user|None|
|Links|[]link|None|False|List of hypermedia links to corresponding or related resources|None|
|Locale|user_account_locale|None|False|The locale and language preferences for the user|None|
|Locked|boolean|None|True|Whether the user account is locked (exceeded maximum password retry attempts)|None|
|Login|string|None|True|The login name of the user|None|
|Name|string|None|True|The full name of the user|None|
|Role|user_account_role|None|False|The privileges and role the user is assigned|None|
  
**remediation_asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Criticality Tag|string|None|False|The criticality tag assigned to the asset|None|
|Hostname|string|None|False|Primary host name (local or FQDN) of the asset|None|
|ID|integer|None|True|Identifier of the asset|None|
|IP|string|None|True|Primary IPv4 or IPv6 address of the asset|None|
|MAC|string|None|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|None|
|OS|string|None|False|Full description of the operating system of the asset|None|
|Risk Score|float|None|False|Risk score (with criticality adjustments) of the asset|None|
  
**remediation_vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVSS Score|string|None|True|The CVSS score of the vulnerability|None|
|Description|string|None|True|The description of the vulnerability|None|
|ID|string|None|True|Identifier of the vulnerability|None|
|Risk Score|integer|None|True|The risk score of the vulnerability|None|
|Severity|integer|None|True|The severity of the vulnerability|None|
|Title|string|None|True|The title of the vulnerability|None|
  
**remediation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Asset Count|integer|None|True|The number of assets that require the solution to be applied|None|
|Assets|[]remediation_asset|None|True|The assets that require the solution to be applied|None|
|Fix|string|None|False|The steps that are part of the fix this solution prescribes|None|
|Rapid7 Solution ID|string|None|True|The identifier of the solution within InsightVM/Nexpose|None|
|Risk Score|integer|None|True|The risk score that is reduced by performing the solution|None|
|Solution ID|integer|None|True|The identifier of the solution|None|
|Summary|string|None|True|Remediation summary|None|
|Vulnerabilities|[]remediation_vulnerability|None|True|The vulnerabilities that would be remediated|None|
|Vulnerability Count|integer|None|True|The number of vulnerabilities that would be remediated|None|
  
**vulnerability_solution**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Solutions|[]resources|None|False|Solutions to vulnerabilities|None|
  
**account**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Authentication Type|string|no-authentication|False|The authentication protocols available to use in SNMP v3|None|
|Community Name|string|None|False|The community name that will be used for authenticating|None|
|Database|string|None|False|The name of the database. If not specified, a default database name will be used during authentication|None|
|Domain|string|None|False|The address of the domain. This property cannot be specified unless property useWindowsAuthentication is set to true|None|
|Enumerate SIDs|string|None|False|Boolean flag instructing the scan engine to attempt to enumerate SIDs from your environment. If set to true, set the Oracle Net Listener password in property oracleListenerPassword|None|
|Notes ID Password|string|None|False|The password for the account that will be used for authenticating|None|
|NTLM Hash|string|None|False|The NTLM password hash|None|
|Oracle Listener Password|string|None|False|The Oracle Net Listener password. Used to enumerate SIDs from your environment|None|
|Password|string|None|False|The password for the account that will be used for authenticating|None|
|PEM Key|string|None|False|The PEM-format private key|None|
|Permission Evaluation|string|none|False|Elevate scan engine permissions to administrative or root access, which is necessary to obtain certain data during the scan. Defaults to "none" if not specified|None|
|Permission Elevation Password|string|None|False|The password for the account with elevated permissions. This property must not be specified when the property permissionElevation is set to either "none" or "pbrun"; otherwise the property is required|None|
|Permission Elevation Username|string|None|False|The user name for the account with elevated permissions. This property must not be specified when the property permissionElevation is set to either "none" or "pbrun"; otherwise the property is required.|None|
|Privacy Password|string|None|False|The privacy password for the account that will be used for authenticating. Is required when the property authenticationType is set to valid value other than "no-authentication" and when the privacyType is set to a valid value other than code>"no-privacy"|None|
|Privacy Type|string|no-privacy|False|The privacy protocols available to use in SNMP v3|None|
|Private Pey Password|string|None|False|The password for private key|None|
|Realm|string|None|False|The realm|None|
|Service|string|None|True|Specify the type of service to authenticate|None|
|SID|string|None|False|The name of the database. If not specified, a default database name will be used during authentication|None|
|Use Windows Authentication|boolean|None|False|Boolean flag signaling whether to connect to the database using Windows authentication. When set to true, Windows authentication is attempted; when set to false, SQL authentication is attempted|None|
|Username|string|None|False|The user name for the account that will be used for authenticating|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 8.0.13 - Resolved Snyk Vulnerability | Updated SDK to latest version (6.3.9)
* 8.0.12 - Resolved Snyk Vulnerabilities | Updated SDK to latest version (6.3.4)
* 8.0.11 - Updated the cache storage path and replaced the external function with internal implementation | Updated SDK to the latest version (6.2.6)
* 8.0.10 - Updated SDK to the latest version (6.2.5)
* 8.0.9 - Address vulnerabilities in buildpack
* 8.0.8 - Bumping requirements.txt | SDK bump to 6.2.2
* 8.0.7 - Bumping requirements.txt | SDK bump to 6.2.0
* 8.0.6 - Trigger `New Exception Request`: Updated the trigger with retry mechanism
* 8.0.5 - Initial updates for fedramp compliance | `New Exception Request`: Fixed an issue where it would not trigger in certain scenarios | Updated SDK to the latest version
* 8.0.4 - Updated SDK to the latest version | Update dependencies
* 8.0.3 - Updated `Dockerfile` permissions from `nobody` to `root`
* 8.0.2 - Updated SDK to the latest version | `Scan Completion`: Updated the query
* 8.0.1 - Updated SDK to the latest version | Fixed issue where triggers were failing due to `SSL Verify`
* 8.0.0 - Updated to the latest SDK version | Updated dependencies to the latest version | Added new connection parameter `SSL Verify`
* 7.0.2 - `Scan Completion` - Update query outputs to match schema types
* 7.0.1 - `Scan Completion` - Update query outputs to match schema names
* 7.0.0 - `Scan Completion` - Rework trigger to use a new query, resulting in a new output & removed all inputs except for `site_id` | `Top Remediations` - Update vulnerability_id to nexpose_id
* 6.2.0 - `Scan Completion` - New trigger added to retrieve vulnerability information on assets when a scan is completed | Improved error handling across all API calls
* 6.1.1 - Update actions `Update Site Excluded Targets` and `Update Site Included Targets` to prevent error on empty addresses
* 6.1.0 - Add new optional input `override_blackout` in `Scan` action
* 6.0.0 - Fix file output type for `Generate Adhoc SQL Report` | Replace custom output type `file` with `insightvm_file` for each item in the `asset` `files` output in multiple actions
* 5.1.0 - Add new action update shared credential
* 5.0.1 - Fix issue in New Scans trigger where an exception was thrown if no scan IDs were previously cached for that site
* 5.0.0 - Fix parameters type, input examples and description for `Get Asset Vulnerability Solutions`, `Get Asset Vulnerabilities`, `Get Asset Software` and `Get Asset` actions
* 4.10.0 - Add new action Tag Assets
* 4.9.2 - Add expiration date conversion to ISO8601 in Create Vulnerability Exception Submission and Update Vulnerability Exception Expiration Date actions | Fix issue with incorrect expiration date format in Get Expiring Vulnerability Exceptions action | Fix issue in List Reports action where first page of reports was not included | Fix issue in List Reports action where `found` output was returned as false even though list of reports was returned | Updated plugin SDK to latest version
* 4.9.1 - Rename the plugin with "console" as there is a new cloud based plugin for InsightVM
* 4.9.0 - Add new `size` input to List Inactive Assets | Update List Inactive Assets to return 500 results by default | Remove the usage of Maya from the plugin
* 4.8.1 - Fixed an issue where some actions were expecting bytes data and were getting strings instead
* 4.8.0 - New action Get Asset Vulnerability Solutions
* 4.7.1 - Code refactor and bug fixes
* 4.7.0 - Update Get Asset Vulnerabilities with new input and output
* 4.6.0 - Update Get Asset Vulnerabilities with new output | Fix issue with RequestParams object set function
* 4.5.0 - Update to Asset Search action to allow search result limiting and sorting
* 4.4.3 - Update to error handling and documentation around console URL in connection
* 4.4.2 - Fix issue where Update Site Included Targets could throw exception
* 4.4.1 - Add improved error handling for List Inactive Assets action
* 4.4.0 - New action Update Vulnerability Exception Expiration Date
* 4.3.0 - New action Get Expiring Vulnerability Exceptions
* 4.2.1 - Fix to make Create Asset Group description required
* 4.2.0 - New action List Inactive Assets
* 4.1.0 - New action Delete Asset
* 4.0.1 - Add the option to limit a scan to specific hosts
* 4.0.0 - Fix output for Generate Adhoc SQL Report action
* 3.6.0 - Add Get Asset Group Assets action
* 3.5.2 - Fix bug in New Vulnerability Exception Activity
* 3.5.1 - New spec and help.md format for the Extension Library
* 3.5.0 - New Actions Get Vulnerability Details, Create Vulnerability Exception Submission,  Delete Vulnerability Exception, Review Vulnerability Exception  | New Trigger New Vulnerability Exception Activity | Misc. Cleanup
* 3.4.0 - New Action Get Asset Software | Fix issue with New Scan trigger not properly caching new scan IDs
* 3.3.1 - Fix issue in Top Remediations action that causes assets without criticality tags to not be returned in asset list
* 3.3.0 - New Actions Get Asset, Get Asset Tags, Get Scan Assets, Generate AdHoc SQL Report, Top Remediations | New trigger New Scans
* 3.2.0 - New Actions Create Site, Update Site, Delete Site, Update Site Included Targets, Update Site Excluded Targets, Update Site Included Asset Groups, and Update Site Excluded Asset Groups
* 3.1.0 - New Actions Get Authentication Sources, Get Authentication Source, Get Roles, Get Role, Get Users, Get User, Create User, Update User, Update User Asset Group Access, Add User Asset Group Access, Remove User Asset Group Access, Update User Site Access, Add User Site Access, Remove User Site Access, Disable User, Enable User, Delete User, Update User Role
* 3.0.1 - Update descriptions
* 3.0.0 - Rename Action Get Vulnerabilities to Get Asset Vulnerabilities | Correct output of Scan action | New Actions Get Vulnerabilities by CVE, Get Scans, Update Scan Status, Generate Shared Secret, Get Scan Engines, Get Scan Engine, Create Scan Engine, Delete Scan Engine, Get Scan Engine Pools, Get Scan Engine Pool, Create Scan Engine Pool, Add Scan Engine Pool Engine, Remove Scan Engine Pool Engine, Delete Scan Engine Pool, Update Site Scan Engine
* 2.3.0 - New Actions Create Tag, Delete Tag, Get Tag, Get Tag Sites, Get Tag Assets, Get Tag Asset Groups, Get Tags, Remove Asset Tag, Remove Asset Group Tags, Remove Tag Asset Groups, Remove Tag Sites, Remove Tag Search Criteria, Tag Site, Tag Asset, Tag Asset Group, Update Tag Search Criteria, Asset Search, Get Sites, Get Site, Get Asset Groups, Get Asset Group, Create Asset Group, Delete Asset Group, and Update Asset Group Search Criteria
* 2.2.1 - Correct output of the Get Scan action
* 2.2.0 - New Action Get Vulnerability Affected Assets
* 2.1.0 - Add Download Report and List Reports action
* 2.0.0 - Support web server mode
* 1.0.0 - Initial plugin release

# Links

* [InsightVM](https://www.rapid7.com/products/insightvm/)

## References

* [InsightVM API 3](https://help.rapid7.com/insightvm/en-us/api/index.html)