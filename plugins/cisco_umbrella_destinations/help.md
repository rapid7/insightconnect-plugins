# Description

Cisco Umbrella Destinations allows users to manage, block, and allow network destinations based on policies within their organization

# Key Features

* Create destination lists
* Modify existing destination lists

# Requirements

* API Key and Secret Key from Cisco Umbrella 
* Cisco Umbrella organization ID

# Supported Product Versions

* All as of 1/25/2022

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Cisco Umbrella Management API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|api_secret|credential_secret_key|None|True|Cisco Umbrella Management API secret key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|organization_id|integer|None|True|ID for organization|None|1234567|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "api_secret": "9de5069c5afe602b2ea0a04b66beb2c0",
  "organization_id": 1234567
}
```

## Technical Details

### Actions

#### Add Destinations to Destination List

This action is used to add a list of destinations to a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Information about domain|None|I trust this domain|
|destination|string|None|True|Title for the destination list|None|https://example.com|
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
|payload|[]integer|None|True|List of destinations|None|1241, 67|

Example input:

```
{
  "destinationListId": 12345678,
  "payload": "1241, 67"
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
|success|destinationsEntity|True|Successful returned value|

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

#### Create Destination List

This action is used to create a destination list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access|string|None|False|Can be allow or block|None|allow|
|destinations|[]destinations|None|False|Values to add to new list|None|Destination, comment|
|isGlobal|boolean|None|False|Boolean value indicating global state|None|True|
|label|string|None|False|Title for the destination list|None|New list|

Example input:

```
{
  "access": "allow",
  "isGlobal": false,
  "label": "TESTLIST123",
  "destinations": [
    {
      "comment": "I don't like this one",
      "destination": "8.8.8.8",
      "type": "IPV4"
    },
    {
      "comment": "Not this one either",
      "destination": "www.example.com",
      "type": "DOMAIN"
    }
  ]
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
|success|dlCollection|True|Successful returned value|

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
|label|string|None|True|Title for the destination list|None|New list|

Example input:

```
{
  "destinationListId": 12345678,
  "label": "NEW NAME"
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
|Access|string|False|Can be allow or block|
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
|Access|string|False|Can be allow or block|
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

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Umbrella](https://umbrella.cisco.com/)
* [Cisco Umbrella Destinations Docs](https://developer.cisco.com/docs/cloud-security/#!destination-lists-introduction-overview)

