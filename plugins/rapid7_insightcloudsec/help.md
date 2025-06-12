# Description

InsightCloudSec by Rapid7 (formerly DivvyCloud) is a Cloud-Native Security Platform that provides real-time analysis and automated remediation for continuous security and compliance for your multi-cloud environment

# Key Features

* Create and remove an exemption
* Detach policy
* Get resource details
* Get resource id
* List resource tags
* Switch organization
* List Clouds

# Requirements

* InsightCloudSec API key

# Supported Product Versions

* 22.10.19

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|apiKey|credential_secret_key|None|True|InsightCloudSec API key|None|3395856ce81f2b7382dee72602f798b642f14140|None|None|
|sslVerify|boolean|True|True|SSL verify|None|True|None|None|
|url|string|None|True|InsightCloudSec URL|None|https://example.com|None|None|

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


#### Create Exemption

This action is used to create an exemption

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|approver|string|None|True|The exemption approver|None|user@example.com|None|None|
|expirationDate|date|None|False|Date the exemption ends, e.g. 2022-10-21T00:00:00Z. If none is provided, the default is no expiration|None|2022-10-21 12:00:00+02:00|None|None|
|insightId|integer|None|True|ID for the Insight associated with the exemption|None|12345|None|None|
|insightSource|string|None|True|Source for the Insight associated with the exemption|["backoffice", "custom"]|backoffice|None|None|
|notes|string|None|False|Any notes or documentation for the exemption|None|example note|None|None|
|resourceIds|[]string|None|True|List of IDs for the resources to be exempted from the given Insight|None|["storagecontainer:123:us-east-1:123456789:"]|None|None|
|resourceType|string|None|True|The type of resource being exempted|None|storagecontainer|None|None|
|startDate|date|None|True|Date the exemption begins, e.g. 2022-10-20T00:00:00Z|None|2022-10-20 12:00:00+02:00|None|None|
  
Example input:

```
{
  "approver": "user@example.com",
  "expirationDate": "2022-10-21 12:00:00+02:00",
  "insightId": 12345,
  "insightSource": "backoffice",
  "notes": "example note",
  "resourceIds": [
    "storagecontainer:123:us-east-1:123456789:"
  ],
  "resourceType": "storagecontainer",
  "startDate": "2022-10-20 12:00:00+02:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|exemption|[]exemption|False|Information about a created exemption|[{"approver": "user@example.com", "createDate": "2022-10-20 12:00:00+02:00", "creatorId": 123, "enabled": True, "exemptionId": 100, "expirationDate": "2022-10-20 12:00:00+02:00", "insightId": 12345, "insightSource": "backoffice", "notes": "example note", "organizationId": 1, "resourceId": "storagecontainer:123:us-east-1:123456789:", "resourceType": "storagecontainer", "startDate": "2022-10-20 12:00:00+02:00"}]|
  
Example output:

```
{
  "exemption": [
    {
      "approver": "user@example.com",
      "createDate": "2022-10-20 12:00:00+02:00",
      "creatorId": 123,
      "enabled": true,
      "exemptionId": 100,
      "expirationDate": "2022-10-20 12:00:00+02:00",
      "insightId": 12345,
      "insightSource": "backoffice",
      "notes": "example note",
      "organizationId": 1,
      "resourceId": "storagecontainer:123:us-east-1:123456789:",
      "resourceType": "storagecontainer",
      "startDate": "2022-10-20 12:00:00+02:00"
    }
  ]
}
```

#### Detach Policy

This action is used to detach a policy from a service user, group, or role

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|policyResourceId|string|None|True|ID of the policy|None|servicepolicy:123:1234567890:|None|None|
|resourceId|string|None|True|ID of the service user, group, or role|None|servicegroup:123:1234567890:|None|None|
  
Example input:

```
{
  "policyResourceId": "servicepolicy:123:1234567890:",
  "resourceId": "servicegroup:123:1234567890:"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Resource Details

This action is used to get all of the details about a resource based on provided resource ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceId|string|None|True|ID of the resource|None|serviceuser:1:ABC1234567890:|None|None|
  
Example input:

```
{
  "resourceId": "serviceuser:1:ABC1234567890:"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|resourceDetails|resourceDetails|False|Information about the resource for the provided ID|{'dependencies': {'serviceaccesskey': [{'id': 'ABC123456790', 'name': 'ABC123456790', 'resourceId': 'serviceaccesskey:1:ABC123456790:', 'type': 'serviceaccesskey'}], 'servicepolicy': [{'id': 'ABC0987654321', 'name': 'Example-Policy', 'resourceId': 'servicepolicy:1:ABC0987654321:', 'type': 'servicepolicy'}]}, 'details': {'resourceType': 'serviceuser', 'serviceuser': {'actionCount': 0, 'activeApiKeys': 1, 'ageInDays': 10, 'common': {'account': 'Test', 'accountId': '123456789098', 'accountStatus': 'DEFAULT', 'cloud': 'AWS', 'creationTimestamp': '2022-10-20 11:16:57', 'directLink': 'https://example.com', 'discoveredTimestamp': '2022-10-20 11:33:49', 'documents': {}, 'lastHarvestedTimestamp': '2022-10-21T08:02:52', 'modifiedTimestamp': '2022-10-21 06:03:03', 'namespaceId': 'arn:aws:iam::123456789098:user/Example-User', 'noncompliance': [], 'organizationServiceId': 1, 'properties': {'propertyList': []}, 'resourceId': 'serviceuser:1:ABC1234567890:', 'resourceName': 'Example-User', 'resourceType': 'serviceuser'}, 'createDate': '2022-10-20 11:16:57', 'disabled': False, 'inactiveApiKeys': 0, 'inlinePolicies': 0, 'lastActivity': '2022-10-21 05:46:00', 'loginProfile': False, 'managedPolicyCount': 0, 'passwordLastChanged': 'None', 'passwordLastUsed': 'None', 'path': '/', 'policyCount': 1, 'serviceCount': 0, 'twoFactorEnabled': False, 'userId': 'ABC1234567890', 'userName': 'Example-User', 'wildcardServiceCount': 0}}}|
  
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

#### Get Resource ID

This action is used to gets a InsightCloudSec resource ID from a given search string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|limit|integer|None|False|The maximum number of resources returned if resources match the provided criteria. The value can be between 1 and 1000|None|0|None|None|
|offset|integer|None|False|The number of entries to skip over before returning anything|None|0|None|None|
|search_string|string|None|True|Partial or full literal string to search for. f.e. you could search for an instance ID, image ID, or resource name|None|i-1234567890|None|None|
  
Example input:

```
{
  "limit": 0,
  "offset": 0,
  "search_string": "i-1234567890"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|resources|[]resource|False|List of the resource IDs|[{"resource_id": "instance:******:ap-northeast-1:*******************:", "resource_type": "instance", "provider_id": "*******************", "name": "my-instance-name", "account_id": "************", "cloud_type_id": "AWS", "account": "my-account-name"}, {"resource_id": "instance:******:ap-northeast-1:*******************:", "resource_type": "instance", "provider_id": "*******************", "name": "my-instance-name", "account_id": "************", "cloud_type_id": "AWS", "account": "my-account-name"}]|
|totalCount|integer|False|Number of resources retrieved|2|
  
Example output:

```
{
  "resources": [
    {
      "account": "my-account-name",
      "account_id": "************",
      "cloud_type_id": "AWS",
      "name": "my-instance-name",
      "provider_id": "*******************",
      "resource_id": "instance:******:ap-northeast-1:*******************:",
      "resource_type": "instance"
    },
    {
      "account": "my-account-name",
      "account_id": "************",
      "cloud_type_id": "AWS",
      "name": "my-instance-name",
      "provider_id": "*******************",
      "resource_id": "instance:******:ap-northeast-1:*******************:",
      "resource_type": "instance"
    }
  ],
  "totalCount": 2
}
```

#### List Clouds

This action is used to retrieve a list of available configured clouds. This supports filtering and sorting to refine 
the results based on specified criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|advanced_search|boolean|None|False|Toggle on whether to enable advanced search functionality or not|None|False|None|None|
|badge_filter_operator|string|None|False|Determines whether the output should contain all badges in `badges` (`AND`), or one of the badges in the list (`OR`)|["OR", "AND"]|AND|None|None|
|badges|[]badges|None|False|Specifies the badges used to filter cloud accounts based on key-value pairs|None|[{"key": "environment", "value": "production"}]|None|None|
|empty_badges|boolean|None|False|Whether or not to filter on cloud accounts which have zero badges (cloud accounts only)|None|False|None|None|
|exclusion_badges|[]badges|None|False|Specifies the badges to exclude when filtering cloud accounts based on key-value pairs|None|[{"key": "region", "value": "us-east-1"}]|None|None|
|filters|[]filters|None|False|Filter Clouds based on `field_name`, `filter_type`, `filter_value` and `filter_list_value`|None|[{"field_name": "account_id", "filter_type": "EXACT", "filter_value": "463792522299"}]|None|None|
|limit|integer|None|False|The limit on the amount of clouds you wish to receive|None|3|None|None|
|offset|integer|None|False|Offset for cloud results, specifying the starting point for clouds returned|None|1|None|None|
|order_by|string|None|False|Sort the output based on `field` and `order`. Specified by field name followed by a space then 'ASC' or 'DESC'|None|name ASC|None|None|
|search_string|string|None|False|Partial or full literal string to search for. f.e. you could search for an instance ID, image ID, or resource name|None|resource_id|None|None|
  
Example input:

```
{
  "advanced_search": false,
  "badge_filter_operator": "AND",
  "badges": [
    {
      "key": "environment",
      "value": "production"
    }
  ],
  "empty_badges": false,
  "exclusion_badges": [
    {
      "key": "region",
      "value": "us-east-1"
    }
  ],
  "filters": [
    {
      "field_name": "account_id",
      "filter_type": "EXACT",
      "filter_value": "463792522299"
    }
  ],
  "limit": 3,
  "offset": 1,
  "order_by": "name ASC",
  "search_string": "resource_id"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|clouds|[]object|True|The list of clouds retrieved, including details such as account ID, badge count, cloud type, and other information|[{"account_id": "463792522299", "badge_count": 7, "cloud_access": "None", "cloud_organization_domain_name": "o-03nsxuwv", "cloud_organization_id": "o-03nsxuwv", "cloud_organization_nickname": "The Organization Formerly Known As Test", "cloud_type_id": "AWS", "creation_time": "2021-08-13 21:01:11", "disabled_resource_types": "None", "event_driven_harvest_role": "idle", "failed_resource_types": "None", "group_resource_id": "divvyorganizationservice:1", "id": 1, "is_platform_managed": False, "last_refreshed": "2025-06-05 08:15:14", "name": "AWS Marketplace", "resource_count": 33, "resource_id": "divvyorganizationservice:1", "role_arn": "OrganizationAccountReadRole", "scan_error": "None", "status": "ASSUME_ROLE_FAIL", "strategy_id": 1, "tenant_id": "None", "trailblazer_account_in_scope": "None", "trailblazer_cloudtrail_trails": []}]|
|total_count|integer|True|Total count of clouds retrieved|1|
  
Example output:

```
{
  "clouds": [
    {
      "account_id": "463792522299",
      "badge_count": 7,
      "cloud_access": "None",
      "cloud_organization_domain_name": "o-03nsxuwv",
      "cloud_organization_id": "o-03nsxuwv",
      "cloud_organization_nickname": "The Organization Formerly Known As Test",
      "cloud_type_id": "AWS",
      "creation_time": "2021-08-13 21:01:11",
      "disabled_resource_types": "None",
      "event_driven_harvest_role": "idle",
      "failed_resource_types": "None",
      "group_resource_id": "divvyorganizationservice:1",
      "id": 1,
      "is_platform_managed": false,
      "last_refreshed": "2025-06-05 08:15:14",
      "name": "AWS Marketplace",
      "resource_count": 33,
      "resource_id": "divvyorganizationservice:1",
      "role_arn": "OrganizationAccountReadRole",
      "scan_error": "None",
      "status": "ASSUME_ROLE_FAIL",
      "strategy_id": 1,
      "tenant_id": "None",
      "trailblazer_account_in_scope": "None",
      "trailblazer_cloudtrail_trails": []
    }
  ],
  "total_count": 1
}
```

#### List Resource Tags

This action is used to list resource tags based on provided resource ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|resourceId|string|None|True|ID of the resource|None|instance:123:example:i-1234567890:|None|None|
  
Example input:

```
{
  "resourceId": "instance:123:example:i-1234567890:"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|resourceTags|[]resourceTag|False|Resource tags for the provided ID|[{"key": "tag1", "value": "test_tag_1"}, {"key": "tag2", "value": "test_tag_2"}, {"key": "tag3", "value": "test_tag_3"}]|
  
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

#### Remove Exemption

This action is used to delete exemptions for provided IDs

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|exemptionIds|[]integer|None|True|List of exemption IDs to delete|None|[111, 222]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Switch Organization

This action is used to change the organization for which all future API requests will be made

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|organizationName|string|None|True|Name of the organization|None|Example Organization|None|None|
  
Example input:

```
{
  "organizationName": "Example Organization"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
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
  
**accountDetails**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account ID|string|None|False|ID of the cloud account|None|
|Cloud Type ID|string|None|False|ID of the cloud type|None|
|Joined Timestamp|string|None|False|When the account was joined|None|
|Name|string|None|False|Name of the account|None|
|Payer Account ID|string|None|False|ID of the payer account|None|
|Resource ID|string|None|False|Resource ID for the account|None|
|Status|string|None|False|Status of the account|None|
  
**exemption**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account|string|None|False|Name of the account|None|
|Account ID|integer|None|False|ID of the account|None|
|Approver|string|None|False|The exemption approver|None|
|Bot ID|string|None|False|ID of the bot|None|
|Bot Name|string|None|False|Name of the bot|None|
|Cloud Type ID|integer|None|False|ID of the cloud type|None|
|Create Date|string|None|False|When the exemption was created|None|
|Creator ID|integer|None|False|ID of the creator of the exemption|None|
|Creator Name|string|None|False|Name of the creator of the exemption|None|
|Enabled|boolean|None|False|Whether the exemption is enabled|None|
|Exemption ID|integer|None|False|ID of the exemption|None|
|Expiration Date|string|None|False|When the exemption expires|None|
|Insight ID|integer|None|False|ID of the Insight associated with the exemption|None|
|Insight Name|string|None|False|Name of the Insight associated with the exemption|None|
|Insight Source|string|None|False|Source for the Insight associated with the exemption|None|
|Notes|string|None|False|Notes|None|
|Organization ID|integer|None|False|ID of the organization|None|
|Provider ID|integer|None|False|ID of the provider|None|
|Resource ID|string|None|False|ID of the resource that was exempted|None|
|ResourceIds|[]string|None|False|List of resource IDs that have been exempted from the given Insight|None|
|Resource Name|string|None|False|Name of the resource|None|
|Resource Type|string|None|False|Type of the resource|None|
|Resource Type Label|string|None|False|Label of the resource type|None|
|Start Date|string|None|False|When the exemption starts|None|
  
**resourceDetails**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Dependencies|object|None|False|Dependencies for the provided resource ID|None|
|Details|object|None|False|Details for the provided resource ID|None|
|Related Resources|object|None|False|Related resources with the provided resource ID|None|
  
**resourceTag**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key|string|None|False|Key of the resource tag|None|
|Value|string|None|False|Value of the resource tag|None|
  
**resource**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account|string|None|False|Account of the resource|my-account-name|
|Account ID|string|None|False|Account ID of the resource|************|
|Cloud type ID|string|None|False|Cloud type ID of the resource|AWS|
|Name|string|None|False|Name of the resource|my-instance-name|
|Provider ID|string|None|False|Provider ID of the resource|*******************|
|Resource ID|string|None|False|Resource of the resource ID|instance:******:ap-northeast-1:*******************:|
|Resource Type|string|None|False|Resource type of the resource|instance|
  
**filters**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Field Name|string|None|False|Specifies the name of the output field used for filtering results|account_id|
|Filter List Value|array|None|False|Can be used instead of `filter_value` to filter multiple values|["AWS_GOV", "AWS_CHINA", "AWS"]|
|Filter Type|string|None|False|Specifies the type of filtering to apply to the selected field|NOT|
|Filter Value|string|None|False|Specifies the value to apply to the filter for the `field_name` field.|463792522299|
  
**badges**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key|string|None|False|Key of the Badge|environment|
|Value|string|None|False|Value of the Badge|production|


## Troubleshooting

* This plugin does not contain any troubleshooting information

# Version History

* 2.2.0 - Added 'list_clouds' action | Unit test added | SDK bump to 6.3.6
* 2.1.2 - Updated SDK to the latest version (v6.3.4) | Updated Documentation 
* 2.1.1 - Updated SDK to the latest version (v6.2.3) | Address vulnerabilities
* 2.1.0 - Updated SDK to the latest version | Adding a get resource id functionality
* 2.0.0 - Enable plugin to run in cloud | Remove actions using defective API endpoints
* 1.0.0 - Initial plugin | Add Get Account Details, Get Resource Details, List Resource Tags, Create Exemption, Remove Exemption, Detach Policy, Run Bot on Demand and Switch Organization actions

# Links

* [Rapid7 InsightCloudSec](https://github.com/rapid7/insightconnect-plugins/tree/master/plugins/rapid7_insightcloudsec)
* [Docs](https://docs.rapid7.com/insightcloudsec/api/v2/)

## References

* [Rapid7 InsightCloudSec](https://www.rapid7.com/products/insightcloudsec/)