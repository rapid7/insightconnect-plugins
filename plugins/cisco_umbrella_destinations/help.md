# Description

Cisco Umbrella Destinations allows users to manage, block, and allow network destinations based on policies within their organization

# Key Features

* Create destination lists
* Modify existing destination lists

# Requirements

* Cisco Umbrella Investigate API key and Secret key (Refer to Links section for API Key management)
* Cisco Umbrella organization ID

# Supported Product Versions

* 2023-03-29

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Cisco Umbrella Management API key|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|api_secret|credential_secret_key|None|True|Cisco Umbrella Management API secret key|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "api_secret": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions


#### Add Destination to Destination List

This action is used to add a destination to the destination list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|False|Information about domain|None|I trust this domain|None|None|
|destination|string|None|True|Title for the destination list|None|www.example.com|None|None|
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|None|None|
  
Example input:

```
{
  "comment": "I trust this domain",
  "destination": "www.example.com",
  "destinationListId": 12345678
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|dlCollection|True|Successful returned value|{'access': 'allow', 'bundleTypeId': 1, 'createdAt': '2021-12-06T16:03:49+0000', 'id': 12345678, 'isGlobal': False, 'isMspDefault': False, 'markedForDeletion': False, 'meta': {'destinationCount': 6}, 'modifiedAt': '2022-01-14T15:09:21+0000', 'name': 'ABCList', 'organizationId': 1234567, 'thirdpartyCategoryId': None}|
  
Example output:

```
{
  "success": {
    "access": "allow",
    "bundleTypeId": 1,
    "createdAt": "2021-12-06T16:03:49+0000",
    "id": 12345678,
    "isGlobal": false,
    "isMspDefault": false,
    "markedForDeletion": false,
    "meta": {
      "destinationCount": 6
    },
    "modifiedAt": "2022-01-14T15:09:21+0000",
    "name": "ABCList",
    "organizationId": 1234567,
    "thirdpartyCategoryId": null
  }
}
```

#### Delete Destinations

This action is used to delete a list of destinations from a destination list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|None|None|
|payload|string|None|True|List of destination IDs separated by a space|None|1241 67|None|None|
  
Example input:

```
{
  "destinationListId": 12345678,
  "payload": "1241 67"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|dlCollection|True|Updated destination list|{'id': 12345678, 'organizationId': 1234567, 'access': 'allow', 'isGlobal': False, 'name': 'AAAA', 'thirdpartyCategoryId': None, 'createdAt': '2021-12-06T16:03:49+0000', 'modifiedAt': '2022-01-27T16:48:52+0000', 'isMspDefault': False, 'markedForDeletion': False, 'bundleTypeId': 1, 'meta': {'destinationCount': 2}}|
  
Example output:

```
{
  "success": {
    "access": "allow",
    "bundleTypeId": 1,
    "createdAt": "2021-12-06T16:03:49+0000",
    "id": 12345678,
    "isGlobal": false,
    "isMspDefault": false,
    "markedForDeletion": false,
    "meta": {
      "destinationCount": 2
    },
    "modifiedAt": "2022-01-27T16:48:52+0000",
    "name": "AAAA",
    "organizationId": 1234567,
    "thirdpartyCategoryId": null
  }
}
```

#### Get Destinations

This action is used to get a list of destinations related to a destination list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|destinationListId|integer|None|True|Unique ID for destination list|None|1234567|None|None|
  
Example input:

```
{
  "destinationListId": 1234567
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|[]destinationsEntity|True|Successful returned value|{'Access': 'allow', 'Created At': '2018-07-23 19:36:45', 'ID': 12345, 'Is Global': True, 'Is MSP Default': True, 'Marked For Deletion': True, 'Modified At': '2018-07-23 19:36:45', 'Name': 'new list', 'Organization ID': 12345, 'Third Party Category ID': 12345}|
  
Example output:

```
{
  "success": {
    "Access": "allow",
    "Created At": "2018-07-23 19:36:45",
    "ID": 12345,
    "Is Global": true,
    "Is MSP Default": true,
    "Marked For Deletion": true,
    "Modified At": "2018-07-23 19:36:45",
    "Name": "new list",
    "Organization ID": 12345,
    "Third Party Category ID": 12345
  }
}
```

#### Create Destination List

This action is used to create a destination list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|access|string|allow|True|Allow or block access to domain|["allow", "block"]|allow|None|None|
|comment|string|None|False|Comment about the destination to be added to the newly created destination list|None|Suspicious domain|None|None|
|destination|string|None|False|Destination to be added to the newly created destination list|None|www.example.com|None|None|
|isGlobal|boolean|True|True|Boolean value indicating global state|None|True|None|None|
|name|string|None|True|Label for the destination list|None|New list|None|None|
|type|string|None|False|Type of the destination to be added to the newly created destination list|["DOMAIN", "URL", "IPV4"]|URL|None|None|
  
Example input:

```
{
  "access": "allow",
  "comment": "Suspicious domain",
  "destination": "www.example.com",
  "isGlobal": true,
  "name": "New list",
  "type": "URL"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|dlCollection|True|Successful returned value|{'access': 'allow', 'bundleTypeId': 1, 'createdAt': '2022-01-14T15:09:30+0000', 'id': 12345678, 'isGlobal': False, 'isMspDefault': False, 'markedForDeletion': False, 'meta': {'destinationCount': 2}, 'modifiedAt': '2022-01-14T15:09:30+0000', 'name': 'TESTLIST123'}|
  
Example output:

```
{
  "success": {
    "access": "allow",
    "bundleTypeId": 1,
    "createdAt": "2022-01-14T15:09:30+0000",
    "id": 12345678,
    "isGlobal": false,
    "isMspDefault": false,
    "markedForDeletion": false,
    "meta": {
      "destinationCount": 2
    },
    "modifiedAt": "2022-01-14T15:09:30+0000",
    "name": "TESTLIST123"
  }
}
```

#### Delete Destination List

This action is used to delete a destination list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|None|None|
  
Example input:

```
{
  "destinationListId": 12345678
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|dlDelete|True|Successful returned value|{}|
  
Example output:

```
{
  "success": {}
}
```

#### Filter Through All Destination Lists

This action is used to filter and Retrieve all destination lists of organization

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|access|string|None|False|Allow or block access to domain|["allow", "block"]|allow|None|None|
|isGlobal|boolean|None|False|Boolean value indicating global state|None|True|None|None|
|isMSPDefault|boolean|None|False|Boolean value indicating if MSP Default|None|True|None|None|
|markedForDeletion|boolean|None|False|Boolean value indicating if marked for deletion|None|True|None|None|
  
Example input:

```
{
  "access": "allow",
  "isGlobal": true,
  "isMSPDefault": true,
  "markedForDeletion": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]dlCollection|False|List of all destination lists|[{"access": "allow", "bundleTypeId": 1, "createdAt": "2022-01-14T15:09:30+0000", "id": 12345678, "isGlobal": False, "isMspDefault": False, "markedForDeletion": False, "meta": {"destinationCount": 2}, "modifiedAt": "2022-01-14T15:09:30+0000", "name": "TESTLIST123"}]|

Example output:

```
{
  "data": [
    {
      "access": "allow",
      "bundleTypeId": 1,
      "createdAt": "2022-01-14T15:09:30+0000",
      "id": 12345678,
      "isGlobal": false,
      "isMspDefault": false,
      "markedForDeletion": false,
      "meta": {
        "destinationCount": 2
      },
      "modifiedAt": "2022-01-14T15:09:30+0000",
      "name": "TESTLIST123"
    }
  ]
}
```

#### Get Destination List

This action is used to get a destination list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|None|None|
  
Example input:

```
{
  "destinationListId": 12345678
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|destinationList|True|Successful returned value|{'access': 'allow', 'bundleTypeId': 1, 'createdAt': '2021-12-06T16:03:49+0000', 'id': 12345678, 'isGlobal': False, 'isMspDefault': False, 'markedForDeletion': False, 'meta': {'destinationCount': 4}, 'modifiedAt': '2022-01-14T15:09:24+0000', 'name': 'ABCList', 'organizationId': 1234567, 'thirdpartyCategoryId': None}|
  
Example output:

```
{
  "success": {
    "access": "allow",
    "bundleTypeId": 1,
    "createdAt": "2021-12-06T16:03:49+0000",
    "id": 12345678,
    "isGlobal": false,
    "isMspDefault": false,
    "markedForDeletion": false,
    "meta": {
      "destinationCount": 4
    },
    "modifiedAt": "2022-01-14T15:09:24+0000",
    "name": "ABCList",
    "organizationId": 1234567,
    "thirdpartyCategoryId": null
  }
}
```

#### Get All Destination Lists

This action is used to retrieve all destination lists of organization

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]dlCollection|False|List of all destination lists|[{"access": "allow", "bundleTypeId": 1, "createdAt": "2022-01-14T15:09:30+0000", "id": 12345678, "isGlobal": False, "isMspDefault": False, "markedForDeletion": False, "meta": {"destinationCount": 2}, "modifiedAt": "2022-01-14T15:09:30+0000", "name": "TESTLIST123"}]|

Example output:

```
{
  "data": [
    {
      "access": "allow",
      "bundleTypeId": 1,
      "createdAt": "2022-01-14T15:09:30+0000",
      "id": 12345678,
      "isGlobal": false,
      "isMspDefault": false,
      "markedForDeletion": false,
      "meta": {
        "destinationCount": 2
      },
      "modifiedAt": "2022-01-14T15:09:30+0000",
      "name": "TESTLIST123"
    }
  ]
}
```

#### Get Destination List by Name

This action is used to get destination list by name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Title for the destination list|None|new list|None|None|
  
Example input:

```
{
  "name": "new list"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|[]destinationList|True|Successful returned value|[{"access": "allow", "bundleTypeId": 1, "createdAt": "2021-12-06T16:03:49+0000", "id": 12345678, "isGlobal": False, "isMspDefault": False, "markedForDeletion": False, "meta": {"destinationCount": 4}, "modifiedAt": "2022-01-14T15:09:24+0000", "name": "ABCList", "organizationId": 1234567, "thirdpartyCategoryId": None}]|

Example output:

```
{
  "success": [
    {
      "access": "allow",
      "bundleTypeId": 1,
      "createdAt": "2021-12-06T16:03:49+0000",
      "id": 12345678,
      "isGlobal": false,
      "isMspDefault": false,
      "markedForDeletion": false,
      "meta": {
        "destinationCount": 4
      },
      "modifiedAt": "2022-01-14T15:09:24+0000",
      "name": "ABCList",
      "organizationId": 1234567,
      "thirdpartyCategoryId": null
    }
  ]
}
```

#### Rename Destination List

This action is used to rename a destination list

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|None|None|
|name|string|None|True|Title for the destination list|None|New list|None|None|
  
Example input:

```
{
  "destinationListId": 12345678,
  "name": "New list"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|dlCollection|True|Successful returned value|{'access': 'allow', 'bundleTypeId': 1, 'createdAt': '2021-12-06T16:03:49+0000', 'id': 12345678, 'isGlobal': False, 'isMspDefault': False, 'markedForDeletion': False, 'meta': {'destinationCount': 6}, 'modifiedAt': '2022-01-14T15:09:21+0000', 'name': 'ABCList', 'organizationId': 1234567, 'thirdpartyCategoryId': None}|
  
Example output:

```
{
  "success": {
    "access": "allow",
    "bundleTypeId": 1,
    "createdAt": "2021-12-06T16:03:49+0000",
    "id": 12345678,
    "isGlobal": false,
    "isMspDefault": false,
    "markedForDeletion": false,
    "meta": {
      "destinationCount": 6
    },
    "modifiedAt": "2022-01-14T15:09:21+0000",
    "name": "ABCList",
    "organizationId": 1234567,
    "thirdpartyCategoryId": null
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**meta**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|destinationCount|integer|None|False|Total number of destinations in a destination list|None|
|domainCount|integer|None|False|Total number of domains in a destination list|None|
|ipv4Count|integer|None|False|Total number of IPs in a destination list|None|
|urlCount|integer|None|False|Total number of URLs in a destination list|None|
  
**dlCollection**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access|string|None|False|Allow or block access to domain|allow|
|Created At|integer|None|False|The unix UTC timestamp in milliseconds for creation of the destination list|1643385816|
|ID|integer|None|False|Unique ID of the destination list|None|
|Is Global|boolean|None|False|Boolean value indicating global state|True|
|Is MSP Default|boolean|None|False|Whether or not MSP is default|False|
|Marked for Deletion|boolean|None|False|Whether or not destination list is marked for deletion|False|
|Metadata|meta|None|False|Secondary information|None|
|Modified At|integer|None|False|The unix UTC timestamp in milliseconds for modification of the destination list|1643385816|
|Name|string|None|False|Title for the destination list|New list|
|Organization ID|integer|None|False|ID of organization|1234567|
|Third Party Category ID|integer|None|False|ID, if any, for third parties|1|
  
**destinationList**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access|string|None|False|Allow or block access to domain|allow|
|Created At|integer|None|False|The unix UTC timestamp in milliseconds for creation of the destination list|1643385816|
|ID|integer|None|False|Unique ID of the destination list|None|
|Is Global|boolean|None|False|Boolean value indicating global state|True|
|Is MSP Default|boolean|None|False|Whether or not MSP is default|False|
|Marked for Deletion|boolean|None|False|Whether or not destination list is marked for deletion|False|
|Modified At|integer|None|False|The unix UTC timestamp in milliseconds for modification of the destination list|1643385816|
|Name|string|None|False|Title for the destination list|New list|
|Third Party Category ID|integer|None|False|ID, if any, for third parties|1|
  
**destinationsEntity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|False|Information about domain|Suspicious domain|
|Created At|date|None|False|Timestamp for creation of entity|2018-07-23 19:36:45|
|Destination|string|None|False|Destination can be DOMAIN, URL or IP|www.example.com|
|ID|string|None|False|Unique ID of the destination|1234|
|Type|string|None|False|Type can be DOMAIN, URL or IPV4|Domain|
  
**dlDelete**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Delete|object|None|False|Delete|None|


## Troubleshooting

Version 3.2.0 uses v2 of the Cisco Umbrella API. The API endpoint for the destinations functionality  is via 
api.umbrella.com/policies/v2/ . To interact with this version of the API, use the reference in the Links session,
to ensure an appropriate key and permissions is used for connecting (not a legacy key as this will not work with v2 of the API).

# Version History

* 4.1.0 - `dlCreate` - Changed some inputs to required
* 4.0.0 - Updated to use V2 of the Cisco Umbrella API api.umbrella.com/policies/v2 | Updated to use OAuth2 client credentials flow
* 3.1.0 - Added dlGetByName and dlFilterAll action | Improved error handling data output
* 3.0.0 - Updated output for 'typeOf' to reflect update to Cisco API
* 2.0.0 - Updated output for dAdd & dDelete - Removed data element in the response
* 1.0.0 - Initial plugin includes create and modify destination lists

# Links

* [Cisco Umbrella](https://umbrella.cisco.com/)

## References

* [Cisco Umbrella API reference](https://developer.cisco.com/docs/cloud-security/#!api-reference-overview)
* [Cisco Umbrella Destinations Docs](https://developer.cisco.com/docs/cloud-security/#!api-reference-policies-overview)
* [Creating/Refreshing/Deleting Umbrella API Keys](https://developer.cisco.com/docs/cloud-security/#!authentication)