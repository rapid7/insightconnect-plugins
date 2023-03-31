# Description

Cisco Umbrella Destinations allows users to manage, block, and allow network destinations based on policies within their organization.

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Cisco Umbrella Management API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|api_secret|credential_secret_key|None|True|Cisco Umbrella Management API secret key|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "api_secret": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions

#### Filter Through All Destination Lists

This action is used to filter and Retrieve all destination lists of organization.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access|string|None|False|Allow or block access to domain|['allow', 'block']|allow|
|isGlobal|boolean|None|False|Boolean value indicating global state|None|True|
|isMSPDefault|boolean|None|False|Boolean value indicating if MSP Default|None|True|
|markedForDeletion|boolean|None|False|Boolean value indicating if marked for deletion|None|True|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]dlCollection|False|List of all destination lists|

Example output:

```
{
    "access": "allow",
    "bundleTypeId": 1,
    "createdAt": "2021-12-06T16:03:49+0000",
    "id": 15609742,
    "isGlobal": false,
    "isMspDefault": false,
    "markedForDeletion": false,
    "meta": {
      "applicationCount": 0,
      "destinationCount": 4,
      "domainCount": 3,
      "ipv4Count": 1,
      "urlCount": 0
    },
    "modifiedAt": "2022-01-14T15:09:24+0000",
    "name": "ABCList",
    "organizationId": 2372338,
    "thirdpartyCategoryId": null
}
```

#### Add Destination to Destination List

This action is used to add a destination to the destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Information about domain|None|I trust this domain|
|destination|string|None|True|Title for the destination list|None|www.example.com|
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|

Example input:

```
{
  "comment": "I trust this domain",
  "destination": "www.example.com",
  "destinationListId": 12345678
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|dlCollection|True|Successful returned value|

Example output:

```
{
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
```

#### Delete Destinations

This action is used to delete a list of destinations from a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|
|payload|string|None|True|List of destination IDs separated by a space|None|1241 67|

Example input:

```
{
  "destinationListId": 12345678,
  "payload": "1241 67"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|dlCollection|True|Updated destination list|

Example output:

```
{
    "id": 12345678,
    "organizationId": 1234567,
    "access": "allow",
    "isGlobal": false,
    "name": "AAAA",
    "thirdpartyCategoryId": null,
    "createdAt": "2021-12-06T16:03:49+0000",
    "modifiedAt": "2022-01-27T16:48:52+0000",
    "isMspDefault": false,
    "markedForDeletion": false,
    "bundleTypeId": 1,
    "meta": {
        "destinationCount": 2
    }
}
```

#### Get Destinations

This action is used to get a list of destinations related to a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|1234567|

Example input:

```
{
  "destinationListId": 1234567
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|[]destinationsEntity|True|Successful returned value|

Example output:

```
[
    {
        "id": "123",
        "destination": "www.example.com",
        "type": "domain",
        "comment": null,
        "createdAt": "2022-01-27 16:10:37"
    },
    {
        "id": "1234",
        "destination": "8.8.8.8",
        "type": "ipv4",
        "comment": "Sample comment",
        "createdAt": "2021-12-16 13:18:57"
    }
]
```

#### Get Destination List by Name

Get destination list by name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Title for the destination list|None|new list|

Example input:

```
{
  "name": "new list"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|[]destinationList|True|Successful returned value|

Example input:

```
{
  "name": "new list"
}
```

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
| success | destinationList | None  | True   | Successful returned value | None | None  |

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

This action is used to create a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access|string|None|False|Allow or block access to domain|['allow', 'block']|allow|
|comment|string|None|False|Information about the destination|None|Suspicious domain|
|destination|string|None|False|Enter the destination here|None|www.example.com|
|isGlobal|boolean|None|False|Boolean value indicating global state|None|True|
|name|string|None|False|Label for the destination list|None|New list|
|type|string|None|False|Can be DOMAIN, URL or IPV4|['DOMAIN', 'URL', 'IPV4']|URL|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|dlCollection|True|Successful returned value|

Example output:

```
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
```

#### Delete Destination List

This action is used to delete a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|

Example input:

```
{
  "destinationListId": 12345678
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|dlDelete|True|Successful returned value|

Example output:

```
[]
```

#### Get Destination List

This action is used to get a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|

Example input:

```
{
  "destinationListId": 12345678
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|destinationList|True|Successful returned value|

Example output:

```
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
```

#### Get All Destination Lists

This action is used to retrieve all destination lists of organization.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]dlCollection|False|List of all destination lists|

Example output:

```
{
    "access": "allow",
    "bundleTypeId": 1,
    "createdAt": "2021-12-06T16:03:49+0000",
    "id": 15609742,
    "isGlobal": false,
    "isMspDefault": false,
    "markedForDeletion": false,
    "meta": {
      "applicationCount": 0,
      "destinationCount": 4,
      "domainCount": 3,
      "ipv4Count": 1,
      "urlCount": 0
    },
    "modifiedAt": "2022-01-14T15:09:24+0000",
    "name": "ABCList",
    "organizationId": 2372338,
    "thirdpartyCategoryId": null
}
```

#### Rename Destination List

This action is used to rename a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|destinationListId|integer|None|True|Unique ID for destination list|None|12345678|
|name|string|None|True|Title for the destination list|None|New list|

Example input:

```
{
  "destinationListId": 12345678,
  "name": "New list"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|dlCollection|True|Successful returned value|

Example output:

```
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
  "modifiedAt": "2022-01-14T15:09:41+0000",
  "name": "NEW NAME",
  "organizationId": 1234567,
  "thirdpartyCategoryId": null
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### destinationList

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access|string|False|Allow or block access to domain|
|Created At|date|False|Timestamp for creation of the destination list|
|ID|integer|False|Unique ID of the destination list.|
|Is Global|boolean|False|Boolean value indicating global state|
|Is MSP Default|boolean|False|Whether or not MSP is default|
|Label|string|False|Title for the destination list|
|Marked For Deletion|boolean|False|Whether or not destination list is marked for deletion|
|Modified At|date|False|Timestamp for modification of the destination list|
|Organization ID|integer|False|ID of organization|
|Third Party Category Id|integer|False|ID, if any, for third parties|

#### destinations

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comment|string|False|Information about the destination|
|Label|string|True|Destination name can be domain, URL or IP|
|Type|string|True|Can be DOMAIN, URL, IPV4|

#### destinationsEntity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comment|string|False|Information about domain|
|Created At|date|False|Timestamp for creation of entity|
|Destination|string|False|Destination can be DOMAIN, URL or IP|
|ID|string|False|Unique ID of the destination|
|Type|string|False|Type can be DOMAIN, URL or IPV4|

#### dlCollection

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access|string|False|Allow or block access to domain|
|Created At|date|False|Timestamp for creation of the destination list|
|ID|integer|False|Unique ID of the destination list|
|Is Global|boolean|False|Boolean value indicating global state|
|Is MSP Default|boolean|False|Whether or not MSP is default|
|Label|string|False|Title for the destination list|
|Marked For Deletion|boolean|False|Whether or not destination list is marked for deletion|
|Meta Data|meta|False|Secondary information|
|Modified At|date|False|Timestamp for modification of the destination list|
|Organization ID|integer|False|ID of organization|
|Third Party Category ID|integer|False|ID, if any, for third parties|

#### dlDelete

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Delete|object|False|Delete|

#### meta

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DestinationCount|integer|False|Total number of destinations in a destination list|
|DomainCount|integer|False|Total number of domains in a destination list|
|Ipv4Count|integer|False|Total number of IP's in a destination list|
|UrlCount|integer|False|Total number of URLs in a destination list|

## Troubleshooting

Version 3.2.0 uses v2 of the Cisco Umbrella API. The API endpoint for the destinations functionality  is via 
api.umbrella.com/policies/v2/ . To interact with this version of the API, use the reference in the Links session,
to ensure an appropriate key and permissions is used for connecting (not a legacy key as this will not work with v2 of the API).

# Version History

* 4.0.0 - Updated to use V2 of the Cisco Umbrella API api.umbrella.com/policies/v2 | Updated to use OAuth2 client credentials flow
* 3.1.0 - Added dlGetByName and dlFilterAll action | Improved error handling data output
* 3.0.0 - Updated output for 'typeOf' to reflect update to Cisco API
* 2.0.0 - Updated output for dAdd & dDelete - Removed data element in the response
* 1.0.0 - Initial plugin includes create and modify destination lists

# Links

* [Cisco Umbrella](https://umbrella.cisco.com/)

## References

* [Cisco Umbrella](https://umbrella.cisco.com/)
* [Cisco Umbrella API reference](https://developer.cisco.com/docs/cloud-security/#!api-reference-overview)
* [Cisco Umbrella Destinations Docs](https://developer.cisco.com/docs/cloud-security/#!api-reference-policies-overview)
* [Creating/Refreshing/Deleting Umbrella API Keys](https://developer.cisco.com/docs/cloud-security/#!authentication)