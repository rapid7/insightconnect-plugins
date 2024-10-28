# Description

Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable. This plugin allows you to list accounts, zones, zone access rules and lists and create or delete access rules for specific zones.

# Key Features

* Get Accounts
* Get Zones
* Get Lists
* Create Zone Access Rule
* Delete Zone Access Rule
* Get Zone Access Rules

# Requirements

The following information is required for using this plugin:

* Cloudflare API token

The used API token must have the following permissions.

For all account:
* `Account Filter Lists:Read`
* `Account Firewall Access Rules:Read`

For all zones:
* `Firewall Services:Read`
* `Firewall Services:Edit`
* `Zone:Read`

# Supported Product Versions

* Cloudflare API v4 2023-02-10

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|apiToken|credential_secret_key|None|True|A Cloudflare API token with a specific scope and permissions|None|{"secretKey": "ABc123456789s-TeSt987654_3x4mpleTOkeN012"}|None|None|

Example input:

```
{
  "apiToken": {
    "secretKey": "ABc123456789s-TeSt987654_3x4mpleTOkeN012"
  }
}
```

## Technical Details

### Actions


#### Create Zone Access Rule

This action creates a new access rule for a zone.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|mode|string|block|True|The action to apply to a matched request|["block", "challenge", "whitelist", "JS challenge", "managed challenge"]|block|None|None|
|notes|string|None|False|An informative summary of the rule, typically used as a reminder or explanation|None|This rule is enabled because of an event that occurred on date X|None|None|
|target|string|None|True|The configuration target in which you can specify IPv4, IPv6, IP range, AS number or two-letter ISO-3166-1 alpha-2 country code|None|198.51.100.1|None|None|
|zoneId|string|None|True|ID of the zone for which you want to create an access rule|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "mode": "block",
  "notes": "This rule is enabled because of an event that occurred on date X",
  "target": "198.51.100.1",
  "zoneId": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|accessRule|accessRule|False|Information about the created access rule|{}|
  
Example output:

```
{
  "accessRule": {
    "id": "9de5069c5afe602b2ea0a04b66beb2c0",
    "paused": false,
    "modifiedOn": "2023-02-15T13:10:28.008463675Z",
    "allowedModes": [
      "whitelist",
      "block",
      "challenge",
      "js_challenge",
      "managed_challenge"
    ],
    "mode": "block",
    "notes": "This rule is enabled because of an event that occurred on date X",
    "configuration": {
      "target": "ip",
      "value": "198.51.100.1"
    },
    "scope": {
      "id": "9de5069c5afe602b2ea0a04b66beb2c0",
      "name": "example.com",
      "type": "zone"
    },
    "createdOn": "2023-02-15T13:10:28.008463675Z"
  }
}
```

#### Delete Zone Access Rule

This action is used to delete an IP access rule defined at the zone level.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ruleId|string|None|True|ID of the access rule you want to delete|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|zoneId|string|None|True|ID of the zone for which you want to delete an access rule|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "ruleId": "9de5069c5afe602b2ea0a04b66beb2c0",
  "zoneId": "9de5069c5afe602b2ea0a04b66beb2c0"
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

#### Get Accounts

This action is used to list all accounts you have ownership or verified access to.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|direction|string|desc|False|Direction to order results|["desc", "asc"]|desc|None|None|
|name|string|None|False|Name of the account|None|Example Account|None|None|
|page|integer|None|False|Page number of paginated results|None|1|None|None|
|perPage|integer|None|False|Maximum number of results per page|None|10|None|None|
  
Example input:

```
{
  "direction": "desc",
  "name": "Example Account",
  "page": 1,
  "perPage": 10
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|accounts|[]account|False|List of accounts|[]|
  
Example output:

```
{
  "accounts": [
    {
      "id": "9de5069c5afe602b2ea0a04b66beb2c0",
      "name": "Example Account",
      "type": "standard",
      "settings": {
        "enforceTwofactor": false,
        "useAccountCustomNsByDefault": false
      },
      "legacyFlags": {
        "enterpriseZoneQuota": {
          "maximum": 0,
          "current": 0,
          "available": 0
        }
      },
      "createdOn": "2023-01-05T22:57:42.821042Z"
    }
  ]
}
```

#### Get Lists

This action is used to fetch all lists in the account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|accountId|string|None|True|Identifier of the account|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "accountId": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|lists|[]list|False|Results containing all lists in the account|[]|
  
Example output:

```
{
  "lists": [
    {
      "id": "9de5069c5afe602b2ea0a04b66beb2c0",
      "name": "ip_list",
      "description": "Test ip list",
      "kind": "ip",
      "numItems": 1,
      "numReferencingFilters": 0,
      "createdOn": "2023-02-06T10:22:58Z",
      "modifiedOn": "2023-02-06T10:23:34Z"
    }
  ]
}
```

#### Get Zone Access Rules

This action is used to fetch IP Access rules of a zone. You can filter the results using several optional parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|configurationTarget|string|all|False|The target to search in existing rules|["all", "IP address", "IP range", "ASN", "country"]|IP address|None|None|
|configurationValue|string|None|False|The target value to search for in existing rules|None|198.51.100.1|None|None|
|direction|string|desc|False|Direction to order results|["desc", "asc"]|desc|None|None|
|match|string|all|False|Whether to match all search requirements or at least one (any)|["all", "any"]|all|None|None|
|mode|string|all|False|The action that was applied to a matched request|["all", "block", "challenge", "whitelist", "JS challenge", "managed challenge"]|all|None|None|
|notes|string|None|False|The string to search for in the notes of existing IP Access rules|None|My notes|None|None|
|order|string|mode|False|Field to order zones by|["configuration target", "configuration value", "mode"]|mode|None|None|
|page|integer|None|False|Page number of paginated results|None|1|None|None|
|perPage|integer|None|False|Maximum number of results per page|None|10|None|None|
|zoneId|string|None|True|The ID of the zone for which you want to list the access rules|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "configurationTarget": "IP address",
  "configurationValue": "198.51.100.1",
  "direction": "desc",
  "match": "all",
  "mode": "all",
  "notes": "My notes",
  "order": "mode",
  "page": 1,
  "perPage": 10,
  "zoneId": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|accessRules|[]accessRule|False|List of zone access rules|[]|
  
Example output:

```
{
  "accessRules": [
    {
      "id": "9de5069c5afe602b2ea0a04b66beb2c0",
      "paused": false,
      "modifiedOn": "2023-02-15T13:10:28.008463675Z",
      "allowedModes": [
        "whitelist",
        "block",
        "challenge",
        "js_challenge",
        "managed_challenge"
      ],
      "mode": "block",
      "notes": "My notes",
      "configuration": {
        "target": "ip",
        "value": "198.51.100.1"
      },
      "scope": {
        "id": "9de5069c5afe602b2ea0a04b66beb2c0",
        "name": "example.com",
        "type": "zone"
      },
      "createdOn": "2023-02-15T13:10:28.008463675Z"
    }
  ]
}
```

#### Get Zones

This action is used to list your zones using different filters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|accountId|string|None|False|Identifier of the account|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|accountName|string|None|False|Name of the account|None|Example Account|None|None|
|direction|string|desc|False|Direction to order results|["desc", "asc"]|desc|None|None|
|match|string|all|False|Whether to match all search requirements or at least one (any)|["all", "any"]|all|None|None|
|name|string|None|False|Name of the domain|None|example.com|None|None|
|order|string|name|False|Field to order zones by|["account ID", "account name", "name", "status"]|name|None|None|
|page|integer|None|False|Page number of paginated results|None|1|None|None|
|perPage|integer|None|False|Maximum number of results per page|None|10|None|None|
|status|string|all|False|Status of the zone|["all", "active", "pending", "initializing", "moved", "deleted", "deactivated"]|all|None|None|
  
Example input:

```
{
  "accountId": "9de5069c5afe602b2ea0a04b66beb2c0",
  "accountName": "Example Account",
  "direction": "desc",
  "match": "all",
  "name": "example.com",
  "order": "name",
  "page": 1,
  "perPage": 10,
  "status": "all"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|zones|[]zone|False|List of zones for given filters|[]|
  
Example output:

```
{
  "zones": [
    {
      "id": "9de5069c5afe602b2ea0a04b66beb2c0",
      "name": "example.com",
      "status": "pending",
      "paused": false,
      "type": "full",
      "developmentMode": 0,
      "nameServers": [
        "example.com",
        "example.com"
      ],
      "originalNameServers": [
        "example.com",
        "example.com"
      ],
      "originalRegistrar": "test (id: 1111)",
      "modifiedOn": "2023-02-02T14:34:09.478563Z",
      "createdOn": "2023-02-02T14:33:55.854402Z",
      "meta": {
        "step": 2,
        "customCertificateQuota": 0,
        "pageRuleQuota": 3,
        "phishingDetected": false,
        "multipleRailgunsAllowed": false
      },
      "owner": {
        "type": "user"
      },
      "account": {
        "id": "9de5069c5afe602b2ea0a04b66beb2c0",
        "name": "Example Account"
      },
      "tenant": {},
      "tenantUnit": {},
      "permissions": [
        "#access:edit",
        "#access:read",
        "#analytics:read",
        "#app:edit",
        "#auditlogs:read",
        "#billing:edit",
        "#billing:read",
        "#blocks:edit",
        "#blocks:read",
        "#cache_purge:edit",
        "#dash_sso:edit",
        "#dash_sso:read",
        "#dns_records:edit",
        "#dns_records:read",
        "#fbm_acc:edit",
        "#fbm:edit",
        "#fbm:read",
        "#healthchecks:edit",
        "#healthchecks:read",
        "#http_applications:edit",
        "#http_applications:read",
        "#image:edit",
        "#image:read",
        "#lb:edit",
        "#lb:read",
        "#legal:edit",
        "#legal:read",
        "#logs:edit",
        "#logs:read",
        "#magic:edit",
        "#magic:read",
        "#member:edit",
        "#member:read",
        "#organization:edit",
        "#organization:read",
        "#ssl:edit",
        "#ssl:read",
        "#stream:edit",
        "#stream:read",
        "#subscription:edit",
        "#subscription:read",
        "#teams:edit",
        "#teams:pii",
        "#teams:read",
        "#teams:report",
        "#waf:edit",
        "#waf:read",
        "#waitingroom:edit",
        "#waitingroom:read",
        "#webhooks:edit",
        "#webhooks:read",
        "#worker:edit",
        "#worker:read",
        "#zaraz:edit",
        "#zaraz:publish",
        "#zaraz:read",
        "#zone:edit",
        "#zone:read",
        "#zone_settings:edit",
        "#zone_settings:read",
        "#zone_versioning:edit",
        "#zone_versioning:read"
      ],
      "plan": {
        "id": "123456789",
        "name": "Free Website",
        "price": 0,
        "currency": "USD",
        "isSubscribed": false,
        "canSubscribe": false,
        "legacyId": "free",
        "legacyDiscount": false,
        "externallyManaged": false
      }
    }
  ]
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
|Custom Certificate Quota|integer|None|False|Custom certificate quota|None|
|Multiple Railguns Allowed|boolean|None|False|Multiple railguns allowed|None|
|Page Rule Quota|integer|None|False|Page rule quota|None|
|Phishing Detected|boolean|None|False|Phishing detected|None|
|Step|integer|None|False|Step|None|
  
**owner**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|False|Email|None|
|ID|string|None|False|ID|None|
|Type|string|None|False|Type|None|
  
**plan**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Can Subscribe|boolean|None|False|Can subscribe|None|
|Currency|string|None|False|Currency|None|
|Externally Managed|boolean|None|False|Externally managed|None|
|Frequency|string|None|False|Frequency|None|
|ID|string|None|False|ID|None|
|Is Subscribed|boolean|None|False|Is subscribed|None|
|Legacy Discount|boolean|None|False|Legacy discount|None|
|Legacy ID|string|None|False|Legacy ID|None|
|Name|string|None|False|Name|None|
|Price|integer|None|False|Price|None|
  
**tenant**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Identifier|None|
|Name|string|None|False|Name|None|
  
**tenantUnit**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Identifier|None|
  
**scope**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID|None|
|Name|string|None|False|Name|None|
|Type|string|None|False|Type|None|
  
**configuration**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Target|string|None|False|Target|None|
|Value|string|None|False|Value|None|
  
**zoneQuota**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Current|integer|None|False|Current|None|
|Maximum|integer|None|False|Maximum|None|
|Available|integer|None|False|Available|None|
  
**legacyFlags**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Enterprise Zone Quota|zoneQuota|None|False|Enterprise Zone Quota|None|
  
**settings**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|API Access Enabled|boolean|None|False|API access enabled|None|
|Enforce Two Factor Authentication|boolean|None|False|Enforce two factor authentication|None|
  
**account**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created On|string|None|False|Created on|None|
|Account ID|string|None|False|Identifier of the account|None|
|Legacy Flags|legacyFlags|None|False|Legacy Flags|None|
|Account Name|string|None|False|Name of the account|None|
|Settings|settings|None|False|Account settings|None|
|Account Type|string|None|False|Type of the account|None|
  
**accessRule**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Allowed Modes|[]string|None|False|Allowed modes|None|
|Configuration|configuration|None|False|Configuration|None|
|Created On|string|None|False|Created on|None|
|Access Rule ID|string|None|False|Identifier of the access rule|None|
|Mode|string|None|False|Mode|None|
|Modified On|string|None|False|Modified on|None|
|Paused|boolean|None|False|Paused|None|
|Scope|scope|None|False|Scope|None|
  
**list**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created On|string|None|False|Created on|None|
|Description|string|None|False|Description|None|
|List ID|string|None|False|Identifier of the list|None|
|Kind|string|None|False|Kind|None|
|Modified On|string|None|False|Modified on|None|
|List Name|string|None|False|Name of the list|None|
|Num Items|integer|None|False|Number of items|None|
|Num Referencing Filters|integer|None|False|Number of referencing filters|None|
  
**zone**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account|tenant|None|False|Account|None|
|Activated On|string|None|False|Activated on|None|
|Created On|string|None|False|Created on|None|
|Development Mode|integer|None|False|Development mode|None|
|Zone ID|string|None|False|Identifier of the zone|None|
|Meta|meta|None|False|Meta|None|
|Modified On|string|None|False|Modified on|None|
|Zone Name|string|None|False|Name of the zone|None|
|Name Servers|[]string|None|False|Name servers|None|
|Original DNS Host|string|None|False|Original DNS host|None|
|Original Name Servers|[]string|None|False|Original name servers|None|
|Original Registrar|string|None|False|Original registrar|None|
|Owner|owner|None|False|Owner|None|
|Paused|boolean|None|False|Paused|None|
|Permissions|[]string|None|False|Permissions|None|
|Plan|plan|None|False|Plan|None|
|Zone Status|string|None|False|Status of the zone|None|
|Tenant|tenant|None|False|Tenant|None|
|Tenant Unit|tenantUnit|None|False|Tenant unit|None|
|Type|string|None|False|Type of the zone|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.1 - Bumping requirements.txt | SDK bump to 6.1.4
* 1.0.0 - Initial plugin | Add Get Accounts, Get Zones, Get Lists, Get Zone Access Rules, Create Zone Access Rule and Delete Zone Access Rule actions

# Links

* [Cloudflare](https://www.cloudflare.com)

## References

* [Cloudflare](https://www.cloudflare.com)