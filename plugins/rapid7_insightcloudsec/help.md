# Description

InsightCloudSec by Rapid7 (formerly DivvyCloud) is a Cloud-Native Security Platform that provides real-time analysis and automated remediation for continuous security and compliance for your multi-cloud environment

# Key Features

* Create and remove an exemption
* Detach policy
* Get account details
* Get resource details
* List resource tags
* Run a bot on demand
* Switch organization

# Requirements

* InsightCloudSec API key

# Supported Product Versions

* 22.10.19

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|apiKey|credential_secret_key|None|True|InsightCloudSec API key|None|02699626f388ed830012e5b787640e71c56d42d8|
|sslVerify|boolean|True|True|SSL verify|None|True|
|url|string|None|True|InsightCloudSec URL|None|https://example.com|

Example input:

```
{
  "apiKey": "3395856ce81f2b7382dee72602f798b642f14140",
  "sslVerify": true,
  "url": "https://example.com"
}
```

## Technical Details

### Actions

#### Remove Exemption

This action is used to delete exemptions for provided IDs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|exemptionIds|[]integer|None|True|List of exemption IDs to delete|None|[111, 222]|

Example input:

```
{
  "exemptionIds": [
    111,
    222
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the action was successful|

Example output:

```
{
  "success": True
}
```

#### Create Exemption

This action is used to create an exemption.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|approver|string|None|True|The exemption approver|None|https://example.com|
|expirationDate|date|None|False|Date the exemption ends, e.g. 2022-10-21T00:00:00Z. If none is provided, the default is no expiration|None|2022-10-21T12:00:00+02:00|
|insightId|integer|None|True|ID for the Insight associated with the exemption|None|12345|
|insightSource|string|None|True|Source for the Insight associated with the exemption|['backoffice', 'custom']|backoffice|
|notes|string|None|False|Any notes or documentation for the exemption|None|example note|
|resourceIds|[]string|None|True|List of IDs for the resources to be exempted from the given Insight|None|["storagecontainer:123:us-east-1:123456789:"]|
|resourceType|string|None|True|The type of resource being exempted|None|storagecontainer|
|startDate|date|None|True|Date the exemption begins, e.g. 2022-10-20T00:00:00Z|None|2022-10-20T12:00:00+02:00|

Example input:

```
{
  "approver": "user@example.com",
  "expirationDate": "2022-10-21T12:00:00+02:00",
  "insightId": 12345,
  "insightSource": "backoffice",
  "notes": "example note",
  "resourceIds": [
    "storagecontainer:123:us-east-1:123456789:"
  ],
  "resourceType": "storagecontainer",
  "startDate": "2022-10-20T12:00:00+02:00"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|exemption|[]exemption|False|Information about a created exemption|

Example output:

```
{
  "exemption": [
    {
      "approver": "user@example.com",
      "createDate": "2022-10-02T13:17:16",
      "creatorId": 123,
      "enabled": true,
      "exemptionId": 100,
      "expirationDate": "2022-10-04T00:00:00",
      "insightId": 12345,
      "insightSource": "backoffice",
      "notes": "example note",
      "organizationId": 1,
      "resourceId": "storagecontainer:123:us-east-1:123456789:",
      "resourceType": "storagecontainer",
      "startDate": "2022-10-03T00:00:00"
    }
  ]
}
```

#### Detach Policy

This action is used to detach a policy from a service user, group, or role.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|policyResourceId|string|None|True|ID of the policy|None|servicepolicy:123:1234567890:|
|resourceId|string|None|True|ID of the service user, group, or role|None|servicegroup:123:1234567890:|

Example input:

```
{
  "policyResourceId": "servicepolicy:123:1234567890:",
  "resourceId": "servicegroup:123:1234567890:"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the action was successful|

Example output:

```
{
  "success": True
}
```

#### Switch Organization

This action is used to change the organization for which all future API requests will be made.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|organizationName|string|None|True|Name of the organization|None|Example Organization|

Example input:

```
{
  "organizationName": "Example Organization"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the action was successful|

Example output:

```
{
  "success": True
}
```

#### List Resource Tags

This action is used to list resource tags based on provided resource ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resourceId|string|None|True|ID of the resource|None|instance:123:example:i-1234567890:|

Example input:

```
{
  "resourceId": "instance:123:example:i-1234567890:"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|resourceTags|[]resourceTag|False|Resource tags for the provided ID|

Example output:

```
{
  "resourceTags": [
    {
      "key": "tag1",
      "value": "test_tag_1"
    },
    {
      "key": "tag2",
      "value": "test_tag_2"
    },
    {
      "key": "tag3",
      "value": "test_tag_3"
    }
  ]
}
```

#### Get Resource Details

This action is used to get all of the details about a resource based on provided resource ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|resourceId|string|None|True|ID of the resource|None|serviceuser:1:ABC1234567890:|

Example input:

```
{
  "resourceId": "serviceuser:1:ABC1234567890:"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|resourceDetails|resourceDetails|False|Information about the resource for the provided ID|

Example output:

```
{
  "resourceDetails": {
    "dependencies": {
      "serviceaccesskey": [
        {
          "id": "ABC123456790",
          "name": "ABC123456790",
          "resourceId": "serviceaccesskey:1:ABC123456790:",
          "type": "serviceaccesskey"
        }
      ],
      "servicepolicy": [
        {
          "id": "ABC0987654321",
          "name": "Example-Policy",
          "resourceId": "servicepolicy:1:ABC0987654321:",
          "type": "servicepolicy"
        }
      ]
    },
    "details": {
      "resourceType": "serviceuser",
      "serviceuser": {
        "actionCount": 0,
        "activeApiKeys": 1,
        "ageInDays": 10,
        "common": {
          "account": "Test",
          "accountId": "123456789098",
          "accountStatus": "DEFAULT",
          "cloud": "AWS",
          "creationTimestamp": "2022-10-20 11:16:57",
          "directLink": "https://example.com",
          "discoveredTimestamp": "2022-10-20 11:33:49",
          "documents": {},
          "lastHarvestedTimestamp": "2022-10-21T08:02:52",
          "modifiedTimestamp": "2022-10-21 06:03:03",
          "namespaceId": "arn:aws:iam::123456789098:user/Example-User",
          "noncompliance": [],
          "organizationServiceId": 1,
          "properties": {
            "propertyList": []
          },
          "resourceId": "serviceuser:1:ABC1234567890:",
          "resourceName": "Example-User",
          "resourceType": "serviceuser"
        },
        "createDate": "2022-10-20 11:16:57",
        "disabled": false,
        "inactiveApiKeys": 0,
        "inlinePolicies": 0,
        "lastActivity": "2022-10-21 05:46:00",
        "loginProfile": false,
        "managedPolicyCount": 0,
        "passwordLastChanged": "None",
        "passwordLastUsed": "None",
        "path": "/",
        "policyCount": 1,
        "serviceCount": 0,
        "twoFactorEnabled": false,
        "userId": "ABC1234567890",
        "userName": "Example-User",
        "wildcardServiceCount": 0
      }
    }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### accountDetails

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account ID|string|False|ID of the cloud account|
|Cloud Type ID|string|False|ID of the cloud type|
|Joined Timestamp|string|False|When the account was joined|
|Name|string|False|Name of the account|
|Payer Account ID|string|False|ID of the payer account|
|Resource ID|string|False|Resource ID for the account|
|Status|string|False|Status of the account|

#### exemption

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account|string|False|Name of the account|
|Account ID|integer|False|ID of the account|
|Approver|string|False|The exemption approver|
|Bot ID|string|False|ID of the bot|
|Bot Name|string|False|Name of the bot|
|Cloud Type ID|integer|False|ID of the cloud type|
|Create Date|string|False|When the exemption was created|
|Creator ID|integer|False|ID of the creator of the exemption|
|Creator Name|string|False|Name of the creator of the exemption|
|Enabled|boolean|False|Whether the exemption is enabled|
|Exemption ID|integer|False|ID of the exemption|
|Expiration Date|string|False|When the exemption expires|
|Insight ID|integer|False|ID of the Insight associated with the exemption|
|Insight Name|string|False|Name of the Insight associated with the exemption|
|Insight Source|string|False|Source for the Insight associated with the exemption|
|Notes|string|False|Notes|
|Organization ID|integer|False|ID of the organization|
|Provider ID|integer|False|ID of the provider|
|Resource ID|string|False|ID of the resource that was exempted|
|ResourceIds|[]string|False|List of resource IDs that have been exempted from the given Insight|
|Resource Name|string|False|Name of the resource|
|Resource Type|string|False|Type of the resource|
|Resource Type Label|string|False|Label of the resource type|
|Start Date|string|False|When the exemption starts|

#### resourceDetails

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Dependencies|object|False|Dependencies for the provided resource ID|
|Details|object|False|Details for the provided resource ID|
|Related Resources|object|False|Related resources with the provided resource ID|

#### resourceTag

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Key|string|False|Key of the resource tag|
|Value|string|False|Value of the resource tag|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - Enable plugin to run in cloud
* 1.0.0 - Initial plugin | Add Get Account Details, Get Resource Details, List Resource Tags, Create Exemption, Remove Exemption, Detach Policy, Run Bot on Demand and Switch Organization actions

# Links

## References

* [Rapid7 InsightCloudSec](https://www.rapid7.com/products/insightcloudsec/)

