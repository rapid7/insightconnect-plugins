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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|apiToken|credential_secret_key|None|True|A Cloudflare API token with a specific scope and permissions|None|{"secretKey": "ABc123456789s-TeSt987654_3x4mpleTOkeN012"}|

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

#### Get Zone Access Rules

This action is used to fetch IP Access rules of a zone. You can filter the results using several optional parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|configurationTarget|string|all|False|The target to search in existing rules|['all', 'IP address', 'IP range', 'ASN', 'country']|IP address|
|configurationValue|string|None|False|The target value to search for in existing rules|None|198.51.100.1|
|direction|string|desc|False|Direction to order results|['desc', 'asc']|desc|
|match|string|all|False|Whether to match all search requirements or at least one (any)|['all', 'any']|all|
|mode|string|all|False|The action that was applied to a matched request|['all', 'block', 'challenge', 'whitelist', 'JS challenge', 'managed challenge']|all|
|notes|string|None|False|The string to search for in the notes of existing IP Access rules|None|My notes|
|order|string|mode|False|Field to order zones by|['configuration target', 'configuration value', 'mode']|mode|
|page|integer|None|False|Page number of paginated results|None|1|
|perPage|integer|None|False|Maximum number of results per page|None|10|
|zoneId|string|None|True|The ID of the zone for which you want to list the access rules|None|9de5069c5afe602b2ea0a04b66beb2c0|

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
|----|----|--------|-----------|-------|
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

#### Delete Zone Access Rule

This action is used to delete an IP access rule defined at the zone level.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ruleId|string|None|True|ID of the access rule you want to delete|None|9de5069c5afe602b2ea0a04b66beb2c0|
|zoneId|string|None|True|ID of the zone for which you want to delete an access rule|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "ruleId": "9de5069c5afe602b2ea0a04b66beb2c0",
  "zoneId": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|True|

Example output:

```
{
  "success": true
}
```

#### Create Zone Access Rule

This action creates a new access rule for a zone.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|mode|string|block|True|The action to apply to a matched request|['block', 'challenge', 'whitelist', 'JS challenge', 'managed challenge']|block|
|notes|string|None|False|An informative summary of the rule, typically used as a reminder or explanation|None|This rule is enabled because of an event that occurred on date X|
|target|string|None|True|The configuration target in which you can specify IPv4, IPv6, IP range, AS number or two-letter ISO-3166-1 alpha-2 country code|None|198.51.100.1|
|zoneId|string|None|True|ID of the zone for which you want to create an access rule|None|9de5069c5afe602b2ea0a04b66beb2c0|

More information about the configuration target can be found [here](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/).

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
|----|----|--------|-----------|-------|
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

#### Get Accounts

This action is used to list all accounts you have ownership or verified access to.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|desc|False|Direction to order results|['desc', 'asc']|desc|
|name|string|None|False|Name of the account|None|Example Account|
|page|integer|None|False|Page number of paginated results|None|1|
|perPage|integer|None|False|Maximum number of results per page|None|10|

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
|----|----|--------|-----------|-------|
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|accountId|string|None|True|Identifier of the account|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "accountId": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
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

#### Get Zones

This action is used to list your zones using different filters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|accountId|string|None|False|Identifier of the account|None|9de5069c5afe602b2ea0a04b66beb2c0|
|accountName|string|None|False|Name of the account|None|Example Account|
|direction|string|desc|False|Direction to order results|['desc', 'asc']|desc|
|match|string|all|False|Whether to match all search requirements or at least one (any)|['all', 'any']|all|
|name|string|None|False|Name of the domain|None|example.com|
|order|string|name|False|Field to order zones by|['account ID', 'account name', 'name', 'status']|name|
|page|integer|None|False|Page number of paginated results|None|1|
|perPage|integer|None|False|Maximum number of results per page|None|10|
|status|string|all|False|Status of the zone|['all', 'active', 'pending', 'initializing', 'moved', 'deleted', 'deactivated']|all|

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
|----|----|--------|-----------|-------|
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

_This plugin does not contain any triggers._

### Custom Output Types

#### accessRule

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Allowed Modes|[]string|False|Allowed modes|
|Configuration|configuration|False|Configuration|
|Created On|string|False|Created on|
|Access Rule ID|string|False|Identifier of the access rule|
|Mode|string|False|Mode|
|Modified On|string|False|Modified on|
|Paused|boolean|False|Paused|
|Scope|scope|False|Scope|

#### account

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created On|string|False|Created on|
|Account ID|string|False|Identifier of the account|
|Legacy Flags|legacyFlags|False|Legacy Flags|
|Account Name|string|False|Name of the account|
|Settings|settings|False|Account settings|
|Account Type|string|False|Type of the account|

#### configuration

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Target|string|False|Target|
|Value|string|False|Value|

#### legacyFlags

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Enterprise Zone Quota|zoneQuota|False|Enterprise Zone Quota|

#### list

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created On|string|False|Created on|
|Description|string|False|Description|
|List ID|string|False|Identifier of the list|
|Kind|string|False|Kind|
|Modified On|string|False|Modified on|
|List Name|string|False|Name of the list|
|Num Items|integer|False|Number of items|
|Num Referencing Filters|integer|False|Number of referencing filters|

#### meta

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Custom Certificate Quota|integer|False|Custom certificate quota|
|Multiple Railguns Allowed|boolean|False|Multiple railguns allowed|
|Page Rule Quota|integer|False|Page rule quota|
|Phishing Detected|boolean|False|Phishing detected|
|Step|integer|False|Step|

#### owner

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|Email|
|ID|string|False|ID|
|Type|string|False|Type|

#### plan

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Can Subscribe|boolean|False|Can subscribe|
|Currency|string|False|Currency|
|Externally Managed|boolean|False|Externally managed|
|Frequency|string|False|Frequency|
|ID|string|False|ID|
|Is Subscribed|boolean|False|Is subscribed|
|Legacy Discount|boolean|False|Legacy discount|
|Legacy ID|string|False|Legacy ID|
|Name|string|False|Name|
|Price|integer|False|Price|

#### scope

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### settings

|Name|Type|Required|Description|
|----|----|--------|-----------|
|API Access Enabled|boolean|False|API access enabled|
|Enforce Two Factor Authentication|boolean|False|Enforce two factor authentication|

#### tenant

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Identifier|
|Name|string|False|Name|

#### tenantUnit

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Identifier|

#### zone

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account|tenant|False|Account|
|Activated On|string|False|Activated on|
|Created On|string|False|Created on|
|Development Mode|integer|False|Development mode|
|Zone ID|string|False|Identifier of the zone|
|Meta|meta|False|Meta|
|Modified On|string|False|Modified on|
|Zone Name|string|False|Name of the zone|
|Name Servers|[]string|False|Name servers|
|Original DNS Host|string|False|Original DNS host|
|Original Name Servers|[]string|False|Original name servers|
|Original Registrar|string|False|Original registrar|
|Owner|owner|False|Owner|
|Paused|boolean|False|Paused|
|Permissions|[]string|False|Permissions|
|Plan|plan|False|Plan|
|Zone Status|string|False|Status of the zone|
|Tenant|tenant|False|Tenant|
|Tenant Unit|tenantUnit|False|Tenant unit|
|Type|string|False|Type of the zone|

#### zoneQuota

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Current|integer|False|Current|
|Maximum|integer|False|Maximum|
|Available|integer|False|Available|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin | Add Get Accounts, Get Zones, Get Lists, Get Zone Access Rules, Create Zone Access Rule and Delete Zone Access Rule actions

# Links

* [Cloudflare](https://www.cloudflare.com)

## References

* [Cloudflare](https://www.cloudflare.com)

